# addfdtd

## 概述

`addfdtd` 命令用于在 FDTD Solutions 仿真中添加一个 FDTD 求解器区域。该命令定义了仿真区域的空间范围、边界条件、网格设置和其他 FDTD 求解器参数。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addfdtd;
```

### Python API (Lumapi)
```python
session.addfdtd()
```

## 参数

`addfdtd` 命令没有直接参数，但需要通过后续的 `set` 命令配置求解器属性。

## 配置属性

添加 FDTD 求解器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 仿真区域中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 仿真区域跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `dimension` | string | "3D" | 仿真维度："3D" 或 "2D" |

### 2. 边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x min bc`, `x max bc` | string | "PML" | X 方向边界条件 |
| `y min bc`, `y max bc` | string | "PML" | Y 方向边界条件 |
| `z min bc`, `z max bc` | string | "PML" | Z 方向边界条件 |
| `pml layers` | int | 8 | PML 层数 |
| `pml type` | string | "standard" | PML 类型 |

### 3. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh accuracy` | int | 2 | 网格精度 (1-8) |
| `mesh type` | string | "auto non-uniform" | 网格类型 |
| `min mesh step` | float | 1e-12 | 最小网格步长 (m) |
| `max mesh step` | float | 1e-6 | 最大网格步长 (m) |
| `dx`, `dy`, `dz` | float | 自动计算 | 网格步长 (m) |

### 4. 仿真设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `simulation time` | float | 1000e-15 | 仿真时间 (s) |
| `auto shutoff min` | float | 1e-5 | 自动停止阈值 |
| `background index` | float | 1.0 | 背景折射率 |
| `simulation temperature` | float | 300 | 仿真温度 (K) |

## 返回值

`addfdtd` 命令没有返回值。成功执行后，会在仿真中添加一个 FDTD 求解器对象。

## 示例

### 示例 1: 基本 FDTD 求解器设置

#### LSF 脚本
```lumerical
// 添加 FDTD 求解器
addfdtd;

// 设置几何参数
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 2e-6);
set("y span", 2e-6);
set("z span", 2e-6);

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");
set("z min bc", "PML");
set("z max bc", "PML");
set("pml layers", 10);

// 设置网格
set("mesh accuracy", 3);
set("mesh type", "auto non-uniform");

// 设置仿真时间
set("simulation time", 500e-15);
set("auto shutoff min", 1e-5);
```

#### Python API
```python
import lumapi

# 创建 FDTD 会话
fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd()

# 设置几何参数
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 2e-6)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)

# 设置边界条件
fdtd.set("x min bc", "PML")
fdtd.set("x max bc", "PML")
fdtd.set("y min bc", "PML")
fdtd.set("y max bc", "PML")
fdtd.set("z min bc", "PML")
fdtd.set("z max bc", "PML")
fdtd.set("pml layers", 10)

# 设置网格
fdtd.set("mesh accuracy", 3)
fdtd.set("mesh type", "auto non-uniform")

# 设置仿真时间
fdtd.set("simulation time", 500e-15)
fdtd.set("auto shutoff min", 1e-5)
```

### 示例 2: 使用对称边界条件

#### LSF 脚本
```lumerical
addfdtd;
set("x span", 1e-6);
set("y span", 1e-6);
set("z span", 1e-6);

// 使用对称边界条件减少计算量
set("x min bc", "Symmetric");
set("x max bc", "PML");
set("y min bc", "Symmetric");
set("y max bc", "PML");
set("z min bc", "Symmetric");
set("z max bc", "PML");

// 强制对称网格
set("force symmetric x mesh", 1);
set("force symmetric y mesh", 1);
set("force symmetric z mesh", 1);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addfdtd()
fdtd.set("x span", 1e-6)
fdtd.set("y span", 1e-6)
fdtd.set("z span", 1e-6)

# 使用对称边界条件减少计算量
fdtd.set("x min bc", "Symmetric")
fdtd.set("x max bc", "PML")
fdtd.set("y min bc", "Symmetric")
fdtd.set("y max bc", "PML")
fdtd.set("z min bc", "Symmetric")
fdtd.set("z max bc", "PML")

# 强制对称网格
fdtd.set("force symmetric x mesh", 1)
fdtd.set("force symmetric y mesh", 1)
fdtd.set("force symmetric z mesh", 1)
```

### 示例 3: 2D 仿真设置

#### LSF 脚本
```lumerical
addfdtd;
set("dimension", "2D");
set("x span", 2e-6);
set("y span", 1e-6);
set("z span", 0);  // 2D 仿真 Z 方向跨度为 0

// 2D 仿真只需要设置 X 和 Y 方向的边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");

// 设置 2D 网格
set("mesh cells x", 200);
set("mesh cells y", 100);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addfdtd()
fdtd.set("dimension", "2D")
fdtd.set("x span", 2e-6)
fdtd.set("y span", 1e-6)
fdtd.set("z span", 0)  # 2D 仿真 Z 方向跨度为 0

# 2D 仿真只需要设置 X 和 Y 方向的边界条件
fdtd.set("x min bc", "PML")
fdtd.set("x max bc", "PML")
fdtd.set("y min bc", "PML")
fdtd.set("y max bc", "PML")

# 设置 2D 网格
fdtd.set("mesh cells x", 200)
fdtd.set("mesh cells y", 100)
```

### 示例 4: 高级网格设置

#### LSF 脚本
```lumerical
addfdtd;
set("x span", 3e-6);
set("y span", 2e-6);
set("z span", 1e-6);

// 自定义网格设置
set("define x mesh by", "maximum mesh step");
set("define y mesh by", "maximum mesh step");
set("define z mesh by", "maximum mesh step");
set("dx", 10e-9);  // X 方向最大网格步长 10nm
set("dy", 10e-9);  // Y 方向最大网格步长 10nm
set("dz", 20e-9);  // Z 方向最大网格步长 20nm

// 设置网格细化区域
set("override mesh", 1);
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addfdtd()
fdtd.set("x span", 3e-6)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 自定义网格设置
fdtd.set("define x mesh by", "maximum mesh step")
fdtd.set("define y mesh by", "maximum mesh step")
fdtd.set("define z mesh by", "maximum mesh step")
fdtd.set("dx", 10e-9)  # X 方向最大网格步长 10nm
fdtd.set("dy", 10e-9)  # Y 方向最大网格步长 10nm
fdtd.set("dz", 20e-9)  # Z 方向最大网格步长 20nm

# 设置网格细化区域
fdtd.set("override mesh", 1)
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)
```

## 注意事项

### 1. 仿真区域大小
- 仿真区域应足够大以包含所有结构和避免边界反射影响
- 通常需要在结构周围留出至少半个波长的缓冲区
- PML 层会增加仿真区域的实际大小

### 2. 网格设置
- 网格精度影响仿真精度和计算时间
- 对于精细结构，需要设置足够小的网格步长
- 可以使用非均匀网格在关键区域细化网格

### 3. 边界条件选择
- **PML**: 吸收边界条件，适合大多数情况
- **Metal**: 完美电导体边界
- **Periodic**: 周期性边界条件
- **Symmetric/Anti-symmetric**: 对称边界条件，可减少计算量

### 4. 仿真时间
- 仿真时间应足够长以使场完全衰减
- `auto shutoff min` 参数可自动停止仿真当能量衰减到阈值以下
- 过长的仿真时间会增加计算成本

### 5. 内存要求
FDTD 仿真内存使用与网格细胞数成正比：
```
内存 ≈ Nx × Ny × Nz × (数据类型大小) × (场分量数)
```
其中 Nx, Ny, Nz 是网格细胞数。

## 错误处理

### 常见错误
1. **内存不足**: 网格太密或仿真区域太大
   - 解决方案：减小网格密度或仿真区域
   
2. **不稳定仿真**: 时间步长太大
   - 解决方案：减小网格步长或使用更小的 CFL 数
   
3. **边界反射**: PML 设置不当
   - 解决方案：增加 PML 层数或调整 PML 参数

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addfdtd()
    
    # 配置求解器
    fdtd.set("x span", 2e-6)
    # ... 其他设置
    
except Exception as e:
    print(f"FDTD 求解器设置失败: {e}")
    # 处理错误
```

## 相关命令

- `addmesh`: 添加局部网格覆盖区
- `addvarfdtd`: 添加变分 FDTD 求解器
- `addefdtd`: 添加电-热 FDTD 求解器
- `setglobalmonitor`: 设置全局监视器
- `setglobalsource`: 设置全局源

## 产品支持

- **主要支持**: FDTD Solutions
- **可选支持**: MODE Solutions (部分功能)
- **不支持**: DEVICE, INTERCONNECT

## 版本历史

| 版本 | 修改 |
|------|------|
| FDTD 2020a | 新增 `auto shutoff min` 参数 |
| FDTD 2019a | 改进 PML 性能 |
| FDTD 2018a | 新增对称边界条件支持 |

## 参考

1. Lumerical FDTD Solutions 用户手册
2. Lumerical 知识库: FDTD 求解器设置最佳实践
3. Lumerical 论坛: FDTD 仿真技巧

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*