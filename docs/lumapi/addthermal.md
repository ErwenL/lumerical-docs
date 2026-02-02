# addthermal

## 概述

`addthermal` 命令用于在 DEVICE 仿真中添加热监视器。热监视器用于测量和记录温度分布、热流、热阻等热学参数，是热电耦合仿真的关键组件。该命令支持稳态和瞬态热分析，可用于热管理、热效应评估、热电优化等应用。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addthermal;
```

### Python API (Lumapi)
```python
session.addthermal()
```

## 参数

`addthermal` 命令没有直接参数，但需要通过后续的 `set` 命令配置热监视器类型、位置和测量参数。

## 配置属性

添加热监视器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "thermal monitor" | 热监视器名称 |
| `enabled` | bool | true | 是否启用监视器 |
| `monitor type` | string | "temperature" | 监视器类型："temperature", "heat flux", "thermal resistance", "power density" |
| `analysis type` | string | "steady state" | 分析类型："steady state", "transient" |
| `dimensionality` | int | 3 | 维度：1（1D）、2（2D）、3（3D） |

### 2. 几何与位置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 监视器中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 监视器尺寸 (m) |
| `rotation x` | float | 0 | X 轴旋转角度 (度) |
| `rotation y` | float | 0 | Y 轴旋转角度 (度) |
| `rotation z` | float | 0 | Z 轴旋转角度 (度) |
| `monitor region` | string | "volume" | 监视区域："volume", "surface", "line", "point" |
| `sampling points` | int | 101 | 采样点数（仅限 line/point 类型） |

### 3. 温度监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `temperature unit` | string | "K" | 温度单位："K", "C", "F" |
| `temperature range` | vector | [273, 373] | 温度范围 [min, max] (K) |
| `reference temperature` | float | 300 | 参考温度 (K) |
| `temperature resolution` | float | 0.1 | 温度分辨率 (K) |
| `show isotherms` | bool | true | 是否显示等温线 |
| `isotherm levels` | int | 10 | 等温线数量 |
| `color map` | string | "thermal" | 颜色映射："thermal", "jet", "hot", "cool" |

### 4. 热流监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `heat flux component` | string | "all" | 热流分量："x", "y", "z", "all", "magnitude" |
| `heat flux unit` | string | "W/m²" | 热流单位："W/m²", "kW/m²", "mW/cm²" |
| `flux direction` | vector | [1,0,0] | 热流方向向量 |
| `normalize flux` | bool | false | 是否归一化热流 |
| `flux scale` | string | "linear" | 热流缩放："linear", "log", "dB" |

### 5. 热阻监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal resistance type` | string | "spreading" | 热阻类型："spreading", "junction-to-case", "junction-to-ambient" |
| `hot side` | string | "junction" | 热端标识 |
| `cold side` | string | "case" | 冷端标识 |
| `power input` | float | 1 | 输入功率 (W) |
| `temperature difference` | float | 自动计算 | 温差 (K) |
| `resistance unit` | string | "K/W" | 热阻单位："K/W", "°C/W" |

### 6. 功率密度监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `power density type` | string | "volumetric" | 功率密度类型："volumetric", "surface", "linear" |
| `power source` | string | "" | 功率源名称 |
| `density unit` | string | "W/m³" | 功率密度单位："W/m³", "W/cm³", "kW/m³" |
| `integrate power` | bool | false | 是否积分总功率 |
| `power threshold` | float | 0 | 功率阈值 (W/m³) |

### 7. 瞬态分析设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `transient duration` | float | 1e-3 | 瞬态持续时间 (s) |
| `time steps` | int | 100 | 时间步数 |
| `sampling rate` | float | 1e6 | 采样率 (Hz) |
| `initial temperature` | float | 300 | 初始温度 (K) |
| `boundary conditions` | dict | {} | 边界条件字典 |
| `thermal mass` | bool | true | 是否考虑热容 |

### 8. 材料热属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal conductivity` | float | 自动获取 | 热导率 (W/m·K) |
| `specific heat capacity` | float | 自动获取 | 比热容 (J/kg·K) |
| `density` | float | 自动获取 | 密度 (kg/m³) |
| `thermal expansion` | float | 自动获取 | 热膨胀系数 (1/K) |
| `emissivity` | float | 0 | 发射率 |
| `convective coefficient` | float | 0 | 对流系数 (W/m²·K) |

### 9. 数据输出
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `data type` | string | "temperature" | 输出数据类型："temperature", "flux", "gradient", "all" |
| `output format` | string | "mat" | 输出格式："mat", "txt", "csv", "vtk" |
| `save raw data` | bool | true | 是否保存原始数据 |
| `save processed data` | bool | true | 是否保存处理后数据 |
| `data compression` | bool | false | 是否压缩数据 |
| `auto export` | bool | false | 是否自动导出数据 |

### 10. 可视化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `visualization` | bool | true | 是否可视化结果 |
| `opacity` | float | 0.7 | 透明度 (0-1) |
| `contour lines` | bool | true | 是否显示等高线 |
| `vector arrows` | bool | false | 是否显示矢量箭头（热流） |
| `arrow density` | float | 0.1 | 箭头密度 |
| `color bar` | bool | true | 是否显示颜色条 |
| `legend` | bool | true | 是否显示图例 |

### 11. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `adaptive meshing` | bool | false | 是否启用自适应网格 |
| `mesh refinement` | int | 1 | 网格细化级别 (1-5) |
| `convergence tolerance` | float | 1e-6 | 收敛容差 |
| `max iterations` | int | 1000 | 最大迭代次数 |
 | `solver type` | string | "direct" | 求解器类型："direct", "iterative", "multigrid" |
| `preconditioner` | string | "none" | 预条件器 |

## 返回值

`addthermal` 命令没有返回值。成功执行后，会在仿真中添加一个热监视器对象。

## 示例

### 示例 1：添加温度分布监视器
```python
import lumapi

session = lumapi.DEVICE()

# 添加温度监视器
session.addthermal()
session.set("name", "temperature_monitor")
session.set("monitor type", "temperature")

# 配置几何尺寸
session.set("x span", 10e-6)  # 10 μm 宽度
session.set("y span", 10e-6)  # 10 μm 高度
session.set("z span", 1e-6)   # 1 μm 厚度
session.set("x", 0)
session.set("y", 0)
session.set("z", 0)

# 配置温度设置
session.set("temperature unit", "C")  # 使用摄氏度
session.set("temperature range", [20, 120])  # 20-120°C
session.set("reference temperature", 25)  # 25°C 参考温度

# 配置可视化
session.set("show isotherms", True)
session.set("isotherm levels", 15)
session.set("color map", "hot")
session.set("opacity", 0.8)

# 配置数据输出
session.set("output format", "csv")
session.set("save raw data", True)
session.set("auto export", True)
```

### 示例 2：添加热流矢量监视器
```python
import lumapi

session = lumapi.DEVICE()

# 添加热流监视器
session.addthermal()
session.set("name", "heat_flux_monitor")
session.set("monitor type", "heat flux")

# 配置几何位置（位于热源表面）
session.set("monitor region", "surface")
session.set("x span", 5e-6)  # 5 μm × 5 μm 表面
session.set("y span", 5e-6)
session.set("z", 0.5e-6)  # 位于表面上方 0.5 μm

# 配置热流设置
session.set("heat flux component", "all")  # 监视所有分量
session.set("heat flux unit", "kW/m²")  # 使用 kW/m² 单位
session.set("flux direction", [0, 0, 1])  # 主要沿 Z 方向

# 配置矢量可视化
session.set("vector arrows", True)
session.set("arrow density", 0.15)  # 中等密度箭头
session.set("color map", "jet")

# 配置高级设置
session.set("adaptive meshing", True)
session.set("mesh refinement", 2)
session.set("convergence tolerance", 1e-5)

# 配置材料热属性（覆盖默认值）
session.set("thermal conductivity", 150)  # 硅的热导率 (W/m·K)
session.set("specific heat capacity", 700)  # 硅的比热容 (J/kg·K)
session.set("density", 2330)  # 硅的密度 (kg/m³)
```

### 示例 3：添加热阻监视器（芯片封装）
```python
import lumapi

session = lumapi.DEVICE()

# 添加热阻监视器
session.addthermal()
session.set("name", "thermal_resistance_monitor")
session.set("monitor type", "thermal resistance")
session.set("thermal resistance type", "junction-to-case")

# 配置热阻测量
session.set("hot side", "junction")  # 热端：芯片结
session.set("cold side", "case_top")  # 冷端：封装顶部
session.set("power input", 2.5)  # 2.5 W 输入功率

# 配置几何位置（连接结和封装）
session.set("x", 0)
session.set("y", 0)
session.set("z span", 100e-6)  # 覆盖结到封装的垂直距离

# 配置材料属性（多层结构）
# 第一层：硅芯片
session.set("thermal conductivity layer1", 150)  # 硅
session.set("thickness layer1", 50e-6)  # 50 μm 硅厚度

# 第二层：热界面材料
session.set("thermal conductivity layer2", 3)  # TIM 材料
session.set("thickness layer2", 20e-6)  # 20 μm TIM 厚度

# 第三层：铜散热器
session.set("thermal conductivity layer3", 400)  # 铜
session.set("thickness layer3", 30e-6)  # 30 μm 铜厚度

# 配置边界条件
boundary_conditions = {
    "bottom": "fixed_temperature",  # 底部固定温度
    "top": "convection",  # 顶部对流
    "sides": "adiabatic"  # 侧面绝热
}
session.set("boundary conditions", boundary_conditions)
session.set("reference temperature", 25)  # 25°C 环境温度
session.set("convective coefficient", 10)  # 10 W/m²·K 对流系数

# 配置输出
session.set("resistance unit", "°C/W")  # 使用 °C/W
session.set("output format", "txt")
session.set("save processed data", True)
```

### 示例 4：瞬态热分析监视器
```python
import lumapi

session = lumapi.DEVICE()

# 添加瞬态热监视器
session.addthermal()
session.set("name", "transient_thermal_monitor")
session.set("analysis type", "transient")

# 配置瞬态参数
session.set("transient duration", 10e-3)  # 10 ms 仿真时间
session.set("time steps", 1000)  # 1000 个时间步
session.set("sampling rate", 100e3)  # 100 kHz 采样率
session.set("initial temperature", 25)  # 初始温度 25°C

# 配置功率脉冲（模拟开关操作）
pulse_script = """
# 定义功率脉冲
def power_pulse(t):
    # 0-2 ms: 0 W (关闭)
    # 2-4 ms: 5 W (开启)
    # 4-10 ms: 0 W (关闭)
    if 2e-3 <= t < 4e-3:
        return 5.0
    else:
        return 0.0
"""
session.set("custom power profile", pulse_script)

# 配置监视器位置（热源区域）
session.set("x span", 2e-6)  # 2 μm × 2 μm 热点区域
session.set("y span", 2e-6)
session.set("z", 0)
session.set("monitor region", "volume")

# 配置温度监视
session.set("monitor type", "temperature")
session.set("temperature resolution", 0.01)  # 0.01°C 分辨率

# 配置材料热属性（考虑热容）
session.set("thermal mass", True)
session.set("specific heat capacity", 700)  # 硅的比热容
session.set("density", 2330)  # 硅的密度

# 配置数据记录
session.set("save raw data", True)
session.set("data compression", True)  # 启用压缩（数据量大）
session.set("output format", "mat")

# 配置可视化（温度随时间变化）
session.set("visualization", True)
session.set("show isotherms", False)
session.set("color map", "thermal")

# 配置高级求解器设置
session.set("solver type", "iterative")
session.set("preconditioner", "ILU")
session.set("max iterations", 5000)
session.set("convergence tolerance", 1e-7)
```

## 错误处理

### 常见错误
1. **内存不足**：热仿真数据量较大，可能导致内存不足
   - 解决方案：减少网格密度、使用数据压缩、分区域仿真

2. **收敛失败**：瞬态热分析可能不收敛
   - 解决方案：减小时间步长、调整求解器参数、检查边界条件

3. **网格质量问题**：不规则网格导致结果不准确
   - 解决方案：使用结构化网格、检查网格质量、启用自适应网格

4. **材料属性缺失**：未定义材料热属性
   - 解决方案：确保所有材料都定义了热导率、比热容和密度

5. **单位不一致**：混合使用不同单位系统
   - 解决方案：统一使用 SI 单位制，检查所有物理量的单位

### Python 错误处理
```python
import lumapi

try:
    device = lumapi.DEVICE()
    
    # 添加热监视器
    device.addthermal()
    
    # 配置热监视器属性
    device.set("name", "thermal_monitor_test")
    device.set("monitor type", "temperature")
    device.set("x span", 10e-6)
    
    # 检查参数有效性
    if device.get("x span") <= 0:
        raise ValueError("几何尺寸必须为正数")
    
    # 运行热分析
    device.runthermal()
    
except lumapi.LumApiError as e:
    print(f"热监视器创建失败: {e}")
    
    # 检查具体错误类型
    if "memory" in str(e).lower():
        print("错误: 内存不足，请减少网格密度或使用数据压缩")
    elif "convergence" in str(e).lower():
        print("错误: 求解器不收敛，请调整时间步长或求解器参数")
    elif "mesh" in str(e).lower():
        print("错误: 网格质量问题，请检查网格设置")
    elif "material" in str(e).lower():
        print("错误: 材料属性缺失，请定义所有材料的热属性")
    else:
        print(f"未知错误: {e}")
        
except ValueError as e:
    print(f"参数错误: {e}")
    
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **网格收敛**：热仿真对网格敏感，确保网格足够精细以获得准确结果
2. **材料属性**：准确的材料热属性对结果可靠性至关重要
3. **边界条件**：合理设置边界条件，反映实际物理环境
4. **瞬态稳定性**：瞬态分析需要满足 Courant-Friedrichs-Lewy (CFL) 条件
5. **计算资源**：3D 热仿真可能需要大量计算资源，合理设置求解器参数
6. **单位一致性**：注意所有物理量的单位一致性
7. **热耦合**：考虑热电耦合、热光耦合等多物理场效应
8. **验证与验证**：通过解析解或实验数据验证仿真结果

## 产品支持

- **FDTD Solutions**: 不支持（使用 `addheat` 命令）
- **MODE Solutions**: 不支持
- **DEVICE**: 支持（主要应用）
- **INTERCONNECT**: 不支持（热学分析在 DEVICE 中进行）

## 相关命令

- `addheat` - 添加热求解器（FDTD）
- `addproperty` - 添加材料热属性
- `set` - 设置热监视器属性
- `getthermal` - 获取热仿真结果
- `runthermal` - 运行热分析
- `animate` - 创建热场动画

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增瞬态热分析支持 |
| Lumerical 2019a | 改进热阻计算精度 |
| Lumerical 2018a | 新增热流矢量监视器 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical DEVICE 热仿真指南
2. 传热学基础理论
3. 热电耦合仿真方法

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*