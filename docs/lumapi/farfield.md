# farfield - 计算远场

## 概述

`farfield` 命令用于计算从近场数据到远场辐射图的变换，是天线设计、光学元件辐射特性分析和散射计算中的关键工具。该命令基于等效原理和矢量衍射理论，将 FDTD 仿真得到的近场数据转换为远场分布。

### 物理原理
远场计算基于以下理论：
1. **等效原理**：用等效电流和磁流代替实际源
2. **矢量衍射理论**：考虑偏振和矢量特性的衍射计算
3. **傅里叶变换关系**：近场与远场之间通过傅里叶变换关联

### 主要功能
- 计算任意方向的远场辐射图
- 支持偏振分解（TE/TM, 左旋/右旋圆偏振等）
- 提供辐射强度、指向性、增益等参数
- 支持多个频率点的宽带分析
- 可导出为各种格式用于后处理

### 典型应用场景
1. **天线设计**：计算天线辐射方向图、增益、波束宽度
2. **光学元件**：分析透镜、反射镜、光栅的衍射特性
3. **散射分析**：计算目标物体的雷达散射截面（RCS）
4. **光源特性**：分析 LED、激光器的远场分布
5. **系统集成**：评估光学系统的远场性能

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
farfield(name, monitor, options);

# 从监视器计算远场
farfield("farfield1", "field_monitor");

# 带选项的远场计算
farfield("ff_antenna", "field_monitor",
        "frequency", 100e9,
        "theta", linspace(-180,180,361),
        "phi", linspace(0,180,181),
        "polarization", "linear");

# 计算多个频率点
farfield("broadband_ff", "field_monitor",
        "frequency points", 5,
        "output", "E");
```

### Python API (Lumapi)
```python
# 基本调用
session.farfield("name", "monitor")

# 带选项调用
session.farfield("ff_antenna", "field_monitor",
                frequency=100e9,
                theta=np.linspace(-180, 180, 361),
                phi=np.linspace(0, 180, 181),
                polarization="linear")

# 使用字典传递选项
options = {
    "frequency points": 5,
    "output": "E",
    "normalize": True
}
session.farfield("broadband_ff", "field_monitor", **options)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `name` | 字符串 | 是 | 无 | 远场对象名称 |
| `monitor` | 字符串 | 是 | 无 | 近场监视器名称 |
| `options` | 键值对 | 否 | 无 | 计算选项（见下表） |

## 计算选项

### 基本选项
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"frequency"` | 数值/数组 | 监视器中心频率 | 计算频率（Hz） |
| `"frequency points"` | 整数 | 1 | 频率点数量（用于宽带分析） |
| `"theta"` | 数组 | `linspace(-180,180,73)` | θ角范围（度），球坐标系极角 |
| `"phi"` | 数组 | `linspace(0,180,37)` | φ角范围（度），球坐标系方位角 |
| `"polarization"` | 字符串 | `"linear"` | 偏振类型：`"linear"`, `"circular"`, `"total"` |
| `"output"` | 字符串 | `"E"` | 输出类型：`"E"`（电场）, `"H"`（磁场）, `"U"`（辐射强度） |
| `"normalize"` | 布尔 | `false` | 是否归一化到最大值 |
| `"dB"` | 布尔 | `false` | 是否以 dB 为单位输出 |

### 高级选项
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"farfield distance"` | 数值 | `1e6` | 远场距离（米） |
| `"sampling"` | 字符串 | `"automatic"` | 采样方法：`"automatic"`, `"manual"` |
| `"window"` | 字符串 | `"none"` | 加窗函数：`"none"`, `"hamming"`, `"hanning"` |
| `"component"` | 字符串 | `"total"` | 场分量：`"total"`, `"x"`, `"y"`, `"z"` |
| `"phase center"` | 数组 | `[0,0,0]` | 相位中心坐标 [x,y,z] |
| `"reference impedance"` | 数值 | 377 | 参考阻抗（欧姆） |

## 配置属性

远场对象创建后，可通过 `set` 命令配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"frequency"` | 数值 | 无 | 工作频率（Hz） |
| `"theta"` | 数组 | `-180:5:180` | θ角采样点（度） |
| `"phi"` | 数组 | `0:5:180` | φ角采样点（度） |
| `"polarization"` | 字符串 | `"linear"` | 偏振类型 |
| `"output"` | 字符串 | `"E"` | 输出场类型 |
| `"normalize"` | 布尔 | `false` | 归一化开关 |
| `"dB"` | 布尔 | `false` | dB 单位开关 |
| `"farfield distance"` | 数值 | `1e6` | 远场距离（米） |
| `"phase center x"` | 数值 | `0` | 相位中心 X 坐标 |
| `"phase center y"` | 数值 | `0` | 相位中心 Y 坐标 |
| `"phase center z"` | 数值 | `0` | 相位中心 Z 坐标 |
| `"window type"` | 字符串 | `"none"` | 加窗函数类型 |
| `"sampling method"` | 字符串 | `"automatic"` | 采样方法 |
| `"monitor"` | 字符串 | 无 | 源监视器名称 |

## 返回值

`farfield` 命令创建并返回一个远场对象，该对象包含计算得到的远场数据，可用于后续分析、可视化和导出操作。

### 返回值类型

| 调用方式 | 返回值类型 | 说明 |
|----------|------------|------|
| **LSF 脚本** | 远场对象名称（字符串） | 返回创建的远场对象名称，用于后续操作 |
| **Python API** | 字符串（远场对象名称） | 返回远场对象在 Lumerical 环境中的名称，需使用 `getdata()` 获取数据 |

### 返回值使用示例

#### Lumerical 脚本语言（LSF）
```lumerical
// farfield 命令返回远场对象名称
ff_name = farfield("antenna_ff", "field_monitor");
?"创建的远场对象: " + ff_name;

// 使用返回的对象进行后续操作
// 1. 获取远场数据
E_theta = getdata(ff_name, "Etheta");
E_phi = getdata(ff_name, "Ephi");

// 2. 可视化
farfieldplot(ff_name, "2D");
farfieldplot(ff_name, "3D");

// 3. 导出数据
export("farfield_data.mat", "MAT", ff_name);

// 4. 计算关键参数
directivity = directivity(ff_name);
gain = gain(ff_name);
?"指向性: " + num2str(directivity) + " dBi";
?"增益: " + num2str(gain) + " dBi";
```

#### Python API (Lumapi)
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# farfield 命令返回远场对象名称
ff_name = fdtd.farfield("test_ff", "field_monitor")
print(f"创建的远场对象名称: {ff_name}")

# 获取远场数据
ff_data = fdtd.getdata(ff_name)
print(f"远场数据类型: {type(ff_data)}")
print(f"可用键: {list(ff_data.keys())}")

# 检查数据内容
if 'theta' in ff_data and 'phi' in ff_data:
    theta = ff_data['theta']
    phi = ff_data['phi']
    print(f"Theta 角度范围: {theta[0]:.1f}° 到 {theta[-1]:.1f}°, 点数: {len(theta)}")
    print(f"Phi 角度范围: {phi[0]:.1f}° 到 {phi[-1]:.1f}°, 点数: {len(phi)}")

# 计算辐射强度（如果包含场数据）
if 'E' in ff_data:
    E_data = ff_data['E']
    intensity = np.abs(E_data)**2
    max_intensity = np.max(intensity)
    print(f"最大辐射强度: {max_intensity:.3e}")
    
# 或者获取特定分量的数据
E_theta = fdtd.getresult(ff_name, "Etheta")
E_phi = fdtd.getresult(ff_name, "Ephi")
if E_theta is not None and E_phi is not None:
    print(f"E_theta 形状: {E_theta.shape}")
    print(f"E_phi 形状: {E_phi.shape}")
```

### 返回值处理技巧

1. **验证远场对象创建成功**：
   ```python
   def verify_farfield_creation(ff_name):
       """验证远场对象是否成功创建"""
       try:
           # 检查对象是否存在
           obj_type = fdtd.getnamedtype(ff_name)
           if obj_type != "farfield":
               print(f"警告: 对象 {ff_name} 不是远场对象，类型为 {obj_type}")
               return False
           
           # 检查是否有数据
           data = fdtd.getdata(ff_name)
           if not data or len(data) == 0:
               print(f"警告: 远场对象 {ff_name} 没有数据")
               return False
           
           print(f"✓ 远场对象 {ff_name} 创建成功")
           return True
           
       except Exception as e:
           print(f"✗ 远场对象验证失败: {e}")
           return False
   
   # 使用示例
   ff_name = fdtd.farfield("test", "field_monitor")
   if verify_farfield_creation(ff_name):
       print("可进行后续分析")
   ```

2. **批量远场计算**：
   ```python
   def batch_farfield_calculation(monitor_names, ff_prefix="ff"):
       """批量计算多个监视器的远场"""
       ff_names = []
       for i, monitor in enumerate(monitor_names):
           ff_name = f"{ff_prefix}_{i+1}"
           try:
               result_name = fdtd.farfield(ff_name, monitor)
               ff_names.append(result_name)
               print(f"成功创建远场对象: {result_name} (源: {monitor})")
           except Exception as e:
               print(f"创建远场对象失败 {ff_name}: {e}")
               ff_names.append(None)
       return ff_names
   
   # 使用示例
   monitors = ["monitor1", "monitor2", "monitor3"]
   ff_objects = batch_farfield_calculation(monitors)
   ```

3. **错误处理中的返回值检查**：
   ```python
   try:
       ff_name = fdtd.farfield("", "invalid_monitor")  # 无效参数
       if not ff_name:
           print("错误: farfield 命令返回空名称")
   except ValueError as e:
       print(f"参数错误: {e}")
   except RuntimeError as e:
       print(f"运行时错误: {e}")
   ```

## 使用示例

### 示例 1：基本远场计算
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 基本远场计算示例 ===")

# 创建简单天线仿真
fdtd.eval("""
    # 创建 FDTD 仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", 10e-6);
    set("y span", 10e-6);
    set("z span", 5e-6);
    set("mesh accuracy", 2);
    
    # 创建偶极子天线
    adddipole;
    set("name", "dipole");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("wavelength", 1.55e-6);
    set("amplitude", 1);
    
    # 创建近场监视器
    addprofile;
    set("name", "nearfield");
    set("monitor type", "3D");
    set("x span", 8e-6);
    set("y span", 8e-6);
    set("z", 0);
    
    # 运行仿真
    run;
""")

# 计算远场
print("计算远场辐射图...")
fdtd.farfield("dipole_ff", "nearfield",
             frequency=193.4e12,  # 1550nm
             theta=np.linspace(-180, 180, 181),
             phi=np.linspace(0, 180, 91),
             polarization="linear",
             output="E",
             normalize=True)

# 获取远场数据
ff_data = fdtd.getdata("dipole_ff")
theta = ff_data["theta"]
phi = ff_data["phi"]
E_theta = ff_data["E_theta"]
E_phi = ff_data["E_phi"]

print(f"远场数据维度:")
print(f"  theta: {theta.shape}")
print(f"  phi: {phi.shape}")
print(f"  E_theta: {E_theta.shape}")
print(f"  E_phi: {E_phi.shape}")

# 计算辐射强度
U = (np.abs(E_theta)**2 + np.abs(E_phi)**2) / (2 * 377)
U_dB = 10 * np.log10(U / np.max(U))

# 绘制辐射方向图
fig, axes = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': 'polar'})

# θ切面（φ=90°）
phi_idx = np.argmin(np.abs(phi - 90))
axes[0].plot(np.deg2rad(theta), U_dB[phi_idx, :], 'b-', linewidth=2)
axes[0].set_title("E-plane (φ=90°) Radiation Pattern", pad=20)
axes[0].set_theta_zero_location("E")
axes[0].set_theta_direction(-1)
axes[0].grid(True)

# φ切面（θ=90°）
theta_idx = np.argmin(np.abs(theta - 90))
axes[1].plot(np.deg2rad(phi), U_dB[:, theta_idx], 'r-', linewidth=2)
axes[1].set_title("H-plane (θ=90°) Radiation Pattern", pad=20)
axes[1].set_theta_zero_location("N")
axes[1].set_theta_direction(-1)
axes[1].grid(True)

plt.tight_layout()
plt.savefig("dipole_radiation_pattern.png", dpi=150)
print("辐射方向图保存为: dipole_radiation_pattern.png")

# 计算天线参数
print("\n天线参数计算:")
# 最大辐射方向
max_idx = np.unravel_index(np.argmax(U), U.shape)
theta_max = theta[max_idx[1]]
phi_max = phi[max_idx[0]]
print(f"  最大辐射方向: θ={theta_max:.1f}°, φ={phi_max:.1f}°")

# 半功率波束宽度（HPBW）
def calculate_hpbw(angles, pattern):
    """计算半功率波束宽度"""
    pattern_norm = pattern / np.max(pattern)
    half_power = pattern_norm >= 0.5
    if np.any(half_power):
        idx = np.where(half_power)[0]
        return angles[idx[-1]] - angles[idx[0]]
    return np.nan

# E-plane HPBW
E_pattern = U_dB[phi_idx, :]
hp_bw_e = calculate_hpbw(theta, 10**(E_pattern/10))
print(f"  E-plane HPBW: {hp_bw_e:.1f}°")

# H-plane HPBW
H_pattern = U_dB[:, theta_idx]
hp_bw_h = calculate_hpbw(phi, 10**(H_pattern/10))
print(f"  H-plane HPBW: {hp_bw_h:.1f}°")

# 方向性系数
total_power = np.trapz(np.trapz(U * np.sin(np.deg2rad(phi[:, np.newaxis])), 
                               np.deg2rad(theta)), np.deg2rad(phi))
directivity = 4 * np.pi * np.max(U) / total_power
print(f"  方向性系数: {directivity:.2f} ({10*np.log10(directivity):.2f} dBi)")
```

### 示例 2：相控阵天线分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fdtd = lumapi.FDTD()

print("=== 相控阵天线分析示例 ===")

# 创建 4×4 相控阵天线
array_size = 4
spacing = 0.75e-6  # 0.75λ 间距
wavelength = 1.55e-6
freq = 3e8 / wavelength

fdtd.eval(f"""
    # 创建 FDTD 仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", {array_size * spacing * 1.5});
    set("y span", {array_size * spacing * 1.5});
    set("z span", 3e-6);
    
    # 创建相控阵单元
    {{
    for(i=0; i<{array_size}; i++) {{
        for(j=0; j<{array_size}; j++) {{
            adddipole;
            set("name", sprintf("dipole_%d_%d", i, j));
            set("x", {spacing} * (i - ({array_size}-1)/2));
            set("y", {spacing} * (j - ({array_size}-1)/2));
            set("z", 0);
            set("wavelength", {wavelength});
            set("amplitude", 1);
            set("phase", 0);  # 初始相位
        }}
    }}
    }}
    
    # 创建近场监视器
    addprofile;
    set("name", "array_nearfield");
    set("monitor type", "3D");
    set("x span", {array_size * spacing * 1.2});
    set("y span", {array_size * spacing * 1.2});
    set("z", 0.5e-6);
    
    run;
""")

def set_phased_array_phase(theta_steer, phi_steer):
    """设置相控阵相位以实现波束指向"""
    k = 2 * np.pi / wavelength
    for i in range(array_size):
        for j in range(array_size):
            x = spacing * (i - (array_size-1)/2)
            y = spacing * (j - (array_size-1)/2)
            
            # 计算所需相位延迟
            phase_delay = -k * (x * np.sin(np.deg2rad(theta_steer)) * np.cos(np.deg2rad(phi_steer)) +
                               y * np.sin(np.deg2rad(theta_steer)) * np.sin(np.deg2rad(phi_steer)))
            
            # 设置偶极子相位
            fdtd.eval(f'setnamed("dipole_{i}_{j}", "phase", {phase_delay});')
    
    # 重新运行仿真
    fdtd.eval("run;")

# 分析不同指向角的辐射特性
steering_angles = [(0, 0), (30, 0), (45, 0), (30, 45)]  # (θ, φ)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, (theta_steer, phi_steer) in enumerate(steering_angles):
    print(f"分析指向角: θ={theta_steer}°, φ={phi_steer}°")
    
    # 设置相位并计算远场
    set_phased_array_phase(theta_steer, phi_steer)
    
    fdtd.farfield(f"array_ff_{idx}", "array_nearfield",
                 frequency=freq,
                 theta=np.linspace(-90, 90, 181),
                 phi=np.linspace(0, 180, 91),
                 output="U",
                 normalize=True)
    
    # 获取数据
    ff_data = fdtd.getdata(f"array_ff_{idx}")
    theta = ff_data["theta"]
    phi = ff_data["phi"]
    U = ff_data["U"]
    
    # 找到主波束方向
    max_idx = np.unravel_index(np.argmax(U), U.shape)
    theta_max = theta[max_idx[1]]
    phi_max = phi[max_idx[0]]
    
    # 绘制辐射方向图（φ=90°切面）
    phi_idx = np.argmin(np.abs(phi - 90))
    pattern = 10 * np.log10(U[phi_idx, :] / np.max(U))
    
    ax = axes[idx]
    ax.plot(theta, pattern, 'b-', linewidth=2)
    ax.axvline(theta_steer, color='r', linestyle='--', alpha=0.5, label=f'Steering: {theta_steer}°')
    ax.axvline(theta_max, color='g', linestyle=':', alpha=0.5, label=f'Actual: {theta_max:.1f}°')
    
    ax.set_xlabel("θ (degrees)")
    ax.set_ylabel("Normalized Radiation (dB)")
    ax.set_title(f"Phased Array Pattern\nSteering: (θ={theta_steer}°, φ={phi_steer}°)")
    ax.grid(True)
    ax.legend()
    ax.set_ylim([-40, 0])
    
    # 计算阵列因子
    print(f"  理论指向: θ={theta_steer}°, φ={phi_steer}°")
    print(f"  实际指向: θ={theta_max:.1f}°, φ={phi_max:.1f}°")
    
    # 计算副瓣电平
    sidelobe_level = np.sort(pattern)[-2] if len(pattern) > 1 else -np.inf
    print(f"  最高副瓣电平: {sidelobe_level:.2f} dB")

plt.tight_layout()
plt.savefig("phased_array_analysis.png", dpi=150)
print("\n相控阵分析图保存为: phased_array_analysis.png")

# 分析扫描损失
print("\n=== 扫描损失分析 ===")
scan_angles = np.linspace(0, 60, 13)
scan_losses = []

for theta_scan in scan_angles:
    set_phased_array_phase(theta_scan, 0)
    fdtd.farfield(f"scan_ff_{theta_scan:.0f}", "array_nearfield",
                 frequency=freq,
                 theta=np.linspace(-90, 90, 181),
                 phi=90,
                 output="U")
    
    ff_data = fdtd.getdata(f"scan_ff_{theta_scan:.0f}")
    U = ff_data["U"]
    max_gain = np.max(U)
    scan_losses.append(max_gain)

# 归一化到 0° 扫描
scan_losses_norm = scan_losses / scan_losses[0]
scan_loss_dB = 10 * np.log10(scan_losses_norm)

plt.figure(figsize=(8, 5))
plt.plot(scan_angles, scan_loss_dB, 'bo-', linewidth=2, markersize=6)
plt.xlabel("Scan Angle (degrees)")
plt.ylabel("Scan Loss (dB)")
plt.title("Phased Array Scan Loss")
plt.grid(True)
plt.savefig("phased_array_scan_loss.png", dpi=150)
print("扫描损失图保存为: phased_array_scan_loss.png")

# 理论扫描损失（由于阵元方向性）
wavelength = 1.55e-6
k = 2 * np.pi / wavelength
theoretical_loss = []
for theta_scan in scan_angles:
    # 阵列因子
    psi = k * spacing * np.sin(np.deg2rad(theta_scan))
    if array_size > 1:
        af = np.abs(np.sin(array_size * psi / 2) / 
                   (array_size * np.sin(psi / 2)))
        theoretical_loss.append(af**2)
    else:
        theoretical_loss.append(1)

theoretical_loss_dB = 10 * np.log10(theoretical_loss)

plt.figure(figsize=(8, 5))
plt.plot(scan_angles, scan_loss_dB, 'bo-', linewidth=2, markersize=6, label="Simulated")
plt.plot(scan_angles, theoretical_loss_dB, 'r--', linewidth=2, label="Theoretical (Array Factor)")
plt.xlabel("Scan Angle (degrees)")
plt.ylabel("Scan Loss (dB)")
plt.title("Scan Loss: Simulation vs Theory")
plt.grid(True)
plt.legend()
plt.savefig("scan_loss_comparison.png", dpi=150)
print("扫描损失对比图保存为: scan_loss_comparison.png")
```

### 示例 3：光学透镜远场分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 光学透镜远场分析示例 ===")

# 创建透镜系统仿真
lens_diameter = 50e-6
focal_length = 100e-6
wavelength = 1.55e-6

fdtd.eval(f"""
    # 创建 FDTD 仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", 80e-6);
    set("y span", 80e-6);
    set("z span", 150e-6);
    set("mesh accuracy", 3);
    
    # 创建理想透镜（通过相位剖面实现）
    addcustom;
    set("name", "lens");
    set("x", 0);
    set("y", 0);
    set("z", 50e-6);
    set("x span", {lens_diameter});
    set("y span", {lens_diameter});
    set("z span", 1e-6);
    
    # 设置透镜相位函数（抛物面）
    # 相位延迟: φ(x,y) = -k(x²+y²)/(2f)
    k = 2*pi/{wavelength};
    f = {focal_length};
    set("phase", "-k*(x^2+y^2)/(2*f)");
    
    # 创建平面波源
    addplane;
    set("name", "source");
    set("injection axis", "z");
    set("direction", "forward");
    set("x span", {lens_diameter * 1.2});
    set("y span", {lens_diameter * 1.2});
    set("z", 0);
    set("wavelength", {wavelength});
    
    # 创建近场监视器（透镜后）
    addprofile;
    set("name", "lens_output");
    set("monitor type", "2D X-normal");
    set("x", 60e-6);
    set("y span", {lens_diameter * 1.5});
    set("z span", {lens_diameter * 1.5});
    
    # 创建远场监视器
    addprofile;
    set("name", "farfield_monitor");
    set("monitor type", "2D X-normal");
    set("x", 120e-6);  # 焦平面附近
    set("y span", {lens_diameter * 2});
    set("z span", {lens_diameter * 2});
    
    run;
""")

# 计算远场
print("计算透镜远场...")
fdtd.farfield("lens_farfield", "lens_output",
             frequency=3e8/wavelength,
             theta=np.linspace(-30, 30, 121),
             phi=np.linspace(-30, 30, 121),
             output="E",
             normalize=True,
             dB=True)

# 获取远场数据
ff_data = fdtd.getdata("lens_farfield")
theta = ff_data["theta"]
phi = ff_data["phi"]
E_field = ff_data["E"]

print(f"远场数据形状: {E_field.shape}")
print(f"θ范围: {theta[0]:.1f}° 到 {theta[-1]:.1f}°")
print(f"φ范围: {phi[0]:.1f}° 到 {phi[-1]:.1f}°")

# 分析聚焦特性
# 寻找主瓣（最大强度方向）
E_intensity = np.abs(E_field)**2
max_idx = np.unravel_index(np.argmax(E_intensity), E_intensity.shape)
theta_focus = theta[max_idx[1]]
phi_focus = phi[max_idx[0]]
focus_intensity = E_intensity[max_idx]

print(f"\n聚焦特性:")
print(f"  聚焦方向: θ={theta_focus:.2f}°, φ={phi_focus:.2f}°")
print(f"  最大强度: {focus_intensity:.2e} (归一化)")

# 计算聚焦光斑尺寸（半高全宽）
# θ方向的强度剖面
theta_profile = E_intensity[max_idx[0], :]
theta_fwhm = calculate_fwhm(theta, theta_profile)

# φ方向的强度剖面
phi_profile = E_intensity[:, max_idx[1]]
phi_fwhm = calculate_fwhm(phi, phi_profile)

print(f"  聚焦光斑尺寸:")
print(f"    θ方向 FWHM: {theta_fwhm:.3f}°")
print(f"    φ方向 FWHM: {phi_fwhm:.3f}°")

# 理论 Airy 斑尺寸
NA = lens_diameter / (2 * focal_length)  # 数值孔径
airy_diameter = 1.22 * wavelength / lens_diameter  # 弧度
airy_diameter_deg = np.rad2deg(airy_diameter)
print(f"  理论 Airy 斑直径: {airy_diameter_deg:.3f}°")

# 绘制远场分布
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 2D 远场分布
im1 = axes[0].imshow(10*np.log10(E_intensity), 
                    extent=[theta[0], theta[-1], phi[0], phi[-1]],
                    origin='lower', aspect='auto', cmap='hot')
axes[0].set_xlabel("θ (degrees)")
axes[0].set_ylabel("φ (degrees)")
axes[0].set_title("Lens Far-field Intensity (dB)")
plt.colorbar(im1, ax=axes[0], label="Intensity (dB)")

# 添加理论 Airy 斑轮廓
theta_center = (theta[0] + theta[-1]) / 2
phi_center = (phi[0] + phi[-1]) / 2
from matplotlib.patches import Circle
airy_circle = Circle((theta_center, phi_center), airy_diameter_deg/2,
                    fill=False, color='cyan', linestyle='--', linewidth=2)
axes[0].add_patch(airy_circle)
axes[0].plot(theta_focus, phi_focus, 'wx', markersize=10, label='Focus')

# 1D 剖面
theta_idx = max_idx[1]
phi_idx = max_idx[0]

axes[1].plot(theta, 10*np.log10(theta_profile), 'b-', linewidth=2, label='θ profile')
axes[1].plot(phi, 10*np.log10(phi_profile), 'r-', linewidth=2, label='φ profile')

# 标记 FWHM
theta_half_max = 10*np.log10(np.max(theta_profile)/2)
phi_half_max = 10*np.log10(np.max(phi_profile)/2)

axes[1].axhline(theta_half_max, color='b', linestyle=':', alpha=0.5)
axes[1].axhline(phi_half_max, color='r', linestyle=':', alpha=0.5)

axes[1].set_xlabel("Angle (degrees)")
axes[1].set_ylabel("Intensity (dB)")
axes[1].set_title("Far-field Angular Profiles")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.savefig("lens_farfield_analysis.png", dpi=150)
print("透镜远场分析图保存为: lens_farfield_analysis.png")

def calculate_fwhm(x, y):
    """计算半高全宽"""
    y_norm = y / np.max(y)
    half_max = 0.5
    
    # 找到超过半高的点
    above_half = y_norm >= half_max
    if not np.any(above_half):
        return np.nan
    
    indices = np.where(above_half)[0]
    if len(indices) < 2:
        return np.nan
    
    # 线性插值找到精确的 FWHM 点
    left_idx = indices[0]
    if left_idx > 0:
        x_left = np.interp(half_max, 
                          [y_norm[left_idx-1], y_norm[left_idx]],
                          [x[left_idx-1], x[left_idx]])
    else:
        x_left = x[left_idx]
    
    right_idx = indices[-1]
    if right_idx < len(x) - 1:
        x_right = np.interp(half_max,
                           [y_norm[right_idx], y_norm[right_idx+1]],
                           [x[right_idx], x[right_idx+1]])
    else:
        x_right = x[right_idx]
    
    return x_right - x_left

# 计算透镜 Strehl 比（实际峰值与理想衍射极限峰值之比）
# 获取焦平面场分布
focal_data = fdtd.getdata("farfield_monitor")
E_focal = focal_data["E"]
x_focal = focal_data["x"]
y_focal = focal_data["y"]

# 计算实际聚焦光斑的峰值强度
actual_peak = np.max(np.abs(E_focal)**2)

# 计算理想衍射极限（Airy 斑）的峰值强度
# 理想 Airy 斑的峰值强度与透镜面积成正比
lens_area = np.pi * (lens_diameter/2)**2
ideal_peak = lens_area * (2*np.pi/wavelength)**2  # 简化模型

strehl_ratio = actual_peak / ideal_peak
print(f"\n透镜质量评估:")
print(f"  Strehl 比: {strehl_ratio:.4f}")
print(f"  透镜面积: {lens_area:.2e} m²")
print(f"  实际峰值强度: {actual_peak:.2e}")
print(f"  理论峰值强度: {ideal_peak:.2e}")

if strehl_ratio > 0.8:
    print("  透镜质量: 优秀 (接近衍射极限)")
elif strehl_ratio > 0.6:
    print("  透镜质量: 良好")
elif strehl_ratio > 0.4:
    print("  透镜质量: 一般")
else:
    print("  透镜质量: 较差")
```

### 示例 4：雷达散射截面（RCS）计算
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 雷达散射截面（RCS）计算示例 ===")

# 创建金属球体作为散射目标
sphere_radius = 2e-6
wavelength = 10e-6  # 10μm 波长
freq = 3e8 / wavelength

fdtd.eval(f"""
    # 创建 FDTD 仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", 20e-6);
    set("y span", 20e-6);
    set("z span", 20e-6);
    set("mesh accuracy", 3);
    
    # 创建金属球体
    addsphere;
    set("name", "target");
    set("material", "Au (Gold) - Palik");
    set("radius", {sphere_radius});
    set("x", 0);
    set("y", 0);
    set("z", 0);
    
    # 创建平面波源（雷达照射）
    addplane;
    set("name", "radar_source");
    set("injection axis", "z");
    set("direction", "forward");
    set("x span", 15e-6);
    set("y span", 15e-6);
    set("z", -8e-6);
    set("wavelength", {wavelength});
    set("amplitude", 1);
    
    # 创建总场散射场（TF/SF）边界
    addtfsf;
    set("name", "tfsf");
    set("injection axis", "z");
    set("x span", 12e-6);
    set("y span", 12e-6);
    set("z span", 12e-6);
    
    # 创建散射场监视器
    addprofile;
    set("name", "scattered_field");
    set("monitor type", "3D");
    set("x span", 18e-6);
    set("y span", 18e-6);
    set("z span", 18e-6);
    
    # 运行仿真
    run;
""")

# 计算远场散射
print("计算散射远场...")
fdtd.farfield("rcs_farfield", "scattered_field",
             frequency=freq,
             theta=np.linspace(-180, 180, 361),
             phi=np.linspace(0, 180, 181),
             output="E",
             normalize=False)

# 获取远场数据
ff_data = fdtd.getdata("rcs_farfield")
theta = ff_data["theta"]
phi = ff_data["phi"]
E_scattered = ff_data["E"]

print(f"散射场数据维度:")
print(f"  theta: {theta.shape}")
print(f"  phi: {phi.shape}")
print(f"  E_scattered: {E_scattered.shape}")

# 计算 RCS（雷达散射截面）
# RCS = 4πR² |E_scattered|² / |E_incident|²
# 假设入射场振幅为 1 V/m
E_incident = 1.0
R = 1.0  # 1米距离（远场条件）

# RCS 矩阵
rcs = 4 * np.pi * R**2 * np.abs(E_scattered)**2 / E_incident**2
rcs_dBsm = 10 * np.log10(rcs)  # dBsm (dB relative to 1 m²)

print(f"\nRCS 统计:")
print(f"  最大 RCS: {np.max(rcs):.2e} m² ({np.max(rcs_dBsm):.2f} dBsm)")
print(f"  最小 RCS: {np.min(rcs):.2e} m² ({np.min(rcs_dBsm):.2f} dBsm)")
print(f"  平均 RCS: {np.mean(rcs):.2e} m² ({np.mean(rcs_dBsm):.2f} dBsm)")

# 理论金属球体 RCS（光学区）
# 对于 ka >> 1，RCS ≈ πa²
k = 2 * np.pi / wavelength
a = sphere_radius
ka = k * a

if ka > 10:  # 光学区
    theoretical_rcs = np.pi * a**2
    print(f"\n理论 RCS (光学区, ka={ka:.1f}):")
    print(f"  σ = πa² = {theoretical_rcs:.2e} m²")
    print(f"        = {10*np.log10(theoretical_rcs):.2f} dBsm")
elif ka < 0.1:  # 瑞利区
    theoretical_rcs = (9 * np.pi * a**6 * k**4) / (4 * np.pi)
    print(f"\n理论 RCS (瑞利区, ka={ka:.1f}):")
    print(f"  σ = 9πa⁶k⁴/4π = {theoretical_rcs:.2e} m²")
    print(f"               = {10*np.log10(theoretical_rcs):.2f} dBsm")
else:  # 谐振区
    print(f"\n理论 RCS (谐振区, ka={ka:.1f}):")
    print("  需要 Mie 级数解，计算复杂")

# 绘制 RCS 方向图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. 2D RCS 分布（φ=90° 切面）
phi_idx = np.argmin(np.abs(phi - 90))
axes[0, 0].plot(theta, rcs_dBsm[phi_idx, :], 'b-', linewidth=2)
axes[0, 0].set_xlabel("θ (degrees)")
axes[0, 0].set_ylabel("RCS (dBsm)")
axes[0, 0].set_title("RCS vs θ (φ=90°)")
axes[0, 0].grid(True)
axes[0, 0].set_ylim([np.min(rcs_dBsm)-5, np.max(rcs_dBsm)+5])

# 标记前向散射（θ=0°）和后向散射（θ=180°）
axes[0, 0].axvline(0, color='r', linestyle='--', alpha=0.5, label='Forward (0°)')
axes[0, 0].axvline(180, color='g', linestyle='--', alpha=0.5, label='Backward (180°)')
axes[0, 0].legend()

# 2. 极坐标 RCS
ax_polar = axes[0, 1]
ax_polar.plot(np.deg2rad(theta), rcs_dBsm[phi_idx, :], 'b-', linewidth=2)
ax_polar.set_theta_zero_location("E")
ax_polar.set_theta_direction(-1)
ax_polar.set_title("RCS Polar Plot (φ=90°)", pad=20)
ax_polar.grid(True)

# 3. 3D RCS 表面图
# 创建网格
THETA, PHI = np.meshgrid(np.deg2rad(theta), np.deg2rad(phi))
X = rcs_dBsm * np.sin(PHI) * np.cos(THETA)
Y = rcs_dBsm * np.sin(PHI) * np.sin(THETA)
Z = rcs_dBsm * np.cos(PHI)

ax_3d = axes[1, 0]
surf = ax_3d.plot_surface(X, Y, Z, cmap='jet', alpha=0.8,
                         linewidth=0, antialiased=True)
ax_3d.set_xlabel("X")
ax_3d.set_ylabel("Y")
ax_3d.set_zlabel("RCS (dBsm)")
ax_3d.set_title("3D RCS Distribution")
plt.colorbar(surf, ax=ax_3d, shrink=0.5, label="RCS (dBsm)")

# 4. 频率扫描 RCS
print("\n=== 频率扫描 RCS 分析 ===")
frequencies = np.linspace(0.5e13, 5e13, 10)  # 20μm 到 2μm
wavelengths = 3e8 / frequencies
backscatter_rcs = []

for f_idx, freq in enumerate(frequencies):
    print(f"  频率 {f_idx+1}/{len(frequencies)}: {freq/1e12:.1f} THz")
    
    # 更新源频率并重新运行
    fdtd.eval(f'setnamed("radar_source", "frequency", {freq});')
    fdtd.eval("run;")
    
    # 计算远场
    fdtd.farfield(f"rcs_freq_{f_idx}", "scattered_field",
                 frequency=freq,
                 theta=180,  # 后向散射
                 phi=90,
                 output="E")
    
    # 获取后向散射场
    ff_data = fdtd.getdata(f"rcs_freq_{f_idx}")
    E_back = ff_data["E"]
    
    # 计算后向散射 RCS
    rcs_back = 4 * np.pi * R**2 * np.abs(E_back)**2 / E_incident**2
    backscatter_rcs.append(rcs_back[0, 0])

backscatter_rcs = np.array(backscatter_rcs)
backscatter_dBsm = 10 * np.log10(backscatter_rcs)

axes[1, 1].plot(wavelengths*1e6, backscatter_dBsm, 'bo-', linewidth=2, markersize=6)
axes[1, 1].set_xlabel("Wavelength (μm)")
axes[1, 1].set_ylabel("Backscatter RCS (dBsm)")
axes[1, 1].set_title("Frequency-dependent RCS")
axes[1, 1].grid(True)
axes[1, 1].invert_xaxis()  # 波长增加方向

# 添加理论曲线
if hasattr(theoretical_rcs, '__len__'):
    axes[1, 1].axhline(10*np.log10(theoretical_rcs), color='r', linestyle='--',
                      label=f'Theoretical: {10*np.log10(theoretical_rcs):.1f} dBsm')
    axes[1, 1].legend()

plt.tight_layout()
plt.savefig("rcs_analysis.png", dpi=150)
print("\nRCS 分析图保存为: rcs_analysis.png")

# 输出 RCS 数据表
print("\n=== RCS 数据表 ===")
print("Frequency (THz) | Wavelength (μm) | Backscatter RCS (dBsm)")
print("-" * 60)
for f, wl, rcs_db in zip(frequencies/1e12, wavelengths*1e6, backscatter_dBsm):
    print(f"{f:12.1f} | {wl:14.2f} | {rcs_db:20.2f}")
```

### 示例 5：复杂天线系统的完整分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, signal

fdtd = lumapi.FDTD()

print("=== 复杂天线系统完整分析示例 ===")

# 设计参数
center_freq = 28e9  # 28 GHz (5G mmWave)
bandwidth = 5e9     # 5 GHz 带宽
wavelength = constants.c / center_freq

# 创建微带贴片天线阵列
fdtd.eval(f"""
    # 创建 FDTD 仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", 100e-3);
    set("y span", 100e-3);
    set("z span", 50e-3);
    set("mesh accuracy", 3);
    
    # 创建接地板
    addrect;
    set("name", "ground_plane");
    set("material", "PEC");
    set("x", 0);
    set("y", 0);
    set("z", -1.6e-3);
    set("x span", 80e-3);
    set("y span", 80e-3);
    set("z span", 0.035e-3);
    
    # 创建介质基板 (FR-4)
    addrect;
    set("name", "substrate");
    set("material", "FR-4 (lossy)");
    set("x", 0);
    set("y", 0);
    set("z", -1.6e-3 + 0.035e-3/2 + 1.6e-3/2);
    set("x span", 80e-3);
    set("y span", 80e-3);
    set("z span", 1.6e-3);
    
    # 创建 4×4 微带贴片天线阵列
    patch_width = {wavelength/2 * 0.9};
    patch_length = {wavelength/2 * 0.9};
    array_spacing = {wavelength * 0.7};
    
    {{
    for(i=0; i<4; i++) {{
        for(j=0; j<4; j++) {{
            # 贴片天线
            addrect;
            set("name", sprintf("patch_%d_%d", i, j));
            set("material", "PEC");
            set("x", (i-1.5)*array_spacing);
            set("y", (j-1.5)*array_spacing);
            set("z", -1.6e-3 + 0.035e-3 + 1.6e-3);
            set("x span", patch_width);
            set("y span", patch_length);
            set("z span", 0.035e-3);
            
            # 馈线（简化模型）
            addrect;
            set("name", sprintf("feed_%d_%d", i, j));
            set("material", "PEC");
            set("x", (i-1.5)*array_spacing);
            set("y", (j-1.5)*array_spacing - patch_length/2 - 5e-3);
            set("z", -1.6e-3 + 0.035e-3 + 1.6e-3);
            set("x span", 0.5e-3);
            set("y span", 5e-3);
            set("z span", 0.035e-3);
            
            # 端口
            addport;
            set("name", sprintf("port_%d_%d", i, j));
            set("x", (i-1.5)*array_spacing);
            set("y", (j-1.5)*array_spacing - patch_length/2 - 10e-3);
            set("z", -1.6e-3 + 0.035e-3 + 1.6e-3);
            set("impedance", 50);
        }}
    }}
    }}
    
    # 创建近场监视器
    addprofile;
    set("name", "antenna_nearfield");
    set("monitor type", "3D");
    set("x span", 60e-3);
    set("y span", 60e-3);
    set("z", 10e-3);  # 天线平面上方
    
    # 运行仿真
    run;
""")

def analyze_antenna_performance(frequency):
    """分析天线在特定频率的性能"""
    print(f"\n分析频率: {frequency/1e9:.2f} GHz")
    
    # 计算远场
    fdtd.farfield("antenna_ff", "antenna_nearfield",
                 frequency=frequency,
                 theta=np.linspace(-90, 90, 181),
                 phi=np.linspace(0, 360, 181),
                 output="U",
                 normalize=True)
    
    # 获取远场数据
    ff_data = fdtd.getdata("antenna_ff")
    theta = ff_data["theta"]
    phi = ff_data["phi"]
    U = ff_data["U"]
    
    # 计算关键参数
    U_dB = 10 * np.log10(U / np.max(U))
    
    # 1. 增益和方向性
    total_power = np.trapz(np.trapz(U * np.sin(np.deg2rad(theta[:, np.newaxis])), 
                                   np.deg2rad(phi)), np.deg2rad(theta))
    directivity = 4 * np.pi * np.max(U) / total_power
    gain_dBi = 10 * np.log10(directivity)
    
    # 2. 波束宽度
    # 寻找主波束方向
    max_idx = np.unravel_index(np.argmax(U), U.shape)
    theta_max = theta[max_idx[0]]
    phi_max = phi[max_idx[1]]
    
    # E-plane 切面 (φ = phi_max)
    phi_slice = U[:, max_idx[1]]
    hp_bw_e = calculate_hpbw(theta, phi_slice)
    
    # H-plane 切面 (θ = theta_max)
    theta_slice = U[max_idx[0], :]
    hp_bw_h = calculate_hpbw(phi, theta_slice)
    
    # 3. 副瓣电平
    # 创建掩码排除主瓣区域
    theta_mask = (np.abs(theta - theta_max) > hp_bw_e/2)
    phi_mask = (np.abs(phi - phi_max) > hp_bw_h/2)
    
    sidelobe_mask = np.outer(theta_mask, phi_mask)
    if np.any(sidelobe_mask):
        sidelobe_level = np.max(U_dB[sidelobe_mask])
    else:
        sidelobe_level = -np.inf
    
    # 4. 前后比
    front_idx = np.argmin(np.abs(theta - theta_max))
    back_idx = np.argmin(np.abs(theta - (theta_max + 180) % 360))
    front_to_back = U_dB[front_idx, max_idx[1]] - U_dB[back_idx, max_idx[1]]
    
    print(f"  增益: {gain_dBi:.2f} dBi")
    print(f"  方向性: {directivity:.2f}")
    print(f"  E-plane HPBW: {hp_bw_e:.1f}°")
    print(f"  H-plane HPBW: {hp_bw_h:.1f}°")
    print(f"  副瓣电平: {sidelobe_level:.2f} dB")
    print(f"  前后比: {front_to_back:.2f} dB")
    
    return {
        'frequency': frequency,
        'gain_dBi': gain_dBi,
        'directivity': directivity,
        'hp_bw_e': hp_bw_e,
        'hp_bw_h': hp_bw_h,
        'sidelobe_level': sidelobe_level,
        'front_to_back': front_to_back,
        'theta': theta,
        'phi': phi,
        'U_dB': U_dB
    }

# 多频率点分析
frequencies = np.linspace(center_freq - bandwidth/2, 
                         center_freq + bandwidth/2, 5)
results = []

for freq in frequencies:
    result = analyze_antenna_performance(freq)
    results.append(result)

# 绘制性能 vs 频率
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 增益 vs 频率
freqs_ghz = [r['frequency']/1e9 for r in results]
gains = [r['gain_dBi'] for r in results]
axes[0, 0].plot(freqs_ghz, gains, 'bo-', linewidth=2, markersize=6)
axes[0, 0].set_xlabel("Frequency (GHz)")
axes[0, 0].set_ylabel("Gain (dBi)")
axes[0, 0].set_title("Antenna Gain vs Frequency")
axes[0, 0].grid(True)

# 波束宽度 vs 频率
hp_bw_e = [r['hp_bw_e'] for r in results]
hp_bw_h = [r['hp_bw_h'] for r in results]
axes[0, 1].plot(freqs_ghz, hp_bw_e, 'bo-', linewidth=2, markersize=6, label='E-plane')
axes[0, 1].plot(freqs_ghz, hp_bw_h, 'rs-', linewidth=2, markersize=6, label='H-plane')
axes[0, 1].set_xlabel("Frequency (GHz)")
axes[0, 1].set_ylabel("Half-power Beamwidth (degrees)")
axes[0, 1].set_title("Beamwidth vs Frequency")
axes[0, 1].grid(True)
axes[0, 1].legend()

# 副瓣电平 vs 频率
sidelobes = [r['sidelobe_level'] for r in results]
axes[1, 0].plot(freqs_ghz, sidelobes, 'go-', linewidth=2, markersize=6)
axes[1, 0].set_xlabel("Frequency (GHz)")
axes[1, 0].set_ylabel("Sidelobe Level (dB)")
axes[1, 0].set_title("Sidelobe Level vs Frequency")
axes[1, 0].grid(True)

# 前后比 vs 频率
ftb = [r['front_to_back'] for r in results]
axes[1, 1].plot(freqs_ghz, ftb, 'mo-', linewidth=2, markersize=6)
axes[1, 1].set_xlabel("Frequency (GHz)")
axes[1, 1].set_ylabel("Front-to-Back Ratio (dB)")
axes[1, 1].set_title("Front-to-Back Ratio vs Frequency")
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig("antenna_performance_vs_frequency.png", dpi=150)
print("\n天线性能 vs 频率图保存为: antenna_performance_vs_frequency.png")

# 在中心频率绘制完整辐射方向图
center_result = results[len(results)//2]
theta = center_result['theta']
phi = center_result['phi']
U_dB = center_result['U_dB']

# 创建 2D 辐射图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 笛卡尔坐标
im1 = axes[0].imshow(U_dB, extent=[phi[0], phi[-1], theta[0], theta[-1]],
                    origin='lower', aspect='auto', cmap='jet')
axes[0].set_xlabel("φ (degrees)")
axes[0].set_ylabel("θ (degrees)")
axes[0].set_title(f"Radiation Pattern at {center_freq/1e9:.1f} GHz")
plt.colorbar(im1, ax=axes[0], label="Normalized Gain (dB)")

# 极坐标
ax_polar = axes[1]
phi_rad = np.deg2rad(phi)
for theta_idx in [0, 30, 60, 90]:
    theta_val = theta_idx
    pattern = U_dB[theta_idx, :]
    ax_polar.plot(phi_rad, pattern - np.max(pattern) + 10, 
                 label=f'θ={theta_val}°')
ax_polar.set_theta_zero_location("N")
ax_polar.set_theta_direction(-1)
ax_polar.set_title("Normalized Patterns", pad=20)
ax_polar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
ax_polar.grid(True)

plt.tight_layout()
plt.savefig("antenna_radiation_pattern.png", dpi=150)
print("天线辐射方向图保存为: antenna_radiation_pattern.png")

# 计算天线效率
print("\n=== 天线效率分析 ===")

# 获取 S 参数
s_params = []
for i in range(4):
    for j in range(4):
        port_name = f"port_{i}_{j}"
        s_data = fdtd.getdata(port_name, "S")
        if s_data is not None:
            s_params.append(s_data)

if s_params:
    # 计算反射系数
    s11_mag = np.abs(s_params[0])  # 第一个端口的 S11
    reflection_loss = 1 - s11_mag**2
    
    # 计算辐射效率（简化）
    # 实际中需要更复杂的计算
    radiation_efficiency = 0.85  # 假设值
    total_efficiency = radiation_efficiency * reflection_loss
    
    print(f"  反射系数 |S11|: {s11_mag[0]:.3f}")
    print(f"  反射损失: {reflection_loss[0]:.3f}")
    print(f"  辐射效率（假设）: {radiation_efficiency:.3f}")
    print(f"  总效率: {total_efficiency[0]:.3f}")
else:
    print("  无法获取 S 参数数据")

print("\n天线系统分析完成！")
```

## 注意事项

### 1. 计算精度
- **采样定理**：近场采样需满足 Nyquist 准则，避免混叠
- **窗口效应**：加窗减少截断误差，但可能降低分辨率
- **相位中心**：正确设置相位中心对方向图计算至关重要

### 2. 数值稳定性
- **动态范围**：大动态范围计算可能产生数值误差
- **奇异点**：避免在 θ=0° 或 φ=0° 附近过密采样
- **收敛性**：确保仿真充分收敛以获得稳定远场

### 3. 内存管理
- **大角度范围**：密集角度采样增加内存消耗
- **多频率点**：宽带分析需要更多存储
- **大型监视器**：大尺寸近场监视器增加计算负担

### 4. 物理假设
- **远场条件**：计算基于远场近似，距离需满足 R > 2D²/λ
- **均匀介质**：假设均匀背景介质，不处理复杂环境
- **单次散射**：忽略多次散射效应

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 主要应用领域，支持所有功能 |
| **MODE Solutions** | 有限支持 | 可用于波导端口辐射分析 |
| **DEVICE** | 不支持 | 不适用 |
| **INTERCONNECT** | 不支持 | 不适用 |

## 相关命令

- [`farfieldprojection`](./farfieldprojection.md) - 远场投影计算
- [`getfarfield`](./getfarfield.md) - 获取远场数据
- [`nearfield2farfield`](./nearfield2farfield.md) - 近场到远场变换
- [`radiationpattern`](./radiationpattern.md) - 辐射方向图计算
- [`antennaparameters`](./antennaparameters.md) - 天线参数计算

## 最佳实践

### 1. 远场计算验证
```python
def validate_farfield_calculation(session, monitor_name, frequency):
    """验证远场计算的正确性"""
    # 计算远场
    session.farfield("validation_ff", monitor_name,
                    frequency=frequency,
                    theta=[0, 90, 180],
                    phi=[0, 90, 180],
                    output="E")
    
    # 获取数据
    ff_data = session.getdata("validation_ff")
    E = ff_data["E"]
    
    # 检查物理合理性
    # 1. 能量守恒
    total_power = np.sum(np.abs(E)**2)
    print(f"总辐射功率: {total_power:.3e}")
    
    # 2. 对称性检查（对于对称结构）
    if np.allclose(E[0,0], E[0,2], rtol=0.1):  # θ=0° 和 θ=180° 比较
        print("对称性检查: 通过")
    else:
        print("对称性检查: 警告 - 不对称")
    
    # 3. 动态范围
    dynamic_range = 20 * np.log10(np.max(np.abs(E)) / np.min(np.abs(E[np.abs(E) > 0])))
    print(f"动态范围: {dynamic_range:.1f} dB")
    
    return dynamic_range < 80  # 合理动态范围
```

### 2. 高效宽带分析
```python
class BroadbandFarfieldAnalyzer:
    """宽带远场分析器"""
    
    def __init__(self, session, monitor_name):
        self.session = session
        self.monitor_name = monitor_name
        self.results = {}
    
    def analyze_band(self, freq_start, freq_stop, num_points=10):
        """分析频带内的远场特性"""
        frequencies = np.linspace(freq_start, freq_stop, num_points)
        
        for freq in frequencies:
            print(f"分析频率: {freq/1e9:.2f} GHz")
            
            # 计算远场
            ff_name = f"ff_{freq/1e9:.1f}GHz"
            self.session.farfield(ff_name, self.monitor_name,
                                 frequency=freq,
                                 theta=np.linspace(-90, 90, 181),
                                 phi=90,
                                 output="U",
                                 normalize=True)
            
            # 存储结果
            ff_data = self.session.getdata(ff_name)
            self.results[freq] = {
                'theta': ff_data['theta'],
                'U': ff_data['U']
            }
        
        return self.results
    
    def plot_frequency_sweep(self):
        """绘制频率扫描结果"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # 所有频率的方向图
        for freq, data in self.results.items():
            axes[0].plot(data['theta'], 10*np.log10(data['U']/np.max(data['U'])),
                        label=f'{freq/1e9:.1f} GHz', alpha=0.7)
        
        axes[0].set_xlabel("θ (degrees)")
        axes[0].set_ylabel("Normalized Gain (dB)")
        axes[0].set_title("Radiation Patterns at Different Frequencies")
        axes[0].grid(True)
        axes[0].legend()
        
        # 频率 vs 增益
        frequencies = list(self.results.keys())
        max_gains = [10*np.log10(np.max(data['U'])) for data in self.results.values()]
        
        axes[1].plot(np.array(frequencies)/1e9, max_gains, 'bo-', linewidth=2)
        axes[1].set_xlabel("Frequency (GHz)")
        axes[1].set_ylabel("Peak Gain (dB)")
        axes[1].set_title("Peak Gain vs Frequency")
        axes[1].grid(True)
        
        plt.tight_layout()
        return fig
```

### 3. 自动化报告生成
```python
def generate_farfield_report(session, ff_name, output_dir="farfield_report"):
    """生成远场分析报告"""
    import os
    import datetime
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取数据
    ff_data = session.getdata(ff_name)
    
    # 生成报告
    report = f"""Farfield Analysis Report
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Farfield Object: {ff_name}

Parameters:
- Theta range: {ff_data['theta'][0]:.1f}° to {ff_data['theta'][-1]:.1f}°
- Phi range: {ff_data['phi'][0]:.1f}° to {ff_data['phi'][-1]:.1f}°
- Data dimensions: {ff_data['E'].shape if 'E' in ff_data else ff_data['U'].shape}

Key Metrics:
- Maximum intensity: {np.max(np.abs(ff_data['E'])**2 if 'E' in ff_data else ff_data['U']):.3e}
- Angular resolution: {(ff_data['theta'][-1] - ff_data['theta'][0]) / len(ff_data['theta']):.2f}°
- Number of samples: {len(ff_data['theta']) * len(ff_data['phi']):,}

Analysis Notes:
1. Ensure far-field condition is satisfied.
2. Check for numerical convergence.
3. Verify symmetry for symmetric structures.
4. Consider polarization effects.
"""
    
    report_file = os.path.join(output_dir, f"{ff_name}_report.txt")
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"报告生成完成: {report_file}")
    return report_file
```

## 错误处理

### 常见错误类型

| 错误类型 | 原因 | 解决方案 |
|----------|------|----------|
| **监视器不存在错误** | 指定的近场监视器不存在或未包含有效数据 | 检查监视器名称，确保监视器已正确设置并包含仿真数据 |
| **参数范围错误** | 角度范围、频率等参数超出有效范围 | 验证参数：θ∈[-180,180]°，φ∈[0,180]°，频率>0 |
| **内存不足错误** | 角度分辨率过高或频率点数过多 | 减少角度采样点，分块计算，或降低频率点数 |
| **相位中心错误** | 相位中心设置不合理导致远场计算错误 | 检查相位中心是否在近场监视器范围内 |
| **数值收敛错误** | 近场数据未收敛导致远场计算不稳定 | 确保仿真收敛，增加仿真时间或细化网格 |
| **偏振设置错误** | 偏振类型不支持或与输入数据不匹配 | 检查偏振设置，确保与仿真设置一致 |

### Python 错误处理示例

```python
import lumapi

fdtd = lumapi.FDTD()

def safe_farfield(name, monitor, **options):
    """安全的 farfield 命令包装器，包含错误处理"""
    try:
        # 参数验证
        if not name or not isinstance(name, str):
            raise ValueError("远场对象名称必须是有效的字符串")
        
        if not monitor or not isinstance(monitor, str):
            raise ValueError("监视器名称必须是有效的字符串")
        
        # 检查监视器是否存在
        try:
            monitor_type = fdtd.getnamedtype(monitor)
            if monitor_type != "field" and monitor_type != "profile":
                print(f"警告: 监视器 {monitor} 类型为 {monitor_type}，可能不是近场监视器")
        except:
            raise RuntimeError(f"监视器 {monitor} 不存在")
        
        # 验证角度参数（如果提供）
        if "theta" in options:
            theta = options["theta"]
            if isinstance(theta, (list, tuple, np.ndarray)):
                if len(theta) > 1000:
                    print("警告: θ角度点数过多，可能影响性能")
        
        if "phi" in options:
            phi = options["phi"]
            if isinstance(phi, (list, tuple, np.ndarray)):
                if len(phi) > 1000:
                    print("警告: φ角度点数过多，可能影响性能")
        
        # 执行 farfield 计算
        ff_name = fdtd.farfield(name, monitor, **options)
        
        # 验证返回结果
        if not ff_name or not isinstance(ff_name, str):
            raise RuntimeError("farfield 命令未返回有效的远场对象名称")
        
        # 检查远场对象是否成功创建
        ff_type = fdtd.getnamedtype(ff_name)
        if ff_type != "farfield":
            raise RuntimeError(f"创建的对象类型为 {ff_type}，不是远场对象")
        
        print(f"✓ 远场计算成功: {ff_name}")
        return ff_name
        
    except ValueError as e:
        print(f"参数错误: {e}")
        return None
        
    except RuntimeError as e:
        print(f"运行时错误: {e}")
        return None
        
    except MemoryError as e:
        print(f"内存错误: {e}")
        print("建议：减少角度分辨率或分块计算")
        return None
        
    except Exception as e:
        print(f"未知错误: {type(e).__name__} - {e}")
        return None

# 使用示例
# 正常情况
ff_normal = safe_farfield("antenna_ff", "field_monitor", 
                         theta=np.linspace(-180, 180, 361),
                         phi=np.linspace(0, 180, 181),
                         frequency=10e9)
if ff_normal:
    print(f"远场对象创建成功: {ff_normal}")

# 错误情况
ff_error = safe_farfield("", "nonexistent_monitor")  # 无效参数
if not ff_error:
    print("预期中的错误处理")

# 带警告的情况
ff_large = safe_farfield("large_ff", "field_monitor",
                        theta=np.linspace(-180, 180, 2000))  # 角度点过多
```

### LSF 脚本错误处理

```lumerical
// LSF 脚本中的远场错误处理函数
function safe_farfield(name, monitor, varargin)
{
    // 参数验证
    if (!isstring(name) || name == "") {
        throw("错误: 远场对象名称不能为空");
    }
    
    if (!isstring(monitor) || monitor == "") {
        throw("错误: 监视器名称不能为空");
    }
    
    // 检查监视器是否存在
    if (!getnamed(monitor)) {
        throw("错误: 监视器 '" + monitor + "' 不存在");
    }
    
    // 检查监视器类型
    monitor_type = getnamedtype(monitor);
    if (monitor_type != "field" && monitor_type != "profile") {
        ?"警告: 监视器类型为 " + monitor_type + "，可能不是近场监视器";
    }
    
    // 尝试计算远场
    try {
        // 构建参数列表
        args = {name, monitor};
        for (i = 1; i <= length(varargin); i++) {
            args = {args, varargin{i}};
        }
        
        // 执行 farfield 命令
        ff_name = farfield(args);
        
        // 验证结果
        if (!getnamed(ff_name)) {
            throw("错误: 远场对象未成功创建");
        }
        
        ff_type = getnamedtype(ff_name);
        if (ff_type != "farfield") {
            throw("错误: 创建的对象类型为 " + ff_type + "，不是远场对象");
        }
        
        ?"成功创建远场对象: " + ff_name;
        return ff_name;
        
    } catch (e) {
        ?"远场计算失败: " + e;
        
        // 尝试简化计算作为备用方案
        try {
            ?"尝试简化计算...";
            ff_simple = farfield(name + "_simple", monitor, 
                                "theta", -180:30:180,
                                "phi", 0:30:180);
            ?"使用简化参数成功创建远场对象: " + ff_simple;
            return ff_simple;
        } catch (e2) {
            ?"简化计算也失败: " + e2;
            return "";
        }
    }
}

// 使用示例
ff1 = safe_farfield("test_ff", "field_monitor");  // 正常情况
ff2 = safe_farfield("", "monitor");               // 错误情况
ff3 = safe_farfield("ff3", "nonexistent");        // 错误情况

// 清理
if (ff1 != "") {
    ?"ff1 创建成功";
}
if (ff2 == "") {
    ?"ff2 创建失败（符合预期）";
}
```

## 故障排除

### 常见问题
1. **无远场数据**：检查近场监视器是否包含有效数据
2. **方向图异常**：验证相位中心设置和网格收敛性
3. **计算缓慢**：减少角度采样点数或使用对称性
4. **内存不足**：降低角度分辨率或分块计算

### 调试建议
- 首先计算少量角度点验证基本功能
- 检查近场数据的质量和收敛性
- 使用 `getdata` 验证中间结果
- 对比理论预期（如偶极子方向图）

## 版本历史

| 版本 | 日期 | 修改内容 | 修改人 |
|------|------|----------|--------|
| 1.0 | 2025-01-31 | 初始版本，包含基本语法、参数说明和示例 | 文档整理团队 |
| 1.1 | 2026-01-31 | 添加返回值章节，完善错误处理，添加版本历史 | AI Agent C |

---

*文档版本：1.0 | 最后更新：2025-01-31*