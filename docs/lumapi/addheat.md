# addheat

## 概述

`addheat` 命令用于在 DEVICE 仿真中添加热求解器。热求解器用于计算半导体器件中的温度分布，分析自热效应、热传导、热对流、热辐射等热物理过程，适用于激光器、功率放大器、晶体管等器件的热管理分析。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addheat;
```

### Python API (Lumapi)
```python
session.addheat()
```

## 参数

`addheat` 命令没有直接参数，但需要通过后续的 `set` 命令配置热求解器属性。

## 配置属性

添加热求解器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "heat" | 热求解器名称 |
| `x`, `y`, `z` | float | 0 | 求解器区域中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 求解器区域跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 求解器区域最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 求解器区域最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 求解器区域最小/最大坐标 (m) |
| `dimension` | string | "3D" | 求解维度："3D", "2D", "1D" |

### 2. 求解器类型
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `solver type` | string | "steady state" | 求解器类型 |
| `transient time` | float | 1e-9 | 瞬态仿真时间 (s) |
| `time steps` | int | 100 | 时间步数 |
| `auto time step` | bool | true | 是否自动时间步长 |
| `time step` | float | 1e-11 | 时间步长 (s) |
| `initial temperature` | float | 300 | 初始温度 (K) |
| `ambient temperature` | float | 300 | 环境温度 (K) |

### 求解器类型选项：
- **稳态求解**: `"steady state"` - 计算稳态温度分布
- **瞬态求解**: `"transient"` - 计算随时间变化的温度分布
- **频域求解**: `"frequency domain"` - 频域热分析

### 3. 边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x min bc`, `x max bc` | string | "convection" | X 方向边界条件 |
| `y min bc`, `y max bc` | string | "convection" | Y 方向边界条件 |
| `z min bc`, `z max bc` | string | "convection" | Z 方向边界条件 |
| `convection coefficient` | float | 5 | 对流系数 (W/m²·K) |
| `heat transfer coefficient` | float | 自动计算 | 热传递系数 |
| `radiation coefficient` | float | 0 | 辐射系数 |
| `fixed temperature` | float | 300 | 固定边界温度 (K) |

### 边界条件选项：
- **对流**: `"convection"` - 对流换热边界
- **固定温度**: `"fixed temperature"` - 固定温度边界
- **绝热**: `"adiabatic"` - 绝热边界（无热流）
- **热流**: `"heat flux"` - 固定热流边界
- **辐射**: `"radiation"` - 辐射换热边界

### 4. 热源设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `heat sources` | matrix | [] | 热源列表 |
| `heat source type` | string | "volume" | 热源类型 |
| `heat source power` | float | 0 | 热源功率 (W) |
| `heat source position` | vector | [0,0,0] | 热源位置 (m) |
| `heat source size` | vector | [1e-6,1e-6,1e-6] | 热源尺寸 (m) |
| `heat source shape` | string | "rectangular" | 热源形状 |
| `heat generation rate` | float | 0 | 热生成率 (W/m³) |

### 热源类型选项：
- **体积热源**: `"volume"` - 体积内热生成
- **表面热源**: `"surface"` - 表面热流
- **点热源**: `"point"` - 点热源
- **线热源**: `"line"` - 线热源

### 5. 材料热属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal conductivity` | float | 自动从材料数据库获取 | 热导率 (W/m·K) |
| `heat capacity` | float | 自动从材料数据库获取 | 热容 (J/kg·K) |
| `density` | float | 自动从材料数据库获取 | 密度 (kg/m³) |
| `thermal expansion coefficient` | float | 自动从材料数据库获取 | 热膨胀系数 (1/K) |
| `temperature coefficient` | float | 0 | 温度系数 |
| `anisotropic conductivity` | matrix | [1,0,0;0,1,0;0,0,1] | 各向异性热导率矩阵 |

### 6. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh accuracy` | int | 2 | 网格精度 (1-8) |
| `mesh type` | string | "auto non-uniform" | 网格类型 |
| `min mesh step` | float | 1e-12 | 最小网格步长 (m) |
| `max mesh step` | float | 1e-6 | 最大网格步长 (m) |
| `dx`, `dy`, `dz` | float | 自动计算 | 网格步长 (m) |
| `mesh refinement` | string | "none" | 网格细化方式 |
| `refinement regions` | matrix | [] | 细化区域列表 |

### 7. 求解器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `solver` | string | "direct" | 求解器方法 |
| `tolerance` | float | 1e-6 | 求解容差 |
| `max iterations` | int | 1000 | 最大迭代次数 |
| `preconditioner` | string | "ilu" | 预处理器类型 |
| `relaxation factor` | float | 1.0 | 松弛因子 |
| `nonlinear iterations` | int | 10 | 非线性迭代次数 |

### 8. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `save temperature` | bool | true | 是否保存温度场 |
| `save heat flux` | bool | false | 是否保存热流场 |
| `save thermal stress` | bool | false | 是否保存热应力 |
| `output frequency` | int | 1 | 输出频率（每多少步输出一次） |
| `data format` | string | "matlab" | 数据格式 |

## 返回值

`addheat` 命令没有返回值。成功执行后，会在仿真中添加一个热求解器对象。

## 示例

### 示例 1：添加基本热求解器
```python
import lumapi

# 创建 DEVICE 会话
session = lumapi.DEVICE()

# 添加热求解器
session.addheat()

# 配置求解器属性
session.set("name", "thermal_solver")
session.set("solver type", "steady state")
session.set("x span", 10e-6)
session.set("y span", 5e-6)
session.set("z span", 2e-6)

# 配置边界条件
session.set("x min bc", "convection")
session.set("x max bc", "convection")
session.set("convection coefficient", 10)  # 10 W/m²·K
session.set("ambient temperature", 300)  # 27°C

# 配置热源
session.set("heat source power", 0.1)  # 100 mW
session.set("heat source position", [0, 0, 0])
session.set("heat source size", [2e-6, 1e-6, 0.5e-6])
```

### 示例 2：瞬态热分析
```python
import lumapi

session = lumapi.DEVICE()

# 添加热求解器
session.addheat()
session.set("name", "transient_thermal")
session.set("solver type", "transient")
session.set("x span", 20e-6)
session.set("y span", 10e-6)
session.set("z span", 5e-6)

# 配置瞬态参数
session.set("transient time", 1e-6)  # 1 μs
session.set("time steps", 1000)
session.set("auto time step", True)
session.set("initial temperature", 300)

# 配置脉冲热源
session.set("heat source type", "volume")
session.set("heat generation rate", 1e12)  # 1e12 W/m³
session.set("heat source shape", "cylindrical")
session.set("heat source size", [1e-6, 1e-6, 5e-6])  # 半径, 半径, 高度

# 配置输出
session.set("save temperature", True)
session.set("save heat flux", True)
session.set("output frequency", 10)  # 每10步输出一次
```

### 示例 3：与电学求解器耦合
```python
import lumapi

session = lumapi.DEVICE()

# 添加热求解器
session.addheat()
session.set("name", "coupled_thermal")
session.set("solver type", "steady state")

# 配置材料热属性（硅）
session.set("thermal conductivity", 150)  # 硅的热导率
session.set("heat capacity", 700)  # 硅的热容
session.set("density", 2329)  # 硅的密度

# 配置热源来自电学仿真
session.set("heat source type", "from electrical")
session.set("electrical solver", "drift diffusion")
session.set("coupling type", "two-way")  # 双向耦合

# 配置高级求解器设置
session.set("solver", "iterative")
session.set("tolerance", 1e-8)
session.set("max iterations", 5000)
session.set("preconditioner", "amg")  # 代数多重网格
```

## 注意事项

1. **材料数据**：准确的材料热属性对结果准确性至关重要
2. **边界条件**：合理的边界条件设置对温度分布有显著影响
3. **网格分辨率**：热梯度大的区域需要更细的网格
4. **收敛性**：非线性问题可能需要调整求解器参数
5. **计算资源**：三维瞬态热分析需要大量计算资源

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 不支持
- **DEVICE**: 支持
- **INTERCONNECT**: 不支持

## 相关命令

- `addthermal` - 添加热监视器
- `addefdtd` - 添加电-热 FDTD 求解器
- `addchar` - 添加特性分析
- `set` - 设置对象属性
- `getthermal` - 获取热场数据
- `solve` - 执行求解

## 错误处理

### 常见错误
1. **收敛失败**: 非线性热问题可能不收敛
   - 解决方案：增加最大迭代次数或放松收敛容差
   
2. **材料属性缺失**: 未定义材料热属性
   - 解决方案：确保所有材料都定义了热导率、热容和密度
   
3. **不稳定求解**: 瞬态仿真时间步长太大
   - 解决方案：减小时间步长或使用自动时间步长

### Python 错误处理
```python
import lumapi

try:
    device = lumapi.DEVICE()
    device.addheat()
    
    # 配置求解器
    device.set("solver type", "steady state")
    device.set("x span", 10e-6)
    device.set("heat source power", 0.1)
    # ... 其他设置
    
    # 运行仿真
    device.run()
    
except RuntimeError as e:
    print(f"热求解器错误: {e}")
    # 检查边界条件和材料属性
except MemoryError as e:
    print(f"内存不足: {e}")
    # 建议减小网格密度
except Exception as e:
    print(f"未知错误: {e}")
```

## 版本历史
| 版本 | 修改 |
|------|------|
| DEVICE 2020a | 新增热求解器 |
| DEVICE 2021a | 增强瞬态热分析 |
| DEVICE 2022a | 改进材料数据库集成 |

## 参考
1. Lumerical DEVICE 用户手册 - 热分析章节
2. Lumerical 知识库: 热管理仿真最佳实践
3. Lumerical 论坛: 热耦合仿真讨论

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*