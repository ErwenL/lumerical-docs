# `createpoly` - 创建多边形

## 概述

`createpoly` 命令用于在仿真中创建多边形几何结构。多边形是由多个直线段组成的闭合二维形状，是光学和光子学仿真中常用的基本形状，用于创建复杂的光学元件、波导、光子晶体、微结构等。与简单几何形状（矩形、圆形）相比，多边形提供了更大的设计灵活性，可以创建任意复杂形状。

该命令允许用户指定多边形的顶点坐标、材料、厚度等属性，是创建自定义光学结构的重要工具。

## 语法

### LSF 语法
```lumerical
createpoly(name);                    # 创建多边形，使用默认设置
createpoly(name, x1, y1, z1, x2, y2, z2, ...);  # 创建多边形并指定顶点
createpoly(name, property, value, ...);  # 创建多边形并设置属性
```

### Python API
```python
session.createpoly(name)                     # 创建多边形，使用默认设置
session.createpoly(name, x1, y1, z1, x2, y2, z2, ...)  # 创建多边形并指定顶点
session.createpoly(name, property1=value1, property2=value2, ...)  # 创建多边形并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 多边形的名称。 | 是 |
| `x, y, z` | number | 多边形顶点的坐标（μm）。至少需要三个顶点来定义多边形。 | 可选 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `points` | array | [[0,0,0], [1,0,0], [0,1,0]] | 多边形的顶点坐标数组。 |
| `x`, `y`, `z` | number | 0 | 多边形参考点位置（μm）。 |
| `height` | number | 0.1 | 多边形的高度（厚度，μm）。 |
| `material` | string | "" | 多边形材料的名称。如果为空，则使用全局材料。 |
| `index` | number | 1.0 | 多边形的折射率（如果未指定材料）。 |
| `color` | string | "custom" | 显示颜色（RGB 值或颜色名称）。 |
| `alpha` | number | 1.0 | 透明度（0-1，1 为不透明）。 |
| `visible` | bool | true | 是否可见。 |
| `mesh order` | number | 2 | 网格划分顺序。 |
| `override global mesh settings` | bool | false | 是否覆盖全局网格设置。 |
| `dx`, `dy`, `dz` | number | 0.02 | 各方向的网格步长（μm）。 |
| `grid mesh cells per wavelength` | number | 20 | 每波长网格单元数。 |
| `use relative coordinates` | bool | false | 是否使用相对坐标。 |
| `closed` | bool | true | 多边形是否闭合（始终为 true）。 |
| `fill` | bool | true | 多边形是否填充。 |
| `edge width` | number | 0 | 多边形边线宽度（显示用）。 |

## 返回值

`createpoly` 命令创建多边形对象，在 Python API 中返回创建的对象名称。在 LSF 中，该命令不直接返回值，但可以通过后续命令访问创建的多边形。

## 示例

### 示例 1：创建基本多边形
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建多边形，使用默认设置（三角形）
fdtd.createpoly("poly1")

print("创建的多边形属性:")
poly_props = fdtd.get("poly1")
print(f"  顶点数: {len(poly_props.get('points', []))}")
print(f"  高度: {poly_props.get('height', '未知')} μm")
print(f"  材料: {poly_props.get('material', '未知')}")

# 创建自定义多边形（指定顶点）
fdtd.createpoly("poly2", 
                0, 0, 0,    # 顶点1
                2, 0, 0,    # 顶点2
                2, 1, 0,    # 顶点3
                1, 2, 0,    # 顶点4
                0, 1, 0)    # 顶点5

print("\n自定义多边形 'poly2' 的顶点:")
poly2_props = fdtd.get("poly2")
points = poly2_props.get('points', [])
for i, point in enumerate(points):
    print(f"  顶点 {i}: ({point[0]}, {point[1]}, {point[2]})")

# 计算多边形面积（使用鞋带公式）
area = 0
n = len(points)
for i in range(n):
    x1, y1, _ = points[i]
    x2, y2, _ = points[(i + 1) % n]
    area += x1 * y2 - x2 * y1
area = abs(area) / 2

print(f"  多边形面积: {area:.3f} μm²")

# 计算周长
perimeter = 0
for i in range(n):
    x1, y1, z1 = points[i]
    x2, y2, z2 = points[(i + 1) % n]
    segment_length = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
    perimeter += segment_length

print(f"  多边形周长: {perimeter:.3f} μm")
```

### 示例 2：创建光子晶体结构
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_photonic_crystal_unit_cell(name, lattice_type="hexagonal", a=0.5, r=0.2, height=0.22, material="Si"):
    """创建光子晶体单元胞"""
    
    if lattice_type == "hexagonal":
        # 六角晶格：创建六边形
        points = []
        for i in range(6):
            angle = 2 * np.pi * i / 6
            x = a * np.cos(angle)
            y = a * np.sin(angle)
            points.extend([x, y, 0])
        
        # 创建六边形多边形
        fdtd.createpoly(name, *points)
        
    elif lattice_type == "square":
        # 正方晶格：创建正方形
        fdtd.createpoly(name,
                        -a/2, -a/2, 0,
                         a/2, -a/2, 0,
                         a/2,  a/2, 0,
                        -a/2,  a/2, 0)
    
    elif lattice_type == "triangular":
        # 三角晶格：创建三角形
        fdtd.createpoly(name,
                        0, a, 0,
                        a*np.sqrt(3)/2, -a/2, 0,
                        -a*np.sqrt(3)/2, -a/2, 0)
    
    # 设置多边形属性
    fdtd.set(name, "height", height)
    fdtd.set(name, "material", material)
    
    # 在中心添加孔（如果是完整单元胞）
    if r > 0:
        fdtd.addcircle(f"{name}_hole", x=0, y=0, z=0, radius=r, height=height, material="Air")
    
    return name

print("创建不同晶格类型的光子晶体单元胞...")

# 创建六角晶格单元胞
hex_cell = create_photonic_crystal_unit_cell("hex_unit_cell", "hexagonal", a=0.5, r=0.2)
print(f"六角晶格单元胞: {hex_cell}")

# 创建正方晶格单元胞
square_cell = create_photonic_crystal_unit_cell("square_unit_cell", "square", a=0.5, r=0.15)
print(f"正方晶格单元胞: {square_cell}")

# 创建三角晶格单元胞
tri_cell = create_photonic_crystal_unit_cell("tri_unit_cell", "triangular", a=0.6, r=0.18)
print(f"三角晶格单元胞: {tri_cell}")

# 计算光子晶体参数
print(f"\n光子晶体参数比较:")
for cell_name, lattice_type in [("hex_unit_cell", "六角"), ("square_unit_cell", "正方"), ("tri_unit_cell", "三角")]:
    try:
        props = fdtd.get(cell_name)
        points = props.get('points', [])
        a = 0.5  # 晶格常数
        
        # 计算填充因子（孔面积/单元胞面积）
        if lattice_type == "六角":
            # 六边形面积 = (3√3/2) * a^2
            area_cell = (3 * np.sqrt(3) / 2) * a**2
            r = 0.2
        elif lattice_type == "正方":
            area_cell = a**2
            r = 0.15
        else:  # 三角
            area_cell = (np.sqrt(3) / 4) * a**2
            r = 0.18
        
        area_hole = np.pi * r**2
        fill_factor = area_hole / area_cell
        
        print(f"  {lattice_type}晶格:")
        print(f"    晶格常数: {a} μm")
        print(f"    孔半径: {r} μm")
        print(f"    单元胞面积: {area_cell:.4f} μm²")
        print(f"    填充因子: {fill_factor:.2%}")
        
        # 估计带隙位置
        # 对于光子晶体，带隙中心波长 ≈ 2a * n_eff
        n_eff = 2.5  # 近似有效折射率
        bandgap_center = 2 * a * n_eff
        print(f"    带隙中心波长估计: {bandgap_center:.3f} μm")
        
    except Exception as e:
        print(f"  无法分析 {cell_name}: {e}")
```

### 示例 3：创建复杂光学元件（超透镜）
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_metalens_unit(name, center, size, phase_profile, wavelength=1.55, height=0.6, material="SiN"):
    """创建超透镜单元（基于相位轮廓）"""
    
    cx, cy, cz = center
    width, length = size
    
    # 根据相位轮廓确定单元形状
    # 相位范围 0-2π 映射到不同的多边形形状
    
    # 创建多边形顶点（示例：可变形状单元）
    points = []
    
    if phase_profile < np.pi/4:
        # 小相位：近矩形
        points = [
            [cx - width/2, cy - length/2, cz],
            [cx + width/2, cy - length/2, cz],
            [cx + width/2, cy + length/2, cz],
            [cx - width/2, cy + length/2, cz]
        ]
    elif phase_profile < np.pi/2:
        # 中等相位：六边形
        for i in range(6):
            angle = 2 * np.pi * i / 6 + phase_profile
            r = width/2 * (0.8 + 0.2 * np.sin(phase_profile))
            x = cx + r * np.cos(angle)
            y = cy + r * np.sin(angle)
            points.append([x, y, cz])
    else:
        # 大相位：复杂形状
        num_points = 8
        for i in range(num_points):
            angle = 2 * np.pi * i / num_points
            # 半径随相位和角度变化
            r = width/2 * (0.7 + 0.3 * np.sin(phase_profile) * np.cos(2*angle))
            x = cx + r * np.cos(angle)
            y = cy + r * np.sin(angle)
            points.append([x, y, cz])
    
    # 展平点列表
    flat_points = []
    for point in points:
        flat_points.extend(point)
    
    # 创建多边形
    fdtd.createpoly(name, *flat_points)
    
    # 设置属性
    fdtd.set(name, "height", height)
    fdtd.set(name, "material", material)
    
    # 根据相位设置颜色（可视化）
    hue = phase_profile / (2 * np.pi)  # 0-1
    r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.8)
    fdtd.set(name, "color", (r, g, b))
    
    return points

print("创建超透镜阵列...")

# 导入 colorsys 用于颜色转换
import colorsys

# 定义超透镜参数
lens_diameter = 20  # 透镜直径，μm
num_units_x = 10    # x方向单元数
num_units_y = 10    # y方向单元数
unit_size = (lens_diameter/num_units_x, lens_diameter/num_units_y)  # 单元尺寸

# 创建超透镜单元
units = []
focal_length = 30  # 焦距，μm

for i in range(num_units_x):
    for j in range(num_units_y):
        # 计算单元位置
        x = (i - (num_units_x-1)/2) * unit_size[0]
        y = (j - (num_units_y-1)/2) * unit_size[1]
        
        # 计算到透镜中心的距离
        r = np.sqrt(x**2 + y**2)
        
        # 计算所需相位（球面波前）
        # φ = (2π/λ) * (√(r² + f²) - f) ≈ (π/λf) * r²（傍轴近似）
        lambda0 = 1.55  # 波长，μm
        phase = (np.pi / (lambda0 * focal_length)) * r**2
        
        # 将相位归一化到 0-2π
        phase = phase % (2 * np.pi)
        
        # 创建单元
        unit_name = f"metalens_unit_{i}_{j}"
        create_metalens_unit(unit_name, 
                            center=(x, y, 0),
                            size=unit_size,
                            phase_profile=phase,
                            height=0.6)
        
        units.append(unit_name)

print(f"创建了 {len(units)} 个超透镜单元")

# 计算超透镜参数
print(f"\n超透镜参数:")
print(f"  直径: {lens_diameter} μm")
print(f"  焦距: {focal_length} μm")
print(f"  数值孔径 NA: {lens_diameter/(2*focal_length):.3f}")
print(f"  单元尺寸: {unit_size[0]:.2f} × {unit_size[1]:.2f} μm")
print(f"  单元数量: {num_units_x} × {num_units_y} = {num_units_x*num_units_y}")

# 计算衍射极限
diffraction_limit = 1.22 * 1.55 / (lens_diameter/focal_length)  # 艾里斑半径，μm
print(f"  衍射极限（艾里斑半径）: {diffraction_limit:.3f} μm")

# 验证相位轮廓
print(f"\n相位轮廓验证（中心、边缘单元）:")
center_unit = f"metalens_unit_{num_units_x//2}_{num_units_y//2}"
edge_unit = f"metalens_unit_0_0"

for unit_name in [center_unit, edge_unit]:
    try:
        props = fdtd.get(unit_name)
        color = props.get('color', (0,0,0))
        # 从颜色反向计算相位（简化）
        hue = colorsys.rgb_to_hsv(color[0], color[1], color[2])[0]
        phase_estimated = hue * 2 * np.pi
        print(f"  {unit_name}: 估计相位 = {phase_estimated:.3f} rad")
    except:
        print(f"  无法获取 {unit_name} 属性")
```

### 示例 4：创建微机电系统（MEMS）结构
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_comb_drive(name, center, num_fingers=10, finger_length=20, finger_width=1, gap=1, height=2, material="Si"):
    """创建梳齿驱动器（MEMS 常见结构）"""
    
    cx, cy, cz = center
    
    # 创建固定梳齿
    fixed_fingers = []
    for i in range(num_fingers):
        finger_name = f"{name}_fixed_finger_{i}"
        
        # 梳齿位置（交错排列）
        x_offset = i * (finger_width + gap)
        
        # 创建梳齿多边形（矩形）
        fdtd.createpoly(finger_name,
                        cx + x_offset, cy, cz,
                        cx + x_offset + finger_width, cy, cz,
                        cx + x_offset + finger_width, cy + finger_length, cz,
                        cx + x_offset, cy + finger_length, cz)
        
        fdtd.set(finger_name, "height", height)
        fdtd.set(finger_name, "material", material)
        fdtd.set(finger_name, "color", (0.7, 0.7, 0.7))  # 灰色
        
        fixed_fingers.append(finger_name)
    
    # 创建可动梳齿（在固定梳齿之间）
    movable_fingers = []
    for i in range(num_fingers - 1):
        finger_name = f"{name}_movable_finger_{i}"
        
        # 梳齿位置（在固定梳齿之间）
        x_offset = i * (finger_width + gap) + finger_width + gap/2
        
        # 创建梳齿多边形（矩形）
        fdtd.createpoly(finger_name,
                        cx + x_offset, cy, cz,
                        cx + x_offset + finger_width, cy, cz,
                        cx + x_offset + finger_width, cy + finger_length, cz,
                        cx + x_offset, cy + finger_length, cz)
        
        fdtd.set(finger_name, "height", height)
        fdtd.set(finger_name, "material", material)
        fdtd.set(finger_name, "color", (0.3, 0.3, 1.0))  # 蓝色
        
        movable_fingers.append(finger_name)
    
    # 创建锚点（固定部分）
    anchor_name = f"{name}_anchor"
    anchor_width = num_fingers * (finger_width + gap)
    fdtd.createpoly(anchor_name,
                    cx, cy - 5, cz,
                    cx + anchor_width, cy - 5, cz,
                    cx + anchor_width, cy, cz,
                    cx, cy, cz)
    
    fdtd.set(anchor_name, "height", height)
    fdtd.set(anchor_name, "material", material)
    fdtd.set(anchor_name, "color", (0.5, 0.5, 0.5))
    
    return fixed_fingers, movable_fingers, anchor_name

print("创建梳齿驱动器（MEMS 结构）...")
fixed, movable, anchor = create_comb_drive("comb_drive", 
                                          center=(0, 0, 0),
                                          num_fingers=8,
                                          finger_length=30,
                                          finger_width=1,
                                          gap=1,
                                          height=2)

print(f"创建的梳齿驱动器组件:")
print(f"  固定梳齿: {len(fixed)} 个")
print(f"  可动梳齿: {len(movable)} 个")
print(f"  锚点: {anchor}")

# 计算梳齿驱动器参数
print(f"\n梳齿驱动器参数:")
total_width = 8 * (1 + 1)  # num_fingers * (finger_width + gap)
print(f"  总宽度: {total_width} μm")
print(f"  梳齿长度: 30 μm")
print(f"  梳齿宽度: 1 μm")
print(f"  梳齿间隙: 1 μm")
print(f"  结构高度: 2 μm")

# 计算静电驱动力（简化）
# F = (1/2) * ε₀ * εᵣ * (V^2/d) * A，其中 A 是重叠面积
epsilon_0 = 8.854e-12 * 1e12  # F/μm
epsilon_r = 1.0  # 空气介电常数
V = 10  # 电压，V
d = 1e-6  # 间隙，m（转换为 μm）

# 单个梳齿的重叠面积
overlap_area_per_finger = 30 * 2  # 长度 * 高度，μm²
total_fingers = len(movable)  # 可动梳齿数量
total_overlap_area = overlap_area_per_finger * total_fingers

# 静电力
F_electrostatic = 0.5 * epsilon_0 * epsilon_r * (V**2 / d) * total_overlap_area
print(f"\n静电驱动分析（电压={V}V）:")
print(f"  单个梳齿重叠面积: {overlap_area_per_finger} μm²")
print(f"  总重叠面积: {total_overlap_area} μm²")
print(f"  估计静电力: {F_electrostatic:.2e} N")
print(f"  估计静电力: {F_electrostatic * 1e6:.2f} μN")

# 计算机械刚度（简化）
# 对于悬臂梁：k = (E * w * t^3) / (4 * L^3)
E_si = 169e9  # 硅的杨氏模量，Pa
w = 1e-6  # 梁宽度，m
t = 2e-6  # 梁厚度，m
L = 20e-6  # 梁长度，m

k_mechanical = (E_si * w * t**3) / (4 * L**3)
print(f"\n机械刚度分析:")
print(f"  估计机械刚度: {k_mechanical:.2f} N/m")

# 计算位移
displacement = F_electrostatic / k_mechanical
print(f"  估计位移: {displacement * 1e9:.2f} nm")

# 计算谐振频率
# f = (1/2π) * √(k/m)，其中 m 是质量
rho_si = 2330  # 硅密度，kg/m³
volume = total_overlap_area * 1e-12 * t  # 体积，m³
mass = rho_si * volume
f_resonant = (1/(2*np.pi)) * np.sqrt(k_mechanical / mass)
print(f"  估计谐振频率: {f_resonant:.2f} Hz")
print(f"  估计谐振频率: {f_resonant/1e3:.2f} kHz")
```

### 示例 5：高级多边形工具
```python
import lumapi
import numpy as np
import matplotlib.path as mpath

class PolygonDesigner:
    """高级多边形设计工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_star_polygon(self, name, center, outer_radius, inner_radius, num_points=5, 
                           height=0.1, material="Si"):
        """创建星形多边形"""
        
        cx, cy, cz = center
        
        points = []
        for i in range(2 * num_points):
            angle = np.pi * i / num_points
            
            if i % 2 == 0:
                radius = outer_radius
            else:
                radius = inner_radius
            
            x = cx + radius * np.cos(angle)
            y = cy + radius * np.sin(angle)
            points.extend([x, y, cz])
        
        # 创建多边形
        self.session.createpoly(name, *points)
        self.session.set(name, "height", height)
        self.session.set(name, "material", material)
        
        return points
    
    def create_rounded_polygon(self, name, center, radius, num_sides=6, corner_radius=0.1,
                              height=0.1, material="Si"):
        """创建圆角多边形"""
        
        cx, cy, cz = center
        
        # 生成多边形的角点
        corners = []
        for i in range(num_sides):
            angle = 2 * np.pi * i / num_sides
            x = cx + radius * np.cos(angle)
            y = cy + radius * np.sin(angle)
            corners.append((x, y))
        
        # 创建圆角多边形的路径
        path = mpath.Path()
        
        # 移动到第一个角
        first_corner = corners[0]
        prev_corner = corners[-1]
        next_corner = corners[1]
        
        # 计算第一个角的切线方向
        # 这里简化处理，实际需要更复杂的圆角算法
        
        # 对于简化版本，我们创建普通多边形
        points = []
        for corner in corners:
            points.extend([corner[0], corner[1], cz])
        
        # 添加第一个点以闭合多边形
        points.extend([corners[0][0], corners[0][1], cz])
        
        # 创建多边形
        self.session.createpoly(name, *points)
        self.session.set(name, "height", height)
        self.session.set(name, "material", material)
        
        print(f"注意: 简化版本创建了 {num_sides} 边形，圆角功能需要更复杂的实现")
        
        return points
    
    def create_fractal_polygon(self, name, center, size, depth=3, height=0.1, material="Si"):
        """创建分形多边形（科赫雪花）"""
        
        def koch_snowflake(order, size):
            """生成科赫雪花的顶点"""
            
            def koch_curve(p1, p2, order):
                if order == 0:
                    return [p1, p2]
                
                # 计算三等分点
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                
                # 三个分段点
                pA = (p1[0] + dx/3, p1[1] + dy/3)
                pC = (p1[0] + 2*dx/3, p1[1] + 2*dy/3)
                
                # 计算凸点
                # 旋转向量 (dx/3, dy/3) 60度
                angle = np.radians(60)
                cos_a = np.cos(angle)
                sin_a = np.sin(angle)
                rx = (dx/3) * cos_a - (dy/3) * sin_a
                ry = (dx/3) * sin_a + (dy/3) * cos_a
                
                pB = (pA[0] + rx, pA[1] + ry)
                
                # 递归生成
                return (koch_curve(p1, pA, order-1)[:-1] + 
                        koch_curve(pA, pB, order-1)[:-1] + 
                        koch_curve(pB, pC, order-1)[:-1] + 
                        koch_curve(pC, p2, order-1))
            
            # 初始等边三角形
            p1 = (0, -size/2)
            p2 = (size * np.sqrt(3)/2, size/2)
            p3 = (-size * np.sqrt(3)/2, size/2)
            
            # 生成三条边
            points = (koch_curve(p1, p2, order)[:-1] + 
                     koch_curve(p2, p3, order)[:-1] + 
                     koch_curve(p3, p1, order))
            
            return points
        
        cx, cy, cz = center
        
        # 生成分形顶点
        fractal_points = koch_snowflake(depth, size)
        
        # 平移和展平顶点
        points = []
        for point in fractal_points:
            points.extend([cx + point[0], cy + point[1], cz])
        
        # 创建分形多边形
        self.session.createpoly(name, *points)
        self.session.set(name, "height", height)
        self.session.set(name, "material", material)
        
        return fractal_points
    
    def analyze_polygon_properties(self, poly_name):
        """分析多边形的几何属性"""
        
        props = self.session.get(poly_name)
        points = props.get('points', [])
        height = props.get('height', 0)
        material = props.get('material', '')
        
        # 计算面积（使用鞋带公式）
        area = 0
        n = len(points)
        for i in range(n):
            x1, y1, _ = points[i]
            x2, y2, _ = points[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        area = abs(area) / 2
        
        # 计算周长和边长统计
        perimeter = 0
        segment_lengths = []
        
        for i in range(n):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[(i + 1) % n]
            length = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
            perimeter += length
            segment_lengths.append(length)
        
        # 计算体积
        volume = area * height
        
        # 计算中心点
        cx = sum(p[0] for p in points) / n
        cy = sum(p[1] for p in points) / n
        
        # 计算凸性（简化）
        def is_convex(polygon_points):
            """检查多边形是否凸"""
            n = len(polygon_points)
            if n < 4:
                return True
            
            def cross(o, a, b):
                return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
            
            # 检查所有连续三个点的转向是否一致
            sign = 0
            for i in range(n):
                o = polygon_points[i]
                a = polygon_points[(i+1)%n]
                b = polygon_points[(i+2)%n]
                curr_sign = cross(o, a, b)
                
                if curr_sign != 0:
                    if sign == 0:
                        sign = curr_sign
                    elif sign * curr_sign < 0:
                        return False
            
            return True
        
        convex = is_convex(points)
        
        return {
            'name': poly_name,
            'num_vertices': n,
            'area': area,
            'perimeter': perimeter,
            'height': height,
            'volume': volume,
            'material': material,
            'centroid': (cx, cy),
            'convex': convex,
            'min_side_length': min(segment_lengths) if segment_lengths else 0,
            'max_side_length': max(segment_lengths) if segment_lengths else 0,
            'avg_side_length': np.mean(segment_lengths) if segment_lengths else 0
        }

# 使用示例
fdtd = lumapi.FDTD()
designer = PolygonDesigner(fdtd)

print("示例1: 创建星形多边形")
star_points = designer.create_star_polygon("star", 
                                          center=(0, 0, 0),
                                          outer_radius=2,
                                          inner_radius=1,
                                          num_points=6,
                                          height=0.22,
                                          material="Si")
print(f"星形多边形有 {len(star_points)//3} 个顶点")

print("\n示例2: 创建圆角六边形")
hex_points = designer.create_rounded_polygon("rounded_hexagon",
                                            center=(5, 0, 0),
                                            radius=1.5,
                                            num_sides=6,
                                            corner_radius=0.2,
                                            height=0.22,
                                            material="SiO2")
print(f"圆角六边形创建完成")

print("\n示例3: 创建分形多边形（科赫雪花）")
fractal_points = designer.create_fractal_polygon("koch_snowflake",
                                                center=(-5, 0, 0),
                                                size=3,
                                                depth=2,
                                                height=0.22,
                                                material="SiN")
print(f"科赫雪花有 {len(fractal_points)} 个顶点（分形深度 2）")

print("\n示例4: 分析多边形属性")
polygons_to_analyze = ["star", "rounded_hexagon", "koch_snowflake"]

for poly_name in polygons_to_analyze:
    try:
        analysis = designer.analyze_polygon_properties(poly_name)
        print(f"\n{poly_name} 分析:")
        print(f"  顶点数: {analysis['num_vertices']}")
        print(f"  面积: {analysis['area']:.4f} μm²")
        print(f"  周长: {analysis['perimeter']:.4f} μm")
        print(f"  高度: {analysis['height']} μm")
        print(f"  体积: {analysis['volume']:.4f} μm³")
        print(f"  材料: {analysis['material']}")
        print(f"  是否凸多边形: {analysis['convex']}")
        print(f"  中心点: ({analysis['centroid'][0]:.3f}, {analysis['centroid'][1]:.3f})")
        print(f"  边长范围: {analysis['min_side_length']:.3f}-{analysis['max_side_length']:.3f} μm")
        print(f"  平均边长: {analysis['avg_side_length']:.3f} μm")
    except Exception as e:
        print(f"  无法分析 {poly_name}: {e}")

# 计算分形维数（近似）
print(f"\n分形维数估计（科赫雪花）:")
# 科赫雪花的理论分形维数 = log(4)/log(3) ≈ 1.2619
depth = 2
size = 3
perimeter_koch = analysis['perimeter']
area_koch = analysis['area']

# 周长增长因子（每增加一级，周长变为 4/3 倍）
perimeter_growth_factor = 4/3
# 面积增长因子（理论值）
area_growth_factor = (4/9)  # 对于科赫雪花

print(f"  理论分形维数: {np.log(4)/np.log(3):.4f}")
print(f"  实际周长/面积比: {perimeter_koch/area_koch:.4f}")
```

## 注意事项

1. **顶点顺序**：多边形的顶点必须按顺序（顺时针或逆时针）提供，以确保正确的形状。

2. **凸多边形与凹多边形**：Lumerical 支持凸多边形和凹多边形，但凹多边形在网格划分和仿真时可能需要特殊处理。

3. **最小顶点数**：多边形至少需要三个顶点。顶点共线或重合可能导致错误。

4. **网格划分**：复杂多边形，特别是凹多边形或带有锐角的多边形，可能需要精细网格以确保计算精度。

5. **性能考虑**：包含大量顶点的复杂多边形会增加网格复杂度和仿真时间。考虑简化或使用参数化形状。

6. **三维结构**：多边形是二维形状，通过设置 `height` 属性可以创建三维棱柱结构。

7. **与 `addpoly` 的区别**：`createpoly` 和 `addpoly` 功能相似，但可能有细微的语法或默认值差异。在 Lumerical 脚本中，两者通常可以互换使用。

8. **布尔运算**：多边形可以与其他几何结构进行布尔运算，用于创建复杂的二维形状。

## 错误处理

使用 `createpoly` 命令时可能遇到的常见错误及其解决方案：

### 1. 顶点数量不足
- **错误信息**: "Insufficient vertices to define a polygon"
- **原因**: 提供的顶点数少于3个
- **解决方案**: 确保提供至少3个顶点坐标

### 2. 顶点共线
- **错误信息**: "Vertices are collinear"
- **原因**: 所有顶点位于同一直线上，无法形成有效多边形
- **解决方案**: 检查顶点坐标，确保至少三个点不共线

### 3. 坐标超出仿真区域
- **错误信息**: "Coordinates outside simulation region"
- **原因**: 多边形顶点位于仿真区域外
- **解决方案**: 调整顶点坐标或扩大仿真区域

### 4. 内存不足
- **错误信息**: "Insufficient memory"
- **原因**: 多边形顶点过多或结构太复杂
- **解决方案**: 简化多边形，减少顶点数量

### 5. 材料未定义
- **错误信息**: "Material not defined"
- **原因**: 指定的材料名称不存在
- **解决方案**: 使用有效材料名称，或先定义材料

### 6. Python API 参数错误
- **错误信息**: "Invalid argument type"
- **原因**: 传递给 `createpoly` 的参数类型不正确
- **解决方案**: 确保坐标参数为数字，名称参数为字符串
  ```python
  try:
      fdtd.createpoly("mypoly", 0, 0, 0, 1, 0, 0, 0, 1, 0)
  except TypeError as e:
      print(f"参数错误: {e}")
  ```

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于创建复杂光学结构 |
| MODE Solutions | ✅ 完全支持 | 用于创建波导和光子晶体 |
| DEVICE | ✅ 完全支持 | 用于创建 MEMS 和微结构 |
| INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用不同的几何系统 |

## 相关命令

- `addpoly` - 添加多边形（功能相似）
- `createrect` - 创建矩形
- `createcircle` - 创建圆形
- `createline` - 创建线
- `set` - 设置多边形属性
- `get` - 获取多边形属性
- `copy` - 复制多边形

## 参考

1. Lumerical FDTD User Guide - Geometry Creation
2. Lumerical Script Language Reference - createpoly command
3. Computational Geometry Algorithms for Polygon Manipulation

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含多边形创建和高级示例 |
| 1.1 | 2026-01-31 | 添加返回值、错误处理章节，完善文档结构 |

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*