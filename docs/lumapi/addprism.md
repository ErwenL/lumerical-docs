# addprism

## 概述

`addprism` 命令用于在仿真中添加一个棱柱结构。棱柱是具有多边形横截面并沿指定方向拉伸形成的三维几何体，常用于创建光学棱镜、波导耦合器、衍射光栅基底、光子晶体结构等光学元件。棱柱可以是三棱柱、四棱柱（长方体）、六棱柱等多边形柱体。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addprism;
```

### Python API (Lumapi)
```python
session.addprism()
```

## 参数

`addprism` 命令没有直接参数，但需要通过后续的 `set` 命令配置棱柱属性。

## 配置属性

添加棱柱后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "prism" | 棱柱名称 |
| `x`, `y`, `z` | float | 0 | 棱柱中心坐标 (m) |
| `number of sides` | int | 6 | 多边形边数（≥3） |
| `radius` | float | 1e-6 | 多边形外接圆半径 (m) |
| `z span` | float | 1e-6 | 棱柱高度 (沿 Z 方向拉伸) (m) |
| `z` | float | 0 | 棱柱中心 Z 坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 棱柱 Z 方向最小/最大坐标 (m) |
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

`addprism` 命令没有返回值。成功执行后，会在仿真中添加一个棱柱对象。

## 示例

### 示例 1: 基本三棱柱创建

#### LSF 脚本
```lumerical
// 添加三棱柱
addprism;

// 设置几何尺寸
set("name", "triangular prism");
set("x", 0);
set("y", 0);
set("z", 0);
set("number of sides", 3);   // 三角形截面
set("radius", 2e-6);         // 外接圆半径 2μm
set("z span", 5e-6);         // 高度 5μm

// 设置材料
set("material", "SiO2 (Glass) - Palik");

// 设置网格顺序
set("override mesh order from material database", 1);
set("mesh order", 2);
```

#### Python API
```python
import lumapi

# 创建会话（FDTD 或 MODE）
fdtd = lumapi.FDTD()

# 添加棱柱
fdtd.addprism()

# 设置几何尺寸
fdtd.set("name", "triangular prism")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("number of sides", 3)   # 三角形截面
fdtd.set("radius", 2e-6)         # 外接圆半径 2μm
fdtd.set("z span", 5e-6)         # 高度 5μm

# 设置材料
fdtd.set("material", "SiO2 (Glass) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 六棱柱光子晶体

#### LSF 脚本
```lumerical
// 创建六棱柱阵列（光子晶体）
for(i = 0; i < 5; i++) {
    for(j = 0; j < 5; j++) {
        addprism;
        set("name", "hex_pillar_" + num2str(i) + "_" + num2str(j));
        set("x", i * 3e-6);          // X 方向周期 3μm
        set("y", j * 3e-6);          // Y 方向周期 3μm
        set("number of sides", 6);   // 六边形截面
        set("radius", 1e-6);         // 半径 1μm
        set("z span", 2e-6);         // 高度 2μm
        set("material", "Si (Silicon) - Palik");
    }
}
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 创建六棱柱阵列（光子晶体）
for i in range(5):
    for j in range(5):
        fdtd.addprism()
        fdtd.set("name", f"hex_pillar_{i}_{j}")
        fdtd.set("x", i * 3e-6)          # X 方向周期 3μm
        fdtd.set("y", j * 3e-6)          # Y 方向周期 3μm
        fdtd.set("number of sides", 6)   # 六边形截面
        fdtd.set("radius", 1e-6)         # 半径 1μm
        fdtd.set("z span", 2e-6)         # 高度 2μm
        fdtd.set("material", "Si (Silicon) - Palik")
```

### 示例 3: 沿 X 轴拉伸的棱柱（水平棱柱）

#### LSF 脚本
```lumerical
// 创建沿 X 轴拉伸的棱柱
addprism;
set("name", "horizontal prism");
set("axis", "x");            // 沿 X 轴拉伸
set("number of sides", 4);   // 四边形截面（长方体）
set("radius", 1e-6);         // 截面半径 1μm
set("x span", 10e-6);        // 长度 10μm
set("y", 0);
set("z", 0);
set("material", "Si (Silicon) - Palik");

// 绕 Y 轴旋转 90 度使棱柱水平
set("first axis", "y");
set("rotation 1", 90);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprism()
fdtd.set("name", "horizontal prism")
fdtd.set("axis", "x")            # 沿 X 轴拉伸
fdtd.set("number of sides", 4)   # 四边形截面（长方体）
fdtd.set("radius", 1e-6)         # 截面半径 1μm
fdtd.set("x span", 10e-6)        # 长度 10μm
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("material", "Si (Silicon) - Palik")

# 绕 Y 轴旋转 90 度使棱柱水平
fdtd.set("first axis", "y")
fdtd.set("rotation 1", 90)
```

### 示例 4: 渐变折射率棱柱（GRIN 棱镜）

#### LSF 脚本
```lumerical
// 创建渐变折射率棱柱
addprism;
set("name", "GRIN prism");
set("number of sides", 8);   // 八边形截面
set("radius", 5e-6);         // 半径 5μm
set("z span", 10e-6);        // 高度 10μm

// 使用自定义材料定义渐变折射率
set("material", "<Object defined dielectric>");
set("index", 1.5);           // 中心折射率
set("index units", "microns");

// 设置渐变折射率分布（通过脚本控制）
// 实际应用中可能需要通过材料数据库定义梯度材料
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprism()
fdtd.set("name", "GRIN prism")
fdtd.set("number of sides", 8)   # 八边形截面
fdtd.set("radius", 5e-6)         # 半径 5μm
fdtd.set("z span", 10e-6)        # 高度 10μm

# 使用自定义材料定义渐变折射率
fdtd.set("material", "<Object defined dielectric>")
fdtd.set("index", 1.5)           # 中心折射率
fdtd.set("index units", "microns")

# 注意：实际渐变折射率可能需要通过材料数据库或脚本控制实现
```

### 示例 5: 旋转棱柱（倾斜棱镜）

#### LSF 脚本
```lumerical
// 创建旋转棱柱
addprism;
set("name", "tilted prism");
set("number of sides", 5);   // 五边形截面
set("radius", 3e-6);         // 半径 3μm
set("z span", 4e-6);         // 高度 4μm
set("material", "Si3N4 (Silicon Nitride) - Luke");

// 绕 X 轴旋转 45 度
set("first axis", "x");
set("rotation 1", 45);

// 绕 Z 轴旋转 30 度
set("second axis", "z");
set("rotation 2", 30);

// 设置半透明显示
set("alpha", 0.7);
set("render type", "wireframe");
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addprism()
fdtd.set("name", "tilted prism")
fdtd.set("number of sides", 5)   # 五边形截面
fdtd.set("radius", 3e-6)         # 半径 3μm
fdtd.set("z span", 4e-6)         # 高度 4μm
fdtd.set("material", "Si3N4 (Silicon Nitride) - Luke")

# 绕 X 轴旋转 45 度
fdtd.set("first axis", "x")
fdtd.set("rotation 1", 45)

# 绕 Z 轴旋转 30 度
fdtd.set("second axis", "z")
fdtd.set("rotation 2", 30)

# 设置半透明显示
fdtd.set("alpha", 0.7)
fdtd.set("render type", "wireframe")
```

## 注意事项

### 1. 几何定义
- 棱柱的多边形边数必须 ≥3，边数越多截面越接近圆形
- `radius` 定义多边形外接圆半径（顶点到中心的距离）
- `z span` 定义沿 `axis` 指定方向的拉伸长度
- 通过 `axis` 属性可以指定拉伸方向（"x", "y", "z"）

### 2. 网格考虑
- 多边形截面在网格离散化时可能产生非均匀网格，特别是边数较少时
- 建议在棱柱边缘区域使用 `addmesh` 添加网格覆盖区提高分辨率
- 对于细长棱柱（高宽比大），可能需要沿拉伸方向增加网格密度

### 3. 旋转与方向
- 默认拉伸方向为 Z 轴，可通过 `axis` 属性更改
- 旋转属性按 `first axis` → `second axis` → `third axis` 顺序应用
- 复杂旋转可能需要按特定顺序应用旋转轴

### 4. 性能优化
- 大量棱柱结构（如光子晶体阵列）可能显著增加网格生成时间
- 考虑使用对称性减少仿真区域
- 对于周期性阵列，可考虑使用周期性边界条件

### 5. 材料设置
- 棱柱材料可以来自材料数据库或自定义折射率
- 自定义折射率材料需设置 `material` 为 "<Object defined dielectric>" 并指定 `index`
- 渐变折射率材料可能需要通过脚本或外部材料定义实现

## 错误处理

### 常见错误
1. **边数无效**: `number of sides` < 3
   - 解决方案：确保边数 ≥3

2. **半径无效**: `radius` ≤ 0
   - 解决方案：确保半径 > 0

3. **拉伸轴无效**: `axis` 不是 "x", "y", "z" 之一
   - 解决方案：检查 `axis` 属性值

4. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

5. **网格生成失败**: 棱柱尺寸过小或形状过于复杂导致网格问题
   - 解决方案：调整棱柱尺寸，确保足够的网格分辨率

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加棱柱
    fdtd.addprism()
    
    # 配置棱柱属性
    fdtd.set("name", "test prism")
    fdtd.set("number of sides", 4)
    fdtd.set("radius", 1e-6)
    fdtd.set("z span", 2e-6)
    
    # 检查参数有效性
    sides = fdtd.get("number of sides")
    radius = fdtd.get("radius")
    
    if sides < 3:
        raise ValueError("边数必须 ≥3")
    if radius <= 0:
        raise ValueError("半径必须 > 0")
    
    # 设置材料
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    fdtd.set("number of sides", 6)
    fdtd.set("radius", 1e-6)
    
except Exception as e:
    print(f"棱柱创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查半径值")
    elif "side" in str(e).lower() or "number" in str(e).lower():
        print("错误: 边数无效，边数必须 ≥3")
    elif "axis" in str(e).lower():
        print("错误: 拉伸轴无效，必须是 'x', 'y', 'z' 之一")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（长方体）
- `addcylinder`: 添加圆柱体
- `addring`: 添加环形结构
- `addsphere`: 添加球体
- `addwaveguide`: 添加波导结构
- `addmesh`: 添加网格覆盖区（用于棱柱区域细化）
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions
- **完全支持**: 所有 Lumerical 产品
- **通用命令**: 在所有产品中功能一致

## 应用场景

### 1. 光学棱镜设计
```python
# 创建三棱镜用于光束偏转
fdtd.addprism()
fdtd.set("name", "beam steering prism")
fdtd.set("number of sides", 3)   # 三角形截面
fdtd.set("radius", 10e-6)        # 大尺寸棱镜
fdtd.set("z span", 2e-6)         # 薄片
fdtd.set("material", "SiO2 (Glass) - Palik")
```

### 2. 光子晶体波导
```python
# 创建六棱柱光子晶体波导
for i in range(10):
    for j in range(3):
        fdtd.addprism()
        fdtd.set("name", f"pc_hex_{i}_{j}")
        fdtd.set("x", i * 500e-9)    # 500nm 周期
        fdtd.set("y", j * 500e-9)
        fdtd.set("number of sides", 6)
        fdtd.set("radius", 200e-9)   # 200nm 半径
        fdtd.set("z span", 220e-9)   # 硅层厚度
        fdtd.set("material", "Si (Silicon) - Palik")
```

### 3. 多面体纳米颗粒
```python
# 创建多面体纳米颗粒用于散射增强
fdtd.addprism()
fdtd.set("name", "nanoparticle")
fdtd.set("number of sides", 8)   # 八面体近似
fdtd.set("radius", 100e-9)       # 100nm 半径
fdtd.set("z span", 100e-9)       # 高度 100nm
fdtd.set("material", "Au (Gold) - Johnson and Christy")
```

### 4. 微结构光学元件
```python
# 创建微结构透镜（多棱柱阵列）
rows, cols = 5, 5
for i in range(rows):
    for j in range(cols):
        fdtd.addprism()
        fdtd.set("name", f"microlens_{i}_{j}")
        fdtd.set("x", (i - rows/2) * 5e-6)
        fdtd.set("y", (j - cols/2) * 5e-6)
        fdtd.set("number of sides", 12)  # 近似圆形
        fdtd.set("radius", 2e-6)
        fdtd.set("z span", 3e-6)
        fdtd.set("material", "PMMA (Polymer)")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `axis` 属性支持 X/Y 轴拉伸 |
| Lumerical 2019a | 改进多边形网格生成算法 |
| Lumerical 2018a | 新增 `number of sides` 属性 |
| 1.1 | 更新日期，完善文档格式 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 多边形网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*