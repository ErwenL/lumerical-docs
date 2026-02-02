# fdtdanalysis - FDTD 分析设置

## 概述

`fdtdanalysis` 命令用于配置和管理 FDTD 仿真的分析参数，包括频率范围、边界条件、网格设置、激励源配置和结果输出选项。这是 FDTD 仿真工作流中的核心命令，直接影响仿真精度、计算效率和结果可靠性。

### 主要功能
- **频率设置**：定义仿真频率范围、采样点和宽带分析参数
- **边界条件**：配置吸收边界条件（ABC）、完美匹配层（PML）和周期边界
- **网格控制**：设置自动网格、手动覆盖区和网格细化规则
- **激励管理**：配置源类型、位置、方向和时域/频域特性
- **监视器设置**：定义场监视器、功率监视器、模式扩展监视器等
- **求解器控制**：设置仿真时间、稳定性条件和收敛判据

### 分析流程
1. **预处理**：定义仿真几何和材料
2. **分析设置**：使用 `fdtdanalysis` 配置求解参数
3. **运行仿真**：执行 FDTD 时域迭代
4. **后处理**：提取频域结果和场分布
5. **验证**：检查收敛性和数值误差

### 典型应用场景
1. **宽带响应分析**：计算器件在宽频率范围内的响应
2. **模式分析**：提取波导模式特性
3. **散射参数计算**：计算 S 参数和传输特性
4. **场分布可视化**：获取空间场分布
5. **优化设计**：参数扫描和优化循环

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
fdtdanalysis(name, options);

# 配置频率分析
fdtdanalysis("analysis1",
            "frequency points", 100,
            "frequency start", 100e12,
            "frequency stop", 500e12,
            "analysis type", "standard");

# 配置高级选项
fdtdanalysis("advanced_analysis",
            "boundary conditions", "PML",
            "pml layers", 16,
            "pml reflection", 1e-8,
            "mesh type", "auto non-uniform",
            "mesh accuracy", 2,
            "simulation time", 1000e-15);
```

### Python API (Lumapi)
```python
# 基本调用
session.fdtdanalysis("name", **options)

# 配置频率分析
session.fdtdanalysis("analysis1",
                    frequency_points=100,
                    frequency_start=100e12,
                    frequency_stop=500e12,
                    analysis_type="standard")

# 使用字典传递选项
options = {
    "boundary_conditions": "PML",
    "pml_layers": 16,
    "pml_reflection": 1e-8,
    "mesh_type": "auto non-uniform",
    "mesh_accuracy": 2,
    "simulation_time": 1000e-15
}
session.fdtdanalysis("advanced_analysis", **options)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `name` | 字符串 | 是 | 无 | 分析设置名称 |
| `options` | 键值对 | 否 | 无 | 分析选项（见下表） |

## 分析选项

### 频率设置
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"frequency points"` | 整数 | 100 | 频率采样点数 |
| `"frequency start"` | 数值 | `f_min` | 起始频率（Hz） |
| `"frequency stop"` | 数值 | `f_max` | 终止频率（Hz） |
| `"frequency center"` | 数值 | 自动 | 中心频率（Hz） |
| `"frequency span"` | 数值 | 自动 | 频率跨度（Hz） |
| `"frequency scale"` | 字符串 | `"linear"` | 频率刻度：`"linear"`, `"log"` |
| `"analysis type"` | 字符串 | `"standard"` | 分析类型：`"standard"`, `"broadband"`, `"pulsed"` |

### 边界条件
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"boundary conditions"` | 字符串 | `"PML"` | 边界类型：`"PML"`, `"metal"`, `"periodic"`, `"symmetric"` |
| `"pml layers"` | 整数 | 8 | PML 层数 |
| `"pml reflection"` | 数值 | 1e-6 | PML 反射系数 |
| `"pml type"` | 字符串 | `"standard"` | PML 类型：`"standard"`, `"stretched"`, `"graded"` |
| `"x min bc"` | 字符串 | `"PML"` | X 负方向边界条件 |
| `"x max bc"` | 字符串 | `"PML"` | X 正方向边界条件 |
| `"y min bc"` | 字符串 | `"PML"` | Y 负方向边界条件 |
| `"y max bc"` | 字符串 | `"PML"` | Y 正方向边界条件 |
| `"z min bc"` | 字符串 | `"PML"` | Z 负方向边界条件 |
| `"z max bc"` | 字符串 | `"PML"` | Z 正方向边界条件 |

### 网格设置
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"mesh type"` | 字符串 | `"auto"` | 网格类型：`"auto"`, `"uniform"`, `"manual"` |
| `"mesh accuracy"` | 整数 | 2 | 网格精度（1-8） |
| `"mesh refinement"` | 字符串 | `"conformal"` | 网格细化：`"conformal"`, `"staircase"` |
| `"dx"` | 数值 | 自动 | X 方向网格步长 |
| `"dy"` | 数值 | 自动 | Y 方向网格步长 |
| `"dz"` | 数值 | 自动 | Z 方向网格步长 |
| `"min mesh step"` | 数值 | λ/20 | 最小网格步长 |
| `"max mesh step"` | 数值 | λ/5 | 最大网格步长 |
| `"mesh override regions"` | 数组 | 无 | 手动网格覆盖区 |

### 求解器控制
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"simulation time"` | 数值 | 自动 | 仿真时间（秒） |
| `"time step"` | 数值 | CFL 限制 | 时间步长（秒） |
| `"courant factor"` | 数值 | 0.99 | CFL 数（稳定性因子） |
| `"stability factor"` | 数值 | 1.0 | 稳定性因子 |
| `"auto shutoff"` | 数值 | 1e-5 | 自动停止判据 |
| `"max iterations"` | 整数 | 10000 | 最大迭代次数 |
| `"convergence test"` | 布尔 | `true` | 收敛性测试 |
| `"convergence tolerance"` | 数值 | 1e-3 | 收敛容差 |

### 激励源设置
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"source type"` | 字符串 | `"total-field"` | 源类型：`"total-field"`, `"scattered-field"` |
| `"source mode"` | 字符串 | `"fundamental"` | 源模式：`"fundamental"`, `"user-defined"` |
| `"source polarization"` | 字符串 | `"TE"` | 源偏振：`"TE"`, `"TM"`, `"custom"` |
| `"source amplitude"` | 数值 | 1.0 | 源振幅 |
| `"source phase"` | 数值 | 0.0 | 源相位（度） |
| `"source position"` | 数组 | `[0,0,0]` | 源位置 [x,y,z] |
| `"source direction"` | 数组 | `[0,0,1]` | 源方向矢量 |
| `"source frequency"` | 数值 | 中心频率 | 源频率（Hz） |

### 输出设置
| 选项 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"output frequency points"` | 整数 | 50 | 输出频率点数 |
| `"output field components"` | 字符串 | `"all"` | 输出场分量：`"all"`, `"Ex"`, `"Ey"`, `"Ez"`, `"Hx"`, `"Hy"`, `"Hz"` |
| `"output normalization"` | 布尔 | `true` | 输出归一化 |
| `"output format"` | 字符串 | `"matlab"` | 输出格式：`"matlab"`, `"csv"`, `"hdf5"` |
| `"save fields"` | 布尔 | `false` | 保存场数据 |
| `"save frequency data"` | 布尔 | `true` | 保存频域数据 |
| `"save simulation data"` | 布尔 | `true` | 保存仿真数据 |

## 配置属性

分析设置对象创建后，可通过 `set` 命令配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `"frequency points"` | 整数 | 100 | 频率点数 |
| `"frequency start"` | 数值 | 自动 | 起始频率 |
| `"frequency stop"` | 数值 | 自动 | 终止频率 |
| `"boundary conditions"` | 字符串 | `"PML"` | 边界条件 |
| `"pml layers"` | 整数 | 8 | PML 层数 |
| `"mesh accuracy"` | 整数 | 2 | 网格精度 |
| `"mesh type"` | 字符串 | `"auto"` | 网格类型 |
| `"simulation time"` | 数值 | 自动 | 仿真时间 |
| `"auto shutoff"` | 数值 | 1e-5 | 自动停止判据 |
| `"source type"` | 字符串 | `"total-field"` | 源类型 |
| `"source polarization"` | 字符串 | `"TE"` | 源偏振 |
| `"output frequency points"` | 整数 | 50 | 输出频率点数 |
| `"save fields"` | 布尔 | `false` | 保存场数据 |
| `"analysis type"` | 字符串 | `"standard"` | 分析类型 |
| `"convergence test"` | 布尔 | `true` | 收敛性测试 |

## 使用示例

### 示例 1：基本 FDTD 分析设置
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("=== 基本 FDTD 分析设置示例 ===")

# 创建简单波导结构
fdtd.eval("""
    # 创建 FDTD 求解器
    addfdtd;
    set("dimension", "3D");
    set("x span", 10e-6);
    set("y span", 10e-6);
    set("z span", 5e-6);
    
    # 创建硅波导
    addrect;
    set("name", "waveguide");
    set("material", "Si (Silicon) - Palik");
    set("x span", 500e-9);
    set("y span", 220e-9);
    set("z span", 10e-6);
    
    # 创建模式源
    addmode;
    set("name", "source");
    set("injection axis", "z");
    set("mode selection", "fundamental TE mode");
    
    # 创建功率监视器
    addpower;
    set("name", "transmission");
    set("monitor type", "2D Z-normal");
    set("z", 9e-6);
""")

# 配置 FDTD 分析
print("配置 FDTD 分析参数...")

fdtd.fdtdanalysis("basic_analysis",
                 frequency_points=200,
                 frequency_start=150e12,    # 2μm
                 frequency_stop=300e12,     # 1μm
                 frequency_scale="linear",
                 boundary_conditions="PML",
                 pml_layers=12,
                 pml_reflection=1e-8,
                 mesh_type="auto non-uniform",
                 mesh_accuracy=3,
                 mesh_refinement="conformal",
                 simulation_time=2000e-15,
                 auto_shutoff=1e-5,
                 courant_factor=0.99,
                 source_type="total-field",
                 source_polarization="TE",
                 output_frequency_points=100,
                 save_fields=False,
                 save_frequency_data=True,
                 analysis_type="standard")

# 运行分析
print("运行 FDTD 分析...")
fdtd.eval("""
    # 应用分析设置
    select("FDTD");
    setanalysis("basic_analysis");
    
    # 运行仿真
    run;
    
    # 获取传输结果
    T = transmission("transmission");
    f = getdata("transmission", "f");
""")

# 获取结果
freq_data = fdtd.getdata("transmission", "f")
transmission_data = fdtd.getdata("transmission", "T")

if freq_data is not None and transmission_data is not None:
    frequencies = freq_data.flatten()
    transmission = transmission_data.flatten()
    
    print(f"\n分析结果:")
    print(f"  频率点数: {len(frequencies)}")
    print(f"  频率范围: {frequencies[0]/1e12:.1f} - {frequencies[-1]/1e12:.1f} THz")
    print(f"  传输范围: {np.min(transmission):.4f} - {np.max(transmission):.4f}")
    
    # 找到最大传输频率
    max_idx = np.argmax(transmission)
    f_max = frequencies[max_idx]
    T_max = transmission[max_idx]
    
    print(f"  最大传输: {T_max:.4f} at {f_max/1e12:.2f} THz (λ={3e8/f_max*1e9:.1f} nm)")
    
    # 计算 3dB 带宽
    half_max = T_max / 2
    above_half = transmission >= half_max
    
    if np.any(above_half):
        idx = np.where(above_half)[0]
        f_low = frequencies[idx[0]]
        f_high = frequencies[idx[-1]]
        bandwidth = f_high - f_low
        
        print(f"  3dB 带宽: {bandwidth/1e12:.2f} THz")
        print(f"  3dB 范围: {f_low/1e12:.2f} - {f_high/1e12:.2f} THz")
else:
    print("错误: 无法获取结果数据")

# 检查收敛性
convergence = fdtd.eval("getnamed('FDTD', 'percent done');")
if convergence is not None:
    print(f"  收敛状态: {convergence:.1f}%")

# 获取仿真统计信息
stats = fdtd.eval("""
    stats = [];
    stats.mesh_cells = getnamed('FDTD', 'mesh cells');
    stats.simulation_time = getnamed('FDTD', 'simulation time');
    stats.memory_used = getnamed('FDTD', 'memory used');
    stats;
""")

if stats is not None:
    print(f"\n仿真统计:")
    print(f"  网格单元数: {stats.get('mesh_cells', 'N/A'):,}")
    print(f"  仿真时间: {stats.get('simulation_time', 'N/A'):.2f} s")
    print(f"  内存使用: {stats.get('memory_used', 'N/A'):.2f} MB")
```

### 示例 2：高级宽带分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 高级宽带分析示例 ===")

# 创建光子晶体谐振腔
pc_period = 500e-9
hole_radius = 150e-9
slab_thickness = 220e-9
num_periods = 10

fdtd.eval(f"""
    # 创建光子晶体板
    addfdtd;
    set("dimension", "3D");
    set("x span", {pc_period * num_periods});
    set("y span", {pc_period * 5});
    set("z span", {slab_thickness * 3});
    
    # 创建硅板
    addrect;
    set("name", "pc_slab");
    set("material", "Si (Silicon) - Palik");
    set("x span", {pc_period * num_periods});
    set("y span", {pc_period * 5});
    set("z span", {slab_thickness});
    set("z", 0);
    
    # 创建空气孔阵列
    {{
    for(i=0; i<{num_periods}; i++) {{
        for(j=-2; j<=2; j++) {{
            addcircle;
            set("name", sprintf("hole_%d_%d", i, j));
            set("material", "Air");
            set("x", (i - ({num_periods}-1)/2) * {pc_period});
            set("y", j * {pc_period});
            set("z", 0);
            set("radius", {hole_radius});
            set("z span", {slab_thickness * 1.5});
        }}
    }}
    }}
    
    # 创建点缺陷（移除中心孔）
    delete("hole_{num_periods//2}_0");
    
    # 创建宽带源
    adddipole;
    set("name", "broadband_source");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("source type", "broadband");
    set("frequency start", 150e12);
    set("frequency stop", 400e12);
    set("amplitude", 1);
    
    # 创建场监视器
    addprofile;
    set("name", "cavity_field");
    set("monitor type", "2D Z-normal");
    set("x span", {pc_period * 3});
    set("y span", {pc_period * 3});
    set("z", 0);
    
    # 创建功率监视器
    addpower;
    set("name", "cavity_power");
    set("monitor type", "2D Z-normal");
    set("x span", {pc_period});
    set("y span", {pc_period});
    set("z", 0);
""")

# 配置高级宽带分析
print("配置高级宽带分析...")

fdtd.fdtdanalysis("broadband_analysis",
                 analysis_type="broadband",
                 frequency_points=500,
                 frequency_start=150e12,
                 frequency_stop=400e12,
                 frequency_scale="linear",
                 boundary_conditions="PML",
                 pml_layers=16,
                 pml_reflection=1e-10,
                 pml_type="stretched",
                 mesh_type="auto non-uniform",
                 mesh_accuracy=4,
                 min_mesh_step=20e-9,
                 max_mesh_step=100e-9,
                 mesh_refinement="conformal variant 1",
                 simulation_time=5000e-15,
                 auto_shutoff=1e-6,
                 courant_factor=0.95,
                 convergence_test=True,
                 convergence_tolerance=1e-4,
                 max_iterations=20000,
                 source_type="total-field",
                 output_frequency_points=250,
                 output_field_components="all",
                 save_fields=True,
                 save_frequency_data=True,
                 output_format="matlab")

# 运行宽带分析
print("运行宽带分析...")
fdtd.eval("""
    # 应用分析设置
    select("FDTD");
    setanalysis("broadband_analysis");
    
    # 运行仿真
    run;
    
    # 获取宽带响应
    f = getdata("cavity_power", "f");
    P = getdata("cavity_power", "P");
""")

# 获取宽带响应数据
freq_data = fdtd.getdata("cavity_power", "f")
power_data = fdtd.getdata("cavity_power", "P")

if freq_data is not None and power_data is not None:
    frequencies = freq_data.flatten()
    power = power_data.flatten()
    
    # 归一化功率谱
    power_norm = power / np.max(power)
    power_db = 10 * np.log10(power_norm)
    
    print(f"\n宽带分析结果:")
    print(f"  频率范围: {frequencies[0]/1e12:.1f} - {frequencies[-1]/1e12:.1f} THz")
    print(f"  频率点数: {len(frequencies)}")
    print(f"  动态范围: {np.max(power_db) - np.min(power_db):.1f} dB")
    
    # 寻找谐振峰
    from scipy.signal import find_peaks
    
    # 寻找显著峰值（高于平均值 3dB）
    peaks, properties = find_peaks(power_db, height=np.mean(power_db)+3, distance=10)
    
    print(f"\n检测到谐振峰: {len(peaks)} 个")
    
    if len(peaks) > 0:
        # 分析每个谐振峰
        resonance_info = []
        
        for i, peak_idx in enumerate(peaks):
            f_res = frequencies[peak_idx]
            P_res_db = power_db[peak_idx]
            P_res = power_norm[peak_idx]
            wavelength = 3e8 / f_res * 1e9
            
            # 计算品质因子（Q 因子）
            # 找到半高全宽点
            half_max_db = P_res_db - 3  # 3dB 带宽
            half_max_linear = 10**(half_max_db/10)
            
            # 寻找左右 3dB 点
            left_idx = peak_idx
            while left_idx > 0 and power_db[left_idx] > half_max_db:
                left_idx -= 1
            if left_idx > 0:
                # 线性插值
                f_left = np.interp(half_max_db, 
                                  [power_db[left_idx], power_db[left_idx+1]],
                                  [frequencies[left_idx], frequencies[left_idx+1]])
            else:
                f_left = frequencies[left_idx]
            
            right_idx = peak_idx
            while right_idx < len(frequencies)-1 and power_db[right_idx] > half_max_db:
                right_idx += 1
            if right_idx < len(frequencies)-1:
                f_right = np.interp(half_max_db,
                                   [power_db[right_idx-1], power_db[right_idx]],
                                   [frequencies[right_idx-1], frequencies[right_idx]])
            else:
                f_right = frequencies[right_idx]
            
            # 计算 3dB 带宽和 Q 因子
            bandwidth_3db = f_right - f_left
            Q_factor = f_res / bandwidth_3db if bandwidth_3db > 0 else np.inf
            
            resonance_info.append({
                'index': i+1,
                'frequency_thz': f_res/1e12,
                'wavelength_nm': wavelength,
                'power_db': P_res_db,
                'bandwidth_thz': bandwidth_3db/1e12,
                'Q_factor': Q_factor
            })
            
            print(f"\n  谐振峰 {i+1}:")
            print(f"    频率: {f_res/1e12:.3f} THz")
            print(f"    波长: {wavelength:.1f} nm")
            print(f"    相对强度: {P_res_db:.1f} dB")
            print(f"    3dB 带宽: {bandwidth_3db/1e12:.3f} THz")
            print(f"    品质因子: {Q_factor:.0f}")
        
        # 绘制宽带响应
        plt.figure(figsize=(12, 6))
        
        # 功率谱
        plt.subplot(1, 2, 1)
        plt.plot(frequencies/1e12, power_db, 'b-', linewidth=1.5)
        plt.xlabel("Frequency (THz)")
        plt.ylabel("Normalized Power (dB)")
        plt.title("Photonic Crystal Cavity Broadband Response")
        plt.grid(True, alpha=0.3)
        
        # 标记谐振峰
        for i, peak_idx in enumerate(peaks):
            f_res = frequencies[peak_idx]/1e12
            P_res_db = power_db[peak_idx]
            plt.plot(f_res, P_res_db, 'ro', markersize=8)
            plt.text(f_res, P_res_db+2, f'Q={resonance_info[i]["Q_factor"]:.0f}',
                    ha='center', fontsize=9)
        
        # 波长坐标
        plt.subplot(1, 2, 2)
        wavelengths = 3e8 / frequencies * 1e9
        plt.plot(wavelengths, power_db, 'b-', linewidth=1.5)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Normalized Power (dB)")
        plt.title("Response vs Wavelength")
        plt.grid(True, alpha=0.3)
        plt.gca().invert_xaxis()  # 波长增加方向
        
        plt.tight_layout()
        plt.savefig("broadband_analysis.png", dpi=150)
        print("\n宽带响应图保存为: broadband_analysis.png")
        
        # 分析场分布
        print("\n分析谐振模式场分布...")
        
        # 获取最高 Q 因子的谐振模式
        if resonance_info:
            best_resonance = max(resonance_info, key=lambda x: x['Q_factor'])
            best_freq = best_resonance['frequency_thz'] * 1e12
            
            # 获取该频率的场分布
            field_data = fdtd.getdata("cavity_field", "E")
            if field_data is not None:
                # 找到最接近的频率点
                freq_idx = np.argmin(np.abs(frequencies - best_freq))
                
                # 提取场分量
                E_field = field_data[:, :, freq_idx]
                E_magnitude = np.abs(E_field)
                
                # 绘制场分布
                plt.figure(figsize=(10, 8))
                
                plt.imshow(E_magnitude, cmap='hot', origin='lower',
                          extent=[-pc_period*1.5*1e6, pc_period*1.5*1e6,
                                  -pc_period*1.5*1e6, pc_period*1.5*1e6])
                plt.colorbar(label="|E| Field Strength")
                plt.xlabel("X (μm)")
                plt.ylabel("Y (μm)")
                plt.title(f"Resonant Mode Field Distribution\nf={best_freq/1e12:.3f} THz, Q={best_resonance['Q_factor']:.0f}")
                
                # 添加光子晶体孔位置
                for i in range(num_periods):
                    for j in range(-2, 3):
                        if not (i == num_periods//2 and j == 0):  # 跳过缺陷位置
                            x = (i - (num_periods-1)/2) * pc_period * 1e6
                            y = j * pc_period * 1e6
                            circle = plt.Circle((x, y), hole_radius*1e6,
                                               fill=False, color='white', linestyle='--', alpha=0.5)
                            plt.gca().add_patch(circle)
                
                plt.savefig("resonant_mode_field.png", dpi=150)
                print(f"谐振模式场分布保存为: resonant_mode_field.png")
        
        # 生成分析报告
        report = f"""光子晶体谐振腔宽带分析报告
        分析时间: {np.datetime64('now')}
        
        结构参数:
        - 晶格周期: {pc_period*1e9:.0f} nm
        - 空气孔半径: {hole_radius*1e9:.0f} nm
        - 板厚度: {slab_thickness*1e9:.0f} nm
        - 周期数: {num_periods}
        
        分析设置:
        - 频率范围: {frequencies[0]/1e12:.1f} - {frequencies[-1]/1e12:.1f} THz
        - 频率点数: {len(frequencies)}
        - 网格精度: 4
        - PML 层数: 16
        - 仿真时间: 5 ps
        
        谐振模式分析:
        """
        
        for res in resonance_info:
            report += f"""
        模式 {res['index']}:
        - 谐振频率: {res['frequency_thz']:.3f} THz
        - 谐振波长: {res['wavelength_nm']:.1f} nm
        - 相对强度: {res['power_db']:.1f} dB
        - 3dB 带宽: {res['bandwidth_thz']:.3f} THz
        - 品质因子: {res['Q_factor']:.0f}
            """
        
        print("\n" + report)
        
else:
    print("错误: 无法获取宽带响应数据")

# 检查数值收敛性
print("\n=== 数值收敛性检查 ===")

# 获取收敛历史
convergence_history = fdtd.eval("getnamed('FDTD', 'convergence');")
if convergence_history is not None:
    print(f"收敛历史长度: {len(convergence_history)}")
    
    # 检查最终收敛值
    final_convergence = convergence_history[-1] if len(convergence_history) > 0 else None
    if final_convergence is not None:
        print(f"最终收敛值: {final_convergence:.2e}")
        
        if final_convergence < 1e-5:
            print("收敛性: 优秀 (< 1e-5)")
        elif final_convergence < 1e-4:
            print("收敛性: 良好 (< 1e-4)")
        elif final_convergence < 1e-3:
            print("收敛性: 可接受 (< 1e-3)")
        else:
            print("收敛性: 警告 (> 1e-3)")
    
    # 绘制收敛曲线
    if len(convergence_history) > 1:
        plt.figure(figsize=(8, 4))
        iterations = np.arange(1, len(convergence_history) + 1)
        plt.semilogy(iterations, convergence_history, 'b-', linewidth=2)
        plt.xlabel("Iteration")
        plt.ylabel("Convergence")
        plt.title("FDTD Convergence History")
        plt.grid(True, which="both", alpha=0.3)
        plt.savefig("convergence_history.png", dpi=150)
        print("收敛历史图保存为: convergence_history.png")

# 获取内存和性能统计
stats = fdtd.eval("""
    stats = [];
    stats.total_iterations = getnamed('FDTD', 'iterations');
    stats.total_time = getnamed('FDTD', 'total time');
    stats.memory_peak = getnamed('FDTD', 'memory peak');
    stats.mesh_cells = getnamed('FDTD', 'mesh cells');
    stats.time_per_iteration = getnamed('FDTD', 'time per iteration');
    stats;
""")

if stats is not None:
    print(f"\n性能统计:")
    print(f"  总迭代次数: {stats.get('total_iterations', 'N/A'):,}")
    print(f"  总仿真时间: {stats.get('total_time', 'N/A'):.2f} s")
    print(f"  峰值内存: {stats.get('memory_peak', 'N/A'):.2f} MB")
    print(f"  网格单元数: {stats.get('mesh_cells', 'N/A'):,}")
    print(f"  每迭代时间: {stats.get('time_per_iteration', 'N/A'):.3f} ms")
```

### 示例 3：参数扫描和优化
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

fdtd = lumapi.FDTD()

print("=== 参数扫描和优化示例 ===")

# 创建可调谐微环谐振器
ring_radius = 5e-6
waveguide_width = 500e-9
waveguide_height = 220e-9
gap = 200e-9

def create_microresonator(radius, width, height, gap_size):
    """创建微环谐振器结构"""
    fdtd.eval(f"""
        # 清理之前的结构
        deleteall;
        
        # 创建 FDTD 求解器
        addfdtd;
        set("dimension", "3D");
        set("x span", 20e-6);
        set("y span", 20e-6);
        set("z span", 2e-6);
        
        # 创建直波导
        addrect;
        set("name", "bus_waveguide");
        set("material", "Si (Silicon) - Palik");
        set("x", 0);
        set("y", -{radius + gap_size + width/2});
        set("z", 0);
        set("x span", 15e-6);
        set("y span", {width});
        set("z span", {height});
        
        # 创建微环谐振器
        addring;
        set("name", "micro_ring");
        set("material", "Si (Silicon) - Palik");
        set("x", 0);
        set("y", 0);
        set("z", 0);
        set("inner radius", {radius - width/2});
        set("outer radius", {radius + width/2});
        set("z span", {height});
        
        # 创建模式源
        addmode;
        set("name", "input");
        set("injection axis", "x");
        set("x", -7e-6);
        set("y", -{radius + gap_size + width/2});
        set("z", 0);
        set("mode selection", "fundamental TE mode");
        
        # 创建传输监视器
        addpower;
        set("name", "through_port");
        set("monitor type", "2D X-normal");
        set("x", 7e-6);
        set("y", -{radius + gap_size + width/2});
        set("z", 0);
        
        # 创建下路监视器
        addpower;
        set("name", "drop_port");
        set("monitor type", "2D Y-normal");
        set("x", 0);
        set("y", {radius + gap_size + width/2});
        set("z", 0);
    """)

# 配置标准分析设置
fdtd.fdtdanalysis("microresonator_analysis",
                 frequency_points=300,
                 frequency_start=180e12,  # 1.67μm
                 frequency_stop=250e12,   # 1.2μm
                 boundary_conditions="PML",
                 pml_layers=10,
                 mesh_accuracy=3,
                 simulation_time=3000e-15,
                 auto_shutoff=1e-5,
                 analysis_type="standard")

print("微环谐振器参数扫描分析...")

# 参数扫描：环半径对谐振特性的影响
radii = np.linspace(4e-6, 6e-6, 5)
gap_sizes = np.linspace(150e-9, 250e-9, 3)

results = []

for radius in radii:
    for gap_size in gap_sizes:
        print(f"分析: 半径={radius*1e6:.1f}μm, 间隙={gap_size*1e9:.0f}nm")
        
        # 创建结构
        create_microresonator(radius, waveguide_width, waveguide_height, gap_size)
        
        # 应用分析设置并运行
        fdtd.eval("""
            select("FDTD");
            setanalysis("microresonator_analysis");
            run;
        """)
        
        # 获取传输谱
        freq_data = fdtd.getdata("through_port", "f")
        through_data = fdtd.getdata("through_port", "T")
        drop_data = fdtd.getdata("drop_port", "T")
        
        if freq_data is not None and through_data is not None:
            frequencies = freq_data.flatten()
            through = through_data.flatten()
            drop = drop_data.flatten() if drop_data is not None else np.zeros_like(through)
            
            # 寻找谐振频率
            from scipy.signal import find_peaks
            
            # 在 drop 端口寻找峰值（谐振时 drop 最大）
            peaks, _ = find_peaks(drop, height=0.1, distance=20)
            
            resonance_info = []
            for peak_idx in peaks[:3]:  # 只取前三个谐振峰
                f_res = frequencies[peak_idx]
                T_through = through[peak_idx]
                T_drop = drop[peak_idx]
                
                # 计算消光比和插入损耗
                extinction_ratio = -10 * np.log10(T_through) if T_through > 0 else np.inf
                insertion_loss = -10 * np.log10(T_drop) if T_drop > 0 else np.inf
                
                # 计算自由光谱范围（FSR） - 需要多个谐振峰
                if len(peaks) > 1:
                    next_peak = peaks[1] if peak_idx == peaks[0] else peaks[0]
                    fsr = abs(frequencies[next_peak] - f_res)
                else:
                    fsr = np.nan
                
                resonance_info.append({
                    'frequency': f_res,
                    'through_transmission': T_through,
                    'drop_transmission': T_drop,
                    'extinction_ratio_db': extinction_ratio,
                    'insertion_loss_db': insertion_loss,
                    'fsr': fsr
                })
            
            results.append({
                'radius': radius,
                'gap': gap_size,
                'frequencies': frequencies,
                'through': through,
                'drop': drop,
                'resonances': resonance_info
            })
            
            if resonance_info:
                print(f"  找到 {len(resonance_info)} 个谐振峰")
                for i, res in enumerate(resonance_info[:2]):  # 显示前两个
                    print(f"    峰{i+1}: {res['frequency']/1e12:.3f} THz, "
                          f"ER={res['extinction_ratio_db']:.1f} dB, "
                          f"IL={res['insertion_loss_db']:.1f} dB")

print(f"\n参数扫描完成，共 {len(results)} 个配置")

# 分析结果
if results:
    # 绘制参数扫描结果
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 半径对谐振频率的影响
    ax1 = axes[0, 0]
    for result in results:
        if result['resonances']:
            radius = result['radius'] * 1e6
            # 取第一个谐振峰
            freq = result['resonances'][0]['frequency'] / 1e12
            gap = result['gap'] * 1e9
            
            # 不同间隙用不同颜色
            color = 'b' if gap < 200 else 'r' if gap > 200 else 'g'
            marker = 'o' if gap < 200 else 's' if gap > 200 else '^'
            
            ax1.plot(radius, freq, marker=marker, color=color, markersize=8)
    
    ax1.set_xlabel("Ring Radius (μm)")
    ax1.set_ylabel("Resonant Frequency (THz)")
    ax1.set_title("Resonant Frequency vs Ring Radius")
    ax1.grid(True)
    
    # 添加理论曲线（微环谐振条件）
    theoretical_radii = np.linspace(4e-6, 6e-6, 100)
    # 简化模型：谐振条件 mλ = 2πR * n_eff
    n_eff = 2.5  # 假设有效折射率
    m = 30  # 模式阶数
    theoretical_freqs = m * 3e8 / (2 * np.pi * theoretical_radii * n_eff) / 1e12
    ax1.plot(theoretical_radii*1e6, theoretical_freqs, 'k--', label='Theoretical')
    ax1.legend()
    
    # 2. 间隙对消光比的影响
    ax2 = axes[0, 1]
    extinction_ratios = []
    gaps = []
    
    for result in results:
        if result['resonances']:
            extinction_db = result['resonances'][0]['extinction_ratio_db']
            if np.isfinite(extinction_db):
                extinction_ratios.append(extinction_db)
                gaps.append(result['gap'] * 1e9)
    
    if extinction_ratios:
        ax2.plot(gaps, extinction_ratios, 'bo-', linewidth=2, markersize=6)
        ax2.set_xlabel("Gap Size (nm)")
        ax2.set_ylabel("Extinction Ratio (dB)")
        ax2.set_title("Extinction Ratio vs Gap Size")
        ax2.grid(True)
    
    # 3. 传输谱示例
    ax3 = axes[1, 0]
    # 选择中间参数的结果
    mid_result = results[len(results)//2]
    if 'frequencies' in mid_result:
        wavelengths = 3e8 / mid_result['frequencies'] * 1e9
        ax3.plot(wavelengths, 10*np.log10(mid_result['through']), 'b-', label='Through')
        ax3.plot(wavelengths, 10*np.log10(mid_result['drop']), 'r-', label='Drop')
        ax3.set_xlabel("Wavelength (nm)")
        ax3.set_ylabel("Transmission (dB)")
        ax3.set_title(f"Transmission Spectrum\nR={mid_result['radius']*1e6:.1f}μm, gap={mid_result['gap']*1e9:.0f}nm")
        ax3.grid(True)
        ax3.legend()
        ax3.invert_xaxis()
    
    # 4. 品质因子分布
    ax4 = axes[1, 1]
    Q_factors = []
    radii_for_q = []
    
    for result in results:
        if result['resonances']:
            # 计算 Q 因子（简化）
            res = result['resonances'][0]
            if 'fsr' in res and not np.isnan(res['fsr']):
                # Q = f / Δf，其中 Δf 用谐振峰宽度估计
                # 这里用 FSR 作为粗略估计
                Q = res['frequency'] / res['fsr']
                Q_factors.append(Q)
                radii_for_q.append(result['radius'] * 1e6)
    
    if Q_factors:
        ax4.plot(radii_for_q, Q_factors, 'go-', linewidth=2, markersize=6)
        ax4.set_xlabel("Ring Radius (μm)")
        ax4.set_ylabel("Quality Factor")
        ax4.set_title("Quality Factor vs Ring Radius")
        ax4.set_yscale('log')
        ax4.grid(True)
    
    plt.tight_layout()
    plt.savefig("parameter_sweep_analysis.png", dpi=150)
    print("参数扫描分析图保存为: parameter_sweep_analysis.png")
    
    # 优化：寻找最佳间隙以达到目标消光比
    print("\n=== 间隙优化 ===")
    
    def objective_function(gap_nm, target_er_db=20):
        """目标函数：最小化消光比与目标的差异"""
        gap = gap_nm * 1e-9
        radius = 5e-6  # 固定半径
        
        # 创建结构并分析
        create_microresonator(radius, waveguide_width, waveguide_height, gap)
        fdtd.eval("""
            select("FDTD");
            setanalysis("microresonator_analysis");
            run;
        """)
        
        # 获取结果
        drop_data = fdtd.getdata("drop_port", "T")
        if drop_data is not None:
            drop = drop_data.flatten()
            # 找到最大 drop（谐振点）
            max_drop = np.max(drop)
            if max_drop > 0:
                # 对应的 through 传输
                through_data = fdtd.getdata("through_port", "T")
                if through_data is not None:
                    through = through_data.flatten()
                    max_drop_idx = np.argmax(drop)
                    through_at_res = through[max_drop_idx]
                    
                    # 计算消光比
                    if through_at_res > 0:
                        er_db = -10 * np.log10(through_at_res)
                        # 返回与目标差异的平方
                        return (er_db - target_er_db)**2
        return 1e6  # 失败时返回大值
    
    # 执行优化
    try:
        initial_guess = 200  # 初始猜测 200nm
        bounds = [(150, 250)]  # 间隙范围 150-250nm
        
        result = optimize.minimize(objective_function, initial_guess, 
                                  bounds=bounds, method='L-BFGS-B',
                                  options={'maxiter': 10, 'disp': True})
        
        if result.success:
            optimal_gap = result.x[0]
            print(f"优化结果:")
            print(f"  最优间隙: {optimal_gap:.1f} nm")
            print(f"  目标函数值: {result.fun:.4f}")
            
            # 验证最优间隙
            final_er = np.sqrt(result.fun) + 20  # 反向计算消光比
            print(f"  达到的消光比: {final_er:.1f} dB")
        else:
            print(f"优化失败: {result.message}")
            
    except Exception as e:
        print(f"优化过程中出错: {e}")

print("\n参数扫描和优化完成！")
```

### 示例 4：多物理场耦合分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

fdtd = lumapi.FDTD()

print("=== 多物理场耦合分析示例 ===")

# 创建热-光调谐器件
device_length = 20e-6
waveguide_width = 500e-9
heater_width = 2e-6
heater_thickness = 200e-9

fdtd.eval(f"""
    # 创建 FDTD 求解器（包含热效应）
    addfdtd;
    set("dimension", "3D");
    set("x span", 30e-6);
    set("y span", 10e-6);
    set("z span", 5e-6);
    set("simulation type", "2.5D varFDTD");  # 使用变分 FDTD 提高效率
    
    # 创建硅波导
    addrect;
    set("name", "waveguide");
    set("material", "Si (Silicon) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", {device_length});
    set("y span", {waveguide_width});
    set("z span", 220e-9);
    
    # 创建二氧化硅衬底
    addrect;
    set("name", "substrate");
    set("material", "SiO2 (Glass) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", -1e-6);
    set("x span", 30e-6);
    set("y span", 10e-6);
    set("z span", 2e-6);
    
    # 创建金属加热器
    addrect;
    set("name", "heater");
    set("material", "Au (Gold) - Palik");
    set("x", 0);
    set("y", 1.5e-6);  # 波导上方
    set("z", 110e-9);  # 波导上方
    set("x span", {device_length});
    set("y span", {heater_width});
    set("z span", {heater_thickness});
    
    # 创建热监视器
    addthermal;
    set("name", "thermal_monitor");
    set("monitor type", "2D Z-normal");
    set("x span", {device_length});
    set("y span", 6e-6);
    set("z", 0);
    
    # 创建光学模式源
    addmode;
    set("name", "optical_source");
    set("injection axis", "x");
    set("x", -8e-6);
    set("y", 0);
    set("z", 0);
    set("mode selection", "fundamental TE mode");
    set("wavelength", 1.55e-6);
    
    # 创建光学监视器
    addpower;
    set("name", "optical_output");
    set("monitor type", "2D X-normal");
    set("x", 8e-6);
    set("y", 0);
    set("z", 0);
""")

# 配置多物理场分析
print("配置多物理场分析...")

fdtd.fdtdanalysis("multiphysics_analysis",
                 analysis_type="coupled",
                 frequency_points=100,
                 frequency_start=180e12,
                 frequency_stop=220e12,
                 boundary_conditions="PML",
                 pml_layers=10,
                 mesh_accuracy=3,
                 simulation_time=2000e-15,
                 auto_shutoff=1e-5,
                 
                 # 热分析设置
                 thermal_analysis=True,
                 thermal_boundary="fixed temperature",
                 ambient_temperature=300,  # 开尔文
                 thermal_solver="steady state",
                 thermal_convergence=1e-3,
                 
                 # 材料热光系数
                 thermo_optic_coefficient=1.86e-4,  # 硅的热光系数 (1/K)
                 
                 # 耦合迭代设置
                 max_coupling_iterations=10,
                 coupling_tolerance=1e-3,
                 
                 # 输出设置
                 save_thermal_data=True,
                 save_optical_data=True,
                 output_frequency_points=50)

# 分析不同加热功率下的热-光调谐
print("\n分析热-光调谐特性...")

heating_powers = np.linspace(0, 100e-3, 6)  # 0-100 mW
results = []

for power in heating_powers:
    print(f"分析加热功率: {power*1e3:.1f} mW")
    
    # 设置加热器功率
    fdtd.eval(f"""
        # 设置热源
        select("heater");
        set("thermal port", "yes");
        set("thermal power", {power});
        
        # 应用分析设置
        select("FDTD");
        setanalysis("multiphysics_analysis");
        
        # 运行耦合分析
        run;
    """)
    
    # 获取热分布
    thermal_data = fdtd.getdata("thermal_monitor", "T")
    if thermal_data is not None:
        max_temp = np.max(thermal_data) - 300  # 相对于环境温升
        avg_temp = np.mean(thermal_data) - 300
    else:
        max_temp = avg_temp = np.nan
    
    # 获取光学响应
    freq_data = fdtd.getdata("optical_output", "f")
    transmission_data = fdtd.getdata("optical_output", "T")
    
    if freq_data is not None and transmission_data is not None:
        frequencies = freq_data.flatten()
        transmission = transmission_data.flatten()
        
        # 找到传输最大点（谐振频率偏移）
        max_idx = np.argmax(transmission)
        resonant_freq = frequencies[max_idx]
        max_transmission = transmission[max_idx]
        
        # 计算波长
        resonant_wavelength = 3e8 / resonant_freq * 1e9
        
        results.append({
            'power': power,
            'max_temperature': max_temp,
            'avg_temperature': avg_temp,
            'resonant_frequency': resonant_freq,
            'resonant_wavelength': resonant_wavelength,
            'transmission': max_transmission,
            'full_spectrum': (frequencies, transmission)
        })
        
        print(f"  最大温升: {max_temp:.1f} K")
        print(f"  谐振波长: {resonant_wavelength:.1f} nm")
        print(f"  最大传输: {max_transmission:.4f}")

# 分析热光调谐特性
if results:
    print("\n=== 热光调谐分析 ===")
    
    powers = [r['power'] for r in results]
    temps = [r['max_temperature'] for r in results]
    wavelengths = [r['resonant_wavelength'] for r in results]
    
    # 计算调谐效率
    if len(wavelengths) > 1:
        # 线性拟合波长 vs 功率
        coeffs = np.polyfit(powers, wavelengths, 1)
        tuning_slope = coeffs[0]  # nm/W
        tuning_efficiency = tuning_slope * 1e3  # nm/mW
        
        print(f"调谐效率: {tuning_efficiency:.3f} nm/mW")
        print(f"线性拟合: λ = {coeffs[1]:.3f} + {coeffs[0]:.3f} * P")
        
        # 计算热光系数
        # Δλ/λ = α * ΔT，其中 α 是热光系数
        if not np.isnan(temps[1]):  # 使用第一个非零功率点
            delta_lambda = wavelengths[1] - wavelengths[0]
            delta_temp = temps[1] - temps[0]
            if delta_temp > 0:
                measured_alpha = (delta_lambda / wavelengths[0]) / delta_temp
                print(f"测量热光系数: {measured_alpha:.3e} /K")
                print(f"理论热光系数（硅）: 1.86e-4 /K")
                print(f"相对误差: {abs(measured_alpha - 1.86e-4)/1.86e-4*100:.1f}%")
    
    # 绘制热光调谐曲线
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 波长调谐 vs 功率
    axes[0, 0].plot(np.array(powers)*1e3, wavelengths, 'bo-', linewidth=2, markersize=8)
    axes[0, 0].set_xlabel("Heating Power (mW)")
    axes[0, 0].set_ylabel("Resonant Wavelength (nm)")
    axes[0, 0].set_title("Thermo-optic Tuning")
    axes[0, 0].grid(True)
    
    # 添加线性拟合
    if len(wavelengths) > 1:
        fit_line = np.polyval(coeffs, powers)
        axes[0, 0].plot(np.array(powers)*1e3, fit_line, 'r--', label=f'Fit: {tuning_efficiency:.3f} nm/mW')
        axes[0, 0].legend()
    
    # 2. 温度分布
    axes[0, 1].plot(np.array(powers)*1e3, temps, 'ro-', linewidth=2, markersize=8)
    axes[0, 1].set_xlabel("Heating Power (mW)")
    axes[0, 1].set_ylabel("Maximum Temperature Rise (K)")
    axes[0, 1].set_title("Thermal Response")
    axes[0, 1].grid(True)
    
    # 3. 传输谱随温度变化
    axes[1, 0].set_prop_cycle(color=plt.cm.viridis(np.linspace(0, 1, len(results))))
    for i, result in enumerate(results):
        freqs, trans = result['full_spectrum']
        wavelengths_spectrum = 3e8 / freqs * 1e9
        axes[1, 0].plot(wavelengths_spectrum, 10*np.log10(trans), 
                       label=f'{result["power"]*1e3:.0f} mW', linewidth=1.5)
    
    axes[1, 0].set_xlabel("Wavelength (nm)")
    axes[1, 0].set_ylabel("Transmission (dB)")
    axes[1, 0].set_title("Transmission Spectra at Different Powers")
    axes[1, 0].grid(True)
    axes[1, 0].legend(title="Power", fontsize=8)
    axes[1, 0].invert_xaxis()
    
    # 4. 热分布（最高功率时）
    if results:
        max_power_result = results[-1]
        # 获取热分布数据
        thermal_dist = fdtd.getdata("thermal_monitor", "T")
        if thermal_dist is not None:
            im = axes[1, 1].imshow(thermal_dist - 300, cmap='hot', origin='lower')
            axes[1, 1].set_xlabel("X position")
            axes[1, 1].set_ylabel("Y position")
            axes[1, 1].set_title(f"Temperature Distribution at {max_power_result['power']*1e3:.0f} mW")
            plt.colorbar(im, ax=axes[1, 1], label="Temperature Rise (K)")
    
    plt.tight_layout()
    plt.savefig("thermo_optic_tuning_analysis.png", dpi=150)
    print("\n热光调谐分析图保存为: thermo_optic_tuning_analysis.png")
    
    # 分析热串扰
    print("\n=== 热串扰分析 ===")
    
    # 获取空间温度分布
    thermal_profile = fdtd.getdata("thermal_monitor", "T")
    if thermal_profile is not None:
        # 提取沿波导方向的温度分布
        center_y = thermal_profile.shape[0] // 2
        temp_along_waveguide = thermal_profile[center_y, :]
        
        # 计算热扩散长度
        # 假设加热器在中心，温度向两边衰减
        max_temp_idx = np.argmax(temp_along_waveguide)
        left_side = temp_along_waveguide[:max_temp_idx]
        right_side = temp_along_waveguide[max_temp_idx:]
        
        # 找到温度下降到 1/e 的点
        max_temp = temp_along_waveguide[max_temp_idx]
        threshold_temp = max_temp * 0.368  # 1/e
        
        def find_thermal_length(temperatures, threshold):
            """计算热扩散长度"""
            for i in range(len(temperatures)-1, 0, -1):
                if temperatures[i] <= threshold:
                    return i
            return len(temperatures)
        
        left_length = find_thermal_length(left_side[::-1], threshold_temp)
        right_length = find_thermal_length(right_side, threshold_temp)
        thermal_diffusion_length = max(left_length, right_length)
        
        print(f"热扩散长度: {thermal_diffusion_length} 像素")
        
        # 转换为实际距离（需要知道像素尺寸）
        # 这里假设每个像素对应 100nm
        pixel_size = 100e-9
        thermal_length_um = thermal_diffusion_length * pixel_size * 1e6
        print(f"热扩散长度: {thermal_length_um:.1f} μm")

print("\n多物理场耦合分析完成！")
```

### 示例 5：大型结构的高性能分析
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt
import time

fdtd = lumapi.FDTD()

print("=== 大型结构的高性能分析示例 ===")

# 创建大型光子集成电路（PIC）结构
circuit_size = 100e-6
num_components = 5

fdtd.eval(f"""
    # 创建大型 FDTD 求解器
    addfdtd;
    set("dimension", "3D");
    set("x span", {circuit_size});
    set("y span", {circuit_size});
    set("z span", 5e-6);
    set("simulation type", "2.5D varFDTD");  # 使用变分 FDTD 提高大型结构效率
    
    # 创建多个波导组件
    {{
    for(i=0; i<{num_components}; i++) {{
        # 创建弯曲波导
        addbend;
        set("name", sprintf("bend_%d", i));
        set("material", "Si (Silicon) - Palik");
        set("x", (i-2) * 15e-6);
        set("y", 0);
        set("z", 0);
        set("inner radius", 5e-6);
        set("angle", 90);
        set("width", 500e-9);
        set("height", 220e-9);
        
        # 创建直波导段
        addrect;
        set("name", sprintf("straight_%d", i));
        set("material", "Si (Silicon) - Palik");
        set("x", (i-2) * 15e-6 + 7.5e-6);
        set("y", -5e-6);
        set("z", 0);
        set("x span", 10e-6);
        set("y span", 500e-9);
        set("z span", 220e-9);
        
        # 创建方向耦合器
        addrect;
        set("name", sprintf("coupler_top_%d", i));
        set("material", "Si (Silicon) - Palik");
        set("x", (i-2) * 15e-6);
        set("y", 3e-6);
        set("z", 0);
        set("x span", 20e-6);
        set("y span", 500e-9);
        set("z span", 220e-9);
        
        addrect;
        set("name", sprintf("coupler_bottom_%d", i));
        set("material", "Si (Silicon) - Palik");
        set("x", (i-2) * 15e-6);
        set("y", 1e-6);
        set("z", 0);
        set("x span", 20e-6);
        set("y span", 500e-9);
        set("z span", 220e-9);
    }}
    }}
    
    # 创建全局源
    addmode;
    set("name", "global_source");
    set("injection axis", "x");
    set("x", -{circuit_size/2 - 5e-6});
    set("y", 0);
    set("z", 0);
    set("mode selection", "fundamental TE mode");
    set("x span", 5e-6);
    set("y span", 5e-6);
    
    # 创建多个监视器
    addpower;
    set("name", "output_monitor");
    set("monitor type", "2D X-normal");
    set("x", {circuit_size/2 - 5e-6});
    set("y", 0);
    set("z", 0);
    set("x span", 10e-6);
    set("y span", 10e-6);
""")

# 配置高性能分析设置
print("配置高性能分析设置...")

high_perf_options = {
    # 基本频率设置
    "frequency_points": 200,
    "frequency_start": 180e12,
    "frequency_stop": 220e12,
    "analysis_type": "broadband",
    
    # 高性能边界条件
    "boundary_conditions": "PML",
    "pml_layers": 8,  # 减少层数提高性能
    "pml_reflection": 1e-6,
    "pml_type": "stretched",
    
    # 高性能网格设置
    "mesh_type": "auto non-uniform",
    "mesh_accuracy": 2,  # 降低精度提高速度
    "mesh_refinement": "conformal variant 0",  # 最快选项
    "min_mesh_step": 50e-9,
    "max_mesh_step": 200e-9,
    
    # 求解器优化
    "simulation_time": 1000e-15,  # 较短时间
    "auto_shutoff": 1e-4,  # 宽松停止条件
    "courant_factor": 0.9,  # 保守 CFL 提高稳定性
    "convergence_test": False,  # 关闭收敛测试加快速度
    "max_iterations": 5000,
    
    # 内存优化
    "save_fields": False,  # 不保存场数据节省内存
    "save_frequency_data": True,
    "output_frequency_points": 100,  # 减少输出点数
    
    # 并行计算设置（如果可用）
    "use_parallel": True,
    "num_cores": 4,  # 假设 4 核
    "parallel_type": "shared memory",
    
    # GPU 加速（如果可用）
    "use_gpu": False,  # 假设无 GPU
}

# 应用高性能设置
fdtd.fdtdanalysis("high_performance_analysis", **high_perf_options)

# 性能基准测试
print("\n运行性能基准测试...")

# 记录初始资源使用
initial_stats = fdtd.eval("""
    stats = [];
    stats.memory_before = memory();
    stats.time_before = time();
    stats;
""")

# 运行仿真
start_time = time.time()

fdtd.eval("""
    select("FDTD");
    setanalysis("high_performance_analysis");
    run;
""")

simulation_time = time.time() - start_time

# 记录最终资源使用
final_stats = fdtd.eval("""
    stats = [];
    stats.memory_after = memory();
    stats.time_after = time();
    stats.mesh_cells = getnamed('FDTD', 'mesh cells');
    stats.total_iterations = getnamed('FDTD', 'iterations');
    stats;
""")

print(f"仿真完成!")
print(f"实际仿真时间: {simulation_time:.2f} s")

if initial_stats is not None and final_stats is not None:
    memory_used = final_stats.get('memory_after', 0) - initial_stats.get('memory_before', 0)
    print(f"内存使用: {memory_used:.2f} MB")
    print(f"网格单元数: {final_stats.get('mesh_cells', 'N/A'):,}")
    print(f"总迭代次数: {final_stats.get('total_iterations', 'N/A'):,}")
    print(f"每迭代时间: {simulation_time/final_stats.get('total_iterations', 1)*1000:.3f} ms")

# 获取结果
freq_data = fdtd.getdata("output_monitor", "f")
transmission_data = fdtd.getdata("output_monitor", "T")

if freq_data is not None and transmission_data is not None:
    frequencies = freq_data.flatten()
    transmission = transmission_data.flatten()
    
    print(f"\n分析结果:")
    print(f"频率点数: {len(frequencies)}")
    print(f"传输范围: {np.min(transmission):.4f} - {np.max(transmission):.4f}")
    
    # 计算性能指标
    performance_metrics = {}
    
    # 1. 计算速度（单元/秒）
    if final_stats is not None and 'mesh_cells' in final_stats:
        cells = final_stats['mesh_cells']
        iterations = final_stats.get('total_iterations', 1)
        total_updates = cells * iterations
        updates_per_second = total_updates / simulation_time if simulation_time > 0 else 0
        performance_metrics['updates_per_second'] = updates_per_second
        print(f"计算速度: {updates_per_second/1e6:.1f} M 单元更新/秒")
    
    # 2. 内存效率（MB/百万单元）
    if 'mesh_cells' in final_stats and memory_used > 0:
        memory_efficiency = memory_used / (final_stats['mesh_cells'] / 1e6)
        performance_metrics['memory_efficiency'] = memory_efficiency
        print(f"内存效率: {memory_efficiency:.2f} MB/百万单元")
    
    # 3. 精度评估（通过检查能量守恒）
    # 获取输入功率
    source_power = fdtd.eval("getnamed('global_source', 'power');")
    if source_power is not None:
        total_output = np.sum(transmission) * (frequencies[1] - frequencies[0])  # 简化积分
        energy_conservation = total_output / source_power if source_power > 0 else np.nan
        performance_metrics['energy_conservation'] = energy_conservation
        print(f"能量守恒: {energy_conservation:.4f}")
    
    # 绘制性能结果
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 传输谱
    wavelengths = 3e8 / frequencies * 1e9
    axes[0].plot(wavelengths, 10*np.log10(transmission), 'b-', linewidth=1.5)
    axes[0].set_xlabel("Wavelength (nm)")
    axes[0].set_ylabel("Transmission (dB)")
    axes[0].set_title("Large PIC Transmission Spectrum")
    axes[0].grid(True, alpha=0.3)
    axes[0].invert_xaxis()
    
    # 性能摘要
    axes[1].axis('off')
    performance_text = f"""Performance Summary:
    
Simulation Statistics:
- Simulation Time: {simulation_time:.2f} s
- Mesh Cells: {final_stats.get('mesh_cells', 'N/A'):,}
- Iterations: {final_stats.get('total_iterations', 'N/A'):,}
- Memory Used: {memory_used:.2f} MB

Performance Metrics:
- Speed: {performance_metrics.get('updates_per_second', 0)/1e6:.1f} M updates/s
- Memory Efficiency: {performance_metrics.get('memory_efficiency', 0):.2f} MB/M cells
- Energy Conservation: {performance_metrics.get('energy_conservation', 0):.4f}

Settings Used:
- Mesh Accuracy: {high_perf_options['mesh_accuracy']}
- PML Layers: {high_perf_options['pml_layers']}
- Auto Shutoff: {high_perf_options['auto_shutoff']}
- Convergence Test: {high_perf_options['convergence_test']}
"""
    
    axes[1].text(0.1, 0.9, performance_text, transform=axes[1].transAxes,
                verticalalignment='top', fontfamily='monospace', fontsize=9)
    
    plt.tight_layout()
    plt.savefig("high_performance_analysis.png", dpi=150)
    print("\n高性能分析结果保存为: high_performance_analysis.png")
    
    # 比较不同设置的性能
    print("\n=== 设置优化比较 ===")
    
    # 测试不同网格精度
    accuracy_levels = [1, 2, 3, 4]
    performance_results = []
    
    for accuracy in accuracy_levels[:2]:  # 只测试前两个以节省时间
        print(f"\n测试网格精度: {accuracy}")
        
        # 更新设置
        high_perf_options['mesh_accuracy'] = accuracy
        
        # 重新应用设置
        fdtd.fdtdanalysis(f"accuracy_test_{accuracy}", **high_perf_options)
        
        # 运行测试
        test_start = time.time()
        fdtd.eval(f"""
            select("FDTD");
            setanalysis("accuracy_test_{accuracy}");
            run;
        """)
        test_time = time.time() - test_start
        
        # 获取网格信息
        test_stats = fdtd.eval("getnamed('FDTD', 'mesh cells');")
        
        performance_results.append({
            'accuracy': accuracy,
            'time': test_time,
            'mesh_cells': test_stats if test_stats is not None else 0
        })
        
        print(f"  仿真时间: {test_time:.2f} s")
        print(f"  网格单元: {test_stats if test_stats is not None else 0:,}")
    
    if performance_results:
        # 绘制性能比较
        fig, ax = plt.subplots(figsize=(8, 5))
        
        accuracies = [r['accuracy'] for r in performance_results]
        times = [r['time'] for r in performance_results]
        cells = [r['mesh_cells'] for r in performance_results]
        
        ax.plot(accuracies, times, 'bo-', linewidth=2, markersize=8, label='Simulation Time')
        ax.set_xlabel("Mesh Accuracy")
        ax.set_ylabel("Simulation Time (s)", color='b')
        ax.tick_params(axis='y', labelcolor='b')
        ax.grid(True, alpha=0.3)
        
        ax2 = ax.twinx()
        ax2.plot(accuracies, cells, 'ro-', linewidth=2, markersize=8, label='Mesh Cells')
        ax2.set_ylabel("Mesh Cells", color='r')
        ax2.tick_params(axis='y', labelcolor='r')
        
        plt.title("Performance vs Mesh Accuracy")
        fig.tight_layout()
        plt.savefig("accuracy_performance_comparison.png", dpi=150)
        print("精度性能比较图保存为: accuracy_performance_comparison.png")
        
        # 计算最佳性价比
        if len(performance_results) > 1:
            # 假设性价比与 1/(时间×网格数) 成正比
            best_value = 0
            best_accuracy = None
            
            for result in performance_results:
                if result['time'] > 0 and result['mesh_cells'] > 0:
                    value = 1 / (result['time'] * result['mesh_cells'])
                    if value > best_value:
                        best_value = value
                        best_accuracy = result['accuracy']
            
            print(f"\n推荐设置: 网格精度 {best_accuracy} (最佳性价比)")

print("\n高性能分析完成！")
```

## 注意事项

### 1. 精度与性能权衡
- **网格精度**：精度每提高一级，计算量增加约 8 倍
- **仿真时间**：过短可能导致未收敛，过长浪费资源
- **PML 层数**：通常 8-16 层，过多增加计算量，过少增加反射
- **自动停止条件**：1e-5 适用于大多数情况，1e-3 可用于快速扫描

### 2. 收敛性验证
- **能量守恒**：检查输入输出能量平衡（应 > 0.95）
- **场监视器**：比较不同时间步的场分布
- **参数扫描**：逐步细化参数验证结果稳定性
- **网格收敛**：测试不同网格精度的结果差异

### 3. 内存管理
- **场数据保存**：仅保存必要数据，避免内存溢出
- **监视器优化**：合理设置监视器范围和分辨率
- **并行计算**：利用多核 CPU 加速大型仿真
- **GPU 加速**：对某些问题可显著提高速度

### 4. 数值稳定性
- **CFL 条件**：保持 Courant 因子 < 1 确保稳定性
- **材料离散化**：高折射率材料需要更细网格
- **边界反射**：检查 PML 性能，避免边界反射影响结果
- **时间步长**：自适应时间步长可提高效率和稳定性

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 核心功能，支持所有选项 |
| **MODE Solutions** | 有限支持 | 部分分析功能可用 |
| **DEVICE** | 不支持 | 不适用 |
| **INTERCONNECT** | 不支持 | 不适用 |

## 相关命令

- [`setanalysis`](./setanalysis.md) - 应用分析设置
- [`getanalysis`](./getanalysis.md) - 获取分析设置
- [`run`](./run.md) - 运行仿真
- [`mesh`](./mesh.md) - 网格设置
- [`setglobalmonitor`](./setglobalmonitor.md) - 设置全局监视器

## 最佳实践

### 1. 分析设置模板
```python
def create_analysis_template(template_name, application_type):
    """创建预定义分析模板"""
    templates = {
        'quick_scan': {
            'frequency_points': 50,
            'mesh_accuracy': 1,
            'simulation_time': 500e-15,
            'auto_shutoff': 1e-4,
            'save_fields': False
        },
        'standard_analysis': {
            'frequency_points': 100,
            'mesh_accuracy': 2,
            'simulation_time': 1000e-15,
            'auto_shutoff': 1e-5,
            'save_fields': True
        },
        'high_accuracy': {
            'frequency_points': 200,
            'mesh_accuracy': 3,
            'simulation_time': 2000e-15,
            'auto_shutoff': 1e-6,
            'save_fields': True
        },
        'broadband': {
            'analysis_type': 'broadband',
            'frequency_points': 300,
            'mesh_accuracy': 2,
            'simulation_time': 3000e-15,
            'auto_shutoff': 1e-5
        }
    }
    
    if application_type in templates:
        return templates[application_type]
    else:
        return templates['standard_analysis']

# 使用模板
template = create_analysis_template("my_analysis", "high_accuracy")
session.fdtdanalysis("custom_analysis", **template)
```

### 2. 自动收敛测试
```python
def auto_convergence_test(session, base_settings, test_parameter, test_values):
    """自动收敛性测试"""
    results = []
    
    for value in test_values:
        print(f"测试 {test_parameter} = {value}")
        
        # 更新设置
        settings = base_settings.copy()
        settings[test_parameter] = value
        
        # 创建并运行分析
        analysis_name = f"conv_test_{test_parameter}_{value}"
        session.fdtdanalysis(analysis_name, **settings)
        session.eval(f"""
            select("FDTD");
            setanalysis("{analysis_name}");
            run;
        """)
        
        # 获取关键结果
        result_key = session.eval("getdata('output_monitor', 'T');")
        if result_key is not None:
            results.append({
                'parameter': test_parameter,
                'value': value,
                'result': np.mean(result_key)
            })
    
    # 分析收敛性
    if len(results) >= 3:
        values = [r['value'] for r in results]
        means = [r['result'] for r in results]
        
        # 计算相对变化
        changes = np.abs(np.diff(means) / means[:-1])
        converged = np.all(changes < 0.01)  # 1% 变化阈值
        
        return {
            'converged': converged,
            'recommended_value': values[-1] if converged else values[np.argmin(changes)],
            'results': results
        }
    
    return None
```

### 3. 分析结果验证
```python
class AnalysisValidator:
    """分析结果验证器"""
    
    def __init__(self, session):
        self.session = session
        self.validation_results = {}
    
    def validate_analysis(self, analysis_name):
        """验证分析结果"""
        validations = {}
        
        # 1. 能量守恒检查
        input_power = self.session.eval("getnamed('source', 'power');")
        output_power = self.session.eval("sum(getdata('output_monitor', 'P'));")
        
        if input_power is not None and output_power is not None:
            energy_conservation = output_power / input_power
            validations['energy_conservation'] = {
                'value': energy_conservation,
                'passed': 0.95 < energy_conservation < 1.05
            }
        
        # 2. 数值收敛检查
        convergence = self.session.eval("getnamed('FDTD', 'percent done');")
        if convergence is not None:
            validations['convergence'] = {
                'value': convergence,
                'passed': convergence > 99.9
            }
        
        # 3. 网格质量检查
        mesh_quality = self.session.eval("getnamed('FDTD', 'mesh quality');")
        if mesh_quality is not None:
            validations['mesh_quality'] = {
                'value': mesh_quality,
                'passed': mesh_quality > 0.8
            }
        
        # 4. 稳定性检查
        stability = self.session.eval("getnamed('FDTD', 'stability');")
        if stability is not None:
            validations['stability'] = {
                'value': stability,
                'passed': stability > 0.99
            }
        
        self.validation_results[analysis_name] = validations
        return validations
    
    def generate_validation_report(self):
        """生成验证报告"""
        report = "Analysis Validation Report\n"
        report += "=" * 50 + "\n"
        
        for analysis_name, validations in self.validation_results.items():
            report += f"\nAnalysis: {analysis_name}\n"
            report += "-" * 30 + "\n"
            
            all_passed = True
            for check_name, check_result in validations.items():
                status = "PASS" if check_result['passed'] else "FAIL"
                report += f"{check_name:20} {status:6} value={check_result['value']:.4f}\n"
                if not check_result['passed']:
                    all_passed = False
            
            report += f"Overall: {'PASS' if all_passed else 'FAIL'}\n"
        
        return report
```

## 故障排除

### 常见问题
1. **仿真不收敛**：增加仿真时间，检查自动停止条件
2. **内存不足**：减少网格精度，关闭场数据保存
3. **数值不稳定**：降低 Courant 因子，检查材料参数
4. **边界反射**：增加 PML 层数，调整 PML 参数
5. **结果异常**：验证能量守恒，检查源和监视器设置

### 调试建议
- 从简单测试案例开始验证基本功能
- 逐步增加复杂度调试参数
- 使用验证工具检查结果合理性
- 对比不同设置的性能和质量

---

*文档版本：1.0 | 最后更新：2025-01-31*