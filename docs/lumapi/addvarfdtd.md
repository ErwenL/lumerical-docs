# addvarfdtd

## 概述

`addvarfdtd` 命令用于添加变分时域有限差分（varFDTD）求解器。varFDTD 是 Lumerical 的一种高效仿真技术，特别适用于参数扫描和优化问题。它通过计算场对设计参数的导数，可以在单次仿真中获取多个参数点的响应，极大提高参数扫描效率。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addvarfdtd;
```

### Python API (Lumapi)
```python
session.addvarfdtd()
```

## 参数

`addvarfdtd` 命令没有直接参数，但需要通过后续的 `set` 命令配置求解器类型、参数空间和仿真设置。

## 配置属性

添加 varFDTD 求解器后，可以使用 `set` 命令配置以下属性：

### 1. 基本求解器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "varFDTD" | 求解器名称 |
| `enabled` | bool | true | 是否启用求解器 |
| `solver type` | string | "3D" | 求解器类型："3D", "2D", "quasi-3D" |
| `dimension` | int | 3 | 空间维度 |
| `background index` | float | 1.0 | 背景折射率 |
| `simulation time` | float | 1000e-15 | 仿真时间 (s) |
| `time step` | float | 自动计算 | 时间步长 (s) |

### 2. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh type` | string | "auto" | 网格类型："auto", "uniform", "non-uniform", "conformal" |
| `mesh accuracy` | int | 2 | 网格精度 (1-5) |
| `dx`, `dy`, `dz` | float | λ/20 | 网格尺寸 (m) |
| `min mesh step` | float | λ/100 | 最小网格步长 (m) |
| `max mesh step` | float | λ/10 | 最大网格步长 (m) |
| `mesh refinement` | int | 3 | 网格细化次数 |
| `conformal mesh` | bool | true | 是否使用共形网格 |

### 3. 边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `boundary conditions` | string | "PML" | 边界条件类型："PML", "metal", "periodic", "symmetric" |
| `pml layers` | int | 8 | PML 层数 |
| `pml thickness` | float | λ | PML 厚度 (m) |
| `pml polynomial` | int | 3 | PML 多项式阶数 |
| `pml reflection` | float | 1e-12 | PML 反射系数目标 |
| `symmetry` | string | "none" | 对称性："none", "x-symmetry", "y-symmetry", "z-symmetry" |

### 4. 变分参数设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parameter names` | array | [] | 变分参数名称列表 |
| `parameter types` | array | [] | 参数类型："geometric", "material", "source" |
| `parameter ranges` | matrix | [] | 参数范围矩阵 [min, max] |
| `parameter values` | array | [] | 参数当前值 |
| `sensitivity order` | int | 1 | 灵敏度计算阶数 (1 或 2) |
| `adjoint method` | bool | true | 是否使用伴随方法 |

### 5. 几何参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `geometric parameters` | dict | {} | 几何参数字典 |
| `parameterization method` | string | "direct" | 参数化方法："direct", "bezier", "spline", "levelset" |
| `control points` | int | 10 | 控制点数 |
| `smoothness` | float | 0.1 | 平滑度参数 |

### 6. 材料参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material parameters` | dict | {} | 材料参数字典 |
| `material model` | string | "constant" | 材料模型："constant", "linear", "quadratic" |
| `dispersion model` | string | "none" | 色散模型 |
| `nonlinear effects` | bool | false | 是否考虑非线性效应 |

### 7. 光源设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `source type` | string | "mode" | 光源类型："mode", "gaussian", "plane wave", "dipole" |
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `bandwidth` | float | 0.1 | 带宽（相对值） |
| `polarization` | string | "TE" | 偏振："TE", "TM", "circular", "elliptical" |
| `injection axis` | string | "x" | 注入方向 |
| `offset` | float | 0 | 光源偏移 (m) |

### 8. 监视器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `monitor type` | string | "frequency" | 监视器类型："frequency", "time", "mode expansion" |
| `frequency points` | int | 1 | 频率点数 |
| `frequency range` | vector | [f0, f0] | 频率范围 [min, max] (Hz) |
| `monitor positions` | array | [] | 监视器位置列表 |
| `field components` | array | ["Ex", "Ey", "Ez"] | 场分量列表 |

### 9. 灵敏度分析
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `sensitivity analysis` | bool | true | 是否进行灵敏度分析 |
| `objective function` | string | "transmission" | 目标函数："transmission", "reflection", "absorption", "custom" |
| `gradient method` | string | "adjoint" | 梯度计算方法："adjoint", "finite difference", "complex step" |
| `hessian method` | string | "none" | 海森矩阵计算方法 |
| `tolerance` | float | 1e-6 | 容差 |

### 10. 优化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `optimization enabled` | bool | false | 是否启用优化 |
| `optimization algorithm` | string | "gradient descent" | 优化算法 |
| `max iterations` | int | 100 | 最大迭代次数 |
| `step size` | float | 0.01 | 步长 |
| `constraints` | dict | {} | 约束条件 |

### 11. 并行计算
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parallel computing` | bool | false | 是否启用并行计算 |
| `num processes` | int | 1 | 进程数 |
| `distribution method` | string | "parameter" | 分布方法："parameter", "frequency", "task" |
| `shared memory` | bool | true | 是否使用共享内存 |

### 12. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `advanced options` | bool | false | 是否启用高级选项 |
| `subpixel smoothing` | bool | true | 是否使用子像素平滑 |
| `material averaging` | string | "standard" | 材料平均方法 |
| `stability factor` | float | 0.99 | 稳定性因子 |
| `courant number` | float | 0.99 | Courant 数 |

## 返回值

`addvarfdtd` 命令没有返回值。成功执行后，会在仿真中添加一个变分 FDTD 求解器对象。

## 示例

### 示例 1：基本 varFDTD 设置
```python
import lumapi

session = lumapi.varFDTD()

# 添加 varFDTD 求解器
session.addvarfdtd()
session.set("name", "varfdtd_solver")

# 配置基本仿真参数
session.set("background index", 1.44)  # SiO₂ 背景
session.set("simulation time", 500e-15)  # 500 fs
session.set("mesh accuracy", 3)

# 配置边界条件
session.set("boundary conditions", "PML")
session.set("pml layers", 10)
session.set("pml thickness", 0.5e-6)  # 0.5 μm PML

# 配置光源
session.set("source type", "mode")
session.set("wavelength", 1.55e-6)  # 1550 nm
session.set("polarization", "TE")

# 配置监视器
session.set("monitor type", "frequency")
session.set("frequency points", 1001)
session.set("frequency range", [180e12, 220e12])  # 180-220 THz
```

### 示例 2：几何参数扫描
```python
import lumapi
import numpy as np

session = lumapi.varFDTD()

# 添加 varFDTD 求解器
session.addvarfdtd()

# 定义变分参数（波导宽度和高度）
session.set("parameter names", ["width", "height"])
session.set("parameter types", ["geometric", "geometric"])

# 设置参数范围
session.set("parameter ranges", [[0.3e-6, 0.8e-6],  # width: 300-800 nm
                                 [0.2e-6, 0.3e-6]]) # height: 200-300 nm

# 设置参数初始值
session.set("parameter values", [0.5e-6, 0.22e-6])  # 500 nm × 220 nm

# 创建参数化波导结构
# 宽度和高度将作为变分参数自动调整
session.addrect()
session.set("name", "waveguide")
session.set("x span", "width")  # 使用参数名称
session.set("y span", "height")
session.set("z span", 10e-6)  # 10 μm 长度
session.set("material", "Si (Silicon)")

# 配置灵敏度分析
session.set("sensitivity analysis", True)
session.set("sensitivity order", 1)
session.set("adjoint method", True)
session.set("objective function", "transmission")

# 配置优化设置
session.set("optimization enabled", True)
session.set("optimization algorithm", "gradient descent")
session.set("max iterations", 50)
session.set("step size", 0.1)

# 添加目标（最大化传输）
session.set("target transmission", 0.95)  # 目标传输率 95%

# 运行参数扫描
print("Running varFDTD parameter sweep...")
session.run()

# 获取灵敏度结果
sensitivities = session.getdata("varfdtd_solver", "sensitivities")
print(f"Sensitivity dT/dwidth: {sensitivities['dT_dwidth']}")
print(f"Sensitivity dT/dheight: {sensitivities['dT_dheight']}")
```

### 示例 3：多参数优化
```python
import lumapi

session = lumapi.varFDTD()

# 添加 varFDTD 求解器
session.addvarfdtd()

# 定义多个设计参数
parameters = {
    "wg_width": {"type": "geometric", "min": 0.4e-6, "max": 0.8e-6, "initial": 0.5e-6},
    "wg_height": {"type": "geometric", "min": 0.2e-6, "max": 0.3e-6, "initial": 0.22e-6},
    "gap": {"type": "geometric", "min": 0.1e-6, "max": 0.5e-6, "initial": 0.2e-6},
    "si_index": {"type": "material", "min": 3.4, "max": 3.6, "initial": 3.48},
    "oxide_index": {"type": "material", "min": 1.44, "max": 1.46, "initial": 1.45}
}

# 配置参数
param_names = list(parameters.keys())
param_types = [params["type"] for params in parameters.values()]
param_ranges = [[params["min"], params["max"]] for params in parameters.values()]
param_values = [params["initial"] for params in parameters.values()]

session.set("parameter names", param_names)
session.set("parameter types", param_types)
session.set("parameter ranges", param_ranges)
session.set("parameter values", param_values)

# 创建定向耦合器结构
# 下波导
session.addrect()
session.set("name", "waveguide_bottom")
session.set("x span", "wg_width")
session.set("y span", "wg_height")
session.set("y", "-gap/2 - wg_height/2")  # 使用参数表达式
session.set("z span", 20e-6)
session.set("index", "si_index")  # 使用材料参数

# 上波导
session.addrect()
session.set("name", "waveguide_top")
session.set("x span", "wg_width")
session.set("y span", "wg_height")
session.set("y", "gap/2 + wg_height/2")  # 使用参数表达式
session.set("z span", 20e-6)
session.set("index", "si_index")

# 衬底
session.addrect()
session.set("name", "substrate")
session.set("x span", 5e-6)
session.set("y span", 2e-6)
session.set("y", 0)
session.set("z span", 20e-6)
session.set("material", "SiO2")
session.set("index", "oxide_index")  # 使用材料参数

# 配置高级变分设置
session.set("sensitivity order", 2)  # 计算二阶导数（海森矩阵）
session.set("adjoint method", True)
session.set("gradient method", "adjoint")

# 配置优化（最大化耦合效率）
session.set("optimization enabled", True)
session.set("optimization algorithm", "BFGS")  # 拟牛顿法
session.set("max iterations", 100)
session.set("constraints", {
    "wg_width >= 0.4e-6": True,
    "gap >= 0.1e-6": True,
    "si_index <= 3.6": True
})

# 定义多目标函数（同时优化传输和耦合）
objective_script = """
# 多目标：最大化通过端口的传输，最小化反射
T_through = transmission("output_through")
T_cross = transmission("output_cross")
R = reflection("input")

# 加权目标函数
weight_through = 0.7
weight_cross = 0.3
weight_reflection = 0.1

objective = (weight_through * T_through + 
             weight_cross * T_cross - 
             weight_reflection * R)

return objective
"""

session.set("custom objective", objective_script)

# 配置并行计算
session.set("parallel computing", True)
session.set("num processes", 4)
session.set("distribution method", "parameter")
```

### 示例 4：拓扑优化
```python
import lumapi
import numpy as np

session = lumapi.varFDTD()

# 添加 varFDTD 求解器
session.addvarfdtd()

# 配置拓扑优化
session.set("name", "topology_optimization")
session.set("parameterization method", "levelset")  # 使用水平集方法
session.set("control points", 100)  # 100 个控制点
session.set("smoothness", 0.2)  # 中等平滑度

# 定义设计区域
session.addrect()
session.set("name", "design_region")
session.set("x span", 3e-6)
session.set("y span", 3e-6)
session.set("z span", 0.22e-6)
session.set("material", "design_material")

# 配置材料插值（SIMP 方法）
session.set("material interpolation", "SIMP")  # Solid Isotropic Material with Penalization
session.set("penalization power", 3.0)  # SIMP 惩罚因子
session.set("minimum density", 0.001)  # 最小密度（避免奇异性）
session.set("filter radius", 0.2e-6)  # 过滤半径（确保可制造性）

# 配置变分参数（密度场）
# 创建密度网格
nx, ny = 30, 30  # 30×30 设计网格
density = np.ones((nx, ny)) * 0.5  # 初始密度 0.5

session.set("density field", density.tolist())
session.set("parameter names", [f"density_{i}_{j}" for i in range(nx) for j in range(ny)])
session.set("parameter types", ["material"] * (nx * ny))
session.set("parameter ranges", [[0.001, 1.0]] * (nx * ny))

# 配置灵敏度分析（用于拓扑优化）
session.set("sensitivity analysis", True)
session.set("sensitivity order", 1)
session.set("adjoint method", True)

# 配置优化算法（MMA：移动渐近线法）
session.set("optimization enabled", True)
session.set("optimization algorithm", "MMA")  # Method of Moving Asymptotes
session.set("max iterations", 200)
session.set("move limit", 0.2)  # 移动限制
session.set("optimality tolerance", 1e-4)

# 定义约束（体积分数约束）
session.set("volume fraction", 0.5)  # 材料体积分数不超过 50%

# 配置目标函数（最大化某方向的传输）
session.set("objective function", "custom")
objective = """
# 计算目标：输出端口的传输
E_out = getelectric("output_monitor")
P_out = sum(abs(E_out)**2)

# 计算输入端口的输入功率
E_in = getelectric("input_monitor")  
P_in = sum(abs(E_in)**2)

# 传输效率
transmission = P_out / P_in

# 添加正则化项（避免棋盘格现象）
density = getdata("design_region", "density")
grad_x = np.gradient(density, axis=0)
grad_y = np.gradient(density, axis=1)
regularization = 0.01 * np.sum(grad_x**2 + grad_y**2)

# 最终目标（最大化传输，最小化正则化）
return transmission - regularization
"""

session.set("custom objective script", objective)

# 配置监视器和可视化
session.set("monitor density evolution", True)
session.set("save iteration data", True)
session.set("visualization interval", 10)  # 每 10 次迭代可视化一次

# 配置高级求解器设置
session.set("advanced options", True)
session.set("subpixel smoothing", True)
session.set("material averaging", "harmonic")  # 谐波平均，适合拓扑优化
```

## 注意事项

1. **参数可微性**：变分参数必须是连续可微的，否则灵敏度计算可能不准确
2. **网格依赖性**：varFDTD 结果可能依赖于网格设置，需要进行网格收敛性分析
3. **计算成本**：虽然 varFDTD 比传统参数扫描高效，但计算量仍可能很大
4. **数值稳定性**：高阶灵敏度计算可能数值不稳定，需要适当调整容差
5. **内存使用**：存储灵敏度信息可能增加内存使用
6. **并行效率**：参数并行可能受限于通信开销，合理选择并行策略
7. **优化收敛**：复杂优化问题可能收敛到局部最优，需要多次尝试不同初始值
8. **物理合理性**：优化结果应检查物理合理性（如最小特征尺寸）

## 产品支持

- **FDTD Solutions**: 不支持（使用标准 FDTD）
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **varFDTD**: 支持（主要应用）

## 相关命令

- `addfdtd` - 添加标准 FDTD 求解器
- `set` - 设置 varFDTD 属性
- `getvarfdtd` - 获取 varFDTD 结果
- `run` - 运行 varFDTD 仿真
- `optimize` - 运行优化
- `sensitivity` - 计算灵敏度

## 错误处理

### 常见错误
1. **内存不足**: 变分 FDTD 需要存储灵敏度矩阵，内存需求较大
   - 解决方案：减少参数数量或使用稀疏存储
   
2. **参数不可微**: 参数不连续导致灵敏度计算失败
   - 解决方案：确保参数化方法连续可微
   
3. **优化不收敛**: 优化算法无法找到可行解
   - 解决方案：调整初始值、约束条件或优化算法参数

### Python 错误处理
```python
import lumapi

try:
    varfdtd = lumapi.varFDTD()
    varfdtd.addvarfdtd()
    
    # 配置求解器
    varfdtd.set("parameter names", ["width", "height"])
    varfdtd.set("parameter ranges", [[0.3e-6, 0.8e-6], [0.2e-6, 0.3e-6]])
    # ... 其他设置
    
    # 运行仿真
    varfdtd.run()
    
except MemoryError as e:
    print(f"内存不足: {e}")
    # 建议减少参数或使用更粗网格
except RuntimeError as e:
    print(f"运行时错误: {e}")
    # 检查参数设置
except Exception as e:
    print(f"未知错误: {e}")
```

## 版本历史
| 版本 | 修改 |
|------|------|
| varFDTD 2021a | 新增变分 FDTD 求解器 |
| varFDTD 2022a | 增加拓扑优化支持 |
| varFDTD 2023a | 改进并行计算性能 |

## 参考
1. Lumerical varFDTD 用户手册
2. Lumerical 知识库: 变分 FDTD 最佳实践
3. Lumerical 论坛: 参数优化讨论

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*