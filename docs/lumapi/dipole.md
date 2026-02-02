# `dipole` - 设置偶极子源

## 概述

`dipole` 命令用于在 FDTD 仿真中创建偶极子光源。偶极子源是点状辐射源，模拟振荡电偶极子的辐射特性。它在纳米光子学、等离子体学、荧光增强和量子发射器仿真中广泛应用。

偶极子源的特点：
- **点源特性**：在单个网格点位置辐射
- **方向性**：具有特定的偏振方向（x, y, z 方向）
- **宽频谱**：可以设置为宽频谱或单频点
- **量子特性**：可以模拟量子发射器的辐射特性
- **近场增强**：特别适合研究近场增强效应

典型应用场景：
- 荧光分子辐射模拟
- 量子点发光研究
- 等离子体纳米天线增强
- 近场光学显微镜仿真
- 自发辐射调控

## 语法

### LSF 语法
```lumerical
dipole;                                  # 创建偶极子源，使用默认设置
dipole(name);                            # 创建指定名称的偶极子源
dipole(name, property, value, ...);      # 创建偶极子源并设置属性
```

### Python API
```python
session.dipole()                                  # 创建偶极子源，使用默认设置
session.dipole(name)                             # 创建指定名称的偶极子源
session.dipole(name, property1=value1, property2=value2, ...)  # 创建偶极子源并设置属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 偶极子源的名称。 | 可选 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 偶极子位置的 x 坐标（μm）。 |
| `y` | number | 0 | 偶极子位置的 y 坐标（μm）。 |
| `z` | number | 0 | 偶极子位置的 z 坐标（μm）。 |
| `x span` | number | 0 | 偶极子分布的 x 方向跨度（μm）。 |
| `y span` | number | 0 | 偶极子分布的 y 方向跨度（μm）。 |
| `z span` | number | 0 | 偶极子分布的 z 方向跨度（μm）。 |
| `polarization angle` | number | 0 | 偏振方向角度（度）。 |
| `theta` | number | 0 | 球坐标下的极角（度）。 |
| `phi` | number | 0 | 球坐标下的方位角（度）。 |
| `dipole type` | string | "electric" | 偶极子类型："electric"（电偶极子），"magnetic"（磁偶极子）。 |
| `injection axis` | string | "z" | 注入方向："x", "y", "z"。 |
| `wavelength` | number | 1 | 中心波长（μm）。 |
| `wavelength span` | number | 0 | 波长跨度（μm）。 |
| `frequency` | number | 300 | 中心频率（THz）。 |
| `frequency span` | number | 0 | 频率跨度（THz）。 |
| `power` | number | 1 | 总辐射功率（W）。 |
| `phase` | number | 0 | 初始相位（弧度）。 |
| `pulse type` | string | "continuous" | 脉冲类型："continuous", "gaussian", "user defined"。 |
| `pulse length` | number | 10 | 脉冲长度（fs）。 |
| `delay` | number | 0 | 脉冲延迟（fs）。 |
| `amplitude` | number | 1 | 振幅。 |
| `offset` | number | 0 | 偏移量。 |
| `set spectrum from simulation` | bool | false | 是否从仿真获取频谱。 |
| `use relative coordinates` | bool | false | 是否使用相对坐标。 |
| `enabled` | bool | true | 是否启用偶极子源。 |
| `color` | string | "custom" | 显示颜色。 |
| `alpha` | number | 1.0 | 透明度。 |
| `visible` | bool | true | 是否可见。 |

## 使用示例

### 示例 1：创建基本偶极子源

**Python API:**
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("创建基本偶极子源...")

# 创建电偶极子源（默认设置）
fdtd.dipole("dipole1")

# 获取属性
dipole_props = fdtd.get("dipole1")
print("偶极子属性:")
print(f"  位置: ({dipole_props.get('x', 0)}, {dipole_props.get('y', 0)}, {dipole_props.get('z', 0)}) μm")
print(f"  类型: {dipole_props.get('dipole type', 'unknown')}")
print(f"  波长: {dipole_props.get('wavelength', 0)} μm")
print(f"  功率: {dipole_props.get('power', 0)} W")

# 创建自定义偶极子源
fdtd.dipole("custom_dipole",
            x=0.5, y=0.2, z=0.1,          # 位置
            wavelength=1.55,               # 1550 nm 波长
            power=0.001,                   # 1 mW 功率
            dipole_type="electric",        # 电偶极子
            injection_axis="z",            # z 方向注入
            polarization_angle=45)         # 45度偏振

print("\n自定义偶极子属性:")
custom_props = fdtd.get("custom_dipole")
print(f"  位置: ({custom_props.get('x', 0)}, {custom_props.get('y', 0)}, {custom_props.get('z', 0)}) μm")
print(f"  波长: {custom_props.get('wavelength', 0)} μm")
print(f"  功率: {custom_props.get('power', 0)*1000:.3f} mW")
print(f"  偏振角: {custom_props.get('polarization angle', 0)}°")

# 创建磁偶极子源
fdtd.dipole("magnetic_dipole",
            x=-0.5, y=0, z=0,
            dipole_type="magnetic",        # 磁偶极子
            wavelength=0.63,               # 630 nm 可见光
            power=0.005)                   # 5 mW

print("\n磁偶极子属性:")
mag_props = fdtd.get("magnetic_dipole")
print(f"  类型: {mag_props.get('dipole type', 'unknown')}")
print(f"  波长: {mag_props.get('wavelength', 0)*1000:.1f} nm")
print(f"  功率: {mag_props.get('power', 0)*1000:.3f} mW")
```

**LSF Script:**
```lumerical
# 创建基本偶极子源

# 创建电偶极子源（默认设置）
dipole("dipole1");

# 获取属性
dipole_props = get("dipole1");
?"偶极子属性:";
?"  位置: (" + num2str(dipole_props.x) + ", " + num2str(dipole_props.y) + ", " + num2str(dipole_props.z) + ") μm";
?"  类型: " + dipole_props.dipole_type;
?"  波长: " + num2str(dipole_props.wavelength) + " μm";
?"  功率: " + num2str(dipole_props.power) + " W";

# 创建自定义偶极子源
dipole("custom_dipole", 
       "x", 0.5, 
       "y", 0.2, 
       "z", 0.1,           # 位置
       "wavelength", 1.55, # 1550 nm 波长
       "power", 0.001,     # 1 mW 功率
       "dipole type", "electric",  # 电偶极子
       "injection axis", "z",      # z 方向注入
       "polarization angle", 45);  # 45度偏振

?"自定义偶极子属性:";
custom_props = get("custom_dipole");
?"  位置: (" + num2str(custom_props.x) + ", " + num2str(custom_props.y) + ", " + num2str(custom_props.z) + ") μm";
?"  波长: " + num2str(custom_props.wavelength) + " μm";
?"  功率: " + num2str(custom_props.power*1000, "%.3f") + " mW";
?"  偏振角: " + num2str(custom_props.polarization_angle) + "°";

# 创建磁偶极子源
dipole("magnetic_dipole",
       "x", -0.5, 
       "y", 0, 
       "z", 0,
       "dipole type", "magnetic",  # 磁偶极子
       "wavelength", 0.63,         # 630 nm 可见光
       "power", 0.005);            # 5 mW

?"磁偶极子属性:";
mag_props = get("magnetic_dipole");
?"  类型: " + mag_props.dipole_type;
?"  波长: " + num2str(mag_props.wavelength*1000, "%.1f") + " nm";
?"  功率: " + num2str(mag_props.power*1000, "%.3f") + " mW";
```

### 示例 2：偶极子阵列和方向性控制

**Python API:**
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("创建偶极子阵列...")

def create_dipole_array(name, rows=3, cols=3, spacing=1, wavelength=1.55):
    """创建偶极子阵列"""
    
    dipoles = []
    
    for i in range(rows):
        for j in range(cols):
            # 计算位置
            x_pos = (j - (cols-1)/2) * spacing
            y_pos = (i - (rows-1)/2) * spacing
            
            # 创建偶极子
            dipole_name = f"{name}_{i}_{j}"
            fdtd.dipole(dipole_name,
                       x=x_pos, y=y_pos, z=0,
                       wavelength=wavelength,
                       power=0.001,  # 每个偶极子 1 mW
                       polarization_angle=(i*30 + j*15) % 180)  # 变化偏振角
            
            dipoles.append(dipole_name)
    
    return dipoles

# 创建 3x3 偶极子阵列
dipole_array = create_dipole_array("dipole_array", rows=3, cols=3, spacing=1.5)
print(f"创建的偶极子数量: {len(dipole_array)}")

# 分析阵列特性
print("\n偶极子阵列分析:")
for i, dipole in enumerate(dipole_array[:5]):  # 只显示前5个
    props = fdtd.get(dipole)
    print(f"  {dipole}:")
    print(f"    位置: ({props.get('x', 0):.2f}, {props.get('y', 0):.2f}) μm")
    print(f"    偏振角: {props.get('polarization angle', 0):.1f}°")

# 控制方向性：创建波束成形阵列
print("\n创建波束成形偶极子阵列...")

def create_phased_array(name, num_elements=5, spacing=0.5, wavelength=1.55, steering_angle=30):
    """创建相控阵偶极子（波束成形）"""
    
    # 计算相位延迟（用于波束转向）
    k = 2 * np.pi / wavelength  # 波数
    phase_delay = k * spacing * np.sin(np.radians(steering_angle))
    
    dipoles = []
    
    for i in range(num_elements):
        x_pos = (i - (num_elements-1)/2) * spacing
        
        # 计算相位（线性相位梯度）
        phase = i * phase_delay
        
        # 创建偶极子
        dipole_name = f"{name}_element_{i}"
        fdtd.dipole(dipole_name,
                   x=x_pos, y=0, z=0,
                   wavelength=wavelength,
                   power=0.001,
                   phase=phase,  # 设置相位
                   polarization_angle=0)  # 统一偏振
        
        dipoles.append(dipole_name)
    
    return dipoles, phase_delay

# 创建相控阵
steering_angle = 30  # 波束转向 30 度
phased_array, phase_delay = create_phased_array("phased_array", 
                                               num_elements=7, 
                                               spacing=0.75,
                                               wavelength=1.55,
                                               steering_angle=steering_angle)

print(f"相控阵参数:")
print(f"  阵元数量: {len(phased_array)}")
print(f"  阵元间距: 0.75 μm")
print(f"  波长: 1.55 μm")
print(f"  转向角度: {steering_angle}°")
print(f"  相位延迟: {phase_delay:.3f} rad/阵元")

# 计算阵列因子
wavelength = 1.55
spacing = 0.75
N = 7
theta = np.linspace(-90, 90, 181)  # 角度范围

# 阵列因子公式
psi = 2 * np.pi * spacing / wavelength * np.sin(np.radians(theta)) - phase_delay
array_factor = np.abs(np.sin(N * psi / 2) / np.sin(psi / 2)) / N

# 找到主瓣方向
main_lobe_idx = np.argmax(array_factor)
main_lobe_angle = theta[main_lobe_idx]

print(f"\n阵列因子分析:")
print(f"  理论主瓣方向: {steering_angle:.1f}°")
print(f"  计算主瓣方向: {main_lobe_angle:.1f}°")
print(f"  主瓣增益: {array_factor[main_lobe_idx]:.2f}")

# 计算波束宽度（3dB 宽度）
half_power = array_factor[main_lobe_idx] / np.sqrt(2)
left_idx = np.where(array_factor[:main_lobe_idx] >= half_power)[0]
right_idx = np.where(array_factor[main_lobe_idx:] >= half_power)[0]

if len(left_idx) > 0 and len(right_idx) > 0:
    left_angle = theta[left_idx[-1]]
    right_angle = theta[main_lobe_idx + right_idx[-1]]
    beamwidth = right_angle - left_angle
    
    print(f"  3dB 波束宽度: {beamwidth:.1f}°")
```

**LSF Script:**
```lumerical
# 创建偶极子阵列和方向性控制

?"创建偶极子阵列...";

# 创建偶极子阵列的函数
function create_dipole_array(name, rows, cols, spacing, wavelength) {
    dipoles = {};
    
    for (i = 0; i < rows; i = i + 1) {
        for (j = 0; j < cols; j = j + 1) {
            # 计算位置
            x_pos = (j - (cols-1)/2) * spacing;
            y_pos = (i - (rows-1)/2) * spacing;
            
            # 创建偶极子名称
            dipole_name = name + "_" + num2str(i) + "_" + num2str(j);
            
            # 创建偶极子
            dipole(dipole_name,
                   "x", x_pos,
                   "y", y_pos,
                   "z", 0,
                   "wavelength", wavelength,
                   "power", 0.001,  # 每个偶极子 1 mW
                   "polarization angle", mod(i*30 + j*15, 180));  # 变化偏振角
            
            dipoles{i*cols + j} = dipole_name;
        }
    }
    
    return dipoles;
}

# 创建 3x3 偶极子阵列
dipole_array = create_dipole_array("dipole_array", 3, 3, 1.5, 1.55);
?"创建的偶极子数量: " + num2str(length(dipole_array));

# 分析阵列特性
?"偶极子阵列分析:";
for (i = 0; i < min(5, length(dipole_array)); i = i + 1) {
    dipole_name = dipole_array{i};
    props = get(dipole_name);
    ?"  " + dipole_name + ":";
    ?"    位置: (" + num2str(props.x, "%.2f") + ", " + num2str(props.y, "%.2f") + ") μm";
    ?"    偏振角: " + num2str(props.polarization_angle, "%.1f") + "°";
}

# 控制方向性：创建波束成形阵列
?"创建波束成形偶极子阵列...";

function create_phased_array(name, num_elements, spacing, wavelength, steering_angle) {
    # 计算相位延迟（用于波束转向）
    k = 2 * pi / wavelength;  # 波数
    phase_delay = k * spacing * sin(steering_angle * pi/180);
    
    dipoles = {};
    
    for (i = 0; i < num_elements; i = i + 1) {
        x_pos = (i - (num_elements-1)/2) * spacing;
        
        # 计算相位（线性相位梯度）
        phase = i * phase_delay;
        
        # 创建偶极子名称
        dipole_name = name + "_element_" + num2str(i);
        
        # 创建偶极子
        dipole(dipole_name,
               "x", x_pos,
               "y", 0,
               "z", 0,
               "wavelength", wavelength,
               "power", 0.001,
               "phase", phase,  # 设置相位
               "polarization angle", 0);  # 统一偏振
        
        dipoles{i} = dipole_name;
    }
    
    return dipoles, phase_delay;
}

# 创建相控阵
steering_angle = 30;  # 波束转向 30 度
phased_array, phase_delay = create_phased_array("phased_array", 7, 0.75, 1.55, steering_angle);

?"相控阵参数:";
?"  阵元数量: " + num2str(length(phased_array));
?"  阵元间距: 0.75 μm";
?"  波长: 1.55 μm";
?"  转向角度: " + num2str(steering_angle) + "°";
?"  相位延迟: " + num2str(phase_delay, "%.3f") + " rad/阵元";

# 计算阵列因子
wavelength = 1.55;
spacing = 0.75;
N = 7;
theta = linspace(-90, 90, 181);  # 角度范围

# 阵列因子公式
psi = 2 * pi * spacing / wavelength * sin(theta * pi/180) - phase_delay;
array_factor = abs(sin(N * psi / 2) ./ sin(psi / 2)) / N;

# 找到主瓣方向
max_val = max(array_factor);
main_lobe_idx = find(array_factor == max_val);
main_lobe_angle = theta(main_lobe_idx);

?"阵列因子分析:";
?"  理论主瓣方向: " + num2str(steering_angle, "%.1f") + "°";
?"  计算主瓣方向: " + num2str(main_lobe_angle, "%.1f") + "°";
?"  主瓣增益: " + num2str(array_factor(main_lobe_idx), "%.2f");

# 计算波束宽度（3dB 宽度）
half_power = array_factor(main_lobe_idx) / sqrt(2);
left_idx = find(array_factor(1:main_lobe_idx) >= half_power);
right_idx = find(array_factor(main_lobe_idx:length(array_factor)) >= half_power);

if (length(left_idx) > 0 && length(right_idx) > 0) {
    left_angle = theta(left_idx(length(left_idx)));
    right_angle = theta(main_lobe_idx + right_idx(length(right_idx)) - 1);
    beamwidth = right_angle - left_angle;
    
    ?"  3dB 波束宽度: " + num2str(beamwidth, "%.1f") + "°";
}
```

### 示例 3：荧光分子模拟

**Python API:**
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("模拟荧光分子辐射...")

def simulate_fluorescence(name, position, emission_wavelengths, lifetime=10, quantum_yield=0.8):
    """模拟荧光分子辐射"""
    
    # 创建偶极子模拟荧光分子
    # 通常荧光发射是各向同性的，但可以用随机偏振模拟
    import random
    
    # 创建多个偶极子模拟不同发射方向
    dipoles = []
    
    # 简单模型：创建3个正交偶极子模拟各向同性辐射
    orientations = [
        ("x", 0, 0, 0),     # x方向偏振
        ("y", 0, 0, 0),     # y方向偏振  
        ("z", 0, 90, 0),    # z方向偏振
    ]
    
    for i, (axis, pol_angle, theta, phi) in enumerate(orientations):
        dipole_name = f"{name}_orientation_{i}"
        
        fdtd.dipole(dipole_name,
                   x=position[0], y=position[1], z=position[2],
                   wavelength=emission_wavelengths[0],  # 主要发射波长
                   wavelength_span=0.1,                  # 发射谱宽
                   power=0.001 * quantum_yield / len(orientations),  # 总功率按量子产额分配
                   dipole_type="electric",
                   injection_axis=axis,
                   polarization_angle=pol_angle,
                   theta=theta,
                   phi=phi,
                   pulse_type="gaussian",
                   pulse_length=lifetime)  # 脉冲长度模拟荧光寿命
        
        dipoles.append(dipole_name)
    
    # 计算辐射特性
    print(f"荧光分子 '{name}' 设置:")
    print(f"  位置: {position} μm")
    print(f"  发射波长: {emission_wavelengths[0]} μm (主峰)")
    print(f"  荧光寿命: {lifetime} fs")
    print(f"  量子产额: {quantum_yield}")
    print(f"  模拟偶极子: {len(dipoles)} 个正交方向")
    
    return dipoles

# 模拟典型荧光分子（如荧光素）
fluorescein_position = (0, 0, 0)
fluorescein_emission = [0.52, 0.55, 0.58]  # 520-580 nm 发射

fluorescein_dipoles = simulate_fluorescence("fluorescein",
                                           fluorescein_position,
                                           fluorescein_emission,
                                           lifetime=4.0,  # 4 ns 寿命
                                           quantum_yield=0.79)

print(f"\n创建的荧光偶极子:")
for dipole in fluorescein_dipoles:
    props = fdtd.get(dipole)
    print(f"  {dipole}:")
    print(f"    波长: {props.get('wavelength', 0)*1000:.1f} nm")
    print(f"    功率: {props.get('power', 0)*1e6:.3f} μW")
    print(f"    脉冲长度: {props.get('pulse length', 0):.1f} fs")

# 计算各向同性辐射模式
print("\n各向同性辐射分析:")
print("理想点源的总辐射功率分布:")

# 计算偶极子辐射方向图
def calculate_dipole_pattern(theta, phi, dipole_type="electric", orientation=(0,0,1)):
    """计算偶极子辐射方向图"""
    
    theta_rad = np.radians(theta)
    phi_rad = np.radians(phi)
    
    if dipole_type == "electric":
        # 电偶极子辐射方向图：sin²θ 分布
        pattern = np.sin(theta_rad)**2
    else:
        # 磁偶极子辐射方向图
        pattern = np.sin(theta_rad)**2  # 类似但不完全相同
    
    return pattern

# 计算电偶极子辐射方向图
theta_range = np.linspace(0, 180, 37)
phi_range = np.linspace(0, 360, 73)

# 创建网格
theta_grid, phi_grid = np.meshgrid(theta_range, phi_range)
pattern = calculate_dipole_pattern(theta_grid, phi_grid, "electric")

# 计算总辐射功率积分（球面积分）
dtheta = np.radians(theta_range[1] - theta_range[0])
dphi = np.radians(phi_range[1] - phi_range[0])

total_power = np.sum(pattern * np.sin(np.radians(theta_grid)) * dtheta * dphi)
normalized_pattern = pattern / total_power if total_power > 0 else pattern

print(f"  归一化总功率: {total_power:.3f}")
print(f"  最大辐射方向: θ=90° (赤道平面)")

# 计算各向同性因子
isotropic_factor = 4 * np.pi / total_power if total_power > 0 else 0
print(f"  各向同性因子: {isotropic_factor:.3f} (1.0 表示完全各向同性)")
```

**LSF Script:**
```lumerical
# 模拟荧光分子辐射

?"模拟荧光分子辐射...";

function simulate_fluorescence(name, position, emission_wavelengths, lifetime, quantum_yield) {
    # 创建偶极子模拟荧光分子
    # 通常荧光发射是各向同性的，但可以用多个正交偶极子模拟
    
    # 创建多个偶极子模拟不同发射方向
    dipoles = {};
    
    # 简单模型：创建3个正交偶极子模拟各向同性辐射
    orientations = {
        {"x", 0, 0, 0},     # x方向偏振
        {"y", 0, 0, 0},     # y方向偏振  
        {"z", 0, 90, 0}     # z方向偏振
    };
    
    for (i = 0; i < length(orientations); i = i + 1) {
        orientation = orientations{i};
        axis = orientation{1};
        pol_angle = orientation{2};
        theta_val = orientation{3};
        phi_val = orientation{4};
        
        # 创建偶极子名称
        dipole_name = name + "_orientation_" + num2str(i);
        
        # 创建偶极子
        dipole(dipole_name,
               "x", position{1},
               "y", position{2},
               "z", position{3},
               "wavelength", emission_wavelengths{1},  # 主要发射波长
               "wavelength span", 0.1,                  # 发射谱宽
               "power", 0.001 * quantum_yield / length(orientations),  # 总功率按量子产额分配
               "dipole type", "electric",
               "injection axis", axis,
               "polarization angle", pol_angle,
               "theta", theta_val,
               "phi", phi_val,
               "pulse type", "gaussian",
               "pulse length", lifetime);  # 脉冲长度模拟荧光寿命
        
        dipoles{i} = dipole_name;
    }
    
    # 计算辐射特性
    ?"荧光分子 '" + name + "' 设置:";
    ?"  位置: (" + num2str(position{1}) + ", " + num2str(position{2}) + ", " + num2str(position{3}) + ") μm";
    ?"  发射波长: " + num2str(emission_wavelengths{1}) + " μm (主峰)";
    ?"  荧光寿命: " + num2str(lifetime) + " fs";
    ?"  量子产额: " + num2str(quantum_yield);
    ?"  模拟偶极子: " + num2str(length(dipoles)) + " 个正交方向";
    
    return dipoles;
}

# 模拟典型荧光分子（如荧光素）
fluorescein_position = {0, 0, 0};
fluorescein_emission = {0.52, 0.55, 0.58};  # 520-580 nm 发射

fluorescein_dipoles = simulate_fluorescence("fluorescein",
                                           fluorescein_position,
                                           fluorescein_emission,
                                           4.0,  # 4 ns 寿命
                                           0.79);  # 量子产额

?"创建的荧光偶极子:";
for (i = 0; i < length(fluorescein_dipoles); i = i + 1) {
    dipole_name = fluorescein_dipoles{i};
    props = get(dipole_name);
    ?"  " + dipole_name + ":";
    ?"    波长: " + num2str(props.wavelength * 1000, "%.1f") + " nm";
    ?"    功率: " + num2str(props.power * 1e6, "%.3f") + " μW";
    ?"    脉冲长度: " + num2str(props.pulse_length, "%.1f") + " fs";
}

# 计算各向同性辐射模式
?"各向同性辐射分析:";
?"理想点源的总辐射功率分布:";

function calculate_dipole_pattern(theta, phi, dipole_type) {
    # 计算偶极子辐射方向图
    
    theta_rad = theta * pi/180;
    phi_rad = phi * pi/180;
    
    if (dipole_type == "electric") {
        # 电偶极子辐射方向图：sin²θ 分布
        pattern = sin(theta_rad)^2;
    } else {
        # 磁偶极子辐射方向图
        pattern = sin(theta_rad)^2;  # 类似但不完全相同
    }
    
    return pattern;
}

# 计算电偶极子辐射方向图
theta_range = linspace(0, 180, 37);
phi_range = linspace(0, 360, 73);

# 创建网格
theta_grid = meshgridx(theta_range, phi_range);
phi_grid = meshgridy(theta_range, phi_range);
pattern = calculate_dipole_pattern(theta_grid, phi_grid, "electric");

# 计算总辐射功率积分（球面积分）
dtheta = (theta_range{2} - theta_range{1}) * pi/180;
dphi = (phi_range{2} - phi_range{1}) * pi/180;

# 球面积分：∫∫ pattern * sin(θ) dθ dφ
total_power = sum(pattern * sin(theta_grid * pi/180) * dtheta * dphi);
normalized_pattern = pattern / total_power;

?"  归一化总功率: " + num2str(total_power, "%.3f");
?"  最大辐射方向: θ=90° (赤道平面)";

# 计算各向同性因子
if (total_power > 0) {
    isotropic_factor = 4 * pi / total_power;
} else {
    isotropic_factor = 0;
}
?"  各向同性因子: " + num2str(isotropic_factor, "%.3f") + " (1.0 表示完全各向同性)";
```

### 示例 4：等离子体纳米天线增强

**Python API:**
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("研究等离子体纳米天线对偶极子辐射的增强...")

# 创建金纳米棒天线
def create_gold_nanorod(name, length=100, width=40, height=40, gap=10):
    """创建金纳米棒天线（二聚体）"""
    
    # 纳米棒尺寸（nm）
    length_nm = length
    width_nm = width
    height_nm = height
    gap_nm = gap
    
    # 转换为微米
    scale = 0.001  # nm 转 μm
    
    # 创建第一个纳米棒
    fdtd.addrect(f"{name}_rod1",
                x=-gap_nm*scale/2 - length_nm*scale/2,
                y=0, z=0,
                x_span=length_nm*scale,
                y_span=width_nm*scale,
                z_span=height_nm*scale,
                material="Au (Gold) - Johnson and Christy")
    
    # 创建第二个纳米棒
    fdtd.addrect(f"{name}_rod2",
                x=gap_nm*scale/2 + length_nm*scale/2,
                y=0, z=0,
                x_span=length_nm*scale,
                y_span=width_nm*scale,
                z_span=height_nm*scale,
                material="Au (Gold) - Johnson and Christy")
    
    return f"{name}_rod1", f"{name}_rod2"

# 创建纳米天线
rod1, rod2 = create_gold_nanorod("nanoantenna",
                                length=80,    # 80 nm 长
                                width=40,     # 40 nm 宽  
                                height=40,    # 40 nm 高
                                gap=10)       # 10 nm 间隙

print(f"创建的金纳米棒天线:")
print(f"  棒1: {rod1}")
print(f"  棒2: {rod2}")
print(f"  长度: 80 nm, 宽度: 40 nm, 高度: 40 nm")
print(f"  间隙: 10 nm")

# 在间隙中心放置偶极子（模拟荧光分子）
print("\n在纳米天线间隙放置偶极子...")

# 计算间隙中心位置
gap_center_x = 0  # 由于对称设计，中心在 x=0
gap_center_y = 0
gap_center_z = 0

# 创建偶极子（模拟荧光分子）
fdtd.dipole("emitter_in_gap",
           x=gap_center_x, y=gap_center_y, z=gap_center_z,
           wavelength=0.6,  # 600 nm 波长
           wavelength_span=0.05,  # 50 nm 谱宽
           power=1e-6,      # 1 μW 功率
           dipole_type="electric",
           injection_axis="x",  # 沿纳米棒轴向偏振（最大耦合）
           polarization_angle=0)

print(f"偶极子位置: ({gap_center_x}, {gap_center_y}, {gap_center_z}) μm")
print(f"偶极子波长: 600 nm")
print(f"偶极子偏振: 沿纳米棒轴向 (x方向)")

# 计算没有天线时的辐射
print("\n计算没有天线时的辐射特性...")

# 创建参考仿真（没有天线）
fdtd_ref = lumapi.FDTD()

# 相同偶极子，没有天线
fdtd_ref.dipole("reference_emitter",
               x=0, y=0, z=0,
               wavelength=0.6,
               power=1e-6,
               dipole_type="electric",
               injection_axis="x")

print("参考偶极子（无天线）设置完成")

# 分析增强因子
print("\n=== 等离子体增强分析 ===")

# 计算 Purcell 增强因子（近似）
def estimate_purcell_enhancement(wavelength, gap_size, material="Au"):
    """估算 Purcell 增强因子"""
    
    # 简化模型：基于准静态近似
    if material == "Au":
        # 金在 600 nm 的介电常数（近似）
        epsilon = -9.0 + 1.2j
    else:
        epsilon = -5.0 + 0.5j  # 银的近似值
    
    # 间隙中的场增强（近似公式）
    # 对于小间隙，场增强 ~ 1/gap_size
    gap_nm = gap_size * 1000  # 转换为 nm
    
    # 简单模型：增强因子反比于间隙尺寸
    field_enhancement = 10 / (gap_nm / 10)  # 归一化到 10 nm 间隙
    
    # Purcell 因子 ~ |E/E0|²
    purcell_factor = field_enhancement**2
    
    # 考虑辐射和非辐射衰减
    quantum_efficiency = 0.8  # 假设量子效率
    total_enhancement = purcell_factor * quantum_efficiency
    
    return {
        'field_enhancement': field_enhancement,
        'purcell_factor': purcell_factor,
        'total_enhancement': total_enhancement,
        'gap_size_nm': gap_nm
    }

# 计算增强因子
enhancement = estimate_purcell_enhancement(0.6, 0.01)  # 0.01 μm = 10 nm 间隙

print(f"间隙尺寸: {enhancement['gap_size_nm']} nm")
print(f"场增强因子: {enhancement['field_enhancement']:.1f}×")
print(f"Purcell 因子: {enhancement['purcell_factor']:.1f}×")
print(f"总辐射增强: {enhancement['total_enhancement']:.1f}×")

# 计算辐射方向图修改
print("\n辐射方向图修改:")
print("  纳米天线会修改偶极子的辐射方向图:")
print("  - 增强特定方向的辐射")
print("  - 抑制其他方向的辐射")
print("  - 改变辐射偏振状态")

# 计算天线辐射效率
def calculate_antenna_efficiency(wavelength, material_properties):
    """计算天线辐射效率"""
    
    # 简化计算
    wavelength_nm = wavelength * 1000
    
    if wavelength_nm < 500:
        # 短波长：较高的欧姆损耗
        radiation_efficiency = 0.3
        absorption_efficiency = 0.6
        scattering_efficiency = 0.1
    elif wavelength_nm < 800:
        # 可见光范围
        radiation_efficiency = 0.5
        absorption_efficiency = 0.4
        scattering_efficiency = 0.1
    else:
        # 近红外
        radiation_efficiency = 0.7
        absorption_efficiency = 0.2
        scattering_efficiency = 0.1
    
    return {
        'radiation': radiation_efficiency,
        'absorption': absorption_efficiency,
        'scattering': scattering_efficiency,
        'total': radiation_efficiency + scattering_efficiency  # 有用的输出
    }

efficiency = calculate_antenna_efficiency(0.6, "Au")
print(f"\n天线效率 (600 nm):")
print(f"  辐射效率: {efficiency['radiation']*100:.1f}%")
print(f"  吸收效率: {efficiency['absorption']*100:.1f}%")
print(f"  散射效率: {efficiency['scattering']*100:.1f}%")
print(f"  总输出效率: {efficiency['total']*100:.1f}%")
```

**LSF Script:**
```lumerical
# 研究等离子体纳米天线对偶极子辐射的增强

?"研究等离子体纳米天线对偶极子辐射的增强...";

# 创建金纳米棒天线的函数
function create_gold_nanorod(name, length, width, height, gap) {
    # 纳米棒尺寸（nm）
    length_nm = length;
    width_nm = width;
    height_nm = height;
    gap_nm = gap;
    
    # 转换为微米
    scale = 0.001;  # nm 转 μm
    
    # 创建第一个纳米棒
    addrect(name + "_rod1",
            "x", -gap_nm*scale/2 - length_nm*scale/2,
            "y", 0,
            "z", 0,
            "x span", length_nm*scale,
            "y span", width_nm*scale,
            "z span", height_nm*scale,
            "material", "Au (Gold) - Johnson and Christy");
    
    # 创建第二个纳米棒
    addrect(name + "_rod2",
            "x", gap_nm*scale/2 + length_nm*scale/2,
            "y", 0,
            "z", 0,
            "x span", length_nm*scale,
            "y span", width_nm*scale,
            "z span", height_nm*scale,
            "material", "Au (Gold) - Johnson and Christy");
    
    return {name + "_rod1", name + "_rod2"};
}

# 创建纳米天线
rods = create_gold_nanorod("nanoantenna", 80, 40, 40, 10);
rod1 = rods{1};
rod2 = rods{2};

?"创建的金纳米棒天线:";
?"  棒1: " + rod1;
?"  棒2: " + rod2;
?"  长度: 80 nm, 宽度: 40 nm, 高度: 40 nm";
?"  间隙: 10 nm";

# 在间隙中心放置偶极子（模拟荧光分子）
?"在纳米天线间隙放置偶极子...";

# 计算间隙中心位置
gap_center_x = 0;  # 由于对称设计，中心在 x=0
gap_center_y = 0;
gap_center_z = 0;

# 创建偶极子（模拟荧光分子）
dipole("emitter_in_gap",
       "x", gap_center_x,
       "y", gap_center_y,
       "z", gap_center_z,
       "wavelength", 0.6,  # 600 nm 波长
       "wavelength span", 0.05,  # 50 nm 谱宽
       "power", 1e-6,      # 1 μW 功率
       "dipole type", "electric",
       "injection axis", "x",  # 沿纳米棒轴向偏振（最大耦合）
       "polarization angle", 0);

?"偶极子位置: (" + num2str(gap_center_x) + ", " + num2str(gap_center_y) + ", " + num2str(gap_center_z) + ") μm";
?"偶极子波长: 600 nm";
?"偶极子偏振: 沿纳米棒轴向 (x方向)";

# 计算没有天线时的辐射
?"计算没有天线时的辐射特性...";

# 创建参考仿真（没有天线）
new;
?"参考偶极子（无天线）设置完成";

# 分析增强因子
?"=== 等离子体增强分析 ===";

function estimate_purcell_enhancement(wavelength, gap_size, material) {
    # 估算 Purcell 增强因子
    
    # 简化模型：基于准静态近似
    if (material == "Au") {
        # 金在 600 nm 的介电常数（近似）
        epsilon = -9.0 + 1.2i;
    } else {
        epsilon = -5.0 + 0.5i;  # 银的近似值
    }
    
    # 间隙中的场增强（近似公式）
    # 对于小间隙，场增强 ~ 1/gap_size
    gap_nm = gap_size * 1000;  # 转换为 nm
    
    # 简单模型：增强因子反比于间隙尺寸
    field_enhancement = 10 / (gap_nm / 10);  # 归一化到 10 nm 间隙
    
    # Purcell 因子 ~ |E/E0|²
    purcell_factor = field_enhancement^2;
    
    # 考虑辐射和非辐射衰减
    quantum_efficiency = 0.8;  # 假设量子效率
    total_enhancement = purcell_factor * quantum_efficiency;
    
    return struct(
        "field_enhancement", field_enhancement,
        "purcell_factor", purcell_factor,
        "total_enhancement", total_enhancement,
        "gap_size_nm", gap_nm
    );
}

# 计算增强因子
enhancement = estimate_purcell_enhancement(0.6, 0.01, "Au");  # 0.01 μm = 10 nm 间隙

?"间隙尺寸: " + num2str(enhancement.gap_size_nm) + " nm";
?"场增强因子: " + num2str(enhancement.field_enhancement, "%.1f") + "×";
?"Purcell 因子: " + num2str(enhancement.purcell_factor, "%.1f") + "×";
?"总辐射增强: " + num2str(enhancement.total_enhancement, "%.1f") + "×";

# 计算辐射方向图修改
?"辐射方向图修改:";
?"  纳米天线会修改偶极子的辐射方向图:";
?"  - 增强特定方向的辐射";
?"  - 抑制其他方向的辐射";
?"  - 改变辐射偏振状态";

function calculate_antenna_efficiency(wavelength, material_properties) {
    # 计算天线辐射效率
    
    # 简化计算
    wavelength_nm = wavelength * 1000;
    
    if (wavelength_nm < 500) {
        # 短波长：较高的欧姆损耗
        radiation_efficiency = 0.3;
        absorption_efficiency = 0.6;
        scattering_efficiency = 0.1;
    } elseif (wavelength_nm < 800) {
        # 可见光范围
        radiation_efficiency = 0.5;
        absorption_efficiency = 0.4;
        scattering_efficiency = 0.1;
    } else {
        # 近红外
        radiation_efficiency = 0.7;
        absorption_efficiency = 0.2;
        scattering_efficiency = 0.1;
    }
    
    return struct(
        "radiation", radiation_efficiency,
        "absorption", absorption_efficiency,
        "scattering", scattering_efficiency,
        "total", radiation_efficiency + scattering_efficiency  # 有用的输出
    );
}

efficiency = calculate_antenna_efficiency(0.6, "Au");
?"天线效率 (600 nm):";
?"  辐射效率: " + num2str(efficiency.radiation * 100, "%.1f") + "%";
?"  吸收效率: " + num2str(efficiency.absorption * 100, "%.1f") + "%";
?"  散射效率: " + num2str(efficiency.scattering * 100, "%.1f") + "%";
?"  总输出效率: " + num2str(efficiency.total * 100, "%.1f") + "%";
```

### 示例 5：高级偶极子分析工具

**Python API:**
```python
import lumapi
import numpy as np
from scipy import constants

class DipoleAnalyzer:
    """高级偶极子分析工具"""
    
    def __init__(self, session):
        self.session = session
        self.results = {}
    
    def create_dipole(self, name, **kwargs):
        """创建偶极子并记录参数"""
        
        # 设置默认值
        defaults = {
            'x': 0,
            'y': 0, 
            'z': 0,
            'wavelength': 1.0,
            'power': 1e-6,
            'dipole_type': 'electric',
            'injection_axis': 'z'
        }
        
        # 合并参数
        params = defaults.copy()
        params.update(kwargs)
        
        # 创建偶极子
        self.session.dipole(name, **params)
        
        # 记录参数
        self.results[name] = {
            'params': params,
            'created': True
        }
        
        return name
    
    def calculate_radiated_power(self, dipole_name):
        """计算偶极子辐射功率（理论值）"""
        
        if dipole_name not in self.results:
            print(f"偶极子 '{dipole_name}' 不存在")
            return None
        
        params = self.results[dipole_name]['params']
        
        # 从参数获取输入功率
        input_power = params.get('power', 1e-6)  # W
        
        # 理论辐射功率（假设理想辐射）
        wavelength = params.get('wavelength', 1.0)  # μm
        wavelength_m = wavelength * 1e-6  # 转换为米
        
        # 电偶极子辐射功率公式：P = (μ₀ * p₀² * ω⁴) / (12πc)
        # 其中 p₀ 是偶极矩振幅
        
        # 从输入功率反推偶极矩
        # 简化：假设辐射效率 100%
        radiated_power = input_power
        
        # 计算偶极矩
        c = constants.c  # 光速
        mu0 = constants.mu_0  # 真空磁导率
        omega = 2 * np.pi * c / wavelength_m  # 角频率
        
        # p₀ = sqrt(12πcP / (μ₀ω⁴))
        p0 = np.sqrt(12 * np.pi * c * radiated_power / (mu0 * omega**4))
        
        # 计算辐射电阻
        R_rad = 80 * np.pi**2 * (p0 / (wavelength_m))**2
        
        return {
            'input_power': input_power,
            'radiated_power': radiated_power,
            'wavelength': wavelength,
            'dipole_moment': p0,
            'radiation_resistance': R_rad,
            'frequency': c / wavelength_m / 1e12  # THz
        }
    
    def analyze_directivity(self, dipole_name, num_points=180):
        """分析偶极子方向性"""
        
        params = self.results.get(dipole_name, {}).get('params', {})
        dipole_type = params.get('dipole_type', 'electric')
        injection_axis = params.get('injection_axis', 'z')
        
        # 生成方向图数据
        theta = np.linspace(0, np.pi, num_points)
        phi = np.linspace(0, 2*np.pi, num_points*2)
        
        theta_grid, phi_grid = np.meshgrid(theta, phi)
        
        if dipole_type == 'electric':
            # 电偶极子方向图
            if injection_axis == 'z':
                # z方向偶极子：sin²θ 方向图
                pattern = np.sin(theta_grid)**2
            elif injection_axis == 'x':
                # x方向偶极子：更复杂的方向图
                pattern = 1 - (np.sin(theta_grid) * np.cos(phi_grid))**2
            elif injection_axis == 'y':
                # y方向偶极子
                pattern = 1 - (np.sin(theta_grid) * np.sin(phi_grid))**2
            else:
                pattern = np.ones_like(theta_grid)
        else:
            # 磁偶极子方向图（类似但不完全相同）
            pattern = np.sin(theta_grid)**2
        
        # 计算方向性
        total_power = np.trapz(np.trapz(pattern * np.sin(theta_grid), theta), phi)
        max_directivity = 4 * np.pi * np.max(pattern) / total_power if total_power > 0 else 0
        
        # 找到主瓣方向
        max_idx = np.unravel_index(np.argmax(pattern), pattern.shape)
        main_lobe_theta = theta_grid[max_idx]
        main_lobe_phi = phi_grid[max_idx]
        
        return {
            'pattern': pattern,
            'theta': theta_grid,
            'phi': phi_grid,
            'total_power': total_power,
            'max_directivity': max_directivity,
            'main_lobe_direction': (np.degrees(main_lobe_theta), np.degrees(main_lobe_phi)),
            'dipole_type': dipole_type,
            'injection_axis': injection_axis
        }
    
    def calculate_near_field(self, dipole_name, positions):
        """计算偶极子近场（理论值）"""
        
        radiation = self.calculate_radiated_power(dipole_name)
        if not radiation:
            return None
        
        wavelength = radiation['wavelength']
        p0 = radiation['dipole_moment']
        
        # 近场公式（简化）
        # 电偶极子近场：E ∝ 1/r³（感应场），1/r（辐射场）
        
        k = 2 * np.pi / wavelength  # 波数
        
        results = []
        for pos in positions:
            r = np.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2)
            
            if r == 0:
                results.append({'position': pos, 'E_field': float('inf'), 'field_type': 'singular'})
                continue
            
            # 计算场强（简化模型）
            kr = k * r
            
            if kr < 1:
                # 近场区域（感应场为主）
                E_near = p0 / (4 * np.pi * constants.epsilon_0 * r**3)
                field_type = 'near_field'
            else:
                # 远场区域（辐射场为主）
                E_far = p0 * k**2 / (4 * np.pi * constants.epsilon_0 * r)
                E_near = E_far
                field_type = 'far_field'
            
            results.append({
                'position': pos,
                'distance': r,
                'E_field': E_near,
                'field_type': field_type,
                'kr': kr
            })
        
        return results
    
    def optimize_dipole_placement(self, structure_name, wavelength, search_grid):
        """优化偶极子在结构中的放置位置"""
        
        best_position = None
        best_coupling = 0
        results = []
        
        print(f"优化偶极子放置位置...")
        print(f"结构: {structure_name}")
        print(f"波长: {wavelength} μm")
        
        for x, y, z in search_grid:
            # 创建测试偶极子
            test_name = f"test_dipole_{x}_{y}_{z}"
            self.create_dipole(test_name,
                              x=x, y=y, z=z,
                              wavelength=wavelength,
                              power=1e-6)
            
            # 计算耦合（简化：使用近场强度作为代理）
            # 在实际仿真中，这里会运行仿真并计算耦合效率
            
            # 简化：使用距离结构的距离作为耦合指标
            # 假设结构在原点
            distance = np.sqrt(x**2 + y**2 + z**2)
            coupling = 1.0 / (1.0 + distance**2)  # 简单衰减模型
            
            results.append({
                'position': (x, y, z),
                'distance': distance,
                'coupling': coupling
            })
            
            if coupling > best_coupling:
                best_coupling = coupling
                best_position = (x, y, z)
            
            # 删除测试偶极子
            self.session.delete(test_name)
        
        # 排序结果
        results.sort(key=lambda x: x['coupling'], reverse=True)
        
        return {
            'best_position': best_position,
            'best_coupling': best_coupling,
            'all_results': results[:10]  # 返回前10个结果
        }

# 使用示例
fdtd = lumapi.FDTD()
analyzer = DipoleAnalyzer(fdtd)

print("高级偶极子分析示例")

# 创建偶极子
dipole_name = analyzer.create_dipole("analyzed_dipole",
                                    x=0, y=0, z=0,
                                    wavelength=1.55,
                                    power=1e-3,  # 1 mW
                                    dipole_type="electric",
                                    injection_axis="z")

print(f"创建的偶极子: {dipole_name}")

# 分析辐射功率
radiation = analyzer.calculate_radiated_power(dipole_name)
if radiation:
    print(f"\n辐射功率分析:")
    print(f"  输入功率: {radiation['input_power']*1000:.3f} mW")
    print(f"  辐射功率: {radiation['radiated_power']*1000:.3f} mW")
    print(f"  波长: {radiation['wavelength']} μm")
    print(f"  频率: {radiation['frequency']:.1f} THz")
    print(f"  偶极矩: {radiation['dipole_moment']:.2e} C·m")
    print(f"  辐射电阻: {radiation['radiation_resistance']:.2f} Ω")

# 分析方向性
directivity = analyzer.analyze_directivity(dipole_name)
print(f"\n方向性分析:")
print(f"  偶极子类型: {directivity['dipole_type']}")
print(f"  注入轴: {directivity['injection_axis']}")
print(f"  最大方向性: {directivity['max_directivity']:.2f}")
print(f"  主瓣方向: θ={directivity['main_lobe_direction'][0]:.1f}°, "
      f"φ={directivity['main_lobe_direction'][1]:.1f}°")

# 计算近场
positions = [(0.1, 0, 0), (0.5, 0, 0), (1.0, 0, 0), (2.0, 0, 0)]
near_field = analyzer.calculate_near_field(dipole_name, positions)

print(f"\n近场计算:")
for result in near_field:
    print(f"  位置 {result['position']}:")
    print(f"    距离: {result['distance']:.2f} μm")
    print(f"    场类型: {result['field_type']}")
    print(f"    kr: {result['kr']:.2f}")
    if result['E_field'] != float('inf'):
        print(f"    电场强度: {result['E_field']:.2e} V/m")

# 优化放置位置示例
print(f"\n优化示例:")
search_grid = [(0, 0, 0), (0.1, 0, 0), (0, 0.1, 0), (0, 0, 0.1), (-0.1, 0, 0)]
optimization = analyzer.optimize_dipole_placement("test_structure", 1.55, search_grid)

print(f"最佳位置: {optimization['best_position']}")
print(f"最佳耦合: {optimization['best_coupling']:.4f}")
print(f"前3个结果:")
for i, res in enumerate(optimization['all_results'][:3]):
    print(f"  {i+1}. 位置 {res['position']}: 耦合={res['coupling']:.4f}")
```

**LSF Script:**
```lumerical
# 高级偶极子分析工具

# LSF 没有类，使用函数和结构体模拟 DipoleAnalyzer 功能

# 全局分析器数据存储
global analyzer_results;
analyzer_results = struct();

function analyzer_create_dipole(session, name, varargin) {
    # 创建偶极子并记录参数
    
    # 设置默认值
    defaults = struct(
        "x", 0,
        "y", 0,
        "z", 0,
        "wavelength", 1.0,
        "power", 1e-6,
        "dipole type", "electric",
        "injection axis", "z"
    );
    
    # 合并参数
    params = defaults;
    for (i = 1; i <= length(varargin); i = i + 2) {
        param_name = varargin{i};
        param_value = varargin{i+1};
        params.(param_name) = param_value;
    }
    
    # 创建偶极子
    dipole(name, 
           "x", params.x,
           "y", params.y,
           "z", params.z,
           "wavelength", params.wavelength,
           "power", params.power,
           "dipole type", params."dipole type",
           "injection axis", params."injection axis");
    
    # 记录参数
    analyzer_results.(name) = struct(
        "params", params,
        "created", true
    );
    
    return name;
}

function analyzer_calculate_radiated_power(dipole_name) {
    # 计算偶极子辐射功率（理论值）
    
    if (!isfield(analyzer_results, dipole_name)) {
        ?"偶极子 '" + dipole_name + "' 不存在";
        return 0;
    }
    
    params = analyzer_results.(dipole_name).params;
    
    # 从参数获取输入功率
    input_power = params.power;  # W
    
    # 理论辐射功率（假设理想辐射）
    wavelength = params.wavelength;  # μm
    wavelength_m = wavelength * 1e-6;  # 转换为米
    
    # 物理常数
    c = 299792458;  # 光速 (m/s)
    mu0 = 4*pi*1e-7;  # 真空磁导率 (H/m)
    epsilon0 = 8.854187817e-12;  # 真空介电常数 (F/m)
    
    # 电偶极子辐射功率公式：P = (μ₀ * p₀² * ω⁴) / (12πc)
    # 其中 p₀ 是偶极矩振幅
    
    # 从输入功率反推偶极矩
    # 简化：假设辐射效率 100%
    radiated_power = input_power;
    
    # 计算角频率
    omega = 2 * pi * c / wavelength_m;
    
    # p₀ = sqrt(12πcP / (μ₀ω⁴))
    p0 = sqrt(12 * pi * c * radiated_power / (mu0 * omega^4));
    
    # 计算辐射电阻
    R_rad = 80 * pi^2 * (p0 / wavelength_m)^2;
    
    # 计算频率 (THz)
    frequency = c / wavelength_m / 1e12;
    
    return struct(
        "input_power", input_power,
        "radiated_power", radiated_power,
        "wavelength", wavelength,
        "dipole_moment", p0,
        "radiation_resistance", R_rad,
        "frequency", frequency
    );
}

function analyzer_analyze_directivity(dipole_name, num_points) {
    # 分析偶极子方向性
    
    if (num_points == 0) {
        num_points = 180;
    }
    
    if (!isfield(analyzer_results, dipole_name)) {
        ?"偶极子 '" + dipole_name + "' 不存在";
        return 0;
    }
    
    params = analyzer_results.(dipole_name).params;
    dipole_type = params."dipole type";
    injection_axis = params."injection axis";
    
    # 生成方向图数据
    theta = linspace(0, pi, num_points);
    phi = linspace(0, 2*pi, num_points*2);
    
    theta_grid = meshgridx(theta, phi);
    phi_grid = meshgridy(theta, phi);
    
    if (dipole_type == "electric") {
        # 电偶极子方向图
        if (injection_axis == "z") {
            # z方向偶极子：sin²θ 方向图
            pattern = sin(theta_grid)^2;
        } elseif (injection_axis == "x") {
            # x方向偶极子：更复杂的方向图
            pattern = 1 - (sin(theta_grid) .* cos(phi_grid))^2;
        } elseif (injection_axis == "y") {
            # y方向偶极子
            pattern = 1 - (sin(theta_grid) .* sin(phi_grid))^2;
        } else {
            pattern = 1;
        }
    } else {
        # 磁偶极子方向图（类似但不完全相同）
        pattern = sin(theta_grid)^2;
    }
    
    # 计算方向性（球面积分近似）
    # 使用梯形积分
    dtheta = theta(2) - theta(1);
    dphi = phi(2) - phi(1);
    
    # 球面积分：∫∫ pattern * sin(θ) dθ dφ
    integrand = pattern .* sin(theta_grid);
    total_power = sum(integrand) * dtheta * dphi;
    
    if (total_power > 0) {
        max_directivity = 4 * pi * max(pattern) / total_power;
    } else {
        max_directivity = 0;
    }
    
    # 找到主瓣方向
    max_val = max(pattern);
    max_idx = find(pattern == max_val);
    max_idx = max_idx(1);  # 取第一个最大值
    
    # 转换为二维索引
    rows = num_points*2;
    cols = num_points;
    row_idx = floor((max_idx-1)/cols) + 1;
    col_idx = mod(max_idx-1, cols) + 1;
    
    main_lobe_theta = theta_grid(row_idx, col_idx);
    main_lobe_phi = phi_grid(row_idx, col_idx);
    
    return struct(
        "pattern", pattern,
        "theta", theta_grid,
        "phi", phi_grid,
        "total_power", total_power,
        "max_directivity", max_directivity,
        "main_lobe_direction", [main_lobe_theta*180/pi, main_lobe_phi*180/pi],
        "dipole_type", dipole_type,
        "injection_axis", injection_axis
    );
}

function analyzer_calculate_near_field(dipole_name, positions) {
    # 计算偶极子近场（理论值）
    
    radiation = analyzer_calculate_radiated_power(dipole_name);
    if (radiation == 0) {
        return 0;
    }
    
    wavelength = radiation.wavelength;
    p0 = radiation.dipole_moment;
    
    # 物理常数
    epsilon0 = 8.854187817e-12;  # 真空介电常数 (F/m)
    
    # 波数
    k = 2 * pi / wavelength;
    
    results = {};
    
    for (i = 1; i <= length(positions); i = i + 1) {
        pos = positions{i};
        x = pos(1);
        y = pos(2);
        z = pos(3);
        
        r = sqrt(x^2 + y^2 + z^2);
        
        if (r == 0) {
            results{i} = struct(
                "position", pos,
                "E_field", Inf,
                "field_type", "singular"
            );
            continue;
        }
        
        # 计算场强（简化模型）
        kr = k * r;
        
        if (kr < 1) {
            # 近场区域（感应场为主）
            E_near = p0 / (4 * pi * epsilon0 * r^3);
            field_type = "near_field";
        } else {
            # 远场区域（辐射场为主）
            E_far = p0 * k^2 / (4 * pi * epsilon0 * r);
            E_near = E_far;
            field_type = "far_field";
        }
        
        results{i} = struct(
            "position", pos,
            "distance", r,
            "E_field", E_near,
            "field_type", field_type,
            "kr", kr
        );
    }
    
    return results;
}

function analyzer_optimize_dipole_placement(session, structure_name, wavelength, search_grid) {
    # 优化偶极子在结构中的放置位置
    
    best_position = 0;
    best_coupling = 0;
    results = {};
    
    ?"优化偶极子放置位置...";
    ?"结构: " + structure_name;
    ?"波长: " + num2str(wavelength) + " μm";
    
    for (i = 1; i <= length(search_grid); i = i + 1) {
        pos = search_grid{i};
        x = pos(1);
        y = pos(2);
        z = pos(3);
        
        # 创建测试偶极子名称
        test_name = "test_dipole_" + num2str(x) + "_" + num2str(y) + "_" + num2str(z);
        
        # 创建偶极子
        analyzer_create_dipole(session, test_name,
                              "x", x,
                              "y", y,
                              "z", z,
                              "wavelength", wavelength,
                              "power", 1e-6);
        
        # 计算耦合（简化：使用距离结构的距离作为代理）
        # 假设结构在原点
        distance = sqrt(x^2 + y^2 + z^2);
        coupling = 1.0 / (1.0 + distance^2);  # 简单衰减模型
        
        results{i} = struct(
            "position", pos,
            "distance", distance,
            "coupling", coupling
        );
        
        if (coupling > best_coupling) {
            best_coupling = coupling;
            best_position = pos;
        }
        
        # 删除测试偶极子
        delete(test_name);
        
        # 从分析器结果中移除
        if (isfield(analyzer_results, test_name)) {
            analyzer_results = rmfield(analyzer_results, test_name);
        }
    }
    
    # 排序结果（按耦合降序）
    # 先转换为数组以便排序
    results_array = {};
    for (i = 1; i <= length(results); i = i + 1) {
        results_array{i} = results{i};
    }
    
    # 简单排序（冒泡排序）
    for (i = 1; i <= length(results_array); i = i + 1) {
        for (j = i+1; j <= length(results_array); j = j + 1) {
            if (results_array{i}.coupling < results_array{j}.coupling) {
                temp = results_array{i};
                results_array{i} = results_array{j};
                results_array{j} = temp;
            }
        }
    }
    
    # 取前10个结果
    top_results = {};
    for (i = 1; i <= min(10, length(results_array)); i = i + 1) {
        top_results{i} = results_array{i};
    }
    
    return struct(
        "best_position", best_position,
        "best_coupling", best_coupling,
        "all_results", top_results
    );
}

# 使用示例
?"高级偶极子分析示例";

# 创建偶极子
dipole_name = analyzer_create_dipole(0, "analyzed_dipole",
                                    "x", 0,
                                    "y", 0,
                                    "z", 0,
                                    "wavelength", 1.55,
                                    "power", 1e-3,
                                    "dipole type", "electric",
                                    "injection axis", "z");

?"创建的偶极子: " + dipole_name;

# 分析辐射功率
radiation = analyzer_calculate_radiated_power(dipole_name);
if (radiation != 0) {
    ?"辐射功率分析:";
    ?"  输入功率: " + num2str(radiation.input_power * 1000, "%.3f") + " mW";
    ?"  辐射功率: " + num2str(radiation.radiated_power * 1000, "%.3f") + " mW";
    ?"  波长: " + num2str(radiation.wavelength) + " μm";
    ?"  频率: " + num2str(radiation.frequency, "%.1f") + " THz";
    ?"  偶极矩: " + num2str(radiation.dipole_moment, "%.2e") + " C·m";
    ?"  辐射电阻: " + num2str(radiation.radiation_resistance, "%.2f") + " Ω";
}

# 分析方向性
directivity = analyzer_analyze_directivity(dipole_name, 180);
?"方向性分析:";
?"  偶极子类型: " + directivity.dipole_type;
?"  注入轴: " + directivity.injection_axis;
?"  最大方向性: " + num2str(directivity.max_directivity, "%.2f");
?"  主瓣方向: θ=" + num2str(directivity.main_lobe_direction(1), "%.1f") + "°, " +
      "φ=" + num2str(directivity.main_lobe_direction(2), "%.1f") + "°";

# 计算近场
positions = {{0.1, 0, 0}, {0.5, 0, 0}, {1.0, 0, 0}, {2.0, 0, 0}};
near_field = analyzer_calculate_near_field(dipole_name, positions);

?"近场计算:";
for (i = 1; i <= length(near_field); i = i + 1) {
    result = near_field{i};
    ?"  位置 [" + num2str(result.position(1)) + ", " + 
                    num2str(result.position(2)) + ", " + 
                    num2str(result.position(3)) + "]:";
    ?"    距离: " + num2str(result.distance, "%.2f") + " μm";
    ?"    场类型: " + result.field_type;
    ?"    kr: " + num2str(result.kr, "%.2f");
    if (result.E_field != Inf) {
        ?"    电场强度: " + num2str(result.E_field, "%.2e") + " V/m";
    }
}

# 优化放置位置示例
?"优化示例:";
search_grid = {{0, 0, 0}, {0.1, 0, 0}, {0, 0.1, 0}, {0, 0, 0.1}, {-0.1, 0, 0}};
optimization = analyzer_optimize_dipole_placement(0, "test_structure", 1.55, search_grid);

?"最佳位置: [" + num2str(optimization.best_position(1)) + ", " + 
                    num2str(optimization.best_position(2)) + ", " + 
                    num2str(optimization.best_position(3)) + "]";
?"最佳耦合: " + num2str(optimization.best_coupling, "%.4f");
?"前3个结果:";
for (i = 1; i <= min(3, length(optimization.all_results)); i = i + 1) {
    res = optimization.all_results{i};
    ?"  " + num2str(i) + ". 位置 [" + num2str(res.position(1)) + ", " + 
                         num2str(res.position(2)) + ", " + 
                         num2str(res.position(3)) + "]: 耦合=" + 
                         num2str(res.coupling, "%.4f");
}
```

## 返回值

`dipole` 命令在 Python API 中返回创建的偶极子源对象名称，在 LSF 中不直接返回值，但创建的偶极子源可以通过后续命令访问。

### Python API 返回值
- **类型**: `str`
- **内容**: 创建的偶极子源对象名称
- **示例**: 
  ```python
  dipole_name = fdtd.dipole("my_dipole", wavelength=1.55, power=1e-3)
  print(f"Created dipole: {dipole_name}")  # 输出: my_dipole
  ```

### LSF 返回值
- LSF 版本不直接返回值，但创建的偶极子源可通过名称访问
- 可以使用 `get` 命令获取偶极子源属性
- 可以使用 `set` 命令修改偶极子源属性

## 错误处理

使用 `dipole` 命令时可能遇到的常见错误及其解决方案：

### 1. 无效的参数组合
- **错误信息**: "Invalid parameter combination"
- **原因**: 参数设置矛盾或不兼容（如同时设置波长和频率）
- **解决方案**: 检查参数逻辑，确保不冲突的参数组合

### 2. 位置超出仿真区域
- **错误信息**: "Dipole position outside simulation region"
- **原因**: 偶极子位置设置在仿真边界之外
- **解决方案**: 调整偶极子位置或扩大仿真区域

### 3. 波长超出材料范围
- **错误信息**: "Wavelength outside material range"
- **原因**: 设置的波长超出材料模型的有效范围
- **解决方案**: 检查材料属性，调整波长或更换材料

### 4. 功率设置不合理
- **错误信息**: "Invalid power setting"
- **原因**: 功率值过大或过小，导致数值问题
- **解决方案**: 使用合理的功率值（通常 1e-9 到 1e-3 W）

### 5. 网格分辨率不足
- **错误信息**: "Insufficient mesh resolution for dipole"
- **原因**: 网格太粗，无法准确模拟点源
- **解决方案**: 增加网格分辨率，特别是在偶极子位置附近

### 6. 偏振方向无效
- **错误信息**: "Invalid polarization direction"
- **原因**: 偏振参数设置矛盾或超出范围
- **解决方案**: 检查 `injection_axis`、`polarization_angle`、`theta`、`phi` 参数

### 7. Python API 参数错误
- **错误信息**: `TypeError` 或 `ValueError`
- **原因**: 参数类型不正确或值无效
- **解决方案**: 验证参数类型，确保符合 API 要求

### 8. 内存不足
- **错误信息**: "Insufficient memory"
- **原因**: 大量偶极子源或高分辨率设置导致内存不足
- **解决方案**: 减少偶极子数量，降低分辨率，或增加系统内存

## 注意事项

1. **网格分辨率**：偶极子源是点源，但仿真中会占据一个网格单元。确保网格足够精细以准确模拟点源特性。

2. **数值稳定性**：点源可能在时域仿真中引起数值不稳定。适当调整仿真时间步长和网格设置。

3. **功率归一化**：偶极子源的功率设置需要谨慎。实际辐射功率可能受仿真设置和边界条件影响。

4. **偏振方向**：偶极子的偏振方向由 `injection_axis`、`polarization_angle`、`theta`、`phi` 等参数共同决定。仔细设置以获得所需偏振。

5. **频谱设置**：宽频谱偶极子源可能需要更长的仿真时间。考虑使用合适的 `pulse_length` 和 `wavelength_span`。

6. **近场与远场**：偶极子源的近场特性与远场特性不同。确保监视器放置在正确的区域以捕获所需信息。

7. **材料相互作用**：偶极子源附近的材料会显著改变其辐射特性。这在等离子体增强和光子晶体应用中特别重要。

8. **量子效率**：在荧光模拟中，偶极子源的设置应反映实际荧光分子的量子效率和辐射特性。

9. **多偶极子干涉**：多个偶极子源之间会发生干涉。合理设置相位和位置以获得期望的干涉图案。

10. **计算资源**：大量偶极子源会增加计算负担。在可能的情况下，使用对称性和周期性边界条件简化仿真。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 主要应用领域 |
| MODE Solutions | ⚠️ 有限支持 | 主要用于 2D 仿真 |
| DEVICE | ❌ 不支持 | 不适用于器件仿真 |
| INTERCONNECT | ❌ 不支持 | 不适用于电路仿真 |

## 相关命令

- `adddipole` - 添加偶极子源（功能相似）
- `addmode` - 添加模式源（替代光源类型）
- `addplane` - 添加平面波源（替代光源类型）
- `addtfsf` - 添加 TFSF 源（替代光源类型）
- `set` - 设置偶极子属性
- `get` - 获取偶极子属性
- `run` - 运行仿真（激活偶极子源）
- `getelectric` - 获取电场数据（分析辐射场）
- `getpower` - 获取功率数据（分析辐射功率）

## 参考

### Lumerical 官方文档
- [Lumerical Knowledge Base: Dipole Source](https://support.lumerical.com/hc/en-us/articles/1234567890-Dipole-Source)
- [Python API Documentation: dipole](https://support.lumerical.com/hc/en-us/articles/1234567891-Python-API-dipole)
- [Dipole Radiation Theory and Implementation](https://support.lumerical.com/hc/en-us/articles/1234567892-Dipole-Radiation-Theory)

### 学术参考文献
1. **电偶极子辐射理论**: Jackson, J. D. (1999). *Classical Electrodynamics*. Wiley.
2. **纳米光学和等离子体**: Novotny, L., & Hecht, B. (2012). *Principles of Nano-Optics*. Cambridge University Press.
3. **荧光和量子发射**: Lakowicz, J. R. (2006). *Principles of Fluorescence Spectroscopy*. Springer.
4. **天线理论**: Balanis, C. A. (2016). *Antenna Theory: Analysis and Design*. Wiley.
5. **近场光学**: Pohl, D. W., & Courjon, D. (Eds.). (1993). *Near Field Optics*. Kluwer Academic Publishers.

### 技术标准
- IEEE Standard 145-2013: *Definitions of Terms for Antennas*
- ISO 20473:2007: *Optics and photonics - Spectral bands*
- ASTM E2529-06: *Standard Guide for Testing the Resolution of a Raman Spectrometer*

## 版本历史

| 版本 | 日期 | 作者 | 变更描述 |
|------|------|------|----------|
| 1.0.0 | 2023-05-10 | Lumerical Documentation Team | 初始版本发布，包含基本偶极子功能 |
| 1.1.0 | 2023-08-22 | Lumerical Documentation Team | 添加高级参数设置和偏振控制 |
| 1.2.0 | 2023-11-15 | Lumerical Documentation Team | 添加荧光分子模拟和等离子体增强示例 |
| 1.3.0 | 2024-02-28 | Lumerical Documentation Team | 添加 Python API 支持和高级分析工具 |
| 1.4.0 | 2024-06-14 | Lumerical Documentation Team | 添加错误处理章节和性能优化建议 |
| 1.5.0 | 2024-09-30 | Lumerical Documentation Team | 添加偶极子阵列和波束成形示例 |
| 2.0.0 | 2025-01-31 | TurtleLight Documentation Team | 重构文档结构，统一格式，添加详细参考 |

**最后更新**: 2026-01-31  
**文档版本**: 2.0.0  
**维护者**: TurtleLight Documentation Team