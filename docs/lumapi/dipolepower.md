# `dipolepower` - 计算偶极子功率

## 概述

`dipolepower` 命令用于计算 FDTD 仿真中偶极子光源的辐射功率、吸收功率和散射功率。该命令是分析偶极子与纳米结构相互作用的关键工具，特别在等离子体增强、荧光增强和量子发射器研究中广泛应用。

主要功能：
- **总辐射功率**：计算偶极子的总辐射功率
- **吸收功率**：计算被周围材料吸收的功率
- **散射功率**：计算被纳米结构散射的功率
- **Purcell 因子**：计算辐射增强因子
- **量子效率**：计算辐射量子效率
- **方向性**：分析辐射方向图

典型应用：
- 荧光分子辐射增强分析
- 等离子体纳米天线效率计算
- 量子点发光效率优化
- 光子晶体 Purcell 因子计算
- 近场能量转移研究

## 语法

### LSF 语法
```lumerical
dipolepower;                                       # 计算当前偶极子的功率
dipolepower("dipole_name");                        # 计算指定偶极子的功率
dipolepower("dipole_name", property, value, ...);  # 计算功率并指定参数
```

### Python API
```python
session.dipolepower()                                       # 计算当前偶极子的功率
session.dipolepower("dipole_name")                         # 计算指定偶极子的功率
session.dipolepower("dipole_name", property1=value1, property2=value2, ...)  # 计算功率并指定参数
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `dipole_name` | string | 偶极子源的名称。 | 可选 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength` | number | 1.0 | 计算波长（μm）。 |
| `frequency` | number | 300 | 计算频率（THz）。 |
| `position` | vector | [0,0,0] | 偶极子位置（μm）。 |
| `polarization` | string | "x" | 偏振方向："x", "y", "z"。 |
| `dipole type` | string | "electric" | 偶极子类型："electric", "magnetic"。 |
| `monitor` | string | "" | 使用的功率监视器名称。 |
| `monitor type` | string | "2D" | 监视器类型："2D", "3D", "linear"。 |
| `monitor position` | vector | [0,0,0] | 监视器位置（μm）。 |
| `monitor size` | vector | [1,1,1] | 监视器尺寸（μm）。 |
| `integration method` | string | "auto" | 积分方法："auto", "trapezoidal", "simpson"。 |
| `normalization` | string | "source" | 归一化方式："source", "total", "none"。 |
| `include absorption` | bool | true | 是否包含吸收功率。 |
| `include scattering` | bool | true | 是否包含散射功率。 |
| `include radiation` | bool | true | 是否包含辐射功率。 |
| `calculate Purcell` | bool | false | 是否计算 Purcell 因子。 |
| `calculate quantum efficiency` | bool | false | 是否计算量子效率。 |
| `calculate directivity` | bool | false | 是否计算方向性。 |
| `save data` | bool | true | 是否保存计算结果。 |
| `data name` | string | "dipolepower_data" | 保存数据的名称。 |
| `visualize` | bool | true | 是否可视化结果。 |
| `color scale` | string | "linear" | 颜色标度："linear", "log", "dB"。 |
| `color map` | string | "rainbow" | 颜色映射："rainbow", "hot", "cool", "gray"。 |

## 使用示例

### 示例 1：计算偶极子基本功率特性
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("计算偶极子功率特性...")

# 创建偶极子源
fdtd.dipole("test_dipole",
           x=0, y=0, z=0,
           wavelength=1.55,
           power=1e-6,  # 1 μW 输入功率
           dipole_type="electric",
           injection_axis="z")

# 计算功率特性
fdtd.dipolepower("test_dipole",
                wavelength=1.55,
                include_absorption=True,
                include_scattering=True,
                include_radiation=True,
                calculate_Purcell=True,
                calculate_quantum_efficiency=True)

# 获取计算结果
power_data = fdtd.getresult("dipolepower_data")
if power_data:
    print("功率特性分析:")
    print(f"  输入功率: {1e6:.3f} μW")
    
    if 'total_power' in power_data:
        total_power = power_data['total_power']
        print(f"  总输出功率: {total_power*1e6:.3f} μW")
        print(f"  功率效率: {total_power/1e-6*100:.2f}%")
    
    if 'radiation_power' in power_data:
        rad_power = power_data['radiation_power']
        print(f"  辐射功率: {rad_power*1e6:.3f} μW")
    
    if 'absorption_power' in power_data:
        abs_power = power_data['absorption_power']
        print(f"  吸收功率: {abs_power*1e6:.3f} μW")
    
    if 'scattering_power' in power_data:
        scat_power = power_data['scattering_power']
        print(f"  散射功率: {scat_power*1e6:.3f} μW")
    
    if 'Purcell_factor' in power_data:
        Purcell = power_data['Purcell_factor']
        print(f"  Purcell 因子: {Purcell:.2f}")
        print(f"  辐射增强: {Purcell:.1f}×")
    
    if 'quantum_efficiency' in power_data:
        QE = power_data['quantum_efficiency']
        print(f"  量子效率: {QE*100:.2f}%")

# 验证功率守恒
if all(key in power_data for key in ['radiation_power', 'absorption_power', 'scattering_power']):
    total_calculated = (power_data.get('radiation_power', 0) + 
                       power_data.get('absorption_power', 0) + 
                       power_data.get('scattering_power', 0))
    input_power = 1e-6
    
    conservation_error = abs(total_calculated - input_power) / input_power
    print(f"\n功率守恒检查:")
    print(f"  计算总功率: {total_calculated*1e6:.3f} μW")
    print(f"  输入功率: {input_power*1e6:.3f} μW")
    print(f"  相对误差: {conservation_error*100:.2f}%")
    
    if conservation_error < 0.01:  # 1% 误差阈值
        print("  ✓ 功率守恒良好")
    else:
        print("  ⚠️ 功率守恒误差较大")
```

### 示例 2：分析等离子体纳米天线对偶极子功率的影响
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("分析等离子体纳米天线增强...")

# 创建金纳米球天线
def create_gold_nanosphere(name, radius=40):
    """创建金纳米球"""
    
    fdtd.addsphere(f"{name}_sphere",
                   x=0, y=0, z=0,
                   radius=radius*0.001,  # 转换为 μm
                   material="Au (Gold) - Johnson and Christy")
    
    return f"{name}_sphere"

# 创建纳米天线
nanosphere = create_gold_nanosphere("gold_nanosphere", radius=40)
print(f"创建的金纳米球: {nanosphere}")
print(f"半径: 40 nm")

# 在纳米球表面放置偶极子
def place_dipole_near_sphere(name, sphere_name, distance=5, wavelength=0.6):
    """在纳米球附近放置偶极子"""
    
    # 获取纳米球位置和半径
    sphere_props = fdtd.get(sphere_name)
    sphere_radius = sphere_props.get("radius", 0)
    sphere_x = sphere_props.get("x", 0)
    
    # 计算偶极子位置（纳米球表面外指定距离）
    dipole_x = sphere_x + sphere_radius + distance*0.001  # 距离转换为 μm
    
    # 创建偶极子
    dipole_name = f"{name}_dipole"
    fdtd.dipole(dipole_name,
               x=dipole_x, y=0, z=0,
               wavelength=wavelength,
               power=1e-6,
               dipole_type="electric",
               injection_axis="x",  # 径向偏振
               polarization_angle=0)
    
    print(f"偶极子位置: x={dipole_x*1000:.1f} nm (表面外 {distance} nm)")
    
    return dipole_name, dipole_x

# 放置偶极子
dipole_name, dipole_x = place_dipole_near_sphere("enhanced", nanosphere, 
                                                distance=5,  # 5 nm 间隙
                                                wavelength=0.6)

# 计算有纳米天线时的功率
print("\n计算有纳米天线时的功率...")
fdtd.dipolepower(dipole_name,
                wavelength=0.6,
                calculate_Purcell=True,
                calculate_quantum_efficiency=True,
                calculate_directivity=True)

power_with_antenna = fdtd.getresult("dipolepower_data")

# 创建参考：没有纳米天线的情况
fdtd_ref = lumapi.FDTD()
fdtd_ref.dipole("reference_dipole",
               x=dipole_x, y=0, z=0,
               wavelength=0.6,
               power=1e-6,
               dipole_type="electric",
               injection_axis="x")

print("计算没有纳米天线时的功率...")
fdtd_ref.dipolepower("reference_dipole",
                    wavelength=0.6,
                    calculate_Purcell=False)

power_without_antenna = fdtd_ref.getresult("dipolepower_data")

# 比较分析
print("\n=== 等离子体增强分析 ===")

if power_with_antenna and power_without_antenna:
    # 提取关键参数
    P_rad_with = power_with_antenna.get('radiation_power', 0)
    P_rad_without = power_without_antenna.get('radiation_power', 0)
    
    P_abs_with = power_with_antenna.get('absorption_power', 0)
    P_abs_without = power_without_antenna.get('absorption_power', 0)
    
    # 计算增强因子
    if P_rad_without > 0:
        enhancement_rad = P_rad_with / P_rad_without
        enhancement_abs = P_abs_with / P_abs_without if P_abs_without > 0 else float('inf')
        
        print(f"辐射功率:")
        print(f"  有天线: {P_rad_with*1e6:.3f} μW")
        print(f"  无天线: {P_rad_without*1e6:.3f} μW")
        print(f"  增强因子: {enhancement_rad:.1f}×")
        
        print(f"\n吸收功率:")
        print(f"  有天线: {P_abs_with*1e6:.3f} μW")
        print(f"  无天线: {P_abs_without*1e6:.3f} μW")
        if P_abs_without > 0:
            print(f"  增强因子: {enhancement_abs:.1f}×")
        
        # 计算 Purcell 因子
        if 'Purcell_factor' in power_with_antenna:
            Purcell = power_with_antenna['Purcell_factor']
            print(f"\nPurcell 因子: {Purcell:.2f}")
            
            # Purcell 因子与增强因子的关系
            print(f"  理论关系: Purcell ∝ 辐射增强")
            print(f"  测量增强: {enhancement_rad:.1f}×")
            print(f"  差异: {abs(Purcell - enhancement_rad)/enhancement_rad*100:.1f}%")
        
        # 计算量子效率
        if 'quantum_efficiency' in power_with_antenna:
            QE_with = power_with_antenna['quantum_efficiency']
            print(f"\n量子效率:")
            print(f"  有天线: {QE_with*100:.2f}%")
            
            # 理想情况下的量子效率（无损耗材料）
            ideal_QE = 1.0  # 假设无损耗
            
            print(f"  理想量子效率: {ideal_QE*100:.2f}%")
            print(f"  效率降低: {(ideal_QE - QE_with)*100:.2f}% (由于金属吸收)")
        
        # 分析方向性变化
        if 'directivity' in power_with_antenna:
            directivity_data = power_with_antenna['directivity']
            print(f"\n方向性分析:")
            
            if isinstance(directivity_data, dict):
                max_directivity = directivity_data.get('max', 0)
                avg_directivity = directivity_data.get('average', 0)
                
                print(f"  最大方向性: {max_directivity:.2f}")
                print(f"  平均方向性: {avg_directivity:.2f}")
                
                # 方向性增强意味着辐射更定向
                if max_directivity > 1.5:  # 经验阈值
                    print(f"  ✓ 辐射方向性显著增强")
                else:
                    print(f"  ⚠️ 辐射方向性变化不大")
    
    # 计算总功率效率
    total_power_with = P_rad_with + P_abs_with
    total_power_without = P_rad_without + (P_abs_without if P_abs_without > 0 else 0)
    
    input_power = 1e-6
    efficiency_with = total_power_with / input_power
    efficiency_without = total_power_without / input_power
    
    print(f"\n总功率效率:")
    print(f"  有天线: {efficiency_with*100:.2f}%")
    print(f"  无天线: {efficiency_without*100:.2f}%")
    print(f"  效率变化: {(efficiency_with - efficiency_without)*100:.2f}%")

# 分析波长依赖性
print("\n=== 波长依赖性分析 ===")
wavelengths = [0.4, 0.5, 0.6, 0.7, 0.8]  # 400-800 nm
enhancement_results = []

for wl in wavelengths:
    print(f"\n波长: {wl*1000:.0f} nm")
    
    # 重新计算当前波长的功率
    fdtd.dipolepower(dipole_name,
                    wavelength=wl,
                    calculate_Purcell=True)
    
    power_data = fdtd.getresult("dipolepower_data")
    
    if power_data:
        P_rad = power_data.get('radiation_power', 0)
        Purcell = power_data.get('Purcell_factor', 1)
        
        # 简单参考：自由空间辐射功率（与波长^4成反比）
        P_ref = 1e-6 * (0.6/wl)**4  # 以 600 nm 为参考
        
        enhancement = P_rad / P_ref if P_ref > 0 else 0
        
        enhancement_results.append({
            'wavelength': wl,
            'wavelength_nm': wl*1000,
            'radiation_power': P_rad,
            'Purcell_factor': Purcell,
            'enhancement': enhancement
        })
        
        print(f"  辐射功率: {P_rad*1e6:.3f} μW")
        print(f"  Purcell 因子: {Purcell:.2f}")
        print(f"  相对增强: {enhancement:.1f}×")

# 找到最大增强波长
if enhancement_results:
    max_enhancement = max(enhancement_results, key=lambda x: x['enhancement'])
    print(f"\n最大增强在 {max_enhancement['wavelength_nm']:.0f} nm:")
    print(f"  增强因子: {max_enhancement['enhancement']:.1f}×")
    print(f"  Purcell 因子: {max_enhancement['Purcell_factor']:.2f}")
    print(f"  辐射功率: {max_enhancement['radiation_power']*1e6:.3f} μW")
    
    # 检查是否是等离子体共振
    gold_resonance = 520  # 金的等离子体共振波长约 520 nm
    resonance_distance = abs(max_enhancement['wavelength_nm'] - gold_resonance)
    
    print(f"\n等离子体共振分析:")
    print(f"  金纳米球理论共振: ~{gold_resonance} nm")
    print(f"  测量共振: {max_enhancement['wavelength_nm']:.0f} nm")
    print(f"  共振偏移: {resonance_distance:.0f} nm")
    
    if resonance_distance < 50:  # 50 nm 容差
        print(f"  ✓ 检测到等离子体共振")
    else:
        print(f"  ⚠️ 未检测到明显的等离子体共振")
```

### 示例 3：计算 Purcell 因子和量子效率
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("详细分析 Purcell 因子和量子效率...")

class PurcellAnalyzer:
    """Purcell 因子分析工具"""
    
    def __init__(self, session):
        self.session = session
    
    def calculate_detailed_purcell(self, dipole_name, reference_dipole_name=None):
        """计算详细的 Purcell 因子"""
        
        print(f"分析偶极子: {dipole_name}")
        
        # 获取偶极子参数
        dipole_props = self.session.get(dipole_name)
        wavelength = dipole_props.get('wavelength', 1.0)
        
        # 计算功率特性（启用所有选项）
        self.session.dipolepower(dipole_name,
                                wavelength=wavelength,
                                calculate_Purcell=True,
                                calculate_quantum_efficiency=True,
                                calculate_directivity=True,
                                include_absorption=True,
                                include_scattering=True,
                                include_radiation=True)
        
        power_data = self.session.getresult("dipolepower_data")
        
        if not power_data:
            print("无法获取功率数据")
            return None
        
        # 提取关键参数
        results = {
            'dipole_name': dipole_name,
            'wavelength': wavelength,
            'input_power': dipole_props.get('power', 0)
        }
        
        # 功率分量
        power_keys = ['radiation_power', 'absorption_power', 'scattering_power', 'total_power']
        for key in power_keys:
            if key in power_data:
                results[key] = power_data[key]
        
        # Purcell 因子
        if 'Purcell_factor' in power_data:
            results['Purcell_factor'] = power_data['Purcell_factor']
        
        # 量子效率
        if 'quantum_efficiency' in power_data:
            results['quantum_efficiency'] = power_data['quantum_efficiency']
        
        # 方向性
        if 'directivity' in power_data:
            results['directivity'] = power_data['directivity']
        
        # 计算附加指标
        self._calculate_additional_metrics(results, power_data)
        
        return results
    
    def _calculate_additional_metrics(self, results, power_data):
        """计算附加性能指标"""
        
        # 提取功率值
        P_rad = results.get('radiation_power', 0)
        P_abs = results.get('absorption_power', 0)
        P_scat = results.get('scattering_power', 0)
        P_total = results.get('total_power', 0)
        P_input = results.get('input_power', 0)
        
        # 1. 辐射效率
        if P_total > 0:
            radiation_efficiency = P_rad / P_total
            results['radiation_efficiency'] = radiation_efficiency
        
        # 2. 吸收效率
        if P_total > 0:
            absorption_efficiency = P_abs / P_total
            results['absorption_efficiency'] = absorption_efficiency
        
        # 3. 散射效率
        if P_total > 0:
            scattering_efficiency = P_scat / P_total
            results['scattering_efficiency'] = scattering_efficiency
        
        # 4. 总效率（输出/输入）
        if P_input > 0:
            total_efficiency = P_total / P_input
            results['total_efficiency'] = total_efficiency
        
        # 5. Purcell 增强的辐射功率
        if 'Purcell_factor' in results:
            Purcell = results['Purcell_factor']
            
            # 自由空间辐射功率（参考）
            # 对于电偶极子，自由空间辐射功率公式: P0 = (μ0 * p0² * ω⁴) / (12πc)
            # 简化：假设输入功率相同，Purcell 因子直接给出增强
            P_rad_free = P_rad / Purcell if Purcell > 0 else 0
            results['free_space_radiation'] = P_rad_free
            
            # 增强的辐射功率
            enhanced_radiation = P_rad - P_rad_free
            results['enhanced_radiation'] = enhanced_radiation
        
        # 6. 损耗分析
        if P_input > 0:
            power_loss = P_input - P_total
            loss_fraction = power_loss / P_input
            results['power_loss'] = power_loss
            results['loss_fraction'] = loss_fraction
        
        return results
    
    def analyze_purcell_vs_position(self, base_name, positions, wavelength=1.55):
        """分析 Purcell 因子与位置的关系"""
        
        results = []
        
        print(f"分析位置依赖性 (波长: {wavelength} μm)")
        
        for i, (x, y, z) in enumerate(positions):
            # 创建测试偶极子
            dipole_name = f"{base_name}_pos{i}"
            self.session.dipole(dipole_name,
                               x=x, y=y, z=z,
                               wavelength=wavelength,
                               power=1e-6,
                               dipole_type="electric")
            
            # 计算 Purcell 因子
            self.session.dipolepower(dipole_name,
                                    wavelength=wavelength,
                                    calculate_Purcell=True)
            
            power_data = self.session.getresult("dipolepower_data")
            
            if power_data and 'Purcell_factor' in power_data:
                Purcell = power_data['Purcell_factor']
                P_rad = power_data.get('radiation_power', 0)
                
                result = {
                    'position': (x, y, z),
                    'distance': np.sqrt(x**2 + y**2 + z**2),
                    'Purcell_factor': Purcell,
                    'radiation_power': P_rad,
                    'dipole_name': dipole_name
                }
                
                results.append(result)
                
                print(f"  位置 ({x:.2f}, {y:.2f}, {z:.2f}): "
                      f"距离={result['distance']:.2f} μm, "
                      f"Purcell={Purcell:.2f}")
            
            # 清理
            self.session.delete(dipole_name)
        
        # 分析趋势
        if results:
            max_purcell = max(results, key=lambda x: x['Purcell_factor'])
            min_purcell = min(results, key=lambda x: x['Purcell_factor'])
            
            print(f"\nPurcell 因子范围:")
            print(f"  最大值: {max_purcell['Purcell_factor']:.2f} "
                  f"在位置 {max_purcell['position']}")
            print(f"  最小值: {min_purcell['Purcell_factor']:.2f} "
                  f"在位置 {min_purcell['position']}")
            
            # 检查距离相关性
            distances = [r['distance'] for r in results]
            purcells = [r['Purcell_factor'] for r in results]
            
            if len(distances) > 1:
                # 简单相关性分析
                correlation = np.corrcoef(distances, purcells)[0, 1]
                print(f"  与距离的相关系数: {correlation:.3f}")
                
                if correlation < -0.5:
                    print(f"  ✓ Purcell 因子随距离增加而减小")
                elif correlation > 0.5:
                    print(f"  ⚠️ Purcell 因子随距离增加而增加（异常）")
                else:
                    print(f"  ⚠️ Purcell 因子与距离无明显相关性")
        
        return results

# 使用示例
fdtd = lumapi.FDTD()
analyzer = PurcellAnalyzer(fdtd)

# 创建测试结构（光子晶体腔）
print("创建测试结构...")
fdtd.addrect("PC_cavity",
            x=0, y=0, z=0,
            x_span=2, y_span=0.22, z_span=0,
            material="Si")

# 在腔中心创建偶极子
fdtd.dipole("cavity_dipole",
           x=0, y=0, z=0,
           wavelength=1.55,
           power=1e-6,
           dipole_type="electric")

# 详细分析
print("\n进行详细 Purcell 分析...")
results = analyzer.calculate_detailed_purcell("cavity_dipole")

if results:
    print("\n=== 详细分析结果 ===")
    print(f"偶极子: {results['dipole_name']}")
    print(f"波长: {results['wavelength']} μm")
    print(f"输入功率: {results['input_power']*1e6:.3f} μW")
    
    print(f"\n功率分布:")
    print(f"  辐射功率: {results.get('radiation_power', 0)*1e6:.3f} μW")
    print(f"  吸收功率: {results.get('absorption_power', 0)*1e6:.3f} μW")
    print(f"  散射功率: {results.get('scattering_power', 0)*1e6:.3f} μW")
    print(f"  总输出功率: {results.get('total_power', 0)*1e6:.3f} μW")
    
    print(f"\n效率分析:")
    print(f"  辐射效率: {results.get('radiation_efficiency', 0)*100:.2f}%")
    print(f"  吸收效率: {results.get('absorption_efficiency', 0)*100:.2f}%")
    print(f"  散射效率: {results.get('scattering_efficiency', 0)*100:.2f}%")
    print(f"  总效率: {results.get('total_efficiency', 0)*100:.2f}%")
    
    print(f"\nPurcell 分析:")
    if 'Purcell_factor' in results:
        print(f"  Purcell 因子: {results['Purcell_factor']:.2f}")
        print(f"  自由空间辐射: {results.get('free_space_radiation', 0)*1e6:.3f} μW")
        print(f"  增强辐射: {results.get('enhanced_radiation', 0)*1e6:.3f} μW")
    
    if 'quantum_efficiency' in results:
        print(f"  量子效率: {results['quantum_efficiency']*100:.2f}%")
    
    print(f"\n损耗分析:")
    print(f"  功率损耗: {results.get('power_loss', 0)*1e6:.3f} μW")
    print(f"  损耗比例: {results.get('loss_fraction', 0)*100:.2f}%")

# 分析位置依赖性
print("\n分析 Purcell 因子位置依赖性...")
positions = [
    (0, 0, 0),      # 中心
    (0.5, 0, 0),    # 偏移
    (0, 0.5, 0),    # 偏移
    (0.5, 0.5, 0),  # 对角
    (1.0, 0, 0),    # 边缘
]

position_results = analyzer.analyze_purcell_vs_position("test", positions, wavelength=1.55)

# 创建热图数据（用于可视化）
if position_results:
    print("\n生成热图数据...")
    
    # 提取 x, y 位置和 Purcell 因子
    x_positions = [pos[0] for pos in positions[:4]]  # 前4个点
    y_positions = [pos[1] for pos in positions[:4]]
    purcell_values = [r['Purcell_factor'] for r in position_results[:4]]
    
    print(f"X 位置: {x_positions}")
    print(f"Y 位置: {y_positions}")
    print(f"Purcell 值: {[f'{v:.2f}' for v in purcell_values]}")
    
    # 计算平均值和标准差
    avg_purcell = np.mean(purcell_values)
    std_purcell = np.std(purcell_values)
    
    print(f"\n统计信息:")
    print(f"  平均 Purcell 因子: {avg_purcell:.2f}")
    print(f"  标准差: {std_purcell:.2f}")
    print(f"  变异系数: {std_purcell/avg_purcell*100:.1f}%")
    
    # 评估位置敏感性
    if std_purcell / avg_purcell > 0.3:  # 30% 变异
        print(f"  ⚠️ Purcell 因子对位置高度敏感")
    elif std_purcell / avg_purcell > 0.1:  # 10% 变异
        print(f"  ⚠️ Purcell 因子对位置中等敏感")
    else:
        print(f"  ✓ Purcell 因子对位置不敏感")
```

### 示例 4：多偶极子干涉和集体效应
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("研究多偶极子干涉效应...")

def create_dipole_array_interference(name, num_dipoles=4, spacing=0.5, wavelength=1.55):
    """创建干涉偶极子阵列"""
    
    dipoles = []
    total_power = 1e-6  # 总功率 1 μW
    individual_power = total_power / num_dipoles
    
    for i in range(num_dipoles):
        # 线性阵列
        x_pos = (i - (num_dipoles-1)/2) * spacing
        
        # 创建偶极子
        dipole_name = f"{name}_dipole_{i}"
        fdtd.dipole(dipole_name,
                   x=x_pos, y=0, z=0,
                   wavelength=wavelength,
                   power=individual_power,
                   dipole_type="electric",
                   injection_axis="z",
                   phase=i * np.pi/2)  # 相位渐变
        
        dipoles.append(dipole_name)
    
    print(f"创建 {num_dipoles} 个偶极子阵列:")
    print(f"  间距: {spacing} μm")
    print(f"  波长: {wavelength} μm")
    print(f"  总功率: {total_power*1e6:.3f} μW")
    print(f"  单个功率: {individual_power*1e6:.3f} μW")
    
    return dipoles

# 创建干涉阵列
dipole_array = create_dipole_array_interference("interference_array", 
                                               num_dipoles=4, 
                                               spacing=0.5,
                                               wavelength=1.55)

# 计算集体功率特性
print("\n计算集体功率特性...")

def calculate_collective_power(dipole_names, session, wavelength=1.55):
    """计算多个偶极子的集体功率"""
    
    # 方法1：逐个计算并求和
    individual_results = []
    total_radiation = 0
    total_absorption = 0
    total_scattering = 0
    
    for dipole in dipole_names:
        session.dipolepower(dipole,
                           wavelength=wavelength,
                           calculate_Purcell=False)
        
        power_data = session.getresult("dipolepower_data")
        
        if power_data:
            P_rad = power_data.get('radiation_power', 0)
            P_abs = power_data.get('absorption_power', 0)
            P_scat = power_data.get('scattering_power', 0)
            
            individual_results.append({
                'dipole': dipole,
                'radiation': P_rad,
                'absorption': P_abs,
                'scattering': P_scat
            })
            
            total_radiation += P_rad
            total_absorption += P_abs
            total_scattering += P_scat
    
    # 方法2：创建等效偶极子（如果可能）
    # 这里简化，直接使用求和结果
    
    total_power = total_radiation + total_absorption + total_scattering
    input_power = len(dipole_names) * 1e-6 / 4  # 每个偶极子 0.25 μW
    
    # 计算集体增强因子
    # 理想非干涉情况下的总辐射功率
    ideal_collective_radiation = len(dipole_names) * individual_results[0]['radiation'] if individual_results else 0
    
    if ideal_collective_radiation > 0:
        collective_enhancement = total_radiation / ideal_collective_radiation
    else:
        collective_enhancement = 1.0
    
    return {
        'individual_results': individual_results,
        'total_radiation': total_radiation,
        'total_absorption': total_absorption,
        'total_scattering': total_scattering,
        'total_power': total_power,
        'input_power': input_power,
        'collective_enhancement': collective_enhancement,
        'efficiency': total_power / input_power if input_power > 0 else 0,
        'radiation_efficiency': total_radiation / total_power if total_power > 0 else 0
    }

# 计算集体功率
collective_results = calculate_collective_power(dipole_array, fdtd, wavelength=1.55)

print("\n=== 集体功率分析 ===")
print(f"偶极子数量: {len(dipole_array)}")

if collective_results['individual_results']:
    print(f"\n单个偶极子结果 (第一个):")
    first_dipole = collective_results['individual_results'][0]
    print(f"  辐射功率: {first_dipole['radiation']*1e6:.3f} μW")
    print(f"  吸收功率: {first_dipole['absorption']*1e6:.3f} μW")
    print(f"  散射功率: {first_dipole['scattering']*1e6:.3f} μW")

print(f"\n集体总和:")
print(f"  总辐射功率: {collective_results['total_radiation']*1e6:.3f} μW")
print(f"  总吸收功率: {collective_results['total_absorption']*1e6:.3f} μW")
print(f"  总散射功率: {collective_results['total_scattering']*1e6:.3f} μW")
print(f"  总输出功率: {collective_results['total_power']*1e6:.3f} μW")
print(f"  总输入功率: {collective_results['input_power']*1e6:.3f} μW")

print(f"\n效率分析:")
print(f"  总效率: {collective_results['efficiency']*100:.2f}%")
print(f"  辐射效率: {collective_results['radiation_efficiency']*100:.2f}%")

print(f"\n集体增强因子: {collective_results['collective_enhancement']:.3f}")
if collective_results['collective_enhancement'] > 1.0:
    print(f"  ✓ 检测到建设性干涉")
elif collective_results['collective_enhancement'] < 1.0:
    print(f"  ⚠️ 检测到破坏性干涉")
else:
    print(f"  ⚠️ 无显著干涉效应")

# 分析干涉条件
print("\n=== 干涉条件分析 ===")
spacing = 0.5  # μm
wavelength = 1.55  # μm

# 计算相位条件
k = 2 * np.pi / wavelength  # 波数
phase_per_spacing = k * spacing  # 每个间距的相位变化

print(f"阵列参数:")
print(f"  间距: {spacing} μm")
print(f"  波长: {wavelength} μm")
print(f"  波数: {k:.3f} rad/μm")
print(f"  每间距相位变化: {phase_per_spacing:.3f} rad = {np.degrees(phase_per_spacing):.1f}°")

# 计算建设性干涉条件
# 建设性干涉：Δφ = 2πn，其中 n 为整数
n = 1
constructive_spacing = n * wavelength
print(f"\n建设性干涉条件:")
print(f"  理论间距: nλ = {constructive_spacing:.3f} μm (n={n})")
print(f"  实际间距: {spacing:.3f} μm")
print(f"  偏差: {abs(spacing - constructive_spacing)/wavelength*100:.1f}% 波长")

if abs(spacing - constructive_spacing) < wavelength/4:  # 四分之一波长容差
    print(f"  ✓ 接近建设性干涉条件")
else:
    print(f"  ⚠️ 不满足建设性干涉条件")

# 计算远场干涉图案
print("\n计算远场干涉图案...")
def calculate_far_field_pattern(num_sources, spacing, wavelength, phases):
    """计算远场干涉图案（简化模型）"""
    
    theta = np.linspace(-90, 90, 181)  # 角度范围（度）
    theta_rad = np.radians(theta)
    
    # 阵列因子
    k = 2 * np.pi / wavelength
    d = spacing
    
    array_factor = np.zeros_like(theta, dtype=complex)
    
    for i in range(num_sources):
        phase = phases[i] if i < len(phases) else 0
        array_factor += np.exp(1j * (k * d * i * np.sin(theta_rad) + phase))
    
    intensity = np.abs(array_factor)**2
    normalized_intensity = intensity / np.max(intensity)
    
    # 找到主瓣
    main_lobe_idx = np.argmax(normalized_intensity)
    main_lobe_angle = theta[main_lobe_idx]
    
    # 计算波束宽度（3dB）
    half_power = 0.5
    above_half = normalized_intensity >= half_power
    indices = np.where(above_half)[0]
    
    if len(indices) >= 2:
        left_idx = indices[0]
        right_idx = indices[-1]
        beamwidth = theta[right_idx] - theta[left_idx]
    else:
        beamwidth = 0
    
    return {
        'theta': theta,
        'intensity': normalized_intensity,
        'main_lobe_angle': main_lobe_angle,
        'beamwidth': beamwidth,
        'array_factor': array_factor
    }

# 应用计算
phases = [0, np.pi/2, np.pi, 3*np.pi/2]  # 四步相位
pattern = calculate_far_field_pattern(4, 0.5, 1.55, phases)

print(f"远场干涉图案:")
print(f"  主瓣方向: {pattern['main_lobe_angle']:.1f}°")
print(f"  3dB 波束宽度: {pattern['beamwidth']:.1f}°")

# 检查是否实现波束转向
expected_steering = np.degrees(np.arcsin(phases[1] / (k * spacing))) if k*spacing > 0 else 0
print(f"  预期转向角度: {expected_steering:.1f}°")
print(f"  实际转向角度: {pattern['main_lobe_angle']:.1f}°")
print(f"  转向误差: {abs(pattern['main_lobe_angle'] - expected_steering):.1f}°")
```

### 示例 5：高级偶极子功率优化工具
```python
import lumapi
import numpy as np
from scipy import optimize

class DipolePowerOptimizer:
    """偶极子功率优化工具"""
    
    def __init__(self, session):
        self.session = session
        self.optimization_history = []
    
    def objective_function(self, params, dipole_name, target_power, power_type='radiation'):
        """目标函数：最小化与目标功率的差异"""
        
        x, y, z, wavelength, polarization = params
        
        # 更新偶极子参数
        self.session.set(dipole_name, "x", x)
        self.session.set(dipole_name, "y", y)
        self.session.set(dipole_name, "z", z)
        self.session.set(dipole_name, "wavelength", wavelength)
        self.session.set(dipole_name, "polarization_angle", polarization)
        
        # 计算功率
        self.session.dipolepower(dipole_name,
                                wavelength=wavelength,
                                calculate_Purcell=False)
        
        power_data = self.session.getresult("dipolepower_data")
        
        if not power_data:
            return float('inf')
        
        # 获取目标功率类型
        if power_type == 'radiation':
            actual_power = power_data.get('radiation_power', 0)
        elif power_type == 'absorption':
            actual_power = power_data.get('absorption_power', 0)
        elif power_type == 'total':
            actual_power = power_data.get('total_power', 0)
        else:
            actual_power = 0
        
        # 计算差异
        error = abs(actual_power - target_power) / target_power
        
        # 记录历史
        self.optimization_history.append({
            'params': params.copy(),
            'actual_power': actual_power,
            'target_power': target_power,
            'error': error
        })
        
        return error
    
    def optimize_power(self, dipole_name, target_power, power_type='radiation',
                      bounds=None, initial_guess=None, max_iter=20):
        """优化偶极子参数以达到目标功率"""
        
        print(f"优化偶极子 '{dipole_name}' 的 {power_type} 功率...")
        print(f"目标功率: {target_power*1e6:.3f} μW")
        
        # 默认边界
        if bounds is None:
            bounds = [
                (-2, 2),    # x
                (-2, 2),    # y
                (-2, 2),    # z
                (0.4, 1.6), # wavelength
                (0, 180)    # polarization
            ]
        
        # 默认初始猜测
        if initial_guess is None:
            dipole_props = self.session.get(dipole_name)
            initial_guess = [
                dipole_props.get('x', 0),
                dipole_props.get('y', 0),
                dipole_props.get('z', 0),
                dipole_props.get('wavelength', 1.0),
                dipole_props.get('polarization_angle', 0)
            ]
        
        # 优化
        result = optimize.minimize(
            self.objective_function,
            initial_guess,
            args=(dipole_name, target_power, power_type),
            bounds=bounds,
            method='L-BFGS-B',
            options={'maxiter': max_iter, 'disp': True}
        )
        
        if result.success:
            print(f"优化成功!")
            print(f"最终参数: {result.x}")
            print(f"最终误差: {result.fun*100:.2f}%")
            
            # 应用优化参数
            self.session.set(dipole_name, "x", result.x[0])
            self.session.set(dipole_name, "y", result.x[1])
            self.session.set(dipole_name, "z", result.x[2])
            self.session.set(dipole_name, "wavelength", result.x[3])
            self.session.set(dipole_name, "polarization_angle", result.x[4])
            
            # 验证最终功率
            self.session.dipolepower(dipole_name,
                                    wavelength=result.x[3],
                                    calculate_Purcell=False)
            
            power_data = self.session.getresult("dipolepower_data")
            final_power = power_data.get('radiation_power', 0) if power_type == 'radiation' else 0
            
            return {
                'success': True,
                'params': result.x,
                'final_power': final_power,
                'error': result.fun,
                'iterations': len(self.optimization_history)
            }
        else:
            print(f"优化失败: {result.message}")
            return {
                'success': False,
                'message': result.message,
                'iterations': len(self.optimization_history)
            }
    
    def optimize_purcell_factor(self, dipole_name, target_purcell, 
                               bounds=None, initial_guess=None):
        """优化 Purcell 因子"""
        
        print(f"优化 Purcell 因子...")
        print(f"目标 Purcell 因子: {target_purcell}")
        
        def purcell_objective(params):
            """Purcell 因子目标函数"""
            
            x, y, z, wavelength = params
            
            # 更新偶极子参数
            self.session.set(dipole_name, "x", x)
            self.session.set(dipole_name, "y", y)
            self.session.set(dipole_name, "z", z)
            self.session.set(dipole_name, "wavelength", wavelength)
            
            # 计算 Purcell 因子
            self.session.dipolepower(dipole_name,
                                    wavelength=wavelength,
                                    calculate_Purcell=True)
            
            power_data = self.session.getresult("dipolepower_data")
            
            if not power_data or 'Purcell_factor' not in power_data:
                return float('inf')
            
            actual_purcell = power_data['Purcell_factor']
            error = abs(actual_purcell - target_purcell) / target_purcell
            
            self.optimization_history.append({
                'params': params.copy(),
                'actual_purcell': actual_purcell,
                'target_purcell': target_purcell,
                'error': error
            })
            
            return error
        
        # 默认边界
        if bounds is None:
            bounds = [
                (-1, 1),    # x
                (-1, 1),    # y
                (-1, 1),    # z
                (0.5, 1.5)  # wavelength
            ]
        
        # 默认初始猜测
        if initial_guess is None:
            dipole_props = self.session.get(dipole_name)
            initial_guess = [
                dipole_props.get('x', 0),
                dipole_props.get('y', 0),
                dipole_props.get('z', 0),
                dipole_props.get('wavelength', 1.0)
            ]
        
        # 优化
        result = optimize.minimize(
            purcell_objective,
            initial_guess,
            bounds=bounds,
            method='L-BFGS-B',
            options={'maxiter': 15, 'disp': True}
        )
        
        if result.success:
            print(f"Purcell 因子优化成功!")
            return {
                'success': True,
                'params': result.x,
                'error': result.fun
            }
        else:
            print(f"Purcell 因子优化失败: {result.message}")
            return {
                'success': False,
                'message': result.message
            }
    
    def analyze_optimization_history(self):
        """分析优化历史"""
        
        if not self.optimization_history:
            print("没有优化历史")
            return None
        
        print(f"\n优化历史分析:")
        print(f"  总迭代次数: {len(self.optimization_history)}")
        
        # 提取数据
        errors = [entry['error'] for entry in self.optimization_history]
        iterations = list(range(1, len(errors) + 1))
        
        print(f"  初始误差: {errors[0]*100:.2f}%")
        print(f"  最终误差: {errors[-1]*100:.2f}%")
        print(f"  误差减少: {(errors[0] - errors[-1])/errors[0]*100:.1f}%")
        
        # 检查收敛性
        if len(errors) >= 3:
            last_errors = errors[-3:]
            convergence_rate = (last_errors[-2] - last_errors[-1]) / last_errors[-2] if last_errors[-2] > 0 else 0
            
            print(f"  收敛速率: {convergence_rate*100:.2f}%/迭代")
            
            if convergence_rate < 0.01:  # 1% 变化阈值
                print(f"  ✓ 优化已收敛")
            else:
                print(f"  ⚠️ 优化可能未完全收敛")
        
        return {
            'iterations': iterations,
            'errors': errors,
            'initial_error': errors[0],
            'final_error': errors[-1]
        }

# 使用示例
fdtd = lumapi.FDTD()
optimizer = DipolePowerOptimizer(fdtd)

# 创建测试结构
print("创建测试结构...")
fdtd.addrect("optimization_structure",
            x=0, y=0, z=0,
            x_span=2, y_span=2, z_span=0,
            material="Si")

# 创建待优化的偶极子
fdtd.dipole("optimizable_dipole",
           x=0, y=0, z=0,
           wavelength=1.0,
           power=1e-6,
           dipole_type="electric")

print("\n初始偶极子设置:")
initial_props = fdtd.get("optimizable_dipole")
print(f"  位置: ({initial_props.get('x', 0)}, {initial_props.get('y', 0)}, {initial_props.get('z', 0)})")
print(f"  波长: {initial_props.get('wavelength', 0)} μm")
print(f"  偏振角: {initial_props.get('polarization_angle', 0)}°")

# 优化辐射功率
target_radiation = 5e-7  # 目标辐射功率 0.5 μW
print(f"\n优化辐射功率到 {target_radiation*1e6:.3f} μW...")

result = optimizer.optimize_power("optimizable_dipole",
                                 target_radiation,
                                 power_type='radiation',
                                 max_iter=10)

if result.get('success', False):
    print(f"\n优化结果:")
    print(f"  最终位置: ({result['params'][0]:.3f}, {result['params'][1]:.3f}, {result['params'][2]:.3f})")
    print(f"  最终波长: {result['params'][3]:.3f} μm")
    print(f"  最终偏振: {result['params'][4]:.1f}°")
    print(f"  最终功率: {result['final_power']*1e6:.3f} μW")
    print(f"  相对误差: {result['error']*100:.2f}%")
    print(f"  迭代次数: {result['iterations']}")

# 分析优化历史
history = optimizer.analyze_optimization_history()

# 优化 Purcell 因子
print("\n优化 Purcell 因子...")
target_purcell = 2.5  # 目标 Purcell 因子

purcell_result = optimizer.optimize_purcell_factor("optimizable_dipole",
                                                  target_purcell)

if purcell_result.get('success', False):
    print(f"\nPurcell 优化结果:")
    print(f"  最终参数: {purcell_result['params']}")
    print(f"  最终误差: {purcell_result['error']*100:.2f}%")
    
    # 验证最终 Purcell 因子
    fdtd.dipolepower("optimizable_dipole",
                    wavelength=purcell_result['params'][3],
                    calculate_Purcell=True)
    
    power_data = fdtd.getresult("dipolepower_data")
    if power_data and 'Purcell_factor' in power_data:
        final_purcell = power_data['Purcell_factor']
        print(f"  最终 Purcell 因子: {final_purcell:.2f}")

print("\n优化完成!")
```

## 注意事项

1. **仿真收敛**：确保仿真完全收敛后再进行功率计算，否则结果可能不准确。

2. **监视器设置**：功率计算依赖监视器的正确设置。确保监视器覆盖所有相关区域且方向正确。

3. **材料模型**：准确的功率计算需要正确的材料模型，特别是对于金属和有损耗材料。

4. **网格分辨率**：足够的网格分辨率对于准确计算近场功率和 Purcell 因子至关重要。

5. **边界条件**：边界条件会影响功率计算。使用 PML 边界以最小化反射。

6. **归一化**：注意功率归一化设置。不同归一化方式会影响结果解释。

7. **干涉效应**：多个偶极子之间的干涉会影响集体功率。仔细分析相位关系。

8. **热效应**：高功率偶极子可能引起热效应，这通常不在标准 FDTD 仿真中考虑。

9. **量子效应**：对于量子发射器，需要考虑 Purcell 因子对辐射寿命的影响。

10. **数值误差**：功率计算可能存在数值误差。通过功率守恒检查验证结果可靠性。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 主要应用领域 |
| MODE Solutions | ⚠️ 有限支持 | 2D 功率计算 |
| DEVICE | ❌ 不支持 | 不适用于器件仿真 |
| INTERCONNECT | ❌ 不支持 | 不适用于电路仿真 |

## 相关命令

- `dipole` - 创建偶极子源
- `getpower` - 获取功率数据
- `getelectric` - 获取电场数据
- `getmagnetic` - 获取磁场数据
- `overlap` - 计算重叠积分
- `findmodes` - 寻找模式（用于 Purcell 因子计算）
- `run` - 运行仿真
- `set` - 设置偶极子属性
- `get` - 获取偶极子属性