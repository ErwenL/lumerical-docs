# `createdisk` - 创建磁盘

## 概述

`createdisk` 命令用于在仿真中创建三维磁盘（圆盘）结构。磁盘是圆柱体的特殊情况，具有有限的厚度，常用于创建微盘谐振器、透镜、光学隔离器、存储介质等光学和光子学元件。与 `createcircle` 创建的二维圆形不同，`createdisk` 创建的是具有厚度的三维结构。

该命令允许用户指定磁盘的位置、半径、厚度、材料等属性，是创建旋转对称三维结构的基本工具。

## 语法

### LSF 语法
```lumerical
createdisk(name);                    # 创建磁盘，使用默认设置
createdisk(name, property, value, ...);  # 创建磁盘并设置属性
```

### Python API
```python
session.createdisk(name)                     # 创建磁盘，使用默认设置
session.createdisk(name, property1=value1, property2=value2, ...)  # 创建磁盘并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 磁盘的名称。 | 是 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 磁盘中心的 x 坐标（μm）。 |
| `y` | number | 0 | 磁盘中心的 y 坐标（μm）。 |
| `z` | number | 0 | 磁盘中心的 z 坐标（μm）。 |
| `radius` | number | 0.5 | 磁盘的半径（μm）。 |
| `height` | number | 0.1 | 磁盘的高度（厚度，μm）。 |
| `x span` | number | 1 | 磁盘的 x 方向跨度（直径，μm）。 |
| `y span` | number | 1 | 磁盘的 y 方向跨度（直径，μm）。 |
| `z span` | number | 0.1 | 磁盘的 z 方向跨度（高度，μm）。 |
| `axis` | string | "z" | 磁盘的轴方向（"x"、"y" 或 "z"）。 |
| `material` | string | "" | 磁盘材料的名称。如果为空，则使用全局材料。 |
| `index` | number | 1.0 | 磁盘的折射率（如果未指定材料）。 |
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

## 返回值

`createdisk` 命令没有返回值。成功执行后，会在仿真中创建一个磁盘对象。

## 示例

### 示例 1：创建基本磁盘
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建磁盘，使用默认设置
fdtd.createdisk("disk1")

print("创建的磁盘属性:")
disk_props = fdtd.get("disk1")
print(f"  位置: ({disk_props.get('x', '未知')}, {disk_props.get('y', '未知')}, {disk_props.get('z', '未知')}) μm")
print(f"  半径: {disk_props.get('radius', '未知')} μm")
print(f"  高度: {disk_props.get('height', disk_props.get('z span', '未知'))} μm")
print(f"  材料: {disk_props.get('material', '未知')}")

# 创建自定义磁盘
fdtd.createdisk("disk2", 
                x=2, y=1, z=0.5,      # 位置
                radius=1.0,            # 半径 1.0 μm
                height=0.22,           # 高度 0.22 μm
                material="Si",         # 硅材料
                axis="z")              # 沿 z 轴方向

print("\n自定义磁盘属性:")
disk2_props = fdtd.get("disk2")
print(f"  位置: ({disk2_props.get('x', '未知')}, {disk2_props.get('y', '未知')}, {disk2_props.get('z', '未知')}) μm")
print(f"  半径: {disk2_props.get('radius', '未知')} μm")
print(f"  高度: {disk2_props.get('height', disk2_props.get('z span', '未知'))} μm")
print(f"  材料: {disk2_props.get('material', '未知')}")
print(f"  轴方向: {disk2_props.get('axis', '未知')}")

# 计算磁盘体积
radius = disk2_props.get("radius", 0)
height = disk2_props.get("height", disk2_props.get("z span", 0))
volume = 3.14159 * radius**2 * height
print(f"  体积: {volume:.4f} μm³")
```

### 示例 2：创建微盘谐振器
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_microdisk_resonator(name, radius=5, thickness=0.22, gap=0.2, material="Si"):
    """创建微盘谐振器结构"""
    
    # 创建微盘
    fdtd.createdisk(f"{name}_disk",
                    x=0, y=0, z=0,
                    radius=radius,
                    height=thickness,
                    material=material,
                    axis="z")
    
    # 创建输入波导（矩形波导）
    fdtd.addrect(f"{name}_input_wg",
                 x=-(radius + gap + 0.25),  # 位置：左侧，留出间隙
                 y=0, z=0,
                 x_span=0.5,                # 波导宽度 0.5 μm
                 y_span=radius*2,           # 波导长度
                 z_span=thickness,          # 与磁盘相同厚度
                 material=material)
    
    # 创建输出波导
    fdtd.addrect(f"{name}_output_wg",
                 x=radius + gap + 0.25,     # 位置：右侧
                 y=0, z=0,
                 x_span=0.5,
                 y_span=radius*2,
                 z_span=thickness,
                 material=material)
    
    # 调整波导位置，形成侧向耦合
    fdtd.set(f"{name}_input_wg", "y span", radius*1.5)  # 缩短波导
    fdtd.set(f"{name}_output_wg", "y span", radius*1.5)
    
    return [f"{name}_disk", f"{name}_input_wg", f"{name}_output_wg"]

print("创建微盘谐振器...")
resonator_parts = create_microdisk_resonator("microdisk1", radius=5, thickness=0.22, gap=0.2)

print(f"创建的部件: {resonator_parts}")

# 计算谐振器参数
disk_radius = fdtd.get("microdisk1_disk").get("radius", 0)
disk_thickness = fdtd.get("microdisk1_disk").get("height", 0)
gap = 0.2

print(f"\n微盘谐振器参数:")
print(f"  磁盘半径: {disk_radius} μm")
print(f"  磁盘厚度: {disk_thickness} μm")
print(f"  波导-磁盘间隙: {gap} μm")

# 计算 Whispering Gallery 模式的理论谐振波长
# 近似公式: mλ ≈ 2πR * n_eff / m，其中 m 是角模式数
n_eff = 2.5  # 近似有效折射率
for m in range(10, 15):
    wavelength = 2 * np.pi * disk_radius * n_eff / m
    if 1.3 <= wavelength <= 1.7:  # 通信波段
        print(f"  模式 m={m}: 谐振波长 ~{wavelength:.3f} μm")

# 计算品质因子估计
# Q = λ/Δλ ≈ (2πR/λ) * n_eff * (1 - loss)
loss = 0.01  # 1% 损耗
Q_estimate = (2 * np.pi * disk_radius / 1.55) * n_eff * (1 - loss)
print(f"  估计品质因子 Q @1.55μm: ~{Q_estimate:.0f}")
```

### 示例 3：创建多层磁盘结构
```python
import lumapi

fdtd = lumapi.FDTD()

def create_multilayer_disk(name, center, radii, heights, materials):
    """创建多层磁盘（类似光学涂层或分布式布拉格反射器）"""
    
    disks = []
    z_offset = 0
    
    for i, (radius, height, material) in enumerate(zip(radii, heights, materials)):
        # 计算每层的位置（沿 z 轴堆叠）
        z_pos = center[2] + z_offset + height/2
        
        # 创建磁盘层
        disk_name = f"{name}_layer_{i}"
        fdtd.createdisk(disk_name,
                        x=center[0], y=center[1], z=z_pos,
                        radius=radius,
                        height=height,
                        material=material,
                        axis="z")
        
        disks.append(disk_name)
        
        # 更新 z 偏移用于下一层
        z_offset += height
    
    return disks

print("创建多层磁盘结构（抗反射涂层示例）...")

# 定义层参数：半径递减，模拟锥形结构
center = (0, 0, 0)
radii = [2.0, 1.8, 1.6, 1.4, 1.2]  # μm
heights = [0.1, 0.1, 0.1, 0.1, 0.1]  # μm
materials = ["Si", "SiO2", "SiN", "SiO2", "Air"]  # 材料交替

layers = create_multilayer_disk("AR_coating", center, radii, heights, materials)

print(f"创建的层数: {len(layers)}")

# 分析多层结构
print("\n多层磁盘结构分析:")
total_height = sum(heights)
print(f"  总高度: {total_height} μm")
print(f"  最大半径: {radii[0]} μm")
print(f"  最小半径: {radii[-1]} μm")
print(f"  锥角: {np.degrees(np.arctan((radii[0]-radii[-1])/total_height)):.2f}°")

# 计算每层的体积和材料占比
total_volume = 0
material_volumes = {}

for i, disk in enumerate(layers):
    props = fdtd.get(disk)
    radius = props.get("radius", 0)
    height = props.get("height", props.get("z span", 0))
    material = props.get("material", "未知")
    
    volume = np.pi * radius**2 * height
    total_volume += volume
    
    if material not in material_volumes:
        material_volumes[material] = 0
    material_volumes[material] += volume
    
    print(f"\n  第 {i} 层 ({disk}):")
    print(f"    半径: {radius} μm")
    print(f"    高度: {height} μm")
    print(f"    材料: {material}")
    print(f"    体积: {volume:.4f} μm³")

print(f"\n总体积: {total_volume:.4f} μm³")
print("材料体积分布:")
for material, volume in material_volumes.items():
    percentage = (volume / total_volume) * 100
    print(f"  {material}: {volume:.4f} μm³ ({percentage:.1f}%)")
```

### 示例 4：创建磁盘阵列（微透镜阵列）
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_disk_array(name, rows=4, cols=4, pitch=3, radius=1.0, height=0.5, material="SiO2"):
    """创建磁盘阵列（如微透镜阵列）"""
    
    disks = []
    
    for i in range(rows):
        for j in range(cols):
            # 计算磁盘位置
            x_pos = (j - (cols-1)/2) * pitch
            y_pos = (i - (rows-1)/2) * pitch
            
            # 创建磁盘
            disk_name = f"{name}_disk_{i}_{j}"
            fdtd.createdisk(disk_name,
                            x=x_pos, y=y_pos, z=0,
                            radius=radius,
                            height=height,
                            material=material,
                            axis="z")
            
            disks.append(disk_name)
    
    return disks

print("创建 4x4 磁盘阵列（微透镜阵列）...")
disks = create_disk_array("microlens", rows=4, cols=4, pitch=3, radius=1.0, height=0.5)

print(f"创建的磁盘数量: {len(disks)}")

# 计算阵列参数
array_width = (4 - 1) * 3 + 2 * 1.0  # 间距*(列数-1) + 2*半径
array_height = (4 - 1) * 3 + 2 * 1.0
print(f"阵列尺寸: {array_width} μm × {array_height} μm")

# 计算填充因子
single_disk_area = np.pi * 1.0**2
total_disk_area = len(disks) * single_disk_area
array_area = array_width * array_height
fill_factor = total_disk_area / array_area
print(f"填充因子: {fill_factor:.2%}")

# 计算焦距估计（薄透镜公式）
# 对于球形透镜：f = R/(n-1)，这里近似处理
n_sio2 = 1.45  # SiO2 折射率
focal_length = 1.0 / (n_sio2 - 1)  # 近似焦距
print(f"单个透镜近似焦距: {focal_length:.2f} μm")

# 为阵列添加基板
fdtd.addrect("microlens_substrate",
             x=0, y=0, z=-0.25,  # 在磁盘下方
             x_span=array_width + 2,  # 稍大于阵列
             y_span=array_height + 2,
             z_span=0.5,
             material="SiO2")

print(f"\n添加基板: microlens_substrate")

# 验证结构
print("\n所有磁盘对象:")
fdtd.eval("?disk;")

print("\n所有矩形对象:")
fdtd.eval("?rect;")
```

### 示例 5：高级磁盘设计工具
```python
import lumapi
import numpy as np

class DiskDesigner:
    """高级磁盘设计工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_elliptical_disk(self, name, center, radius_x, radius_y, height, material="Si"):
        """创建椭圆形磁盘（通过组合和变形）"""
        
        # 创建圆形磁盘
        self.session.createdisk(f"{name}_base",
                                x=center[0], y=center[1], z=center[2],
                                radius=max(radius_x, radius_y),
                                height=height,
                                material=material)
        
        # 通过缩放创建椭圆
        # 注意：Lumerical 可能需要使用不同的方法创建椭圆
        # 这里使用近似方法：创建多个扇形组合
        
        # 实际应用中可能需要使用脚本创建椭圆
        print(f"注意: Lumerical 的 createdisk 命令创建的是圆形磁盘。")
        print(f"要创建椭圆磁盘，可以使用多个扇形组合或使用其他建模方法。")
        
        return f"{name}_base"
    
    def create_tapered_disk(self, name, center, base_radius, top_radius, height, material="Si"):
        """创建锥形磁盘（截锥体）"""
        
        # 创建底部磁盘
        bottom_name = f"{name}_bottom"
        self.session.createdisk(bottom_name,
                                x=center[0], y=center[1], z=center[2],
                                radius=base_radius,
                                height=height/2,
                                material=material)
        
        # 创建顶部磁盘（较小半径）
        top_name = f"{name}_top"
        self.session.createdisk(top_name,
                                x=center[0], y=center[1], z=center[2] + height/4,
                                radius=top_radius,
                                height=height/2,
                                material=material)
        
        return bottom_name, top_name
    
    def create_disk_with_hole(self, name, center, outer_radius, inner_radius, height, material="Si"):
        """创建带孔的磁盘（环形磁盘）"""
        
        # 创建外磁盘
        outer_name = f"{name}_outer"
        self.session.createdisk(outer_name,
                                x=center[0], y=center[1], z=center[2],
                                radius=outer_radius,
                                height=height,
                                material=material)
        
        # 创建内磁盘（孔）
        inner_name = f"{name}_inner"
        self.session.createdisk(inner_name,
                                x=center[0], y=center[1], z=center[2],
                                radius=inner_radius,
                                height=height * 1.1,  # 稍高以确保完全穿透
                                material="Air")  # 空气形成孔
        
        return outer_name, inner_name
    
    def analyze_disk_modes(self, disk_name, wavelength=1.55, n_eff_guess=2.0):
        """分析磁盘的 Whispering Gallery 模式"""
        
        props = self.session.get(disk_name)
        radius = props.get("radius", 0)
        height = props.get("height", props.get("z span", 0))
        material = props.get("material", "")
        
        # 简化模式分析
        # 对于 Whispering Gallery 模式，谐振条件：2πR * n_eff = mλ
        
        print(f"\n磁盘模式分析: {disk_name}")
        print(f"  半径: {radius} μm")
        print(f"  厚度: {height} μm")
        print(f"  材料: {material}")
        
        # 计算模式数范围
        m_min = int(2 * np.pi * radius * n_eff_guess / (wavelength * 1.2))  # 较长波长
        m_max = int(2 * np.pi * radius * n_eff_guess / (wavelength * 0.8))  # 较短波长
        
        print(f"\n在 {wavelength} μm 附近的谐振模式 (m 为角模式数):")
        
        modes = []
        for m in range(m_min, m_max + 1):
            resonant_wavelength = 2 * np.pi * radius * n_eff_guess / m
            if 1.2 <= resonant_wavelength <= 1.7:  # 通信波段
                modes.append((m, resonant_wavelength))
                print(f"  模式 m={m}: λ={resonant_wavelength:.4f} μm")
        
        # 计算模式间距（FSR）
        if len(modes) >= 2:
            m1, λ1 = modes[0]
            m2, λ2 = modes[1]
            fsr = abs(λ1 - λ2)
            print(f"\n自由光谱范围 (FSR): {fsr:.4f} μm ({fsr*1000:.2f} nm)")
            
            # 计算精细度 F = FSR / Δλ (假设 Δλ = 0.1 nm)
            delta_lambda = 0.0001  # 0.1 nm
            finesse = fsr / delta_lambda
            print(f"  精细度 (Δλ={delta_lambda*1000:.1f} nm): {finesse:.0f}")
        
        return modes
    
    def calculate_disk_properties(self, disk_name):
        """计算磁盘的几何和光学属性"""
        
        props = self.session.get(disk_name)
        
        radius = props.get("radius", 0)
        height = props.get("height", props.get("z span", 0))
        material = props.get("material", "")
        
        # 几何属性
        diameter = 2 * radius
        area = np.pi * radius**2
        volume = area * height
        lateral_area = 2 * np.pi * radius * height  # 侧面积
        total_area = 2 * area + lateral_area  # 总表面积
        
        # 光学属性（简化）
        # 实际中需要材料数据库
        if material == "Si":
            n = 3.48  # 硅在 1.55 μm 的折射率
        elif material == "SiO2":
            n = 1.44
        elif material == "SiN":
            n = 2.0
        else:
            n = 1.5  # 默认
        
        return {
            'name': disk_name,
            'radius': radius,
            'diameter': diameter,
            'height': height,
            'material': material,
            'refractive_index': n,
            'area': area,
            'volume': volume,
            'surface_area': total_area,
            'aspect_ratio': height / diameter
        }

# 使用示例
fdtd = lumapi.FDTD()
designer = DiskDesigner(fdtd)

print("示例1: 创建锥形磁盘")
bottom, top = designer.create_tapered_disk("tapered_disk", 
                                           center=(0, 0, 0), 
                                           base_radius=2.0, 
                                           top_radius=1.0, 
                                           height=1.0)
print(f"锥形磁盘: {bottom}, {top}")

print("\n示例2: 创建环形磁盘")
outer, inner = designer.create_disk_with_hole("annular_disk",
                                              center=(5, 0, 0),
                                              outer_radius=2.0,
                                              inner_radius=1.0,
                                              height=0.22)
print(f"环形磁盘: {outer}, {inner}")

print("\n示例3: 分析磁盘模式")
# 先创建一个测试磁盘
fdtd.createdisk("test_disk", radius=5, height=0.22, material="Si")
modes = designer.analyze_disk_modes("test_disk", wavelength=1.55, n_eff_guess=2.5)

print("\n示例4: 计算磁盘属性")
properties = designer.calculate_disk_properties("test_disk")
print(f"\n磁盘属性分析:")
for key, value in properties.items():
    print(f"  {key}: {value}")
```

## 注意事项

1. **三维结构**：`createdisk` 创建的是三维结构，具有厚度（高度）。这与 `createcircle` 创建的二维圆形不同。

2. **轴方向**：默认情况下，磁盘沿 z 轴方向（`axis="z"`）。可以更改为 "x" 或 "y" 轴以创建垂直方向的磁盘。

3. **网格划分**：磁盘的曲面边界需要精细网格划分以确保计算精度。对于大半径或薄磁盘，可能需要调整网格设置。

4. **材料定义**：确保指定的材料已在材料数据库中定义，或使用 `index` 属性直接指定折射率。

5. **性能考虑**：大量磁盘或复杂磁盘结构可能增加网格复杂度和仿真时间。考虑使用对称性或简化模型。

6. **与 `addcylinder` 的关系**：`createdisk` 创建的磁盘本质上是短圆柱体。对于更一般的圆柱体，可以使用 `addcylinder` 命令。

7. **布尔运算**：磁盘可以与其他几何结构进行布尔运算，用于创建复杂的三维形状。

 8. **可视化**：在 Lumerical 可视化器中，磁盘显示为圆柱体。使用 `color` 和 `alpha` 属性调整外观。

## 错误处理

### 常见错误
1. **半径无效**: `radius` ≤ 0
   - 解决方案：确保 `radius` > 0

2. **高度无效**: `height` ≤ 0 或 `z span` ≤ 0
   - 解决方案：确保 `height` > 0

3. **轴方向无效**: `axis` 不是 "x"、"y" 或 "z"
   - 解决方案：检查 `axis` 属性值，必须是 "x"、"y" 或 "z"

4. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率通过 `index` 属性指定

5. **网格生成失败**: 磁盘尺寸过小或厚度太薄导致网格问题
   - 解决方案：调整磁盘尺寸，确保足够的网格分辨率

6. **名称冲突**: 磁盘名称与现有对象重复
   - 解决方案：使用唯一的名称，或先删除同名对象

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 创建磁盘
    fdtd.createdisk("test_disk", radius=1.0, height=0.22, material="Si")
    
    # 检查参数有效性
    radius = fdtd.get("test_disk").get("radius", 0)
    height = fdtd.get("test_disk").get("height", fdtd.get("test_disk").get("z span", 0))
    
    if radius <= 0:
        raise ValueError("半径必须 > 0")
    if height <= 0:
        raise ValueError("高度必须 > 0")
    
    # 验证轴方向
    axis = fdtd.get("test_disk").get("axis", "z")
    if axis not in ["x", "y", "z"]:
        raise ValueError("轴方向必须是 'x', 'y' 或 'z'")
    
    # 验证材料
    material = fdtd.get("test_disk").get("material", "")
    if material and material not in fdtd.getmaterialnames():
        print(f"警告: 材料 '{material}' 不在数据库中，使用自定义折射率")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    fdtd.set("test_disk", "radius", 0.5)
    fdtd.set("test_disk", "height", 0.1)
    
except Exception as e:
    print(f"磁盘创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "radius" in str(e).lower():
        print("错误: 半径无效，请检查半径值")
    elif "height" in str(e).lower() or "span" in str(e).lower():
        print("错误: 高度无效，请检查高度值")
    elif "axis" in str(e).lower():
        print("错误: 轴方向无效，必须是 'x', 'y' 或 'z'")
    elif "name" in str(e).lower():
        print("错误: 名称冲突，请使用不同的名称")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `createcircle` - 创建二维圆形
- `addcylinder` - 添加圆柱体（更一般）
- `adddisk` - 添加磁盘（功能相似）
- `addsphere` - 添加球体
- `addrect` - 添加矩形
- `set` - 设置磁盘属性
- `get` - 获取磁盘属性
- `copy` - 复制磁盘

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于创建三维磁盘结构 |
| MODE Solutions | ✅ 完全支持 | 用于创建磁盘波导和耦合器 |
| DEVICE | ✅ 完全支持 | 用于创建磁盘电极和器件 |
 | INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用不同的几何系统 |

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `rotation angle` 和 `rotation axis` 属性支持旋转 |
| Lumerical 2019a | 改进磁盘网格生成算法 |
| Lumerical 2018a | 新增 `createdisk` 命令，提供更直观的磁盘创建接口 |
| 1.1 | 更新日期，完善文档格式，添加错误处理和版本历史 |

## 参考

1. Lumerical 几何建模指南
2. Lumerical 三维结构网格生成技术说明
3. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*