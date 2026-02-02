# eigensolver - 设置本征求解器

## 概述

`eigensolver` 命令用于配置 Lumerical MODE 产品中的本征求解器（eigenmode solver）。本征求解器是计算波导、谐振腔等结构中电磁模式的核心工具，用于分析模式的传播常数、场分布、有效折射率等关键参数。

### 主要功能
- 设置本征求解器的求解参数（频率范围、模式数量、边界条件等）
- 配置求解器算法选项（迭代方法、收敛容差、最大迭代次数）
- 控制求解精度和性能设置
- 指定输出选项和结果存储

### 典型应用场景
1. **波导模式分析** - 计算单模和多模波导中的传播模式
2. **谐振腔模式计算** - 分析光学谐振腔的本征频率和品质因子
3. **光子晶体带隙分析** - 计算周期性结构中的能带分布
4. **耦合器模式分析** - 分析定向耦合器中的超模
5. **有效折射率计算** - 确定模式的等效折射率

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
eigensolver("solver name", "parameter", value);

# 设置多个参数
eigensolver("solver name", "parameter1", value1, "parameter2", value2, ...);
```

### Python API (Lumapi)
```python
# 基本调用
session.eigensolver("solver name", "parameter", value)

# 设置多个参数
session.eigensolver("solver name", "parameter1", value1, "parameter2", value2, ...)

# 使用字典配置参数
params = {
    "frequency": 193.1e12,
    "number of trial modes": 10,
    "search": "max index"
}
for param, value in params.items():
    session.eigensolver("solver name", param, value)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `"solver name"` | 字符串 | 是 | 无 | 要配置的本征求解器对象名称 |
| `"parameter"` | 字符串 | 是 | 无 | 要设置的参数名称（见下表） |
| `value` | 多种 | 是 | 无 | 参数值，类型取决于具体参数 |

## 配置属性

本征求解器支持通过 `set` 命令或 `eigensolver` 命令配置以下属性：

| 属性名称 | 类型 | 默认值 | 描述 | 适用范围 |
|----------|------|--------|------|----------|
| `"frequency"` | 数值 | 193.1e12 | 求解频率（Hz） | 所有模式求解 |
| `"wavelength"` | 数值 | 1.55e-6 | 求解波长（m），与频率互斥 | 所有模式求解 |
| `"number of trial modes"` | 整数 | 10 | 尝试计算的模式数量 | 所有模式求解 |
| `"number of modes"` | 整数 | 1 | 实际返回的模式数量 | 所有模式求解 |
| `"search"` | 字符串 | `"max index"` | 搜索模式的方法：<br>`"max index"` - 最高有效折射率<br>`"near n"` - 接近指定折射率<br>`"max confinement"` - 最大限制因子 | 所有模式求解 |
| `"target n"` | 数值 | 1.0 | 目标有效折射率（search="near n"时使用） | 特定搜索模式 |
| `"boundary conditions"` | 字符串 | `"metal"` | 边界条件类型：<br>`"metal"` - 完美电导体<br>`"periodic"` - 周期性边界<br>`"PMC"` - 完美磁导体<br>`"PEC"` - 完美电导体 | 所有模式求解 |
| `"sweep type"` | 字符串 | `"single frequency"` | 扫描类型：<br>`"single frequency"` - 单频率点<br>`"broadband"` - 宽带扫描<br>`"wavelength sweep"` - 波长扫描 | 扫描求解 |
| `"sweep start wavelength"` | 数值 | 1.5e-6 | 扫描起始波长（m） | 波长扫描 |
| `"sweep stop wavelength"` | 数值 | 1.6e-6 | 扫描结束波长（m） | 波长扫描 |
| `"sweep points"` | 整数 | 11 | 扫描点数 | 扫描求解 |
| `"mesh refinement"` | 字符串 | `"conformal variant 0"` | 网格细化方法 | 高级求解 |
| `"convergence"` | 数值 | 1e-8 | 收敛容差 | 迭代求解 |
| `"max iterations"` | 整数 | 100 | 最大迭代次数 | 迭代求解 |
| `"solver type"` | 字符串 | `"2D"` | 求解器类型：`"2D"`, `"3D"` | 维度选择 |
| `"polarization"` | 字符串 | `"TE"` | 偏振类型：`"TE"`, `"TM"`, `"full vector"` | 2D求解器 |
| `"store all solutions"` | 布尔 | 0 | 是否存储所有求解结果 | 结果控制 |
| `"group index calculation"` | 布尔 | 0 | 是否计算群折射率 | 高级分析 |
| `"bent waveguide"` | 布尔 | 0 | 是否启用弯曲波导模式求解 | 特殊几何 |

## 使用示例

### 示例 1：基本波导模式分析
```python
import lumapi

# 创建 MODE 会话
mode = lumapi.MODE()

# 添加硅波导结构
mode.addrect()
mode.set("name", "waveguide")
mode.set("material", "Si (Silicon) - Palik")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 220e-9)
mode.set("y span", 500e-9)
mode.set("z", 0)

# 添加 FDE 求解器
mode.addfde()
mode.set("solver type", "2D")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 2e-6)

# 配置本征求解器
mode.eigensolver("FDE::data::model", "frequency", 193.1e12)  # 1550nm
mode.eigensolver("FDE::data::model", "number of trial modes", 10)
mode.eigensolver("FDE::data::model", "number of modes", 3)
mode.eigensolver("FDE::data::model", "search", "max index")

# 运行求解
mode.findmodes()

# 获取结果
neff = mode.getresult("FDE::data::model", "neff")
print(f"有效折射率: {neff}")
```

### 示例 2：光子晶体带隙分析
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 创建光子晶体结构
mode.addcircle()
mode.set("name", "hole")
mode.set("material", "Air")
mode.set("radius", 100e-9)
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 220e-9)

# 创建周期性结构
mode.addfde()
mode.set("solver type", "2D")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 2e-6)

# 设置周期性边界条件
mode.eigensolver("FDE::data::model", "boundary conditions", "periodic")
mode.eigensolver("FDE::data::model", "frequency", 300e12)  # 1μm
mode.eigensolver("FDE::data::model", "number of trial modes", 20)

# 扫描波矢以计算能带
k_points = np.linspace(0, np.pi/500e-9, 20)  # 第一布里渊区
frequencies = []

for k in k_points:
    mode.setnamed("FDE::data::model", "k", k)
    mode.findmodes()
    freq = mode.getresult("FDE::data::model", "frequencies")
    frequencies.append(freq[0])  # 基模频率
    
    # 可选：存储所有模式频率
    # all_freqs = mode.getresult("FDE::data::model", "frequencies")
    # frequencies.append(all_freqs)

print(f"带隙频率范围: {min(frequencies):.2e} - {max(frequencies):.2e} Hz")
```

### 示例 3：宽带模式分析
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 添加 SOI 波导
mode.addrect()
mode.set("name", "SOI waveguide")
mode.set("material", "Si (Silicon) - Palik")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 220e-9)  # 厚度
mode.set("y span", 500e-9)  # 宽度

# 添加 FDE 求解器
mode.addfde()
mode.set("solver type", "2D")

# 配置宽带本征求解器
mode.eigensolver("FDE::data::model", "sweep type", "wavelength sweep")
mode.eigensolver("FDE::data::model", "sweep start wavelength", 1.5e-6)
mode.eigensolver("FDE::data::model", "sweep stop wavelength", 1.6e-6)
mode.eigensolver("FDE::data::model", "sweep points", 21)
mode.eigensolver("FDE::data::model", "number of trial modes", 5)
mode.eigensolver("FDE::data::model", "number of modes", 2)

# 运行宽带求解
mode.findmodes()

# 获取波长扫描结果
wavelengths = mode.getresult("FDE::data::model", "sweep wavelength")
neff_sweep = mode.getresult("FDE::data::model", "neff")

print(f"波长范围: {wavelengths[0]*1e9:.1f} - {wavelengths[-1]*1e9:.1f} nm")
print(f"基模有效折射率变化: {neff_sweep[0,0]:.4f} - {neff_sweep[0,-1]:.4f}")
```

### 示例 4：高精度谐振腔模式分析
```python
import lumapi

mode = lumapi.MODE()

# 创建微环谐振腔结构
mode.addring()
mode.set("name", "microring")
mode.set("material", "Si (Silicon) - Palik")
mode.set("inner radius", 5e-6)
mode.set("outer radius", 5.5e-6)
mode.set("z span", 220e-9)

# 添加 3D FDE 求解器
mode.addfde()
mode.set("solver type", "3D")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("x span", 12e-6)
mode.set("y span", 12e-6)
mode.set("z span", 1e-6)

# 配置高精度本征求解器
mode.eigensolver("FDE::data::model", "frequency", 193.1e12)
mode.eigensolver("FDE::data::model", "number of trial modes", 15)
mode.eigensolver("FDE::data::model", "search", "max confinement")
mode.eigensolver("FDE::data::model", "convergence", 1e-10)  # 高精度收敛
mode.eigensolver("FDE::data::model", "max iterations", 200)
mode.eigensolver("FDE::data::model", "mesh refinement", "conformal variant 1")
mode.eigensolver("FDE::data::model", "store all solutions", True)

# 运行求解
mode.findmodes()

# 获取谐振腔模式参数
neff = mode.getresult("FDE::data::model", "neff")
Q_factor = mode.getresult("FDE::data::model", "Q")
loss = mode.getresult("FDE::data::model", "loss")

print(f"谐振模式有效折射率: {neff[0]:.6f}")
print(f"品质因子: {Q_factor[0]:.2e}")
print(f"损耗: {loss[0]:.2e} dB/m")
```

### 示例 5：弯曲波导模式分析
```python
import lumapi

mode = lumapi.MODE()

# 添加弯曲波导结构（已在布局中定义）
# 假设已有弯曲波导几何

# 添加 FDE 求解器
mode.addfde()
mode.set("solver type", "2D")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z span", 2e-6)

# 配置弯曲波导本征求解器
mode.eigensolver("FDE::data::model", "frequency", 193.1e12)
mode.eigensolver("FDE::data::model", "bent waveguide", True)
mode.eigensolver("FDE::data::model", "bent waveguide radius", 10e-6)  # 弯曲半径
mode.eigensolver("FDE::data::model", "number of trial modes", 8)
mode.eigensolver("FDE::data::model", "search", "near n")
mode.eigensolver("FDE::data::model", "target n", 2.5)  # 目标有效折射率

# 设置弯曲波导特定参数
mode.setnamed("FDE::data::model", "bent waveguide shift", 0.1)  # 偏移参数

# 运行求解
mode.findmodes()

# 获取弯曲模式结果
neff_bent = mode.getresult("FDE::data::model", "neff")
bent_loss = mode.getresult("FDE::data::model", "bent loss")  # 弯曲损耗

print(f"弯曲波导模式有效折射率: {neff_bent[0]:.6f}")
print(f"弯曲损耗: {bent_loss[0]:.2f} dB/90°")
```

## 注意事项

### 1. 求解器选择
- **2D 求解器**：适用于平面波导结构，计算速度快，内存需求小
- **3D 求解器**：适用于三维结构，计算资源需求大，但精度更高
- 选择依据：结构对称性、精度要求和计算资源

### 2. 收敛性问题
- 复杂结构或高折射率对比度可能导致收敛困难
- 可尝试调整 `"convergence"`（放宽容差）或 `"max iterations"`（增加迭代次数）
- 使用 `"search"` 参数的不同选项可能改善收敛性

### 3. 模式数量设置
- `"number of trial modes"` 应大于 `"number of modes"`，确保找到足够数量的有效模式
- 对于泄漏模式或辐射模式，可能需要计算更多模式
- 宽带扫描时，模式数量应在整个频带内保持一致

### 4. 边界条件影响
- **金属边界**：模拟完美电导体，适用于金属包层结构
- **周期性边界**：用于光子晶体和周期性结构分析
- **PML 边界**：通过添加 PML 层模拟开放边界（需额外设置）

### 5. 内存和性能
- 3D 求解器需要大量内存，建议对大型结构使用粗网格或对称性简化
- 宽带扫描会显著增加计算时间，可考虑使用并行计算或减少扫描点数
- `"mesh refinement"` 设置影响精度和计算时间，需权衡选择

### 6. 结果验证
- 始终检查模式场分布的合理性
- 验证模式正交性和功率归一化
- 对比不同网格密度的结果以确保收敛

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 不支持 | 使用 `findmodes` 命令进行模式分析 |
| **MODE Solutions** | 完全支持 | 主要应用领域 |
| **DEVICE** | 不支持 | 专注于电学-热学仿真 |
| **INTERCONNECT** | 不支持 | 使用 `addmode` 导入模式数据 |

## 相关命令

- [`findmodes`](./findmodes.md) - 执行本征模式求解
- [`addfde`](./addfde.md) - 添加 FDE 求解器
- [`getresult`](./getresult.md) - 获取求解结果
- [`set`](./set.md) - 设置对象属性（替代方法）
- [`addmode`](./addmode.md) - 添加模式源（FDTD 中导入模式）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2025-01-31 | 初始版本，基于 Lumerical 2023R2 文档 |
| 1.1 | 2025-02-15 | 增加弯曲波导配置示例和注意事项 |

## 故障排除

### 常见问题
1. **求解不收敛**：
   - 检查网格密度是否足够
   - 尝试不同的 `"search"` 方法
   - 增加 `"max iterations"` 或放宽 `"convergence"`

2. **模式数量不足**：
   - 增加 `"number of trial modes"`
   - 调整 `"search"` 参数的目标值

3. **内存不足**：
   - 减小求解区域尺寸
   - 使用 2D 求解器替代 3D
   - 增加系统内存或使用计算集群

4. **结果异常**：
   - 验证边界条件设置
   - 检查材料属性是否正确
   - 确认频率/波长单位转换

### 调试建议
- 使用 `get("FDE::data::model")` 查看当前求解器设置
- 保存中间结果进行逐步验证
- 对比简单结构的解析解或已知结果

---

*文档版本：1.0 | 最后更新：2025-01-31*