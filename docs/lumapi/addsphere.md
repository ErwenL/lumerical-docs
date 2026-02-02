# addsphere

## 概述

`addsphere` 命令用于在仿真中添加一个球体结构。球体是 Lumerical 中的基本几何形状之一，常用于创建纳米颗粒、微球透镜、散射体等光学元件。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addsphere;
```

### Python API (Lumapi)
```python
session.addsphere()
```

## 参数

`addsphere` 命令没有直接参数，但需要通过后续的 `set` 命令配置球体属性。

## 配置属性

添加球体后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "sphere" | 球体名称 |
| `x`, `y`, `z` | float | 0 | 球体中心坐标 (m) |
| `radius` | float | 0.5e-6 | 球体半径 (m) |
| `inner radius` | float | 0 | 内半径 (m)，用于创建空心球体 |

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

`addsphere` 命令没有返回值。成功执行后，会在仿真中添加一个球体对象。

## 示例

### 示例 1: 基本球体创建

#### LSF 脚本
```lumerical
// 添加球体
addsphere;

// 设置几何尺寸
set("name", "SiO2 microsphere");
set("x", 0);
set("y", 0);
set("z", 0);
set("radius", 2.5e-6);    // 半径 2.5μm

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

# 添加球体
fdtd.addsphere()

# 设置几何尺寸
fdtd.set("name", "SiO2 microsphere")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("radius", 2.5e-6)    # 半径 2.5μm

# 设置材料
fdtd.set("material", "SiO2 (Glass) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 空心球体（核壳结构）

#### LSF 脚本
```lumerical
addsphere;
set("name", "core-shell nanoparticle");

// 设置外半径和内半径创建空心球体
set("radius", 100e-9);        // 外半径 100nm
set("inner radius", 70e-9);   // 内半径 70nm，壳层厚度 30nm

// 设置材料为金
set("material", "Au (Gold) - Johnson and Christy");

// 设置颜色为金色
set("color", [1, 0.84, 0, 1]);
set("alpha", 0.8);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addsphere()
fdtd.set("name", "core-shell nanoparticle")

# 设置外半径和内半径创建空心球体
fdtd.set("radius", 100e-9)        # 外半径 100nm
fdtd.set("inner radius", 70e-9)   # 内半径 70nm，壳层厚度 30nm

# 设置材料为金
fdtd.set("material", "Au (Gold) - Johnson and Christy")

# 设置颜色为金色
fdtd.set("color", [1, 0.84, 0, 1])
fdtd.set("alpha", 0.8)
```

### 示例 3: 使用自定义折射率

#### LSF 脚本
```lumerical
addsphere;
set("name", "dielectric sphere");

// 设置几何尺寸
set("radius", 1.5e-6);

// 使用自定义折射率而不是材料数据库
set("material", "<Object defined dielectric>");
set("index", 2.0);          // 折射率 2.0
set("index units", "microns");

// 设置渲染为线框模式
set("render type", "wireframe");
set("alpha", 0.6);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addsphere()
fdtd.set("name", "dielectric sphere")

# 设置几何尺寸
fdtd.set("radius", 1.5e-6)

# 使用自定义折射率而不是材料数据库
fdtd.set("material", "<Object defined dielectric>")
fdtd.set("index", 2.0)          # 折射率 2.0
fdtd.set("index units", "microns")

# 设置渲染为线框模式
fdtd.set("render type", "wireframe")
fdtd.set("alpha", 0.6)
```

### 示例 4: 球体阵列

#### LSF 脚本
```lumerical
// 创建 3x3 球体阵列
for(i = -1; i <= 1; i = i + 1) {
    for(j = -1; j <= 1; j = j + 1) {
        addsphere;
        set("name", "sphere_" + num2str(i+2) + "_" + num2str(j+2));
        set("x", i * 3e-6);      // X 方向间距 3μm
        set("y", j * 3e-6);      // Y 方向间距 3μm
        set("z", 0);
        set("radius", 1e-6);     // 半径 1μm
        
        // 交替材料
        if((i+j) % 2 == 0) {
            set("material", "Si (Silicon) - Palik");
            set("color", [0.8, 0.2, 0.2, 1]);  // 红色
        } else {
            set("material", "SiO2 (Glass) - Palik");
            set("color", [0.2, 0.2, 0.8, 1]);  // 蓝色
        }
    }
}
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 创建 3x3 球体阵列
for i in range(-1, 2):
    for j in range(-1, 2):
        fdtd.addsphere()
        fdtd.set("name", f"sphere_{i+2}_{j+2}")
        fdtd.set("x", i * 3e-6)      # X 方向间距 3μm
        fdtd.set("y", j * 3e-6)      # Y 方向间距 3μm
        fdtd.set("z", 0)
        fdtd.set("radius", 1e-6)     # 半径 1μm
        
        # 交替材料
        if (i + j) % 2 == 0:
            fdtd.set("material", "Si (Silicon) - Palik")
            fdtd.set("color", [0.8, 0.2, 0.2, 1])  # 红色
        else:
            fdtd.set("material", "SiO2 (Glass) - Palik")
            fdtd.set("color", [0.2, 0.2, 0.8, 1])  # 蓝色
```

### 示例 5: 旋转球体（用于非球对称材料）

#### LSF 脚本
```lumerical
addsphere;
set("name", "anisotropic sphere");
set("radius", 2e-6);

// 设置各向异性材料（需要自定义材料属性）
set("material", "<Object defined dielectric>");
set("index", 2.5);

// 旋转球体以对齐材料主轴
set("first axis", "x");
set("rotation 1", 45);   // 绕 X 轴旋转 45 度

set("second axis", "y");
set("rotation 2", 30);   // 绕 Y 轴旋转 30 度

// 设置半透明显示
set("alpha", 0.7);
set("color", [0.5, 0.8, 0.3, 0.7]);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addsphere()
fdtd.set("name", "anisotropic sphere")
fdtd.set("radius", 2e-6)

# 设置各向异性材料（需要自定义材料属性）
fdtd.set("material", "<Object defined dielectric>")
fdtd.set("index", 2.5)

# 旋转球体以对齐材料主轴
fdtd.set("first axis", "x")
fdtd.set("rotation 1", 45)   # 绕 X 轴旋转 45 度

fdtd.set("second axis", "y")
fdtd.set("rotation 2", 30)   # 绕 Y 轴旋转 30 度

# 设置半透明显示
fdtd.set("alpha", 0.7)
fdtd.set("color", [0.5, 0.8, 0.3, 0.7])
```

## 注意事项

### 1. 坐标系统
- Lumerical 使用右手笛卡尔坐标系
- 默认单位是米 (m)，但通常使用微米 (μm) 或纳米 (nm) 更方便
- 球体位置由中心坐标 `(x, y, z)` 和半径 `radius` 定义

### 2. 空心球体
- 设置 `inner radius` 大于 0 可创建空心球体（核壳结构）
- `inner radius` 必须小于 `radius`
- 空心球体可用于模拟涂层、多层纳米颗粒等

### 3. 材料选择
- 可以从材料数据库选择预定义材料
- 使用 `<Object defined dielectric>` 并设置 `index` 属性创建自定义材料
- 材料名称区分大小写

### 4. 网格顺序
- 网格顺序决定不同材料交界处的网格优先级
- 较高网格顺序的材料优先
- 默认从材料数据库获取，但可以覆盖
- 对于球体，网格会自适应曲面形状

### 5. 旋转应用
- 球体本身是球对称的，旋转不影响几何形状
- 旋转主要用于对齐各向异性材料的主轴
- 旋转按 `first axis` → `second axis` → `third axis` 顺序应用

### 6. 性能考虑
- 球体曲面需要更精细的网格离散化
- 大量球体结构可能显著增加网格生成时间
- 考虑使用近似模型（如多面体）代替高精度球体以提高性能

## 错误处理

### 常见错误
1. **半径无效**: `radius` 小于等于 0 或 `inner radius` 大于等于 `radius`
   - 解决方案：确保 `radius` > 0 且 `inner radius` < `radius`

2. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

3. **网格生成失败**: 球体尺寸过小或与其他几何体重叠导致网格问题
   - 解决方案：调整球体尺寸或网格设置，确保足够的网格分辨率

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加球体
    fdtd.addsphere()
    
    # 配置球体属性
    fdtd.set("name", "test sphere")
    fdtd.set("radius", 1e-6)
    
    # 检查半径有效性
    if fdtd.get("radius") <= 0:
        raise ValueError("球体半径必须大于0")
    
    # 设置材料
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认半径
    fdtd.set("radius", 0.5e-6)
    
except Exception as e:
    print(f"球体创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查半径值")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形
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

### 1. 纳米颗粒散射
```python
# 创建金纳米颗粒用于散射分析
fdtd.addsphere()
fdtd.set("name", "Au nanoparticle")
fdtd.set("radius", 50e-9)  # 50nm 半径
fdtd.set("material", "Au (Gold) - Johnson and Christy")
```

### 2. 微球透镜
```python
# 创建二氧化硅微球透镜
fdtd.addsphere()
fdtd.set("name", "SiO2 microsphere lens")
fdtd.set("radius", 5e-6)   # 5μm 半径
fdtd.set("material", "SiO2 (Glass) - Palik")
fdtd.set("z", 10e-6)       # 提升到衬底上方
```

### 3. 核壳纳米颗粒
```python
# 创建核壳结构纳米颗粒
fdtd.addsphere()
fdtd.set("name", "Au@SiO2 core-shell")
fdtd.set("radius", 80e-9)       # 总半径 80nm
fdtd.set("inner radius", 50e-9) # 核半径 50nm，壳层厚度 30nm
fdtd.set("material", "SiO2 (Glass) - Palik")
```

### 4. 光子晶体球阵列
```python
# 创建二维光子晶体球阵列
import numpy as np

pitch = 3e-6  # 阵列间距
radius = 1e-6 # 球体半径

for i in range(5):
    for j in range(5):
        fdtd.addsphere()
        fdtd.set("name", f"sphere_{i}_{j}")
        fdtd.set("x", i * pitch)
        fdtd.set("y", j * pitch)
        fdtd.set("radius", radius)
        fdtd.set("material", "Si (Silicon) - Palik")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `inner radius` 属性支持空心球体 |
| Lumerical 2019a | 改进球体网格生成算法 |
| Lumerical 2018a | 新增 `color` 属性直接设置 |
| 1.1 | 更新日期，完善文档格式 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 材料数据库文档
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*