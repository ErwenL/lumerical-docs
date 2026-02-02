# addgrating

## 概述

`addgrating` 命令用于在仿真中添加一个光栅结构。光栅是周期性微纳结构，广泛用于光子学中的波长选择性器件、波导耦合器、偏振分束器和衍射光学元件。该命令支持创建一维和二维光栅，可配置周期、占空比、高度、倾斜角等参数，适用于 FDTD Solutions 和 MODE Solutions。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addgrating;
```

### Python API (Lumapi)
```python
session.addgrating()
```

## 参数

`addgrating` 命令没有直接参数，但需要通过后续的 `set` 命令配置光栅属性。

## 配置属性

添加光栅后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "grating" | 光栅名称 |
| `x`, `y`, `z` | float | 0 | 光栅中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 光栅尺寸 (m) |
| `period` | float | 500e-9 | 光栅周期 (m) |
| `duty cycle` | float | 0.5 | 占空比 (0-1) |
| `height` | float | 100e-9 | 光栅高度 (m) |
| `depth` | float | 100e-9 | 光栅槽深 (m) |
| `grating type` | string | "rectangular" | 光栅类型："rectangular", "triangular", "sinusoidal", "blazed" |
| `grating direction` | string | "x" | 光栅方向："x", "y", "both"（二维光栅） |

### 2. 材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material` | string | "Si (Silicon) - Palik" | 光栅材料名称 |
| `substrate material` | string | "SiO2 (Glass) - Palik" | 衬底材料名称 |
| `cladding material` | string | "Air" | 包层材料名称 |
| `index` | float | 1.0 | 折射率（当 material 为 "<Object defined dielectric>" 时使用） |
| `index units` | string | "microns" | 折射率单位："m", "microns", "nm" |

### 3. 倾斜与方向属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `tilt angle` | float | 0 | 光栅倾斜角 (度) |
| `rotation angle` | float | 0 | 光栅旋转角 (度) |
| `orientation` | string | "normal" | 光栅方向："normal", "rotated", "tilted" |
| `blaze angle` | float | 0 | 闪耀角 (度)，当 `grating type` = "blazed" 时使用 |

### 4. 网格与渲染属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override mesh order from material database` | int | 0 | 是否覆盖材料数据库中的网格顺序 |
| `mesh order` | int | 2 | 网格顺序（需先启用覆盖） |
| `render type` | string | "detailed" | 渲染类型："detailed", "wireframe" |
| `alpha` | float | 1.0 | 透明度 (0.0-1.0) |
| `color` | array[4] | [0.5, 0.5, 0.5, 1.0] | RGBA 颜色值 |

### 5. 周期性边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `periodic` | int | 1 | 是否启用周期性边界条件 |
| `periodic x` | int | 1 | X方向周期性 |
| `periodic y` | int | 1 | Y方向周期性 |
| `periodic z` | int | 0 | Z方向周期性 |
| `periodic boundary` | string | "Bloch" | 周期性边界类型："Bloch", "PML", "periodic" |

## 返回值

`addgrating` 命令没有返回值。成功执行后，会在仿真中添加一个光栅对象。

## 示例

### 示例 1: 基本矩形光栅创建

#### LSF 脚本
```lumerical
// 添加矩形光栅
addgrating;

// 设置几何尺寸
set("name", "rectangular grating");
set("x span", 5e-6);        // X方向尺寸 5μm
set("y span", 2e-6);        // Y方向尺寸 2μm
set("z span", 500e-9);      // Z方向尺寸 500nm
set("period", 300e-9);      // 周期 300nm
set("duty cycle", 0.5);     // 占空比 0.5
set("height", 100e-9);      // 高度 100nm

// 设置材料
set("material", "Si (Silicon) - Palik");
set("substrate material", "SiO2 (Glass) - Palik");
set("cladding material", "Air");

// 设置光栅类型
set("grating type", "rectangular");
set("grating direction", "x");

// 启用周期性边界条件
set("periodic", 1);
set("periodic x", 1);
set("periodic y", 0);
```

#### Python API
```python
import lumapi

# 创建会话（FDTD Solutions）
fdtd = lumapi.FDTD()

# 添加光栅
fdtd.addgrating()

# 设置几何尺寸
fdtd.set("name", "rectangular grating")
fdtd.set("x span", 5e-6)        # X方向尺寸 5μm
fdtd.set("y span", 2e-6)        # Y方向尺寸 2μm
fdtd.set("z span", 500e-9)      # Z方向尺寸 500nm
fdtd.set("period", 300e-9)      # 周期 300nm
fdtd.set("duty cycle", 0.5)     # 占空比 0.5
fdtd.set("height", 100e-9)      # 高度 100nm

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Air")

# 设置光栅类型
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "x")

# 启用周期性边界条件
fdtd.set("periodic", 1)
fdtd.set("periodic x", 1)
fdtd.set("periodic y", 0)
```

### 示例 2: 闪耀光栅

#### LSF 脚本
```lumerical
// 添加闪耀光栅
addgrating;
set("name", "blazed grating");
set("x span", 10e-6);       // X方向尺寸 10μm
set("y span", 5e-6);        // Y方向尺寸 5μm
set("z span", 1e-6);        // Z方向尺寸 1μm
set("period", 500e-9);      // 周期 500nm
set("duty cycle", 0.7);     // 占空比 0.7
set("height", 300e-9);      // 高度 300nm

// 设置闪耀角
set("grating type", "blazed");
set("blaze angle", 15);     // 闪耀角 15度

// 设置材料
set("material", "Au (Gold) - CRC");
set("substrate material", "SiO2 (Glass) - Palik");
set("cladding material", "Air");

// 设置倾斜角
set("tilt angle", 10);      // 整体倾斜 10度
set("rotation angle", 0);

// 设置周期性边界
set("periodic", 1);
set("periodic x", 1);
set("periodic y", 1);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addgrating()
fdtd.set("name", "blazed grating")
fdtd.set("x span", 10e-6)       # X方向尺寸 10μm
fdtd.set("y span", 5e-6)        # Y方向尺寸 5μm
fdtd.set("z span", 1e-6)        # Z方向尺寸 1μm
fdtd.set("period", 500e-9)      # 周期 500nm
fdtd.set("duty cycle", 0.7)     # 占空比 0.7
fdtd.set("height", 300e-9)      # 高度 300nm

# 设置闪耀角
fdtd.set("grating type", "blazed")
fdtd.set("blaze angle", 15)     # 闪耀角 15度

# 设置材料
fdtd.set("material", "Au (Gold) - CRC")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Air")

# 设置倾斜角
fdtd.set("tilt angle", 10)      # 整体倾斜 10度
fdtd.set("rotation angle", 0)

# 设置周期性边界
fdtd.set("periodic", 1)
fdtd.set("periodic x", 1)
fdtd.set("periodic y", 1)
```

### 示例 3: 二维光栅（光子晶体平板）

#### LSF 脚本
```lumerical
// 添加二维光栅（光子晶体）
addgrating;
set("name", "2D photonic crystal grating");
set("x span", 4e-6);        // X方向尺寸 4μm
set("y span", 4e-6);        // Y方向尺寸 4μm
set("z span", 220e-9);      // Z方向尺寸 220nm
set("period", 400e-9);      // 周期 400nm
set("duty cycle", 0.3);     // 占空比 0.3
set("height", 220e-9);      // 高度 220nm

// 设置二维光栅
set("grating type", "rectangular");
set("grating direction", "both");  // 二维光栅

// 设置材料
set("material", "Si (Silicon) - Palik");
set("substrate material", "SiO2 (Glass) - Palik");
set("cladding material", "Air");

// 设置周期性边界
set("periodic", 1);
set("periodic x", 1);
set("periodic y", 1);
set("periodic boundary", "Bloch");

// 设置网格细化
set("override mesh order from material database", 1);
set("mesh order", 3);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addgrating()
fdtd.set("name", "2D photonic crystal grating")
fdtd.set("x span", 4e-6)        # X方向尺寸 4μm
fdtd.set("y span", 4e-6)        # Y方向尺寸 4μm
fdtd.set("z span", 220e-9)      # Z方向尺寸 220nm
fdtd.set("period", 400e-9)      # 周期 400nm
fdtd.set("duty cycle", 0.3)     # 占空比 0.3
fdtd.set("height", 220e-9)      # 高度 220nm

# 设置二维光栅
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "both")  # 二维光栅

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Air")

# 设置周期性边界
fdtd.set("periodic", 1)
fdtd.set("periodic x", 1)
fdtd.set("periodic y", 1)
fdtd.set("periodic boundary", "Bloch")

# 设置网格细化
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 3)
```

### 示例 4: 光栅耦合器（硅光子）

#### LSF 脚本
```lumerical
// 添加光栅耦合器
addgrating;
set("name", "grating coupler");
set("x span", 20e-6);       // X方向尺寸 20μm
set("y span", 10e-6);       // Y方向尺寸 10μm
set("z span", 220e-9);      // Z方向尺寸 220nm
set("period", 630e-9);      // 周期 630nm（针对1550nm波长）
set("duty cycle", 0.5);     // 占空比 0.5
set("height", 70e-9);       // 刻蚀深度 70nm

// 设置光栅参数
set("grating type", "rectangular");
set("grating direction", "x");
set("tilt angle", 10);      // 10度倾斜角改善耦合效率

// 设置材料
set("material", "Si (Silicon) - Palik");
set("substrate material", "SiO2 (Glass) - Palik");
set("cladding material", "Air");

// 设置渐变周期（apodized grating）
// 注：实际应用中可能需要多个光栅对象实现渐变
set("period", 630e-9);      // 初始周期

// 设置光纤耦合优化
set("rotation angle", 0);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addgrating()
fdtd.set("name", "grating coupler")
fdtd.set("x span", 20e-6)       # X方向尺寸 20μm
fdtd.set("y span", 10e-6)       # Y方向尺寸 10μm
fdtd.set("z span", 220e-9)      # Z方向尺寸 220nm
fdtd.set("period", 630e-9)      # 周期 630nm（针对1550nm波长）
fdtd.set("duty cycle", 0.5)     # 占空比 0.5
fdtd.set("height", 70e-9)       # 刻蚀深度 70nm

# 设置光栅参数
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "x")
fdtd.set("tilt angle", 10)      # 10度倾斜角改善耦合效率

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Air")

# 设置渐变周期（apodized grating）
# 注：实际应用中可能需要多个光栅对象实现渐变
fdtd.set("period", 630e-9)      # 初始周期

# 设置光纤耦合优化
fdtd.set("rotation angle", 0)
```

### 示例 5: 偏振分束光栅

#### LSF 脚本
```lumerical
// 添加偏振分束光栅
addgrating;
set("name", "polarization beam splitter grating");
set("x span", 5e-6);        // X方向尺寸 5μm
set("y span", 5e-6);        // Y方向尺寸 5μm
set("z span", 300e-9);      // Z方向尺寸 300nm
set("period", 400e-9);      // 周期 400nm
set("duty cycle", 0.6);     // 占空比 0.6
set("height", 150e-9);      // 高度 150nm

// 设置二维倾斜光栅
set("grating type", "rectangular");
set("grating direction", "both");  // 二维光栅
set("tilt angle", 45);      // 45度倾斜角
set("rotation angle", 0);

// 设置材料
set("material", "TiO2 (Titanium dioxide) - Palik");
set("substrate material", "SiO2 (Glass) - Palik");
set("cladding material", "Air");

// 设置周期性边界
set("periodic", 1);
set("periodic x", 1);
set("periodic y", 1);
set("periodic boundary", "Bloch");

// 设置颜色可视化
set("color", [0.8, 0.2, 0.2, 0.8]);  // 红色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addgrating()
fdtd.set("name", "polarization beam splitter grating")
fdtd.set("x span", 5e-6)        # X方向尺寸 5μm
fdtd.set("y span", 5e-6)        # Y方向尺寸 5μm
fdtd.set("z span", 300e-9)      # Z方向尺寸 300nm
fdtd.set("period", 400e-9)      # 周期 400nm
fdtd.set("duty cycle", 0.6)     # 占空比 0.6
fdtd.set("height", 150e-9)      # 高度 150nm

# 设置二维倾斜光栅
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "both")  # 二维光栅
fdtd.set("tilt angle", 45)      # 45度倾斜角
fdtd.set("rotation angle", 0)

# 设置材料
fdtd.set("material", "TiO2 (Titanium dioxide) - Palik")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Air")

# 设置周期性边界
fdtd.set("periodic", 1)
fdtd.set("periodic x", 1)
fdtd.set("periodic y", 1)
fdtd.set("periodic boundary", "Bloch")

# 设置颜色可视化
fdtd.set("color", [0.8, 0.2, 0.2, 0.8])  # 红色
```

## 注意事项

### 1. 周期性边界条件
- 光栅通常需要周期性边界条件以正确模拟衍射效应
- `periodic` 属性必须设置为 1 以启用周期性
- 对于二维光栅，`periodic x` 和 `periodic y` 都应设置为 1
- `periodic boundary` 类型影响计算精度和收敛速度

### 2. 网格设置
- 光栅周期通常远小于波长，需要精细网格
- 建议在光栅区域使用 `addmesh` 命令添加网格覆盖区
- `mesh order` 影响材料优先级，通常设置为 2 或 3

### 3. 收敛性考虑
- 光栅仿真可能需要更多的时间步长才能收敛
- 对于金属光栅，可能需要更小的网格和时间步长
- 二维光栅的计算量显著大于一维光栅

### 4. 衍射级次
- 光栅周期决定衍射级次：`period < λ/n` 只产生 0 级衍射
- 对于波导耦合，需要设计周期使得特定衍射级次满足相位匹配条件
- 使用 `gratingorder` 命令分析衍射效率

### 5. 材料选择
- 金属光栅（Au, Ag）用于表面等离子体共振
- 介质光栅（Si, SiO₂, TiO₂）用于低损耗器件
- 材料色散影响光栅性能，特别是宽波段应用

## 错误处理

### 常见错误
1. **周期无效**: `period` ≤ 0
   - 解决方案：确保 `period` > 0，通常为波长量级

2. **占空比无效**: `duty cycle` < 0 或 > 1
   - 解决方案：确保 0 ≤ `duty cycle` ≤ 1

3. **尺寸冲突**: `period` > `x span` 或 `y span`
   - 解决方案：确保 `x span` 和 `y span` 足够容纳多个周期

4. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

5. **周期性边界冲突**: 周期性边界与仿真区域边界不兼容
   - 解决方案：确保仿真区域边界类型支持周期性条件

6. **网格生成失败**: 光栅特征尺寸过小导致网格问题
   - 解决方案：增加网格分辨率或调整光栅尺寸

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加光栅
    fdtd.addgrating()
    
    # 配置光栅属性
    fdtd.set("name", "test grating")
    fdtd.set("x span", 5e-6)
    fdtd.set("period", 500e-9)
    fdtd.set("duty cycle", 0.5)
    fdtd.set("height", 100e-9)
    
    # 检查参数有效性
    period = fdtd.get("period")
    duty_cycle = fdtd.get("duty cycle")
    x_span = fdtd.get("x span")
    
    if period <= 0:
        raise ValueError("光栅周期必须 > 0")
    if duty_cycle < 0 or duty_cycle > 1:
        raise ValueError("占空比必须在 0 到 1 之间")
    if x_span < period:
        raise ValueError("X方向尺寸必须至少包含一个完整周期")
    
    # 检查周期性边界设置
    if fdtd.get("periodic") == 1:
        if fdtd.get("periodic x") != 1 and fdtd.get("grating direction") == "x":
            print("警告: X方向光栅但未设置X方向周期性")
    
    # 设置材料
    fdtd.set("material", "Si (Silicon) - Palik")
    fdtd.set("substrate material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值
    fdtd.set("period", 500e-9)
    fdtd.set("duty cycle", 0.5)
    fdtd.set("x span", 1e-6)
    
except Exception as e:
    print(f"光栅创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "period" in str(e).lower():
        print("错误: 周期无效，请检查周期值")
    elif "duty" in str(e).lower() or "cycle" in str(e).lower():
        print("错误: 占空比无效，必须在 0 到 1 之间")
    elif "span" in str(e).lower():
        print("错误: 尺寸无效，请检查跨度值")
    elif "periodic" in str(e).lower():
        print("错误: 周期性边界设置冲突")
    elif "mesh" in str(e).lower():
        print("错误: 网格生成失败，请调整光栅尺寸或网格设置")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（可用于创建简单光栅单元）
- `addplanarsolid`: 添加平面实体（可用于光栅衬底）
- `addwaveguide`: 添加波导（与光栅耦合器配合使用）
- `gratingorder`: 计算光栅衍射级次和效率
- `addmesh`: 添加网格覆盖区（用于光栅区域细化）
- `setnamed`: 按名称设置对象属性
- `select`: 选择对象进行进一步操作

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions
- **有限支持**: varFDTD
- **不支持**: DEVICE, INTERCONNECT

## 应用场景

### 1. 波长分束器
```python
# 创建用于波分复用的光栅
fdtd.addgrating()
fdtd.set("name", "WDM grating")
fdtd.set("x span", 50e-6)       # 长度 50μm
fdtd.set("period", 500e-9)      # 周期 500nm
fdtd.set("duty cycle", 0.5)
fdtd.set("height", 200e-9)
fdtd.set("material", "Si (Silicon) - Palik")
fdtd.set("grating type", "rectangular")
fdtd.set("periodic", 1)
```

### 2. 表面等离子体共振传感器
```python
# 创建金属光栅用于生物传感
fdtd.addgrating()
fdtd.set("name", "SPR grating sensor")
fdtd.set("x span", 20e-6)
fdtd.set("period", 400e-9)      # 金光栅周期
fdtd.set("duty cycle", 0.4)
fdtd.set("height", 50e-9)       # 金层厚度 50nm
fdtd.set("material", "Au (Gold) - CRC")
fdtd.set("substrate material", "SiO2 (Glass) - Palik")
fdtd.set("cladding material", "Water")
fdtd.set("grating type", "rectangular")
fdtd.set("periodic", 1)
```

### 3. 光子晶体LED提取增强
```python
# 创建光子晶体光栅增强LED光提取
fdtd.addgrating()
fdtd.set("name", "PhC LED grating")
fdtd.set("x span", 10e-6)
fdtd.set("y span", 10e-6)
fdtd.set("period", 250e-9)      # 短周期用于可见光
fdtd.set("duty cycle", 0.3)
fdtd.set("height", 100e-9)
fdtd.set("material", "GaN (Gallium nitride)")
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "both")  # 二维光子晶体
fdtd.set("periodic", 1)
fdtd.set("periodic x", 1)
fdtd.set("periodic y", 1)
```

### 4. 超表面光束整形
```python
# 创建超表面光栅用于波前调控
fdtd.addgrating()
fdtd.set("name", "metasurface grating")
fdtd.set("x span", 20e-6)
fdtd.set("y span", 20e-6)
fdtd.set("period", 300e-9)      # 亚波长周期
fdtd.set("duty cycle", 0.5)
fdtd.set("height", 600e-9)      # 高深宽比结构
fdtd.set("material", "TiO2 (Titanium dioxide) - Palik")
fdtd.set("grating type", "rectangular")
fdtd.set("grating direction", "both")
fdtd.set("tilt angle", 0)
fdtd.set("periodic", 1)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `grating direction` = "both" 支持二维光栅 |
| Lumerical 2019a | 新增 `blaze angle` 和 `tilt angle` 属性 |
| Lumerical 2018a | 新增 `grating type` 属性支持多种光栅轮廓 |
| Lumerical 2017a | 首次引入 `addgrating` 命令 |
| 1.1 | 更新日期，完善文档格式，补充应用场景 |

## 参考

1. Lumerical FDTD Solutions 用户指南 - 光栅仿真章节
2. Lumerical 衍射光学元件设计手册
3. 光子晶体和超表面设计原理
4. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*