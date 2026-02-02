# emeanalysis - EME 分析设置

## 概述

`emeanalysis` 命令用于配置 Lumerical MODE 产品中的 EME（Eigenmode Expansion，本征模展开）分析参数。EME 方法是一种频域仿真技术，特别适用于分析长距离波导结构、耦合器和光子集成电路中的光传播问题。

### 主要功能
- 设置 EME 求解器的基本参数（波长、模式数量、传播方向等）
- 配置 EME 算法的数值选项（收敛容差、最大模式数等）
- 控制 EME 分析的计算精度和性能
- 指定 EME 结果的输出选项和存储格式

### EME 方法特点
1. **高效处理长结构** - 特别适合毫米级甚至厘米级波导结构
2. **频域方法** - 直接计算频域响应，避免时域方法的长时间仿真
3. **模式基展开** - 将场展开为本征模的线性组合
4. **S 矩阵方法** - 使用散射矩阵连接不同截面

### 典型应用场景
1. **长距离波导传播** - 分析光在长波导中的传输和损耗
2. **定向耦合器** - 计算耦合长度和耦合效率
3. **多模干涉器** - 分析 MMI 耦合器的性能
4. **波导弯曲** - 计算弯曲波导的辐射损耗
5. **光子晶体波导** - 分析周期性结构的传输特性

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
emeanalysis("analysis name", "parameter", value);

# 设置多个参数
emeanalysis("analysis name", "parameter1", value1, "parameter2", value2, ...);
```

### Python API (Lumapi)
```python
# 基本调用
session.emeanalysis("analysis name", "parameter", value)

# 设置多个参数
session.emeanalysis("analysis name", "parameter1", value1, "parameter2", value2, ...)

# 使用字典配置参数
params = {
    "wavelength": 1.55e-6,
    "number of modes": 10,
    "propagation direction": "forward"
}
for param, value in params.items():
    session.emeanalysis("analysis name", param, value)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `"analysis name"` | 字符串 | 是 | 无 | 要配置的 EME 分析对象名称 |
| `"parameter"` | 字符串 | 是 | 无 | 要设置的参数名称（见下表） |
| `value` | 多种 | 是 | 无 | 参数值，类型取决于具体参数 |

## 配置属性

EME 分析支持通过 `set` 命令或 `emeanalysis` 命令配置以下属性：

| 属性名称 | 类型 | 默认值 | 描述 | 适用范围 |
|----------|------|--------|------|----------|
| `"wavelength"` | 数值 | 1.55e-6 | 分析波长（m） | 所有 EME 分析 |
| `"wavelength span"` | 数值 | 0 | 波长扫描范围 | 宽带分析 |
| `"frequency"` | 数值 | 193.1e12 | 分析频率（Hz） | 频率指定分析 |
| `"number of modes"` | 整数 | 10 | 使用的模式数量 | 模式展开 |
| `"propagation direction"` | 字符串 | `"both"` | 传播方向：<br>`"forward"` - 前向<br>`"backward"` - 后向<br>`"both"` - 双向 | 传播设置 |
| `"override global monitor settings"` | 布尔 | 0 | 是否覆盖全局监视器设置 | 结果输出 |
| `"group index calculation"` | 布尔 | 0 | 是否计算群折射率 | 高级分析 |
| `"bent waveguide"` | 布尔 | 0 | 是否考虑弯曲波导效应 | 弯曲结构 |
| `"bend radius"` | 数值 | 0 | 弯曲半径（m） | 弯曲波导 |
| `"bend orientation"` | 字符串 | `"z"` | 弯曲方向轴 | 弯曲波导 |
| `"mesh refinement"` | 字符串 | `"conformal variant 0"` | 网格细化方法 | 数值精度 |
| `"convergence"` | 数值 | 1e-8 | 收敛容差 | 迭代求解 |
| `"max iterations"` | 整数 | 100 | 最大迭代次数 | 迭代求解 |
| `"store s matrix"` | 布尔 | 0 | 是否存储 S 矩阵 | 结果存储 |
| `"store field profiles"` | 布尔 | 0 | 是否存储场分布 | 结果存储 |
| `"store mode coefficients"` | 布尔 | 0 | 是否存储模式系数 | 结果存储 |
| `"normalization"` | 字符串 | `"power"` | 归一化方法：`"power"`, `"amplitude"` | 结果归一化 |
| `"phase reference"` | 字符串 | `"first mode"` | 相位参考模式 | 相位处理 |
| `"xy span"` | 数值 | 0 | XY 平面分析区域跨度 | 2D 分析 |
| `"z span"` | 数值 | 0 | Z 方向分析长度 | 传播方向 |
| `"x"` | 数值 | 0 | 分析区域 X 坐标 | 位置设置 |
| `"y"` | 数值 | 0 | 分析区域 Y 坐标 | 位置设置 |
| `"z"` | 数值 | 0 | 分析区域 Z 坐标 | 位置设置 |
| `"background index"` | 数值 | 1.0 | 背景折射率 | 材料设置 |
| `"surface roughness"` | 数值 | 0 | 表面粗糙度（m） | 损耗计算 |
| `"sidewall angle"` | 数值 | 90 | 侧壁角度（度） | 制造误差 |

## 使用示例

### 示例 1：基本波导 EME 分析
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
mode.set("z", 0)
mode.set("x span", 500e-9)  # 宽度
mode.set("y span", 220e-9)  # 厚度
mode.set("z span", 10e-6)   # 长度

# 添加 EME 求解器
mode.addeme()
mode.set("name", "eme_solver")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("z span", 10e-6)

# 配置 EME 分析参数
mode.emeanalysis("eme_solver", "wavelength", 1.55e-6)
mode.emeanalysis("eme_solver", "number of modes", 8)
mode.emeanalysis("eme_solver", "propagation direction", "forward")
mode.emeanalysis("eme_solver", "override global monitor settings", True)

# 运行 EME 分析
mode.run()

# 获取传输结果
transmission = mode.getresult("eme_solver", "transmission")
print(f"波导传输效率: {transmission*100:.2f}%")

# 获取模式信息
modes = mode.getresult("eme_solver", "modes")
print(f"使用的模式数量: {len(modes)}")
```

### 示例 2：定向耦合器分析
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 创建两个平行波导（定向耦合器）
for i in [-1, 1]:
    mode.addrect()
    mode.set("name", f"waveguide_{i}")
    mode.set("material", "Si (Silicon) - Palik")
    mode.set("x", i * 750e-9)  # 间距 1.5μm
    mode.set("y", 0)
    mode.set("z", 0)
    mode.set("x span", 500e-9)   # 宽度
    mode.set("y span", 220e-9)   # 厚度
    mode.set("z span", 100e-6)   # 耦合长度

# 添加 EME 求解器
mode.addeme()
mode.set("name", "coupler_analysis")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("z span", 100e-6)

# 配置耦合器分析
mode.emeanalysis("coupler_analysis", "wavelength", 1.55e-6)
mode.emeanalysis("coupler_analysis", "number of modes", 12)  # 需要更多模式分析耦合
mode.emeanalysis("coupler_analysis", "propagation direction", "both")
mode.emeanalysis("coupler_analysis", "store s matrix", True)
mode.emeanalysis("coupler_analysis", "store field profiles", True)

# 运行分析
mode.run()

# 获取耦合结果
s_matrix = mode.getresult("coupler_analysis", "s matrix")
through_port = np.abs(s_matrix[0, 0])**2  # 直通端口功率
cross_port = np.abs(s_matrix[1, 0])**2     # 交叉端口功率

print(f"直通端口传输: {through_port*100:.2f}%")
print(f"交叉端口耦合: {cross_port*100:.2f}%")

# 计算耦合长度
coupling_length = 100e-6  # 已知长度
print(f"在 {coupling_length*1e6:.0f}μm 长度上的耦合效率: {cross_port*100:.2f}%")
```

### 示例 3：宽带 EME 分析
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 创建波导结构
mode.addrect()
mode.set("name", "broadband_waveguide")
mode.set("material", "Si (Silicon) - Palik")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("x span", 500e-9)
mode.set("y span", 220e-9)
mode.set("z span", 5e-3)  # 5mm 长波导

# 添加 EME 求解器
mode.addeme()
mode.set("name", "broadband_analysis")
mode.set("z span", 5e-3)

# 配置宽带分析
mode.emeanalysis("broadband_analysis", "wavelength", 1.55e-6)
mode.emeanalysis("broadband_analysis", "wavelength span", 100e-9)  # 100nm 扫描范围
mode.emeanalysis("broadband_analysis", "number of modes", 6)
mode.emeanalysis("broadband_analysis", "store s matrix", True)

# 运行宽带分析
mode.run()

# 获取波长扫描结果
wavelengths = mode.getresult("broadband_analysis", "wavelength")
transmission = mode.getresult("broadband_analysis", "transmission")

# 找到最佳传输波长
best_idx = np.argmax(transmission)
best_wavelength = wavelengths[best_idx]
best_transmission = transmission[best_idx]

print(f"波长扫描范围: {wavelengths[0]*1e9:.1f} - {wavelengths[-1]*1e9:.1f} nm")
print(f"最佳传输波长: {best_wavelength*1e9:.1f} nm")
print(f"最佳传输效率: {best_transmission*100:.2f}%")
print(f"3dB 带宽: {(wavelengths[-1] - wavelengths[0])*1e9:.1f} nm")

# 绘制传输谱
import matplotlib.pyplot as plt
plt.figure()
plt.plot(wavelengths*1e9, transmission*100)
plt.xlabel("波长 (nm)")
plt.ylabel("传输效率 (%)")
plt.title("波导宽带传输特性")
plt.grid(True)
plt.show()
```

### 示例 4：弯曲波导损耗分析
```python
import lumapi

mode = lumapi.MODE()

# 创建弯曲波导结构（90度弯曲）
# 实际结构中应有弯曲几何，这里简化为直波导加弯曲参数

# 添加 EME 求解器
mode.addeme()
mode.set("name", "bend_analysis")
mode.set("z span", 50e-6)  # 弯曲波导等效长度

# 配置弯曲波导分析
mode.emeanalysis("bend_analysis", "wavelength", 1.55e-6)
mode.emeanalysis("bend_analysis", "number of modes", 8)
mode.emeanalysis("bend_analysis", "bent waveguide", True)
mode.emeanalysis("bend_analysis", "bend radius", 10e-6)  # 10μm 弯曲半径
mode.emeanalysis("bend_analysis", "bend orientation", "z")
mode.emeanalysis("bend_analysis", "propagation direction", "forward")

# 设置弯曲损耗计算参数
mode.setnamed("bend_analysis", "surface roughness", 5e-9)  # 5nm 表面粗糙度
mode.setnamed("bend_analysis", "sidewall angle", 87)        # 87度侧壁角

# 运行分析
mode.run()

# 获取弯曲损耗结果
transmission = mode.getresult("bend_analysis", "transmission")
bend_loss_db = -10 * np.log10(transmission)  # 转换为 dB

print(f"弯曲波导传输效率: {transmission*100:.2f}%")
print(f"弯曲损耗: {bend_loss_db:.2f} dB")
print(f"弯曲半径: 10μm, 波长: 1550nm")

# 对比直波导（关闭弯曲效应）
mode.emeanalysis("bend_analysis", "bent waveguide", False)
mode.run()
straight_transmission = mode.getresult("bend_analysis", "transmission")
straight_loss_db = -10 * np.log10(straight_transmission)

print(f"\n直波导传输效率: {straight_transmission*100:.2f}%")
print(f"直波导损耗: {straight_loss_db:.2f} dB")
print(f"弯曲引起的附加损耗: {bend_loss_db - straight_loss_db:.2f} dB")
```

### 示例 5：MMI 耦合器优化
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 创建多模干涉耦合器基本结构
mode.addrect()
mode.set("name", "MMI_coupler")
mode.set("material", "Si (Silicon) - Palik")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("x span", 6e-6)    # MMI 宽度
mode.set("y span", 220e-9)  # 厚度
mode.set("z span", 50e-6)   # MMI 长度

# 添加输入/输出波导（简化为端口设置）
# 实际结构中应有输入输出波导

# 添加 EME 求解器
mode.addeme()
mode.set("name", "MMI_analysis")
mode.set("z span", 50e-6)

# 配置 MMI 分析
mode.emeanalysis("MMI_analysis", "wavelength", 1.55e-6)
mode.emeanalysis("MMI_analysis", "number of modes", 20)  # MMI 需要较多模式
mode.emeanalysis("MMI_analysis", "propagation direction", "forward")
mode.emeanalysis("MMI_analysis", "store field profiles", True)
mode.emeanalysis("MMI_analysis", "store mode coefficients", True)

# 运行分析
mode.run()

# 获取 MMI 性能参数
s_matrix = mode.getresult("MMI_analysis", "s matrix")
field_profiles = mode.getresult("MMI_analysis", "field profiles")

# 分析输出端口功率分配
# 假设端口1为输入，端口2和3为输出
input_power = 1.0  # 归一化输入功率
output1_power = np.abs(s_matrix[1, 0])**2
output2_power = np.abs(s_matrix[2, 0])**2

total_output = output1_power + output2_power
imbalance = abs(output1_power - output2_power) / total_output

print(f"MMI 耦合器性能分析:")
print(f"输入端口: 端口 1")
print(f"输出端口1功率: {output1_power*100:.2f}%")
print(f"输出端口2功率: {output2_power*100:.2f}%")
print(f"总输出功率: {total_output*100:.2f}% (损耗: {(1-total_output)*100:.2f}%)")
print(f"功率不平衡度: {imbalance*100:.2f}%")

# 优化建议
if imbalance < 0.05:  # 5% 不平衡度
    print("MMI 设计良好，功率分配均衡")
else:
    print("建议调整 MMI 宽度或长度以改善功率分配")
    
if total_output > 0.9:
    print("插入损耗可接受")
else:
    print("插入损耗较高，建议检查模式匹配")
```

## 注意事项

### 1. 模式数量选择
- **太少模式**：可能导致精度不足，特别是对于宽波导或多模结构
- **太多模式**：增加计算时间，可能引入数值噪声
- **经验法则**：至少包含所有导模，加上几个辐射模以提高精度

### 2. 波长设置
- 确保波长在材料透明窗口内
- 对于宽带分析，合理选择扫描范围和点数
- 注意波长与频率的换算关系：`frequency = c / wavelength`

### 3. 收敛性控制
- 复杂结构可能需要更严格的收敛容差
- 增加最大迭代次数以处理难收敛问题
- 使用网格细化提高数值精度

### 4. 内存管理
- 存储 S 矩阵、场分布等结果需要额外内存
- 对于大型结构，考虑选择性存储必要结果
- 使用 `"store s matrix"` 等选项控制存储内容

### 5. 边界条件
- EME 默认使用完美匹配层（PML）边界
- 确保分析区域足够大，避免边界反射影响结果
- 对于周期性结构，考虑使用周期性边界条件

### 6. 结果验证
- 对比不同模式数量的结果以确保收敛
- 验证功率守恒：输入功率应等于输出功率加损耗
- 检查模式正交性和归一化

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 不支持 | 使用时域方法分析类似结构 |
| **MODE Solutions** | 完全支持 | EME 是 MODE 的核心功能 |
| **DEVICE** | 不支持 | 专注于电学-热学仿真 |
| **INTERCONNECT** | 不支持 | 使用紧凑模型方法 |

## 相关命令

- [`addeme`](./addeme.md) - 添加 EME 求解器
- [`addemeprofile`](./addemeprofile.md) - 添加 EME 场监视器
- [`run`](./run.md) - 运行仿真（包括 EME 分析）
- [`getresult`](./getresult.md) - 获取 EME 分析结果
- [`set`](./set.md) - 设置对象属性（替代方法）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2025-01-31 | 初始版本，基于 Lumerical 2023R2 文档 |
| 1.1 | 2025-02-15 | 增加弯曲波导和 MMI 示例 |

## 理论基础

### EME 方法原理
1. **模式分解**：在每个截面将场展开为本征模的线性组合
2. **模式传播**：每个模式以各自的传播常数在 z 方向传播
3. **S 矩阵连接**：使用散射矩阵连接不同截面
4. **全局求解**：组合所有截面的 S 矩阵得到整体响应

### 数值优势
- **计算效率**：与结构长度线性相关，适合长结构
- **频率选择性**：直接计算特定频率的响应
- **模式洞察**：提供模式耦合和转换的详细信息

### 局限性
- **假设**：假设截面在传播方向不变（缓变近似）
- **模式截断**：有限模式数量可能引入误差
- **非线性效应**：不适合非线性光学仿真

## 故障排除

### 常见问题
1. **收敛失败**：
   - 增加模式数量
   - 放宽收敛容差
   - 检查结构参数是否合理

2. **功率不守恒**：
   - 检查模式数量是否足够
   - 验证边界条件设置
   - 确认材料参数正确

3. **内存不足**：
   - 减少存储的数据量
   - 使用更少的模式
   - 减小分析区域

4. **结果异常**：
   - 检查波长是否在材料透明窗口
   - 验证网格密度是否足够
   - 确认传播方向设置正确

### 调试建议
- 从简单结构开始验证设置
- 逐步增加复杂度并监控结果变化
- 使用 `get("eme_solver")` 查看当前设置
- 保存中间结果进行对比分析

---

*文档版本：1.0 | 最后更新：2025-01-31*