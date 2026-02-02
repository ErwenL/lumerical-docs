# addefdtd

## 概述

`addefdtd` 命令用于在 FDTD Solutions 仿真中添加一个电-热 FDTD 求解器区域。该求解器支持电-热耦合仿真，同时求解电磁场和热场方程，适用于分析电热效应、热光调制器、激光器热管理、光子集成电路的热效应等应用。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addefdtd;
```

### Python API (Lumapi)
```python
session.addefdtd()
```

## 参数

`addefdtd` 命令没有直接参数，但需要通过后续的 `set` 命令配置求解器属性。

## 配置属性

添加电-热 FDTD 求解器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "efdtd" | 求解器名称 |
| `x`, `y`, `z` | float | 0 | 仿真区域中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 仿真区域跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `dimension` | string | "3D" | 仿真维度："3D" 或 "2D" |

### 2. 电磁场设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `background index` | float | 1.0 | 背景折射率 |
| `simulation time` | float | 1000e-15 | 仿真时间 (s) |
| `simulation temperature` | float | 300 | 仿真温度 (K) |
| `simulate heat` | bool | true | 是否仿真热效应 |

### 3. 边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x min bc`, `x max bc` | string | "PML" | X 方向电磁边界条件 |
| `y min bc`, `y max bc` | string | "PML" | Y 方向电磁边界条件 |
| `z min bc`, `z max bc` | string | "PML" | Z 方向电磁边界条件 |
| `thermal x min bc`, `thermal x max bc` | string | "convection" | X 方向热边界条件 |
| `thermal y min bc`, `thermal y max bc` | string | "convection" | Y 方向热边界条件 |
| `thermal z min bc`, `thermal z max bc` | string | "convection" | Z 方向热边界条件 |
| `pml layers` | int | 8 | PML 层数 |
| `convection coefficient` | float | 5 | 对流系数 (W/m²·K) |

### 4. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh accuracy` | int | 2 | 网格精度 (1-8) |
| `mesh type` | string | "auto non-uniform" | 网格类型 |
| `min mesh step` | float | 1e-12 | 最小网格步长 (m) |
| `max mesh step` | float | 1e-6 | 最大网格步长 (m) |
| `dx`, `dy`, `dz` | float | 自动计算 | 网格步长 (m) |
| `thermal mesh accuracy` | int | 2 | 热网格精度 |
| `thermal mesh type` | string | "auto non-uniform" | 热网格类型 |

### 5. 热源设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `heat sources` | matrix | [] | 热源列表 |
| `heat source power` | float | 0 | 热源功率 (W) |
| `heat source frequency` | float | 0 | 热源频率 (Hz) |
| `heat source position` | vector | [0,0,0] | 热源位置 (m) |

### 6. 材料热属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal conductivity` | float | 自动 | 热导率 (W/m·K) |
| `heat capacity` | float | 自动 | 热容 (J/kg·K) |
| `density` | float | 自动 | 密度 (kg/m³) |
| `thermal expansion coefficient` | float | 自动 | 热膨胀系数 (1/K) |

### 7. 求解器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `solver type` | string | "coupled" | 求解器类型："coupled", "sequential" |
| `max coupled iterations` | int | 10 | 最大耦合迭代次数 |
| `coupled tolerance` | float | 1e-3 | 耦合容差 |
| `thermal solver type` | string | "steady state" | 热求解器类型："steady state", "transient" |
| `thermal time steps` | int | 100 | 热时间步数 |
| `thermal time step` | float | 1e-9 | 热时间步长 (s) |

### 8. 监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `monitors` | matrix | [] | 监视器列表 |
| `save fields` | bool | false | 是否保存场数据 |
| `save thermal fields` | bool | false | 是否保存热场数据 |

## 返回值

`addefdtd` 命令没有返回值。成功执行后，会在仿真中添加一个电-热 FDTD 求解器对象。
## 示例

### 示例 1: 基本电-热 FDTD 求解器设置
#### LSF 脚本
```lumerical
// 添加电-热 FDTD 求解器
addefdtd;

// 配置求解器属性
set("name", "electro_thermal_solver");
set("x span", 5e-6);
set("y span", 3e-6);
set("z span", 1e-6);
set("simulation time", 2000e-15);
set("simulate heat", 1);

// 设置热边界条件
set("thermal x min bc", "convection");
set("thermal x max bc", "convection");
set("convection coefficient", 10);
```

#### Python API
```python
import lumapi

# 创建会话
session = lumapi.FDTD()

# 添加电-热 FDTD 求解器
session.addefdtd()

# 配置求解器属性
session.set("name", "electro_thermal_solver")
session.set("x span", 5e-6)
session.set("y span", 3e-6)
session.set("z span", 1e-6)
session.set("simulation time", 2000e-15)
session.set("simulate heat", True)

# 设置热边界条件
session.set("thermal x min bc", "convection")
session.set("thermal x max bc", "convection")
session.set("convection coefficient", 10)
```

### 示例 2: 配置热源和材料属性
#### LSF 脚本
```lumerical
// 添加电-热 FDTD 求解器
addefdtd;

// 设置几何尺寸
set("x span", 10e-6);
set("y span", 5e-6);
set("z span", 2e-6);

// 配置热源
set("heat sources", [[0, 0, 0, 1e-3]]);  // [x, y, z, power]
set("heat source power", 1e-3);  // 1 mW

// 配置材料热属性
set("thermal conductivity", 150);  // 硅的热导率
set("heat capacity", 700);  // 硅的热容
set("density", 2329);  // 硅的密度

// 设置求解器参数
set("solver type", "coupled");
set("max coupled iterations", 15);
set("coupled tolerance", 1e-4);
set("thermal solver type", "steady state");
```

#### Python API
```python
import lumapi

session = lumapi.FDTD()

# 添加电-热 FDTD 求解器
session.addefdtd()

# 设置几何尺寸
session.set("x span", 10e-6)
session.set("y span", 5e-6) 
session.set("z span", 2e-6)

# 配置热源
session.set("heat sources", [[0, 0, 0, 1e-3]])  # [x, y, z, power]
session.set("heat source power", 1e-3)  # 1 mW

# 配置材料热属性
session.set("thermal conductivity", 150)  # 硅的热导率
session.set("heat capacity", 700)  # 硅的热容
session.set("density", 2329)  # 硅的密度

# 设置求解器参数
session.set("solver type", "coupled")
session.set("max coupled iterations", 15)
session.set("coupled tolerance", 1e-4)
session.set("thermal solver type", "steady state")
```

## 注意事项

1. **计算资源**：电-热耦合仿真需要更多计算资源，建议从简单模型开始
2. **收敛性**：耦合仿真可能收敛较慢，需要调整容差和迭代次数
3. **时间尺度**：电磁和热过程的时间尺度差异很大，需要合理设置时间步长
4. **材料数据**：准确的材料热属性数据对结果准确性至关重要
5. **边界条件**：热边界条件对温度分布有显著影响，应根据实际情况设置

## 产品支持

- **FDTD Solutions**: 支持
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 不支持

## 相关命令

- `addfdtd` - 添加标准 FDTD 求解器
- `addheat` - 添加热求解器
- `addthermal` - 添加热监视器
- `set` - 设置对象属性
- `getthermal` - 获取热场数据

## 错误处理

### 常见错误
1. **内存不足**: 电-热耦合仿真需要大量内存，特别是使用精细网格时
   - 解决方案：减少网格密度或使用对称边界条件
   
2. **收敛失败**: 耦合仿真可能无法收敛
   - 解决方案：增加最大耦合迭代次数或放宽容差
   
3. **不稳定仿真**: 时间步长太大导致仿真不稳定
   - 解决方案：减小时间步长或使用自适应时间步长

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addefdtd()
    
    # 配置求解器
    fdtd.set("x span", 5e-6)
    fdtd.set("simulate heat", True)
    # ... 其他设置
    
except MemoryError as e:
    print(f"内存不足: {e}")
    # 建议减小网格密度
except RuntimeError as e:
    print(f"仿真错误: {e}")
    # 检查参数设置
except Exception as e:
    print(f"未知错误: {e}")
```

## 版本历史
| 版本 | 修改 |
|------|------|
| FDTD 2021a | 新增电-热 FDTD 求解器 |
| FDTD 2022a | 改进热边界条件支持 |
| FDTD 2023a | 增强耦合求解器稳定性 |

## 参考
1. Lumerical FDTD Solutions 用户手册 - 电-热耦合仿真章节
2. Lumerical 知识库: 电-热 FDTD 仿真最佳实践
3. Lumerical 论坛: 热管理仿真讨论

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*