# addprofile

## 概述

`addprofile` 命令用于在仿真中添加场监视器。场监视器记录电磁场（电场 E 和磁场 H）的空间分布，是分析场模式、场强分布、偏振特性等关键物理量的基础工具。该命令支持多种监视器类型（点、线、面、体积），可以记录频域或时域场数据。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addprofile;
```

### Python API (Lumapi)
```python
session.addprofile()
```

## 参数

`addprofile` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加场监视器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "profile" | 监视器名称 |
| `x`, `y`, `z` | float | 0 | 监视器中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 监视器各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 监视器 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 监视器 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 监视器 Z 方向最小/最大坐标 (m) |

### 2. 监视器类型与方向
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `monitor type` | string | "2D X-normal" | 监视器类型 |
| `normal direction` | string | "x" | 法线方向："x", "y", "z" |
| `dimension` | string | "3D" | 维度："3D", "2D", "1D", "0D" |

### 监视器类型选项：
- **体积监视器**: `"3D"`, `"volume"`
- **平面监视器**: `"2D X-normal"`, `"2D Y-normal"`, `"2D Z-normal"`
- **线监视器**: `"1D X-line"`, `"1D Y-line"`, `"1D Z-line"`
- **点监视器**: `"0D"`, `"point"`

### 3. 场分量记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record E` | int | 0 | 是否记录电场 (0/1) |
| `record Ex` | int | 0 | 是否记录 Ex 分量 (0/1) |
| `record Ey` | int | 0 | 是否记录 Ey 分量 (0/1) |
| `record Ez` | int | 0 | 是否记录 Ez 分量 (0/1) |
| `record H` | int | 0 | 是否记录磁场 (0/1) |
| `record Hx` | int | 0 | 是否记录 Hx 分量 (0/1) |
| `record Hy` | int | 0 | 是否记录 Hy 分量 (0/1) |
| `record Hz` | int | 0 | 是否记录 Hz 分量 (0/1) |
| `record E2` | int | 0 | 是否记录电场强度平方 (0/1) |
| `record H2` | int | 0 | 是否记录磁场强度平方 (0/1) |

### 4. 频率/时间设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency points` | int | 1 | 频率点数 |
| `wavelength start` | float | 1.5e-6 | 起始波长 (m) |
| `wavelength stop` | float | 1.6e-6 | 结束波长 (m) |
| `use source limits` | int | 1 | 是否使用光源波长范围 (0/1) |
| `override global monitor settings` | int | 0 | 是否覆盖全局监视器设置 (0/1) |
| `time step` | float | 自动计算 | 时域监视器时间步长 (s) |
| `number of time steps` | int | 1000 | 时域监视器时间步数 |

### 5. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `output Ex` | string | "Ex" | Ex 输出名称 |
| `output Ey` | string | "Ey" | Ey 输出名称 |
| `output Ez` | string | "Ez" | Ez 输出名称 |
| `output Hx` | string | "Hx" | Hx 输出名称 |
| `output Hy` | string | "Hy" | Hy 输出名称 |
| `output Hz` | string | "Hz" | Hz 输出名称 |
| `output E2` | string | "E2" | 电场强度平方输出名称 |
| `output H2` | string | "H2" | 磁场强度平方输出名称 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `spatial interpolation` | string | "none" | 空间插值方法 |
| `frequency interpolation` | string | "linear" | 频率插值方法 |
| `down sample X` | int | 1 | X 方向下采样因子 |
| `down sample Y` | int | 1 | Y 方向下采样因子 |
| `down sample Z` | int | 1 | Z 方向下采样因子 |
| `down sample T` | int | 1 | 时间下采样因子 |
| `subgrid interpolation` | int | 0 | 是否使用亚网格插值 (0/1) |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.0, 1.0, 0.0, 0.3] | RGBA 颜色值（绿色半透明） |
| `alpha` | float | 0.3 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addprofile` 命令没有返回值。成功执行后，会在仿真中添加一个场监视器对象。

## 示例

### 示例 1: 基本场监视器（平面电场分布）

#### LSF 脚本
```lumerical
// 添加场监视器
addprofile;

// 设置几何参数
set("name", "field_monitor");
set("x", 0);          // 中心位置
set("y", 0);
set("z", 0);
set("x span", 10e-6);  // 覆盖整个器件区域
set("y span", 4e-6);
set("z span", 2e-6);

// 设置监视器类型
set("monitor type", "2D Z-normal");
set("normal direction", "z");  // Z 方向平面

// 设置场记录选项
set("record E", 1);      // 记录总电场
set("record Ex", 1);     // 记录 Ex 分量
set("record Ey", 1);     // 记录 Ey 分量
set("record Ez", 0);     // 不记录 Ez（平面内分量）

// 使用光源波长范围
set("use source limits", 1);
set("frequency points", 50);  // 50个频率点

// 设置输出名称
set("output Ex", "Ex_plane");
set("output Ey", "Ey_plane");

// 设置显示属性
set("color", [0.0, 1.0, 0.0, 0.3]);  // 绿色半透明
set("alpha", 0.3);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加场监视器
fdtd.addprofile()

# 设置几何参数
fdtd.set("name", "field_monitor")
fdtd.set("x", 0)          # 中心位置
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)  # 覆盖整个器件区域
fdtd.set("y span", 4e-6)
fdtd.set("z span", 2e-6)

# 设置监视器类型
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("normal direction", "z")  # Z 方向平面

# 设置场记录选项
fdtd.set("record E", 1)      # 记录总电场
fdtd.set("record Ex", 1)     # 记录 Ex 分量
fdtd.set("record Ey", 1)     # 记录 Ey 分量
fdtd.set("record Ez", 0)     # 不记录 Ez（平面内分量）

# 使用光源波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 50)  # 50个频率点

# 设置输出名称
fdtd.set("output Ex", "Ex_plane")
fdtd.set("output Ey", "Ey_plane")

# 设置显示属性
fdtd.set("color", [0.0, 1.0, 0.0, 0.3])  # 绿色半透明
fdtd.set("alpha", 0.3)
```

### 示例 2: 体积场监视器（3D 场分布）

#### LSF 脚本
```lumerical
addprofile;
set("name", "volume_field");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 8e-6);
set("y span", 4e-6);
set("z span", 2e-6);

// 体积监视器
set("monitor type", "3D");
set("dimension", "3D");

// 记录所有场分量
set("record E", 1);      // 记录电场
set("record Ex", 1);
set("record Ey", 1);
set("record Ez", 1);
set("record H", 1);      // 记录磁场
set("record Hx", 1);
set("record Hy", 1);
set("record Hz", 1);

// 设置波长范围
set("override global monitor settings", 1);
set("wavelength start", 1.5e-6);
set("wavelength stop", 1.6e-6);
set("frequency points", 20);  // 减少频率点以控制数据量

// 设置输出名称
set("output Ex", "Ex_vol");
set("output Ey", "Ey_vol");
set("output Ez", "Ez_vol");
set("output Hx", "Hx_vol");
set("output Hy", "Hy_vol");
set("output Hz", "Hz_vol");

// 下采样以减少数据量
set("down sample X", 2);
set("down sample Y", 2);
set("down sample Z", 2);

// 显示属性
set("color", [0.0, 0.5, 1.0, 0.15]);  // 蓝色半透明
set("alpha", 0.15);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprofile()
fdtd.set("name", "volume_field")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 8e-6)
fdtd.set("y span", 4e-6)
fdtd.set("z span", 2e-6)

# 体积监视器
fdtd.set("monitor type", "3D")
fdtd.set("dimension", "3D")

# 记录所有场分量
fdtd.set("record E", 1)      # 记录电场
fdtd.set("record Ex", 1)
fdtd.set("record Ey", 1)
fdtd.set("record Ez", 1)
fdtd.set("record H", 1)      # 记录磁场
fdtd.set("record Hx", 1)
fdtd.set("record Hy", 1)
fdtd.set("record Hz", 1)

# 设置波长范围
fdtd.set("override global monitor settings", 1)
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)
fdtd.set("frequency points", 20)  # 减少频率点以控制数据量

# 设置输出名称
fdtd.set("output Ex", "Ex_vol")
fdtd.set("output Ey", "Ey_vol")
fdtd.set("output Ez", "Ez_vol")
fdtd.set("output Hx", "Hx_vol")
fdtd.set("output Hy", "Hy_vol")
fdtd.set("output Hz", "Hz_vol")

# 下采样以减少数据量
fdtd.set("down sample X", 2)
fdtd.set("down sample Y", 2)
fdtd.set("down sample Z", 2)

# 显示属性
fdtd.set("color", [0.0, 0.5, 1.0, 0.15])  # 蓝色半透明
fdtd.set("alpha", 0.15)
```

### 示例 3: 点场监视器与时域记录

#### LSF 脚本
```lumerical
// 点场监视器
addprofile;
set("name", "point_field");
set("x", 2e-6);
set("y", 1e-6);
set("z", 0.5e-6);
set("monitor type", "0D");  // 点监视器

// 记录时域场（FDTD 仿真）
set("record E", 1);
set("record H", 1);
set("frequency points", 1);  // 时域记录不需要多个频率点

// 设置时间参数
set("number of time steps", 2000);
set("time step", 1e-16);  // 时间步长

// 输出名称
set("output Ex", "Ex_point_time");
set("output Ey", "Ey_point_time");
set("output Ez", "Ez_point_time");
set("output Hx", "Hx_point_time");
set("output Hy", "Hy_point_time");
set("output Hz", "Hz_point_time");

// 显示属性
set("color", [1.0, 0.0, 1.0, 0.8]);  // 紫色
set("alpha", 0.8);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprofile()
fdtd.set("name", "point_field")
fdtd.set("x", 2e-6)
fdtd.set("y", 1e-6)
fdtd.set("z", 0.5e-6)
fdtd.set("monitor type", "0D")  # 点监视器

# 记录时域场（FDTD 仿真）
fdtd.set("record E", 1)
fdtd.set("record H", 1)
fdtd.set("frequency points", 1)  # 时域记录不需要多个频率点

# 设置时间参数
fdtd.set("number of time steps", 2000)
fdtd.set("time step", 1e-16)  # 时间步长

# 输出名称
fdtd.set("output Ex", "Ex_point_time")
fdtd.set("output Ey", "Ey_point_time")
fdtd.set("output Ez", "Ez_point_time")
fdtd.set("output Hx", "Hx_point_time")
fdtd.set("output Hy", "Hy_point_time")
fdtd.set("output Hz", "Hz_point_time")

# 显示属性
fdtd.set("color", [1.0, 0.0, 1.0, 0.8])  # 紫色
fdtd.set("alpha", 0.8)
```

### 示例 4: 多平面场监视器（交叉截面分析）

#### LSF 脚本
```lumerical
// XY 平面（Z=0）
addprofile;
set("name", "field_xy");
set("z", 0);
set("x span", 10e-6);
set("y span", 5e-6);
set("monitor type", "2D Z-normal");
set("record Ex", 1);
set("record Ey", 1);
set("output Ex", "Ex_xy");
set("output Ey", "Ey_xy");
set("color", [1.0, 0.0, 0.0, 0.2]);  // 红色

// XZ 平面（Y=0）
addprofile;
set("name", "field_xz");
set("y", 0);
set("x span", 10e-6);
set("z span", 2e-6);
set("monitor type", "2D Y-normal");
set("record Ex", 1);
set("record Ez", 1);
set("output Ex", "Ex_xz");
set("output Ez", "Ez_xz");
set("color", [0.0, 1.0, 0.0, 0.2]);  // 绿色

// YZ 平面（X=0）
addprofile;
set("name", "field_yz");
set("x", 0);
set("y span", 5e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("record Ey", 1);
set("record Ez", 1);
set("output Ey", "Ey_yz");
set("output Ez", "Ez_yz");
set("color", [0.0, 0.0, 1.0, 0.2]);  // 蓝色

// 设置公共参数
setnamed("field_xy", "use source limits", 1);
setnamed("field_xy", "frequency points", 30);
setnamed("field_xz", "use source limits", 1);
setnamed("field_xz", "frequency points", 30);
setnamed("field_yz", "use source limits", 1);
setnamed("field_yz", "frequency points", 30);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# XY 平面（Z=0）
fdtd.addprofile()
fdtd.set("name", "field_xy")
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)
fdtd.set("y span", 5e-6)
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("record Ex", 1)
fdtd.set("record Ey", 1)
fdtd.set("output Ex", "Ex_xy")
fdtd.set("output Ey", "Ey_xy")
fdtd.set("color", [1.0, 0.0, 0.0, 0.2])  # 红色

# XZ 平面（Y=0）
fdtd.addprofile()
fdtd.set("name", "field_xz")
fdtd.set("y", 0)
fdtd.set("x span", 10e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D Y-normal")
fdtd.set("record Ex", 1)
fdtd.set("record Ez", 1)
fdtd.set("output Ex", "Ex_xz")
fdtd.set("output Ez", "Ez_xz")
fdtd.set("color", [0.0, 1.0, 0.0, 0.2])  # 绿色

# YZ 平面（X=0）
fdtd.addprofile()
fdtd.set("name", "field_yz")
fdtd.set("x", 0)
fdtd.set("y span", 5e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("record Ey", 1)
fdtd.set("record Ez", 1)
fdtd.set("output Ey", "Ey_yz")
fdtd.set("output Ez", "Ez_yz")
fdtd.set("color", [0.0, 0.0, 1.0, 0.2])  # 蓝色

# 设置公共参数
fdtd.set("use source limits", 1, "field_xy")
fdtd.set("frequency points", 30, "field_xy")
fdtd.set("use source limits", 1, "field_xz")
fdtd.set("frequency points", 30, "field_xz")
fdtd.set("use source limits", 1, "field_yz")
fdtd.set("frequency points", 30, "field_yz")
```

### 示例 5: 线场监视器（沿波导场分布）

#### LSF 脚本
```lumerical
// 沿波导中心线的场分布
addprofile;
set("name", "line_field");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 12e-6);  // 沿 X 方向 12μm
set("y span", 0);      // Y 方向零跨度（线）
set("z span", 0);      // Z 方向零跨度

set("monitor type", "1D X-line");

// 记录主要场分量（波导模式）
set("record Ex", 1);
set("record Ey", 1);
set("record Ez", 1);
set("record Hz", 1);  // TE 模式的 Hz 分量

// 输出名称
set("output Ex", "Ex_line");
set("output Ey", "Ey_line");
set("output Ez", "Ez_line");
set("output Hz", "Hz_line");

// 设置波长范围
set("use source limits", 1);
set("frequency points", 20);

// 显示属性
set("color", [0.5, 0.5, 0.0, 0.6]);  // 黄色
set("alpha", 0.6);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprofile()
fdtd.set("name", "line_field")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 12e-6)  # 沿 X 方向 12μm
fdtd.set("y span", 0)      # Y 方向零跨度（线）
fdtd.set("z span", 0)      # Z 方向零跨度

fdtd.set("monitor type", "1D X-line")

# 记录主要场分量（波导模式）
fdtd.set("record Ex", 1)
fdtd.set("record Ey", 1)
fdtd.set("record Ez", 1)
fdtd.set("record Hz", 1)  # TE 模式的 Hz 分量

# 输出名称
fdtd.set("output Ex", "Ex_line")
fdtd.set("output Ey", "Ey_line")
fdtd.set("output Ez", "Ez_line")
fdtd.set("output Hz", "Hz_line")

# 设置波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 20)

# 显示属性
fdtd.set("color", [0.5, 0.5, 0.0, 0.6])  # 黄色
fdtd.set("alpha", 0.6)
```

## 注意事项

### 1. 监视器类型选择
- **平面监视器**：适用于截面场分析，法线方向应与主要场传播方向垂直
- **体积监视器**：提供完整 3D 场分布，但数据量巨大
- **线监视器**：适用于沿波导或光路的场分布分析
- **点监视器**：适用于特定位置场的时间演化分析

### 2. 场分量选择
- **电场分量**：分析偏振、耦合效率、场强分布
- **磁场分量**：分析模式特性、能量流、磁光效应
- **分量组合**：根据仿真类型选择相关分量（如 TE 模式：Ex, Ey, Hz；TM 模式：Hx, Hy, Ez）

### 3. 数据量与性能优化
- 体积监视器产生海量数据，谨慎使用
- 使用下采样减少数据量
- 只记录必要的场分量
- 频域监视器减少频率点数
- 使用 `override global monitor settings` 控制波长范围

### 4. 数值准确性
- 监视器应远离 PML 边界以避免数值反射
- 网格分辨率影响场采样精度
- 亚网格插值可提高场分布准确性（但增加计算量）

### 5. 后处理与分析
- 场分布可视化：使用 `plot` 或 `image` 命令
- 场强计算：`E_total = sqrt(Ex^2 + Ey^2 + Ez^2)`
- 模式重叠：计算场分布与目标模式的重叠积分
- 偏振分析：分析各电场分量的相对强度和相位

## 错误处理

### 常见错误
1. **监视器位置无效**
   - 解决方案：确保监视器在仿真区域内

2. **数据量过大导致内存不足**
   - 解决方案：减少频率点数、使用下采样、选择部分场分量

3. **场分量记录冲突**
   - 解决方案：`record E=1` 会覆盖 `record Ex/Ey/Ez` 设置，需注意优先级

4. **时域/频域设置不当**
   - 解决方案：FDTD 仿真使用 `number of time steps`，频域仿真使用 `frequency points`

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加场监视器
    fdtd.addprofile()
    
    # 配置监视器属性
    fdtd.set("name", "test_profile")
    fdtd.set("monitor type", "2D X-normal")
    fdtd.set("record E", 1)
    fdtd.set("frequency points", 50)
    
except lumapi.LumApiError as e:
    print(f"场监视器创建失败: {e}")
    
    # 检查具体错误
    if "position" in str(e).lower():
        print("错误: 监视器位置无效")
    elif "memory" in str(e).lower():
        print("错误: 数据量过大，请减少频率点或使用下采样")
    elif "parameter" in str(e).lower():
        print("错误: 参数设置错误")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addpower`: 添加功率监视器
- `addindex`: 添加折射率监视器
- `addmodeexpansion`: 添加模式扩展监视器
- `addtime`: 添加时域监视器
- `setglobalmonitor`: 设置全局监视器参数
- `getresult`: 获取监视器数据
- `getelectric`: 获取电场数据
- `getmagnetic`: 获取磁场数据

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: varFDTD（部分场分量）
- **不支持**: INTERCONNECT, DEVICE

## 应用场景

### 1. 波导模式分析
```python
# 分析波导中的模式场分布
fdtd.addprofile()
fdtd.set("monitor type", "2D X-normal")
fdtd.set("record Ex", 1)
fdtd.set("record Ey", 1)
fdtd.set("record Hz", 1)  # TE 模式
```

### 2. 谐振腔场分布
```python
# 分析光学谐振腔的驻波场
fdtd.addprofile()
fdtd.set("monitor type", "3D")
fdtd.set("record E", 1)
fdtd.set("record H", 1)
fdtd.set("frequency points", 5)  # 多个谐振频率
```

### 3. 近场扫描
```python
# 模拟近场扫描显微镜
fdtd.addprofile()
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("z", 100e-9)  # 距离样品 100nm
fdtd.set("record E", 1)
```

### 4. 时域场演化
```python
# 记录时域场演化
fdtd.addprofile()
fdtd.set("monitor type", "0D")  # 点监视器
fdtd.set("record E", 1)
fdtd.set("record H", 1)
fdtd.set("number of time steps", 5000)
```

## 版本历史

| 版本 | 修改 |
|------|------|
 | Lumerical 2020a | 新增时域场记录支持 |
| Lumerical 2019a | 改进场分量选择逻辑 |
| Lumerical 2018a | 新增点/线监视器类型 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical 监视器设置指南
2. 电磁场理论与仿真方法
3. 光学器件场分布分析方法

---

 *最后更新: 2026-01-31*  
*文档版本: 1.1*