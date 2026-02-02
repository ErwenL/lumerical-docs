# addindex

## 概述

`addindex` 命令用于在仿真中添加折射率监视器。折射率监视器记录材料的折射率分布（n 和 k）、介电常数（ε）和磁导率（μ），是分析波导模式、光子晶体带隙、材料色散等关键特性的重要工具。该监视器可以记录空间变化的折射率分布，支持频域分析。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addindex;
```

### Python API (Lumapi)
```python
session.addindex()
```

## 参数

`addindex` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加折射率监视器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "index" | 监视器名称 |
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

### 3. 折射率记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record index` | int | 1 | 是否记录折射率 (0/1) |
| `record n` | int | 1 | 是否记录实部折射率 n (0/1) |
| `record k` | int | 0 | 是否记录虚部折射率 k (0/1) |
| `record epsilon` | int | 0 | 是否记录介电常数 ε (0/1) |
| `record epsilon xx` | int | 0 | 是否记录 ε_xx 分量 (0/1) |
| `record epsilon yy` | int | 0 | 是否记录 ε_yy 分量 (0/1) |
| `record epsilon zz` | int | 0 | 是否记录 ε_zz 分量 (0/1) |
| `record mu` | int | 0 | 是否记录磁导率 μ (0/1) |
| `record mu xx` | int | 0 | 是否记录 μ_xx 分量 (0/1) |
| `record mu yy` | int | 0 | 是否记录 μ_yy 分量 (0/1) |
| `record mu zz` | int | 0 | 是否记录 μ_zz 分量 (0/1) |
| `record material` | int | 0 | 是否记录材料标识 (0/1) |

### 4. 频率/波长设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency points` | int | 1 | 频率点数 |
| `wavelength start` | float | 1.5e-6 | 起始波长 (m) |
| `wavelength stop` | float | 1.6e-6 | 结束波长 (m) |
| `use source limits` | int | 1 | 是否使用光源波长范围 (0/1) |
| `override global monitor settings` | int | 0 | 是否覆盖全局监视器设置 (0/1) |

### 5. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `output n` | string | "n" | 实部折射率输出名称 |
| `output k` | string | "k" | 虚部折射率输出名称 |
| `output index` | string | "index" | 复数折射率输出名称 |
| `output epsilon` | string | "epsilon" | 介电常数输出名称 |
| `output epsilon xx` | string | "epsilon_xx" | ε_xx 输出名称 |
| `output epsilon yy` | string | "epsilon_yy" | ε_yy 输出名称 |
| `output epsilon zz` | string | "epsilon_zz" | ε_zz 输出名称 |
| `output mu` | string | "mu" | 磁导率输出名称 |
| `output mu xx` | string | "mu_xx" | μ_xx 输出名称 |
| `output mu yy` | string | "mu_yy" | μ_yy 输出名称 |
| `output mu zz` | string | "mu_zz" | μ_zz 输出名称 |
| `output material` | string | "material" | 材料标识输出名称 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `spatial interpolation` | string | "none" | 空间插值方法 |
| `frequency interpolation` | string | "linear" | 频率插值方法 |
| `down sample X` | int | 1 | X 方向下采样因子 |
| `down sample Y` | int | 1 | Y 方向下采样因子 |
| `down sample Z` | int | 1 | Z 方向下采样因子 |
| `subgrid interpolation` | int | 0 | 是否使用亚网格插值 (0/1) |
| `use effective index` | int | 0 | 是否使用等效折射率 (0/1) |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.5, 0.0, 0.5, 0.3] | RGBA 颜色值（紫色半透明） |
| `alpha` | float | 0.3 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addindex` 命令没有返回值。成功执行后，会在仿真中添加一个折射率监视器对象。

## 示例

### 示例 1: 基本折射率监视器（波导截面）

#### LSF 脚本
```lumerical
// 添加折射率监视器
addindex;

// 设置几何参数
set("name", "waveguide_index");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 10e-6);  // 覆盖整个波导区域
set("y span", 3e-6);
set("z span", 2e-6);

// 设置监视器类型
set("monitor type", "2D Z-normal");
set("normal direction", "z");  // Z 方向平面

// 设置记录选项
set("record n", 1);      // 记录实部折射率
set("record k", 0);      // 不记录消光系数（低损耗波导）
set("record material", 1);  // 记录材料标识

// 使用光源波长范围
set("use source limits", 1);
set("frequency points", 1);  // 折射率通常对波长变化不敏感

// 设置输出名称
set("output n", "n_waveguide");
set("output material", "material_map");

// 设置显示属性
set("color", [0.5, 0.0, 0.5, 0.3]);  // 紫色半透明
set("alpha", 0.3);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加折射率监视器
fdtd.addindex()

# 设置几何参数
fdtd.set("name", "waveguide_index")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)  # 覆盖整个波导区域
fdtd.set("y span", 3e-6)
fdtd.set("z span", 2e-6)

# 设置监视器类型
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("normal direction", "z")  # Z 方向平面

# 设置记录选项
fdtd.set("record n", 1)      # 记录实部折射率
fdtd.set("record k", 0)      # 不记录消光系数（低损耗波导）
fdtd.set("record material", 1)  # 记录材料标识

# 使用光源波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 1)  # 折射率通常对波长变化不敏感

# 设置输出名称
fdtd.set("output n", "n_waveguide")
fdtd.set("output material", "material_map")

# 设置显示属性
fdtd.set("color", [0.5, 0.0, 0.5, 0.3])  # 紫色半透明
fdtd.set("alpha", 0.3)
```

### 示例 2: 体积折射率监视器（光子晶体）

#### LSF 脚本
```lumerical
addindex;
set("name", "photonic_crystal_index");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5e-6);
set("y span", 5e-6);
set("z span", 1e-6);

// 体积监视器
set("monitor type", "3D");
set("dimension", "3D");

// 记录折射率和介电常数
set("record n", 1);          // 实部折射率
set("record epsilon", 1);    // 介电常数
set("record epsilon xx", 1); // 各向异性材料需要
set("record epsilon yy", 1);
set("record epsilon zz", 1);

// 设置波长范围（光子晶体带隙分析）
set("override global monitor settings", 1);
set("wavelength start", 1.4e-6);
set("wavelength stop", 1.7e-6);
set("frequency points", 10);  // 多个波长点分析色散

// 设置输出名称
set("output n", "n_photonic");
set("output epsilon", "epsilon_photonic");
set("output epsilon xx", "epsilon_xx");
set("output epsilon yy", "epsilon_yy");
set("output epsilon zz", "epsilon_zz");

// 下采样以减少数据量
set("down sample X", 2);
set("down sample Y", 2);
set("down sample Z", 2);

// 显示属性
set("color", [0.3, 0.0, 0.7, 0.2]);  // 深紫色半透明
set("alpha", 0.2);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addindex()
fdtd.set("name", "photonic_crystal_index")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 5e-6)
fdtd.set("y span", 5e-6)
fdtd.set("z span", 1e-6)

# 体积监视器
fdtd.set("monitor type", "3D")
fdtd.set("dimension", "3D")

# 记录折射率和介电常数
fdtd.set("record n", 1)          # 实部折射率
fdtd.set("record epsilon", 1)    # 介电常数
fdtd.set("record epsilon xx", 1) # 各向异性材料需要
fdtd.set("record epsilon yy", 1)
fdtd.set("record epsilon zz", 1)

# 设置波长范围（光子晶体带隙分析）
fdtd.set("override global monitor settings", 1)
fdtd.set("wavelength start", 1.4e-6)
fdtd.set("wavelength stop", 1.7e-6)
fdtd.set("frequency points", 10)  # 多个波长点分析色散

# 设置输出名称
fdtd.set("output n", "n_photonic")
fdtd.set("output epsilon", "epsilon_photonic")
fdtd.set("output epsilon xx", "epsilon_xx")
fdtd.set("output epsilon yy", "epsilon_yy")
fdtd.set("output epsilon zz", "epsilon_zz")

# 下采样以减少数据量
fdtd.set("down sample X", 2)
fdtd.set("down sample Y", 2)
fdtd.set("down sample Z", 2)

# 显示属性
fdtd.set("color", [0.3, 0.0, 0.7, 0.2])  # 深紫色半透明
fdtd.set("alpha", 0.2)
```

### 示例 3: 线折射率监视器（沿波导折射率分布）

#### LSF 脚本
```lumerical
// 沿波导中心线的折射率分布
addindex;
set("name", "line_index");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 15e-6);  // 沿 X 方向 15μm
set("y span", 0);      // Y 方向零跨度（线）
set("z span", 0);      // Z 方向零跨度

set("monitor type", "1D X-line");

// 记录折射率和材料信息
set("record n", 1);
set("record k", 1);      // 记录消光系数（损耗分析）
set("record material", 1);

// 设置波长范围
set("use source limits", 1);
set("frequency points", 5);  // 多个波长分析波导色散

// 输出名称
set("output n", "n_line");
set("output k", "k_line");
set("output material", "material_line");

// 显示属性
set("color", [0.7, 0.0, 0.3, 0.6]);  // 紫红色
set("alpha", 0.6);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addindex()
fdtd.set("name", "line_index")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 15e-6)  # 沿 X 方向 15μm
fdtd.set("y span", 0)      # Y 方向零跨度（线）
fdtd.set("z span", 0)      # Z 方向零跨度

fdtd.set("monitor type", "1D X-line")

# 记录折射率和材料信息
fdtd.set("record n", 1)
fdtd.set("record k", 1)      # 记录消光系数（损耗分析）
fdtd.set("record material", 1)

# 设置波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 5)  # 多个波长分析波导色散

# 输出名称
fdtd.set("output n", "n_line")
fdtd.set("output k", "k_line")
fdtd.set("output material", "material_line")

# 显示属性
fdtd.set("color", [0.7, 0.0, 0.3, 0.6])  # 紫红色
fdtd.set("alpha", 0.6)
```

### 示例 4: 多平面折射率监视器（各向异性材料分析）

#### LSF 脚本
```lumerical
// XY 平面（各向同性材料）
addindex;
set("name", "index_xy");
set("z", 0);
set("x span", 8e-6);
set("y span", 4e-6);
set("monitor type", "2D Z-normal");
set("record n", 1);
set("record epsilon", 1);
set("output n", "n_xy");
set("output epsilon", "epsilon_xy");
set("color", [1.0, 0.0, 0.0, 0.2]);  // 红色

// XZ 平面（各向异性材料，不同分量）
addindex;
set("name", "index_xz");
set("y", 0);
set("x span", 8e-6);
set("z span", 2e-6);
set("monitor type", "2D Y-normal");
set("record epsilon xx", 1);  // 各向异性材料
set("record epsilon zz", 1);
set("output epsilon xx", "epsilon_xx_xz");
set("output epsilon zz", "epsilon_zz_xz");
set("color", [0.0, 1.0, 0.0, 0.2]);  // 绿色

// YZ 平面（各向异性材料）
addindex;
set("name", "index_yz");
set("x", 0);
set("y span", 4e-6);
set("z span", 2e-6);
set("monitor type", "2D X-normal");
set("record epsilon yy", 1);
set("record epsilon zz", 1);
set("output epsilon yy", "epsilon_yy_yz");
set("output epsilon zz", "epsilon_zz_yz");
set("color", [0.0, 0.0, 1.0, 0.2]);  // 蓝色

// 设置公共参数
setnamed("index_xy", "use source limits", 1);
setnamed("index_xy", "frequency points", 3);
setnamed("index_xz", "use source limits", 1);
setnamed("index_xz", "frequency points", 3);
setnamed("index_yz", "use source limits", 1);
setnamed("index_yz", "frequency points", 3);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# XY 平面（各向同性材料）
fdtd.addindex()
fdtd.set("name", "index_xy")
fdtd.set("z", 0)
fdtd.set("x span", 8e-6)
fdtd.set("y span", 4e-6)
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("record n", 1)
fdtd.set("record epsilon", 1)
fdtd.set("output n", "n_xy")
fdtd.set("output epsilon", "epsilon_xy")
fdtd.set("color", [1.0, 0.0, 0.0, 0.2])  # 红色

# XZ 平面（各向异性材料，不同分量）
fdtd.addindex()
fdtd.set("name", "index_xz")
fdtd.set("y", 0)
fdtd.set("x span", 8e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D Y-normal")
fdtd.set("record epsilon xx", 1)  # 各向异性材料
fdtd.set("record epsilon zz", 1)
fdtd.set("output epsilon xx", "epsilon_xx_xz")
fdtd.set("output epsilon zz", "epsilon_zz_xz")
fdtd.set("color", [0.0, 1.0, 0.0, 0.2])  # 绿色

# YZ 平面（各向异性材料）
fdtd.addindex()
fdtd.set("name", "index_yz")
fdtd.set("x", 0)
fdtd.set("y span", 4e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("record epsilon yy", 1)
fdtd.set("record epsilon zz", 1)
fdtd.set("output epsilon yy", "epsilon_yy_yz")
fdtd.set("output epsilon zz", "epsilon_zz_yz")
fdtd.set("color", [0.0, 0.0, 1.0, 0.2])  # 蓝色

# 设置公共参数
fdtd.set("use source limits", 1, "index_xy")
fdtd.set("frequency points", 3, "index_xy")
fdtd.set("use source limits", 1, "index_xz")
fdtd.set("frequency points", 3, "index_xz")
fdtd.set("use source limits", 1, "index_yz")
fdtd.set("frequency points", 3, "index_yz")
```

### 示例 5: 点折射率监视器（材料参数提取）

#### LSF 脚本
```lumerical
// 点折射率监视器（特定位置）
addindex;
set("name", "point_index");
set("x", 2.5e-6);
set("y", 1.2e-6);
set("z", 0.3e-6);
set("monitor type", "0D");  // 点监视器

// 记录所有折射率参数
set("record n", 1);
set("record k", 1);
set("record epsilon", 1);
set("record mu", 1);  // 磁性材料需要

// 设置波长扫描范围
set("override global monitor settings", 1);
set("wavelength start", 1.2e-6);
set("wavelength stop", 1.8e-6);
set("frequency points", 20);  // 密集波长点分析色散

// 输出名称
set("output n", "n_point");
set("output k", "k_point");
set("output epsilon", "epsilon_point");
set("output mu", "mu_point");

// 显示属性
set("color", [1.0, 0.5, 0.0, 0.8]);  // 橙色
set("alpha", 0.8);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addindex()
fdtd.set("name", "point_index")
fdtd.set("x", 2.5e-6)
fdtd.set("y", 1.2e-6)
fdtd.set("z", 0.3e-6)
fdtd.set("monitor type", "0D")  # 点监视器

# 记录所有折射率参数
fdtd.set("record n", 1)
fdtd.set("record k", 1)
fdtd.set("record epsilon", 1)
fdtd.set("record mu", 1)  # 磁性材料需要

# 设置波长扫描范围
fdtd.set("override global monitor settings", 1)
fdtd.set("wavelength start", 1.2e-6)
fdtd.set("wavelength stop", 1.8e-6)
fdtd.set("frequency points", 20)  # 密集波长点分析色散

# 输出名称
fdtd.set("output n", "n_point")
fdtd.set("output k", "k_point")
fdtd.set("output epsilon", "epsilon_point")
fdtd.set("output mu", "mu_point")

# 显示属性
fdtd.set("color", [1.0, 0.5, 0.0, 0.8])  # 橙色
fdtd.set("alpha", 0.8)
```

## 注意事项

### 1. 监视器类型选择
- **平面监视器**：适用于波导截面、界面折射率分析
- **体积监视器**：适用于光子晶体、复杂三维结构折射率分布
- **线监视器**：适用于沿波导的折射率变化分析
- **点监视器**：适用于特定位置材料参数提取

### 2. 折射率参数选择
- **实部折射率 (n)**：相位延迟、模式有效折射率
- **虚部折射率 (k)**：吸收损耗、增益材料
- **介电常数 (ε)**：电磁响应、各向异性材料分析
- **磁导率 (μ)**：磁性材料、超材料分析

### 3. 数据量与性能优化
- 体积监视器产生大量数据，谨慎使用
- 使用下采样减少数据量
- 只记录必要的折射率参数
- 减少频率点数（折射率通常对波长变化较慢）

### 4. 材料模型考虑
- **色散材料**：需要多个频率点记录折射率变化
- **各向异性材料**：需要记录不同方向的介电常数分量
- **非线性材料**：折射率监视器通常记录线性响应
- **有源材料**：需要记录复数折射率（n+ik）

### 5. 数值准确性
- 监视器网格应足够精细以分辨折射率变化
- 亚网格插值可提高界面处折射率精度
- 避免监视器位于材料边界模糊区域

## 错误处理

### 常见错误
1. **监视器位置无效**
   - 解决方案：确保监视器在仿真区域内

2. **材料数据不可用**
   - 解决方案：检查材料定义是否完整，波长范围是否在材料模型范围内

3. **数据量过大**
   - 解决方案：减少频率点数、使用下采样、选择部分参数记录

4. **各向异性分量记录错误**
   - 解决方案：确保记录的分量与材料坐标系一致

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加折射率监视器
    fdtd.addindex()
    
    # 配置监视器属性
    fdtd.set("name", "test_index")
    fdtd.set("monitor type", "2D Z-normal")
    fdtd.set("record n", 1)
    fdtd.set("frequency points", 5)
    
except lumapi.LumApiError as e:
    print(f"折射率监视器创建失败: {e}")
    
    # 检查具体错误
    if "position" in str(e).lower():
        print("错误: 监视器位置无效")
    elif "material" in str(e).lower():
        print("错误: 材料数据不可用")
    elif "memory" in str(e).lower():
        print("错误: 数据量过大，请减少频率点或使用下采样")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addprofile`: 添加场监视器
- `addpower`: 添加功率监视器
- `addmodeexpansion`: 添加模式扩展监视器
- `setmaterial`: 设置材料属性
- `getmaterial`: 获取材料数据
- `getresult`: 获取监视器数据

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: varFDTD（基本折射率记录）
- **不支持**: INTERCONNECT, DEVICE

## 应用场景

### 1. 波导有效折射率分析
```python
# 分析波导模式的有效折射率
fdtd.addindex()
fdtd.set("monitor type", "2D X-normal")
fdtd.set("record n", 1)
fdtd.set("use effective index", 1)  # 计算等效折射率
```

### 2. 光子晶体带隙分析
```python
# 分析光子晶体的折射率分布
fdtd.addindex()
fdtd.set("monitor type", "3D")
fdtd.set("record n", 1)
fdtd.set("record epsilon", 1)
fdtd.set("frequency points", 15)  # 分析带隙随频率变化
```

### 3. 材料色散表征
```python
# 提取材料的折射率色散
fdtd.addindex()
fdtd.set("monitor type", "0D")  # 点监视器
fdtd.set("record n", 1)
fdtd.set("record k", 1)
fdtd.set("frequency points", 30)  # 密集频率采样
```

### 4. 各向异性材料分析
```python
# 分析各向异性材料的介电张量
fdtd.addindex()
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("record epsilon xx", 1)
fdtd.set("record epsilon yy", 1)
fdtd.set("record epsilon zz", 1)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增等效折射率计算选项 |
| Lumerical 2019a | 改进各向异性材料记录 |
| Lumerical 2018a | 新增点/线监视器类型 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical 材料与折射率分析指南
2. 光学材料特性与测量方法
3. 光子晶体与超材料设计原理

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*