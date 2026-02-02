# callsplitter

## 概述

`callsplitter` 命令用于在 INTERCONNECT 仿真中调用分路器模型。分路器是光子集成电路中的基本组件，用于将光信号从一个输入端口分配到多个输出端口，或合并多个输入信号到一个输出端口。该命令支持多种分路器类型，包括 Y 分支、多模干涉（MMI）、定向耦合器、星形耦合器等。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
callsplitter;
```

### Python API (Lumapi)
```python
session.callsplitter()
```

## 参数

`callsplitter` 命令没有直接参数，但需要通过后续的 `set` 命令配置分路器类型、端口配置和性能参数。

## 配置属性

调用分路器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "splitter" | 分路器名称 |
| `splitter type` | string | "y_branch" | 分路器类型："y_branch", "mmi", "directional_coupler", "star_coupler", "multimode", "custom" |
| `num inputs` | int | 1 | 输入端口数量 |
| `num outputs` | int | 2 | 输出端口数量 |
| `enabled` | bool | true | 是否启用分路器 |
| `model type` | string | "ideal" | 模型类型："ideal", "physical", "measured", "behavioral" |

### 2. Y 分支分路器参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `branch angle` | float | 1 | 分支角度 (度) |
| `branch length` | float | 10e-6 | 分支长度 (m) |
| `taper length` | float | 5e-6 | 锥形过渡长度 (m) |
| `taper type` | string | "linear" | 锥形类型："linear", "parabolic", "exponential" |
| `symmetric` | bool | true | 是否对称分支 |

### 3. MMI 分路器参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mmi width` | float | 10e-6 | MMI 区域宽度 (m) |
| `mmi length` | float | 50e-6 | MMI 区域长度 (m) |
| `access waveguide width` | float | 0.5e-6 | 接入波导宽度 (m) |
| `access waveguide gap` | float | 2e-6 | 接入波导间距 (m) |
| `self imaging` | bool | true | 是否启用自成像 |
| `multimode order` | int | 1 | 多模阶数 |

### 4. 定向耦合器参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `coupling length` | float | 10e-6 | 耦合长度 (m) |
| `coupling gap` | float | 0.2e-6 | 耦合间隙 (m) |
| `coupling coefficient` | float | 0.5 | 耦合系数 |
| `synchronism` | bool | true | 是否同步耦合 |
| `coupling type` | string | "evanescent" | 耦合类型："evanescent", "multimode", "resonant" |

### 5. 星形耦合器参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `star radius` | float | 50e-6 | 星形半径 (m) |
| `num waveguides` | int | 8 | 波导数量 |
| `waveguide spacing` | float | 2e-6 | 波导间距 (m) |
| `free propagation region` | float | 20e-6 | 自由传播区域长度 (m) |
| `focusing` | bool | true | 是否启用聚焦 |

### 6. 性能参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `insertion loss` | float | 0.5 | 插入损耗 (dB) |
| `excess loss` | float | 0.1 | 附加损耗 (dB) |
| `uniformity` | float | 0.2 | 均匀性 (dB) |
| `return loss` | float | 40 | 回波损耗 (dB) |
| `isolation` | float | 30 | 隔离度 (dB) |
| `polarization dependent loss` | float | 0.1 | 偏振相关损耗 (dB) |
| `wavelength dependent loss` | float | 0.05 | 波长相关损耗 (dB/nm) |
| `temperature dependence` | float | 0.01 | 温度依赖性 (dB/°C) |

### 7. 端口配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `port names` | array | ["in1", "out1", "out2"] | 端口名称数组 |
| `port positions` | matrix | [] | 端口位置矩阵 |
| `port orientations` | array | [] | 端口方向数组 |
| `port impedances` | array | [50, 50, 50] | 端口阻抗数组 (Ω) |
| `port matching` | bool | true | 是否端口匹配 |

### 8. S 参数配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `s parameters` | matrix | 自动计算 | S 参数矩阵 |
| `s parameter type` | string | "complex" | S 参数类型："complex", "magnitude", "phase", "db" |
| `frequency points` | int | 101 | 频率点数 |
| `frequency range` | vector | [150e12, 200e12] | 频率范围 [min, max] (Hz) |
| `s parameter file` | string | "" | S 参数文件路径 |

### 9. 物理模型参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material` | string | "Si" | 材料 |
| `core index` | float | 3.48 | 纤芯折射率 |
| `cladding index` | float | 1.44 | 包层折射率 |
| `waveguide width` | float | 0.5e-6 | 波导宽度 (m) |
| `waveguide height` | float | 0.22e-6 | 波导高度 (m) |
| `etch depth` | float | 0.22e-6 | 刻蚀深度 (m) |
| `sidewall angle` | float | 90 | 侧壁角度 (度) |

### 10. 行为模型参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `behavioral model` | string | "linear" | 行为模型："linear", "nonlinear", "time_varying" |
| `transfer function` | string | "" | 传递函数表达式 |
| `impulse response` | array | [] | 冲激响应数组 |
| `frequency response` | array | [] | 频率响应数组 |
| `nonlinear coefficients` | dict | {} | 非线性系数字典 |

### 11. 测量数据参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `measured data file` | string | "" | 测量数据文件路径 |
| `data format` | string | "s4p" | 数据格式："s4p", "csv", "mat", "touchstone" |
| `interpolation method` | string | "linear" | 插值方法 |
| `extrapolation` | bool | false | 是否外推 |

### 12. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal effects` | bool | false | 是否考虑热效应 |
| `nonlinear effects` | bool | false | 是否考虑非线性效应 |
| `noise figure` | float | 3 | 噪声系数 (dB) |
| `group delay` | float | 0 | 群延迟 (s) |
| `dispersion` | float | 0 | 色散 (ps/nm·km) |
| `crosstalk` | float | -30 | 串扰 (dB) |

## 返回值

`callsplitter` 命令没有直接返回值。调用该命令会在 INTERCONNECT 仿真中创建一个分路器对象，该对象可以通过后续的 `set` 命令进行配置。在 Python API 中，该命令返回 `None`。

## 示例

### 示例 1：基本 Y 分支分路器

#### LSF 脚本
```lumerical
// 创建 Y 分支分路器
callsplitter;
set("name", "y_branch_splitter");
set("splitter type", "y_branch");

// 配置分路器参数
set("num inputs", 1);
set("num outputs", 2);
set("branch angle", 1.0);      # 1度分支角
set("branch length", 15e-6);   # 15 μm 分支长度
set("taper length", 5e-6);     # 5 μm 锥形长度
set("taper type", "parabolic");

// 配置性能参数
set("insertion loss", 0.3);    # 0.3 dB 插入损耗
set("excess loss", 0.1);       # 0.1 dB 附加损耗
set("uniformity", 0.15);       # 0.15 dB 均匀性
set("return loss", 45);        # 45 dB 回波损耗

// 配置端口
set("port names", {"input", "output1", "output2"});
set("port impedances", {50, 50, 50});

// 配置 S 参数
set("frequency range", {150e12, 200e12});  # 150-200 THz
set("frequency points", 201);

// 配置物理参数
set("material", "Si (Silicon) - Palik");
set("waveguide width", 0.5e-6);
set("waveguide height", 0.22e-6);

// 显示成功信息
?"Y-branch splitter configured successfully";
```

#### Python API
```python
import lumapi

session = lumapi.INTERCONNECT()

# 调用 Y 分支分路器
session.callsplitter()
session.set("name", "y_branch_splitter")
session.set("splitter type", "y_branch")

# 配置分路器参数
session.set("num inputs", 1)
session.set("num outputs", 2)
session.set("branch angle", 1.0)      # 1度分支角
session.set("branch length", 15e-6)   # 15 μm 分支长度
session.set("taper length", 5e-6)     # 5 μm 锥形长度
session.set("taper type", "parabolic")

# 配置性能参数
session.set("insertion loss", 0.3)    # 0.3 dB 插入损耗
session.set("excess loss", 0.1)       # 0.1 dB 附加损耗
session.set("uniformity", 0.15)       # 0.15 dB 均匀性
session.set("return loss", 45)        # 45 dB 回波损耗

# 配置端口
session.set("port names", ["input", "output1", "output2"])
session.set("port impedances", [50, 50, 50])

# 配置 S 参数
session.set("frequency range", [150e12, 200e12])  # 150-200 THz
session.set("frequency points", 201)

# 配置物理参数
session.set("material", "Si (Silicon) - Palik")
session.set("waveguide width", 0.5e-6)
session.set("waveguide height", 0.22e-6)

print("Y-branch splitter configured successfully")
```

### 示例 2：MMI 1×4 分路器
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 调用 MMI 分路器
session.callsplitter()
session.set("name", "mmi_1x4_splitter")
session.set("splitter type", "mmi")
session.set("num inputs", 1)
session.set("num outputs", 4)

# 配置 MMI 几何参数
session.set("mmi width", 12e-6)       # 12 μm MMI 宽度
session.set("mmi length", 80e-6)      # 80 μm MMI 长度
session.set("access waveguide width", 0.5e-6)
session.set("access waveguide gap", 2.5e-6)
session.set("self imaging", True)
session.set("multimode order", 2)

# 配置非理想性能（基于制造数据）
session.set("model type", "physical")
session.set("insertion loss", 0.8)    # MMI 通常有较高损耗
session.set("uniformity", 0.3)        # 1×4 均匀性较差
session.set("polarization dependent loss", 0.25)
session.set("wavelength dependent loss", 0.02)  # dB/nm

# 配置波长相关响应
wavelengths = np.linspace(1.53e-6, 1.57e-6, 101)  # C-band
# 创建波长相关的插入损耗（模拟实际响应）
il_vs_wl = 0.8 + 0.1 * np.sin(2*np.pi*(wavelengths-1.55e-6)/0.04e-6)
session.set("wavelength dependent il", il_vs_wl.tolist())

# 配置端口命名
output_ports = [f"out{i+1}" for i in range(4)]
session.set("port names", ["input"] + output_ports)

# 配置测量数据（可选）
session.set("measured data file", "mmi_1x4_measured.s4p")
session.set("data format", "touchstone")
session.set("interpolation method", "cubic")

# 配置高级特性
session.set("thermal effects", True)
session.set("temperature dependence", 0.015)  # 0.015 dB/°C
session.set("crosstalk", -35)  # -35 dB 串扰

print("MMI 1×4 splitter configured with wavelength-dependent response")
```

### 示例 3：定向耦合器作为分路器
```python
import lumapi

session = lumapi.INTERCONNECT()

# 调用定向耦合器分路器
session.callsplitter()
session.set("name", "dc_3dB_splitter")
session.set("splitter type", "directional_coupler")
session.set("num inputs", 2)
session.set("num outputs", 2)

# 配置耦合器参数（3dB 耦合器）
session.set("coupling length", 7.5e-6)    # 7.5 μm 耦合长度
session.set("coupling gap", 0.18e-6)      # 180 nm 耦合间隙
session.set("coupling coefficient", 0.5)  # 3dB 耦合
session.set("coupling type", "evanescent")
session.set("synchronism", True)

# 配置波长敏感型耦合（用于 WDM）
session.set("wavelength dependent loss", 0.03)  # dB/nm
session.set("center wavelength", 1.55e-6)

# 配置 S 参数矩阵（理想 3dB 耦合器）
import numpy as np
# 2×2 耦合器 S 矩阵
s11 = 0.0  # 无反射
s12 = 1/np.sqrt(2)  # 直通 3dB
s13 = 1/np.sqrt(2)  # 耦合 3dB  
s14 = 0.0  # 无反向耦合
s21 = s12
s22 = 0.0
s23 = 0.0
s24 = s13
s31 = s13
s32 = 0.0
s33 = 0.0
s34 = s12
s41 = 0.0
s42 = s13
s43 = s12
s44 = 0.0

s_matrix = [[s11, s12, s13, s14],
            [s21, s22, s23, s24],
            [s31, s32, s33, s34],
            [s41, s42, s43, s44]]

session.set("s parameters", s_matrix)
session.set("s parameter type", "complex")

# 配置端口
session.set("port names", ["in1", "in2", "out1", "out2"])
session.set("port positions", [
    [0, 0, 0],      # in1
    [0, 2e-6, 0],   # in2
    [10e-6, 0, 0],  # out1
    [10e-6, 2e-6, 0] # out2
])

# 配置性能参数
session.set("insertion loss", 0.2)    # 0.2 dB 插入损耗
session.set("isolation", 40)          # 40 dB 隔离度
session.set("return loss", 50)        # 50 dB 回波损耗
session.set("polarization dependent loss", 0.15)

# 配置温度依赖性
session.set("thermal effects", True)
session.set("temperature dependence", 0.02)  # 0.02 dB/°C

print("3dB directional coupler splitter configured with ideal S-parameters")
```

### 示例 4：复杂星形耦合器阵列
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 创建星形耦合器阵列（用于 AWG 或分光器）
num_splitters = 4
splitter_configs = [
    {"name": "star_8x8", "inputs": 8, "outputs": 8, "radius": 60e-6},
    {"name": "star_16x16", "inputs": 16, "outputs": 16, "radius": 80e-6},
    {"name": "star_32x32", "inputs": 32, "outputs": 32, "radius": 120e-6},
    {"name": "star_1x8", "inputs": 1, "outputs": 8, "radius": 40e-6}
]

results = []

for config in splitter_configs:
    # 调用星形耦合器
    session.callsplitter()
    session.set("name", config["name"])
    session.set("splitter type", "star_coupler")
    session.set("num inputs", config["inputs"])
    session.set("num outputs", config["outputs"])
    
    # 配置几何参数
    session.set("star radius", config["radius"])
    session.set("num waveguides", max(config["inputs"], config["outputs"]))
    session.set("waveguide spacing", 1.5e-6)
    session.set("free propagation region", 25e-6)
    session.set("focusing", True)
    
    # 计算性能参数（基于规模的经验公式）
    base_loss = 0.5  # dB
    excess_loss = 0.1 * np.log2(max(config["inputs"], config["outputs"]))
    uniformity = 0.2 + 0.05 * np.log2(max(config["inputs"], config["outputs"]))
    
    session.set("insertion loss", base_loss + excess_loss)
    session.set("excess loss", excess_loss)
    session.set("uniformity", uniformity)
    session.set("return loss", 40)
    
    # 配置波长相关性能
    wavelengths = np.linspace(1.52e-6, 1.58e-6, 5)
    il_vs_wl = (base_loss + excess_loss) + 0.05 * np.sin(
        2*np.pi*(wavelengths-1.55e-6)/0.06e-6
    )
    session.set("wavelength dependent il", il_vs_wl.tolist())
    
    # 配置端口
    input_names = [f"{config['name']}_in{i+1}" for i in range(config["inputs"])]
    output_names = [f"{config['name']}_out{i+1}" for i in range(config["outputs"])]
    session.set("port names", input_names + output_names)
    
    # 配置 S 参数（简化的均匀分光）
    n_ports = config["inputs"] + config["outputs"]
    s_matrix = np.zeros((n_ports, n_ports), dtype=complex)
    
    # 输入到输出的均匀分光
    for i in range(config["inputs"]):
        for j in range(config["inputs"], n_ports):
            # 均匀分光，考虑插入损耗
            s_value = (1/np.sqrt(config["outputs"])) * \
                      10**(-(base_loss + excess_loss)/20) * \
                      np.exp(1j*np.pi*(i+j)/n_ports)
            s_matrix[i, j] = s_value
            s_matrix[j, i] = s_value
    
    session.set("s parameters", s_matrix.tolist())
    
    # 收集性能数据
    results.append({
        "name": config["name"],
        "inputs": config["inputs"],
        "outputs": config["outputs"],
        "radius_um": config["radius"] * 1e6,
        "insertion_loss_dB": base_loss + excess_loss,
        "uniformity_dB": uniformity,
        "port_count": n_ports
    })
    
    print(f"Configured {config['name']}: {config['inputs']}×{config['outputs']}, "
          f"R={config['radius']*1e6:.0f}μm, IL={base_loss+excess_loss:.2f}dB")

# 分析结果
print("\nStar coupler array analysis:")
for r in results:
    print(f"  {r['name']}: {r['inputs']}×{r['outputs']}, "
          f"Ports={r['port_count']}, IL={r['insertion_loss_dB']:.2f}dB, "
          f"Uniformity={r['uniformity_dB']:.2f}dB")

# 找到最佳设计（权衡端口数和损耗）
best_design = min(results, key=lambda x: x['insertion_loss_dB']/x['port_count'])
print(f"\nBest design (loss per port): {best_design['name']}")
```

## 注意事项

1. **分路器选择**：根据应用需求选择合适的分路器类型（Y分支适合1×2，MMI适合1×N，星形适合大端口数）
2. **损耗预算**：分路器会引入插入损耗和附加损耗，需要在系统设计中考虑
3. **均匀性**：多端口分路器的输出均匀性可能不理想，需要校准或补偿
4. **波长依赖性**：分路器性能通常与波长相关，特别是用于WDM系统时
5. **偏振敏感性**：分路器可能有偏振相关损耗，需要评估或使用偏振不敏感设计
6. **制造公差**：物理分路器对制造公差敏感，需要容差分析
7. **热稳定性**：分路器性能可能随温度变化，高精度应用需要温度控制
8. **模式匹配**：分路器与连接波导的模式匹配影响插入损耗

## 错误处理

使用 `callsplitter` 命令时可能遇到的常见错误及其解决方案：

### 1. 无效的分路器类型
- **错误信息**: "Invalid splitter type specified"
- **原因**: 指定的分路器类型不在支持列表中
- **解决方案**: 检查 `splitter type` 属性是否为有效值：`"y_branch"`, `"mmi"`, `"directional_coupler"`, `"star_coupler"`, `"multimode"`, `"custom"`

### 2. 端口数量不匹配
- **错误信息**: "Port count mismatch"
- **原因**: 端口名称数组长度与输入/输出端口数量不一致
- **解决方案**: 确保 `port names` 数组长度等于 `num inputs` + `num outputs`

### 3. 频率范围无效
- **错误信息**: "Invalid frequency range"
- **原因**: 频率范围最小值大于最大值，或包含非正值
- **解决方案**: 确保 `frequency range` 为两个元素的数组，且 `[min, max]` 满足 `min < max`

### 4. S 参数矩阵维度错误
- **错误信息**: "S-parameter matrix dimension mismatch"
- **原因**: S 参数矩阵维度与端口数量不匹配
- **解决方案**: 确保 S 参数矩阵为 N×N 复数矩阵，其中 N = `num inputs` + `num outputs`

### 5. Python API 连接错误
- **错误信息**: "Unable to connect to INTERCONNECT"
- **原因**: INTERCONNECT 未运行或连接失败
- **解决方案**: 
  ```python
  try:
      session = lumapi.INTERCONNECT()
      session.callsplitter()
  except Exception as e:
      print(f"Connection error: {e}")
      # 尝试重新启动 INTERCONNECT
  ```

### 6. 文件路径错误
- **错误信息**: "Cannot open measurement data file"
- **原因**: 测量数据文件路径无效或文件格式不支持
- **解决方案**: 检查文件路径是否存在，确保文件格式为支持的类型

## 产品支持

- **FDTD Solutions**: 不支持（分路器仿真在FDTD中进行，但模型调用在INTERCONNECT）
- **MODE Solutions**: 不支持（分路器设计在MODE中进行，但模型调用在INTERCONNECT）
- **DEVICE**: 不支持
- **INTERCONNECT**: 支持（主要应用）

## 相关命令

- `addport` - 添加端口
- `addoptical` - 添加光学端口
- `cascadedsmatrix` - 计算级联 S 矩阵
- `setsmatrix` - 设置 S 参数
- `getsmatrix` - 获取 S 参数
- `analyze` - 分析电路性能
- `optimizesplitter` - 优化分路器设计

## 参考

1. Lumerical INTERCONNECT User Guide - Splitter Models
2. Lumerical Script Language Reference - callsplitter command
3. Lumerical Python API Documentation - INTERCONNECT module

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本命令说明和配置属性 |
| 1.1 | 2026-01-31 | 添加 LSF 脚本示例，完善错误处理章节 |

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*