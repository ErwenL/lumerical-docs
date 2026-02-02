# `createline` - 创建线

## 概述

`createline` 命令用于在仿真中创建线状几何结构。线是 Lumerical 中的一维或二维结构，常用于创建波导、导线、电极、光栅线条等。该命令允许用户通过指定顶点坐标来定义折线或多段线，可以设置线的宽度、高度、材料等属性，用于模拟各种线状光学和电学元件。

线结构在光子集成电路（PIC）、微波电路和微机电系统（MEMS）设计中非常常见，特别是用于创建复杂的布线、耦合结构和衍射元件。

## 语法

### LSF 语法
```lumerical
createline(name);                    # 创建线，使用默认设置
createline(name, x1, y1, z1, x2, y2, z2, ...);  # 创建线并指定顶点
createline(name, property, value, ...);  # 创建线并设置属性
```

### Python API
```python
session.createline(name)                     # 创建线，使用默认设置
session.createline(name, x1, y1, z1, x2, y2, z2, ...)  # 创建线并指定顶点
session.createline(name, property1=value1, property2=value2, ...)  # 创建线并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 线的名称。 | 是 |
| `x, y, z` | number | 线的顶点坐标（μm）。可以指定多个顶点来定义折线。 | 可选 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `points` | array | [[0,0,0], [1,0,0]] | 线的顶点坐标数组。 |
| `x`, `y`, `z` | number | 0 | 线的参考点位置（μm）。 |
| `width` | number | 0.1 | 线的宽度（μm）。 |
| `height` | number | 0.1 | 线的高度（厚度，μm）。 |
| `material` | string | "" | 线材料的名称。如果为空，则使用全局材料。 |
| `index` | number | 1.0 | 线的折射率（如果未指定材料）。 |
| `color` | string | "custom" | 显示颜色（RGB 值或颜色名称）。 |
| `alpha` | number | 1.0 | 透明度（0-1，1 为不透明）。 |
| `visible` | bool | true | 是否可见。 |
| `mesh order` | number | 2 | 网格划分顺序。 |
| `override global mesh settings` | bool | false | 是否覆盖全局网格设置。 |
| `dx`, `dy`, `dz` | number | 0.02 | 各方向的网格步长（μm）。 |
| `grid mesh cells per wavelength` | number | 20 | 每波长网格单元数。 |
| `use relative coordinates` | bool | false | 是否使用相对坐标。 |
| `line type` | string | "solid" | 线类型："solid"（实线）、"dashed"（虚线）、"dotted"（点线）。 |
| `line width` | number | 1 | 显示线宽（像素）。 |
| `round ends` | bool | false | 线端是否圆角。 |
 | `closed` | bool | false | 线是否闭合（形成多边形）。 |

## 返回值

`createline` 命令没有返回值。成功执行后，会在仿真中创建一个线对象。

## 示例

### 示例 1：创建基本线
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建线，使用默认设置（从 (0,0,0) 到 (1,0,0)）
fdtd.createline("line1")

print("创建的线属性:")
line_props = fdtd.get("line1")
print(f"  顶点数: {len(line_props.get('points', []))}")
print(f"  宽度: {line_props.get('width', '未知')} μm")
print(f"  高度: {line_props.get('height', '未知')} μm")
print(f"  材料: {line_props.get('material', '未知')}")

# 创建自定义线（指定顶点）
fdtd.createline("line2", 
                0, 0, 0,    # 起点
                2, 0, 0,    # 第二点
                2, 1, 0,    # 第三点
                0, 1, 0)    # 终点

print("\n自定义线 'line2' 的顶点:")
line2_props = fdtd.get("line2")
points = line2_props.get('points', [])
for i, point in enumerate(points):
    print(f"  顶点 {i}: ({point[0]}, {point[1]}, {point[2]})")

# 计算线长度
total_length = 0
for i in range(len(points) - 1):
    p1 = points[i]
    p2 = points[i + 1]
    segment_length = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)**0.5
    total_length += segment_length
    print(f"  段 {i}-{i+1} 长度: {segment_length:.3f} μm")

print(f"  总长度: {total_length:.3f} μm")
```

### 示例 2：创建弯曲波导
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_bent_waveguide(name, start_point, end_point, radius, width=0.5, height=0.22, material="Si"):
    """创建弯曲波导（S-弯曲或圆弧弯曲）"""
    
    x1, y1, z1 = start_point
    x2, y2, z2 = end_point
    
    # 计算弯曲参数
    dx = x2 - x1
    dy = y2 - y1
    
    # 创建 S-弯曲波导的顶点
    points = []
    
    # 起点
    points.append([x1, y1, z1])
    
    # 第一段水平线
    points.append([x1 + dx/4, y1, z1])
    
    # 第一弯曲（使用多个点近似圆弧）
    center_x1 = x1 + dx/4
    center_y1 = y1 + radius
    for angle in np.linspace(-90, 0, 10):  # 90度圆弧
        rad = np.radians(angle)
        x = center_x1 + radius * np.cos(rad)
        y = center_y1 + radius * np.sin(rad)
        points.append([x, y, z1])
    
    # 中间水平线
    points.append([x2 - dx/4, y1 + 2*radius, z1])
    
    # 第二弯曲
    center_x2 = x2 - dx/4
    center_y2 = y1 + radius
    for angle in np.linspace(0, 90, 10):  # 90度圆弧
        rad = np.radians(angle)
        x = center_x2 + radius * np.cos(rad)
        y = center_y2 + radius * np.sin(rad)
        points.append([x, y, z1])
    
    # 最后一段水平线
    points.append([x2, y2, z1])
    
    # 创建线
    # 注意：createline 需要将点列表展平
    flat_points = []
    for point in points:
        flat_points.extend(point)
    
    # 创建线结构
    fdtd.createline(name, *flat_points)
    
    # 设置线属性
    fdtd.set(name, "width", width)
    fdtd.set(name, "height", height)
    fdtd.set(name, "material", material)
    fdtd.set(name, "closed", False)
    
    return points

print("创建 S-弯曲波导...")
waveguide_points = create_bent_waveguide("s_bend_waveguide",
                                         start_point=(0, 0, 0),
                                         end_point=(10, 0, 0),
                                         radius=5,
                                         width=0.5,
                                         height=0.22)

print(f"创建的波导 '{s_bend_waveguide}' 有 {len(waveguide_points)} 个顶点")

# 计算波导参数
print(f"\n波导参数:")
print(f"  宽度: 0.5 μm")
print(f"  高度: 0.22 μm")
print(f"  弯曲半径: 5 μm")
print(f"  总水平跨度: 10 μm")

# 计算弯曲损耗估计
# 对于弯曲波导，弯曲损耗与 exp(-R/Rc) 成正比，其中 Rc 是临界半径
R = 5  # 弯曲半径
lambda0 = 1.55  # 波长
n_eff = 2.5  # 有效折射率
Rc = n_eff * lambda0 / (2 * np.pi)  # 临界半径近似
loss_factor = np.exp(-R / Rc)
print(f"  临界半径 Rc: {Rc:.3f} μm")
print(f"  弯曲损耗因子: {loss_factor:.6f} (约 {-10*np.log10(loss_factor):.2f} dB/90°)")

# 可视化顶点
print(f"\n前5个顶点:")
for i, point in enumerate(waveguide_points[:5]):
    print(f"  顶点 {i}: ({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})")
```

### 示例 3：创建复杂布线（电极）
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_electrode_wiring(name, start_point, width=0.2, height=0.1, material="Au"):
    """创建复杂的电极布线"""
    
    x, y, z = start_point
    
    # 定义布线路径（模拟复杂的集成电路布线）
    points = [
        [x, y, z],                    # 起点
        [x + 5, y, z],                # 向右5μm
        [x + 5, y + 3, z],            # 向上3μm
        [x + 2, y + 3, z],            # 向左3μm
        [x + 2, y + 5, z],            # 向上2μm
        [x + 8, y + 5, z],            # 向右6μm
        [x + 8, y + 2, z],            # 向下3μm
        [x + 10, y + 2, z],           # 向右2μm
        [x + 10, y + 8, z],           # 向上6μm
        [x + 3, y + 8, z],            # 向左7μm
        [x + 3, y + 10, z],           # 向上2μm
        [x + 12, y + 10, z],          # 向右9μm（终点）
    ]
    
    # 展平点列表
    flat_points = []
    for point in points:
        flat_points.extend(point)
    
    # 创建线
    fdtd.createline(name, *flat_points)
    
    # 设置电极属性
    fdtd.set(name, "width", width)
    fdtd.set(name, "height", height)
    fdtd.set(name, "material", material)
    fdtd.set(name, "color", (1.0, 0.84, 0.0))  # 金色
    
    return points

print("创建复杂电极布线...")
electrode_points = create_electrode_wiring("electrode_wiring", start_point=(0, 0, 0))

print(f"创建的电极 '{electrode_wiring}' 有 {len(electrode_points)} 个顶点")

# 计算布线总长度
total_length = 0
for i in range(len(electrode_points) - 1):
    p1 = electrode_points[i]
    p2 = electrode_points[i + 1]
    segment_length = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)**0.5
    total_length += segment_length

print(f"\n电极布线参数:")
print(f"  总长度: {total_length:.2f} μm")
print(f"  线宽: 0.2 μm")
print(f"  线高: 0.1 μm")
print(f"  材料: Au (金)")

# 计算电阻（简化）
# R = ρ * L / (w * h)，其中 ρ 是电阻率
rho_au = 2.44e-8  # 金的电阻率，Ω·m（转换为 Ω·μm）
length_um = total_length
width_um = 0.2
height_um = 0.1

# 单位转换：1 Ω·m = 1e12 Ω·μm
rho_au_um = rho_au * 1e12

resistance = rho_au_um * length_um / (width_um * height_um)
print(f"  估计电阻: {resistance:.2f} Ω")

# 计算电容（简化，与基板形成平行板电容）
epsilon_r = 3.9  # SiO2的相对介电常数
epsilon_0 = 8.854e-12 * 1e12  # F/μm
distance_to_ground = 0.5  # 到地平面的距离，μm

# 电容 C = ε₀εᵣ * (L*w) / d
capacitance = epsilon_0 * epsilon_r * (length_um * width_um) / distance_to_ground
print(f"  估计电容: {capacitance:.2e} F")

# 计算 RC 时间常数
RC_constant = resistance * capacitance
print(f"  RC 时间常数: {RC_constant:.2e} s")
print(f"  3dB 带宽: {1/(2*np.pi*RC_constant):.2e} Hz")
```

### 示例 4：创建光栅结构
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_grating_lines(name, start_point, length=10, period=0.5, duty_cycle=0.5, 
                        line_width=None, gap_width=None, height=0.22, material="Si"):
    """创建光栅线结构"""
    
    if line_width is None:
        line_width = period * duty_cycle
    if gap_width is None:
        gap_width = period * (1 - duty_cycle)
    
    x_start, y_start, z_start = start_point
    
    # 计算光栅线数量
    num_lines = int(length / period)
    
    # 创建所有光栅线的顶点
    all_points = []
    
    for i in range(num_lines):
        # 每条线的起点和终点
        x_line_start = x_start + i * period
        x_line_end = x_line_start + line_width
        
        # 创建一条光栅线（垂直线）
        line_points = [
            [x_line_start, y_start, z_start],           # 起点
            [x_line_start, y_start + length, z_start],  # 向上
            [x_line_end, y_start + length, z_start],    # 向右
            [x_line_end, y_start, z_start],             # 向下
            [x_line_start, y_start, z_start]            # 闭合
        ]
        
        all_points.extend(line_points)
    
    # 展平点列表
    flat_points = []
    for point in all_points:
        flat_points.extend(point)
    
    # 创建线（闭合多边形）
    fdtd.createline(name, *flat_points)
    fdtd.set(name, "closed", True)  # 闭合线形成多边形
    fdtd.set(name, "height", height)
    fdtd.set(name, "material", material)
    
    return num_lines, period, duty_cycle

print("创建光栅结构...")
num_lines, period, duty_cycle = create_grating_lines("grating",
                                                     start_point=(0, 0, 0),
                                                     length=5,
                                                     period=0.7,
                                                     duty_cycle=0.6,
                                                     height=0.22)

print(f"创建的光栅 '{grating}' 有 {num_lines} 条线")

print(f"\n光栅参数:")
print(f"  周期: {period} μm")
print(f"  占空比: {duty_cycle}")
print(f"  线宽: {period * duty_cycle:.3f} μm")
print(f"  间隙: {period * (1 - duty_cycle):.3f} μm")
print(f"  光栅长度: 5 μm")
print(f"  光栅高度: 0.22 μm")

# 计算光栅的衍射特性
lambda0 = 1.55  # 波长，μm
n_eff = 2.5     # 有效折射率

# 布拉格条件：mλ = 2Λ sinθ，其中 Λ 是光栅周期
# 对于垂直入射（θ=90°），mλ = 2Λ
bragg_wavelength = 2 * period * n_eff
print(f"\n衍射特性:")
print(f"  布拉格波长（一阶）: {bragg_wavelength:.3f} μm")

# 计算不同衍射级次
print(f"  衍射级次对应的波长:")
for m in range(1, 4):  # 1-3级
    wavelength = 2 * period * n_eff / m
    if 1.2 <= wavelength <= 1.7:  # 通信波段
        print(f"    第 {m} 级: {wavelength:.3f} μm")

# 计算光栅的耦合系数 κ
# 近似公式：κ ≈ πΔn/λ，其中 Δn 是折射率调制深度
delta_n = 0.1  # 假设折射率调制深度
kappa = np.pi * delta_n / lambda0
print(f"  耦合系数 κ: {kappa:.3f} μm⁻¹")

# 计算最佳光栅长度（π/2 耦合器）
L_opt = np.pi / (2 * kappa)
print(f"  π/2 耦合器最佳长度: {L_opt:.3f} μm")

# 计算反射率（简化）
R_max = np.tanh(kappa * 5)**2  # 假设光栅长度 5μm
print(f"  最大反射率（长度 5μm）: {R_max:.3f}")
```

### 示例 5：高级线设计工具
```python
import lumapi
import numpy as np

class LineDesigner:
    """高级线设计工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_spiral(self, name, center, radius_start, radius_end, turns, 
                     height=0, width=0.1, material="Si"):
        """创建螺旋线"""
        
        cx, cy, cz = center
        
        # 生成螺旋点
        points = []
        num_points_per_turn = 50
        total_points = int(turns * num_points_per_turn)
        
        for i in range(total_points + 1):
            # 计算当前角度和半径
            angle = 2 * np.pi * turns * i / total_points
            radius = radius_start + (radius_end - radius_start) * i / total_points
            
            # 计算螺旋点坐标
            x = cx + radius * np.cos(angle)
            y = cy + radius * np.sin(angle)
            z = cz + height
            
            points.append([x, y, z])
        
        # 展平点列表
        flat_points = []
        for point in points:
            flat_points.extend(point)
        
        # 创建螺旋线
        self.session.createline(name, *flat_points)
        self.session.set(name, "width", width)
        self.session.set(name, "material", material)
        
        return points
    
    def create_meander_line(self, name, start_point, length, width, pitch, 
                           num_segments, height=0, material="Au"):
        """创建曲折线（meander line）"""
        
        x, y, z = start_point
        
        points = [[x, y, z]]
        
        segment_length = length / num_segments
        
        for i in range(num_segments):
            if i % 2 == 0:
                # 向右
                x += segment_length
            else:
                # 向左
                x -= segment_length
            
            points.append([x, y, z])
            
            # 每次转折后向上移动
            if i < num_segments - 1:
                y += pitch
                points.append([x, y, z])
        
        # 展平点列表
        flat_points = []
        for point in points:
            flat_points.extend(point)
        
        # 创建曲折线
        self.session.createline(name, *flat_points)
        self.session.set(name, "width", width)
        self.session.set(name, "height", 0.1)  # 默认高度
        self.session.set(name, "material", material)
        
        return points
    
    def create_spline_curve(self, name, control_points, num_samples=100, 
                           width=0.1, material="Si"):
        """创建样条曲线"""
        
        # 简单的 Catmull-Rom 样条
        def catmull_rom(p0, p1, p2, p3, t):
            """Catmull-Rom 样条插值"""
            return 0.5 * (
                (2 * p1) +
                (-p0 + p2) * t +
                (2*p0 - 5*p1 + 4*p2 - p3) * t**2 +
                (-p0 + 3*p1 - 3*p2 + p3) * t**3
            )
        
        # 生成样条点
        points = []
        n = len(control_points)
        
        for i in range(n):
            p0 = control_points[max(i-1, 0)]
            p1 = control_points[i]
            p2 = control_points[min(i+1, n-1)]
            p3 = control_points[min(i+2, n-1)]
            
            for j in range(num_samples):
                t = j / num_samples
                x = catmull_rom(p0[0], p1[0], p2[0], p3[0], t)
                y = catmull_rom(p0[1], p1[1], p2[1], p3[1], t)
                z = catmull_rom(p0[2], p1[2], p2[2], p3[2], t)
                
                points.append([x, y, z])
        
        # 展平点列表
        flat_points = []
        for point in points:
            flat_points.extend(point)
        
        # 创建样条线
        self.session.createline(name, *flat_points)
        self.session.set(name, "width", width)
        self.session.set(name, "material", material)
        
        return points
    
    def analyze_line_properties(self, line_name):
        """分析线的几何属性"""
        
        props = self.session.get(line_name)
        points = props.get('points', [])
        width = props.get('width', 0)
        height = props.get('height', 0)
        material = props.get('material', '')
        
        # 计算总长度
        total_length = 0
        segment_lengths = []
        
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            length = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)**0.5
            total_length += length
            segment_lengths.append(length)
        
        # 计算体积
        cross_section_area = width * height
        volume = total_length * cross_section_area
        
        return {
            'name': line_name,
            'num_points': len(points),
            'num_segments': len(segment_lengths),
            'total_length': total_length,
            'width': width,
            'height': height,
            'material': material,
            'cross_section_area': cross_section_area,
            'volume': volume,
            'min_segment_length': min(segment_lengths) if segment_lengths else 0,
            'max_segment_length': max(segment_lengths) if segment_lengths else 0,
            'avg_segment_length': np.mean(segment_lengths) if segment_lengths else 0
        }

# 使用示例
fdtd = lumapi.FDTD()
designer = LineDesigner(fdtd)

print("示例1: 创建螺旋线")
spiral_points = designer.create_spiral("spiral_inductor",
                                       center=(0, 0, 0),
                                       radius_start=1,
                                       radius_end=5,
                                       turns=3,
                                       width=0.2,
                                       material="Au")
print(f"螺旋线有 {len(spiral_points)} 个点")

print("\n示例2: 创建曲折线")
meander_points = designer.create_meander_line("meander_line",
                                              start_point=(0, 0, 0),
                                              length=20,
                                              width=0.1,
                                              pitch=1,
                                              num_segments=10,
                                              material="Al")
print(f"曲折线有 {len(meander_points)} 个点")

print("\n示例3: 创建样条曲线")
control_points = [[0, 0, 0], [2, 3, 0], [5, 1, 0], [8, 4, 0], [10, 0, 0]]
spline_points = designer.create_spline_curve("spline_waveguide",
                                             control_points,
                                             num_samples=20,
                                             width=0.5,
                                             material="Si")
print(f"样条曲线有 {len(spline_points)} 个点")

print("\n示例4: 分析线属性")
lines_to_analyze = ["spiral_inductor", "meander_line", "spline_waveguide"]

for line_name in lines_to_analyze:
    try:
        analysis = designer.analyze_line_properties(line_name)
        print(f"\n{line_name} 分析:")
        print(f"  总长度: {analysis['total_length']:.2f} μm")
        print(f"  点数: {analysis['num_points']}")
        print(f"  段数: {analysis['num_segments']}")
        print(f"  截面积: {analysis['cross_section_area']:.4f} μm²")
        print(f"  体积: {analysis['volume']:.4f} μm³")
        print(f"  材料: {analysis['material']}")
    except Exception as e:
        print(f"  无法分析 {line_name}: {e}")

# 计算螺旋电感器的电感（简化）
print("\n螺旋电感器参数估计:")
spiral_analysis = designer.analyze_line_properties("spiral_inductor")
avg_radius = (1 + 5) / 2  # 平均半径
turns = 3

# 简化电感公式：L ≈ μ₀ * N² * r_avg * ln(2r_avg/w)
mu0 = 4 * np.pi * 1e-7 * 1e6  # H/μm
N = turns
r_avg = avg_radius
w = 0.2  # 线宽

L_estimate = mu0 * N**2 * r_avg * np.log(2 * r_avg / w)
print(f"  估计电感: {L_estimate:.2e} H")
print(f"  估计电感: {L_estimate * 1e9:.2f} nH")
```

## 注意事项

1. **线宽和高度**：`createline` 创建的线具有宽度和高度，实际上是细长的矩形截面结构，不是数学意义上的线。

2. **顶点顺序**：顶点顺序决定了线的路径。确保顶点按所需顺序提供。

3. **闭合线**：设置 `closed=True` 可以使线首尾相连形成闭合多边形，用于创建环形结构。

4. **网格划分**：细线结构可能需要精细网格以确保计算精度，特别是当线宽小于波长时。

5. **性能考虑**：包含大量顶点的复杂线结构会增加网格复杂度和仿真时间。考虑简化或使用等效模型。

6. **与 `addline` 的区别**：`createline` 和 `addline` 功能相似，但可能有细微的语法或默认值差异。在 Lumerical 脚本中，两者通常可以互换使用。

7. **三维线**：虽然线通常用于二维布局，但通过指定 z 坐标可以创建三维空间中的线。

 8. **布尔运算**：线可以与其他几何结构进行布尔运算，用于创建更复杂的形状。

## 错误处理

### 常见错误
1. **顶点无效**: 顶点坐标不是数字，或顶点数量不足（至少需要2个顶点）
   - 解决方案：确保提供有效的数字坐标，且至少2个顶点

2. **宽度/高度无效**: `width` ≤ 0 或 `height` ≤ 0
   - 解决方案：确保 `width` > 0 且 `height` > 0

3. **点数组格式错误**: `points` 属性格式不正确
   - 解决方案：确保 `points` 是包含 [x,y,z] 列表的数组

4. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率通过 `index` 属性指定

5. **网格生成失败**: 线宽或线高太小导致网格问题
   - 解决方案：调整线尺寸，确保足够的网格分辨率

6. **名称冲突**: 线名称与现有对象重复
   - 解决方案：使用唯一的名称，或先删除同名对象

### Python 错误处理
```python
import lumapi
import numpy as np

try:
    fdtd = lumapi.FDTD()
    
    # 创建线
    fdtd.createline("test_line", 0, 0, 0, 5, 0, 0)  # 从 (0,0,0) 到 (5,0,0)
    
    # 检查参数有效性
    points = fdtd.get("test_line").get("points", [])
    width = fdtd.get("test_line").get("width", 0)
    height = fdtd.get("test_line").get("height", 0)
    
    if len(points) < 2:
        raise ValueError("至少需要2个顶点")
    if width <= 0:
        raise ValueError("线宽必须 > 0")
    if height <= 0:
        raise ValueError("线高必须 > 0")
    
    # 验证顶点坐标
    for i, point in enumerate(points):
        if len(point) != 3:
            raise ValueError(f"顶点 {i} 必须包含 x,y,z 三个坐标")
        if not all(isinstance(coord, (int, float)) for coord in point):
            raise ValueError(f"顶点 {i} 的坐标必须是数字")
    
    # 验证材料
    material = fdtd.get("test_line").get("material", "")
    if material and material not in fdtd.getmaterialnames():
        print(f"警告: 材料 '{material}' 不在数据库中，使用自定义折射率")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    fdtd.set("test_line", "width", 0.1)
    fdtd.set("test_line", "height", 0.1)
    
except Exception as e:
    print(f"线创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "width" in str(e).lower():
        print("错误: 线宽无效，请检查宽度值")
    elif "height" in str(e).lower():
        print("错误: 线高无效，请检查高度值")
    elif "points" in str(e).lower() or "vertex" in str(e).lower():
        print("错误: 顶点数据无效，请检查顶点坐标")
    elif "name" in str(e).lower():
        print("错误: 名称冲突，请使用不同的名称")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addline` - 添加线（功能相似）
- `createrect` - 创建矩形
- `createpoly` - 创建多边形
- `createcircle` - 创建圆形
- `set` - 设置线属性
- `get` - 获取线属性
- `copy` - 复制线

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于创建波导、电极等线状结构 |
| MODE Solutions | ✅ 完全支持 | 用于创建波导和耦合结构 |
| DEVICE | ✅ 完全支持 | 用于创建导线和互连 |
 | INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用不同的几何系统 |

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `line type` 和 `line width` 属性支持不同线型 |
| Lumerical 2019a | 改进线结构网格生成算法 |
| Lumerical 2018a | 新增 `createline` 命令，提供更灵活的线创建接口 |
| 1.1 | 更新日期，完善文档格式，添加错误处理和版本历史 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 线结构网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*