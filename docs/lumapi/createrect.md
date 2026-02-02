# `createrect` - 创建矩形

## 概述

`createrect` 命令用于在仿真中创建矩形几何结构。矩形是光学和光子学仿真中最常用的基本形状之一，用于创建波导、电极、基底、像素阵列等各种光学和电学元件。该命令允许用户指定矩形的位置、尺寸、材料等属性，是构建复杂仿真结构的基础工具。

矩形结构在光子集成电路（PIC）、微机电系统（MEMS）和半导体器件设计中无处不在，因其简单的几何形状和易于制造的优点而被广泛使用。

## 语法

### LSF 语法
```lumerical
createrect(name);                    # 创建矩形，使用默认设置
createrect(name, property, value, ...);  # 创建矩形并设置属性
```

### Python API
```python
session.createrect(name)                     # 创建矩形，使用默认设置
session.createrect(name, property1=value1, property2=value2, ...)  # 创建矩形并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 矩形的名称。 | 是 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 矩形中心的 x 坐标（μm）。 |
| `y` | number | 0 | 矩形中心的 y 坐标（μm）。 |
| `z` | number | 0 | 矩形中心的 z 坐标（μm）。 |
| `x span` | number | 1 | 矩形的 x 方向跨度（宽度，μm）。 |
| `y span` | number | 1 | 矩形的 y 方向跨度（长度，μm）。 |
| `z span` | number | 0.1 | 矩形的 z 方向跨度（高度，厚度，μm）。 |
| `x min` | number | -0.5 | 矩形的 x 最小边界（μm）。 |
| `x max` | number | 0.5 | 矩形的 x 最大边界（μm）。 |
| `y min` | number | -0.5 | 矩形的 y 最小边界（μm）。 |
| `y max` | number | 0.5 | 矩形的 y 最大边界（μm）。 |
| `z min` | number | -0.05 | 矩形的 z 最小边界（μm）。 |
| `z max` | number | 0.05 | 矩形的 z 最大边界（μm）。 |
| `material` | string | "" | 矩形材料的名称。如果为空，则使用全局材料。 |
| `index` | number | 1.0 | 矩形的折射率（如果未指定材料）。 |
| `color` | string | "custom" | 显示颜色（RGB 值或颜色名称）。 |
| `alpha` | number | 1.0 | 透明度（0-1，1 为不透明）。 |
| `visible` | bool | true | 是否可见。 |
| `mesh order` | number | 2 | 网格划分顺序。 |
| `override global mesh settings` | bool | false | 是否覆盖全局网格设置。 |
| `dx`, `dy`, `dz` | number | 0.02 | 各方向的网格步长（μm）。 |
| `grid mesh cells per wavelength` | number | 20 | 每波长网格单元数。 |
| `use relative coordinates` | bool | false | 是否使用相对坐标。 |
| `rotation angle` | number | 0 | 旋转角度（度）。 |
| `rotation axis` | string | "z" | 旋转轴方向。 |

## 使用示例

### 示例 1：创建基本矩形

#### LSF 脚本
```lumerical
// 创建矩形，使用默认设置
createrect("rect1");

// 显示创建的矩形属性
?"创建的矩形属性:";
x = get("rect1", "x");
y = get("rect1", "y");
z = get("rect1", "z");
x_span = get("rect1", "x span");
y_span = get("rect1", "y span");
z_span = get("rect1", "z span");
material = get("rect1", "material");
?"  位置: (" + num2str(x) + ", " + num2str(y) + ", " + num2str(z) + ") μm";
?"  尺寸: " + num2str(x_span) + " × " + num2str(y_span) + " × " + num2str(z_span) + " μm";
?"  材料: " + material;

// 创建自定义矩形
createrect("rect2", 
           "x", 2, "y", 1, "z", 0.5,        # 位置
           "x span", 3, "y span", 2, "z span", 0.22,  # 尺寸
           "material", "Si");           # 硅材料

?"\n自定义矩形 'rect2' 属性:";
x2 = get("rect2", "x");
y2 = get("rect2", "y");
z2 = get("rect2", "z");
x_span2 = get("rect2", "x span");
y_span2 = get("rect2", "y span");
z_span2 = get("rect2", "z span");
material2 = get("rect2", "material");
?"  位置: (" + num2str(x2) + ", " + num2str(y2) + ", " + num2str(z2) + ") μm";
?"  尺寸: " + num2str(x_span2) + " × " + num2str(y_span2) + " × " + num2str(z_span2) + " μm";
?"  材料: " + material2;

// 计算矩形体积
volume = x_span2 * y_span2 * z_span2;
?"  体积: " + num2str(volume, 3) + " μm³";
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建矩形，使用默认设置
fdtd.createrect("rect1")

print("创建的矩形属性:")
rect_props = fdtd.get("rect1")
print(f"  位置: ({rect_props.get('x', '未知')}, {rect_props.get('y', '未知')}, {rect_props.get('z', '未知')}) μm")
print(f"  尺寸: {rect_props.get('x span', '未知')} × {rect_props.get('y span', '未知')} × {rect_props.get('z span', '未知')} μm")
print(f"  材料: {rect_props.get('material', '未知')}")

# 创建自定义矩形
fdtd.createrect("rect2", 
                x=2, y=1, z=0.5,        # 位置
                x_span=3, y_span=2, z_span=0.22,  # 尺寸
                material="Si")           # 硅材料

print("\n自定义矩形 'rect2' 属性:")
rect2_props = fdtd.get("rect2")
print(f"  位置: ({rect2_props.get('x', '未知')}, {rect2_props.get('y', '未知')}, {rect2_props.get('z', '未知')}) μm")
print(f"  尺寸: {rect2_props.get('x span', '未知')} × {rect2_props.get('y span', '未知')} × {rect2_props.get('z span', '未知')} μm")
print(f"  材料: {rect2_props.get('material', '未知')}")

# 计算矩形体积
volume = (rect2_props.get('x span', 0) * 
          rect2_props.get('y span', 0) * 
          rect2_props.get('z span', 0))
print(f"  体积: {volume:.3f} μm³")
```

### 示例 2：创建波导结构
```python
import lumapi

fdtd = lumapi.FDTD()

def create_waveguide(name, start_point, length, width=0.5, height=0.22, material="Si"):
    """创建矩形波导"""
    
    x_start, y_start, z_start = start_point
    
    # 创建波导矩形
    fdtd.createrect(name,
                    x=x_start + length/2,  # 中心位置
                    y=y_start,
                    z=z_start,
                    x_span=length,
                    y_span=width,
                    z_span=height,
                    material=material)
    
    return name

def create_waveguide_bend(name, start_point, bend_radius, bend_angle=90, width=0.5, height=0.22, material="Si"):
    """创建弯曲波导（由多个矩形段近似）"""
    
    x_start, y_start, z_start = start_point
    
    # 将弯曲波导近似为多个矩形段
    num_segments = 10
    angle_rad = np.radians(bend_angle)
    
    segments = []
    
    for i in range(num_segments):
        # 计算当前角度
        angle_start = i * angle_rad / num_segments
        angle_end = (i + 1) * angle_rad / num_segments
        
        # 计算弧长
        arc_length = bend_radius * (angle_end - angle_start)
        
        # 计算段中心位置
        angle_mid = (angle_start + angle_end) / 2
        x_center = x_start + bend_radius * np.sin(angle_mid)
        y_center = y_start + bend_radius * (1 - np.cos(angle_mid))
        
        # 创建矩形段
        segment_name = f"{name}_segment_{i}"
        fdtd.createrect(segment_name,
                        x=x_center,
                        y=y_center,
                        z=z_start,
                        x_span=arc_length,
                        y_span=width,
                        z_span=height,
                        material=material,
                        rotation_angle=np.degrees(angle_mid))
        
        segments.append(segment_name)
    
    return segments

print("创建波导结构...")

# 创建直波导
straight_wg = create_waveguide("straight_waveguide",
                               start_point=(0, 0, 0),
                               length=20,
                               width=0.5,
                               height=0.22)
print(f"直波导: {straight_wg}")

# 创建弯曲波导
bent_segments = create_waveguide_bend("bent_waveguide",
                                      start_point=(20, 0, 0),
                                      bend_radius=10,
                                      bend_angle=90,
                                      width=0.5,
                                      height=0.22)
print(f"弯曲波导: {len(bent_segments)} 个矩形段")

# 计算波导参数
print(f"\n波导参数:")
print(f"  宽度: 0.5 μm")
print(f"  高度: 0.22 μm")
print(f"  直波导长度: 20 μm")
print(f"  弯曲半径: 10 μm")
print(f"  弯曲角度: 90°")

# 计算弯曲波导长度
bend_length = 10 * np.radians(90)  # R * θ
print(f"  弯曲波导长度: {bend_length:.2f} μm")

# 计算有效折射率估计
# 对于矩形波导，有效折射率介于核心和包层折射率之间
n_core = 3.48  # 硅的折射率
n_clad = 1.44  # SiO2的折射率
# 简化估计：n_eff ≈ n_core - (n_core - n_clad) * (λ/h)^2
lambda0 = 1.55  # 波长，μm
h = 0.22  # 波导高度，μm
n_eff_estimate = n_core - (n_core - n_clad) * (lambda0/h)**2
print(f"  估计有效折射率: {n_eff_estimate:.3f}")

# 计算模式限制因子
confinement_factor = (n_eff_estimate - n_clad) / (n_core - n_clad)
print(f"  模式限制因子: {confinement_factor:.3f}")
```

### 示例 3：创建多层结构
```python
import lumapi

fdtd = lumapi.FDTD()

def create_multilayer_stack(name, base_point, layer_thicknesses, layer_materials, 
                           width=10, length=10):
    """创建多层堆叠结构"""
    
    x_base, y_base, z_base = base_point
    
    layers = []
    z_offset = 0
    
    for i, (thickness, material) in enumerate(zip(layer_thicknesses, layer_materials)):
        # 计算当前层的位置
        z_layer = z_base + z_offset + thickness/2
        
        # 创建层
        layer_name = f"{name}_layer_{i}"
        fdtd.createrect(layer_name,
                        x=x_base,
                        y=y_base,
                        z=z_layer,
                        x_span=width,
                        y_span=length,
                        z_span=thickness,
                        material=material)
        
        layers.append(layer_name)
        
        # 更新 z 偏移
        z_offset += thickness
    
    return layers

print("创建 CMOS 图像传感器多层结构...")

# 定义 CMOS 图像传感器层堆叠
layer_thicknesses = [
    0.5,    # 微透镜层
    0.1,    # 滤色层
    0.05,   # 平坦化层
    0.3,    # 金属布线层
    0.02,   # 钝化层
    0.2,    # 光电二极管层
    0.5,    # 基底
]

layer_materials = [
    "SiO2",    # 微透镜（通常为聚合物，这里用 SiO2 近似）
    "custom",  # 滤色层（自定义材料）
    "SiO2",    # 平坦化层
    "Al",      # 金属布线
    "SiN",     # 钝化层
    "Si",      # 光电二极管
    "Si",      # 基底
]

layers = create_multilayer_stack("cmos_sensor",
                                 base_point=(0, 0, 0),
                                 layer_thicknesses=layer_thicknesses,
                                 layer_materials=layer_materials,
                                 width=5,
                                 length=5)

print(f"创建了 {len(layers)} 层结构")

# 分析多层结构
print(f"\nCMOS 图像传感器层堆叠分析:")
total_thickness = sum(layer_thicknesses)
print(f"  总厚度: {total_thickness} μm")
print(f"  像素尺寸: 5 × 5 μm")

# 计算各层体积和材料占比
print(f"  各层详细信息:")
for i, (layer_name, thickness, material) in enumerate(zip(layers, layer_thicknesses, layer_materials)):
    volume = 5 * 5 * thickness
    percentage = (thickness / total_thickness) * 100
    
    print(f"    第 {i} 层: {layer_name}")
    print(f"      材料: {material}")
    print(f"      厚度: {thickness} μm")
    print(f"      体积: {volume:.2f} μm³")
    print(f"      厚度占比: {percentage:.1f}%")

# 计算光学特性（简化）
print(f"\n光学特性估计:")
# 假设光从顶部入射，计算各层的透射率
# 使用菲涅尔公式简化计算
n_air = 1.0
n_sio2 = 1.44
n_si = 3.48
n_sin = 2.0
n_al = 0.14 + 7.63j  # 铝在可见光波段的复折射率

# 计算界面反射
def fresnel_reflection(n1, n2):
    """计算垂直入射的菲涅尔反射系数"""
    R = ((n1 - n2) / (n1 + n2))**2
    return R

# 计算各界面反射
interfaces = [
    ("空气-SiO2", fresnel_reflection(n_air, n_sio2)),
    ("SiO2-滤色层", fresnel_reflection(n_sio2, 1.5)),  # 假设滤色层 n=1.5
    ("滤色层-SiO2", fresnel_reflection(1.5, n_sio2)),
    ("SiO2-Al", fresnel_reflection(n_sio2, n_al.real)),
    ("Al-SiN", fresnel_reflection(n_al.real, n_sin)),
    ("SiN-Si", fresnel_reflection(n_sin, n_si)),
]

print(f"  各界面反射率:")
for interface_name, R in interfaces:
    print(f"    {interface_name}: {R:.4f}")

# 计算总透射率（简化，忽略多次反射）
total_transmission = 1
for _, R in interfaces:
    total_transmission *= (1 - R)

print(f"  估计总透射率: {total_transmission:.4f} ({total_transmission*100:.1f}%)")
```

### 示例 4：创建像素阵列
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_pixel_array(name, rows, cols, pixel_size, pitch, height=0.1, material="Si"):
    """创建像素阵列"""
    
    pixels = []
    
    for i in range(rows):
        for j in range(cols):
            # 计算像素位置
            x = (j - (cols-1)/2) * pitch
            y = (i - (rows-1)/2) * pitch
            
            # 创建像素矩形
            pixel_name = f"{name}_pixel_{i}_{j}"
            fdtd.createrect(pixel_name,
                            x=x, y=y, z=0,
                            x_span=pixel_size,
                            y_span=pixel_size,
                            z_span=height,
                            material=material)
            
            # 根据位置设置颜色（用于可视化）
            red = i / (rows-1) if rows > 1 else 0.5
            green = j / (cols-1) if cols > 1 else 0.5
            blue = 0.5
            fdtd.set(pixel_name, "color", (red, green, blue))
            
            pixels.append(pixel_name)
    
    return pixels

print("创建 8x8 像素阵列...")
pixels = create_pixel_array("sensor_array",
                           rows=8,
                           cols=8,
                           pixel_size=1.0,
                           pitch=1.2,
                           height=0.22)

print(f"创建了 {len(pixels)} 个像素")

# 计算阵列参数
print(f"\n像素阵列参数:")
print(f"  像素尺寸: 1.0 × 1.0 × 0.22 μm")
print(f"  像素间距: 1.2 μm")
print(f"  填充因子: {(1.0/1.2)**2:.3f} ({((1.0/1.2)**2*100):.1f}%)")
print(f"  阵列尺寸: {8*1.2 - 0.2:.1f} × {8*1.2 - 0.2:.1f} μm")

# 计算分辨率（像素数）
resolution = 8 * 8
print(f"  分辨率: {resolution} 像素 ({8}×{8})")

# 计算 Nyquist 频率
# f_nyquist = 1/(2*pixel_pitch) cycles/μm
f_nyquist = 1 / (2 * 1.2)  # cycles/μm
print(f"  Nyquist 频率: {f_nyquist:.3f} cycles/μm")

# 计算最大可分辨空间频率（光学系统）
# 对于衍射限制系统，最大空间频率 f_max = NA/λ
NA = 0.5  # 数值孔径假设
lambda0 = 0.55  # 可见光中心波长，μm
f_max = NA / lambda0
print(f"  光学衍射极限最大频率: {f_max:.3f} cycles/μm")

# 比较像素阵列和光学极限
if f_nyquist > f_max:
    print(f"  像素阵列采样足够（f_nyquist > f_max）")
else:
    print(f"  警告: 像素阵列采样可能不足（f_nyquist < f_max）")

# 创建微透镜阵列（在像素上方）
print(f"\n添加微透镜阵列...")
for i, pixel in enumerate(pixels[:4]):  # 仅为前4个像素添加微透镜（示例）
    props = fdtd.get(pixel)
    x, y, z = props.get('x', 0), props.get('y', 0), props.get('z', 0)
    
    lens_name = f"{pixel}_lens"
    fdtd.addsphere(lens_name,
                   x=x, y=y, z=z+0.22,
                   radius=0.6,
                   material="SiO2")
    
    print(f"  为 {pixel} 添加微透镜")

# 计算聚光效率提升
# 微透镜可以将光聚焦到像素上，提高聚光效率
lens_NA = 0.3  # 微透镜数值孔径
efficiency_gain = 1 / (np.sin(np.arcsin(NA))**2)  # 简化估计
print(f"  微透镜聚光效率提升估计: {efficiency_gain:.2f} 倍")
```

### 示例 5：高级矩形设计工具
```python
import lumapi
import numpy as np

class RectangleDesigner:
    """高级矩形设计工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_tapered_rect(self, name, start_point, end_point, start_width, end_width, 
                           height=0.1, material="Si"):
        """创建锥形矩形（宽度线性变化）"""
        
        x1, y1, z1 = start_point
        x2, y2, z2 = end_point
        
        # 计算中心线方向
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        
        if length == 0:
            print("错误: 起点和终点相同")
            return None
        
        # 单位方向向量
        ux = dx / length
        uy = dy / length
        
        # 垂直方向向量
        vx = -uy
        vy = ux
        
        # 将锥形矩形分解为多个小矩形
        num_segments = 10
        rectangles = []
        
        for i in range(num_segments):
            # 计算当前段的位置
            t_start = i / num_segments
            t_end = (i + 1) / num_segments
            
            # 当前段的宽度
            width_start = start_width + (end_width - start_width) * t_start
            width_end = start_width + (end_width - start_width) * t_end
            width_avg = (width_start + width_end) / 2
            
            # 当前段中心位置
            t_center = (t_start + t_end) / 2
            x_center = x1 + dx * t_center
            y_center = y1 + dy * t_center
            z_center = (z1 + z2) / 2
            
            # 段长度
            segment_length = length / num_segments
            
            # 创建矩形段
            segment_name = f"{name}_segment_{i}"
            self.session.createrect(segment_name,
                                    x=x_center,
                                    y=y_center,
                                    z=z_center,
                                    x_span=segment_length,
                                    y_span=width_avg,
                                    z_span=height,
                                    material=material,
                                    rotation_angle=np.degrees(np.arctan2(dy, dx)))
            
            rectangles.append(segment_name)
        
        return rectangles
    
    def create_interdigitated_electrodes(self, name, center, num_fingers, finger_length, 
                                        finger_width, gap, height=0.1, material="Au"):
        """创建交错式电极"""
        
        cx, cy, cz = center
        
        electrodes = []
        
        # 创建两组交错电极
        for group in [0, 1]:
            for i in range(num_fingers):
                # 计算电极位置
                x_offset = i * (finger_width + gap) * 2 + group * (finger_width + gap)
                
                # 创建电极矩形
                electrode_name = f"{name}_electrode_{group}_{i}"
                self.session.createrect(electrode_name,
                                        x=cx + x_offset,
                                        y=cy,
                                        z=cz,
                                        x_span=finger_width,
                                        y_span=finger_length,
                                        z_span=height,
                                        material=material)
                
                # 设置颜色：第一组红色，第二组蓝色
                color = (1.0, 0.2, 0.2) if group == 0 else (0.2, 0.2, 1.0)
                self.session.set(electrode_name, "color", color)
                
                electrodes.append(electrode_name)
        
        return electrodes
    
    def create_rectangular_spiral(self, name, center, num_turns, turn_spacing, line_width, 
                                 height=0.1, material="Al"):
        """创建矩形螺旋（电感器）"""
        
        cx, cy, cz = center
        
        segments = []
        current_x, current_y = cx, cy
        
        # 螺旋参数
        direction = 1  # 1: 向右，-1: 向左
        current_length = turn_spacing
        
        for turn in range(num_turns):
            # 四条边
            sides = [
                (current_length, 0),      # 右
                (0, current_length),      # 上
                (-current_length, 0),     # 左
                (0, -current_length),     # 下
            ]
            
            for dx, dy in sides:
                # 计算段中心
                segment_center_x = current_x + dx/2
                segment_center_y = current_y + dy/2
                
                # 创建矩形段
                segment_name = f"{name}_turn{turn}_{len(segments)}"
                self.session.createrect(segment_name,
                                        x=segment_center_x,
                                        y=segment_center_y,
                                        z=cz,
                                        x_span=abs(dx) if dx != 0 else line_width,
                                        y_span=abs(dy) if dy != 0 else line_width,
                                        z_span=height,
                                        material=material)
                
                # 旋转角度
                if dx == 0:  # 垂直段
                    pass  # 不需要旋转
                else:  # 水平段
                    self.session.set(segment_name, "rotation_angle", 0)
                
                segments.append(segment_name)
                
                # 更新当前位置
                current_x += dx
                current_y += dy
            
            # 为下一圈增加长度
            current_length += turn_spacing * 2
        
        return segments
    
    def analyze_rectangle_properties(self, rect_name):
        """分析矩形的几何和电气属性"""
        
        props = self.session.get(rect_name)
        
        x_span = props.get('x span', 0)
        y_span = props.get('y span', 0)
        z_span = props.get('z span', 0)
        material = props.get('material', '')
        
        # 几何属性
        area = x_span * y_span
        volume = area * z_span
        aspect_ratio = max(x_span, y_span) / min(x_span, y_span) if min(x_span, y_span) > 0 else 0
        
        # 电气属性（如果材料是导体）
        conductive_materials = ["Au", "Al", "Cu", "Ag", "Pt"]
        is_conductor = material in conductive_materials
        
        resistance = 0
        capacitance = 0
        inductance = 0
        
        if is_conductor:
            # 电阻 R = ρ * L / (w * t)
            # 需要材料电阻率数据（简化处理）
            resistivity = {
                "Au": 2.44e-8,  # Ω·m
                "Al": 2.82e-8,
                "Cu": 1.68e-8,
                "Ag": 1.59e-8,
                "Pt": 1.06e-7,
            }.get(material, 1e-7)
            
            # 单位转换：Ω·m 到 Ω·μm
            resistivity_um = resistivity * 1e12
            
            # 假设电流沿最长方向流动
            length = max(x_span, y_span)
            width = min(x_span, y_span)
            thickness = z_span
            
            resistance = resistivity_um * length / (width * thickness)
            
            # 电容（简化，与理想导体平面相关）
            # C = ε₀εᵣ * area / d
            epsilon_0 = 8.854e-12 * 1e12  # F/μm
            epsilon_r = 3.9  # SiO2的相对介电常数
            distance_to_ground = 1.0  # 到地平面距离，μm（假设）
            
            capacitance = epsilon_0 * epsilon_r * area / distance_to_ground
        
        return {
            'name': rect_name,
            'dimensions': (x_span, y_span, z_span),
            'area': area,
            'volume': volume,
            'aspect_ratio': aspect_ratio,
            'material': material,
            'is_conductor': is_conductor,
            'resistance_ohms': resistance,
            'capacitance_farads': capacitance,
            'resistance_kohms': resistance / 1000 if resistance > 0 else 0,
            'capacitance_ff': capacitance * 1e15 if capacitance > 0 else 0,
        }

# 使用示例
fdtd = lumapi.FDTD()
designer = RectangleDesigner(fdtd)

print("示例1: 创建锥形矩形")
tapered_segments = designer.create_tapered_rect("tapered_waveguide",
                                                start_point=(0, 0, 0),
                                                end_point=(20, 0, 0),
                                                start_width=1.0,
                                                end_width=0.2,
                                                height=0.22,
                                                material="Si")
print(f"锥形矩形由 {len(tapered_segments)} 个段组成")

print("\n示例2: 创建交错式电极")
electrodes = designer.create_interdigitated_electrodes("interdigitated",
                                                      center=(0, 10, 0),
                                                      num_fingers=5,
                                                      finger_length=20,
                                                      finger_width=1,
                                                      gap=1,
                                                      height=0.1,
                                                      material="Au")
print(f"交错式电极: {len(electrodes)} 个电极")

print("\n示例3: 创建矩形螺旋电感器")
spiral_segments = designer.create_rectangular_spiral("spiral_inductor",
                                                    center=(0, -10, 0),
                                                    num_turns=3,
                                                    turn_spacing=2,
                                                    line_width=0.5,
                                                    height=0.1,
                                                    material="Al")
print(f"矩形螺旋: {len(spiral_segments)} 个段")

print("\n示例4: 分析矩形属性")
rectangles_to_analyze = tapered_segments[:1] + electrodes[:1] + spiral_segments[:1]

for rect_name in rectangles_to_analyze:
    try:
        analysis = designer.analyze_rectangle_properties(rect_name)
        print(f"\n{rect_name} 分析:")
        print(f"  尺寸: {analysis['dimensions'][0]:.2f} × {analysis['dimensions'][1]:.2f} × {analysis['dimensions'][2]:.2f} μm")
        print(f"  面积: {analysis['area']:.2f} μm²")
        print(f"  体积: {analysis['volume']:.2f} μm³")
        print(f"  纵横比: {analysis['aspect_ratio']:.2f}")
        print(f"  材料: {analysis['material']}")
        
        if analysis['is_conductor']:
            print(f"  电阻: {analysis['resistance_kohms']:.2f} kΩ")
            print(f"  电容: {analysis['capacitance_ff']:.2f} fF")
        else:
            print(f"  绝缘体")
    except Exception as e:
        print(f"  无法分析 {rect_name}: {e}")

# 计算螺旋电感器的电感（简化）
print(f"\n螺旋电感器参数估计:")
# 简化公式：L ≈ μ₀ * N² * d_avg * c1 * ln(c2/ρ)
# 其中 N 是圈数，d_avg 是平均直径，ρ 是填充因子
mu0 = 4 * np.pi * 1e-7 * 1e6  # H/μm
N = 3
d_avg = 5  # 平均直径，μm
rho = 0.7  # 填充因子
c1, c2 = 1.27, 2.07  # 经验常数

L_estimate = mu0 * N**2 * d_avg * c1 * np.log(c2/rho)
print(f"  估计电感: {L_estimate:.2e} H")
print(f"  估计电感: {L_estimate * 1e9:.2f} nH")

# 计算谐振频率（与寄生电容）
if analysis['capacitance_farads'] > 0:
    f_resonant = 1 / (2 * np.pi * np.sqrt(L_estimate * analysis['capacitance_farads']))
    print(f"  估计自谐振频率: {f_resonant:.2e} Hz")
    print(f"  估计自谐振频率: {f_resonant/1e9:.2f} GHz")
```

## 返回值

`createrect` 命令创建矩形对象，在 Python API 中返回创建的对象名称。在 LSF 中，该命令不直接返回值，但可以通过后续命令访问创建的矩形。

## 错误处理

使用 `createrect` 命令时可能遇到的常见错误及其解决方案：

### 1. 无效的名称参数
- **错误信息**: "Invalid object name"
- **原因**: 名称参数包含无效字符或为空
- **解决方案**: 使用有效的对象名称，避免特殊字符和空格

### 2. 尺寸参数无效
- **错误信息**: "Invalid span value"
- **原因**: 跨度参数为负数或零
- **解决方案**: 确保 `x span`、`y span`、`z span` 为正值

### 3. 材料未定义
- **错误信息**: "Material not found"
- **原因**: 指定的材料名称不存在于材料数据库中
- **解决方案**: 先定义材料或使用 `index` 属性直接指定折射率

### 4. 坐标超出仿真区域
- **错误信息**: "Object outside simulation region"
- **原因**: 矩形位置或尺寸超出仿真区域边界
- **解决方案**: 调整矩形位置/尺寸或扩大仿真区域

### 5. 网格设置冲突
- **错误信息**: "Mesh settings conflict"
- **原因**: 局部网格设置与全局设置冲突
- **解决方案**: 检查 `dx`、`dy`、`dz` 值，确保与仿真网格兼容

### 6. Python API 参数错误
- **错误信息**: "TypeError" 或 "ValueError"
- **原因**: 参数类型不正确或值超出范围
- **解决方案**: 验证参数类型和取值范围

## 注意事项

1. **尺寸单位**：所有尺寸参数的单位是微米（μm）。确保输入正确的单位值。

2. **边界定义**：矩形可以通过中心点和跨度（`x span`、`y span`、`z span`）定义，也可以通过最小/最大边界（`x min`、`x max` 等）定义。两种方法等效，修改一种会自动更新另一种。

3. **材料定义**：确保指定的材料已在材料数据库中定义，或使用 `index` 属性直接指定折射率。

4. **网格划分**：对于薄矩形（小 `z span`）或细长矩形（大纵横比），可能需要调整网格设置以确保计算精度。

5. **性能考虑**：大量小矩形可能会增加网格复杂度和仿真时间。考虑使用参数化形状或简化模型。

6. **与 `addrect` 的区别**：`createrect` 和 `addrect` 功能相似，但可能有细微的语法或默认值差异。在 Lumerical 脚本中，两者通常可以互换使用。

7. **旋转**：矩形可以绕指定轴旋转。旋转中心是矩形的中心点。

8. **布尔运算**：矩形可以与其他几何结构进行布尔运算，用于创建复杂的形状。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于创建波导、器件等 |
| MODE Solutions | ✅ 完全支持 | 用于创建波导和耦合器 |
| DEVICE | ✅ 完全支持 | 用于创建电极和结构 |
| INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用不同的几何系统 |

## 相关命令

- `addrect` - 添加矩形（功能相似）
- `createcircle` - 创建圆形
- `createpoly` - 创建多边形
- `createline` - 创建线
- `set` - 设置矩形属性
- `get` - 获取矩形属性
- `copy` - 复制矩形

## 参考

1. Lumerical FDTD User Guide - Geometry Creation
2. Lumerical Script Language Reference - createrect command
3. Photonic Integrated Circuit Design - Waveguide Fundamentals

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含矩形创建和高级示例 |
| 1.1 | 2026-01-31 | 添加返回值、错误处理章节，补充LSF示例 |

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*