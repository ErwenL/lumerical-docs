# `change` - 更改对象属性

## 概述

`change` 命令用于修改仿真中现有对象的属性。这是 Lumerical 脚本中一个非常常用的命令，允许用户动态调整对象的几何尺寸、材料、位置、方向等参数，而无需删除和重新创建对象。

该命令提供了一种灵活的方式来更新仿真设置，特别适用于参数扫描、优化设计和自动化脚本中。

## 语法

### LSF 语法
```lumerical
change(object_name, property, value);
change(object_name, property1, value1, property2, value2, ...);
```

### Python API
```python
session.change(object_name, property, value)
session.change(object_name, property1=value1, property2=value2, ...)
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `object_name` | string | 要修改的对象的名称。可以是任何仿真对象（结构、源、监视器、求解器等）。 | 是 |
| `property` | string | 要修改的属性名称。 | 是 |
| `value` | varies | 属性的新值。 | 是 |

## 配置属性

`change` 命令可以修改任何对象的任何可配置属性。以下是一些常见对象的常用属性：

### 几何结构对象（矩形、圆柱体等）
| 属性 | 类型 | 描述 |
|------|------|------|
| `x`, `y`, `z` | number | 对象中心位置（μm）。 |
| `x span`, `y span`, `z span` | number | 对象尺寸（μm）。 |
| `x min`, `x max` | number | 对象边界（μm）。 |
| `y min`, `y max` | number | 对象边界（μm）。 |
| `z min`, `z max` | number | 对象边界（μm）。 |
| `material` | string | 材料名称。 |
| `color` | string | 显示颜色。 |
| `alpha` | number | 透明度（0-1）。 |
| `visible` | bool | 是否可见。 |

### 光源对象
| 属性 | 类型 | 描述 |
|------|------|------|
| `injection axis` | string | 注入方向（"x"、"y"、"z"）。 |
| `center wavelength` | number | 中心波长（μm）。 |
| `wavelength span` | number | 波长范围（μm）。 |
| `amplitude` | number | 振幅。 |
| `phase` | number | 相位（弧度）。 |
| `angle theta` | number | 入射角 θ（度）。 |
| `angle phi` | number | 入射角 φ（度）。 |

### 监视器对象
| 属性 | 类型 | 描述 |
|------|------|------|
| `monitor type` | string | 监视器类型。 |
| `x span`, `y span`, `z span` | number | 监视器区域尺寸。 |
| `frequency points` | number | 频率点数。 |
| `wavelength center` | number | 中心波长。 |
| `wavelength span` | number | 波长范围。 |

### 求解器对象
| 属性 | 类型 | 描述 |
|------|------|------|
| `background index` | number | 背景折射率。 |
| `mesh accuracy` | number | 网格精度。 |
| `simulation time` | number | 仿真时间（fs）。 |
| `boundary conditions` | string | 边界条件类型。 |

## 使用示例

### 示例 1：修改矩形结构的位置和尺寸

#### LSF 脚本
```lumerical
// 添加矩形结构
addrect;
set("name", "rect_1");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 1);
set("y span", 1);
set("z span", 0.1);
set("material", "Si");

// 修改矩形位置和尺寸
change("rect_1", "x", 0.5);           // 将 x 位置移动到 0.5 μm
change("rect_1", "x span", 1.5);      // 将 x 方向尺寸改为 1.5 μm
change("rect_1", "material", "SiO2"); // 更改材料为 SiO2

// 同时修改多个属性
change("rect_1", "y", 0.3);
change("rect_1", "y span", 0.8);
change("rect_1", "z span", 0.15);
```

#### Python API
```python
import lumapi

# 创建 FDTD 会话
fdtd = lumapi.FDTD()

# 添加矩形结构
fdtd.addrect("rect_1", x=0, y=0, z=0, x_span=1, y_span=1, z_span=0.1, material="Si")

# 修改矩形位置和尺寸
fdtd.change("rect_1", "x", 0.5)           # 将 x 位置移动到 0.5 μm
fdtd.change("rect_1", "x span", 1.5)      # 将 x 方向尺寸改为 1.5 μm
fdtd.change("rect_1", "material", "SiO2") # 更改材料为 SiO2

# 同时修改多个属性
fdtd.change("rect_1", y=0.3, y_span=0.8, z_span=0.15)
```

### 示例 2：修改光源参数

#### LSF 脚本
```lumerical
// 添加模式源
addmode;
set("name", "source_1");
set("x", 0);
set("y", 0);
set("z", 0);
set("injection axis", "z");
set("center wavelength", 1.55);
set("wavelength span", 0.2);

// 修改光源参数
change("source_1", "center wavelength", 1.31);  // 改为 1310 nm
change("source_1", "wavelength span", 0.1);     // 缩小波长范围
change("source_1", "amplitude", 1.5);           // 增加振幅

// 设置角度参数
change("source_1", "angle theta", 15);
change("source_1", "angle phi", 30);
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加模式源
fdtd.addmode("source_1", x=0, y=0, z=0, 
             injection_axis="z", 
             center_wavelength=1.55,
             wavelength_span=0.2)

# 修改光源参数
fdtd.change("source_1", "center wavelength", 1.31)  # 改为 1310 nm
fdtd.change("source_1", "wavelength span", 0.1)     # 缩小波长范围
fdtd.change("source_1", "amplitude", 1.5)           # 增加振幅

# 使用关键字参数语法
fdtd.change("source_1", angle_theta=15, angle_phi=30)
```

### 示例 3：修改监视器设置

#### LSF 脚本
```lumerical
// 添加功率监视器
addpower;
set("name", "monitor_1");
set("x", 0);
set("y", 0);
set("z", 0.5);
set("x span", 2);
set("y span", 2);
set("z span", 0);
set("monitor type", "linear x");

// 修改监视器属性和位置
change("monitor_1", "x", 1.0);                 // 移动位置
change("monitor_1", "x span", 3.0);            // 扩大监视区域
change("monitor_1", "monitor type", "2D X-normal");  // 更改监视器类型
change("monitor_1", "frequency points", 100);  // 增加频率点数
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加功率监视器
fdtd.addpower("monitor_1", x=0, y=0, z=0.5, 
              x_span=2, y_span=2, z_span=0,
              monitor_type="linear x")

# 修改监视器属性和位置
fdtd.change("monitor_1", "x", 1.0)                 # 移动位置
fdtd.change("monitor_1", "x span", 3.0)            # 扩大监视区域
fdtd.change("monitor_1", "monitor type", "2D X-normal")  # 更改监视器类型
fdtd.change("monitor_1", "frequency points", 100)  # 增加频率点数
```

### 示例 4：在参数扫描中使用

#### LSF 脚本
```lumerical
// 添加波导结构
addrect;
set("name", "waveguide");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 0.5);
set("y span", 0.22);
set("z span", 10);
set("material", "Si");

// 参数扫描：改变波导宽度
widths = linspace(0.4, 0.6, 5);  // 0.4 到 0.6 μm
transmissions = matrix(length(widths), 1);

for (i = 1:length(widths)) {
    width = widths(i);
    
    // 修改波导宽度
    change("waveguide", "x span", width);
    
    // 运行仿真
    run;
    
    // 获取传输结果（假设有名为 monitor_1 的监视器）
    T = getresult("monitor_1", "T");
    transmissions(i) = mean(T);
    
    // 打印结果
    ?format "宽度 %.3f μm: 传输率 = %.4f\n", width, transmissions(i);
}
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 添加波导结构
fdtd.addrect("waveguide", x=0, y=0, z=0, 
             x_span=0.5, y_span=0.22, z_span=10, 
             material="Si")

# 参数扫描：改变波导宽度
widths = np.linspace(0.4, 0.6, 5)  # 0.4 到 0.6 μm
transmissions = []

for i, width in enumerate(widths):
    # 修改波导宽度
    fdtd.change("waveguide", "x span", width)
    
    # 运行仿真
    fdtd.run()
    
    # 获取传输结果
    T = fdtd.getresult("monitor_1", "T")
    transmissions.append(T)
    
    print(f"宽度 {width:.3f} μm: 传输率 = {np.mean(T):.4f}")
```

### 示例 5：修改求解器设置

#### LSF 脚本
```lumerical
// 添加 FDTD 求解器
addfdtd;
set("name", "FDTD_solver");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5);
set("y span", 5);
set("z span", 2);

// 修改求解器参数
change("FDTD_solver", "simulation time", 1000);  // 延长仿真时间到 1000 fs
change("FDTD_solver", "mesh accuracy", 3);       // 提高网格精度
change("FDTD_solver", "background index", 1.44); // 更改背景折射率

// 修改边界条件
change("FDTD_solver", "x min bc", "PML");        // x 最小边界为 PML
change("FDTD_solver", "x max bc", "PML");        // x 最大边界为 PML
change("FDTD_solver", "y min bc", "Periodic");   // y 最小边界为周期性
change("FDTD_solver", "y max bc", "Periodic");   // y 最大边界为周期性
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd("FDTD_solver", x=0, y=0, z=0,
             x_span=5, y_span=5, z_span=2)

# 修改求解器参数
fdtd.change("FDTD_solver", "simulation time", 1000)  # 延长仿真时间到 1000 fs
fdtd.change("FDTD_solver", "mesh accuracy", 3)       # 提高网格精度
fdtd.change("FDTD_solver", "background index", 1.44) # 更改背景折射率

# 修改边界条件
fdtd.change("FDTD_solver", "x min bc", "PML")        # x 最小边界为 PML
fdtd.change("FDTD_solver", "x max bc", "PML")        # x 最大边界为 PML
fdtd.change("FDTD_solver", "y min bc", "Periodic")   # y 最小边界为周期性
fdtd.change("FDTD_solver", "y max bc", "Periodic")   # y 最大边界为周期性
```

## 返回值

`change` 命令没有返回值。成功执行后，对象的指定属性被更新。如果命令失败（例如对象不存在或属性无效），Lumerical 会抛出错误。

## 错误处理

### 常见错误

1. **对象不存在错误**
   ```lumerical
   // 错误：对象 "nonexistent" 不存在
   change("nonexistent", "x", 0);
   ```
   解决方案：使用 `add` 命令先创建对象，或使用 `hasexisting` 检查对象是否存在。

2. **属性不存在错误**
   ```lumerical
   // 错误：属性 "invalid_property" 不存在
   change("rect_1", "invalid_property", 1);
   ```
   解决方案：检查属性名称拼写，参考对象的可用属性列表。

3. **无效的属性值错误**
   ```lumerical
   // 错误：负的跨度值无效
   change("rect_1", "x span", -1e-6);
   ```
   解决方案：提供有效的属性值范围。

4. **类型不匹配错误**
   ```lumerical
   // 错误：期望数值但提供了字符串
   change("rect_1", "x span", "text");
   ```
   解决方案：提供正确类型的值。

### Python 错误处理示例

```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addrect("rect_1", x=0, y=0, z=0, x_span=1, y_span=1, material="Si")
    
    # 尝试修改属性
    fdtd.change("rect_1", "x span", 2.0)
    
    # 尝试修改不存在的对象
    fdtd.change("nonexistent", "x", 0)
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
except Exception as e:
    print(f"一般错误: {e}")
    
    # 检查错误类型
    if "object" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 对象不存在")
    elif "property" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 属性不存在")
    elif "invalid" in str(e).lower() and "value" in str(e).lower():
        print("错误: 无效的属性值")
```

## 注意事项

1. **对象名称**：`change` 命令要求对象名称必须存在。如果对象不存在，命令将失败。可以使用 `add` 命令先创建对象，或使用 `select` 命令选择现有对象。

2. **属性名称**：属性名称区分大小写，且必须使用 Lumerical 的内部属性名称。这些名称通常与图形界面中的显示名称略有不同。

3. **属性值类型**：确保提供的属性值类型正确（数字、字符串、布尔值等）。错误的类型可能导致脚本错误。

4. **性能考虑**：频繁调用 `change` 命令可能会影响脚本性能。如果需要修改多个属性，尽量使用单次调用传递多个属性值对。

5. **与 `set` 命令的关系**：`change` 和 `set` 命令功能相似，但语法不同。`set` 使用 `set("object", "property", value)` 语法，而 `change` 使用 `change("object", "property", value)` 或关键字参数语法。

6. **撤销操作**：`change` 命令的效果可以通过 `undo` 命令撤销（如果支持）。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 可用于所有对象类型 |
| MODE Solutions | ✅ 完全支持 | 可用于所有对象类型 |
| DEVICE | ✅ 完全支持 | 可用于所有对象类型 |
| INTERCONNECT | ✅ 完全支持 | 可用于所有对象类型 |

## 相关命令

- `set` - 设置对象属性（与 `change` 功能相似但语法不同）
- `get` - 获取对象属性
- `add` - 添加新对象
- `select` - 选择对象
- `delete` - 删除对象
- `undo` - 撤销更改

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2024-01-01 | 初始版本，包含基本语法和示例 |
| 1.1 | 2025-12-01 | 添加详细配置属性表格和Python API示例 |
| 1.2 | 2026-01-31 | 完善错误处理章节，补充参数扫描示例 |

## 参考

1. Lumerical Script Language Reference - Change Command
2. Lumerical Python API Documentation - session.change() Method
3. Lumerical Knowledge Base: "How to Modify Object Properties in Scripts"

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*