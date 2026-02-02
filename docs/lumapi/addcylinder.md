# addcylinder

## 概述

`addcylinder` 命令用于在仿真中添加一个圆柱体结构。圆柱体是 Lumerical 中的基本几何形状之一，常用于创建波导、光纤、纳米柱、微柱阵列、光子晶体等光学元件。圆柱体可以沿指定轴（X、Y 或 Z）拉伸，创建具有圆形横截面的柱状结构。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addcylinder;
```

### Python API (Lumapi)
```python
session.addcylinder()
```

## 参数

`addcylinder` 命令没有直接参数，但需要通过后续的 `set` 命令配置圆柱体属性。

## 配置属性

添加圆柱体后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "cylinder" | 圆柱体名称 |
| `x`, `y`, `z` | float | 0 | 圆柱体中心坐标 (m) |
| `radius` | float | 0.5e-6 | 圆柱体半径 (m) |
| `inner radius` | float | 0 | 内半径 (m)，用于创建空心圆柱体 |
| `z span` | float | 1e-6 | 圆柱体高度 (沿指定轴方向) (m) |
| `z` | float | 0 | 圆柱体中心 Z 坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 圆柱体 Z 方向最小/最大坐标 (m) |
| `axis` | string | "z" | 拉伸轴方向："x", "y", "z" |

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

`addcylinder` 命令没有返回值。成功执行后，会在仿真中添加一个圆柱体对象。

## 示例

### 示例 1: 基本圆柱体创建

#### LSF 脚本
```lumerical
// 添加圆柱体
addcylinder;

// 设置几何尺寸
set("name", "Si cylinder");
set("x", 0);
set("y", 0);
set("z", 0);
set("radius", 0.5e-6);     // 半径 0.5μm
set("z span", 2e-6);       // 高度 2μm

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

# 添加圆柱体
fdtd.addcylinder()

# 设置几何尺寸
fdtd.set("name", "Si cylinder")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("radius", 0.5e-6)     # 半径 0.5μm
fdtd.set("z span", 2e-6)       # 高度 2μm

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 空心圆柱体（纳米管）

#### LSF 脚本
```lumerical
// 添加空心圆柱体（纳米管）
addcylinder;
set("name", "carbon nanotube");
set("radius", 10e-9);          // 外半径 10nm
set("inner radius", 8e-9);     // 内半径 8nm，壁厚 2nm
set("z span", 100e-9);         // 长度 100nm
set("material", "C (Carbon) - Palik");

// 设置线框渲染以查看空心结构
set("render type", "wireframe");
set("alpha", 0.7);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addcylinder()
fdtd.set("name", "carbon nanotube")
fdtd.set("radius", 10e-9)          # 外半径 10nm
fdtd.set("inner radius", 8e-9)     # 内半径 8nm，壁厚 2nm
fdtd.set("z span", 100e-9)         # 长度 100nm
fdtd.set("material", "C (Carbon) - Palik")

# 设置线框渲染以查看空心结构
fdtd.set("render type", "wireframe")
fdtd.set("alpha", 0.7)
```

### 示例 3: 沿 X 轴拉伸的圆柱体（水平圆柱）

#### LSF 脚本
```lumerical
// 创建沿 X 轴拉伸的圆柱体
addcylinder;
set("name", "horizontal cylinder");
set("axis", "x");            // 沿 X 轴拉伸
set("radius", 0.2e-6);       // 半径 0.2μm
set("x span", 5e-6);         // 长度 5μm
set("y", 0);
set("z", 0);
set("material", "SiO2 (Glass) - Palik");

// 绕 Y 轴旋转 90 度使圆柱体水平（可选）
set("first axis", "y");
set("rotation 1", 90);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addcylinder()
fdtd.set("name", "horizontal cylinder")
fdtd.set("axis", "x")            # 沿 X 轴拉伸
fdtd.set("radius", 0.2e-6)       # 半径 0.2μm
fdtd.set("x span", 5e-6)         # 长度 5μm
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("material", "SiO2 (Glass) - Palik")

# 绕 Y 轴旋转 90 度使圆柱体水平（可选）
fdtd.set("first axis", "y")
fdtd.set("rotation 1", 90)
```

### 示例 4: 圆柱体阵列（纳米柱光子晶体）

#### LSF 脚本
```lumerical
// 创建圆柱体阵列（光子晶体）
for(i = 0; i < 5; i++) {
    for(j = 0; j < 5; j++) {
        addcylinder;
        set("name", "pillar_" + num2str(i) + "_" + num2str(j));
        set("x", i * 500e-9);    // X 方向周期 500nm
        set("y", j * 500e-9);    // Y 方向周期 500nm
        set("radius", 100e-9);   // 半径 100nm
        set("z span", 300e-9);   // 高度 300nm
        set("material", "Si (Silicon) - Palik");
    }
}
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 创建圆柱体阵列（光子晶体）
for i in range(5):
    for j in range(5):
        fdtd.addcylinder()
        fdtd.set("name", f"pillar_{i}_{j}")
        fdtd.set("x", i * 500e-9)    # X 方向周期 500nm
        fdtd.set("y", j * 500e-9)    # Y 方向周期 500nm
        fdtd.set("radius", 100e-9)   # 半径 100nm
        fdtd.set("z span", 300e-9)   # 高度 300nm
        fdtd.set("material", "Si (Silicon) - Palik")
```

### 示例 5: 旋转圆柱体（倾斜波导）

#### LSF 脚本
```lumerical
// 创建旋转圆柱体（倾斜波导）
addcylinder;
set("name", "tilted waveguide");
set("radius", 250e-9);       // 半径 250nm
set("z span", 5e-6);         // 长度 5μm
set("material", "Si (Silicon) - Palik");

// 绕 X 轴旋转 30 度
set("first axis", "x");
set("rotation 1", 30);

// 绕 Y 轴旋转 15 度（在 X 轴旋转之后）
set("second axis", "y");
set("rotation 2", 15);

// 设置半透明显示
set("alpha", 0.7);
set("render type", "wireframe");
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addcylinder()
fdtd.set("name", "tilted waveguide")
fdtd.set("radius", 250e-9)       # 半径 250nm
fdtd.set("z span", 5e-6)         # 长度 5μm
fdtd.set("material", "Si (Silicon) - Palik")

# 绕 X 轴旋转 30 度
fdtd.set("first axis", "x")
fdtd.set("rotation 1", 30)

# 绕 Y 轴旋转 15 度（在 X 轴旋转之后）
fdtd.set("second axis", "y")
fdtd.set("rotation 2", 15)

# 设置半透明显示
fdtd.set("alpha", 0.7)
fdtd.set("render type", "wireframe")
```

## 注意事项

### 1. 几何定义
- 圆柱体由 `radius` 和 `z span` 定义（或使用 `z min` 和 `z max`）
- `inner radius` > 0 时创建空心圆柱体（管状结构）
- 通过 `axis` 属性可以指定拉伸方向（"x", "y", "z"），默认沿 Z 轴
- 当 `axis` 设置为 "x" 或 "y" 时，相应的跨度属性变为 `x span` 或 `y span`

### 2. 网格考虑
- 圆柱体曲面需要精细的网格离散化，特别是在边界处
- 对于细长圆柱体（高宽比大），可能需要沿拉伸方向增加网格密度
- 空心圆柱体需要更精细的网格以解析薄壁结构
- 考虑使用 `addmesh` 命令在圆柱体区域添加网格覆盖区

### 3. 旋转与方向
- 默认拉伸方向为 Z 轴，可通过 `axis` 属性更改
- 旋转属性按 `first axis` → `second axis` → `third axis` 顺序应用
- 复杂旋转可能需要按特定顺序应用旋转轴
- 当 `axis` 不是 "z" 时，可能需要额外的旋转来正确定向

### 4. 性能优化
- 大量圆柱体结构（如光子晶体阵列）可能显著增加网格生成时间
- 考虑使用对称性减少仿真区域
- 对于周期性阵列，可考虑使用周期性边界条件
- 对于参数扫描，重用网格可以提高效率

### 5. 材料设置
- 圆柱体材料可以来自材料数据库或自定义折射率
- 自定义折射率材料需设置 `material` 为 "<Object defined dielectric>" 并指定 `index`
- 对于多层圆柱体（核壳结构），可能需要多个圆柱体对象叠加

## 错误处理

### 常见错误
1. **半径无效**: `radius` ≤ 0 或 `inner radius` ≥ `radius`
   - 解决方案：确保 `radius` > 0 且 `inner radius` < `radius`

2. **跨度无效**: `z span` ≤ 0 或 `z min` ≥ `z max`
   - 解决方案：确保 `z span` > 0 且 `z min` < `z max`

3. **拉伸轴无效**: `axis` 不是 "x", "y", "z" 之一
   - 解决方案：检查 `axis` 属性值

4. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

5. **网格生成失败**: 圆柱体尺寸过小或壁厚过薄导致网格问题
   - 解决方案：调整圆柱体尺寸，确保足够的网格分辨率

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加圆柱体
    fdtd.addcylinder()
    
    # 配置圆柱体属性
    fdtd.set("name", "test cylinder")
    fdtd.set("radius", 1e-6)
    fdtd.set("inner radius", 0.5e-6)
    fdtd.set("z span", 2e-6)
    
    # 检查参数有效性
    radius = fdtd.get("radius")
    inner_radius = fdtd.get("inner radius")
    z_span = fdtd.get("z span")
    
    if radius <= 0:
        raise ValueError("半径必须 > 0")
    if inner_radius >= radius:
        raise ValueError("内半径必须小于外半径")
    if z_span <= 0:
        raise ValueError("高度必须 > 0")
    
    # 设置材料
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    fdtd.set("radius", 0.5e-6)
    fdtd.set("inner radius", 0)
    fdtd.set("z span", 1e-6)
    
except Exception as e:
    print(f"圆柱体创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查内外半径值")
    elif "span" in str(e).lower() or "height" in str(e).lower():
        print("错误: 高度无效，请检查跨度值")
    elif "axis" in str(e).lower():
        print("错误: 拉伸轴无效，必须是 'x', 'y', 'z' 之一")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（长方体）
- `addsphere`: 添加球体
- `addring`: 添加环形结构
- `addprism`: 添加棱柱
- `addwaveguide`: 添加波导结构
- `addmesh`: 添加网格覆盖区（用于圆柱体区域细化）
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions
- **完全支持**: 所有 Lumerical 产品
- **通用命令**: 在所有产品中功能一致

## 应用场景

### 1. 硅波导设计
```python
# 创建硅波导（圆柱形近似）
fdtd.addcylinder()
fdtd.set("name", "Si waveguide")
fdtd.set("radius", 250e-9)       # 半径 250nm
fdtd.set("z span", 10e-6)        # 长度 10μm
fdtd.set("material", "Si (Silicon) - Palik")
```

### 2. 纳米柱增强发光
```python
# 创建金纳米柱用于等离子增强
fdtd.addcylinder()
fdtd.set("name", "Au nanorod")
fdtd.set("radius", 20e-9)        # 半径 20nm
fdtd.set("z span", 50e-9)        # 长度 50nm
fdtd.set("material", "Au (Gold) - Johnson and Christy")
```

### 3. 光子晶体平板
```python
# 创建圆柱体阵列形成光子晶体平板
rows, cols = 10, 10
for i in range(rows):
    for j in range(cols):
        fdtd.addcylinder()
        fdtd.set("name", f"pc_pillar_{i}_{j}")
        fdtd.set("x", (i - rows/2) * 400e-9)
        fdtd.set("y", (j - cols/2) * 400e-9)
        fdtd.set("radius", 150e-9)
        fdtd.set("z span", 220e-9)
        fdtd.set("material", "Si (Silicon) - Palik")
```

### 4. 光纤耦合器
```python
# 创建光纤纤芯（圆柱体）
fdtd.addcylinder()
fdtd.set("name", "fiber core")
fdtd.set("radius", 4.5e-6)       # 半径 4.5μm (SMF-28)
fdtd.set("z span", 10e-6)        # 长度 10μm
fdtd.set("material", "SiO2 (Glass) - Palik")
fdtd.set("index", 1.444)         # 自定义折射率
fdtd.set("index units", "microns")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `axis` 属性支持 X/Y 轴拉伸 |
| Lumerical 2019a | 改进圆柱体网格生成算法 |
| Lumerical 2018a | 新增 `inner radius` 属性支持空心圆柱体 |
| 1.1 | 更新日期，完善文档格式，添加应用场景示例 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 圆柱体网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*