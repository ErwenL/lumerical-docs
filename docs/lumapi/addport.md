# addport

## 概述

`addport` 命令用于在 FDTD、MODE 和 INTERCONNECT 仿真中添加端口。端口是仿真中信号输入输出的边界条件，可以是光学端口、电学端口或模式端口，用于定义激励源、监视器或外部连接接口。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addport;
```

### Python API (Lumapi)
```python
session.addport()
```

## 参数

`addport` 命令没有直接参数，但需要通过后续的 `set` 命令配置端口类型和属性。端口的具体配置取决于仿真类型（FDTD、MODE 或 INTERCONNECT）。

## 配置属性

添加端口后，可以使用 `set` 命令配置以下属性。不同仿真器支持的属性有所不同：

### 1. 基本设置（通用）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "port" | 端口名称 |
| `enabled` | bool | true | 是否启用端口 |
| `port type` | string | "standard" | 端口类型："standard", "modal", "lumped" |
| `monitor type` | string | "none" | 监视器类型："none", "time", "frequency" |
| `injection axis` | string | "x" | 注入方向："x", "y", "z" |
| `direction` | string | "forward" | 传播方向："forward", "backward", "bidirectional" |

### 2. FDTD 特定属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `source type` | string | "mode source" | 源类型："mode source", "gaussian", "plane wave" |
| `mode selection` | string | "fundamental" | 模式选择："fundamental", "user defined" |
| `mode number` | int | 1 | 模式编号 |
| `frequency` | float | 200e12 | 频率 (Hz) |
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `bandwidth` | float | 50e12 | 带宽 (Hz) |
| `amplitude` | float | 1 | 振幅 (归一化) |
| `phase` | float | 0 | 相位 (弧度) |
| `polarization angle` | float | 0 | 偏振角 (度) |
| `offset` | float | 0 | 偏移距离 (m) |
| `spread factor` | float | 1 | 扩展因子 |

### 3. MODE 特定属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mode expansion` | bool | false | 是否启用模式扩展 |
| `number of modes` | int | 1 | 模式数量 |
| `mode solver` | string | "FDE" | 模式求解器："FDE", "EME" |
| `boundary conditions` | string | "PML" | 边界条件："PML", "metal", "periodic" |
| `mesh accuracy` | int | 2 | 网格精度 (1-5) |
| `effective index` | float | 自动计算 | 有效折射率 |
| `group index` | float | 自动计算 | 群折射率 |
| `confinement factor` | float | 自动计算 | 限制因子 |

### 4. INTERCONNECT 特定属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `port subtype` | string | "optical" | 端口子类型："optical", "electrical", "thermal" |
| `impedance` | float | 50 | 阻抗 (Ω) |
| `voltage` | float | 1 | 电压 (V) |
| `current` | float | 0.02 | 电流 (A) |
| `power` | float | 1e-3 | 功率 (W) |
| `s parameters` | matrix | 单位矩阵 | S 参数矩阵 |
| `noise figure` | float | 3 | 噪声系数 (dB) |
| `temperature` | float | 300 | 温度 (K) |

### 5. 几何与位置（通用）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 端口中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 端口尺寸 (m) |
| `rotation x` | float | 0 | X 轴旋转角度 (度) |
| `rotation y` | float | 0 | Y 轴旋转角度 (度) |
| `rotation z` | float | 0 | Z 轴旋转角度 (度) |
| `normal` | vector | [1,0,0] | 法线方向向量 |
| `tangent` | vector | [0,1,0] | 切线方向向量 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `advanced options` | bool | false | 是否启用高级选项 |
| `custom source` | string | "" | 自定义源脚本 |
| `custom monitor` | string | "" | 自定义监视器脚本 |
| `data logging` | bool | true | 是否记录数据 |
| `visualization` | bool | true | 是否可视化 |
| `overwrite` | bool | false | 是否覆盖现有数据 |

## 示例

### 示例 1：FDTD 中的模式源端口

#### LSF 脚本
```lumerical
// 添加模式源端口
addport;
set("name", "fdtd_mode_source");
set("port type", "modal");
set("source type", "mode source");

// 配置模式设置
set("mode selection", "fundamental");
set("mode number", 1);
set("wavelength", 1.55e-6);  // 1550 nm
set("bandwidth", 100e12);    // 100 GHz 带宽

// 配置位置和方向
set("x", 0);
set("y", 0);
set("z", 0);
set("injection axis", "x");
set("direction", "forward");

// 配置振幅和相位
set("amplitude", 1.0);
set("phase", 0.0);
set("polarization angle", 0);
```

#### Python API
```python
import lumapi

session = lumapi.MODE()

# 添加模式扩展端口
session.addport()
session.set("name", "mode_expansion_port")
session.set("port type", "modal")
session.set("mode expansion", True)

# 配置模式求解器设置
session.set("mode solver", "FDE")
session.set("number of modes", 3)  # 计算前 3 个模式
session.set("mesh accuracy", 3)

# 配置边界条件
session.set("boundary conditions", "PML")

# 配置几何尺寸
session.set("x span", 2e-6)  # 2 μm 宽度
session.set("y span", 0.5e-6) # 0.5 μm 高度
session.set("z", 0)

# 配置监视器
session.set("monitor type", "frequency")
session.set("data logging", True)
```

### 示例 3：INTERCONNECT 中的电学端口
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加电学端口
session.addport()
session.set("name", "electrical_port")
session.set("port subtype", "electrical")

# 配置电学参数
session.set("impedance", 50)  # 50 Ω 阻抗匹配
session.set("voltage", 3.3)   # 3.3 V 电压
session.set("current", 0.1)   # 100 mA 电流

# 配置位置
session.set("x", 10e-6)
session.set("y", 5e-6)

# 配置高级选项
session.set("noise figure", 2.5)  # 2.5 dB 噪声系数
session.set("data logging", True)
session.set("visualization", True)

# 配置 S 参数（2×2 矩阵）
import numpy as np
s_matrix = [[0.1, 0.9], [0.9, 0.1]]  # 10% 反射，90% 传输
session.set("s parameters", s_matrix)
```

### 示例 4：多端口系统
```python
import lumapi

session = lumapi.FDTD()

# 创建输入和输出端口对
for i in range(4):
    # 输入端口
    session.addport()
    session.set("name", f"input_port_{i+1}")
    session.set("port type", "modal")
    session.set("source type", "mode source")
    session.set("x", i * 5e-6)  # 间隔 5 μm
    session.set("y", 0)
    session.set("direction", "forward")
    
    # 输出端口
    session.addport()
    session.set("name", f"output_port_{i+1}")
    session.set("port type", "modal")
    session.set("monitor type", "frequency")
    session.set("x", i * 5e-6)
    session.set("y", 10e-6)  # 在 Y 方向偏移 10 μm
    session.set("direction", "backward")
```

## 返回值

`addport` 命令没有直接的返回值。成功执行后，会在仿真中添加一个端口对象，该对象可以通过 `set` 命令配置各种端口属性。端口的具体行为和可用属性取决于仿真器类型（FDTD、MODE 或 INTERCONNECT）。

## 错误处理

### 常见错误
1. **端口位置无效**
   - 错误信息：`Invalid port position`
   - 解决方案：确保端口位置在仿真区域内且不与其他结构冲突

2. **仿真器不支持**
   - 错误信息：`Port type not supported by current solver`
   - 解决方案：检查端口类型是否与当前仿真器兼容

3. **模式求解失败**
   - 错误信息：`Mode solver failed`
   - 解决方案：检查模式设置和几何结构

4. **阻抗不匹配**
   - 错误信息：`Impedance mismatch`
   - 解决方案：调整阻抗值或使用匹配网络

5. **内存不足**
   - 错误信息：`Insufficient memory`
   - 解决方案：减少端口尺寸或仿真区域

### Python 错误处理示例
```python
import lumapi

try:
    # 创建 FDTD 会话
    fdtd = lumapi.FDTD()
    
    # 添加端口
    fdtd.addport()
    fdtd.set("name", "test_port")
    fdtd.set("port type", "modal")
    fdtd.set("source type", "mode source")
    
    # 设置无效位置（可能引发错误）
    fdtd.set("x", 1000)  # 可能超出仿真区域
    
except lumapi.LumApiError as e:
    print(f"端口创建失败: {e}")
    
    # 检查具体错误类型
    if "position" in str(e).lower():
        print("错误: 端口位置无效")
    elif "not supported" in str(e).lower():
        print("错误: 仿真器不支持此端口类型")
    elif "mode solver" in str(e).lower():
        print("错误: 模式求解失败")
    elif "impedance" in str(e).lower():
        print("错误: 阻抗不匹配")
    elif "memory" in str(e).lower():
        print("错误: 内存不足")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **端口类型匹配**：确保端口类型与仿真器兼容（FDTD、MODE 或 INTERCONNECT）
2. **边界条件**：端口位置应远离 PML 边界以避免反射伪影
3. **模式匹配**：对于模式端口，确保模式设置与波导结构匹配
4. **阻抗匹配**：对于电学端口，设置正确的阻抗以减少反射
5. **功率校准**：确保端口功率设置在合理范围内
6. **网格收敛**：网格设置应足够精细以准确解析端口场
7. **仿真效率**：过多端口会增加计算复杂度，合理设置端口数量

## 产品支持

- **FDTD Solutions**: 支持模式源、平面波源、高斯源等端口类型
- **MODE Solutions**: 支持模式扩展、模式监视器等端口类型
- **DEVICE**: 不支持（使用 `addthermal` 等专用命令）
- **INTERCONNECT**: 支持光学、电学、热学端口类型

## 相关命令

- `addmode` - 添加模式监视器
- `addpower` - 添加功率监视器
- `addprofile` - 添加场监视器
- `addoptical` - 添加光学端口（INTERCONNECT 专用）
- `addnoise` - 添加噪声源
- `set` - 设置对象属性
- `getport` - 获取端口数据
- `selectport` - 选择端口对象

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 统一跨仿真器端口接口 |
| Lumerical 2019a | 增强 INTERCONNECT 端口功能 |
| Lumerical 2018a | 初始多仿真器端口支持 |

## 参考

1. Lumerical 端口和边界条件用户指南
2. FDTD Solutions 模式源技术说明
3. INTERCONNECT 端口建模手册

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*