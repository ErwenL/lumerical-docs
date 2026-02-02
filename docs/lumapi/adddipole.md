# adddipole

## 概述

`adddipole` 命令用于在 FDTD 仿真中添加一个偶极子光源。偶极子光源模拟一个理想电偶极子，产生球面波辐射，常用于分析近场辐射特性、光子晶体缺陷模式、量子点发光、以及天线辐射模式等应用。该光源是点源，具有明确的偏振方向和空间位置。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
adddipole;
```

### Python API (Lumapi)
```python
session.adddipole()
```

## 参数

`adddipole` 命令没有直接参数，但需要通过后续的 `set` 命令配置光源属性。

## 配置属性

添加偶极子光源后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "dipole" | 光源名称 |
| `x`, `y`, `z` | float | 0 | 偶极子位置坐标 (m) |
| `position` | array[3] | [0, 0, 0] | 位置数组 [x, y, z] (m) |

### 2. 偶极子方向与偏振
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `dipole type` | string | "electric" | 偶极子类型："electric", "magnetic" |
| `dipole orientation` | string | "x" | 偶极子方向："x", "y", "z", "custom" |
| `theta` | float | 0 | 球坐标极角 (度)，0 表示沿 z 轴 |
| `phi` | float | 0 | 球坐标方位角 (度)，0 表示沿 x 轴 |
| `polarization angle` | float | 0 | 偏振角 (度) |
| `polarization ellipticity` | float | 0 | 偏振椭圆度 (0=线偏振，1=圆偏振) |

### 3. 波长与频率设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength start` | float | 1.5e-6 | 起始波长 (m) |
| `wavelength stop` | float | 1.6e-6 | 结束波长 (m) |
| `frequency points` | int | 1 | 频率点数 |
| `center wavelength` | float | 1.55e-6 | 中心波长 (m) |
| `wavelength span` | float | 0.1e-6 | 波长跨度 (m) |
| `set wavelength` | int | 0 | 是否设置波长 (0/1) |
| `frequency` | float | 1.94e14 | 频率 (Hz)，对应 1.55μm |

### 4. 幅度与相位
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `amplitude` | float | 1.0 | 振幅 (V/m 或 A/m) |
| `phase` | float | 0 | 相位 (弧度) |
| `power` | float | 1.0 | 功率 (W) |
| `normalize by total power` | int | 0 | 是否按总功率归一化 (0/1) |

### 5. 时间波形设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `pulse type` | string | "continuous" | 脉冲类型："continuous", "gaussian", "custom" |
| `pulse width` | float | 10e-15 | 脉冲宽度 (秒) |
| `pulse offset` | float | 0 | 脉冲时间偏移 (秒) |
| `frequency chirp` | float | 0 | 频率啁啾 (Hz/s) |
| `modulation frequency` | float | 0 | 调制频率 (Hz) |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override global source settings` | int | 0 | 是否覆盖全局光源设置 (0/1) |
| `source type` | string | "point" | 光源类型："point", "gaussian" |
| `beam width` | float | 1e-6 | 光束宽度 (m)，当 source type="gaussian" 时使用 |
| `numerical aperture` | float | 0.1 | 数值孔径，用于高斯光束 |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [1.0, 0.0, 0.0, 1.0] | RGBA 颜色值（红色） |
| `alpha` | float | 0.5 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |
| `size` | float | 0.2e-6 | 显示尺寸 (m) |

## 返回值

`adddipole` 命令没有返回值。成功执行后，会在仿真中添加一个偶极子光源对象。

## 示例

### 示例 1: 基本电偶极子创建

#### LSF 脚本
```lumerical
// 添加电偶极子光源
adddipole;

// 设置几何参数
set("name", "electric_dipole");
set("x", 0);
set("y", 0);
set("z", 0);

// 设置偶极子方向（沿 x 轴）
set("dipole type", "electric");
set("dipole orientation", "x");

// 设置波长（单波长 1550nm）
set("wavelength start", 1.55e-6);
set("wavelength stop", 1.55e-6);
set("frequency points", 1);

// 设置幅度和相位
set("amplitude", 1.0);
set("phase", 0);

// 设置显示属性
set("color", [1.0, 0.0, 0.0, 0.8]);  // 红色
set("size", 0.3e-6);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加偶极子光源
fdtd.adddipole()

# 设置几何参数
fdtd.set("name", "electric_dipole")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)

# 设置偶极子方向（沿 x 轴）
fdtd.set("dipole type", "electric")
fdtd.set("dipole orientation", "x")

# 设置波长（单波长 1550nm）
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.55e-6)
fdtd.set("frequency points", 1)

# 设置幅度和相位
fdtd.set("amplitude", 1.0)
fdtd.set("phase", 0)

# 设置显示属性
fdtd.set("color", [1.0, 0.0, 0.0, 0.8])  # 红色
fdtd.set("size", 0.3e-6)
```

### 示例 2: 球坐标方向偶极子

#### LSF 脚本
```lumerical
// 添加球坐标方向的偶极子
adddipole;
set("name", "spherical_dipole");
set("position", [1e-6, 2e-6, 0]);  // 位置 (1μm, 2μm, 0)

// 使用球坐标设置方向
set("dipole type", "electric");
set("theta", 45);      // 与 z 轴夹角 45 度
set("phi", 30);        // 在 xy 平面投影与 x 轴夹角 30 度

// 设置波长范围（宽带扫描）
set("wavelength start", 1.4e-6);   // 1400nm
set("wavelength stop", 1.7e-6);    // 1700nm
set("frequency points", 31);       // 31 个波长点

// 设置圆偏振
set("polarization ellipticity", 1.0);  // 圆偏振

// 设置显示
set("color", [0.0, 1.0, 0.0, 0.7]);  // 绿色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.adddipole()
fdtd.set("name", "spherical_dipole")
fdtd.set("position", [1e-6, 2e-6, 0])  # 位置 (1μm, 2μm, 0)

# 使用球坐标设置方向
fdtd.set("dipole type", "electric")
fdtd.set("theta", 45)      # 与 z 轴夹角 45 度
fdtd.set("phi", 30)        # 在 xy 平面投影与 x 轴夹角 30 度

# 设置波长范围（宽带扫描）
fdtd.set("wavelength start", 1.4e-6)   # 1400nm
fdtd.set("wavelength stop", 1.7e-6)    # 1700nm
fdtd.set("frequency points", 31)       # 31 个波长点

# 设置圆偏振
fdtd.set("polarization ellipticity", 1.0)  # 圆偏振

# 设置显示
fdtd.set("color", [0.0, 1.0, 0.0, 0.7])  # 绿色
```

### 示例 3: 高斯脉冲偶极子

#### LSF 脚本
```lumerical
// 添加高斯脉冲偶极子
adddipole;
set("name", "gaussian_pulse_dipole");
set("x", 0);
set("y", 0);
set("z", 0);

// 设置脉冲参数
set("pulse type", "gaussian");
set("pulse width", 20e-15);     // 20fs 脉冲宽度
set("pulse offset", 50e-15);    // 50fs 时间偏移

// 设置中心波长
set("center wavelength", 1.55e-6);
set("wavelength span", 0.2e-6);  // 200nm 带宽

// 设置偶极子方向
set("dipole type", "electric");
set("dipole orientation", "z");

// 设置调制频率（用于振幅调制）
set("modulation frequency", 10e9);  // 10GHz

// 设置显示
set("color", [0.0, 0.0, 1.0, 0.6]);  // 蓝色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.adddipole()
fdtd.set("name", "gaussian_pulse_dipole")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)

# 设置脉冲参数
fdtd.set("pulse type", "gaussian")
fdtd.set("pulse width", 20e-15)     # 20fs 脉冲宽度
fdtd.set("pulse offset", 50e-15)    # 50fs 时间偏移

# 设置中心波长
fdtd.set("center wavelength", 1.55e-6)
fdtd.set("wavelength span", 0.2e-6)  # 200nm 带宽

# 设置偶极子方向
fdtd.set("dipole type", "electric")
fdtd.set("dipole orientation", "z")

# 设置调制频率（用于振幅调制）
fdtd.set("modulation frequency", 10e9)  # 10GHz

# 设置显示
fdtd.set("color", [0.0, 0.0, 1.0, 0.6])  # 蓝色
```

### 示例 4: 磁偶极子（环形电流）

#### LSF 脚本
```lumerical
// 添加磁偶极子（模拟环形电流）
adddipole;
set("name", "magnetic_dipole");
set("position", [0, 0, 100e-9]);  // 略高于平面

// 设置磁偶极子
set("dipole type", "magnetic");
set("dipole orientation", "z");   // 磁偶极矩沿 z 轴

// 设置波长
set("wavelength start", 600e-9);  // 可见光范围 600nm
set("wavelength stop", 600e-9);

// 设置功率归一化
set("normalize by total power", 1);
set("power", 0.001);  // 1mW 总功率

// 设置显示
set("color", [1.0, 0.5, 0.0, 0.8]);  // 橙色
set("size", 0.5e-6);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.adddipole()
fdtd.set("name", "magnetic_dipole")
fdtd.set("position", [0, 0, 100e-9])  # 略高于平面

# 设置磁偶极子
fdtd.set("dipole type", "magnetic")
fdtd.set("dipole orientation", "z")   # 磁偶极矩沿 z 轴

# 设置波长
fdtd.set("wavelength start", 600e-9)  # 可见光范围 600nm
fdtd.set("wavelength stop", 600e-9)

# 设置功率归一化
fdtd.set("normalize by total power", 1)
fdtd.set("power", 0.001)  # 1mW 总功率

# 设置显示
fdtd.set("color", [1.0, 0.5, 0.0, 0.8])  # 橙色
fdtd.set("size", 0.5e-6)
```

### 示例 5: 偶极子阵列（用于波前调控）

#### LSF 脚本
```lumerical
// 创建偶极子阵列（用于超表面设计）
for(i = 0; i < 5; i++) {
    for(j = 0; j < 5; j++) {
        adddipole;
        set("name", "dipole_array_" + num2str(i) + "_" + num2str(j));
        set("x", i * 200e-9);  // 200nm 间距
        set("y", j * 200e-9);
        set("z", 0);
        
        // 设置方向（渐变相位）
        phase_shift = (i + j) * 45;  // 45度步进相位
        set("phase", phase_shift * pi/180);
        
        // 设置幅度（切趾函数）
        amplitude = exp(-((i-2)^2 + (j-2)^2)/4.0);
        set("amplitude", amplitude);
        
        // 设置波长
        set("wavelength start", 1.55e-6);
        set("wavelength stop", 1.55e-6);
        
        // 设置方向（所有沿 z 轴）
        set("dipole orientation", "z");
        
        // 设置颜色根据相位
        hue = phase_shift / 360;
        set("color", [hue, 0.8, 0.5, 0.6]);
    }
}
```

#### Python API
```python
import numpy as np
import lumapi

fdtd = lumapi.FDTD()

# 创建偶极子阵列（用于超表面设计）
for i in range(5):
    for j in range(5):
        fdtd.adddipole()
        fdtd.set("name", f"dipole_array_{i}_{j}")
        fdtd.set("x", i * 200e-9)  # 200nm 间距
        fdtd.set("y", j * 200e-9)
        fdtd.set("z", 0)
        
        # 设置方向（渐变相位）
        phase_shift = (i + j) * 45  # 45度步进相位
        fdtd.set("phase", phase_shift * np.pi/180)
        
        # 设置幅度（切趾函数）
        amplitude = np.exp(-((i-2)**2 + (j-2)**2)/4.0)
        fdtd.set("amplitude", amplitude)
        
        # 设置波长
        fdtd.set("wavelength start", 1.55e-6)
        fdtd.set("wavelength stop", 1.55e-6)
        
        # 设置方向（所有沿 z 轴）
        fdtd.set("dipole orientation", "z")
        
        # 设置颜色根据相位
        hue = phase_shift / 360
        fdtd.set("color", [hue, 0.8, 0.5, 0.6])
```

## 注意事项

### 1. 偶极子类型选择
- **电偶极子 (electric)**: 模拟振荡电荷对，辐射电场为主
- **磁偶极子 (magnetic)**: 模拟环形电流，辐射磁场为主
- 电偶极子更常用，磁偶极子用于特殊应用（如磁共振、手性材料）

### 2. 方向设置方式
- 使用 `dipole orientation` 设置沿坐标轴方向（x/y/z）
- 使用 `theta` 和 `phi` 设置任意球坐标方向
- 使用 `polarization angle` 和 `polarization ellipticity` 控制偏振态

### 3. 近场与远场
- 偶极子近场具有强烈的空间变化
- 远场辐射模式为球面波，具有特定的角分布
- 使用 `farfield` 命令计算远场辐射

### 4. 数值考虑
- 偶极子是点源，网格尺寸应远小于波长
- 近场区域需要精细网格以获得准确结果
- 避免将偶极子放置在金属表面或高折射率对比度界面附近

### 5. 功率归一化
- 默认振幅为 1.0，但实际辐射功率取决于仿真设置
- 使用 `normalize by total power` 确保功率一致性
- 多波长扫描时注意功率谱密度

## 错误处理

### 常见错误
1. **位置无效**: 坐标超出仿真区域
   - 解决方案：确保坐标在仿真边界内

2. **波长设置冲突**: `wavelength start` > `wavelength stop`
   - 解决方案：确保 `wavelength start` ≤ `wavelength stop`

3. **方向无效**: `dipole orientation` 不是有效方向
   - 解决方案：检查方向值，必须是 "x", "y", "z", "custom" 之一

4. **网格太粗**: 点源特征尺寸小于网格尺寸
   - 解决方案：在偶极子位置附近细化网格

5. **功率溢出**: 振幅过大导致数值不稳定
   - 解决方案：减小振幅或启用功率归一化

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加偶极子光源
    fdtd.adddipole()
    
    # 配置光源属性
    fdtd.set("name", "test_dipole")
    fdtd.set("x", 0)
    fdtd.set("y", 0)
    fdtd.set("z", 0)
    
    # 检查波长设置
    wavelength_start = fdtd.get("wavelength start")
    wavelength_stop = fdtd.get("wavelength stop")
    
    if wavelength_start <= 0 or wavelength_stop <= 0:
        raise ValueError("波长必须 > 0")
    if wavelength_start > wavelength_stop:
        raise ValueError("起始波长必须 ≤ 结束波长")
    
    # 检查方向设置
    orientation = fdtd.get("dipole orientation")
    valid_orientations = ["x", "y", "z", "custom"]
    if orientation not in valid_orientations:
        raise ValueError(f"方向必须是 {valid_orientations} 之一")
    
    # 设置偶极子类型
    fdtd.set("dipole type", "electric")
    
    # 设置波长
    fdtd.set("wavelength start", 1.55e-6)
    fdtd.set("wavelength stop", 1.55e-6)
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值
    fdtd.set("wavelength start", 1.5e-6)
    fdtd.set("wavelength stop", 1.6e-6)
    fdtd.set("dipole orientation", "x")
    
except lumapi.LumApiError as e:
    print(f"偶极子创建失败: {e}")
    
    # 检查具体错误
    if "position" in str(e).lower():
        print("错误: 位置无效，请检查坐标值")
    elif "wavelength" in str(e).lower():
        print("错误: 波长设置无效")
    elif "orientation" in str(e).lower():
        print("错误: 方向设置无效")
    elif "mesh" in str(e).lower():
        print("错误: 网格分辨率不足，请在偶极子位置附近细化网格")
    elif "amplitude" in str(e).lower() or "power" in str(e).lower():
        print("错误: 振幅/功率过大，请减小值或启用功率归一化")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addmode`: 添加模式光源（用于波导注入）
- `addtds`: 添加时域光源（用于自定义波形）
- `addmodesource`: 添加模式源（varFDTD）
- `farfield`: 计算远场辐射
- `nearfield2farfield`: 近场到远场转换
- `setglobalsource`: 设置全局光源参数

## 产品支持

- **完全支持**: FDTD Solutions
- **有限支持**: MODE Solutions（部分功能）
- **不支持**: varFDTD, DEVICE, INTERCONNECT

## 应用场景

### 1. 光子晶体缺陷模式分析
```python
# 在光子晶体缺陷中放置偶极子分析局域模式
fdtd.adddipole()
fdtd.set("name", "PhC_defect_dipole")
fdtd.set("position", [0, 0, 0])  # 缺陷中心
fdtd.set("dipole type", "electric")
fdtd.set("dipole orientation", "z")
fdtd.set("wavelength start", 1.55e-6)
fdtd.set("wavelength stop", 1.6e-6)
fdtd.set("frequency points", 51)  # 宽带扫描
```

### 2. 天线辐射特性分析
```python
# 分析微带天线辐射模式
fdtd.adddipole()
fdtd.set("name", "antenna_feed")
fdtd.set("position", [0, 0, 1.5e-3])  # 天线馈电点
fdtd.set("dipole type", "electric")
fdtd.set("dipole orientation", "z")  # 垂直极化
fdtd.set("center wavelength", 30e-3)  # 10GHz
fdtd.set("wavelength span", 6e-3)     # 2GHz 带宽
```

### 3. 量子点发光模拟
```python
# 模拟量子点发光
fdtd.adddipole()
fdtd.set("name", "quantum_dot")
fdtd.set("position", [50e-9, 50e-9, 50e-9])  # 纳米尺度位置
fdtd.set("dipole type", "electric")
# 随机方向模拟各向同性辐射
import random
fdtd.set("theta", random.uniform(0, 180))
fdtd.set("phi", random.uniform(0, 360))
fdtd.set("wavelength start", 600e-9)  # 可见光
fdtd.set("wavelength stop", 650e-9)
```

### 4. 超表面相位调控
```python
# 创建相位梯度超表面
period = 300e-9  # 300nm 周期
for i in range(10):
    for j in range(10):
        fdtd.adddipole()
        fdtd.set("name", f"meta_atom_{i}_{j}")
        fdtd.set("x", i * period)
        fdtd.set("y", j * period)
        fdtd.set("z", 0)
        # 线性相位梯度
        phase = 2 * np.pi * (i + j) / 10
        fdtd.set("phase", phase)
        fdtd.set("dipole orientation", "z")
        fdtd.set("wavelength start", 1.55e-6)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `pulse type` 和脉冲参数 |
| Lumerical 2019a | 新增 `polarization ellipticity` 和球坐标支持 |
| Lumerical 2018a | 新增 `dipole type` 支持磁偶极子 |
| Lumerical 2017a | 首次引入 `adddipole` 命令 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical FDTD Solutions 用户指南 - 光源章节
2. 电动力学与辐射理论
3. 光子晶体与超材料设计
4. 天线理论与设计

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*