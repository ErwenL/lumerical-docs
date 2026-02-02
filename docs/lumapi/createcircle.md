# `createcircle` - 创建圆形

## 概述

`createcircle` 命令用于在仿真中创建圆形几何结构。圆形是光学和光子学仿真中常用的基本形状，常用于创建波导弯曲、环形谐振器、透镜、光圈等元件。该命令允许用户指定圆形的位置、半径、方向、材料等属性，并可以进一步通过 `set` 命令修改其他属性。

在 Lumerical 中，圆形通常用于 2D 仿真或作为 3D 结构的基础形状，可以通过拉伸（extrude）操作转换为圆柱体。

## 语法

### LSF 语法
```lumerical
createcircle(name);                    # 创建圆形，使用默认设置
createcircle(name, property, value, ...);  # 创建圆形并设置属性
```

### Python API
```python
session.createcircle(name)                     # 创建圆形，使用默认设置
session.createcircle(name, property1=value1, property2=value2, ...)  # 创建圆形并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 圆形的名称。 | 是 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 圆形中心的 x 坐标（μm）。 |
| `y` | number | 0 | 圆形中心的 y 坐标（μm）。 |
| `z` | number | 0 | 圆形中心的 z 坐标（μm）。 |
| `radius` | number | 0.5 | 圆形的半径（μm）。 |
| `x span` | number | 1 | 圆形的 x 方向跨度（直径，μm）。 |
| `y span` | number | 1 | 圆形的 y 方向跨度（直径，μm）。 |
| `z span` | number | 0 | 圆形的 z 方向跨度（厚度，μm）。 |
| `first axis` | string | "x" | 圆形的第一个轴方向（"x" 或 "y"）。 |
| `second axis` | string | "y" | 圆形的第二个轴方向（"x" 或 "y"）。 |
| `material` | string | "" | 圆形材料的名称。如果为空，则使用全局材料。 |
| `index` | number | 1.0 | 圆形的折射率（如果未指定材料）。 |
| `color` | string | "custom" | 显示颜色（RGB 值或颜色名称）。 |
| `alpha` | number | 1.0 | 透明度（0-1，1 为不透明）。 |
| `visible` | bool | true | 是否可见。 |
| `mesh order` | number | 2 | 网格划分顺序。 |
| `override global mesh settings` | bool | false | 是否覆盖全局网格设置。 |
| `dx`, `dy`, `dz` | number | 0.02 | 各方向的网格步长（μm）。 |
| `grid mesh cells per wavelength` | number | 20 | 每波长网格单元数。 |
 | `use relative coordinates` | bool | false | 是否使用相对坐标。 |

## 返回值

`createcircle` 命令没有返回值。成功执行后，会在仿真中创建一个圆形对象。

## 示例

### 示例 1：创建基本圆形
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建圆形，使用默认设置
fdtd.createcircle("circle1")

print("创建的圆形属性:")
circle_props = fdtd.get("circle1")
print(f"  位置: ({circle_props.get('x', '未知')}, {circle_props.get('y', '未知')}, {circle_props.get('z', '未知')}) μm")
print(f"  半径: {circle_props.get('radius', '未知')} μm")
print(f"  材料: {circle_props.get('material', '未知')}")

# 创建圆形并指定属性
fdtd.createcircle("circle2", 
                  x=2, y=1, z=0,        # 位置
                  radius=0.8,            # 半径 0.8 μm
                  material="Si")         # 硅材料

print("\n自定义圆形属性:")
circle2_props = fdtd.get("circle2")
print(f"  位置: ({circle2_props.get('x', '未知')}, {circle2_props.get('y', '未知')}, {circle2_props.get('z', '未知')}) μm")
print(f"  半径: {circle2_props.get('radius', '未知')} μm")
print(f"  材料: {circle2_props.get('material', '未知')}")
```

### 示例 2：创建环形谐振器
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_ring_resonator(name, center_x=0, center_y=0, radius=5, waveguide_width=0.5):
    """创建环形谐振器结构"""
    
    # 创建环形波导（大圆形）
    fdtd.createcircle(f"{name}_ring",
                      x=center_x, y=center_y, z=0,
                      radius=radius,
                      material="Si",
                      z_span=0.22)  # 波导厚度
    
    # 创建输入波导（直线波导，这里用矩形近似）
    fdtd.addrect(f"{name}_input_wg",
                 x=center_x - radius - waveguide_width/2, 
                 y=center_y,
                 z=0,
                 x_span=waveguide_width,
                 y_span=radius*2,  # 足够长
                 z_span=0.22,
                 material="Si")
    
    # 创建输出波导
    fdtd.addrect(f"{name}_output_wg",
                 x=center_x + radius + waveguide_width/2,
                 y=center_y,
                 z=0,
                 x_span=waveguide_width,
                 y_span=radius*2,
                 z_span=0.22,
                 material="Si")
    
    # 设置间隙（环形波导与直波导之间的距离）
    gap = 0.2  # 200 nm 间隙
    
    # 调整直波导位置，形成间隙
    fdtd.set(f"{name}_input_wg", "y span", radius*2 - gap)
    fdtd.set(f"{name}_output_wg", "y span", radius*2 - gap)
    
    return [f"{name}_ring", f"{name}_input_wg", f"{name}_output_wg"]

print("创建环形谐振器...")
ring_parts = create_ring_resonator("ring1", radius=5, waveguide_width=0.5)

print(f"创建的部件: {ring_parts}")

# 计算环形谐振器周长
ring_radius = fdtd.get("ring1_ring").get("radius", 0)
circumference = 2 * np.pi * ring_radius
print(f"\n环形谐振器参数:")
print(f"  半径: {ring_radius} μm")
print(f"  周长: {circumference:.4f} μm")
print(f"  波导宽度: 0.5 μm")
print(f"  间隙: 0.2 μm")

# 验证结构
print("\n所有圆形对象:")
fdtd.eval("?circle;")

print("\n所有矩形对象:")
fdtd.eval("?rect;")
```

### 示例 3：创建透镜阵列
```python
import lumapi

fdtd = lumapi.FDTD()

def create_lens_array(name, rows=3, cols=3, spacing=3, radius=1.0):
    """创建透镜阵列"""
    
    lenses = []
    
    for i in range(rows):
        for j in range(cols):
            # 计算透镜位置
            x_pos = (j - (cols-1)/2) * spacing
            y_pos = (i - (rows-1)/2) * spacing
            
            # 创建透镜（圆形）
            lens_name = f"{name}_lens_{i}_{j}"
            fdtd.createcircle(lens_name,
                              x=x_pos, y=y_pos, z=0,
                              radius=radius,
                              material="SiO2",  # 二氧化硅透镜
                              z_span=0.5)       # 透镜厚度
            
            lenses.append(lens_name)
    
    return lenses

print("创建 3x3 透镜阵列...")
lenses = create_lens_array("microlens_array", rows=3, cols=3, spacing=3, radius=1.0)

print(f"创建的透镜数量: {len(lenses)}")

# 计算阵列参数
total_width = 2 * 3  # 3个透镜，间距3μm
total_height = 2 * 3
print(f"阵列尺寸: {total_width} μm × {total_height} μm")
print(f"填充因子: {len(lenses) * np.pi * 1.0**2 / (total_width * total_height):.2%}")

# 为不同透镜设置不同属性（示例）
print("\n设置透镜属性变化...")
for i, lens in enumerate(lenses):
    # 根据位置设置不同的折射率（渐变折射率透镜）
    props = fdtd.get(lens)
    x_pos = props.get("x", 0)
    
    # 计算渐变折射率：中心高，边缘低
    distance_from_center = np.sqrt(x_pos**2 + props.get("y", 0)**2)
    max_distance = np.sqrt(3**2 + 3**2)  # 阵列角到中心的距离
    
    # 折射率从 1.5 到 1.45 渐变
    n = 1.5 - 0.05 * (distance_from_center / max_distance)
    
    fdtd.set(lens, "index", n)
    
    # 设置颜色渐变（可视化）
    red = 0.5 + 0.5 * (distance_from_center / max_distance)
    blue = 0.5 - 0.5 * (distance_from_center / max_distance)
    fdtd.set(lens, "color", (red, 0.5, blue))
    
    if i < 3:  # 只显示前3个透镜的信息
        print(f"  {lens}: 位置({x_pos:.1f}, {props.get('y', 0):.1f}), 折射率={n:.3f}")
```

### 示例 4：创建光子晶体孔阵列
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_photonic_crystal_holes(name, rows=10, cols=10, pitch=0.5, hole_radius=0.1):
    """创建光子晶体孔阵列（在背景材料中打孔）"""
    
    # 首先创建背景材料（平板）
    fdtd.addrect(f"{name}_background",
                 x=0, y=0, z=0,
                 x_span=cols * pitch,
                 y_span=rows * pitch,
                 z_span=0.22,
                 material="Si")
    
    holes = []
    
    # 创建孔阵列（圆形孔）
    for i in range(rows):
        for j in range(cols):
            # 计算孔位置
            x_pos = (j - (cols-1)/2) * pitch
            y_pos = (i - (rows-1)/2) * pitch
            
            # 创建孔（材料为空气）
            hole_name = f"{name}_hole_{i}_{j}"
            fdtd.createcircle(hole_name,
                              x=x_pos, y=y_pos, z=0,
                              radius=hole_radius,
                              material="Air",  # 空气孔
                              z_span=0.22)     # 与背景相同厚度
            
            holes.append(hole_name)
    
    return f"{name}_background", holes

print("创建光子晶体孔阵列...")
background, holes = create_photonic_crystal_holes("photonic_crystal", 
                                                  rows=5, cols=5, 
                                                  pitch=0.5, hole_radius=0.15)

print(f"背景平板: {background}")
print(f"孔数量: {len(holes)}")

# 计算光子晶体参数
pitch = 0.5
radius = 0.15
fill_factor = (np.pi * radius**2) / (pitch**2)

print(f"\n光子晶体参数:")
print(f"  晶格常数: {pitch} μm")
print(f"  孔半径: {radius} μm")
print(f"  填充因子: {fill_factor:.2%}")
print(f"  带隙中心波长估计: {2 * pitch / 1.5:.3f} μm (假设有效折射率 1.5)")

# 验证结构
print(f"\n背景材料体积:")
bg_props = fdtd.get(background)
bg_volume = bg_props.get("x span", 0) * bg_props.get("y span", 0) * bg_props.get("z span", 0)
print(f"  {bg_volume:.4f} μm³")

print(f"孔总体积:")
total_hole_volume = 0
for hole in holes[:3]:  # 只检查前3个孔
    hole_props = fdtd.get(hole)
    hole_volume = np.pi * hole_props.get("radius", 0)**2 * hole_props.get("z span", 0)
    total_hole_volume += hole_volume
total_hole_volume *= len(holes) / 3  # 估算总孔体积

print(f"  ~{total_hole_volume:.4f} μm³")
print(f"  有效材料体积: {bg_volume - total_hole_volume:.4f} μm³")
```

### 示例 5：高级圆形创建工具
```python
import lumapi
import numpy as np

class CircleDesigner:
    """高级圆形设计工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_concentric_circles(self, base_name, center, radii, materials=None):
        """创建同心圆"""
        
        circles = []
        
        for i, radius in enumerate(radii):
            circle_name = f"{base_name}_ring_{i}"
            
            # 创建圆形
            self.session.createcircle(circle_name,
                                      x=center[0], y=center[1], z=center[2],
                                      radius=radius)
            
            # 设置材料（如果提供）
            if materials and i < len(materials):
                self.session.set(circle_name, "material", materials[i])
            
            circles.append(circle_name)
        
        return circles
    
    def create_annulus(self, name, center, inner_radius, outer_radius, material="Si"):
        """创建圆环（环形区域）"""
        
        # 创建外圆
        self.session.createcircle(f"{name}_outer",
                                  x=center[0], y=center[1], z=center[2],
                                  radius=outer_radius,
                                  material=material)
        
        # 创建内圆（孔）
        self.session.createcircle(f"{name}_inner",
                                  x=center[0], y=center[1], z=center[2],
                                  radius=inner_radius,
                                  material="Air")  # 空气材料形成孔
        
        return f"{name}_outer", f"{name}_inner"
    
    def create_gradient_circle(self, name, center, radius, 
                              gradient_type="radial", param_name="index", 
                              start_value=1.0, end_value=2.0):
        """创建渐变圆形"""
        
        # 首先创建基本圆形
        self.session.createcircle(name,
                                  x=center[0], y=center[1], z=center[2],
                                  radius=radius)
        
        if gradient_type == "radial":
            # 径向渐变：创建多个同心圆环来近似
            num_segments = 20
            segment_width = radius / num_segments
            
            for i in range(num_segments):
                inner_r = i * segment_width
                outer_r = (i + 1) * segment_width
                
                # 计算该环的参数值
                t = i / (num_segments - 1) if num_segments > 1 else 0
                param_value = start_value + (end_value - start_value) * t
                
                # 创建环
                ring_name = f"{name}_segment_{i}"
                inner, outer = self.create_annulus(ring_name, center, inner_r, outer_r)
                
                # 设置参数
                self.session.set(outer, param_name, param_value)
                
                # 设置颜色渐变（可视化）
                color_value = 0.5 + 0.5 * t
                self.session.set(outer, "color", (color_value, 0.5, 1-color_value))
        
        return name
    
    def analyze_circle_properties(self, circle_name):
        """分析圆形属性"""
        
        props = self.session.get(circle_name)
        
        radius = props.get("radius", 0)
        area = np.pi * radius**2
        
        # 如果定义了材料，获取材料属性
        material = props.get("material", "")
        index = props.get("index", 1.0)
        
        return {
            'name': circle_name,
            'radius': radius,
            'diameter': 2 * radius,
            'area': area,
            'circumference': 2 * np.pi * radius,
            'material': material,
            'index': index,
            'position': (props.get('x', 0), props.get('y', 0), props.get('z', 0))
        }

# 使用示例
fdtd = lumapi.FDTD()
designer = CircleDesigner(fdtd)

print("示例1: 创建同心圆")
concentric = designer.create_concentric_circles("target", 
                                                center=(0, 0, 0), 
                                                radii=[0.5, 1.0, 1.5, 2.0],
                                                materials=["Au", "Ag", "Al", "Si"])
print(f"创建的同心圆: {concentric}")

print("\n示例2: 创建圆环（环形谐振器基础）")
annulus_outer, annulus_inner = designer.create_annulus("ring_waveguide", 
                                                       center=(5, 0, 0), 
                                                       inner_radius=4.5, 
                                                       outer_radius=5.0,
                                                       material="Si")
print(f"圆环: 外圆={annulus_outer}, 内圆={annulus_inner}")

print("\n示例3: 创建渐变折射率透镜")
gradient_lens = designer.create_gradient_circle("grad_lens",
                                                center=(-5, 0, 0),
                                                radius=2.0,
                                                gradient_type="radial",
                                                param_name="index",
                                                start_value=1.45,
                                                end_value=1.55)
print(f"渐变透镜: {gradient_lens}")

print("\n圆形属性分析:")
for circle in concentric:
    analysis = designer.analyze_circle_properties(circle)
    print(f"\n{analysis['name']}:")
    print(f"  半径: {analysis['radius']} μm")
    print(f"  面积: {analysis['area']:.4f} μm²")
    print(f"  材料: {analysis['material']}")
    print(f"  折射率: {analysis['index']}")
```

## 注意事项

1. **2D 与 3D**：默认情况下，圆形是 2D 结构（`z span=0`）。要创建圆柱体，需要设置 `z span` 属性或使用 `addcylinder` 命令。

2. **坐标方向**：圆形在 xy 平面内创建。可以通过设置 `first axis` 和 `second axis` 属性改变圆形平面。

3. **网格划分**：圆形边界可能需要在网格划分时特殊处理。Lumerical 会自动处理圆形边界的网格适配。

4. **材料定义**：如果未指定材料，圆形将使用全局默认材料或通过 `index` 属性指定折射率。

5. **性能考虑**：大量小圆形可能会增加网格复杂度和仿真时间。考虑使用等效模型或简化结构。

6. **布尔运算**：圆形可以与其他几何结构进行布尔运算（并集、交集、差集），用于创建复杂形状。

7. **与 `addcircle` 的区别**：`createcircle` 和 `addcircle` 功能相似，但可能有细微的语法或默认值差异。在 Lumerical 脚本中，两者通常可以互换使用。

 8. **可视化**：圆形在可视化器中显示为圆盘。可以通过 `color` 和 `alpha` 属性调整外观。

## 错误处理

### 常见错误
1. **半径无效**: `radius` ≤ 0
   - 解决方案：确保 `radius` > 0

2. **坐标轴无效**: `first axis` 或 `second axis` 不是 "x" 或 "y"
   - 解决方案：检查 `first axis` 和 `second axis` 属性值，必须是 "x" 或 "y"

3. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率通过 `index` 属性指定

4. **网格生成失败**: 圆形尺寸过小或与其他结构重叠导致网格问题
   - 解决方案：调整圆形尺寸，确保足够的网格分辨率

5. **名称冲突**: 圆形名称与现有对象重复
   - 解决方案：使用唯一的名称，或先删除同名对象

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 创建圆形
    fdtd.createcircle("test_circle", radius=0.5, material="Si")
    
    # 检查参数有效性
    radius = fdtd.get("test_circle").get("radius", 0)
    if radius <= 0:
        raise ValueError("半径必须 > 0")
    
    # 验证坐标轴设置
    first_axis = fdtd.get("test_circle").get("first axis", "x")
    second_axis = fdtd.get("test_circle").get("second axis", "y")
    if first_axis not in ["x", "y"] or second_axis not in ["x", "y"]:
        raise ValueError("坐标轴必须是 'x' 或 'y'")
    
    # 验证材料
    material = fdtd.get("test_circle").get("material", "")
    if material and material not in fdtd.getmaterialnames():
        print(f"警告: 材料 '{material}' 不在数据库中，使用自定义折射率")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    fdtd.set("test_circle", "radius", 0.5)
    
except Exception as e:
    print(f"圆形创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查半径值")
    elif "axis" in str(e).lower():
        print("错误: 坐标轴无效，必须是 'x' 或 'y'")
    elif "name" in str(e).lower():
        print("错误: 名称冲突，请使用不同的名称")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addcircle` - 添加圆形（功能相似）
- `addcylinder` - 添加圆柱体（3D 圆形）
- `adddisk` - 添加圆盘
- `addrect` - 添加矩形（用于对比）
- `addpoly` - 添加多边形
- `set` - 设置圆形属性
- `get` - 获取圆形属性
- `copy` - 复制圆形

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于创建圆形光学元件 |
| MODE Solutions | ✅ 完全支持 | 用于创建圆形波导和耦合器 |
| DEVICE | ✅ 完全支持 | 用于创建圆形电极和接触 |
 | INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用不同的几何系统 |

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `first axis` 和 `second axis` 属性支持不同平面 |
| Lumerical 2019a | 改进圆形网格生成算法 |
| Lumerical 2018a | 新增 `createcircle` 命令，替代部分 `addcircle` 功能 |
| 1.1 | 更新日期，完善文档格式，添加错误处理和版本历史 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 圆形网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*