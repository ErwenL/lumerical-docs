# addmode

## 概述

`addmode` 命令用于在 FDTD 或 MODE 仿真中添加模式光源。模式光源将选定模式从波导或光纤中注入仿真区域，是光子集成电路仿真中最常用的光源类型。该光源可以模拟实际波导中的模式激发，支持单波长、宽带扫描以及自定义模式分布。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addmode;
```

### Python API (Lumapi)
```python
session.addmode()
```

## 参数

`addmode` 命令没有直接参数，但需要通过后续的 `set` 命令配置光源属性。

## 配置属性

添加模式光源后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "mode source" | 光源名称 |
| `x`, `y`, `z` | float | 0 | 光源中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 光源各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 光源 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 光源 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 光源 Z 方向最小/最大坐标 (m) |

### 2. 光源方向与模式
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `injection axis` | string | "x" | 注入方向："x", "y", "z" |
| `direction` | string | "forward" | 传播方向："forward", "backward", "both" |
| `mode selection` | string | "fundamental TE mode" | 模式选择 |
| `selected mode number` | int | 1 | 选择的模式编号 |
| `mode calculation` | string | "use global source settings" | 模式计算方法 |

### 3. 波长与频率设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength start` | float | 1.5e-6 | 起始波长 (m) |
| `wavelength stop` | float | 1.6e-6 | 结束波长 (m) |
| `frequency points` | int | 1 | 频率点数 |
| `center wavelength` | float | 1.55e-6 | 中心波长 (m) |
| `wavelength span` | float | 0.1e-6 | 波长跨度 (m) |
| `set wavelength` | int | 0 | 是否设置波长 (0/1) |

### 4. 幅度与相位
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `amplitude` | float | 1.0 | 振幅 |
| `phase` | float | 0 | 相位 (弧度) |
| `power` | float | 1.0 | 功率 (W) |
| `normalize by total power` | int | 0 | 是否按总功率归一化 (0/1) |

### 5. 偏振设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `polarization angle` | float | 0 | 偏振角 (度) |
| `polarization ellipse angle` | float | 0 | 偏振椭圆角 (度) |
| `polarization ellipticity` | float | 0 | 偏振椭圆度 |
| `TE fraction` | float | 1.0 | TE 分量比例 |
| `TM fraction` | float | 0 | TM 分量比例 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override global source settings` | int | 0 | 是否覆盖全局光源设置 (0/1) |
| `bent waveguide` | int | 0 | 是否弯曲波导 (0/1) |
| `tilt angle` | float | 0 | 倾斜角 (度) |
| `offset` | float | 0 | 偏移距离 (m) |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [1.0, 0.0, 0.0, 1.0] | RGBA 颜色值（红色） |
| `alpha` | float | 0.5 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addmode` 命令没有返回值。成功执行后，会在仿真中添加一个模式光源对象。

## 示例

### 示例 1: 基本模式光源设置

#### LSF 脚本
```lumerical
// 添加模式光源
addmode;

// 设置几何参数
set("name", "TE_mode_source");
set("x", -5e-6);      // 左侧注入
set("y", 0);
set("z", 0);
set("y span", 2e-6);  // 覆盖波导宽度
set("z span", 1e-6);  // 覆盖波导高度

// 设置光源方向
set("injection axis", "x");
set("direction", "forward");

// 设置模式选择
set("mode selection", "fundamental TE mode");
set("selected mode number", 1);

// 设置波长（单波长）
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);
set("frequency points", 1);

// 设置幅度
set("amplitude", 1.0);
set("phase", 0);

// 设置显示属性
set("color", [1.0, 0.0, 0.0, 0.5]);  // 红色半透明
set("alpha", 0.5);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加模式光源
fdtd.addmode()

# 设置几何参数
fdtd.set("name", "TE_mode_source")
fdtd.set("x", -5e-6)      # 左侧注入
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)  # 覆盖波导宽度
fdtd.set("z span", 1e-6)  # 覆盖波导高度

# 设置光源方向
fdtd.set("injection axis", "x")
fdtd.set("direction", "forward")

# 设置模式选择
fdtd.set("mode selection", "fundamental TE mode")
fdtd.set("selected mode number", 1)

# 设置波长（单波长）
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)
fdtd.set("frequency points", 1)

# 设置幅度
fdtd.set("amplitude", 1.0)
fdtd.set("phase", 0)

# 设置显示属性
fdtd.set("color", [1.0, 0.0, 0.0, 0.5])  # 红色半透明
fdtd.set("alpha", 0.5)
```

### 示例 2: 宽带扫描光源

#### LSF 脚本
```lumerical
addmode;
set("name", "broadband_source");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置宽带扫描
set("wavelength start", 1.5e-6);   // 1500nm
set("wavelength stop", 1.6e-6);    // 1600nm
set("frequency points", 50);       // 50个波长点

// 设置模式
set("injection axis", "x");
set("mode selection", "fundamental TE mode");

// 设置偏振
set("polarization angle", 0);
set("TE fraction", 1.0);
set("TM fraction", 0);

// 覆盖全局设置
set("override global source settings", 1);

// 设置显示
set("color", [0.0, 1.0, 0.0, 0.4]);  // 绿色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmode()
fdtd.set("name", "broadband_source")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置宽带扫描
fdtd.set("wavelength start", 1.5e-6)   # 1500nm
fdtd.set("wavelength stop", 1.6e-6)    # 1600nm
fdtd.set("frequency points", 50)       # 50个波长点

# 设置模式
fdtd.set("injection axis", "x")
fdtd.set("mode selection", "fundamental TE mode")

# 设置偏振
fdtd.set("polarization angle", 0)
fdtd.set("TE fraction", 1.0)
fdtd.set("TM fraction", 0)

# 覆盖全局设置
fdtd.set("override global source settings", 1)

# 设置显示
fdtd.set("color", [0.0, 1.0, 0.0, 0.4])  # 绿色半透明
```

### 示例 3: 高阶模式注入

#### LSF 脚本
```lumerical
addmode;
set("name", "higher_order_mode");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 3e-6);
set("z span", 1.5e-6);

// 选择高阶模式
set("mode selection", "user select");
set("selected mode number", 3);      // 第三个模式

// 设置波长
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);

// 设置注入方向
set("injection axis", "x");
set("direction", "forward");

// 设置模式计算
set("mode calculation", "use global source settings");

// 设置显示
set("color", [0.0, 0.0, 1.0, 0.5]);  // 蓝色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmode()
fdtd.set("name", "higher_order_mode")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 1.5e-6)

# 选择高阶模式
fdtd.set("mode selection", "user select")
fdtd.set("selected mode number", 3)      # 第三个模式

# 设置波长
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)

# 设置注入方向
fdtd.set("injection axis", "x")
fdtd.set("direction", "forward")

# 设置模式计算
fdtd.set("mode calculation", "use global source settings")

# 设置显示
fdtd.set("color", [0.0, 0.0, 1.0, 0.5])  # 蓝色半透明
```

### 示例 4: 椭圆偏振光源

#### LSF 脚本
```lumerical
addmode;
set("name", "elliptical_polarization");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置椭圆偏振
set("polarization angle", 45);           // 45度偏振角
set("polarization ellipse angle", 30);   // 椭圆主轴角度
set("polarization ellipticity", 0.5);    // 椭圆度

// 或使用 TE/TM 分量
set("TE fraction", 0.7);                 // 70% TE
set("TM fraction", 0.3);                 // 30% TM

// 设置波长
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);

// 设置注入方向
set("injection axis", "x");

// 设置显示
set("color", [1.0, 0.5, 0.0, 0.6]);  // 橙色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmode()
fdtd.set("name", "elliptical_polarization")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置椭圆偏振
fdtd.set("polarization angle", 45)           # 45度偏振角
fdtd.set("polarization ellipse angle", 30)   # 椭圆主轴角度
fdtd.set("polarization ellipticity", 0.5)    # 椭圆度

# 或使用 TE/TM 分量
fdtd.set("TE fraction", 0.7)                 # 70% TE
fdtd.set("TM fraction", 0.3)                 # 30% TM

# 设置波长
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)

# 设置注入方向
fdtd.set("injection axis", "x")

# 设置显示
fdtd.set("color", [1.0, 0.5, 0.0, 0.6])  # 橙色半透明
```

### 示例 5: 倾斜注入与弯曲波导

#### LSF 脚本
```lumerical
addmode;
set("name", "tilted_injection");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置倾斜注入
set("tilt angle", 15);      // 15度倾斜角
set("offset", 0.5e-6);      // 0.5μm 偏移

// 设置弯曲波导
set("bent waveguide", 1);
set("radius", 10e-6);       // 弯曲半径 10μm

// 设置模式
set("injection axis", "x");
set("mode selection", "fundamental TE mode");

// 设置波长
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);

// 设置显示
set("color", [0.5, 0.0, 0.5, 0.5]);  // 紫色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmode()
fdtd.set("name", "tilted_injection")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置倾斜注入
fdtd.set("tilt angle", 15)      # 15度倾斜角
fdtd.set("offset", 0.5e-6)      # 0.5μm 偏移

# 设置弯曲波导
fdtd.set("bent waveguide", 1)
fdtd.set("radius", 10e-6)       # 弯曲半径 10μm

# 设置模式
fdtd.set("injection axis", "x")
fdtd.set("mode selection", "fundamental TE mode")

# 设置波长
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)

# 设置显示
fdtd.set("color", [0.5, 0.0, 0.5, 0.5])  # 紫色半透明
```

### 示例 6: 双向注入与相位控制

#### LSF 脚本
```lumerical
addmode;
set("name", "bidirectional_source");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 2e-6);    // 注意：对于双向注入，X跨度应较小
set("y span", 2e-6);
set("z span", 1e-6);

// 设置双向注入
set("injection axis", "x");
set("direction", "both");        // 双向传播

// 设置前向和后向模式比例
set("forward mode fraction", 0.7);   // 70% 前向
set("backward mode fraction", 0.3);  // 30% 后向

// 设置相位差
set("forward phase", 0);        // 前向相位 0
set("backward phase", pi);      // 后向相位 π

// 设置波长
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);

// 设置显示
set("color", [0.0, 1.0, 1.0, 0.4]);  // 青色半透明
```

#### Python API
```python
import numpy as np

fdtd = lumapi.FDTD()
fdtd.addmode()
fdtd.set("name", "bidirectional_source")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 2e-6)    # 注意：对于双向注入，X跨度应较小
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置双向注入
fdtd.set("injection axis", "x")
fdtd.set("direction", "both")        # 双向传播

# 设置前向和后向模式比例
fdtd.set("forward mode fraction", 0.7)   # 70% 前向
fdtd.set("backward mode fraction", 0.3)  # 30% 后向

# 设置相位差
fdtd.set("forward phase", 0)        # 前向相位 0
fdtd.set("backward phase", np.pi)   # 后向相位 π

# 设置波长
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)

# 设置显示
fdtd.set("color", [0.0, 1.0, 1.0, 0.4])  # 青色半透明
```

## 注意事项

### 1. 光源位置与方向
- 光源应放置在仿真区域边缘
- 注入方向应指向仿真区域内部
- 光源尺寸应覆盖整个波导截面

### 2. 模式选择与计算
- 使用 `findmodes` 命令先计算模式
- 确保光源区域包含完整的模式场
- 高阶模式可能需要更大的光源区域

### 3. 波长设置
- 单波长仿真：`wavelength start` = `wavelength stop`
- 宽带仿真：设置波长范围和频率点数
- 确保波长在材料模型的适用范围内

### 4. 偏振控制
- TE/TM 模式对应不同的偏振态
- 椭圆偏振可以模拟实际光源的不完美性
- 偏振角影响耦合效率

### 5. 功率与归一化
- 默认振幅为 1.0，但实际功率取决于模式归一化
- 使用 `normalize by total power` 确保功率一致性
- 多波长扫描时注意功率谱密度

### 6. 数值稳定性
- 光源太靠近边界可能引起反射
- 倾斜注入可能增加数值噪声
- 弯曲波导需要足够精细的网格

## 错误处理

### 常见错误
1. **模式未找到**
   - 解决方案：先运行 `findmodes` 计算模式

2. **光源区域太小**
   - 解决方案：增加光源跨度以覆盖完整模式

3. **波长超出范围**
   - 解决方案：检查材料模型的有效波长范围

4. **数值不稳定**
   - 解决方案：调整光源位置或网格设置

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加模式光源
    fdtd.addmode()
    
    # 配置光源属性
    fdtd.set("name", "test_source")
    fdtd.set("injection axis", "x")
    fdtd.set("wavelength start", 1.55e-6)
    
except lumapi.LumApiError as e:
    print(f"模式光源创建失败: {e}")
    
    # 检查具体错误
    if "mode" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 模式未找到，请先运行 findmodes")
    elif "wavelength" in str(e).lower():
        print("错误: 波长设置无效")
    elif "source" in str(e).lower() and "too small" in str(e).lower():
        print("错误: 光源区域太小")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `findmodes`: 计算模式
- `setglobalsource`: 设置全局光源参数
- `adddipole`: 添加偶极子光源
- `addtds`: 添加时域光源
- `addmodesource`: 添加模式源（varFDTD）
- `set`: 设置光源属性

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **有限支持**: varFDTD (使用 `addmodesource`)
- **不支持**: DEVICE, INTERCONNECT

## 应用场景

### 1. 波导传输分析
```python
# 分析波导传输特性
fdtd.addmode()
fdtd.set("injection axis", "x")
fdtd.set("mode selection", "fundamental TE mode")
fdtd.set("wavelength start", 1.55e-6)
```

### 2. 耦合器设计
```python
# 分析定向耦合器
fdtd.addmode()
fdtd.set("injection axis", "x")
fdtd.set("y span", 4e-6)  # 覆盖两个波导
fdtd.set("mode selection", "fundamental TE mode")
```

### 3. 偏振分束器
```python
# 测试偏振相关器件
fdtd.addmode()
fdtd.set("TE fraction", 0.5)  # 50% TE
fdtd.set("TM fraction", 0.5)  # 50% TM
fdtd.set("polarization angle", 45)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增双向注入支持 |
| Lumerical 2019a | 改进模式匹配算法 |
| Lumerical 2018a | 新增倾斜注入功能 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical 光源设置指南
2. Lumerical 模式分析教程
3. 波导模式耦合理论

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*