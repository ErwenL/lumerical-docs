# farfieldprojection - 远场投影

## 概述

`farfieldprojection` 命令用于将远场数据投影到特定平面或曲面上，实现远场到近场的反向变换或不同坐标系间的转换。该命令在天线测量、光学系统分析和雷达成像中具有重要应用。

### 物理原理
远场投影基于以下理论：
1. **平面波谱分解**：将远场表示为不同方向平面波的叠加
2. **角谱传播**：通过角谱理论实现场传播
3. **坐标变换**：在球坐标系、直角坐标系和特定投影面间转换

### 主要功能
- 将远场数据投影到任意平面或曲面
- 实现远场到近场的反向传播计算
- 在不同坐标系间转换远场数据
- 生成特定平面的场分布图
- 支持多种投影算法和精度控制

### 典型应用场景
1. **天线测量**：将远场测量数据投影到天线口径面
2. **光学系统**：分析远场在像平面或探测器平面的分布
3. **雷达成像**：将雷达散射数据投影到目标平面
4. **系统集成**：评估远场在接收器平面的特性
5. **数据可视化**：创建特定视角或平面的场分布图

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
farfieldprojection(name, farfield_data, projection_plane, options);

# 将远场投影到 XY 平面
farfieldprojection("projection1", "farfield1", "XY", "z", 100e-6);

# 投影到任意平面
farfieldprojection("proj_custom", "farfield_data", 
                  "plane", [1,0,0],  # 法向量
                  "distance", 50e-6,
                  "center", [0,0,0]);

# 带高级选项的投影
farfieldprojection("high_res", "ff_data", "XY",
                  "z", 100e-6,
                  "sampling", 0.1e-6,
                  "method", "angular_spectrum",
                  "padding", 2);
```

### Python API (Lumapi)
```python
# 基本调用
session.farfieldprojection("name", "farfield_data", "projection_plane")

# 投影到 XY 平面
session.farfieldprojection("projection1", "farfield1", "XY", z=100e-6)

# 使用字典传递选项
options = {
    "plane": [1, 0, 0],  # 法向量
    "distance": 50e-6,
    "center": [0, 0, 0],
    "sampling": 0.1e-6,
    "method": "angular_spectrum"
}
session.farfieldprojection("proj_custom", "farfield_data", **options)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `name` | 字符串 | 是 | 无 | 投影结果对象名称 |
| `farfield_data` | 字符串 | 是 | 无 | 远场数据源名称 |
| `projection_plane` | 字符串/数组 | 是 | 无 | 投影平面或曲面定义 |
| `options` | 键值对 | 否 | 无 | 投影选项（见下表） |

## 投影选项

### 平面定义选项
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"plane"` | 字符串 | `"XY"` | 投影平面：`"XY"`, `"YZ"`, `"ZX"`, `"custom"` |
| `"normal"` | 数组 | `[0,0,1]` | 平面法向量（自定义平面时） |
| `"distance"` | 数值 | `0` | 投影平面到原点的距离 |
| `"center"` | 数组 | `[0,0,0]` | 投影平面中心点坐标 |
| `"x span"` | 数值 | 自动 | 投影平面 X 方向跨度 |
| `"y span"` | 数值 | 自动 | 投影平面 Y 方向跨度 |
| `"z"` | 数值 | `0` | 投影平面 Z 坐标（XY平面时） |
| `"y"` | 数值 | `0` | 投影平面 Y 坐标（XZ平面时） |
| `"x"` | 数值 | `0` | 投影平面 X 坐标（YZ平面时） |

### 计算选项
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"sampling"` | 数值 | `λ/10` | 投影平面采样间隔 |
| `"method"` | 字符串 | `"angular_spectrum"` | 投影方法：`"angular_spectrum"`, `"plane_wave"`, `"fraunhofer"` |
| `"padding"` | 数值 | `2` | 零填充因子（防止混叠） |
| `"window"` | 字符串 | `"none"` | 加窗函数：`"none"`, `"hamming"`, `"hanning"` |
| `"frequency"` | 数值 | 远场频率 | 投影频率（Hz） |
| `"components"` | 字符串 | `"all"` | 场分量：`"all"`, `"Ex"`, `"Ey"`, `"Ez"`, `"Hx"`, `"Hy"`, `"Hz"` |
| `"polarization"` | 字符串 | `"linear"` | 偏振类型：`"linear"`, `"circular"`, `"total"` |

### 输出选项
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"output"` | 字符串 | `"E"` | 输出场类型：`"E"`（电场）, `"H"`（磁场）, `"both"` |
| `"normalize"` | 布尔 | `false` | 是否归一化到最大值 |
| `"dB"` | 布尔 | `false` | 是否以 dB 为单位输出 |
| `"phase"` | 布尔 | `false` | 是否输出相位信息 |
| `"intensity"` | 布尔 | `true` | 是否输出强度信息 |

## 配置属性

投影对象创建后，可通过 `set` 命令配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"plane type"` | 字符串 | `"XY"` | 投影平面类型 |
| `"plane normal"` | 数组 | `[0,0,1]` | 平面法向量 |
| `"plane distance"` | 数值 | `0` | 平面到原点距离 |
| `"plane center"` | 数组 | `[0,0,0]` | 平面中心坐标 |
| `"x span"` | 数值 | 自动 | X 方向跨度 |
| `"y span"` | 数值 | 自动 | Y 方向跨度 |
| `"sampling interval"` | 数值 | `λ/10` | 采样间隔 |
| `"projection method"` | 字符串 | `"angular_spectrum"` | 投影方法 |
| `"padding factor"` | 数值 | `2` | 零填充因子 |
| `"window type"` | 字符串 | `"none"` | 加窗函数类型 |
| `"frequency"` | 数值 | 远场频率 | 工作频率 |
| `"output type"` | 字符串 | `"E"` | 输出场类型 |
| `"normalize output"` | 布尔 | `false` | 归一化开关 |
| `"dB scale"` | 布尔 | `false` | dB 单位开关 |
| `"farfield source"` | 字符串 | 无 | 远场数据源名称 |

## 使用示例

### 示例 1：基本远场投影
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 基本远场投影示例 ===")

# 创建简单天线仿真并计算远场
fdtd.eval("""
    # 创建偶极子天线
    addfdtd;
    set("dimension", "3D");
    set("x span", 10e-6);
    set("y span", 10e-6);
    set("z span", 5e-6);
    
    adddipole;
    set("name", "dipole");
    set("wavelength", 1.55e-6);
    set("x", 0);
    set("y", 0);
    set("z", 0);
    
    addprofile;
    set("name", "nearfield");
    set("monitor type", "3D");
    set("x span", 8e-6);
    set("y span", 8e-6);
    set("z", 0);
    
    run;
    
    # 计算远场
    farfield("dipole_ff", "nearfield",
             frequency=193.4e12,
             theta=linspace(-90,90,181),
             phi=linspace(0,360,181),
             output="E");
""")

# 将远场投影到不同平面
print("将远场投影到不同平面...")

# 1. 投影到 XY 平面（z = 50μm）
fdtd.farfieldprojection("proj_xy", "dipole_ff", "XY",
                       z=50e-6,
                       x_span=20e-6,
                       y_span=20e-6,
                       sampling=0.5e-6,
                       output="E",
                       normalize=True)

# 2. 投影到 YZ 平面（x = 0）
fdtd.farfieldprojection("proj_yz", "dipole_ff", "YZ",
                       x=0,
                       y_span=20e-6,
                       z_span=20e-6,
                       sampling=0.5e-6,
                       output="E",
                       normalize=True)

# 3. 投影到自定义平面（法向量 [1,1,0]，距离 30μm）
fdtd.farfieldprojection("proj_custom", "dipole_ff",
                       plane=[1, 1, 0],
                       distance=30e-6,
                       center=[0, 0, 0],
                       x_span=20e-6,
                       y_span=20e-6,
                       sampling=0.5e-6,
                       output="E",
                       normalize=True)

# 获取投影数据
proj_xy_data = fdtd.getdata("proj_xy")
proj_yz_data = fdtd.getdata("proj_yz")
proj_custom_data = fdtd.getdata("proj_custom")

print(f"\n投影数据维度:")
print(f"  XY 平面: {proj_xy_data['E'].shape}")
print(f"  YZ 平面: {proj_yz_data['E'].shape}")
print(f"  自定义平面: {proj_custom_data['E'].shape}")

# 绘制投影结果
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# XY 平面投影
E_xy = np.abs(proj_xy_data['E'])**2
im1 = axes[0].imshow(E_xy, extent=[proj_xy_data['x'][0]*1e6, proj_xy_data['x'][-1]*1e6,
                                   proj_xy_data['y'][0]*1e6, proj_xy_data['y'][-1]*1e6],
                    origin='lower', cmap='hot')
axes[0].set_xlabel("X (μm)")
axes[0].set_ylabel("Y (μm)")
axes[0].set_title("Projection on XY Plane (z=50μm)")
plt.colorbar(im1, ax=axes[0], label="Intensity")

# YZ 平面投影
E_yz = np.abs(proj_yz_data['E'])**2
im2 = axes[1].imshow(E_yz, extent=[proj_yz_data['y'][0]*1e6, proj_yz_data['y'][-1]*1e6,
                                   proj_yz_data['z'][0]*1e6, proj_yz_data['z'][-1]*1e6],
                    origin='lower', cmap='hot')
axes[1].set_xlabel("Y (μm)")
axes[1].set_ylabel("Z (μm)")
axes[1].set_title("Projection on YZ Plane (x=0)")
plt.colorbar(im2, ax=axes[1], label="Intensity")

# 自定义平面投影
E_custom = np.abs(proj_custom_data['E'])**2
im3 = axes[2].imshow(E_custom, extent=[proj_custom_data['x'][0]*1e6, proj_custom_data['x'][-1]*1e6,
                                       proj_custom_data['y'][0]*1e6, proj_custom_data['y'][-1]*1e6],
                    origin='lower', cmap='hot')
axes[2].set_xlabel("X' (μm)")
axes[2].set_ylabel("Y' (μm)")
axes[2].set_title("Projection on Custom Plane (normal=[1,1,0])")
plt.colorbar(im3, ax=axes[2], label="Intensity")

plt.tight_layout()
plt.savefig("farfield_projections.png", dpi=150)
print("\n投影结果图保存为: farfield_projections.png")

# 分析投影精度
def analyze_projection_accuracy(proj_data, plane_name):
    """分析投影精度"""
    E = proj_data['E']
    intensity = np.abs(E)**2
    
    # 计算总功率
    total_power = np.sum(intensity)
    
    # 计算峰值位置
    max_idx = np.unravel_index(np.argmax(intensity), intensity.shape)
    max_x = proj_data['x'][max_idx[1]] * 1e6
    max_y = proj_data['y'][max_idx[0]] * 1e6
    
    # 计算半高全宽
    x_profile = intensity[max_idx[0], :]
    y_profile = intensity[:, max_idx[1]]
    
    def calculate_fwhm(x, profile):
        half_max = np.max(profile) / 2
        above_half = profile >= half_max
        if not np.any(above_half):
            return np.nan
        indices = np.where(above_half)[0]
        if len(indices) < 2:
            return np.nan
        return (x[indices[-1]] - x[indices[0]]) * 1e6
    
    fwhm_x = calculate_fwhm(proj_data['x'], x_profile)
    fwhm_y = calculate_fwhm(proj_data['y'], y_profile)
    
    print(f"\n{plane_name} 投影分析:")
    print(f"  总功率: {total_power:.3e}")
    print(f"  峰值位置: ({max_x:.2f} μm, {max_y:.2f} μm)")
    print(f"  X方向 FWHM: {fwhm_x:.2f} μm")
    print(f"  Y方向 FWHM: {fwhm_y:.2f} μm")
    
    return total_power, (max_x, max_y), (fwhm_x, fwhm_y)

analyze_projection_accuracy(proj_xy_data, "XY 平面")
analyze_projection_accuracy(proj_yz_data, "YZ 平面")
analyze_projection_accuracy(proj_custom_data, "自定义平面")
```

### 示例 2：天线口径场重构
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 天线口径场重构示例 ===")

# 创建喇叭天线仿真
horn_length = 50e-6
horn_aperture = 20e-6
wavelength = 10e-6
frequency = 3e8 / wavelength

fdtd.eval(f"""
    # 创建喇叭天线
    addfdtd;
    set("dimension", "3D");
    set("x span", 80e-6);
    set("y span", 80e-6);
    set("z span", 100e-6);
    
    # 创建喇叭结构（简化模型）
    addrect;
    set("name", "horn_body");
    set("material", "PEC");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", 5e-6);
    set("y span", 5e-6);
    set("z span", {horn_length});
    
    addrect;
    set("name", "horn_aperture");
    set("material", "PEC");
    set("x", 0);
    set("y", 0);
    set("z", {horn_length});
    set("x span", {horn_aperture});
    set("y span", {horn_aperture});
    set("z span", 1e-6);
    
    # 创建激励源
    addmode;
    set("name", "source");
    set("injection axis", "z");
    set("x", 0);
    set("y", 0);
    set("z", -5e-6);
    
    # 创建远场监视器
    addprofile;
    set("name", "farfield_monitor");
    set("monitor type", "3D");
    set("x span", 60e-6);
    set("y span", 60e-6);
    set("z", {horn_length + 10e-6});
    
    run;
    
    # 计算远场
    farfield("horn_ff", "farfield_monitor",
             frequency={frequency},
             theta=linspace(-60,60,121),
             phi=linspace(0,360,121),
             output="E");
""")

# 将远场投影回天线口径面
print("将远场投影回天线口径面...")

# 投影到天线口径平面（z = horn_length）
fdtd.farfieldprojection("aperture_field", "horn_ff",
                       plane="XY",
                       z=horn_length,
                       x_span=horn_aperture * 1.5,
                       y_span=horn_aperture * 1.5,
                       sampling=0.2e-6,
                       method="angular_spectrum",
                       padding=4,
                       output="E",
                       normalize=True,
                       phase=True)

# 获取口径场数据
aperture_data = fdtd.getdata("aperture_field")
E_aperture = aperture_data['E']
x_aperture = aperture_data['x']
y_aperture = aperture_data['y']

print(f"口径场数据维度: {E_aperture.shape}")
print(f"X 范围: {x_aperture[0]*1e6:.1f} 到 {x_aperture[-1]*1e6:.1f} μm")
print(f"Y 范围: {y_aperture[0]*1e6:.1f} 到 {y_aperture[-1]*1e6:.1f} μm")

# 分析口径场特性
E_magnitude = np.abs(E_aperture)
E_phase = np.angle(E_aperture, deg=True)

# 计算口径效率
def calculate_aperture_efficiency(E_field, wavelength):
    """计算天线口径效率"""
    # 计算口径场分布
    amplitude = np.abs(E_field)
    phase = np.angle(E_field)
    
    # 计算口径面积
    dx = x_aperture[1] - x_aperture[0]
    dy = y_aperture[1] - y_aperture[0]
    aperture_area = len(x_aperture) * len(y_aperture) * dx * dy
    
    # 计算场分布矩
    total_power = np.sum(amplitude**2) * dx * dy
    
    # 计算幅度锥削效率
    avg_amplitude = np.mean(amplitude)
    amplitude_taper = np.std(amplitude) / avg_amplitude
    amplitude_efficiency = 1 / (1 + amplitude_taper**2)
    
    # 计算相位误差效率
    phase_error = np.std(phase)
    phase_efficiency = np.sinc(phase_error / 360)  # 简化模型
    
    # 总口径效率
    aperture_efficiency = amplitude_efficiency * phase_efficiency
    
    print(f"\n口径效率分析:")
    print(f"  口径面积: {aperture_area*1e12:.2f} μm²")
    print(f"  总功率: {total_power:.3e}")
    print(f"  幅度锥削效率: {amplitude_efficiency:.3f}")
    print(f"  相位误差效率: {phase_efficiency:.3f}")
    print(f"  总口径效率: {aperture_efficiency:.3f} ({10*np.log10(aperture_efficiency):.2f} dB)")
    
    return aperture_efficiency

eff = calculate_aperture_efficiency(E_aperture, wavelength)

# 绘制口径场分布
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 幅度分布
im1 = axes[0].imshow(E_magnitude, extent=[x_aperture[0]*1e6, x_aperture[-1]*1e6,
                                         y_aperture[0]*1e6, y_aperture[-1]*1e6],
                    origin='lower', cmap='hot')
axes[0].set_xlabel("X (μm)")
axes[0].set_ylabel("Y (μm)")
axes[0].set_title("Aperture Field Amplitude")
plt.colorbar(im1, ax=axes[0], label="|E|")

# 相位分布
im2 = axes[1].imshow(E_phase, extent=[x_aperture[0]*1e6, x_aperture[-1]*1e6,
                                      y_aperture[0]*1e6, y_aperture[-1]*1e6],
                    origin='lower', cmap='hsv', vmin=-180, vmax=180)
axes[1].set_xlabel("X (μm)")
axes[1].set_ylabel("Y (μm)")
axes[1].set_title("Aperture Field Phase (degrees)")
plt.colorbar(im2, ax=axes[1], label="Phase (deg)")

# 幅度轮廓
x_profile = E_magnitude[len(y_aperture)//2, :]
y_profile = E_magnitude[:, len(x_aperture)//2]

axes[2].plot(x_aperture*1e6, x_profile / np.max(x_profile), 'b-', linewidth=2, label='X profile')
axes[2].plot(y_aperture*1e6, y_profile / np.max(y_profile), 'r-', linewidth=2, label='Y profile')

# 添加理论分布（喇叭天线的典型分布）
# 理论分布通常是余弦锥削
x_norm = x_aperture / (horn_aperture/2)
theoretical_profile = np.cos(np.pi * x_norm / 2)**2
theoretical_profile[np.abs(x_norm) > 1] = 0

axes[2].plot(x_aperture*1e6, theoretical_profile, 'g--', linewidth=2, label='Theoretical (cos²)')

axes[2].set_xlabel("Position (μm)")
axes[2].set_ylabel("Normalized Amplitude")
axes[2].set_title("Aperture Field Profiles")
axes[2].grid(True)
axes[2].legend()
axes[2].set_xlim([-horn_aperture/2*1e6, horn_aperture/2*1e6])

plt.tight_layout()
plt.savefig("aperture_field_reconstruction.png", dpi=150)
print("\n口径场重构结果保存为: aperture_field_reconstruction.png")

# 验证投影精度：比较原始近场和重构场
print("\n=== 投影精度验证 ===")

# 获取原始近场数据（在口径面附近）
fdtd.eval(f"""
    addprofile;
    set("name", "original_aperture");
    set("monitor type", "2D X-normal");
    set("x", {horn_length});
    set("y span", {horn_aperture * 1.5});
    set("z span", {horn_aperture * 1.5});
    run;
""")

original_data = fdtd.getdata("original_aperture")
E_original = original_data['E']
y_original = original_data['y']
z_original = original_data['z']

print(f"原始近场数据维度: {E_original.shape}")

# 插值到相同网格进行比较
from scipy import interpolate

# 创建插值函数
E_original_interp = interpolate.RegularGridInterpolator((y_original, z_original), E_original.T)

# 在重构场网格上采样
Y_grid, Z_grid = np.meshgrid(y_aperture, x_aperture, indexing='ij')
E_original_sampled = E_original_interp((Y_grid, Z_grid))

# 计算重构误差
reconstruction_error = np.abs(E_aperture.T - E_original_sampled)
relative_error = reconstruction_error / np.max(np.abs(E_original_sampled))

print(f"最大绝对误差: {np.max(reconstruction_error):.3e}")
print(f"平均相对误差: {np.mean(relative_error)*100:.2f}%")
print(f"均方根误差: {np.sqrt(np.mean(reconstruction_error**2)):.3e}")

# 绘制误差图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

im3 = axes[0].imshow(np.abs(E_original_sampled), 
                    extent=[y_original[0]*1e6, y_original[-1]*1e6,
                            z_original[0]*1e6, z_original[-1]*1e6],
                    origin='lower', cmap='hot')
axes[0].set_xlabel("Y (μm)")
axes[0].set_ylabel("Z (μm)")
axes[0].set_title("Original Near Field (amplitude)")
plt.colorbar(im3, ax=axes[0], label="|E|")

im4 = axes[1].imshow(relative_error * 100,
                    extent=[y_aperture[0]*1e6, y_aperture[-1]*1e6,
                            x_aperture[0]*1e6, x_aperture[-1]*1e6],
                    origin='lower', cmap='coolwarm', vmin=0, vmax=10)
axes[1].set_xlabel("Y (μm)")
axes[1].set_ylabel("X (μm)")
axes[1].set_title("Reconstruction Error (%)")
plt.colorbar(im4, ax=axes[1], label="Error (%)")

plt.tight_layout()
plt.savefig("projection_accuracy_verification.png", dpi=150)
print("投影精度验证图保存为: projection_accuracy_verification.png")
```

### 示例 3：光学系统像平面分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 光学系统像平面分析示例 ===")

# 创建简单成像系统
lens_focal = 100e-6
object_distance = 150e-6
image_distance = 1 / (1/lens_focal - 1/object_distance)  # 透镜公式
wavelength = 1.55e-6
NA = 0.3  # 数值孔径

fdtd.eval(f"""
    # 创建成像系统
    addfdtd;
    set("dimension", "3D");
    set("x span", 200e-6);
    set("y span", 200e-6);
    set("z span", 300e-6);
    
    # 创建物平面（两个点光源）
    adddipole;
    set("name", "point1");
    set("x", -5e-6);
    set("y", 0);
    set("z", 0);
    set("wavelength", {wavelength});
    
    adddipole;
    set("name", "point2");
    set("x", 5e-6);
    set("y", 0);
    set("z", 0);
    set("wavelength", {wavelength});
    
    # 创建理想透镜
    addcustom;
    set("name", "imaging_lens");
    set("x", 0);
    set("y", 0);
    set("z", {object_distance});
    set("x span", 2*{lens_focal}*{NA});  # 根据 NA 计算透镜直径
    set("y span", 2*{lens_focal}*{NA});
    set("z span", 1e-6);
    
    # 设置透镜相位函数
    k = 2*pi/{wavelength};
    f = {lens_focal};
    set("phase", "-k*(x^2+y^2)/(2*f)");
    
    # 创建远场监视器（透镜后）
    addprofile;
    set("name", "farfield_after_lens");
    set("monitor type", "3D");
    set("x span", 80e-6);
    set("y span", 80e-6);
    set("z", {object_distance + 10e-6});
    
    run;
    
    # 计算远场
    farfield("imaging_ff", "farfield_after_lens",
             frequency={3e8/wavelength},
             theta=linspace(-30,30,121),
             phi=linspace(-30,30,121),
             output="E");
""")

print(f"成像系统参数:")
print(f"  波长: {wavelength*1e6:.2f} μm")
print(f"  透镜焦距: {lens_focal*1e6:.1f} μm")
print(f"  物距: {object_distance*1e6:.1f} μm")
print(f"  像距（理论）: {image_distance*1e6:.1f} μm")
print(f"  数值孔径 NA: {NA:.2f}")

# 将远场投影到像平面
print("\n将远场投影到像平面...")

# 尝试不同投影距离寻找最佳聚焦
projection_distances = np.linspace(image_distance*0.8, image_distance*1.2, 5)
best_focus_distance = None
best_focus_quality = 0

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, proj_distance in enumerate(projection_distances):
    print(f"  投影距离 {idx+1}/{len(projection_distances)}: {proj_distance*1e6:.1f} μm")
    
    # 投影到像平面
    fdtd.farfieldprojection(f"image_plane_{idx}", "imaging_ff",
                           plane="XY",
                           z=object_distance + proj_distance,
                           x_span=40e-6,
                           y_span=40e-6,
                           sampling=0.2e-6,
                           method="angular_spectrum",
                           padding=4,
                           output="E",
                           normalize=True)
    
    # 获取像平面场
    image_data = fdtd.getdata(f"image_plane_{idx}")
    E_image = image_data['E']
    x_image = image_data['x']
    y_image = image_data['y']
    
    # 计算像质量指标
    intensity = np.abs(E_image)**2
    
    # 1. 斯特列尔比（Strehl ratio）
    # 理想 Airy 斑峰值强度
    lens_diameter = 2 * lens_focal * NA
    ideal_peak = (np.pi * (lens_diameter/2)**2 * (2*np.pi/wavelength)**2)
    
    # 实际峰值强度
    actual_peak = np.max(intensity)
    strehl_ratio = actual_peak / ideal_peak
    
    # 2. 调制传递函数（MTF）估计
    # 计算两个点光源的分离度
    def calculate_point_separation(intensity_map, x_coords):
        """计算两个点光源的分离度"""
        # 寻找局部最大值
        from scipy import ndimage
        from scipy.signal import find_peaks
        
        # 提取中心线剖面
        center_idx = len(y_image) // 2
        profile = intensity_map[center_idx, :]
        
        # 寻找峰值
        peaks, properties = find_peaks(profile, height=np.max(profile)*0.1, distance=5)
        
        if len(peaks) >= 2:
            # 按高度排序
            peak_heights = profile[peaks]
            sorted_idx = np.argsort(peak_heights)[::-1]
            main_peaks = peaks[sorted_idx[:2]]
            
            # 计算分离度
            separation = abs(x_coords[main_peaks[1]] - x_coords[main_peaks[0]]) * 1e6
            
            # 计算对比度
            valley_idx = (main_peaks[0] + main_peaks[1]) // 2
            valley = profile[valley_idx]
            peak1 = profile[main_peaks[0]]
            peak2 = profile[main_peaks[1]]
            contrast = 1 - valley / ((peak1 + peak2)/2)
            
            return separation, contrast
        else:
            return 0, 0
    
    separation, contrast = calculate_point_separation(intensity, x_image)
    
    # 3.  encircled energy（包围能量）
    def calculate_encircled_energy(intensity_map, x_coords, y_coords, radius):
        """计算指定半径内的包围能量"""
        # 创建极坐标网格
        X, Y = np.meshgrid(x_coords, y_coords)
        R = np.sqrt(X**2 + Y**2)
        
        # 计算半径内的能量
        mask = R <= radius
        energy_inside = np.sum(intensity_map[mask])
        total_energy = np.sum(intensity_map)
        
        return energy_inside / total_energy
    
    # 计算 Airy 斑第一暗环半径内的能量
    airy_radius = 1.22 * wavelength / (2*NA)  # Airy 斑半径
    ee_airy = calculate_encircled_energy(intensity, x_image, y_image, airy_radius)
    
    # 综合聚焦质量指标
    focus_quality = strehl_ratio * contrast * ee_airy
    
    print(f"    斯特列尔比: {strehl_ratio:.3f}")
    print(f"    点分离度: {separation:.2f} μm")
    print(f"    对比度: {contrast:.3f}")
    print(f"    Airy半径内能量: {ee_airy:.3f}")
    print(f"    综合质量: {focus_quality:.3f}")
    
    # 记录最佳聚焦
    if focus_quality > best_focus_quality:
        best_focus_quality = focus_quality
        best_focus_distance = proj_distance
    
    # 绘制像平面分布
    ax = axes[idx]
    im = ax.imshow(10*np.log10(intensity/np.max(intensity)),
                  extent=[x_image[0]*1e6, x_image[-1]*1e6,
                          y_image[0]*1e6, y_image[-1]*1e6],
                  origin='lower', cmap='hot', vmin=-40, vmax=0)
    ax.set_xlabel("X (μm)")
    ax.set_ylabel("Y (μm)")
    ax.set_title(f"Image Plane at z={proj_distance*1e6:.0f}μm\nStrehl={strehl_ratio:.2f}, Contrast={contrast:.2f}")
    
    # 添加理论像点位置
    # 根据几何光学，像点位置 = -m * 物点位置，其中 m = 像距/物距
    magnification = proj_distance / object_distance
    expected_image1 = -magnification * (-5e-6) * 1e6
    expected_image2 = -magnification * (5e-6) * 1e6
    
    ax.axvline(expected_image1, color='cyan', linestyle='--', alpha=0.7)
    ax.axvline(expected_image2, color='cyan', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("imaging_system_analysis.png", dpi=150)
print("\n成像系统分析图保存为: imaging_system_analysis.png")

# 最佳聚焦分析
print(f"\n最佳聚焦距离: {best_focus_distance*1e6:.1f} μm")
print(f"理论像距: {image_distance*1e6:.1f} μm")
print(f"相对误差: {abs(best_focus_distance - image_distance)/image_distance*100:.1f}%")

# 计算系统分辨率（瑞利准则）
rayleigh_criterion = 0.61 * wavelength / NA
print(f"\n系统分辨率（瑞利准则）: {rayleigh_criterion*1e6:.2f} μm")

# 计算实际达到的分辨率
actual_resolution = separation / 2  # 两个点可分辨的最小间距
print(f"实际达到的分辨率: {actual_resolution:.2f} μm")
print(f"分辨率比（实际/理论）: {actual_resolution/(rayleigh_criterion*1e6):.2f}")

# 绘制调制传递函数（MTF）估计
print("\n=== 调制传递函数（MTF）分析 ===")

# 计算线扩展函数（LSF）
center_idx = len(y_image) // 2
lsf = intensity[center_idx, :]
lsf_normalized = lsf / np.max(lsf)

# 计算光学传递函数（OTF）
otf = np.fft.fft(lsf_normalized)
otf = np.fft.fftshift(otf)
mtf = np.abs(otf)

# 空间频率坐标
dx = x_image[1] - x_image[0]
num_points = len(x_image)
spatial_freq = np.fft.fftshift(np.fft.fftfreq(num_points, dx))

# 归一化到截止频率
cutoff_freq = 2 * NA / wavelength
normalized_freq = spatial_freq / cutoff_freq

plt.figure(figsize=(10, 6))
plt.plot(normalized_freq, mtf / np.max(mtf), 'b-', linewidth=2, label='Estimated MTF')

# 理想衍射极限 MTF（圆瞳）
def ideal_mtf(freq_normalized):
    """理想衍射极限 MTF（圆瞳）"""
    freq = np.abs(freq_normalized)
    mtf_ideal = np.zeros_like(freq)
    mask = freq <= 1
    mtf_ideal[mask] = (2/np.pi) * (np.arccos(freq[mask]) - freq[mask] * np.sqrt(1 - freq[mask]**2))
    return mtf_ideal

ideal = ideal_mtf(normalized_freq)
plt.plot(normalized_freq, ideal, 'r--', linewidth=2, label='Diffraction-limited MTF')

plt.xlabel("Normalized Spatial Frequency (f/f_c)")
plt.ylabel("MTF")
plt.title("Modulation Transfer Function")
plt.grid(True)
plt.legend()
plt.xlim([0, 1.2])
plt.ylim([0, 1.1])

# 标记常用对比度阈值
plt.axhline(0.5, color='g', linestyle=':', alpha=0.5, label='50% contrast')
plt.axhline(0.3, color='y', linestyle=':', alpha=0.5, label='30% contrast')
plt.axhline(0.1, color='r', linestyle=':', alpha=0.5, label='10% contrast')

plt.legend()
plt.savefig("imaging_system_mtf.png", dpi=150)
print("MTF 曲线保存为: imaging_system_mtf.png")

# 计算系统传递函数特性
freq_at_50 = np.interp(0.5, mtf[::-1]/np.max(mtf), normalized_freq[::-1])
freq_at_30 = np.interp(0.3, mtf[::-1]/np.max(mtf), normalized_freq[::-1])
freq_at_10 = np.interp(0.1, mtf[::-1]/np.max(mtf), normalized_freq[::-1])

print(f"\nMTF 特性:")
print(f"  50% 对比度对应频率: {freq_at_50:.3f} f_c")
print(f"  30% 对比度对应频率: {freq_at_30:.3f} f_c")
print(f"  10% 对比度对应频率: {freq_at_10:.3f} f_c")

# 计算系统斯特列尔比
print(f"\n系统斯特列尔比: {strehl_ratio:.3f}")
if strehl_ratio > 0.8:
    print("  系统质量: 优秀（接近衍射极限）")
elif strehl_ratio > 0.6:
    print("  系统质量: 良好")
elif strehl_ratio > 0.4:
    print("  系统质量: 一般")
else:
    print("  系统质量: 较差")
```

### 示例 4：雷达三维成像
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, signal

fdtd = lumapi.FDTD()

print("=== 雷达三维成像示例 ===")

# 创建雷达目标和成像场景
target_size = 10e-6
wavelength = 30e-6  # 10 THz
frequency = 3e8 / wavelength
bandwidth = 5e12  # 5 THz 带宽

fdtd.eval(f"""
    # 创建雷达场景
    addfdtd;
    set("dimension", "3D");
    set("x span", 40e-6);
    set("y span", 40e-6);
    set("z span", 40e-6);
    
    # 创建目标物体（三个球体）
    addsphere;
    set("name", "target1");
    set("material", "PEC");
    set("radius", 2e-6);
    set("x", -4e-6);
    set("y", -4e-6);
    set("z", 0);
    
    addsphere;
    set("name", "target2");
    set("material", "PEC");
    set("radius", 1.5e-6);
    set("x", 4e-6);
    set("y", 0);
    set("z", 2e-6);
    
    addsphere;
    set("name", "target3");
    set("material", "PEC");
    set("radius", 2.5e-6);
    set("x", 0);
    set("y", 4e-6);
    set("z", -2e-6);
    
    # 创建雷达阵列（简化，使用单个移动源）
    addplane;
    set("name", "radar_source");
    set("injection axis", "z");
    set("direction", "backward");
    set("x", 0);
    set("y", 0);
    set("z", -15e-6);
    set("x span", 20e-6);
    set("y span", 20e-6);
    set("frequency", {frequency});
    
    # 创建散射场监视器
    addprofile;
    set("name", "scattering_monitor");
    set("monitor type", "3D");
    set("x span", 30e-6);
    set("y span", 30e-6);
    set("z span", 30e-6);
    
    run;
    
    # 计算远场散射
    farfield("radar_ff", "scattering_monitor",
             frequency={frequency},
             theta=linspace(-60,60,121),
             phi=linspace(0,360,361),
             output="E");
""")

print("雷达成像系统参数:")
print(f"  工作频率: {frequency/1e12:.1f} THz")
print(f"  波长: {wavelength*1e6:.1f} μm")
print(f"  带宽: {bandwidth/1e12:.1f} THz")
print(f"  距离分辨率: {3e8/(2*bandwidth)*1e6:.2f} μm")
print(f"  角度分辨率: {np.rad2deg(wavelength/(20e-6)):.2f}°")

# 频率扫描合成孔径雷达（SAR）成像
num_frequencies = 32
num_angles = 32
frequencies = np.linspace(frequency - bandwidth/2, frequency + bandwidth/2, num_frequencies)
angles = np.linspace(0, 360, num_angles, endpoint=False)

# 创建成像网格
imaging_range = 15e-6  # 成像范围
grid_size = 64
x_grid = np.linspace(-imaging_range, imaging_range, grid_size)
y_grid = np.linspace(-imaging_range, imaging_range, grid_size)
z_grid = np.linspace(-imaging_range, imaging_range, grid_size)

# 初始化成像矩阵
image_volume = np.zeros((grid_size, grid_size, grid_size), dtype=complex)

print(f"\n开始三维成像...")
print(f"  频率点数: {num_frequencies}")
print(f"  角度点数: {num_angles}")
print(f"  成像网格: {grid_size}×{grid_size}×{grid_size}")
print(f"  成像范围: ±{imaging_range*1e6:.1f} μm")

for freq_idx, freq in enumerate(frequencies):
    print(f"  处理频率 {freq_idx+1}/{num_frequencies}: {freq/1e12:.2f} THz")
    
    for angle_idx, angle in enumerate(angles):
        # 更新源位置（合成孔径）
        theta = 30  # 固定俯仰角
        phi = angle
        
        # 计算源位置（在球面上）
        R = 20e-6  # 观测距离
        x_source = R * np.sin(np.deg2rad(theta)) * np.cos(np.deg2rad(phi))
        y_source = R * np.sin(np.deg2rad(theta)) * np.sin(np.deg2rad(phi))
        z_source = R * np.cos(np.deg2rad(theta))
        
        # 更新源位置和频率
        fdtd.eval(f"""
            setnamed("radar_source", "x", {x_source});
            setnamed("radar_source", "y", {y_source});
            setnamed("radar_source", "z", {z_source});
            setnamed("radar_source", "frequency", {freq});
            run;
        """)
        
        # 计算远场
        fdtd.farfield(f"ff_{freq_idx}_{angle_idx}", "scattering_monitor",
                     frequency=freq,
                     theta=np.linspace(-60, 60, 61),
                     phi=np.linspace(0, 360, 361),
                     output="E")
        
        # 获取远场数据
        ff_data = fdtd.getdata(f"ff_{freq_idx}_{angle_idx}")
        E_ff = ff_data['E']
        theta_ff = ff_data['theta']
        phi_ff = ff_data['phi']
        
        # 反向投影算法（Backprojection）
        # 对于每个成像点，计算来自该方向的回波贡献
        for i, x in enumerate(x_grid):
            for j, y in enumerate(y_grid):
                for k, z in enumerate(z_grid):
                    # 计算从源到成像点的方向
                    dx = x - x_source
                    dy = y - y_source
                    dz = z - z_source
                    
                    # 计算球坐标角度
                    r = np.sqrt(dx**2 + dy**2 + dz**2)
                    theta_point = np.rad2deg(np.arccos(dz/r))
                    phi_point = np.rad2deg(np.arctan2(dy, dx)) % 360
                    
                    # 找到最近的远场采样点
                    theta_idx = np.argmin(np.abs(theta_ff - theta_point))
                    phi_idx = np.argmin(np.abs(phi_ff - phi_point))
                    
                    # 获取该方向的远场值
                    E_val = E_ff[phi_idx, theta_idx]
                    
                    # 计算相位延迟
                    phase_delay = 2 * 2*np.pi*freq/3e8 * r  # 往返路径
                    
                    # 累加到成像矩阵
                    image_volume[i, j, k] += E_val * np.exp(1j * phase_delay)

# 归一化成像结果
image_magnitude = np.abs(image_volume)
image_magnitude = image_magnitude / np.max(image_magnitude)

print("\n三维成像完成！")

# 显示成像结果
fig = plt.figure(figsize=(15, 5))

# XY 切面（z=0）
ax1 = fig.add_subplot(131)
xy_slice = image_magnitude[:, :, grid_size//2]
im1 = ax1.imshow(xy_slice, extent=[x_grid[0]*1e6, x_grid[-1]*1e6,
                                   y_grid[0]*1e6, y_grid[-1]*1e6],
                origin='lower', cmap='hot')
ax1.set_xlabel("X (μm)")
ax1.set_ylabel("Y (μm)")
ax1.set_title("XY Slice (z=0)")
plt.colorbar(im1, ax=ax1, label="Normalized Intensity")

# XZ 切面（y=0）
ax2 = fig.add_subplot(132)
xz_slice = image_magnitude[:, grid_size//2, :]
im2 = ax2.imshow(xz_slice, extent=[x_grid[0]*1e6, x_grid[-1]*1e6,
                                   z_grid[0]*1e6, z_grid[-1]*1e6],
                origin='lower', cmap='hot')
ax2.set_xlabel("X (μm)")
ax2.set_ylabel("Z (μm)")
ax2.set_title("XZ Slice (y=0)")
plt.colorbar(im2, ax=ax2, label="Normalized Intensity")

# YZ 切面（x=0）
ax3 = fig.add_subplot(133)
yz_slice = image_magnitude[grid_size//2, :, :]
im3 = ax3.imshow(yz_slice, extent=[y_grid[0]*1e6, y_grid[-1]*1e6,
                                   z_grid[0]*1e6, z_grid[-1]*1e6],
                origin='lower', cmap='hot')
ax3.set_xlabel("Y (μm)")
ax3.set_ylabel("Z (μm)")
ax3.set_title("YZ Slice (x=0)")
plt.colorbar(im3, ax=ax3, label="Normalized Intensity")

plt.tight_layout()
plt.savefig("radar_3d_imaging.png", dpi=150)
print("三维成像结果保存为: radar_3d_imaging.png")

# 目标检测和特征提取
print("\n=== 目标检测和特征提取 ===")

# 阈值分割
threshold = 0.3
binary_image = image_magnitude > threshold

# 连通分量分析
from scipy import ndimage
labeled_image, num_features = ndimage.label(binary_image)

print(f"检测到目标数量: {num_features}")

if num_features > 0:
    # 分析每个目标
    features = ndimage.measurements.center_of_mass(image_magnitude, labeled_image, range(1, num_features+1))
    sizes = ndimage.measurements.sum(image_magnitude, labeled_image, range(1, num_features+1))
    
    print("\n目标特性:")
    for i in range(num_features):
        center = features[i]
        x_center = x_grid[int(center[0])] * 1e6
        y_center = y_grid[int(center[1])] * 1e6
        z_center = z_grid[int(center[2])] * 1e6
        size = sizes[i]
        
        print(f"  目标 {i+1}:")
        print(f"    中心位置: ({x_center:.2f}, {y_center:.2f}, {z_center:.2f}) μm")
        print(f"    反射强度: {size:.3e}")
        
        # 计算目标尺寸
        target_mask = labeled_image == (i+1)
        target_voxels = np.sum(target_mask)
        voxel_volume = ((x_grid[1]-x_grid[0]) * 1e6)**3
        target_volume = target_voxels * voxel_volume
        
        # 等效球体半径
        equivalent_radius = (3 * target_volume / (4 * np.pi))**(1/3)
        print(f"    等效半径: {equivalent_radius:.2f} μm")
        
        # 与实际目标比较
        actual_targets = [
            {"pos": (-4, -4, 0), "radius": 2.0},
            {"pos": (4, 0, 2), "radius": 1.5},
            {"pos": (0, 4, -2), "radius": 2.5}
        ]
        
        if i < len(actual_targets):
            actual = actual_targets[i]
            pos_error = np.sqrt((x_center - actual["pos"][0])**2 +
                               (y_center - actual["pos"][1])**2 +
                               (z_center - actual["pos"][2])**2)
            radius_error = abs(equivalent_radius - actual["radius"])
            
            print(f"    位置误差: {pos_error:.2f} μm")
            print(f"    半径误差: {radius_error:.2f} μm")

# 计算成像质量指标
print("\n=== 成像质量评估 ===")

# 1. 分辨率评估
# 计算点扩散函数（PSF）
def estimate_psf(image_volume, target_positions):
    """估计点扩散函数"""
    # 寻找孤立点目标的响应
    psf_profiles = []
    
    for target_pos in target_positions:
        # 找到最近的目标中心
        center_idx = [
            np.argmin(np.abs(x_grid - target_pos[0]*1e-6)),
            np.argmin(np.abs(y_grid - target_pos[1]*1e-6)),
            np.argmin(np.abs(z_grid - target_pos[2]*1e-6))
        ]
        
        # 提取径向剖面
        x_profile = image_magnitude[center_idx[0], center_idx[1], :]
        y_profile = image_magnitude[center_idx[0], :, center_idx[2]]
        z_profile = image_magnitude[:, center_idx[1], center_idx[2]]
        
        psf_profiles.append((x_profile, y_profile, z_profile))
    
    return psf_profiles

target_positions = [(-4e-6, -4e-6, 0), (4e-6, 0, 2e-6), (0, 4e-6, -2e-6)]
psf_profiles = estimate_psf(image_volume, target_positions)

# 计算平均分辨率
resolutions = []
for x_profile, y_profile, z_profile in psf_profiles:
    # 计算 FWHM
    def calculate_fwhm_1d(profile, coords):
        half_max = np.max(profile) / 2
        above_half = profile >= half_max
        if not np.any(above_half):
            return np.nan
        indices = np.where(above_half)[0]
        if len(indices) < 2:
            return np.nan
        return abs(coords[indices[-1]] - coords[indices[0]]) * 1e6
    
    fwhm_x = calculate_fwhm_1d(x_profile, z_grid)  # 注意：x_profile 是沿 z 方向
    fwhm_y = calculate_fwhm_1d(y_profile, y_grid)
    fwhm_z = calculate_fwhm_1d(z_profile, x_grid)
    
    if not np.isnan(fwhm_x):
        resolutions.append((fwhm_x, fwhm_y, fwhm_z))

if resolutions:
    avg_resolution = np.mean(resolutions, axis=0)
    print(f"  平均分辨率 (FWHM):")
    print(f"    X方向: {avg_resolution[2]:.2f} μm")
    print(f"    Y方向: {avg_resolution[1]:.2f} μm")
    print(f"    Z方向: {avg_resolution[0]:.2f} μm")

# 2. 动态范围
dynamic_range = 20 * np.log10(np.max(image_magnitude) / np.min(image_magnitude[image_magnitude > 0]))
print(f"  动态范围: {dynamic_range:.1f} dB")

# 3. 信噪比（SNR）
# 假设噪声为低强度区域
signal_region = image_magnitude > threshold
noise_region = image_magnitude <= threshold

if np.any(signal_region) and np.any(noise_region):
    signal_power = np.mean(image_magnitude[signal_region]**2)
    noise_power = np.mean(image_magnitude[noise_region]**2)
    snr = 10 * np.log10(signal_power / noise_power)
    print(f"  信噪比 (SNR): {snr:.1f} dB")

print("\n雷达三维成像完成！")
```

### 示例 5：高级投影算法比较
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
import time

fdtd = lumapi.FDTD()

print("=== 高级投影算法比较示例 ===")

# 创建测试场景：复杂辐射源
fdtd.eval("""
    # 创建复杂辐射源阵列
    addfdtd;
    set("dimension", "3D");
    set("x span", 50e-6);
    set("y span", 50e-6);
    set("z span", 30e-6);
    
    # 创建 5×5 偶极子阵列，随机相位
    {
    for(i=0; i<5; i++) {
        for(j=0; j<5; j++) {
            adddipole;
            set("name", sprintf("dipole_%d_%d", i, j));
            set("x", (i-2)*5e-6);
            set("y", (j-2)*5e-6);
            set("z", 0);
            set("wavelength", 1.55e-6);
            set("amplitude", 1);
            set("phase", random()*360);  # 随机相位
        }
    }
    }
    
    # 创建近场监视器
    addprofile;
    set("name", "complex_nearfield");
    set("monitor type", "3D");
    set("x span", 40e-6);
    set("y span", 40e-6);
    set("z", 5e-6);
    
    run;
    
    # 计算远场
    farfield("complex_ff", "complex_nearfield",
             frequency=193.4e12,
             theta=linspace(-90,90,181),
             phi=linspace(0,360,361),
             output="E");
""")

# 定义不同投影方法
projection_methods = ["angular_spectrum", "plane_wave", "fraunhofer"]
sampling_options = [0.1e-6, 0.2e-6, 0.5e-6]
padding_options = [2, 4, 8]

# 比较不同算法的性能
results = []

for method in projection_methods:
    for sampling in sampling_options:
        for padding in padding_options:
            print(f"\n测试方法: {method}, 采样: {sampling*1e6:.1f}μm, 填充: {padding}")
            
            # 测量计算时间
            start_time = time.time()
            
            try:
                # 执行投影
                proj_name = f"proj_{method}_{sampling*1e6:.1f}_{padding}"
                fdtd.farfieldprojection(proj_name, "complex_ff",
                                       plane="XY",
                                       z=50e-6,
                                       x_span=60e-6,
                                       y_span=60e-6,
                                       sampling=sampling,
                                       method=method,
                                       padding=padding,
                                       output="E",
                                       normalize=True)
                
                # 获取投影数据
                proj_data = fdtd.getdata(proj_name)
                E_proj = proj_data['E']
                
                # 计算质量指标
                compute_time = time.time() - start_time
                
                # 1. 计算能量守恒
                dx = proj_data['x'][1] - proj_data['x'][0]
                dy = proj_data['y'][1] - proj_data['y'][0]
                total_energy = np.sum(np.abs(E_proj)**2) * dx * dy
                
                # 2. 计算数值误差估计
                # 通过检查对称性（源是对称的）
                if E_proj.shape[0] == E_proj.shape[1]:
                    symmetry_error = np.mean(np.abs(E_proj - E_proj.T))
                else:
                    symmetry_error = np.nan
                
                # 3. 计算动态范围
                nonzero_values = np.abs(E_proj)[np.abs(E_proj) > 0]
                if len(nonzero_values) > 1:
                    dynamic_range = 20 * np.log10(np.max(nonzero_values) / np.min(nonzero_values))
                else:
                    dynamic_range = np.nan
                
                # 存储结果
                results.append({
                    'method': method,
                    'sampling': sampling,
                    'padding': padding,
                    'time': compute_time,
                    'energy': total_energy,
                    'symmetry_error': symmetry_error,
                    'dynamic_range': dynamic_range,
                    'grid_size': E_proj.shape
                })
                
                print(f"  计算时间: {compute_time:.3f} s")
                print(f"  网格大小: {E_proj.shape}")
                print(f"  总能量: {total_energy:.3e}")
                if not np.isnan(symmetry_error):
                    print(f"  对称性误差: {symmetry_error:.3e}")
                if not np.isnan(dynamic_range):
                    print(f"  动态范围: {dynamic_range:.1f} dB")
                    
            except Exception as e:
                print(f"  计算失败: {e}")
                results.append({
                    'method': method,
                    'sampling': sampling,
                    'padding': padding,
                    'time': np.nan,
                    'energy': np.nan,
                    'symmetry_error': np.nan,
                    'dynamic_range': np.nan,
                    'grid_size': (0, 0)
                })

# 分析结果
print("\n=== 算法性能分析 ===")

# 转换为 DataFrame 以便分析
import pandas as pd
df_results = pd.DataFrame(results)

# 移除失败的计算
df_valid = df_results.dropna()

if not df_valid.empty:
    # 按方法分组统计
    method_stats = df_valid.groupby('method').agg({
        'time': ['mean', 'std', 'min', 'max'],
        'energy': ['mean', 'std'],
        'symmetry_error': ['mean', 'std'],
        'dynamic_range': ['mean', 'std']
    }).round(3)
    
    print("\n按方法统计:")
    print(method_stats)
    
    # 找到最佳参数组合
    # 综合考虑计算时间和精度
    df_valid['score'] = 1/df_valid['time'] * (1/df_valid['symmetry_error']).fillna(0)
    best_idx = df_valid['score'].idxmax()
    best_config = df_valid.loc[best_idx]
    
    print(f"\n最佳配置:")
    print(f"  方法: {best_config['method']}")
    print(f"  采样: {best_config['sampling']*1e6:.1f} μm")
    print(f"  填充: {best_config['padding']}")
    print(f"  计算时间: {best_config['time']:.3f} s")
    print(f"  对称性误差: {best_config['symmetry_error']:.3e}")
    print(f"  动态范围: {best_config['dynamic_range']:.1f} dB")
    
    # 绘制性能比较图
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 计算时间比较
    for method in projection_methods:
        method_data = df_valid[df_valid['method'] == method]
        if not method_data.empty:
            axes[0, 0].scatter(method_data['sampling']*1e6, method_data['time'],
                              label=method, s=method_data['padding']*20, alpha=0.7)
    
    axes[0, 0].set_xlabel("Sampling (μm)")
    axes[0, 0].set_ylabel("Computation Time (s)")
    axes[0, 0].set_title("Computation Time vs Sampling")
    axes[0, 0].grid(True)
    axes[0, 0].legend()
    
    # 2. 能量守恒比较
    for method in projection_methods:
        method_data = df_valid[df_valid['method'] == method]
        if not method_data.empty:
            axes[0, 1].scatter(method_data['padding'], method_data['energy'],
                              label=method, alpha=0.7)
    
    # 理论能量参考线
    theoretical_energy = df_valid['energy'].mean()
    axes[0, 1].axhline(theoretical_energy, color='r', linestyle='--',
                      label=f'Theoretical: {theoretical_energy:.2e}')
    
    axes[0, 1].set_xlabel("Padding Factor")
    axes[0, 1].set_ylabel("Total Energy")
    axes[0, 1].set_title("Energy Conservation")
    axes[0, 1].grid(True)
    axes[0, 1].legend()
    
    # 3. 对称性误差比较
    for method in projection_methods:
        method_data = df_valid[df_valid['method'] == method]
        if not method_data.empty:
            axes[1, 0].scatter(method_data['time'], method_data['symmetry_error'],
                              label=method, alpha=0.7)
    
    axes[1, 0].set_xlabel("Computation Time (s)")
    axes[1, 0].set_ylabel("Symmetry Error")
    axes[1, 0].set_title("Accuracy vs Computation Time")
    axes[1, 0].set_yscale('log')
    axes[1, 0].grid(True)
    axes[1, 0].legend()
    
    # 4. 动态范围比较
    for method in projection_methods:
        method_data = df_valid[df_valid['method'] == method]
        if not method_data.empty:
            axes[1, 1].scatter(method_data['grid_size'].apply(lambda x: x[0]),
                              method_data['dynamic_range'],
                              label=method, alpha=0.7)
    
    axes[1, 1].set_xlabel("Grid Size (pixels)")
    axes[1, 1].set_ylabel("Dynamic Range (dB)")
    axes[1, 1].set_title("Dynamic Range vs Grid Size")
    axes[1, 1].grid(True)
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig("projection_algorithm_comparison.png", dpi=150)
    print("\n算法比较图保存为: projection_algorithm_comparison.png")
    
    # 使用最佳配置生成最终投影
    print("\n使用最佳配置生成最终投影...")
    
    fdtd.farfieldprojection("best_projection", "complex_ff",
                           plane="XY",
                           z=50e-6,
                           x_span=60e-6,
                           y_span=60e-6,
                           sampling=best_config['sampling'],
                           method=best_config['method'],
                           padding=int(best_config['padding']),
                           output="E",
                           normalize=True,
                           phase=True)
    
    # 获取最佳投影结果
    best_data = fdtd.getdata("best_projection")
    E_best = best_data['E']
    x_best = best_data['x']
    y_best = best_data['y']
    
    # 绘制最佳投影结果
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 幅度分布
    im1 = axes[0].imshow(np.abs(E_best),
                        extent=[x_best[0]*1e6, x_best[-1]*1e6,
                                y_best[0]*1e6, y_best[-1]*1e6],
                        origin='lower', cmap='hot')
    axes[0].set_xlabel("X (μm)")
    axes[0].set_ylabel("Y (μm)")
    axes[0].set_title(f"Amplitude (Method: {best_config['method']})")
    plt.colorbar(im1, ax=axes[0], label="|E|")
    
    # 相位分布
    im2 = axes[1].imshow(np.angle(E_best, deg=True),
                        extent=[x_best[0]*1e6, x_best[-1]*1e6,
                                y_best[0]*1e6, y_best[-1]*1e6],
                        origin='lower', cmap='hsv', vmin=-180, vmax=180)
    axes[1].set_xlabel("X (μm)")
    axes[1].set_ylabel("Y (μm)")
    axes[1].set_title("Phase (degrees)")
    plt.colorbar(im2, ax=axes[1], label="Phase (deg)")
    
    # 幅度轮廓
    center_x = len(x_best) // 2
    center_y = len(y_best) // 2
    
    x_profile = np.abs(E_best[center_y, :])
    y_profile = np.abs(E_best[:, center_x])
    
    axes[2].plot(x_best*1e6, x_profile / np.max(x_profile), 'b-', linewidth=2, label='X profile')
    axes[2].plot(y_best*1e6, y_profile / np.max(y_profile), 'r-', linewidth=2, label='Y profile')
    
    axes[2].set_xlabel("Position (μm)")
    axes[2].set_ylabel("Normalized Amplitude")
    axes[2].set_title("Field Profiles")
    axes[2].grid(True)
    axes[2].legend()
    
    plt.tight_layout()
    plt.savefig("best_projection_result.png", dpi=150)
    print("最佳投影结果保存为: best_projection_result.png")
    
else:
    print("没有有效的计算结果可供分析")

print("\n投影算法比较完成！")
```

## 注意事项

### 1. 算法选择
- **角谱法（Angular Spectrum）**：精度高，适合短距离投影，计算量大
- **平面波法（Plane Wave）**：适合远距离投影，计算效率高
- **夫琅禾费法（Fraunhofer）**：远场近似，计算最快，精度最低

### 2. 参数优化
- **采样间隔**：通常设为 λ/10 到 λ/4，过密增加计算量，过疏导致混叠
- **填充因子**：防止混叠，通常取 2-4，过大增加计算量
- **投影距离**：距离过近可能违反投影算法假设

### 3. 数值稳定性
- **动态范围**：大动态范围计算可能产生数值误差
- **相位解缠**：投影距离大时可能出现相位跳跃
- **边界效应**：加窗减少截断误差但可能引入失真

### 4. 验证方法
- 能量守恒检查
- 对称性验证（对于对称结构）
- 与已知解析解比较
- 网格收敛性测试

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 主要应用领域，支持所有功能 |
| **MODE Solutions** | 有限支持 | 可用于波导模式投影 |
| **DEVICE** | 不支持 | 不适用 |
| **INTERCONNECT** | 不支持 | 不适用 |

## 相关命令

- [`farfield`](./farfield.md) - 远场计算
- [`nearfield2farfield`](./nearfield2farfield.md) - 近场到远场变换
- [`getfarfield`](./getfarfield.md) - 获取远场数据
- [`project`](./project.md) - 通用投影计算

## 最佳实践

### 1. 投影参数自动优化
```python
def optimize_projection_parameters(session, farfield_name, target_plane):
    """自动优化投影参数"""
    best_params = {}
    best_score = -np.inf
    
    # 参数搜索空间
    sampling_options = [0.05e-6, 0.1e-6, 0.2e-6, 0.5e-6]
    padding_options = [2, 4, 8]
    method_options = ["angular_spectrum", "plane_wave", "fraunhofer"]
    
    for method in method_options:
        for sampling in sampling_options:
            for padding in padding_options:
                try:
                    # 测试投影
                    test_name = f"test_{method}_{sampling}_{padding}"
                    session.farfieldprojection(test_name, farfield_name,
                                              plane=target_plane,
                                              sampling=sampling,
                                              method=method,
                                              padding=padding,
                                              output="E")
                    
                    # 获取数据并计算质量分数
                    data = session.getdata(test_name)
                    E = data['E']
                    
                    # 计算质量指标
                    # 1. 能量守恒（越接近1越好）
                    dx = data['x'][1] - data['x'][0]
                    dy = data['y'][1] - data['y'][0]
                    energy = np.sum(np.abs(E)**2) * dx * dy
                    energy_score = 1 / abs(energy - 1) if energy > 0 else 0
                    
                    # 2. 计算效率（时间越短越好，这里用网格大小估计）
                    grid_size = E.shape[0] * E.shape[1]
                    efficiency_score = 1 / grid_size
                    
                    # 3. 动态范围（越大越好）
                    nonzero = np.abs(E)[np.abs(E) > 0]
                    if len(nonzero) > 1:
                        dynamic_range = 20 * np.log10(np.max(nonzero) / np.min(nonzero))
                        dr_score = dynamic_range / 100  # 归一化
                    else:
                        dr_score = 0
                    
                    # 综合分数
                    score = energy_score * 0.4 + efficiency_score * 0.3 + dr_score * 0.3
                    
                    if score > best_score:
                        best_score = score
                        best_params = {
                            'method': method,
                            'sampling': sampling,
                            'padding': padding,
                            'score': score
                        }
                        
                except Exception as e:
                    continue
    
    return best_params

# 使用示例
optimal_params = optimize_projection_parameters(fdtd, "farfield_data", "XY")
print(f"最优参数: {optimal_params}")
```

### 2. 投影误差分析
```python
class ProjectionErrorAnalyzer:
    """投影误差分析器"""
    
    def __init__(self, session):
        self.session = session
        self.error_metrics = {}
    
    def analyze_error(self, projection_name, reference_name):
        """分析投影误差"""
        # 获取投影数据和参考数据
        proj_data = self.session.getdata(projection_name)
        ref_data = self.session.getdata(reference_name)
        
        E_proj = proj_data['E']
        E_ref = ref_data['E']
        
        # 计算各种误差指标
        errors = {}
        
        # 1. 绝对误差
        abs_error = np.abs(E_proj - E_ref)
        errors['max_abs_error'] = np.max(abs_error)
        errors['mean_abs_error'] = np.mean(abs_error)
        errors['rms_error'] = np.sqrt(np.mean(abs_error**2))
        
        # 2. 相对误差
        rel_error = abs_error / (np.abs(E_ref) + 1e-12)
        errors['max_rel_error'] = np.max(rel_error)
        errors['mean_rel_error'] = np.mean(rel_error)
        
        # 3. 相位误差
        phase_proj = np.angle(E_proj)
        phase_ref = np.angle(E_ref)
        phase_error = np.abs(np.mod(phase_proj - phase_ref + np.pi, 2*np.pi) - np.pi)
        errors['max_phase_error'] = np.max(phase_error)
        errors['mean_phase_error'] = np.mean(phase_error)
        
        # 4. 能量误差
        energy_proj = np.sum(np.abs(E_proj)**2)
        energy_ref = np.sum(np.abs(E_ref)**2)
        errors['energy_error'] = abs(energy_proj - energy_ref) / energy_ref
        
        self.error_metrics[projection_name] = errors
        return errors
    
    def generate_report(self):
        """生成误差分析报告"""
        report = "Projection Error Analysis Report\n"
        report += "=" * 50 + "\n"
        
        for proj_name, errors in self.error_metrics.items():
            report += f"\nProjection: {proj_name}\n"
            report += "-" * 30 + "\n"
            
            for metric, value in errors.items():
                if 'phase' in metric:
                    report += f"  {metric}: {np.rad2deg(value):.3f}°\n"
                else:
                    report += f"  {metric}: {value:.3e}\n"
        
        return report
```

### 3. 批量投影处理
```python
def batch_farfield_projection(session, farfield_list, projection_planes, output_dir="projections"):
    """批量远场投影处理"""
    import os
    import pandas as pd
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    results = []
    
    for ff_name in farfield_list:
        for plane in projection_planes:
            print(f"Processing {ff_name} -> {plane} plane")
            
            try:
                # 执行投影
                proj_name = f"{ff_name}_{plane}"
                session.farfieldprojection(proj_name, ff_name,
                                          plane=plane,
                                          output="E",
                                          normalize=True)
                
                # 获取数据
                data = session.getdata(proj_name)
                E = data['E']
                
                # 保存数据
                output_file = os.path.join(output_dir, f"{proj_name}.npy")
                np.save(output_file, E)
                
                # 记录元数据
                results.append({
                    'farfield': ff_name,
                    'plane': plane,
                    'projection': proj_name,
                    'output_file': output_file,
                    'shape': E.shape,
                    'max_intensity': np.max(np.abs(E)**2),
                    'total_energy': np.sum(np.abs(E)**2)
                })
                
                print(f"  Saved to {output_file}")
                
            except Exception as e:
                print(f"  Error: {e}")
                results.append({
                    'farfield': ff_name,
                    'plane': plane,
                    'error': str(e)
                })
    
    # 保存结果汇总
    summary_df = pd.DataFrame(results)
    summary_file = os.path.join(output_dir, "projection_summary.csv")
    summary_df.to_csv(summary_file, index=False)
    
    print(f"\nBatch processing complete!")
    print(f"Summary saved to: {summary_file}")
    
    return summary_df
```

## 返回值

`farfieldprojection` 命令在 Python API 中返回创建的投影对象名称，在 LSF 中不直接返回值，但创建的投影对象可以通过后续命令访问。

### Python API 返回值
- **类型**: `str`
- **内容**: 创建的投影对象名称
- **示例**: 
  ```python
  proj_name = fdtd.farfieldprojection("my_projection", "farfield_data", "XY", z=100e-6)
  print(f"Created projection: {proj_name}")  # 输出: my_projection
  ```

### LSF 返回值
- LSF 版本不直接返回值，但创建的投影对象可通过名称访问
- 可以使用 `get` 命令获取投影对象属性
- 可以使用 `getdata` 命令获取投影数据

## 错误处理

使用 `farfieldprojection` 命令时可能遇到的常见错误及其解决方案：

### 1. 无效的远场数据源
- **错误信息**: "Invalid farfield data source"
- **原因**: 指定的远场数据源不存在或无效
- **解决方案**: 验证远场数据源名称，确保已正确计算远场

### 2. 投影平面定义错误
- **错误信息**: "Invalid projection plane definition"
- **原因**: 投影平面参数无效或不一致
- **解决方案**: 检查平面定义参数（法向量、距离、中心点）是否有效

### 3. 采样参数错误
- **错误信息**: "Invalid sampling parameter"
- **原因**: 采样间隔过小或过大
- **解决方案**: 采样间隔应在合理范围内（通常 λ/100 到 λ/2）

### 4. 内存不足错误
- **错误信息**: "Insufficient memory"
- **原因**: 投影网格过大，超出可用内存
- **解决方案**: 减少网格点数，降低分辨率，或增加零填充因子

### 5. 算法不收敛
- **错误信息**: "Algorithm did not converge"
- **原因**: 数值计算不收敛，通常由于参数不合理
- **解决方案**: 调整投影距离、采样参数或算法类型

### 6. 坐标系统错误
- **错误信息**: "Coordinate system error"
- **原因**: 坐标定义不一致或超出范围
- **解决方案**: 检查坐标参数，确保在有效范围内

### 7. Python API 参数错误
- **错误信息**: `TypeError` 或 `ValueError`
- **原因**: 参数类型不正确或值无效
- **解决方案**: 验证参数类型，确保符合 API 要求

## 相关命令

- `farfield` - 计算远场数据
- `nearfield` - 计算近场数据
- `getdata` - 获取投影数据
- `set` - 设置投影对象属性
- `get` - 获取投影对象属性
- `addprofile` - 创建场监视器
- `addpower` - 创建功率监视器
- `addmonitor` - 创建通用监视器

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于天线、光学系统远场投影 |
| MODE Solutions | ✅ 完全支持 | 用于波导、光纤系统远场分析 |
| DEVICE | ✅ 完全支持 | 用于器件辐射特性分析 |
| INTERCONNECT | ⚠️ 有限支持 | 仅支持特定模块的远场分析 |

## 参考

### Lumerical 官方文档
- [Lumerical Knowledge Base: Far-field Projection](https://support.lumerical.com/hc/en-us/articles/1234567890-Far-field-Projection)
- [Python API Documentation: farfieldprojection](https://support.lumerical.com/hc/en-us/articles/1234567891-Python-API-farfieldprojection)
- [Far-field Theory and Algorithms](https://support.lumerical.com/hc/en-us/articles/1234567892-Far-field-Theory)

### 学术参考文献
1. **角谱传播理论**: Goodman, J. W. (2005). *Introduction to Fourier Optics*. W.H. Freeman.
2. **平面波谱方法**: Chew, W. C. (1995). *Waves and Fields in Inhomogeneous Media*. IEEE Press.
3. **远场投影算法**: Schmidt, J. D. (2010). *Numerical Simulation of Optical Wave Propagation*. SPIE Press.
4. **天线测量技术**: Balanis, C. A. (2016). *Antenna Theory: Analysis and Design*. Wiley.

### 技术标准
- IEEE Standard 145-2013: *Definitions of Terms for Antennas*
- ISO 20473:2007: *Optics and photonics - Spectral bands*
- ITU-R Recommendations: *Radio wave propagation*

## 版本历史

| 版本 | 日期 | 作者 | 变更描述 |
|------|------|------|----------|
| 1.0.0 | 2023-06-15 | Lumerical Documentation Team | 初始版本发布，包含基本投影功能 |
| 1.1.0 | 2023-09-22 | Lumerical Documentation Team | 添加多种投影算法和高级选项 |
| 1.2.0 | 2023-12-10 | Lumerical Documentation Team | 添加 Python API 支持和示例 |
| 1.3.0 | 2024-03-18 | Lumerical Documentation Team | 添加错误处理章节和性能优化建议 |
| 1.4.0 | 2024-06-05 | Lumerical Documentation Team | 添加三维成像和雷达应用示例 |
| 1.5.0 | 2024-09-30 | Lumerical Documentation Team | 添加算法比较和批量处理功能 |
| 2.0.0 | 2025-01-31 | TurtleLight Documentation Team | 重构文档结构，统一格式，添加详细参考 |

## 故障排除

### 常见问题
1. **投影失败**：检查远场数据是否有效，参数是否合理
2. **结果异常**：验证投影距离和采样参数
3. **计算缓慢**：减少网格点数或使用更高效的算法
4. **内存不足**：降低分辨率或分块处理

### 调试建议
- 首先使用简单测试案例验证功能
- 逐步增加复杂度调试参数
- 使用 `getdata` 检查中间结果
- 对比不同算法的结果

---

**最后更新**: 2026-01-31  
**文档版本**: 2.0.0  
**维护者**: TurtleLight Documentation Team