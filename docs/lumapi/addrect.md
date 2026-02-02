# addrect

## 概述

`addrect` 命令用于在仿真中添加一个矩形结构。矩形是 Lumerical 中最常用的基本几何形状之一，可用于创建波导、平板、电极等各种结构。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addrect;
```

### Python API (Lumapi)
```python
session.addrect()
```

## 参数

`addrect` 命令没有直接参数，但需要通过后续的 `set` 命令配置矩形属性。

## 配置属性

添加矩形后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "rectangle" | 矩形名称 |
| `x`, `y`, `z` | float | 0 | 矩形中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 矩形各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 矩形 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 矩形 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 矩形 Z 方向最小/最大坐标 (m) |

### 2. 材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material` | string | "<Object defined dielectric>" | 材料名称 |
| `index` | float | 1.0 | 折射率（当 material 为 "<Object defined dielectric>" 时使用） |
| `index units` | string | "microns" | 折射率单位："m", "microns", "nm" |

### 3. 网格与渲染属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override mesh order from material database` | int | 0 | 是否覆盖材料数据库中的网格顺序 |
| `mesh order` | int | 2 | 网格顺序（需先启用覆盖） |
| `render type` | string | "detailed" | 渲染类型："detailed", "wireframe" |
| `alpha` | float | 1.0 | 透明度 (0.0-1.0) |
| `color` | array[4] | [0.5, 0.5, 0.5, 1.0] | RGBA 颜色值 |

### 4. 旋转属性（可选）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `first axis` | string | "none" | 第一旋转轴："none", "x", "y", "z" |
| `rotation 1` | float | 0 | 第一旋转角度 (度) |
| `second axis` | string | "none" | 第二旋转轴 |
| `rotation 2` | float | 0 | 第二旋转角度 (度) |
| `third axis` | string | "none" | 第三旋转轴 |
| `rotation 3` | float | 0 | 第三旋转角度 (度) |

## 返回值

`addrect` 命令没有返回值。成功执行后，会在仿真中添加一个矩形对象。

## 示例

### 示例 1: 基本矩形创建

#### LSF 脚本
```lumerical
// 添加矩形
addrect;

// 设置几何尺寸
set("name", "Si waveguide");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5e-6);    // 长度 5μm
set("y span", 500e-9);  // 宽度 500nm
set("z span", 220e-9);  // 高度 220nm

// 设置材料
set("material", "Si (Silicon) - Palik");

// 设置网格顺序
set("override mesh order from material database", 1);
set("mesh order", 2);
```

#### Python API
```python
import lumapi

# 创建会话（FDTD 或 MODE）
fdtd = lumapi.FDTD()

# 添加矩形
fdtd.addrect()

# 设置几何尺寸
fdtd.set("name", "Si waveguide")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 5e-6)    # 长度 5μm
fdtd.set("y span", 500e-9)  # 宽度 500nm
fdtd.set("z span", 220e-9)  # 高度 220nm

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 使用自定义折射率

#### LSF 脚本
```lumerical
addrect;
set("name", "custom dielectric");
set("x span", 2e-6);
set("y span", 1e-6);
set("z span", 0.5e-6);

// 使用自定义折射率而不是材料数据库
set("material", "<Object defined dielectric>");
set("index", 3.45);          // 硅的折射率
set("index units", "microns");

// 设置颜色为蓝色半透明
set("color", [0, 0, 1, 0.5]);
set("alpha", 0.5);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addrect()
fdtd.set("name", "custom dielectric")
fdtd.set("x span", 2e-6)
fdtd.set("y span", 1e-6)
fdtd.set("z span", 0.5e-6)

# 使用自定义折射率而不是材料数据库
fdtd.set("material", "<Object defined dielectric>")
fdtd.set("index", 3.45)          # 硅的折射率
fdtd.set("index units", "microns")

# 设置颜色为蓝色半透明
fdtd.set("color", [0, 0, 1, 0.5])
fdtd.set("alpha", 0.5)
```

### 示例 3: 旋转矩形

#### LSF 脚本
```lumerical
addrect;
set("name", "rotated rectangle");
set("x span", 3e-6);
set("y span", 1e-6);
set("z span", 0.2e-6);

// 设置材料
set("material", "SiO2 (Glass) - Palik");

// 绕 Z 轴旋转 45 度
set("first axis", "z");
set("rotation 1", 45);

// 绕 X 轴旋转 30 度（在 Z 轴旋转之后）
set("second axis", "x");
set("rotation 2", 30);

// 设置渲染为线框模式
set("render type", "wireframe");
set("alpha", 0.7);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addrect()
fdtd.set("name", "rotated rectangle")
fdtd.set("x span", 3e-6)
fdtd.set("y span", 1e-6)
fdtd.set("z span", 0.2e-6)

# 设置材料
fdtd.set("material", "SiO2 (Glass) - Palik")

# 绕 Z 轴旋转 45 度
fdtd.set("first axis", "z")
fdtd.set("rotation 1", 45)

# 绕 X 轴旋转 30 度（在 Z 轴旋转之后）
fdtd.set("second axis", "x")
fdtd.set("rotation 2", 30)

# 设置渲染为线框模式
fdtd.set("render type", "wireframe")
fdtd.set("alpha", 0.7)
```

### 示例 4: 创建多个矩形（堆叠结构）

#### LSF 脚本
```lumerical
// 底层二氧化硅
addrect;
set("name", "SiO2 substrate");
set("x span", 10e-6);
set("y span", 10e-6);
set("z span", 2e-6);
set("z", -1e-6);  // 中心在 z = -1μm
set("material", "SiO2 (Glass) - Palik");

// 中间硅层
addrect;
set("name", "Si device layer");
set("x span", 5e-6);
set("y span", 5e-6);
set("z span", 220e-9);
set("z", 110e-9);  // 中心在 z = 110nm
set("material", "Si (Silicon) - Palik");

// 顶层氧化层
addrect;
set("name", "SiO2 cladding");
set("x span", 10e-6);
set("y span", 10e-6);
set("z span", 1e-6);
set("z", 720e-9);  // 中心在 z = 720nm
set("material", "SiO2 (Glass) - Palik");
set("alpha", 0.3);  // 半透明显示
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 底层二氧化硅
fdtd.addrect()
fdtd.set("name", "SiO2 substrate")
fdtd.set("x span", 10e-6)
fdtd.set("y span", 10e-6)
fdtd.set("z span", 2e-6)
fdtd.set("z", -1e-6)  # 中心在 z = -1μm
fdtd.set("material", "SiO2 (Glass) - Palik")

# 中间硅层
fdtd.addrect()
fdtd.set("name", "Si device layer")
fdtd.set("x span", 5e-6)
fdtd.set("y span", 5e-6)
fdtd.set("z span", 220e-9)
fdtd.set("z", 110e-9)  # 中心在 z = 110nm
fdtd.set("material", "Si (Silicon) - Palik")

# 顶层氧化层
fdtd.addrect()
fdtd.set("name", "SiO2 cladding")
fdtd.set("x span", 10e-6)
fdtd.set("y span", 10e-6)
fdtd.set("z span", 1e-6)
fdtd.set("z", 720e-9)  # 中心在 z = 720nm
fdtd.set("material", "SiO2 (Glass) - Palik")
fdtd.set("alpha", 0.3)  # 半透明显示
```

### 示例 5: 使用 min/max 坐标而非中心/跨度

#### LSF 脚本
```lumerical
addrect;
set("name", "asymmetric rectangle");

// 使用最小/最大坐标定义矩形
set("x min", -2e-6);
set("x max", 3e-6);    // 总跨度 5μm，中心在 0.5μm
set("y min", -1e-6);
set("y max", 1e-6);    // 总跨度 2μm，中心在 0
set("z min", 0);
set("z max", 500e-9);  // 总跨度 500nm，中心在 250nm

set("material", "Au (Gold) - Johnson and Christy");
set("render type", "wireframe");
set("color", [1, 0.84, 0, 1]);  // 金色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addrect()
fdtd.set("name", "asymmetric rectangle")

# 使用最小/最大坐标定义矩形
fdtd.set("x min", -2e-6)
fdtd.set("x max", 3e-6)    # 总跨度 5μm，中心在 0.5μm
fdtd.set("y min", -1e-6)
fdtd.set("y max", 1e-6)    # 总跨度 2μm，中心在 0
fdtd.set("z min", 0)
fdtd.set("z max", 500e-9)  # 总跨度 500nm，中心在 250nm

fdtd.set("material", "Au (Gold) - Johnson and Christy")
fdtd.set("render type", "wireframe")
fdtd.set("color", [1, 0.84, 0, 1])  # 金色
```

## 注意事项

### 1. 坐标系统
- Lumerical 使用右手笛卡尔坐标系
- 默认单位是米 (m)，但通常使用微米 (μm) 或纳米 (nm) 更方便
- 可以使用 `x span`/`y span`/`z span` 或 `x min`/`x max` 等定义尺寸

### 2. 材料选择
- 可以从材料数据库选择预定义材料
- 使用 `<Object defined dielectric>` 并设置 `index` 属性创建自定义材料
- 材料名称区分大小写

### 3. 网格顺序
- 网格顺序决定不同材料交界处的网格优先级
- 较高网格顺序的材料优先
- 默认从材料数据库获取，但可以覆盖

### 4. 旋转顺序
- 旋转按 `first axis` → `second axis` → `third axis` 顺序应用
- 旋转角度单位为度
- 复杂的旋转可能需要按特定顺序应用

### 5. 性能考虑
- 大量矩形结构可能增加网格生成时间
- 使用简单几何近似复杂形状可以提高性能
- 考虑使用 `addplanarsolid` 或 `addwaveguide` 创建更复杂的形状

## 错误处理

### 常见错误
1. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

2. **无效坐标**: 最小坐标大于最大坐标
   - 解决方案：确保 `x min` < `x max`, `y min` < `y max`, `z min` < `z max`

3. **网格顺序冲突**: 多个对象重叠且网格顺序相同
   - 解决方案：为重叠对象设置不同的网格顺序

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加矩形
    fdtd.addrect()
    
    # 配置矩形属性
    fdtd.set("name", "test rectangle")
    fdtd.set("x span", 1e-6)
    # ... 其他设置
    
except Exception as e:
    print(f"矩形创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "coordinate" in str(e).lower():
        print("错误: 坐标无效，请检查最小/最大坐标")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addsphere`: 添加球体
- `addcylinder`: 添加圆柱体
- `addring`: 添加环形结构
- `addwaveguide`: 添加波导结构
- `addplanarsolid`: 添加平面实体
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions, DEVICE
- **完全支持**: 所有 Lumerical 产品
- **通用命令**: 在所有产品中功能一致

## 应用场景

### 1. 波导结构
```python
# 创建硅波导
fdtd.addrect()
fdtd.set("name", "Si waveguide")
fdtd.set("x span", 10e-6)    # 长度
fdtd.set("y span", 500e-9)   # 宽度
fdtd.set("z span", 220e-9)   # 高度
fdtd.set("material", "Si (Silicon) - Palik")
```

### 2. 电极与接触
```python
# 创建金属电极
fdtd.addrect()
fdtd.set("name", "metal contact")
fdtd.set("x span", 2e-6)
fdtd.set("y span", 100e-9)   # 薄层金属
fdtd.set("z span", 1e-6)
fdtd.set("material", "Al (Aluminium) - Palik")
```

### 3. 基底与包层
```python
# 创建二氧化硅基底
fdtd.addrect()
fdtd.set("name", "SiO2 substrate")
fdtd.set("x span", 20e-6)
fdtd.set("y span", 20e-6)
fdtd.set("z span", 2e-6)
fdtd.set("z", -1e-6)  # 向下偏移
fdtd.set("material", "SiO2 (Glass) - Palik")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `color` 属性直接设置 |
| Lumerical 2019a | 改进旋转操作性能 |
| Lumerical 2018a | 新增 `index units` 属性 |
| 1.1 | 更新日期，完善文档格式 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 材料数据库文档
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*