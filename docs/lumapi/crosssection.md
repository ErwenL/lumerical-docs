# `crosssection` - 计算横截面

## 概述

`crosssection` 命令用于计算光学或电磁结构的横截面特性。在光子学仿真中，横截面分析是理解波导、光纤、光子晶体等结构光学行为的关键工具。该命令可以计算模式分布、功率流、场分布、有效折射率、损耗等横截面相关的物理量。

横截面分析通常用于：
- 分析波导中的模式特性
- 计算光纤中的模场直径
- 评估光子晶体结构的带隙特性
- 分析等离子体结构的场增强
- 计算功率传输效率
- 评估耦合效率

## 语法

### LSF 语法
```lumerical
crosssection;                            # 计算当前选择结构的横截面
crosssection("parameter", value, ...);   # 计算横截面并指定参数
```

### Python API
```python
session.crosssection()                           # 计算当前选择结构的横截面
session.crosssection(parameter1=value1, parameter2=value2, ...)  # 计算横截面并指定参数
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `object` | string | 要计算横截面的对象名称。 | 可选 |
| `plane` | string | 横截面平面："xy", "xz", "yz"。 | 可选 |
| `position` | number | 横截面在指定轴上的位置（μm）。 | 可选 |
| `output` | string | 输出数据类型："E", "H", "P", "n_eff", "loss" 等。 | 可选 |
| `mode` | number/string | 模式编号或模式选择。 | 可选 |
| `wavelength` | number | 计算波长（μm）。 | 可选 |
| `frequency` | number | 计算频率（THz）。 | 可选 |
| `normalization` | string | 场归一化方式："peak", "power", "custom"。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 横截面中心的 x 坐标（μm）。 |
| `y` | number | 0 | 横截面中心的 y 坐标（μm）。 |
| `z` | number | 0 | 横截面中心的 z 坐标（μm）。 |
| `x span` | number | 1 | 横截面的 x 方向跨度（μm）。 |
| `y span` | number | 1 | 横截面的 y 方向跨度（μm）。 |
| `z span` | number | 1 | 横截面的 z 方向跨度（μm）。 |
| `plane` | string | "xy" | 横截面平面："xy", "xz", "yz"。 |
| `position` | number | 0 | 横截面在平面法向上的位置（μm）。 |
| `resolution` | number | 100 | 横截面网格分辨率（点数）。 |
| `wavelength` | number | 1.55 | 计算波长（μm）。 |
| `frequency` | number | 193.1 | 计算频率（THz）。 |
| `mode number` | number | 1 | 要计算的模式编号。 |
| `polarization` | string | "TE" | 偏振模式："TE", "TM", "both"。 |
| `field component` | string | "all" | 场分量："Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "all"。 |
| `normalization` | string | "peak" | 场归一化方式："peak", "power", "custom"。 |
| `output` | string | "E" | 输出数据类型："E"（电场），"H"（磁场），"P"（坡印廷矢量），"n_eff"（有效折射率），"loss"（损耗）。 |
| `overlap` | bool | false | 计算与参考场的重叠积分。 |
| `reference field` | string | "" | 参考场名称（用于重叠积分）。 |
| `background index` | number | 1.0 | 背景折射率。 |
| `material dispersion` | bool | true | 是否考虑材料色散。 |
| `waveguide dispersion` | bool | false | 是否计算波导色散。 |
| `group index` | bool | false | 是否计算群折射率。 |
| `effective area` | bool | false | 是否计算有效面积。 |
| `confinement factor` | bool | false | 是否计算限制因子。 |
| `power fraction` | bool | false | 是否计算功率分数。 |
| `save data` | bool | true | 是否保存计算结果。 |
| `data name` | string | "crosssection_data" | 保存数据的名称。 |
| `visualize` | bool | true | 是否可视化结果。 |
| `color scale` | string | "linear" | 颜色标度："linear", "log", "dB"。 |
| `color map` | string | "rainbow" | 颜色映射："rainbow", "hot", "cool", "gray"。 |

## 使用示例

### 示例 1：计算波导横截面的基本模式
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 创建硅波导
fdtd.addrect("Si_waveguide",
             x=0, y=0, z=0,
             x_span=0.5,    # 宽度 500 nm
             y_span=0.22,   # 高度 220 nm
             z_span=0,      # 2D 结构
             material="Si") # 硅材料

print("计算硅波导横截面...")

# 计算横截面（默认设置）
fdtd.crosssection(object="Si_waveguide",
                  plane="xy",
                  position=0,
                  wavelength=1.55,
                  mode=1,
                  polarization="TE")

# 获取计算结果
crosssection_data = fdtd.getresult("crosssection_data")
if crosssection_data:
    print("横截面计算结果:")
    print(f"  有效折射率: {crosssection_data.get('n_eff', 'N/A')}")
    print(f"  模式面积: {crosssection_data.get('effective_area', 'N/A')} μm²")
    
    # 获取场分布
    if 'E' in crosssection_data:
        E_field = crosssection_data['E']
        print(f"  电场数据形状: {E_field.shape}")
        
        # 计算模场直径（1/e² 强度）
        intensity = np.abs(E_field)**2
        max_intensity = np.max(intensity)
        threshold = max_intensity / np.e**2
        
        # 找到强度超过阈值的区域
        mask = intensity > threshold
        if np.any(mask):
            y_coords = np.linspace(-0.5, 0.5, intensity.shape[0])
            x_coords = np.linspace(-0.25, 0.25, intensity.shape[1])
            
            y_indices = np.where(np.any(mask, axis=1))[0]
            x_indices = np.where(np.any(mask, axis=0))[0]
            
            if len(y_indices) > 0 and len(x_indices) > 0:
                mfd_y = y_coords[y_indices[-1]] - y_coords[y_indices[0]]
                mfd_x = x_coords[x_indices[-1]] - x_coords[x_indices[0]]
                print(f"  模场直径 (y): {mfd_y:.3f} μm")
                print(f"  模场直径 (x): {mfd_x:.3f} μm")
```

### 示例 2：分析光纤中的多模特性
```python
import lumapi
import matplotlib.pyplot as plt

mode = lumapi.MODE()

# 创建阶跃折射率光纤
def create_step_index_fiber(name, core_radius=5, cladding_radius=25, 
                           n_core=1.45, n_cladding=1.44):
    """创建阶跃折射率光纤"""
    
    # 创建包层
    mode.addcircle(f"{name}_cladding",
                   x=0, y=0, z=0,
                   radius=cladding_radius,
                   material=f"user_defined_{n_cladding}",
                   index=n_cladding)
    
    # 创建纤芯
    mode.addcircle(f"{name}_core",
                   x=0, y=0, z=0,
                   radius=core_radius,
                   material=f"user_defined_{n_core}",
                   index=n_core)
    
    return f"{name}_core", f"{name}_cladding"

print("创建阶跃折射率光纤...")
core, cladding = create_step_index_fiber("SMF28", 
                                        core_radius=4.1,  # 4.1 μm 纤芯
                                        cladding_radius=62.5,  # 125 μm 直径
                                        n_core=1.450,  # 纤芯折射率
                                        n_cladding=1.444)  # 包层折射率

print(f"纤芯: {core}")
print(f"包层: {cladding}")

# 计算多个模式的横截面
num_modes = 5
modes_data = []

for mode_num in range(1, num_modes + 1):
    print(f"\n计算模式 {mode_num}...")
    
    # 计算横截面
    mode.crosssection(object=core,
                      plane="xy",
                      position=0,
                      wavelength=1.55,
                      mode=mode_num,
                      output="E",
                      polarization="both",
                      effective_area=True,
                      confinement_factor=True)
    
    # 获取结果
    data_name = f"crosssection_mode{mode_num}"
    result = mode.getresult(data_name)
    
    if result:
        n_eff = result.get('n_eff', 0)
        area = result.get('effective_area', 0)
        confinement = result.get('confinement_factor', 0)
        
        modes_data.append({
            'mode': mode_num,
            'n_eff': n_eff,
            'area': area,
            'confinement': confinement
        })
        
        print(f"  有效折射率: {n_eff:.6f}")
        print(f"  有效面积: {area:.2f} μm²")
        print(f"  限制因子: {confinement:.3f}")
        
        # 保存电场分布
        if 'E' in result:
            E_field = result['E']
            mode.set(f"E_mode{mode_num}", E_field)

# 分析模式特性
print("\n=== 光纤模式特性总结 ===")
print("模式 | 有效折射率 | 有效面积 (μm²) | 限制因子")
print("-----|------------|----------------|----------")

for data in modes_data:
    print(f"{data['mode']:4d} | {data['n_eff']:.6f} | {data['area']:14.2f} | {data['confinement']:.3f}")

# 计算 V 参数
wavelength = 1.55  # μm
core_radius = 4.1  # μm
n_core = 1.450
n_cladding = 1.444
NA = np.sqrt(n_core**2 - n_cladding**2)  # 数值孔径
V = 2 * np.pi * core_radius * NA / wavelength

print(f"\n光纤参数:")
print(f"  纤芯半径: {core_radius} μm")
print(f"  波长: {wavelength} μm")
print(f"  数值孔径: {NA:.4f}")
print(f"  V 参数: {V:.2f}")

# 估算模式数量
if V < 2.405:
    print("  单模条件: V < 2.405，应为单模光纤")
else:
    M_estimate = V**2 / 2  # 近似模式数
    print(f"  估算模式数: ~{int(M_estimate)}")
```

### 示例 3：光子晶体波导的横截面分析
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_photonic_crystal_waveguide(name, rows=10, cols=30, pitch=0.5, hole_radius=0.15, defect_width=3):
    """创建光子晶体波导（线缺陷波导）"""
    
    # 创建背景平板（硅）
    fdtd.addrect(f"{name}_slab",
                 x=0, y=0, z=0,
                 x_span=cols * pitch,
                 y_span=rows * pitch,
                 z_span=0.22,  # 220 nm 厚硅层
                 material="Si")
    
    holes = []
    
    # 创建光子晶体孔阵列（在中心留出线缺陷）
    for i in range(rows):
        for j in range(cols):
            # 跳过中心区域的孔，形成线缺陷波导
            if abs(i - rows//2) < defect_width//2:
                continue
                
            x_pos = (j - (cols-1)/2) * pitch
            y_pos = (i - (rows-1)/2) * pitch
            
            hole_name = f"{name}_hole_{i}_{j}"
            fdtd.addcircle(hole_name,
                          x=x_pos, y=y_pos, z=0,
                          radius=hole_radius,
                          material="Air",
                          z_span=0.22)
            
            holes.append(hole_name)
    
    return f"{name}_slab", holes

print("创建光子晶体波导...")
slab, holes = create_photonic_crystal_waveguide("PCW",
                                               rows=15, cols=50,
                                               pitch=0.42,  # 420 nm 晶格常数
                                               hole_radius=0.12,  # 120 nm 孔半径
                                               defect_width=3)  # 3行线缺陷

print(f"背景平板: {slab}")
print(f"空气孔数量: {len(holes)}")

# 计算光子晶体带隙
print("\n计算光子晶体带隙横截面...")

# 在不同位置计算横截面，分析模式演化
positions = [-5, 0, 5]  # 沿波导不同位置
results = []

for i, pos in enumerate(positions):
    print(f"\n位置 x = {pos} μm:")
    
    # 计算横截面
    fdtd.crosssection(object=slab,
                      plane="yz",  # 垂直于传播方向
                      position=pos,
                      wavelength=1.55,
                      mode=1,
                      output="E",
                      field_component="all",
                      effective_area=True,
                      confinement_factor=True)
    
    # 获取结果
    data_name = f"crosssection_pos{pos}"
    result = fdtd.getresult(data_name)
    
    if result:
        n_eff = result.get('n_eff', 0)
        area = result.get('effective_area', 0)
        confinement = result.get('confinement_factor', 0)
        
        results.append({
            'position': pos,
            'n_eff': n_eff,
            'area': area,
            'confinement': confinement
        })
        
        print(f"  有效折射率: {n_eff:.4f}")
        print(f"  模式面积: {area:.2f} μm²")
        print(f"  限制因子: {confinement:.3f}")

# 分析模式特性变化
print("\n=== 沿波导的模式特性变化 ===")
print("位置 (μm) | 有效折射率 | 模式面积 (μm²) | 限制因子")
print("----------|------------|----------------|----------")

for res in results:
    print(f"{res['position']:8.1f} | {res['n_eff']:.6f} | {res['area']:14.2f} | {res['confinement']:.3f}")

# 计算群速度色散
if len(results) >= 2:
    # 简单估算群折射率变化
    positions = [r['position'] for r in results]
    n_effs = [r['n_eff'] for r in results]
    
    # 使用中心差分计算导数
    if len(results) == 3:
        delta_x = positions[2] - positions[0]
        delta_n = n_effs[2] - n_effs[0]
        
        if delta_x != 0:
            dn_dx = delta_n / delta_x
            print(f"\n有效折射率梯度: {dn_dx:.6f} μm⁻¹")
            
            # 估算群速度变化
            c = 299.792  # μm/ps
            v_g_estimate = c / (n_effs[1] + wavelength * dn_dx)  # 简单估算
            print(f"  估算群速度: {v_g_estimate:.2f} μm/ps")
            print(f"  群折射率: {c/v_g_estimate:.3f}")

# 计算带隙频率
pitch = 0.42
hole_radius = 0.12
fill_factor = np.pi * hole_radius**2 / pitch**2

print(f"\n光子晶体参数:")
print(f"  晶格常数: {pitch} μm")
print(f"  孔半径: {hole_radius} μm")
print(f"  填充因子: {fill_factor:.2%}")

# 简单带隙估算（基于经验公式）
n_si = 3.48  # 硅在 1.55 μm 的折射率
gap_center_wavelength = 2 * pitch * n_si / np.sqrt(3)  # 三角晶格
gap_width_estimate = 0.2 * gap_center_wavelength  # 20% 相对带宽

print(f"  估算带隙中心波长: {gap_center_wavelength:.3f} μm")
print(f"  估算带隙宽度: {gap_width_estimate:.3f} μm")
print(f"  带隙范围: [{gap_center_wavelength - gap_width_estimate/2:.3f}, {gap_center_wavelength + gap_width_estimate/2:.3f}] μm")

# 检查工作波长是否在带隙内
if abs(wavelength - gap_center_wavelength) < gap_width_estimate/2:
    print(f"  ✓ 工作波长 {wavelength} μm 在带隙内")
else:
    print(f"  ✗ 工作波长 {wavelength} μm 不在带隙内")
```

### 示例 4：计算等离子体纳米结构的场增强
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 创建金纳米颗粒二聚体
def create_gold_dimer(name, gap=10, radius=40, height=40):
    """创建金纳米颗粒二聚体（纳米天线）"""
    
    # 第一个金纳米颗粒
    fdtd.addcircle(f"{name}_particle1",
                   x=-gap/2 - radius, y=0, z=0,
                   radius=radius,
                   material="Au (Gold) - Johnson and Christy",
                   z_span=height)
    
    # 第二个金纳米颗粒
    fdtd.addcircle(f"{name}_particle2",
                   x=gap/2 + radius, y=0, z=0,
                   radius=radius,
                   material="Au (Gold) - Johnson and Christy",
                   z_span=height)
    
    return f"{name}_particle1", f"{name}_particle2"

print("创建金纳米颗粒二聚体...")
particle1, particle2 = create_gold_dimer("nanoantenna",
                                        gap=10,  # 10 nm 间隙
                                        radius=40,  # 40 nm 半径
                                        height=40)  # 40 nm 高度

print(f"纳米颗粒 1: {particle1}")
print(f"纳米颗粒 2: {particle2}")

# 计算间隙区域的横截面场增强
print("\n计算纳米间隙场增强...")

# 在多个波长计算
wavelengths = [400, 500, 600, 700, 800]  # nm
enhancement_factors = []

for wl_nm in wavelengths:
    wl_um = wl_nm / 1000  # 转换为 μm
    
    print(f"\n波长: {wl_nm} nm")
    
    # 计算间隙中心的横截面
    fdtd.crosssection(object=particle1,  # 选择其中一个颗粒
                      plane="xy",
                      position=0,  # 间隙中心
                      x_span=30,   # 30 nm 扫描区域
                      y_span=30,
                      wavelength=wl_um,
                      output="E",
                      field_component="all",
                      normalization="peak")
    
    # 获取电场数据
    data_name = "crosssection_data"
    result = fdtd.getresult(data_name)
    
    if result and 'E' in result:
        E_field = result['E']
        
        # 计算场增强因子（与入射场比较）
        # 假设入射场为单位强度
        E_magnitude = np.abs(E_field)
        max_enhancement = np.max(E_magnitude)**2  # 强度增强
        
        # 找到最大增强位置
        max_idx = np.unravel_index(np.argmax(E_magnitude), E_magnitude.shape)
        
        enhancement_factors.append({
            'wavelength': wl_nm,
            'enhancement': max_enhancement,
            'max_position': max_idx
        })
        
        print(f"  最大场增强: {max_enhancement:.1f}×")
        print(f"  最大场位置: 索引 {max_idx}")

# 分析共振特性
print("\n=== 场增强频谱分析 ===")
print("波长 (nm) | 场增强因子 | 共振特性")
print("----------|------------|----------")

max_enhancement = 0
resonant_wavelength = 0

for ef in enhancement_factors:
    wl = ef['wavelength']
    enh = ef['enhancement']
    
    # 判断是否为共振峰
    resonance_note = ""
    if enh > 10:  # 强增强
        resonance_note = "强共振"
    elif enh > 3:
        resonance_note = "弱共振"
    else:
        resonance_note = "非共振"
    
    print(f"{wl:8d} | {enh:10.1f}× | {resonance_note}")
    
    if enh > max_enhancement:
        max_enhancement = enh
        resonant_wavelength = wl

print(f"\n最大增强: {max_enhancement:.1f}× 在 {resonant_wavelength} nm")

# 计算等离子体共振品质因子
if len(enhancement_factors) >= 3:
    # 寻找半高全宽（FWHM）
    half_max = max_enhancement / 2
    wavelengths = [ef['wavelength'] for ef in enhancement_factors]
    enhancements = [ef['enhancement'] for ef in enhancement_factors]
    
    # 插值寻找 FWHM 点
    try:
        # 简单线性插值
        idx_above = [i for i, enh in enumerate(enhancements) if enh > half_max]
        if len(idx_above) >= 2:
            left_idx = idx_above[0]
            right_idx = idx_above[-1]
            
            # 如果有精确点，使用精确值
            left_wl = wavelengths[left_idx]
            right_wl = wavelengths[right_idx]
            
            fwhm = right_wl - left_wl
            Q_factor = resonant_wavelength / fwhm if fwhm > 0 else 0
            
            print(f"  共振 FWHM: {fwhm:.1f} nm")
            print(f"  品质因子 Q: {Q_factor:.1f}")
    except:
        print("  无法计算 FWHM")

# 计算热点尺寸
print("\n计算热点尺寸...")
resonant_data = next((ef for ef in enhancement_factors if ef['wavelength'] == resonant_wavelength), None)

if resonant_data and 'max_position' in resonant_data:
    # 重新计算共振波长的详细场分布
    fdtd.crosssection(object=particle1,
                      plane="xy",
                      position=0,
                      x_span=50,  # 50 nm 区域
                      y_span=50,
                      wavelength=resonant_wavelength/1000,
                      output="E",
                      resolution=200)  # 高分辨率
    
    result = fdtd.getresult("crosssection_data")
    if result and 'E' in result:
        E_field = result['E']
        intensity = np.abs(E_field)**2
        max_intensity = np.max(intensity)
        
        # 计算热点面积（强度 > 10% 最大强度）
        threshold = 0.1 * max_intensity
        hotspot_mask = intensity > threshold
        hotspot_area = np.sum(hotspot_mask) * (50/200)**2  # 每个像素的面积 (nm²)
        
        # 计算等效直径
        equivalent_diameter = 2 * np.sqrt(hotspot_area / np.pi)
        
        print(f"  热点面积: {hotspot_area:.1f} nm²")
        print(f"  等效直径: {equivalent_diameter:.1f} nm")
        print(f"  热点强度范围: {np.min(intensity[hotspot_mask]):.2f} - {max_intensity:.2f}")
```

### 示例 5：高级横截面分析工具类
```python
import lumapi
import numpy as np
from scipy import integrate

class CrossSectionAnalyzer:
    """高级横截面分析工具"""
    
    def __init__(self, session):
        self.session = session
        
    def analyze_waveguide_modes(self, waveguide_name, wavelengths, num_modes=3):
        """分析波导在不同波长下的模式特性"""
        
        results = {}
        
        for wl in wavelengths:
            print(f"分析波长 {wl} μm...")
            
            wavelength_results = []
            for mode_num in range(1, num_modes + 1):
                # 计算横截面
                self.session.crosssection(object=waveguide_name,
                                         plane="xy",
                                         position=0,
                                         wavelength=wl,
                                         mode=mode_num,
                                         output="E",
                                         effective_area=True,
                                         confinement_factor=True,
                                         group_index=True)
                
                # 获取结果
                data_name = f"crosssection_wl{wl}_mode{mode_num}"
                result = self.session.getresult(data_name)
                
                if result:
                    mode_data = {
                        'mode': mode_num,
                        'n_eff': result.get('n_eff', 0),
                        'n_g': result.get('group_index', 0),
                        'A_eff': result.get('effective_area', 0),
                        'confinement': result.get('confinement_factor', 0)
                    }
                    
                    # 计算色散参数
                    if 'E' in result:
                        E_field = result['E']
                        mode_data['field_shape'] = E_field.shape
                        
                        # 计算模场不对称性
                        if E_field.ndim == 2:
                            asymmetry = self._calculate_field_asymmetry(E_field)
                            mode_data['asymmetry'] = asymmetry
                    
                    wavelength_results.append(mode_data)
            
            results[wl] = wavelength_results
        
        return results
    
    def _calculate_field_asymmetry(self, field):
        """计算场分布的不对称性"""
        
        intensity = np.abs(field)**2
        
        # 计算质心
        y_indices = np.arange(field.shape[0])
        x_indices = np.arange(field.shape[1])
        
        total_power = np.sum(intensity)
        if total_power == 0:
            return 0
        
        y_center = np.sum(y_indices[:, np.newaxis] * intensity) / total_power
        x_center = np.sum(x_indices * intensity.sum(axis=0)) / total_power
        
        # 计算二阶矩（方差）
        y_variance = np.sum((y_indices[:, np.newaxis] - y_center)**2 * intensity) / total_power
        x_variance = np.sum((x_indices - x_center)**2 * intensity.sum(axis=0)) / total_power
        
        # 不对称性定义为方差比
        asymmetry = abs(y_variance - x_variance) / max(y_variance, x_variance)
        
        return asymmetry
    
    def calculate_coupling_efficiency(self, source_waveguide, target_waveguide, 
                                     wavelength=1.55, mode=1):
        """计算两个波导之间的耦合效率"""
        
        # 计算源波导模式
        self.session.crosssection(object=source_waveguide,
                                 plane="xy",
                                 position=0,
                                 wavelength=wavelength,
                                 mode=mode,
                                 output="E",
                                 normalization="power")
        
        source_result = self.session.getresult("crosssection_data")
        if not source_result or 'E' not in source_result:
            return 0
        
        E_source = source_result['E']
        
        # 计算目标波导模式
        self.session.crosssection(object=target_waveguide,
                                 plane="xy",
                                 position=0,
                                 wavelength=wavelength,
                                 mode=mode,
                                 output="E",
                                 normalization="power")
        
        target_result = self.session.getresult("crosssection_data")
        if not target_result or 'E' not in target_result:
            return 0
        
        E_target = target_result['E']
        
        # 确保场尺寸匹配
        if E_source.shape != E_target.shape:
            # 调整尺寸（简单插值）
            from scipy import ndimage
            zoom_factor = (E_target.shape[0]/E_source.shape[0], 
                          E_target.shape[1]/E_source.shape[1])
            E_source_resized = ndimage.zoom(E_source, zoom_factor)
            
            if E_source_resized.shape != E_target.shape:
                # 裁剪或填充
                min_shape = (min(E_source_resized.shape[0], E_target.shape[0]),
                            min(E_source_resized.shape[1], E_target.shape[1]))
                E_source_cropped = E_source_resized[:min_shape[0], :min_shape[1]]
                E_target_cropped = E_target[:min_shape[0], :min_shape[1]]
                
                E_source_final = E_source_cropped
                E_target_final = E_target_cropped
            else:
                E_source_final = E_source_resized
                E_target_final = E_target
        else:
            E_source_final = E_source
            E_target_final = E_target
        
        # 计算重叠积分（耦合效率）
        overlap_integral = np.abs(np.sum(E_source_final.conj() * E_target_final))**2
        source_power = np.sum(np.abs(E_source_final)**2)
        target_power = np.sum(np.abs(E_target_final)**2)
        
        coupling_efficiency = overlap_integral / (source_power * target_power)
        
        return coupling_efficiency
    
    def analyze_tapered_waveguide(self, waveguide_base_name, taper_length, 
                                 start_width, end_width, num_points=10):
        """分析锥形波导的模式演化"""
        
        results = []
        
        for i in range(num_points + 1):
            # 计算当前位置
            position = i * taper_length / num_points
            width = start_width + (end_width - start_width) * i / num_points
            
            print(f"位置 {position:.1f} μm, 宽度 {width:.2f} μm")
            
            # 计算横截面
            self.session.crosssection(object=waveguide_base_name,
                                     plane="yz",
                                     position=position,
                                     wavelength=1.55,
                                     mode=1,
                                     output="n_eff")  # 只获取有效折射率
            
            result = self.session.getresult("crosssection_data")
            if result and 'n_eff' in result:
                n_eff = result['n_eff']
                
                results.append({
                    'position': position,
                    'width': width,
                    'n_eff': n_eff
                })
        
        return results

# 使用示例
fdtd = lumapi.FDTD()

# 创建测试波导
fdtd.addrect("test_wg",
             x=0, y=0, z=0,
             x_span=0.5, y_span=0.22, z_span=0,
             material="Si")

print("创建横截面分析器...")
analyzer = CrossSectionAnalyzer(fdtd)

# 分析波导模式
print("\n分析波导模式...")
wavelengths = [1.3, 1.4, 1.5, 1.6, 1.7]
mode_results = analyzer.analyze_waveguide_modes("test_wg", wavelengths, num_modes=2)

# 显示结果
print("\n=== 波导模式特性 ===")
for wl, modes in mode_results.items():
    print(f"\n波长: {wl} μm")
    for mode in modes:
        print(f"  模式 {mode['mode']}: n_eff={mode['n_eff']:.4f}, "
              f"n_g={mode.get('n_g', 'N/A')}, "
              f"A_eff={mode['A_eff']:.2f} μm²")

# 创建第二个波导（用于耦合计算）
fdtd.addrect("test_wg2",
             x=2, y=0, z=0,
             x_span=0.6, y_span=0.25, z_span=0,
             material="Si")

# 计算耦合效率
print("\n计算波导间耦合效率...")
coupling = analyzer.calculate_coupling_efficiency("test_wg", "test_wg2", wavelength=1.55)
print(f"耦合效率: {coupling*100:.2f}%")

# 分析锥形波导（模拟）
print("\n分析锥形波导模式演化...")
taper_results = analyzer.analyze_tapered_waveguide("test_wg", 
                                                  taper_length=10,
                                                  start_width=0.5,
                                                  end_width=0.2,
                                                  num_points=5)

print("位置 (μm) | 宽度 (μm) | 有效折射率")
print("----------|-----------|------------")
for res in taper_results:
    print(f"{res['position']:8.1f} | {res['width']:9.2f} | {res['n_eff']:.6f}")
```

## 注意事项

1. **计算资源**：横截面计算可能消耗大量内存和计算时间，特别是高分辨率和多个模式的计算。

2. **网格收敛**：确保仿真网格足够精细以获得准确的横截面结果。通常需要每个波长至少 10-20 个网格点。

3. **边界条件**：横截面计算受仿真区域边界条件影响。确保边界足够远以避免边界反射影响结果。

4. **材料模型**：使用准确的材料模型，特别是对于金属和色散材料。Lumerical 的材料数据库提供了多种材料模型。

5. **模式选择**：对于多模波导，确保选择正确的模式编号。可以使用 `findmodes` 命令先找到所有模式。

6. **偏振**：明确指定偏振状态（TE/TM）以获得正确结果。某些结构可能支持混合偏振模式。

7. **归一化**：注意场归一化设置。不同归一化方式会影响重叠积分和耦合效率计算。

8. **数据保存**：默认情况下，横截面数据会保存到项目文件中。可以通过 `data name` 参数指定保存名称。

9. **可视化**：使用 `visualize` 参数可以即时查看横截面结果。这对于调试和初步分析非常有用。

10. **与频域求解器的关系**：`crosssection` 命令通常与频域求解器（如 MODE Solutions）结合使用。在时域仿真（FDTD）中，可能需要先运行仿真获取场数据。

## 错误处理

使用 `crosssection` 命令时可能遇到的常见错误及其解决方案：

### 1. 仿真数据不存在错误
- **错误信息**: `"No simulation data available"`
- **原因**: 尝试计算横截面但未运行仿真或未保存场数据
- **解决方案**:
  ```lumerical
  // 检查并运行仿真
  function safe_crosssection(monitor_name)
      if (!exists(monitor_name)) {
          ? "错误: 监视器不存在";
          return nan;
      }
      
      // 检查是否有数据
      data_available = get(monitor_name, "data recorded");
      if (!data_available) {
          ? "警告: 无仿真数据，运行仿真...";
          run;
          data_available = get(monitor_name, "data recorded");
          if (!data_available) {
              ? "错误: 仿真后仍无数据";
              return nan;
          }
      }
      
      // 计算横截面
      return crosssection(monitor_name);
  end
  ```

### 2. 无效的平面或方向错误
- **错误信息**: `"Invalid plane or orientation"`
- **原因**: 指定的横截平面参数无效
- **解决方案**:
  ```lumerical
  // 验证平面参数
  function validate_plane(plane, position)
      valid_planes = {"x", "y", "z", "xy", "xz", "yz"};
      if (!find(valid_planes, plane)) {
          ? "错误: 无效平面，使用 'x', 'y', 'z', 'xy', 'xz', 或 'yz'";
          plane = "xy";  // 默认值
      }
      
      // 检查位置是否在仿真区域内
      sim_region = get("FDTD", "simulation region");
      if (position < sim_region(1) || position > sim_region(2)) {
          ? "警告: 位置在仿真区域外，调整到边界";
          position = max(min(position, sim_region(2)), sim_region(1));
      }
      
      return {plane, position};
  end
  ```

### 3. 内存不足错误
- **错误信息**: `"Out of memory"`
- **原因**: 横截面数据量太大
- **解决方案**:
  ```lumerical
  // 分块计算横截面
  function chunked_crosssection(monitor_name, chunk_size=100)
      // 获取数据维度
      data_size = get(monitor_name, "data size");
      
      // 分块处理
      results = [];
      for (i = 1:chunk_size:data_size(1)) {
          end_i = min(i + chunk_size - 1, data_size(1));
          // 计算部分横截面
          partial = crosssection(monitor_name, "range", [i, end_i]);
          results = [results; partial];
          ? "处理块 " + num2str(i) + " 到 " + num2str(end_i);
      }
      
      return results;
  end
  ```

### 4. 数据维度不匹配错误
- **错误信息**: `"Data dimension mismatch"`
- **原因**: 请求的横截面与数据维度不兼容
- **解决方案**:
  ```lumerical
  // 自动调整横截平面
  function auto_crosssection(monitor_name)
      // 获取数据维度
      data_size = get(monitor_name, "data size");
      
      // 根据维度选择最佳平面
      if (data_size(3) > 1) {
          // 3D 数据，使用 xy 平面
          plane = "xy";
          position = data_size(3) / 2;  // 中间位置
      } elseif (data_size(2) > 1) {
          // 2D 数据，使用 xz 平面
          plane = "xz";
          position = data_size(2) / 2;
      } else {
          // 1D 数据，使用线性横截面
          plane = "x";
          position = 0;
      }
      
      ? "自动选择平面: " + plane + "，位置: " + num2str(position);
      return crosssection(monitor_name, plane, position);
  end
  ```

### 5. Python API 错误处理示例
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def safe_crosssection_python(monitor_name, plane="xy", position=0):
    """安全的横截面计算函数"""
    try:
        # 检查监视器是否存在
        all_monitors = fdtd.getall("monitor")
        if monitor_name not in all_monitors:
            raise ValueError(f"监视器 '{monitor_name}' 不存在")
        
        # 检查是否有数据
        data_recorded = fdtd.get(monitor_name, "data recorded")
        if not data_recorded:
            print("警告: 无仿真数据，运行仿真...")
            fdtd.run()
            data_recorded = fdtd.get(monitor_name, "data recorded")
            if not data_recorded:
                raise RuntimeError(f"监视器 '{monitor_name}' 无数据")
        
        # 计算横截面
        result = fdtd.crosssection(monitor_name, plane, position)
        
        # 验证结果
        if np.any(np.isnan(result)):
            print("警告: 结果包含 NaN")
            
        if np.any(np.isinf(result)):
            print("警告: 结果包含无穷大")
        
        return result
        
    except lumapi.LumapiError as e:
        print(f"Lumerical API 错误: {e}")
        # 尝试恢复
        if "plane" in str(e).lower():
            print("尝试默认平面 'xy'...")
            return fdtd.crosssection(monitor_name, "xy", 0)
        raise
    
    except Exception as e:
        print(f"未知错误: {e}")
        raise

# 使用示例
try:
    crosssection_data = safe_crosssection_python("monitor1", "xy", 0)
    print(f"横截面数据形状: {crosssection_data.shape}")
except Exception as e:
    print(f"横截面计算失败: {e}")
```

### 6. 调试建议
1. **验证仿真状态**: 确保仿真已运行并保存了所需数据
2. **检查监视器设置**: 确认监视器类型支持横截面分析
3. **验证平面参数**: 确保平面和位置在仿真区域内
4. **监控内存使用**: 对于大横截面，监控内存消耗
5. **逐步调试**: 分步骤验证数据获取、平面选择和计算过程

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 需要先运行仿真获取场数据 |
| MODE Solutions | ✅ 完全支持 | 原生支持横截面分析 |
| DEVICE | ⚠️ 有限支持 | 主要用于载流子分布分析 |
| INTERCONNECT | ❌ 不支持 | INTERCONNECT 使用电路模型而非场分析 |

## 相关命令

- `findmodes` - 寻找结构中的模式
- `mode` - 计算模式特性
- `overlap` - 计算场重叠积分
- `getelectric` - 获取电场数据
- `getmagnetic` - 获取磁场数据
- `getpower` - 获取功率数据
- `getdata` - 获取仿真数据
- `visualize` - 可视化场分布
- `export` - 导出横截面数据

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本横截面操作和示例 |
| 1.1 | 2026-01-31 | 添加错误处理章节、版本历史和参考 |
| 1.2 | 2026-01-31 | 完善数据验证和高级分析示例 |

## 参考

1. Lumerical Script Language Reference - Analysis Commands
2. Lumerical Python API Documentation - `crosssection()` Method
3. Computational Electromagnetics: The Finite-Difference Time-Domain Method
4. Optical Waveguide Analysis Using Numerical Methods
5. IEEE Transactions on Microwave Theory and Techniques - Cross-Section Analysis

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*