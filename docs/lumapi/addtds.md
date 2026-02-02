# addtds

## 概述

`addtds` 命令用于在 FDTD 仿真中添加一个时域光源。时域光源允许用户定义任意时间波形，支持自定义脉冲形状、调制信号和复杂激励波形。该光源特别适用于超快光学、脉冲传播、非线性效应和自定义调制信号等时域分析场景。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addtds;
```

### Python API (Lumapi)
```python
session.addtds()
```

## 参数

`addtds` 命令没有直接参数，但需要通过后续的 `set` 命令配置光源属性。

## 配置属性

添加时域光源后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "tds" | 光源名称 |
| `x`, `y`, `z` | float | 0 | 光源中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 光源各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 光源 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 光源 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 光源 Z 方向最小/最大坐标 (m) |

### 2. 光源方向与类型
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `injection axis` | string | "x" | 注入方向："x", "y", "z" |
| `source type` | string | "plane wave" | 光源类型："plane wave", "gaussian", "mode" |
| `direction` | string | "forward" | 传播方向："forward", "backward" |
| `angle theta` | float | 0 | 入射极角 (度) |
| `angle phi` | float | 0 | 入射方位角 (度) |

### 3. 时域波形设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `time start` | float | 0 | 时间起点 (秒) |
| `time stop` | float | 100e-15 | 时间终点 (秒) |
| `time points` | int | 1000 | 时间点数 |
| `waveform type` | string | "gaussian" | 波形类型："gaussian", "sine", "custom", "user defined" |
| `pulse width` | float | 10e-15 | 脉冲宽度 (FWHM，秒) |
| `center time` | float | 50e-15 | 中心时间 (秒) |
| `amplitude` | float | 1.0 | 振幅 |
| `frequency` | float | 1.94e14 | 载波频率 (Hz)，对应 1.55μm |
| `phase` | float | 0 | 相位 (弧度) |

### 4. 调制与啁啾
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `modulation type` | string | "none" | 调制类型："none", "amplitude", "frequency", "phase" |
| `modulation frequency` | float | 1e9 | 调制频率 (Hz) |
| `modulation depth` | float | 0.1 | 调制深度 (0-1) |
| `chirp type` | string | "none" | 啁啾类型："none", "linear", "quadratic" |
| `chirp rate` | float | 0 | 啁啾率 (Hz/s) |
| `bandwidth` | float | 0.1e14 | 带宽 (Hz) |

### 5. 偏振设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `polarization angle` | float | 0 | 偏振角 (度) |
| `polarization ellipticity` | float | 0 | 偏振椭圆度 (0=线偏振，1=圆偏振) |
| `TE fraction` | float | 1.0 | TE 分量比例 |
| `TM fraction` | float | 0 | TM 分量比例 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override global source settings` | int | 0 | 是否覆盖全局光源设置 (0/1) |
| `use full time span` | int | 1 | 是否使用完整时间跨度 (0/1) |
| `window type` | string | "none" | 时间窗类型："none", "hamming", "hanning", "blackman" |
| `custom waveform` | array | [] | 自定义波形数据 [时间, 振幅] |

### 7. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.0, 1.0, 0.0, 1.0] | RGBA 颜色值（绿色） |
| `alpha` | float | 0.5 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addtds` 命令没有返回值。成功执行后，会在仿真中添加一个时域光源对象。

## 示例

### 示例 1: 基本高斯脉冲创建

#### LSF 脚本
```lumerical
// 添加时域光源（高斯脉冲）
addtds;

// 设置几何参数
set("name", "gaussian_pulse");
set("x", -5e-6);      // 左侧注入
set("y", 0);
set("z", 0);
set("y span", 2e-6);  // 覆盖波导宽度
set("z span", 1e-6);  // 覆盖波导高度

// 设置光源方向
set("injection axis", "x");
set("direction", "forward");
set("source type", "plane wave");

// 设置时域参数
set("waveform type", "gaussian");
set("pulse width", 20e-15);    // 20fs 脉冲宽度
set("center time", 50e-15);    // 50fs 中心时间
set("time start", 0);
set("time stop", 200e-15);     // 200fs 时间窗口
set("time points", 1000);

// 设置载波频率（1550nm）
set("frequency", 1.94e14);     // 193.5THz

// 设置偏振
set("polarization angle", 0);
set("TE fraction", 1.0);

// 设置显示
set("color", [0.0, 1.0, 0.0, 0.7]);  // 绿色半透明
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加时域光源
fdtd.addtds()

# 设置几何参数
fdtd.set("name", "gaussian_pulse")
fdtd.set("x", -5e-6)      # 左侧注入
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)  # 覆盖波导宽度
fdtd.set("z span", 1e-6)  # 覆盖波导高度

# 设置光源方向
fdtd.set("injection axis", "x")
fdtd.set("direction", "forward")
fdtd.set("source type", "plane wave")

# 设置时域参数
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 20e-15)    # 20fs 脉冲宽度
fdtd.set("center time", 50e-15)    # 50fs 中心时间
fdtd.set("time start", 0)
fdtd.set("time stop", 200e-15)     # 200fs 时间窗口
fdtd.set("time points", 1000)

# 设置载波频率（1550nm）
fdtd.set("frequency", 1.94e14)     # 193.5THz

# 设置偏振
fdtd.set("polarization angle", 0)
fdtd.set("TE fraction", 1.0)

# 设置显示
fdtd.set("color", [0.0, 1.0, 0.0, 0.7])  # 绿色半透明
```

### 示例 2: 正弦调制脉冲

#### LSF 脚本
```lumerical
// 添加正弦调制时域光源
addtds;
set("name", "modulated_pulse");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 3e-6);
set("z span", 1.5e-6);

// 设置调制参数
set("waveform type", "gaussian");
set("pulse width", 50e-15);       // 50fs 脉冲宽度
set("modulation type", "amplitude");  // 振幅调制
set("modulation frequency", 10e9);    // 10GHz 调制频率
set("modulation depth", 0.5);         // 50% 调制深度

// 设置时间窗口
set("time start", 0);
set("time stop", 500e-15);        // 500fs 时间窗口
set("time points", 2000);         // 高时间分辨率

// 设置载波频率
set("frequency", 1.94e14);        // 1550nm

// 设置光源类型
set("source type", "gaussian");
set("beam width", 2e-6);          // 2μm 光束宽度

// 设置显示
set("color", [1.0, 0.5, 0.0, 0.6]);  // 橙色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addtds()
fdtd.set("name", "modulated_pulse")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 1.5e-6)

# 设置调制参数
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 50e-15)       # 50fs 脉冲宽度
fdtd.set("modulation type", "amplitude")  # 振幅调制
fdtd.set("modulation frequency", 10e9)    # 10GHz 调制频率
fdtd.set("modulation depth", 0.5)         # 50% 调制深度

# 设置时间窗口
fdtd.set("time start", 0)
fdtd.set("time stop", 500e-15)        # 500fs 时间窗口
fdtd.set("time points", 2000)         # 高时间分辨率

# 设置载波频率
fdtd.set("frequency", 1.94e14)        # 1550nm

# 设置光源类型
fdtd.set("source type", "gaussian")
fdtd.set("beam width", 2e-6)          # 2μm 光束宽度

# 设置显示
fdtd.set("color", [1.0, 0.5, 0.0, 0.6])  # 橙色
```

### 示例 3: 自定义波形（用户定义）

#### LSF 脚本
```lumerical
// 添加自定义波形时域光源
addtds;
set("name", "custom_waveform");

// 设置几何
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置自定义波形
set("waveform type", "user defined");

// 创建自定义波形数据（时间, 振幅）
t = linspace(0, 200e-15, 1000);
// 双高斯脉冲
amplitude = exp(-(t-50e-15)^2/(10e-15)^2) + 0.5*exp(-(t-100e-15)^2/(15e-15)^2);
set("custom waveform", [t; amplitude]);

// 设置时间参数（必须与自定义波形匹配）
set("time start", 0);
set("time stop", 200e-15);
set("time points", 1000);

// 设置载波频率
set("frequency", 1.94e14);  // 1550nm

// 设置光源方向
set("injection axis", "x");
set("direction", "forward");

// 设置显示
set("color", [0.5, 0.0, 0.5, 0.7]);  // 紫色
```

#### Python API
```python
import numpy as np
import lumapi

fdtd = lumapi.FDTD()
fdtd.addtds()
fdtd.set("name", "custom_waveform")

# 设置几何
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置自定义波形
fdtd.set("waveform type", "user defined")

# 创建自定义波形数据（时间, 振幅）
t = np.linspace(0, 200e-15, 1000)
# 双高斯脉冲
amplitude = np.exp(-(t-50e-15)**2/(10e-15)**2) + 0.5*np.exp(-(t-100e-15)**2/(15e-15)**2)
custom_waveform = np.vstack([t, amplitude])
fdtd.set("custom waveform", custom_waveform)

# 设置时间参数（必须与自定义波形匹配）
fdtd.set("time start", 0)
fdtd.set("time stop", 200e-15)
fdtd.set("time points", 1000)

# 设置载波频率
fdtd.set("frequency", 1.94e14)  # 1550nm

# 设置光源方向
fdtd.set("injection axis", "x")
fdtd.set("direction", "forward")

# 设置显示
fdtd.set("color", [0.5, 0.0, 0.5, 0.7])  # 紫色
```

### 示例 4: 线性啁啾脉冲

#### LSF 脚本
```lumerical
// 添加线性啁啾脉冲
addtds;
set("name", "chirped_pulse");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置啁啾参数
set("waveform type", "gaussian");
set("pulse width", 100e-15);      // 100fs 脉冲宽度
set("chirp type", "linear");      // 线性啁啾
set("chirp rate", 1e24);          // 啁啾率 1e24 Hz/s
set("bandwidth", 2e13);           // 20GHz 带宽

// 设置中心频率
set("frequency", 1.94e14);        // 1550nm 中心波长

// 设置时间窗口
set("time start", 0);
set("time stop", 300e-15);        // 300fs 时间窗口
set("time points", 1500);

// 设置光源类型
set("source type", "plane wave");
set("injection axis", "x");

// 设置圆偏振
set("polarization ellipticity", 1.0);  // 圆偏振

// 设置显示
set("color", [0.0, 1.0, 1.0, 0.6]);  // 青色
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addtds()
fdtd.set("name", "chirped_pulse")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置啁啾参数
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 100e-15)      # 100fs 脉冲宽度
fdtd.set("chirp type", "linear")      # 线性啁啾
fdtd.set("chirp rate", 1e24)          # 啁啾率 1e24 Hz/s
fdtd.set("bandwidth", 2e13)           # 20GHz 带宽

# 设置中心频率
fdtd.set("frequency", 1.94e14)        # 1550nm 中心波长

# 设置时间窗口
fdtd.set("time start", 0)
fdtd.set("time stop", 300e-15)        # 300fs 时间窗口
fdtd.set("time points", 1500)

# 设置光源类型
fdtd.set("source type", "plane wave")
fdtd.set("injection axis", "x")

# 设置圆偏振
fdtd.set("polarization ellipticity", 1.0)  # 圆偏振

# 设置显示
fdtd.set("color", [0.0, 1.0, 1.0, 0.6])  # 青色
```

### 示例 5: 倾斜入射平面波

#### LSF 脚本
```lumerical
// 添加倾斜入射时域光源
addtds;
set("name", "tilted_plane_wave");
set("x", -5e-6);
set("y", 0);
set("z", 0);
set("y span", 5e-6);      // 较大区域以覆盖倾斜波前
set("z span", 3e-6);

// 设置倾斜角度
set("angle theta", 30);   // 30度极角（与z轴夹角）
set("angle phi", 45);     // 45度方位角（在xy平面投影）

// 设置时域参数
set("waveform type", "sine");        // 连续正弦波
set("frequency", 1.94e14);           // 1550nm
set("time start", 0);
set("time stop", 100e-15);           // 100fs 时间窗口
set("time points", 500);

// 设置光源类型
set("source type", "plane wave");
set("injection axis", "x");           // 仍沿x轴注入，但通过角度倾斜

// 设置振幅调制
set("modulation type", "amplitude");
set("modulation frequency", 1e9);     // 1GHz 振幅调制
set("modulation depth", 0.3);

// 设置显示
set("color", [1.0, 0.0, 0.0, 0.5]);  // 红色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addtds()
fdtd.set("name", "tilted_plane_wave")
fdtd.set("x", -5e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 5e-6)      # 较大区域以覆盖倾斜波前
fdtd.set("z span", 3e-6)

# 设置倾斜角度
fdtd.set("angle theta", 30)   # 30度极角（与z轴夹角）
fdtd.set("angle phi", 45)     # 45度方位角（在xy平面投影）

# 设置时域参数
fdtd.set("waveform type", "sine")        # 连续正弦波
fdtd.set("frequency", 1.94e14)           # 1550nm
fdtd.set("time start", 0)
fdtd.set("time stop", 100e-15)           # 100fs 时间窗口
fdtd.set("time points", 500)

# 设置光源类型
fdtd.set("source type", "plane wave")
fdtd.set("injection axis", "x")           # 仍沿x轴注入，但通过角度倾斜

# 设置振幅调制
fdtd.set("modulation type", "amplitude")
fdtd.set("modulation frequency", 1e9)     # 1GHz 振幅调制
fdtd.set("modulation depth", 0.3)

# 设置显示
fdtd.set("color", [1.0, 0.0, 0.0, 0.5])  # 红色半透明
```

## 注意事项

### 1. 时间分辨率与稳定性
- 时间步长 `dt` 必须满足 Courant 稳定性条件：`dt ≤ dx/(c√3)` 对于三维 FDTD
- 时间点数 `time points` 决定时间分辨率，影响波形细节
- 总时间跨度 `time stop - time start` 应足够长以包含完整脉冲

### 2. 频率内容与网格
- 脉冲带宽决定所需的最小网格尺寸：`dx ≤ λ_min/10`（建议）
- 高斯脉冲的带宽近似为 `Δf ≈ 0.44/τ`，其中 τ 是脉冲宽度（FWHM）
- 啁啾脉冲需要更宽的频率范围和更精细的网格

### 3. 自定义波形要求
- 自定义波形数据必须是二维数组 `[时间; 振幅]`
- 时间值必须单调递增
- 振幅值应在合理范围内，避免数值溢出
- 自定义波形会覆盖其他波形设置（如 `waveform type`）

### 4. 倾斜入射注意事项
- 倾斜角度较大时需要更大的光源区域以覆盖整个仿真区域
- 角度设置使用 `angle theta`（极角）和 `angle phi`（方位角）
- 对于大角度入射，可能需要调整边界条件（如 PML 设置）

### 5. 调制与啁啾
- 振幅调制：`amplitude × (1 + depth × sin(2πf_mod t))`
- 频率调制：`frequency + chirp_rate × t`
- 相位调制：`phase + depth × sin(2πf_mod t)`
- 调制频率应远小于载波频率

## 错误处理

### 常见错误
1. **时间参数无效**: `time start` ≥ `time stop` 或 `time points` ≤ 0
   - 解决方案：确保 `time start` < `time stop`，`time points` > 0

2. **自定义波形格式错误**: 数组维度不正确或时间非单调
   - 解决方案：检查自定义波形数组格式为 `[时间; 振幅]`

3. **频率超出范围**: `frequency` 为负值或过大
   - 解决方案：确保频率在合理范围内（通常 > 0）

4. **网格不匹配**: 脉冲带宽要求的网格尺寸小于实际网格
   - 解决方案：细化网格或减小脉冲带宽

5. **数值溢出**: 振幅过大导致计算不稳定
   - 解决方案：减小振幅或启用归一化

### Python 错误处理
```python
import lumapi
import numpy as np

try:
    fdtd = lumapi.FDTD()
    
    # 添加时域光源
    fdtd.addtds()
    
    # 配置光源属性
    fdtd.set("name", "test_tds")
    fdtd.set("x", -5e-6)
    
    # 检查时间参数
    time_start = fdtd.get("time start")
    time_stop = fdtd.get("time stop")
    time_points = fdtd.get("time points")
    
    if time_start >= time_stop:
        raise ValueError("time start 必须 < time stop")
    if time_points <= 0:
        raise ValueError("time points 必须 > 0")
    
    # 检查频率
    frequency = fdtd.get("frequency")
    if frequency <= 0:
        raise ValueError("频率必须 > 0")
    
    # 设置波形参数
    fdtd.set("waveform type", "gaussian")
    fdtd.set("pulse width", 20e-15)
    fdtd.set("center time", 50e-15)
    
    # 设置时间窗口
    fdtd.set("time start", 0)
    fdtd.set("time stop", 200e-15)
    fdtd.set("time points", 1000)
    
    # 设置频率
    fdtd.set("frequency", 1.94e14)  # 1550nm
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值
    fdtd.set("time start", 0)
    fdtd.set("time stop", 100e-15)
    fdtd.set("time points", 1000)
    fdtd.set("frequency", 1.94e14)
    
except lumapi.LumApiError as e:
    print(f"时域光源创建失败: {e}")
    
    # 检查具体错误
    if "time" in str(e).lower():
        print("错误: 时间参数无效")
    elif "waveform" in str(e).lower() or "custom" in str(e).lower():
        print("错误: 波形数据格式错误")
    elif "frequency" in str(e).lower():
        print("错误: 频率设置无效")
    elif "amplitude" in str(e).lower():
        print("错误: 振幅过大导致数值不稳定")
    elif "mesh" in str(e).lower():
        print("错误: 网格分辨率不足，请细化网格")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `addmode`: 添加模式光源（频域光源）
- `adddipole`: 添加偶极子光源（点源）
- `addmodesource`: 添加模式源（varFDTD）
- `setglobalsource`: 设置全局光源参数
- `getdata`: 获取时域数据
- `fourier`: 傅里叶变换（时域到频域）

## 产品支持

- **完全支持**: FDTD Solutions
- **有限支持**: MODE Solutions（部分功能）
- **不支持**: varFDTD, DEVICE, INTERCONNECT

## 应用场景

### 1. 超快脉冲传播
```python
# 分析飞秒脉冲在波导中的传播
fdtd.addtds()
fdtd.set("name", "femtosecond_pulse")
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 10e-15)  # 10fs 脉冲
fdtd.set("frequency", 1.94e14)   # 1550nm 中心波长
fdtd.set("time start", 0)
fdtd.set("time stop", 500e-15)   # 500fs 时间窗口
```

### 2. 调制信号传输
```python
# 模拟调制光信号在光链路中的传输
fdtd.addtds()
fdtd.set("name", "modulated_signal")
fdtd.set("waveform type", "sine")
fdtd.set("frequency", 1.94e14)           # 1550nm 载波
fdtd.set("modulation type", "amplitude")
fdtd.set("modulation frequency", 10e9)   # 10GHz 调制
fdtd.set("modulation depth", 0.8)        # 80% 调制深度
```

### 3. 非线性效应研究
```python
# 研究自相位调制等非线性效应
fdtd.addtds()
fdtd.set("name", "high_power_pulse")
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 100e-15)  # 100fs 脉冲
fdtd.set("amplitude", 5.0)        # 高功率
fdtd.set("chirp type", "linear")  # 包含啁啾以观察频谱展宽
fdtd.set("chirp rate", 5e23)
```

### 4. 脉冲压缩与展宽
```python
# 分析啁啾脉冲在色散介质中的压缩/展宽
fdtd.addtds()
fdtd.set("name", "chirped_pulse_compression")
fdtd.set("waveform type", "gaussian")
fdtd.set("pulse width", 200e-15)  # 200fs 初始脉冲
fdtd.set("chirp type", "linear")
fdtd.set("chirp rate", 2e24)      # 强啁啾
fdtd.set("bandwidth", 5e13)       # 50GHz 带宽
```

## 版本历史

| 版本 | 修改 |
|------|------|
 | Lumerical 2020a | 新增 `chirp type` 和啁啾参数 |
| Lumerical 2019a | 新增 `custom waveform` 支持用户定义波形 |
| Lumerical 2018a | 新增 `modulation type` 和调制参数 |
| Lumerical 2017a | 首次引入 `addtds` 命令 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical FDTD Solutions 用户指南 - 时域光源章节
2. 超快光学与脉冲传播理论
3. 调制技术与光通信
4. 非线性光学效应

---

 *最后更新: 2026-01-31*  
*文档版本: 1.1*