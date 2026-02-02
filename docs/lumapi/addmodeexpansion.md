# addmodeexpansion

## 概述

`addmodeexpansion` 命令用于在仿真中添加模式扩展监视器。模式扩展监视器将总电磁场分解为预先定义的模式基组，计算各模式系数、功率耦合效率、模式转换效率等关键参数。该监视器广泛应用于波导耦合分析、多模干涉器件、模式分复用系统等场景。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addmodeexpansion;
```

### Python API (Lumapi)
```python
session.addmodeexpansion()
```

## 参数

`addmodeexpansion` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加模式扩展监视器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "mode expansion" | 监视器名称 |
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
- **平面监视器**: `"2D X-normal"`, `"2D Y-normal"`, `"2D Z-normal"`
- **注意**: 模式扩展监视器通常使用平面监视器

### 3. 模式扩展设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `expansion type` | string | "all" | 扩展类型 |
| `mode selection` | string | "user select" | 模式选择方法 |
| `number of modes` | int | 1 | 模式数量 |
| `mode number` | int | 1 | 特定模式编号 |
| `wavelength` | float | 1.55e-6 | 模式计算波长 (m) |
| `background index` | float | 1.0 | 背景折射率 |
| `use global monitor settings` | int | 1 | 使用全局监视器设置 (0/1) |

### 扩展类型选项：
- `"all"`: 扩展到所有模式
- `"fundamental TE"`: 仅基模 TE 模式
- `"fundamental TM"`: 仅基模 TM 模式
- `"TE"`: 所有 TE 模式
- `"TM"`: 所有 TM 模式
- `"user select"`: 用户选择特定模式

### 4. 端口与模式源设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `source` | string | "" | 模式源名称 |
| `port name` | string | "" | 端口名称 |
| `use source mode` | int | 0 | 使用源模式 (0/1) |
| `injection axis` | string | "x" | 注入轴方向 |
| `direction` | string | "forward" | 模式方向："forward", "backward" |

### 5. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record expansion coefficients` | int | 1 | 是否记录扩展系数 (0/1) |
| `record power` | int | 1 | 是否记录模式功率 (0/1) |
| `record phase` | int | 0 | 是否记录模式相位 (0/1) |
| `record overlap` | int | 0 | 是否记录重叠积分 (0/1) |
| `record E` | int | 0 | 是否记录电场 (0/1) |
| `record H` | int | 0 | 是否记录磁场 (0/1) |
| `record mode profiles` | int | 0 | 是否记录模式剖面 (0/1) |

### 6. 频率/波长设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency points` | int | 1 | 频率点数 |
| `wavelength start` | float | 1.5e-6 | 起始波长 (m) |
| `wavelength stop` | float | 1.6e-6 | 结束波长 (m) |
| `use source limits` | int | 1 | 是否使用光源波长范围 (0/1) |
| `override global monitor settings` | int | 0 | 是否覆盖全局监视器设置 (0/1) |

### 7. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `output a` | string | "a" | 前向模式系数输出名称 |
| `output b` | string | "b" | 后向模式系数输出名称 |
| `output power forward` | string | "power_forward" | 前向功率输出名称 |
| `output power backward` | string | "power_backward" | 后向功率输出名称 |
| `output phase forward` | string | "phase_forward" | 前向相位输出名称 |
| `output phase backward` | string | "phase_backward" | 后向相位输出名称 |
| `output overlap` | string | "overlap" | 重叠积分输出名称 |
| `output mode index` | string | "mode_index" | 模式有效折射率输出名称 |

### 8. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `spatial interpolation` | string | "none" | 空间插值方法 |
| `frequency interpolation` | string | "linear" | 频率插值方法 |
| `down sample X` | int | 1 | X 方向下采样因子 |
| `down sample Y` | int | 1 | Y 方向下采样因子 |
| `down sample Z` | int | 1 | Z 方向下采样因子 |
| `normalization` | string | "power" | 归一化方法："power", "amplitude" |
| `phase reference` | string | "center" | 相位参考点："center", "user defined" |
| `phase reference x` | float | 0 | 相位参考 X 坐标 (m) |
| `phase reference y` | float | 0 | 相位参考 Y 坐标 (m) |
| `phase reference z` | float | 0 | 相位参考 Z 坐标 (m) |

### 9. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.0, 0.5, 1.0, 0.3] | RGBA 颜色值（蓝色半透明） |
| `alpha` | float | 0.3 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addmodeexpansion` 命令没有返回值。成功执行后，会在仿真中添加一个模式扩展监视器对象。

## 示例

### 示例 1: 基本模式扩展监视器（波导输出端）

#### LSF 脚本
```lumerical
// 添加模式扩展监视器
addmodeexpansion;

// 设置几何参数
set("name", "output_mode_expansion");
set("x", 10e-6);      // 波导输出端位置
set("y", 0);
set("z", 0);
set("y span", 3e-6);  // 覆盖波导截面
set("z span", 2e-6);

// 设置监视器类型
set("monitor type", "2D X-normal");
set("normal direction", "x");  // 前向传播

// 设置模式扩展参数
set("expansion type", "all");  // 扩展到所有模式
set("number of modes", 5);     // 计算前5个模式
set("wavelength", 1.55e-6);    // 通信波长

// 记录设置
set("record expansion coefficients", 1);
set("record power", 1);
set("record phase", 1);

// 使用光源波长范围
set("use source limits", 1);
set("frequency points", 50);  // 50个频率点

// 输出设置
set("output a", "a_output");
set("output power forward", "power_fwd");
set("output phase forward", "phase_fwd");

// 显示属性
set("color", [0.0, 0.5, 1.0, 0.3]);  // 蓝色半透明
set("alpha", 0.3);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加模式扩展监视器
fdtd.addmodeexpansion()

# 设置几何参数
fdtd.set("name", "output_mode_expansion")
fdtd.set("x", 10e-6)      # 波导输出端位置
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)  # 覆盖波导截面
fdtd.set("z span", 2e-6)

# 设置监视器类型
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "x")  # 前向传播

# 设置模式扩展参数
fdtd.set("expansion type", "all")  # 扩展到所有模式
fdtd.set("number of modes", 5)     # 计算前5个模式
fdtd.set("wavelength", 1.55e-6)    # 通信波长

# 记录设置
fdtd.set("record expansion coefficients", 1)
fdtd.set("record power", 1)
fdtd.set("record phase", 1)

# 使用光源波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 50)  # 50个频率点

# 输出设置
fdtd.set("output a", "a_output")
fdtd.set("output power forward", "power_fwd")
fdtd.set("output phase forward", "phase_fwd")

# 显示属性
fdtd.set("color", [0.0, 0.5, 1.0, 0.3])  # 蓝色半透明
fdtd.set("alpha", 0.3)
```

### 示例 2: 定向耦合器模式分析

#### LSF 脚本
```lumerical
// 输出端口1模式扩展
addmodeexpansion;
set("name", "port1_mode");
set("x", 15e-6);      // 端口1位置
set("y", 2e-6);
set("z", 0);
set("y span", 2e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("expansion type", "fundamental TE");  // 仅基模TE
set("record power", 1);
set("output power forward", "power_port1");
set("color", [1.0, 0.0, 0.0, 0.2]);  // 红色

// 输出端口2模式扩展
addmodeexpansion;
set("name", "port2_mode");
set("x", 15e-6);      // 端口2位置
set("y", -2e-6);
set("z", 0);
set("y span", 2e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("expansion type", "fundamental TE");
set("record power", 1);
set("output power forward", "power_port2");
set("color", [0.0, 1.0, 0.0, 0.2]);  // 绿色

// 输入端口（参考）
addmodeexpansion;
set("name", "input_mode");
set("x", -1e-6);      // 输入端口（稍前位置）
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("normal direction", "-x");  // 反向法线（输入方向）
set("expansion type", "fundamental TE");
set("record power", 1);
set("output power forward", "power_input");
set("color", [0.0, 0.0, 1.0, 0.2]);  // 蓝色

// 设置公共参数
setnamed("port1_mode", "use source limits", 1);
setnamed("port1_mode", "frequency points", 30);
setnamed("port2_mode", "use source limits", 1);
setnamed("port2_mode", "frequency points", 30);
setnamed("input_mode", "use source limits", 1);
setnamed("input_mode", "frequency points", 30);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 输出端口1模式扩展
fdtd.addmodeexpansion()
fdtd.set("name", "port1_mode")
fdtd.set("x", 15e-6)      # 端口1位置
fdtd.set("y", 2e-6)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("expansion type", "fundamental TE")  # 仅基模TE
fdtd.set("record power", 1)
fdtd.set("output power forward", "power_port1")
fdtd.set("color", [1.0, 0.0, 0.0, 0.2])  # 红色

# 输出端口2模式扩展
fdtd.addmodeexpansion()
fdtd.set("name", "port2_mode")
fdtd.set("x", 15e-6)      # 端口2位置
fdtd.set("y", -2e-6)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("expansion type", "fundamental TE")
fdtd.set("record power", 1)
fdtd.set("output power forward", "power_port2")
fdtd.set("color", [0.0, 1.0, 0.0, 0.2])  # 绿色

# 输入端口（参考）
fdtd.addmodeexpansion()
fdtd.set("name", "input_mode")
fdtd.set("x", -1e-6)      # 输入端口（稍前位置）
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "-x")  # 反向法线（输入方向）
fdtd.set("expansion type", "fundamental TE")
fdtd.set("record power", 1)
fdtd.set("output power forward", "power_input")
fdtd.set("color", [0.0, 0.0, 1.0, 0.2])  # 蓝色

# 设置公共参数
fdtd.set("use source limits", 1, "port1_mode")
fdtd.set("frequency points", 30, "port1_mode")
fdtd.set("use source limits", 1, "port2_mode")
fdtd.set("frequency points", 30, "port2_mode")
fdtd.set("use source limits", 1, "input_mode")
fdtd.set("frequency points", 30, "input_mode")
```

### 示例 3: 多模干涉器模式分解

#### LSF 脚本
```lumerical
addmodeexpansion;
set("name", "MMI_mode_expansion");
set("x", 20e-6);      // MMI输出端
set("y", 0);
set("z", 0);
set("y span", 10e-6);  // 覆盖整个MMI宽度
set("z span", 2e-6);

// 设置监视器类型
set("monitor type", "2D X-normal");
set("normal direction", "x");

// 扩展到多个模式
set("expansion type", "all");
set("number of modes", 8);  // MMI通常支持多个模式

// 记录详细数据
set("record expansion coefficients", 1);
set("record power", 1);
set("record phase", 1);
set("record mode profiles", 1);  // 记录模式剖面

// 设置波长范围
set("override global monitor settings", 1);
set("wavelength start", 1.5e-6);
set("wavelength stop", 1.6e-6);
set("frequency points", 20);

// 输出设置
set("output a", "a_MMI");
set("output power forward", "power_MMI");
set("output phase forward", "phase_MMI");
set("output mode index", "neff_MMI");

// 高级设置
set("normalization", "power");  // 功率归一化
set("phase reference", "center");
set("phase reference x", 20e-6);
set("phase reference y", 0);
set("phase reference z", 0);

// 显示属性
set("color", [0.5, 0.0, 0.5, 0.25]);  // 紫色半透明
set("alpha", 0.25);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmodeexpansion()
fdtd.set("name", "MMI_mode_expansion")
fdtd.set("x", 20e-6)      # MMI输出端
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 10e-6)  # 覆盖整个MMI宽度
fdtd.set("z span", 2e-6)

# 设置监视器类型
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "x")

# 扩展到多个模式
fdtd.set("expansion type", "all")
fdtd.set("number of modes", 8)  # MMI通常支持多个模式

# 记录详细数据
fdtd.set("record expansion coefficients", 1)
fdtd.set("record power", 1)
fdtd.set("record phase", 1)
fdtd.set("record mode profiles", 1)  # 记录模式剖面

# 设置波长范围
fdtd.set("override global monitor settings", 1)
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)
fdtd.set("frequency points", 20)

# 输出设置
fdtd.set("output a", "a_MMI")
fdtd.set("output power forward", "power_MMI")
fdtd.set("output phase forward", "phase_MMI")
fdtd.set("output mode index", "neff_MMI")

# 高级设置
fdtd.set("normalization", "power")  # 功率归一化
fdtd.set("phase reference", "center")
fdtd.set("phase reference x", 20e-6)
fdtd.set("phase reference y", 0)
fdtd.set("phase reference z", 0)

# 显示属性
fdtd.set("color", [0.5, 0.0, 0.5, 0.25])  # 紫色半透明
fdtd.set("alpha", 0.25)
```

### 示例 4: 模式转换器效率分析

#### LSF 脚本
```lumerical
// 输入模式监视器（TE0模式）
addmodeexpansion;
set("name", "input_TE0");
set("x", -1e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("normal direction", "-x");  // 反向法线
set("expansion type", "fundamental TE");
set("mode selection", "user select");
set("mode number", 1);  // TE0模式
set("record power", 1);
set("output power forward", "power_TE0_in");
set("color", [1.0, 0.5, 0.0, 0.3]);  // 橙色

// 输出模式监视器（TM0模式）
addmodeexpansion;
set("name", "output_TM0");
set("x", 25e-6);      // 转换器输出端
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("expansion type", "fundamental TM");
set("mode selection", "user select");
set("mode number", 1);  // TM0模式
set("record power", 1);
set("record overlap", 1);  // 记录重叠积分
set("output power forward", "power_TM0_out");
set("output overlap", "overlap_TE_TM");
set("color", [0.0, 0.5, 1.0, 0.3]);  // 蓝色

// 设置波长扫描
setnamed("input_TE0", "override global monitor settings", 1);
setnamed("input_TE0", "wavelength start", 1.5e-6);
setnamed("input_TE0", "wavelength stop", 1.6e-6);
setnamed("input_TE0", "frequency points", 40);

setnamed("output_TM0", "override global monitor settings", 1);
setnamed("output_TM0", "wavelength start", 1.5e-6);
setnamed("output_TM0", "wavelength stop", 1.6e-6);
setnamed("output_TM0", "frequency points", 40);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 输入模式监视器（TE0模式）
fdtd.addmodeexpansion()
fdtd.set("name", "input_TE0")
fdtd.set("x", -1e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "-x")  # 反向法线
fdtd.set("expansion type", "fundamental TE")
fdtd.set("mode selection", "user select")
fdtd.set("mode number", 1)  # TE0模式
fdtd.set("record power", 1)
fdtd.set("output power forward", "power_TE0_in")
fdtd.set("color", [1.0, 0.5, 0.0, 0.3])  # 橙色

# 输出模式监视器（TM0模式）
fdtd.addmodeexpansion()
fdtd.set("name", "output_TM0")
fdtd.set("x", 25e-6)      # 转换器输出端
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("expansion type", "fundamental TM")
fdtd.set("mode selection", "user select")
fdtd.set("mode number", 1)  # TM0模式
fdtd.set("record power", 1)
fdtd.set("record overlap", 1)  # 记录重叠积分
fdtd.set("output power forward", "power_TM0_out")
fdtd.set("output overlap", "overlap_TE_TM")
fdtd.set("color", [0.0, 0.5, 1.0, 0.3])  # 蓝色

# 设置波长扫描
fdtd.set("override global monitor settings", 1, "input_TE0")
fdtd.set("wavelength start", 1.5e-6, "input_TE0")
fdtd.set("wavelength stop", 1.6e-6, "input_TE0")
fdtd.set("frequency points", 40, "input_TE0")

fdtd.set("override global monitor settings", 1, "output_TM0")
fdtd.set("wavelength start", 1.5e-6, "output_TM0")
fdtd.set("wavelength stop", 1.6e-6, "output_TM0")
fdtd.set("frequency points", 40, "output_TM0")
```

### 示例 5: 反向模式分析（反射模式）

#### LSF 脚本
```lumerical
// 前向模式扩展（输出）
addmodeexpansion;
set("name", "forward_expansion");
set("x", 12e-6);      // 器件输出端
set("y", 0);
set("z", 0);
set("y span", 3e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("direction", "forward");  // 前向模式
set("expansion type", "all");
set("number of modes", 3);
set("record expansion coefficients", 1);
set("record power", 1);
set("output a", "a_forward");
set("output power forward", "power_forward");
set("color", [0.0, 0.7, 0.0, 0.25]);  // 绿色

// 反向模式扩展（反射）
addmodeexpansion;
set("name", "backward_expansion");
set("x", -1e-6);      // 器件输入端（稍前位置）
set("y", 0);
set("z", 0);
set("y span", 3e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("normal direction", "-x");  // 反向法线
set("direction", "backward");   // 反向模式
set("expansion type", "all");
set("number of modes", 3);
set("record expansion coefficients", 1);
set("record power", 1);
set("output b", "b_backward");
set("output power backward", "power_backward");
set("color", [0.7, 0.0, 0.0, 0.25]);  // 红色

// 设置公共参数
setnamed("forward_expansion", "use source limits", 1);
setnamed("forward_expansion", "frequency points", 25);
setnamed("backward_expansion", "use source limits", 1);
setnamed("backward_expansion", "frequency points", 25);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 前向模式扩展（输出）
fdtd.addmodeexpansion()
fdtd.set("name", "forward_expansion")
fdtd.set("x", 12e-6)      # 器件输出端
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("direction", "forward")  # 前向模式
fdtd.set("expansion type", "all")
fdtd.set("number of modes", 3)
fdtd.set("record expansion coefficients", 1)
fdtd.set("record power", 1)
fdtd.set("output a", "a_forward")
fdtd.set("output power forward", "power_forward")
fdtd.set("color", [0.0, 0.7, 0.0, 0.25])  # 绿色

# 反向模式扩展（反射）
fdtd.addmodeexpansion()
fdtd.set("name", "backward_expansion")
fdtd.set("x", -1e-6)      # 器件输入端（稍前位置）
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "-x")  # 反向法线
fdtd.set("direction", "backward")   # 反向模式
fdtd.set("expansion type", "all")
fdtd.set("number of modes", 3)
fdtd.set("record expansion coefficients", 1)
fdtd.set("record power", 1)
fdtd.set("output b", "b_backward")
fdtd.set("output power backward", "power_backward")
fdtd.set("color", [0.7, 0.0, 0.0, 0.25])  # 红色

# 设置公共参数
fdtd.set("use source limits", 1, "forward_expansion")
fdtd.set("frequency points", 25, "forward_expansion")
fdtd.set("use source limits", 1, "backward_expansion")
fdtd.set("frequency points", 25, "backward_expansion")
```

## 注意事项

### 1. 模式基组定义
- 模式扩展需要预先定义模式基组
- 模式基组可以通过端口、模式源或模式求解器定义
- 确保模式基组的波长、偏振与仿真一致

### 2. 监视器位置
- 监视器应位于模式传播方向垂直的平面
- 平面监视器应完全覆盖模式截面
- 避免监视器位于模式变化剧烈的区域

### 3. 模式选择
- **基模分析**: 选择 `fundamental TE` 或 `fundamental TM`
- **多模分析**: 设置 `number of modes` 为所需模式数
- **特定模式**: 使用 `mode selection` 和 `mode number` 选择特定模式

### 4. 数据解释
- **扩展系数 (a,b)**: 模式振幅（复数）
- **模式功率**: `P = |a|²`（功率归一化）
- **重叠积分**: 模式与总场的重叠程度
- **相位信息**: 模式相对相位，受相位参考点影响

### 5. 性能优化
- 减少模式数量以提高计算速度
- 只记录必要的输出数据
- 合理设置频率点数（宽带分析需要更多点）

## 错误处理

### 常见错误
1. **模式基组未定义**
   - 解决方案：先定义端口或模式源，再添加模式扩展监视器

2. **监视器位置不当**
   - 解决方案：确保监视器位于模式传播路径上，且平面垂直传播方向

3. **模式数量不足**
   - 解决方案：增加 `number of modes` 设置

4. **波长不匹配**
   - 解决方案：确保模式基组波长与仿真波长一致

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 首先定义模式源或端口
    fdtd.addmode()
    fdtd.set("name", "source_mode")
    
    # 添加模式扩展监视器
    fdtd.addmodeexpansion()
    
    # 配置监视器属性
    fdtd.set("name", "mode_expansion_test")
    fdtd.set("monitor type", "2D X-normal")
    fdtd.set("expansion type", "fundamental TE")
    fdtd.set("record power", 1)
    
except lumapi.LumApiError as e:
    print(f"模式扩展监视器创建失败: {e}")
    
    # 检查具体错误
    if "mode" in str(e).lower() and "basis" in str(e).lower():
        print("错误: 模式基组未定义")
    elif "position" in str(e).lower():
        print("错误: 监视器位置不当")
    elif "number of modes" in str(e).lower():
        print("错误: 模式数量不足")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addmode`: 添加模式光源
- `addport`: 添加端口
- `addpower`: 添加功率监视器
- `addprofile`: 添加场监视器
- `setexpansion`: 设置扩展监视器参数
- `getresult`: 获取监视器数据

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: varFDTD（基本模式扩展）
- **不支持**: INTERCONNECT, DEVICE

## 应用场景

### 1. 波导耦合效率计算
```python
# 计算波导间模式耦合效率
fdtd.addmodeexpansion()
fdtd.set("expansion type", "fundamental TE")
fdtd.set("record power", 1)
fdtd.set("record overlap", 1)
```

### 2. 多模干涉器分析
```python
# 分析MMI中模式干涉
fdtd.addmodeexpansion()
fdtd.set("expansion type", "all")
fdtd.set("number of modes", 6)  # MMI支持的模式数
fdtd.set("record expansion coefficients", 1)
```

### 3. 模式转换器表征
```python
# 分析模式转换效率
fdtd.addmodeexpansion()
fdtd.set("expansion type", "fundamental TM")  # 目标模式
fdtd.set("record power", 1)
fdtd.set("record overlap", 1)  # 与输入模式重叠
```

### 4. 反射模式分析
```python
# 分析器件反射模式成分
fdtd.addmodeexpansion()
fdtd.set("direction", "backward")  # 反向模式
fdtd.set("expansion type", "all")
fdtd.set("record expansion coefficients", 1)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增反向模式分析支持 |
| Lumerical 2019a | 改进模式重叠积分计算 |
| Lumerical 2018a | 新增模式剖面记录功能 |

## 参考

1. Lumerical 模式扩展分析指南
2. 光波导模式理论与耦合分析
3. 集成光子器件设计与表征方法

---

*最后更新: 2025-01-30*  
*文档版本: 1.0*