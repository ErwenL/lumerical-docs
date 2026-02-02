# addring

## 概述

`addring` 命令用于在仿真中添加一个环形结构。环形是光子集成电路中的关键几何形状，常用于创建环形谐振器、环形波导、环形耦合器等光学元件。环形结构由一个圆柱体挖去中心圆柱体形成，具有内外半径参数。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addring;
```

### Python API (Lumapi)
```python
session.addring()
```

## 参数

`addring` 命令没有直接参数，但需要通过后续的 `set` 命令配置环形属性。

## 配置属性

添加环形后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "ring" | 环形名称 |
| `x`, `y`, `z` | float | 0 | 环形中心坐标 (m) |
| `inner radius` | float | 0.5e-6 | 内半径 (m) |
| `outer radius` | float | 1e-6 | 外半径 (m) |
| `z span` | float | 1e-6 | 环形高度 (m) |
| `z` | float | 0 | 环形中心 Z 坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 环形 Z 方向最小/最大坐标 (m) |

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

`addring` 命令没有返回值。成功执行后，会在仿真中添加一个环形对象。

## 示例

### 示例 1: 基本环形谐振器创建

#### LSF 脚本
```lumerical
// 添加环形谐振器
addring;

// 设置几何尺寸
set("name", "Si ring resonator");
set("x", 0);
set("y", 0);
set("z", 0);
set("inner radius", 4.5e-6);   // 内半径 4.5μm
set("outer radius", 5e-6);      // 外半径 5μm，环宽 0.5μm
set("z span", 220e-9);          // 高度 220nm

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

# 添加环形
fdtd.addring()

# 设置几何尺寸
fdtd.set("name", "Si ring resonator")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("inner radius", 4.5e-6)   # 内半径 4.5μm
fdtd.set("outer radius", 5e-6)     # 外半径 5μm，环宽 0.5μm
fdtd.set("z span", 220e-9)         # 高度 220nm

# 设置材料
fdtd.set("material", "Si (Silicon) - Palik")

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 垂直堆叠环形（3D环形谐振器）

#### LSF 脚本
```lumerical
// 底层环形
addring;
set("name", "bottom ring");
set("inner radius", 3e-6);
set("outer radius", 3.5e-6);
set("z span", 200e-9);
set("z", -300e-9);  // 中心在 z = -300nm

// 顶层环形
addring;
set("name", "top ring");
set("inner radius", 3e-6);
set("outer radius", 3.5e-6);
set("z span", 200e-9);
set("z", 300e-9);   // 中心在 z = 300nm
set("material", "Si (Silicon) - Palik");

// 设置颜色区分
set("color", [0.8, 0.2, 0.2, 0.7]);  // 红色半透明
select("bottom ring");
set("color", [0.2, 0.2, 0.8, 0.7]);  // 蓝色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 底层环形
fdtd.addring()
fdtd.set("name", "bottom ring")
fdtd.set("inner radius", 3e-6)
fdtd.set("outer radius", 3.5e-6)
fdtd.set("z span", 200e-9)
fdtd.set("z", -300e-9)  # 中心在 z = -300nm

# 顶层环形
fdtd.addring()
fdtd.set("name", "top ring")
fdtd.set("inner radius", 3e-6)
fdtd.set("outer radius", 3.5e-6)
fdtd.set("z span", 200e-9)
fdtd.set("z", 300e-9)   # 中心在 z = 300nm
fdtd.set("material", "Si (Silicon) - Palik")

# 设置颜色区分
fdtd.set("color", [0.8, 0.2, 0.2, 0.7])  # 红色半透明
fdtd.select("bottom ring")
fdtd.set("color", [0.2, 0.2, 0.8, 0.7])  # 蓝色半透明
```

### 示例 3: 环形波导耦合器

#### LSF 脚本
```lumerical
// 创建环形谐振器
addring;
set("name", "ring resonator");
set("inner radius", 4.8e-6);
set("outer radius", 5.2e-6);  // 环宽 400nm
set("z span", 220e-9);
set("material", "Si (Silicon) - Palik");

// 创建直波导（与环形耦合）
addrect;
set("name", "bus waveguide");
set("x span", 20e-6);     // 长度 20μm
set("y span", 500e-9);    // 宽度 500nm
set("z span", 220e-9);
set("y", 5.5e-6);         // 与环形间距 300nm (5.5μm - 5.2μm)
set("material", "Si (Silicon) - Palik");

// 设置线框渲染以查看耦合区域
setnamed("ring resonator", "render type", "wireframe");
setnamed("bus waveguide", "render type", "wireframe");
setnamed("ring resonator", "alpha", 0.6);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 创建环形谐振器
fdtd.addring()
fdtd.set("name", "ring resonator")
fdtd.set("inner radius", 4.8e-6)
fdtd.set("outer radius", 5.2e-6)  # 环宽 400nm
fdtd.set("z span", 220e-9)
fdtd.set("material", "Si (Silicon) - Palik")

# 创建直波导（与环形耦合）
fdtd.addrect()
fdtd.set("name", "bus waveguide")
fdtd.set("x span", 20e-6)     # 长度 20μm
fdtd.set("y span", 500e-9)    # 宽度 500nm
fdtd.set("z span", 220e-9)
fdtd.set("y", 5.5e-6)         # 与环形间距 300nm (5.5μm - 5.2μm)
fdtd.set("material", "Si (Silicon) - Palik")

# 设置线框渲染以查看耦合区域
fdtd.setnamed("ring resonator", "render type", "wireframe")
fdtd.setnamed("bus waveguide", "render type", "wireframe")
fdtd.setnamed("ring resonator", "alpha", 0.6)
```

### 示例 4: 使用自定义折射率材料

#### LSF 脚本
```lumerical
addring;
set("name", "polymer ring");

// 设置几何尺寸
set("inner radius", 10e-6);   // 内半径 10μm
set("outer radius", 12e-6);   // 外半径 12μm，环宽 2μm
set("z span", 1e-6);          // 高度 1μm

// 使用自定义聚合物材料
set("material", "<Object defined dielectric>");
set("index", 1.45);           // 聚合物折射率
set("index units", "microns");

// 设置颜色为绿色半透明
set("color", [0.2, 0.8, 0.2, 0.5]);
set("alpha", 0.5);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addring()
fdtd.set("name", "polymer ring")

# 设置几何尺寸
fdtd.set("inner radius", 10e-6)   # 内半径 10μm
fdtd.set("outer radius", 12e-6)   # 外半径 12μm，环宽 2μm
fdtd.set("z span", 1e-6)          # 高度 1μm

# 使用自定义聚合物材料
fdtd.set("material", "<Object defined dielectric>")
fdtd.set("index", 1.45)           # 聚合物折射率
fdtd.set("index units", "microns")

# 设置颜色为绿色半透明
fdtd.set("color", [0.2, 0.8, 0.2, 0.5])
fdtd.set("alpha", 0.5)
```

### 示例 5: 旋转环形（倾斜环形谐振器）

#### LSF 脚本
```lumerical
addring;
set("name", "tilted ring resonator");
set("inner radius", 5e-6);
set("outer radius", 5.5e-6);
set("z span", 300e-9);

// 设置材料
set("material", "SiO2 (Glass) - Palik");

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
fdtd.addring()
fdtd.set("name", "tilted ring resonator")
fdtd.set("inner radius", 5e-6)
fdtd.set("outer radius", 5.5e-6)
fdtd.set("z span", 300e-9)

# 设置材料
fdtd.set("material", "SiO2 (Glass) - Palik")

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
- 环形由 `inner radius` 和 `outer radius` 定义，必须满足 `inner radius` < `outer radius`
- 环形高度由 `z span` 定义，或者使用 `z min` 和 `z max`
- 中心位置由 `(x, y, z)` 坐标定义

### 2. 环形谐振器设计
- 环形谐振器的自由光谱范围 (FSR) 与环形周长成反比
- 耦合效率取决于环形与波导之间的间距
- 环形宽度影响模式限制和损耗

### 3. 网格考虑
- 环形曲面需要精细的网格离散化，特别是在内外边界处
- 对于 thin-ring 结构（环宽远小于半径），可能需要局部网格细化
- 考虑使用 `addmesh` 命令在环形区域添加网格覆盖区

### 4. 旋转应用
- 环形旋转主要用于创建倾斜环形谐振器或3D环形结构
- 旋转按 `first axis` → `second axis` → `third axis` 顺序应用
- 复杂的旋转可能需要按特定顺序应用

### 5. 性能优化
- 大量环形结构可能增加网格生成时间
- 考虑使用对称性减少仿真区域
- 对于参数扫描，重用网格可以提高效率

## 错误处理

### 常见错误
1. **半径无效**: `inner radius` ≥ `outer radius`
   - 解决方案：确保 `inner radius` < `outer radius`

2. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

3. **网格生成失败**: 环形尺寸过小或环宽过窄导致网格问题
   - 解决方案：调整环形尺寸，确保足够的网格分辨率

4. **Z坐标冲突**: `z min` ≥ `z max`
   - 解决方案：确保 `z min` < `z max`

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加环形
    fdtd.addring()
    
    # 配置环形属性
    fdtd.set("name", "test ring")
    fdtd.set("inner radius", 1e-6)
    fdtd.set("outer radius", 2e-6)
    
    # 检查半径有效性
    inner_radius = fdtd.get("inner radius")
    outer_radius = fdtd.get("outer radius")
    
    if inner_radius >= outer_radius:
        raise ValueError("内半径必须小于外半径")
    
    # 设置材料
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认半径
    fdtd.set("inner radius", 0.5e-6)
    fdtd.set("outer radius", 1e-6)
    
except Exception as e:
    print(f"环形创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查内外半径值")
    elif "coordinate" in str(e).lower():
        print("错误: 坐标无效，请检查最小/最大坐标")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（用于创建耦合波导）
- `addsphere`: 添加球体
- `addcylinder`: 添加圆柱体
- `addwaveguide`: 添加波导结构
- `addmesh`: 添加网格覆盖区（用于环形区域细化）
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: FDTD Solutions, MODE Solutions
- **完全支持**: 所有 Lumerical 产品
- **通用命令**: 在所有产品中功能一致

## 应用场景

### 1. 环形谐振器滤波
```python
# 创建硅基环形谐振器滤波器
fdtd.addring()
fdtd.set("name", "filter ring")
fdtd.set("inner radius", 4.5e-6)   # 内半径
fdtd.set("outer radius", 5e-6)     # 外半径，环宽 500nm
fdtd.set("z span", 220e-9)         # 硅层厚度
fdtd.set("material", "Si (Silicon) - Palik")
```

### 2. 垂直耦合环形
```python
# 创建垂直耦合双环形结构
for i, z_pos in enumerate([-200e-9, 200e-9]):
    fdtd.addring()
    fdtd.set("name", f"ring_{i+1}")
    fdtd.set("inner radius", 3e-6)
    fdtd.set("outer radius", 3.5e-6)
    fdtd.set("z span", 150e-9)
    fdtd.set("z", z_pos)
    fdtd.set("material", "Si (Silicon) - Palik")
```

### 3. 环形激光器
```python
# 创建增益材料环形激光器
fdtd.addring()
fdtd.set("name", "laser ring")
fdtd.set("inner radius", 10e-6)    # 较大半径用于低阈值
fdtd.set("outer radius", 10.5e-6)  # 窄环宽
fdtd.set("z span", 200e-9)
fdtd.set("material", "InGaAsP (Gain)")
```

### 4. 环形传感器
```python
# 创建环形生物传感器
fdtd.addring()
fdtd.set("name", "biosensor ring")
fdtd.set("inner radius", 15e-6)    # 大半径提高灵敏度
fdtd.set("outer radius", 15.2e-6)  # 薄环增强表面灵敏度
fdtd.set("z span", 100e-9)         # 薄层
fdtd.set("material", "Si3N4 (Silicon Nitride) - Luke")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `color` 属性直接设置 |
| Lumerical 2019a | 改进环形网格生成算法 |
| Lumerical 2018a | 新增 `inner radius` 和 `outer radius` 独立控制 |
| 1.1 | 更新日期，完善文档格式 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 环形谐振器应用笔记
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*