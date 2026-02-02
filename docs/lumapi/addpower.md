# addpower

## 概述

`addpower` 命令用于在仿真中添加功率监视器。功率监视器记录电磁场的功率流（坡印廷矢量），用于计算透射率、反射率、吸收率等关键性能指标。该命令支持频域和时域功率监视，可以配置为点、线、面或体积监视器。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addpower;
```

### Python API (Lumapi)
```python
session.addpower()
```

## 参数

`addpower` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加功率监视器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "power" | 监视器名称 |
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

### 3. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record E` | int | 0 | 是否记录电场 (0/1) |
| `record H` | int | 0 | 是否记录磁场 (0/1) |
| `record P` | int | 1 | 是否记录坡印廷矢量 (0/1) |
| `record S` | int | 0 | 是否记录坡印廷矢量分量 (0/1) |
| `record absorbed power` | int | 0 | 是否记录吸收功率 (0/1) |
| `record transmission` | int | 0 | 是否记录透射率 (0/1) |
| `record reflection` | int | 0 | 是否记录反射率 (0/1) |

### 4. 频率/时间设置
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
| `output P` | string | "P" | 坡印廷矢量输出名称 |
| `output Sx` | string | "Sx" | X方向坡印廷分量输出名称 |
| `output Sy` | string | "Sy" | Y方向坡印廷分量输出名称 |
| `output Sz` | string | "Sz" | Z方向坡印廷分量输出名称 |
| `output absorption` | string | "absorption" | 吸收功率输出名称 |
| `output transmission` | string | "transmission" | 透射率输出名称 |
| `output reflection` | string | "reflection" | 反射率输出名称 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `spatial interpolation` | string | "none" | 空间插值方法 |
| `frequency interpolation` | string | "linear" | 频率插值方法 |
| `down sample X` | int | 1 | X方向下采样因子 |
| `down sample Y` | int | 1 | Y方向下采样因子 |
| `down sample Z` | int | 1 | Z方向下采样因子 |
| `down sample T` | int | 1 | 时间下采样因子 |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [1.0, 1.0, 0.0, 0.3] | RGBA 颜色值（黄色半透明） |
| `alpha` | float | 0.3 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addpower` 命令没有返回值。成功执行后，会在仿真中添加一个功率监视器对象。

## 示例

### 示例 1: 基本功率监视器

#### LSF 脚本
```lumerical
// 添加功率监视器
addpower;

// 设置几何参数
set("name", "output_power");
set("x", 5e-6);      // 输出端位置
set("y", 0);
set("z", 0);
set("y span", 3e-6);  // 覆盖输出波导
set("z span", 2e-6);

// 设置监视器类型
set("monitor type", "2D X-normal");
set("normal direction", "x");

// 设置记录选项
set("record P", 1);      // 记录坡印廷矢量
set("record transmission", 1);  // 记录透射率

// 使用光源波长范围
set("use source limits", 1);
set("frequency points", 100);  // 100个频率点

// 设置输出名称
set("output P", "Pout");
set("output transmission", "T");

// 设置显示属性
set("color", [1.0, 1.0, 0.0, 0.3]);  // 黄色半透明
set("alpha", 0.3);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加功率监视器
fdtd.addpower()

# 设置几何参数
fdtd.set("name", "output_power")
fdtd.set("x", 5e-6)      # 输出端位置
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)  # 覆盖输出波导
fdtd.set("z span", 2e-6)

# 设置监视器类型
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "x")

# 设置记录选项
fdtd.set("record P", 1)      # 记录坡印廷矢量
fdtd.set("record transmission", 1)  # 记录透射率

# 使用光源波长范围
fdtd.set("use source limits", 1)
fdtd.set("frequency points", 100)  # 100个频率点

# 设置输出名称
fdtd.set("output P", "Pout")
fdtd.set("output transmission", "T")

# 设置显示属性
fdtd.set("color", [1.0, 1.0, 0.0, 0.3])  # 黄色半透明
fdtd.set("alpha", 0.3)
```

### 示例 2: 透射率与反射率监视器

#### LSF 脚本
```lumerical
// 透射率监视器（输出端）
addpower;
set("name", "transmission_monitor");
set("x", 10e-6);     // 器件输出端
set("y span", 5e-6);
set("z span", 3e-6);
set("monitor type", "2D X-normal");
set("record transmission", 1);
set("output transmission", "T_total");
set("color", [0.0, 1.0, 0.0, 0.2]);  // 绿色

// 反射率监视器（输入端）
addpower;
set("name", "reflection_monitor");
set("x", -1e-6);     // 器件输入端（稍前位置）
set("y span", 5e-6);
set("z span", 3e-6);
set("monitor type", "2D X-normal");
set("normal direction", "-x");  // 反向法线
set("record reflection", 1);
set("output reflection", "R_total");
set("color", [1.0, 0.0, 0.0, 0.2]);  // 红色

// 设置公共参数
setnamed("transmission_monitor", "use source limits", 1);
setnamed("transmission_monitor", "frequency points", 50);
setnamed("reflection_monitor", "use source limits", 1);
setnamed("reflection_monitor", "frequency points", 50);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 透射率监视器（输出端）
fdtd.addpower()
fdtd.set("name", "transmission_monitor")
fdtd.set("x", 10e-6)     # 器件输出端
fdtd.set("y span", 5e-6)
fdtd.set("z span", 3e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("record transmission", 1)
fdtd.set("output transmission", "T_total")
fdtd.set("color", [0.0, 1.0, 0.0, 0.2])  # 绿色

# 反射率监视器（输入端）
fdtd.addpower()
fdtd.set("name", "reflection_monitor")
fdtd.set("x", -1e-6)     # 器件输入端（稍前位置）
fdtd.set("y span", 5e-6)
fdtd.set("z span", 3e-6)
fdtd.set("monitor type", "2D X-normal")
fdtd.set("normal direction", "-x")  # 反向法线
fdtd.set("record reflection", 1)
fdtd.set("output reflection", "R_total")
fdtd.set("color", [1.0, 0.0, 0.0, 0.2])  # 红色

# 设置公共参数
fdtd.set("use source limits", 1, "transmission_monitor")
fdtd.set("frequency points", 50, "transmission_monitor")
fdtd.set("use source limits", 1, "reflection_monitor")
fdtd.set("frequency points", 50, "reflection_monitor")
```

### 示例 3: 体积功率监视器（吸收分析）

#### LSF 脚本
```lumerical
addpower;
set("name", "absorption_monitor");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 8e-6);
set("y span", 4e-6);
set("z span", 2e-6);

// 体积监视器
set("monitor type", "3D");
set("dimension", "3D");

// 记录吸收功率
set("record absorbed power", 1);
set("record P", 1);          // 记录总功率流
set("record S", 1);          // 记录坡印廷分量

// 设置波长范围
set("override global monitor settings", 1);
set("wavelength start", 1.5e-6);
set("wavelength stop", 1.6e-6);
set("frequency points", 30);

// 设置输出
set("output absorption", "abs");
set("output Sx", "Sx_vol");
set("output Sy", "Sy_vol");
set("output Sz", "Sz_vol");

// 下采样以减少数据量
set("down sample X", 2);
set("down sample Y", 2);
set("down sample Z", 2);

// 显示属性
set("color", [1.0, 0.5, 0.0, 0.15]);  // 橙色半透明
set("alpha", 0.15);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addpower()
fdtd.set("name", "absorption_monitor")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 8e-6)
fdtd.set("y span", 4e-6)
fdtd.set("z span", 2e-6)

# 体积监视器
fdtd.set("monitor type", "3D")
fdtd.set("dimension", "3D")

# 记录吸收功率
fdtd.set("record absorbed power", 1)
fdtd.set("record P", 1)          # 记录总功率流
fdtd.set("record S", 1)          # 记录坡印廷分量

# 设置波长范围
fdtd.set("override global monitor settings", 1)
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)
fdtd.set("frequency points", 30)

# 设置输出
fdtd.set("output absorption", "abs")
fdtd.set("output Sx", "Sx_vol")
fdtd.set("output Sy", "Sy_vol")
fdtd.set("output Sz", "Sz_vol")

# 下采样以减少数据量
fdtd.set("down sample X", 2)
fdtd.set("down sample Y", 2)
fdtd.set("down sample Z", 2)

# 显示属性
fdtd.set("color", [1.0, 0.5, 0.0, 0.15])  # 橙色半透明
fdtd.set("alpha", 0.15)
```

### 示例 4: 多平面功率监视器

#### LSF 脚本
```lumerical
// X 方向多个截面监视器
for(i=0; i<5; i=i+1) {
    addpower;
    set("name", "power_x" + num2str(i));
    set("x", -5e-6 + i*2.5e-6);  // 等间距布置
    set("y span", 4e-6);
    set("z span", 2e-6);
    set("monitor type", "2D X-normal");
    set("record P", 1);
    set("output P", "P_x" + num2str(i));
    set("color", [i*0.2, 1-i*0.2, 0.5, 0.2]);  // 渐变颜色
}

// Y 方向监视器
addpower;
set("name", "power_y_center");
set("y", 0);
set("x span", 10e-6);
set("z span", 2e-6);
set("monitor type", "2D Y-normal");
set("record P", 1);
set("output P", "P_y_center");
set("color", [0.5, 0.5, 1.0, 0.2]);  // 蓝色

// Z 方向监视器
addpower;
set("name", "power_z_center");
set("z", 0);
set("x span", 10e-6);
set("y span", 4e-6);
set("monitor type", "2D Z-normal");
set("record P", 1);
set("output P", "P_z_center");
set("color", [1.0, 0.5, 0.5, 0.2]);  // 粉色

// 设置公共参数
monitor_names = get("objectname");
for(i=1:length(monitor_names)) {
    setnamed(monitor_names{i}, "use source limits", 1);
    setnamed(monitor_names{i}, "frequency points", 20);
}
```

#### Python API
```python
import numpy as np

fdtd = lumapi.FDTD()

# X 方向多个截面监视器
for i in range(5):
    fdtd.addpower()
    name = f"power_x{i}"
    fdtd.set("name", name)
    fdtd.set("x", -5e-6 + i*2.5e-6)  # 等间距布置
    fdtd.set("y span", 4e-6)
    fdtd.set("z span", 2e-6)
    fdtd.set("monitor type", "2D X-normal")
    fdtd.set("record P", 1)
    fdtd.set("output P", f"P_x{i}")
    # 渐变颜色
    fdtd.set("color", [i*0.2, 1-i*0.2, 0.5, 0.2])

# Y 方向监视器
fdtd.addpower()
fdtd.set("name", "power_y_center")
fdtd.set("y", 0)
fdtd.set("x span", 10e-6)
fdtd.set("z span", 2e-6)
fdtd.set("monitor type", "2D Y-normal")
fdtd.set("record P", 1)
fdtd.set("output P", "P_y_center")
fdtd.set("color", [0.5, 0.5, 1.0, 0.2])  # 蓝色

# Z 方向监视器
fdtd.addpower()
fdtd.set("name", "power_z_center")
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)
fdtd.set("y span", 4e-6)
fdtd.set("monitor type", "2D Z-normal")
fdtd.set("record P", 1)
fdtd.set("output P", "P_z_center")
fdtd.set("color", [1.0, 0.5, 0.5, 0.2])  # 粉色

# 设置公共参数（需要获取监视器名称列表）
# 注意：实际应用中可能需要其他方法获取所有监视器名称
```

### 示例 5: 点功率监视器与线监视器

#### LSF 脚本
```lumerical
// 点功率监视器
addpower;
set("name", "point_power");
set("x", 2e-6);
set("y", 1e-6);
set("z", 0.5e-6);
set("monitor type", "0D");  // 点监视器
set("record P", 1);
set("output P", "P_point");
set("frequency points", 50);
set("color", [1.0, 0.0, 1.0, 0.5]);  // 紫色

// 线功率监视器（沿波导）
addpower;
set("name", "line_power_x");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 10e-6);  // 沿 X 方向 10μm
set("y span", 0);      // Y 方向零跨度
set("z span", 0);      // Z 方向零跨度
set("monitor type", "1D X-line");
set("record P", 1);
set("record Sx", 1);   // 记录 X 方向功率流
set("output P", "P_line");
set("output Sx", "Sx_line");
set("frequency points", 20);
set("color", [0.0, 1.0, 1.0, 0.4]);  // 青色

// 设置公共参数
setnamed("point_power", "use source limits", 1);
setnamed("line_power_x", "use source limits", 1);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 点功率监视器
fdtd.addpower()
fdtd.set("name", "point_power")
fdtd.set("x", 2e-6)
fdtd.set("y", 1e-6)
fdtd.set("z", 0.5e-6)
fdtd.set("monitor type", "0D")  # 点监视器
fdtd.set("record P", 1)
fdtd.set("output P", "P_point")
fdtd.set("frequency points", 50)
fdtd.set("color", [1.0, 0.0, 1.0, 0.5])  # 紫色

# 线功率监视器（沿波导）
fdtd.addpower()
fdtd.set("name", "line_power_x")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)  # 沿 X 方向 10μm
fdtd.set("y span", 0)      # Y 方向零跨度
fdtd.set("z span", 0)      # Z 方向零跨度
fdtd.set("monitor type", "1D X-line")
fdtd.set("record P", 1)
fdtd.set("record Sx", 1)   # 记录 X 方向功率流
fdtd.set("output P", "P_line")
fdtd.set("output Sx", "Sx_line")
fdtd.set("frequency points", 20)
fdtd.set("color", [0.0, 1.0, 1.0, 0.4])  # 青色

# 设置公共参数
fdtd.set("use source limits", 1, "point_power")
fdtd.set("use source limits", 1, "line_power_x")
```

## 注意事项

### 1. 监视器位置与方向
- 平面监视器应垂直于功率流方向
- 法线方向应指向功率流正方向
- 监视器尺寸应覆盖整个感兴趣区域

### 2. 数据记录选择
- **坡印廷矢量 (P)**: 总功率流，用于计算透射/反射
- **坡印廷分量 (Sx, Sy, Sz)**: 方向功率流，用于分析功率分布
- **吸收功率**: 材料吸收的功率
- **电场/磁场**: 需要时记录，但增加数据量

### 3. 频率/时间设置
- 使用光源范围确保一致性
- 频率点数影响频谱分辨率
- 宽带仿真需要足够多的频率点

### 4. 数据量与性能
- 体积监视器产生大量数据
- 使用下采样减少数据量
- 只记录需要的数据类型

### 5. 后处理与分析
- 透射率: `T = P_out / P_in`
- 反射率: `R = P_ref / P_in`
- 吸收率: `A = 1 - T - R`
- 功率分布: 分析坡印廷分量

### 6. 数值准确性
- 监视器应远离边界以避免数值误差
- 网格分辨率影响功率计算精度
- 验证功率守恒: `P_in ≈ P_out + P_ref + P_abs`

## 错误处理

### 常见错误
1. **监视器位置无效**
   - 解决方案：确保监视器在仿真区域内

2. **数据量过大**
   - 解决方案：减少频率点数或使用下采样

3. **法线方向错误**
   - 解决方案：检查 `normal direction` 设置

4. **波长范围不匹配**
   - 解决方案：确保监视器与光源波长范围一致

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加功率监视器
    fdtd.addpower()
    
    # 配置监视器属性
    fdtd.set("name", "test_power")
    fdtd.set("monitor type", "2D X-normal")
    fdtd.set("record P", 1)
    
except lumapi.LumApiError as e:
    print(f"功率监视器创建失败: {e}")
    
    # 检查具体错误
    if "position" in str(e).lower():
        print("错误: 监视器位置无效")
    elif "memory" in str(e).lower():
        print("错误: 数据量过大，请减少频率点或使用下采样")
    elif "normal" in str(e).lower():
        print("错误: 法线方向设置错误")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addtime`: 添加时域监视器
- `addprofile`: 添加场监视器
- `addindex`: 添加折射率监视器
- `addmodeexpansion`: 添加模式扩展监视器
- `setglobalmonitor`: 设置全局监视器参数
- `getresult`: 获取监视器数据

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: DEVICE（热功率监视）
- **不支持**: INTERCONNECT

## 应用场景

### 1. 波导传输分析
```python
# 测量波导透射率
fdtd.addpower()
fdtd.set("monitor type", "2D X-normal")
fdtd.set("x", 10e-6)  # 输出端
fdtd.set("record transmission", 1)
```

### 2. 耦合器性能分析
```python
# 分析定向耦合器分光比
fdtd.addpower()
fdtd.set("name", "output1_power")
fdtd.set("record P", 1)

fdtd.addpower()
fdtd.set("name", "output2_power")
fdtd.set("record P", 1)
```

### 3. 吸收材料分析
```python
# 测量材料吸收
fdtd.addpower()
fdtd.set("monitor type", "3D")
fdtd.set("record absorbed power", 1)
```

## 版本历史

| 版本 | 修改 |
|------|------|
 | Lumerical 2020a | 新增吸收功率记录 |
| Lumerical 2019a | 改进坡印廷矢量计算精度 |
| Lumerical 2018a | 新增点/线监视器类型 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical 监视器设置指南
2. 坡印廷矢量与功率流计算
3. 光学器件性能表征方法

---

 *最后更新: 2026-01-31*  
*文档版本: 1.1*