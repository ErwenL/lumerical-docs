# addplanarsolid

## 概述

`addplanarsolid` 命令用于在仿真中添加一个平面实体结构。平面实体是具有多边形横截面并沿指定方向拉伸形成的三维几何体，常用于创建平板波导、多层结构、平面光栅、光子集成电路基底等光学元件。平面实体类似于棱柱，但横截面可以是任意多边形，通常用于创建具有复杂轮廓的平面结构。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addplanarsolid;
```

### Python API (Lumapi)
```python
session.addplanarsolid()
```

## 参数

`addplanarsolid` 命令没有直接参数，但需要通过后续的 `set` 命令配置平面实体属性。

## 配置属性

添加平面实体后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "planar solid" | 平面实体名称 |
| `x`, `y`, `z` | float | 0 | 平面实体中心坐标 (m) |
| `vertices` | array[N][2] | [[-0.5e-6, -0.5e-6], [0.5e-6, -0.5e-6], [0.5e-6, 0.5e-6], [-0.5e-6, 0.5e-6]] | 多边形顶点坐标 (m)，定义 XY 平面横截面 |
| `z span` | float | 1e-6 | 平面实体厚度 (沿 Z 方向) (m) |
| `z` | float | 0 | 平面实体中心 Z 坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 平面实体 Z 方向最小/最大坐标 (m) |
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

`addplanarsolid` 命令没有返回值。成功执行后，会在仿真中添加一个平面实体对象。

## 示例

### 示例 1: 基本平面实体创建

#### LSF 脚本
```lumerical
// 添加平面实体
addplanarsolid;

// 设置几何尺寸
set("name", "Si planar slab");
set("x", 0);
set("y", 0);
set("z", 0);

// 设置顶点（矩形横截面）
set("vertices", [[-5e-6, -2e-6], [5e-6, -2e-6], [5e-6, 2e-6], [-5e-6, 2e-6]]);
set("z span", 220e-9);      // 厚度 220nm

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

# 添加平面实体
fdtd.addplanarsolid()

# 设置几何尺寸
fdtd.set("name", "Si planar slab")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)

# 设置顶点（矩形横截面）
vertices = [
    [-5e-6, -2e-6],
    [5e-6, -2e-6],
    [5e-6, 2e-6],
    [-5e-6, 2e-6]
]
fdtd.set("vertices", vertices)
fdtd.set("z span", 220e-9)      # 厚度 220nm

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: L形平面波导

#### LSF 脚本
```lumerical
// 创建 L 形平面波导
addplanarsolid;
set("name", "L-shaped waveguide");

// 定义 L 形横截面顶点
vertices = [
    [-5e-6, -0.5e-6],   // 左下
    [0, -0.5e-6],       // 右下（水平段末端）
    [0, 0.5e-6],        // 右上（垂直段起点）
    [5e-6, 0.5e-6],     // 右上（水平段末端）
    [5e-6, -0.5e-6],    // 右下（垂直段终点）
    [-5e-6, -0.5e-6]    // 闭合
];
set("vertices", vertices);
set("z span", 220e-9);      // 厚度 220nm
set("material", "Si (Silicon) - Palik");

// 设置线框渲染
set("render type", "wireframe");
set("alpha", 0.7);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addplanarsolid()
fdtd.set("name", "L-shaped waveguide")

# 定义 L 形横截面顶点
vertices = [
    [-5e-6, -0.5e-6],   # 左下
    [0, -0.5e-6],       # 右下（水平段末端）
    [0, 0.5e-6],        # 右上（垂直段起点）
    [5e-6, 0.5e-6],     # 右上（水平段末端）
    [5e-6, -0.5e-6],    # 右下（垂直段终点）
    [-5e-6, -0.5e-6]    # 闭合
]
fdtd.set("vertices", vertices)
fdtd.set("z span", 220e-9)      # 厚度 220nm
fdtd.set("material", "Si (Silicon) - Palik")

# 设置线框渲染
fdtd.set("render type", "wireframe")
fdtd.set("alpha", 0.7)
```

### 示例 3: 沿 X 轴拉伸的平面实体（垂直平板）

#### LSF 脚本
```lumerical
// 创建沿 X 轴拉伸的平面实体（垂直平板）
addplanarsolid;
set("name", "vertical slab");
set("axis", "x");            // 沿 X 轴拉伸

// 定义 YZ 平面横截面（矩形）
set("vertices", [[-2e-6, -5e-6], [2e-6, -5e-6], [2e-6, 5e-6], [-2e-6, 5e-6]]);
set("x span", 220e-9);       // 厚度 220nm（沿 X 方向）
set("y", 0);
set("z", 0);
set("material", "SiO2 (Glass) - Palik");

// 绕 Y 轴旋转 90 度使平板垂直（可选）
set("first axis", "y");
set("rotation 1", 90);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addplanarsolid()
fdtd.set("name", "vertical slab")
fdtd.set("axis", "x")            # 沿 X 轴拉伸

# 定义 YZ 平面横截面（矩形）
vertices = [
    [-2e-6, -5e-6],
    [2e-6, -5e-6],
    [2e-6, 5e-6],
    [-2e-6, 5e-6]
]
fdtd.set("vertices", vertices)
fdtd.set("x span", 220e-9)       # 厚度 220nm（沿 X 方向）
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("material", "SiO2 (Glass) - Palik")

# 绕 Y 轴旋转 90 度使平板垂直（可选）
fdtd.set("first axis", "y")
fdtd.set("rotation 1", 90)
```

### 示例 4: 复杂多边形平面实体（星形结构）

#### LSF 脚本
```lumerical
// 创建星形平面实体
addplanarsolid;
set("name", "star structure");

// 生成星形顶点
n_points = 10;
outer_radius = 3e-6;
inner_radius = 1.5e-6;
vertices = [];
for(i = 0; i < n_points; i++) {
    angle = 2*pi*i/n_points;
    if(i % 2 == 0) {
        // 外点
        x = outer_radius * cos(angle);
        y = outer_radius * sin(angle);
    } else {
        // 内点
        x = inner_radius * cos(angle);
        y = inner_radius * sin(angle);
    }
    vertices = [vertices; [x, y]];
}
set("vertices", vertices);
set("z span", 500e-9);       // 厚度 500nm
set("material", "Si3N4 (Silicon Nitride) - Luke");

// 设置颜色和透明度
set("color", [0.8, 0.2, 0.2, 0.6]);  // 红色半透明
set("alpha", 0.6);
```

#### Python API
```python
import numpy as np

fdtd = lumapi.FDTD()
fdtd.addplanarsolid()
fdtd.set("name", "star structure")

# 生成星形顶点
n_points = 10
outer_radius = 3e-6
inner_radius = 1.5e-6
vertices = []
for i in range(n_points):
    angle = 2 * np.pi * i / n_points
    if i % 2 == 0:
        # 外点
        x = outer_radius * np.cos(angle)
        y = outer_radius * np.sin(angle)
    else:
        # 内点
        x = inner_radius * np.cos(angle)
        y = inner_radius * np.sin(angle)
    vertices.append([x, y])

fdtd.set("vertices", vertices)
fdtd.set("z span", 500e-9)       # 厚度 500nm
fdtd.set("material", "Si3N4 (Silicon Nitride) - Luke")

# 设置颜色和透明度
fdtd.set("color", [0.8, 0.2, 0.2, 0.6])  # 红色半透明
fdtd.set("alpha", 0.6)
```

### 示例 5: 平面实体阵列（光子晶体平板）

#### LSF 脚本
```lumerical
// 创建平面实体阵列（光子晶体平板）
for(i = 0; i < 5; i++) {
    for(j = 0; j < 5; j++) {
        addplanarsolid;
        set("name", "pc_slab_" + num2str(i) + "_" + num2str(j));
        
        // 每个单元为六边形平面实体
        radius = 200e-9;
        vertices = [];
        for(k = 0; k < 6; k++) {
            angle = 2*pi*k/6;
            x = radius * cos(angle);
            y = radius * sin(angle);
            vertices = [vertices; [x, y]];
        }
        set("vertices", vertices);
        set("x", i * 600e-9);    // X 方向周期 600nm
        set("y", j * 600e-9);    // Y 方向周期 600nm
        set("z span", 220e-9);   // 厚度 220nm
        set("material", "Si (Silicon) - Palik");
    }
}
```

#### Python API
```python
import numpy as np

fdtd = lumapi.FDTD()

# 创建平面实体阵列（光子晶体平板）
for i in range(5):
    for j in range(5):
        fdtd.addplanarsolid()
        fdtd.set("name", f"pc_slab_{i}_{j}")
        
        # 每个单元为六边形平面实体
        radius = 200e-9
        vertices = []
        for k in range(6):
            angle = 2 * np.pi * k / 6
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            vertices.append([x, y])
        
        fdtd.set("vertices", vertices)
        fdtd.set("x", i * 600e-9)    # X 方向周期 600nm
        fdtd.set("y", j * 600e-9)    # Y 方向周期 600nm
        fdtd.set("z span", 220e-9)   # 厚度 220nm
        fdtd.set("material", "Si (Silicon) - Palik")
```

## 注意事项

### 1. 几何定义
- 平面实体由 `vertices` 定义的多边形横截面沿 `axis` 指定方向拉伸形成
- `vertices` 为 N×2 数组，定义 XY 平面内的多边形顶点（当 `axis` 为 "z" 时）
- 多边形必须为凸多边形或简单多边形，复杂形状可能需要分解为多个平面实体
- 顶点应按顺时针或逆时针顺序排列，形成闭合多边形
- 通过 `axis` 属性可以指定拉伸方向（"x", "y", "z"），默认沿 Z 轴

### 2. 网格考虑
- 复杂多边形可能需要精细的网格离散化，特别是在顶点和边缘处
- 对于薄平面实体（厚度远小于横向尺寸），可能需要沿厚度方向增加网格密度
- 考虑使用 `addmesh` 命令在平面实体区域添加网格覆盖区
- 非凸多边形可能导致网格生成问题，建议使用凸多边形或分解为多个凸多边形

### 3. 旋转与方向
- 默认拉伸方向为 Z 轴，可通过 `axis` 属性更改
- 当 `axis` 设置为 "x" 或 "y" 时，相应的跨度属性变为 `x span` 或 `y span`
- 旋转属性按 `first axis` → `second axis` → `third axis` 顺序应用
- 复杂旋转可能需要按特定顺序应用旋转轴

### 4. 性能优化
- 大量平面实体结构可能显著增加网格生成时间
- 考虑使用对称性减少仿真区域
- 对于周期性阵列，可考虑使用周期性边界条件
- 对于参数扫描，重用网格可以提高效率

### 5. 材料设置
- 平面实体材料可以来自材料数据库或自定义折射率
- 自定义折射率材料需设置 `material` 为 "<Object defined dielectric>" 并指定 `index`
- 对于多层平面结构，可能需要多个平面实体对象叠加

## 错误处理

### 常见错误
1. **顶点无效**: `vertices` 数组格式错误或顶点数 < 3
   - 解决方案：确保 `vertices` 为 N×2 数组且 N ≥ 3

2. **多边形不自闭**: 首尾顶点不重合
   - 解决方案：确保多边形闭合，或提供闭合顶点序列

3. **跨度无效**: `z span` ≤ 0 或 `z min` ≥ `z max`
   - 解决方案：确保 `z span` > 0 且 `z min` < `z max`

4. **拉伸轴无效**: `axis` 不是 "x", "y", "z" 之一
   - 解决方案：检查 `axis` 属性值

5. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

6. **网格生成失败**: 平面实体尺寸过小或形状过于复杂导致网格问题
   - 解决方案：调整平面实体尺寸，确保足够的网格分辨率

### Python 错误处理
```python
import lumapi
import numpy as np

try:
    fdtd = lumapi.FDTD()
    
    # 添加平面实体
    fdtd.addplanarsolid()
    
    # 配置平面实体属性
    fdtd.set("name", "test planar solid")
    
    # 设置三角形横截面
    vertices = [
        [-1e-6, -1e-6],
        [1e-6, -1e-6],
        [0, 1e-6]
    ]
    fdtd.set("vertices", vertices)
    fdtd.set("z span", 500e-9)
    
    # 检查参数有效性
    vertices_array = fdtd.get("vertices")
    if len(vertices_array) < 3:
        raise ValueError("顶点数必须 ≥ 3")
    
    z_span = fdtd.get("z span")
    if z_span <= 0:
        raise ValueError("厚度必须 > 0")
    
    # 设置材料
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    default_vertices = [[-0.5e-6, -0.5e-6], [0.5e-6, -0.5e-6], [0.5e-6, 0.5e-6], [-0.5e-6, 0.5e-6]]
    fdtd.set("vertices", default_vertices)
    fdtd.set("z span", 1e-6)
    
except Exception as e:
    print(f"平面实体创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "vertices" in str(e).lower():
        print("错误: 顶点无效，请检查顶点数组格式")
    elif "span" in str(e).lower():
        print("错误: 厚度无效，请检查跨度值")
    elif "axis" in str(e).lower():
        print("错误: 拉伸轴无效，必须是 'x', 'y', 'z' 之一")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（长方体）
- `addprism`: 添加棱柱
- `addcylinder`: 添加圆柱体
- `addwaveguide`: 添加波导结构
- `addmesh`: 添加网格覆盖区（用于平面实体区域细化）
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions
- **完全支持**: 所有 Lumerical 产品
- **通用命令**: 在所有产品中功能一致

## 应用场景

### 1. 平板波导设计
```python
# 创建硅平板波导
fdtd.addplanarsolid()
fdtd.set("name", "Si slab waveguide")
fdtd.set("vertices", [[-10e-6, -0.5e-6], [10e-6, -0.5e-6], [10e-6, 0.5e-6], [-10e-6, 0.5e-6]])
fdtd.set("z span", 220e-9)      # 厚度 220nm
fdtd.set("material", "Si (Silicon) - Palik")
```

### 2. 光子晶体平板
```python
# 创建六边形晶格光子晶体平板
import numpy as np

rows, cols = 5, 5
for i in range(rows):
    for j in range(cols):
        fdtd.addplanarsolid()
        fdtd.set("name", f"pc_hex_{i}_{j}")
        
        # 六边形横截面
        radius = 200e-9
        vertices = []
        for k in range(6):
            angle = 2 * np.pi * k / 6
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            vertices.append([x, y])
        
        fdtd.set("vertices", vertices)
        fdtd.set("x", (i + 0.5 * (j % 2)) * 500e-9)  # 六边形晶格偏移
        fdtd.set("y", j * 500e-9 * np.sqrt(3)/2)
        fdtd.set("z span", 220e-9)
        fdtd.set("material", "Si (Silicon) - Palik")
```

### 3. 定制化光学元件
```python
# 创建自定义形状光学元件（如微环谐振器耦合区）
fdtd.addplanarsolid()
fdtd.set("name", "custom coupler")

# 定义复杂多边形横截面
vertices = [
    [-2e-6, -0.5e-6],
    [-1e-6, -0.5e-6],
    [-0.5e-6, 0],
    [-1e-6, 0.5e-6],
    [-2e-6, 0.5e-6],
    [-2.5e-6, 0],
    [-2e-6, -0.5e-6]  # 闭合
]
fdtd.set("vertices", vertices)
fdtd.set("z span", 220e-9)
fdtd.set("material", "Si (Silicon) - Palik")
```

### 4. 多层堆叠结构
```python
# 创建多层平面堆叠结构
materials = ["SiO2 (Glass) - Palik", "Si (Silicon) - Palik", "Si3N4 (Silicon Nitride) - Luke"]
thicknesses = [1e-6, 220e-9, 300e-9]

z_pos = 0
for i, (material, thickness) in enumerate(zip(materials, thicknesses)):
    fdtd.addplanarsolid()
    fdtd.set("name", f"layer_{i}")
    fdtd.set("vertices", [[-5e-6, -5e-6], [5e-6, -5e-6], [5e-6, 5e-6], [-5e-6, 5e-6]])
    fdtd.set("z span", thickness)
    fdtd.set("z", z_pos + thickness/2)
    fdtd.set("material", material)
    z_pos += thickness
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `axis` 属性支持 X/Y 轴拉伸 |
| Lumerical 2019a | 改进多边形网格生成算法 |
| Lumerical 2018a | 新增 `vertices` 属性支持自定义多边形 |
| 1.1 | 更新日期，完善文档格式 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 多边形网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*