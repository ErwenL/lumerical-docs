# addnoise

## 概述

`addnoise` 命令用于在 INTERCONNECT 仿真中添加噪声源。噪声源模拟电子和光学系统中的各种噪声机制，包括热噪声、散粒噪声、闪烁噪声等，用于分析系统的噪声特性、信噪比、噪声系数等性能指标。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addnoise;
```

### Python API (Lumapi)
```python
session.addnoise()
```

## 参数

`addnoise` 命令没有直接参数，但需要通过后续的 `set` 命令配置噪声源属性。

## 配置属性

添加噪声源后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "noise" | 噪声源名称 |
| `enabled` | bool | true | 是否启用噪声源 |
| `noise type` | string | "white" | 噪声类型 |
| `port type` | string | "electrical" | 端口类型："electrical", "optical" |

### 2. 噪声类型设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `noise density` | float | 1e-12 | 噪声密度 (A²/Hz 或 V²/Hz) |
| `noise figure` | float | 3 | 噪声系数 (dB) |
| `temperature` | float | 300 | 温度 (K)，用于热噪声 |
| `resistance` | float | 50 | 电阻 (Ω)，用于热噪声 |
| `shot current` | float | 1e-3 | 散粒噪声电流 (A) |
| `flicker coefficient` | float | 1e-12 | 闪烁噪声系数 |
| `flicker exponent` | float | 1 | 闪烁噪声指数 |

### 噪声类型选项：
- **白噪声**: `"white"` - 平坦频谱噪声
- **热噪声**: `"thermal"` - 约翰逊-奈奎斯特噪声
- **散粒噪声**: `"shot"` - 散粒噪声
- **闪烁噪声**: `"flicker"` - 1/f 噪声
- **自定义噪声**: `"custom"` - 用户定义噪声谱

### 3. 频谱特性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency range` | vector | [0, 100e9] | 频率范围 [fmin, fmax] (Hz) |
| `frequency points` | int | 1001 | 频率点数 |
| `psd` | matrix | [] | 功率谱密度数据 |
| `psd frequency` | vector | [] | PSD 频率点 |
| `correlation` | matrix | 单位矩阵 | 噪声相关矩阵 |
| `noise bandwidth` | float | 1e9 | 噪声带宽 (Hz) |

### 4. 端口与连接
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `input port` | string | "" | 输入端口名称 |
| `output port` | string | "" | 输出端口名称 |
| `impedance` | float | 50 | 阻抗 (Ω) |
| `reference impedance` | float | 50 | 参考阻抗 (Ω) |
| `matching network` | string | "none" | 匹配网络类型 |

### 5. 光学噪声设置（光学端口）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `optical power` | float | 1e-3 | 光功率 (W) |
| `phase noise` | float | 1e-6 | 相位噪声 (rad²/Hz) |
| `amplitude noise` | float | 1e-6 | 幅度噪声 |
-6 | 幅度噪声 (W²/Hz) |
| `relative intensity noise` | float | -150 | 相对强度噪声 (dB/Hz) |
| `linewidth` | float | 1e6 | 线宽 (Hz) |
| `coherence time` | float | 自动计算 | 相干时间 (s) |

### 6. 统计特性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `distribution` | string | "gaussian" | 统计分布 |
| `mean` | float | 0 | 均值 |
| `standard deviation` | float | 1 | 标准差 |
| `skewness` | float | 0 | 偏度 |
| `kurtosis` | float | 3 | 峰度 |
| `seed` | int | 0 | 随机数种子（0 表示随机） |

### 分布类型选项：
- **高斯分布**: `"gaussian"` - 正态分布
- **均匀分布**: `"uniform"` - 均匀分布
- **瑞利分布**: `"rayleigh"` - 瑞利分布
- **泊松分布**: `"poisson"` - 泊松分布
- **自定义分布**: `"custom"` - 用户定义分布

### 7. 仿真设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `simulation type` | string | "small signal" | 仿真类型 |
| `noise analysis` | bool | true | 是否进行噪声分析 |
| `monte carlo samples` | int | 1000 | 蒙特卡洛采样数 |
| `convergence tolerance` | float | 1e-3 | 收敛容差 |
| `max iterations` | int | 100 | 最大迭代次数 |

### 8. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `save noise data` | bool | true | 是否保存噪声数据 |
| `noise figure output` | bool | false | 是否输出噪声系数 |
| `psd output` | bool | true | 是否输出功率谱密度 |
| `time domain output` | bool | false | 是否输出时域噪声 |
- `time domain output` | bool | false | 是否输出时域噪声 |
| `output format` | string | "complex" | 输出格式："complex", "magnitude", "phase" |

## 示例

### 示例 1：添加基本热噪声源

#### LSF 脚本
```lumerical
// 添加热噪声源
addnoise;

// 配置噪声源属性
set("name", "thermal_noise");
set("noise type", "thermal");
set("port type", "electrical");
set("temperature", 300);  // 室温
set("resistance", 50);    // 50 Ω 电阻
set("noise bandwidth", 10e9);  // 10 GHz 带宽

// 配置频谱设置
set("frequency range", [0, 20e9]);  // 0-20 GHz
set("frequency points", 2001);

// 配置输出
set("save noise data", true);
set("psd output", true);
```

#### Python API
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加光学噪声源
session.addnoise()
session.set("name", "optical_shot_noise")
session.set("port type", "optical")
session.set("noise type", "shot")

# 配置光学参数
session.set("wavelength", 1.55e-6)  # 1550 nm
session.set("optical power", 1e-3)  # 1 mW
session.set("shot current", 1e-3)   # 1 mA 对应电流

# 配置噪声特性
session.set("relative intensity noise", -140)  # -140 dB/Hz RIN
session.set("linewidth", 1e6)  # 1 MHz 线宽

# 配置统计特性
session.set("distribution", "poisson")  # 散粒噪声服从泊松统计
session.set("seed", 12345)  # 固定随机种子用于可重复性
```

### 示例 3：自定义噪声谱
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 添加噪声源
session.addnoise()
session.set("name", "custom_noise_profile")
session.set("noise type", "custom")

# 生成自定义噪声谱
frequencies = np.linspace(0, 100e9, 1001)  # 0-100 GHz
# 创建低频增强的噪声谱（1/f 特性）
psd = 1e-12 / (frequencies + 1e6)  # 1/f 特性，避免除零
psd[0] = psd[1]  # 修复 DC 点

# 设置自定义 PSD
session.set("psd frequency", frequencies)
session.set("psd", psd)

# 配置相关噪声（双端口）
session.set("correlation", [[1, 0.5], [0.5, 1]])  # 部分相关

# 配置高级仿真
session.set("simulation type", "large signal")
session.set("monte carlo samples", 5000)
session.set("convergence tolerance", 1e-4)

# 配置输出
session.set("time domain output", True)
session.set("output format", "complex")
```

## 返回值

`addnoise` 命令没有直接的返回值。成功执行后，会在 INTERCONNECT 仿真中添加一个噪声源对象，该对象可以通过 `set` 命令配置各种噪声属性。

## 错误处理

### 常见错误
1. **无效的噪声类型**
   - 错误信息：`Invalid noise type`
   - 解决方案：检查噪声类型是否受支持

2. **频率范围错误**
   - 错误信息：`Invalid frequency range`
   - 解决方案：确保频率范围合理（fmin < fmax）

3. **功率谱密度数据不匹配**
   - 错误信息：`PSD data mismatch`
   - 解决方案：检查 PSD 数据和频率点数组长度是否一致

4. **参数超出范围**
   - 错误信息：`Parameter out of range`
   - 解决方案：检查噪声参数是否在物理合理范围内

### Python 错误处理示例
```python
import lumapi

try:
    # 创建 INTERCONNECT 会话
    ic = lumapi.INTERCONNECT()
    
    # 添加噪声源
    ic.addnoise()
    ic.set("name", "test_noise")
    ic.set("noise type", "invalid_type")  # 无效的噪声类型
    
except lumapi.LumApiError as e:
    print(f"噪声源创建失败: {e}")
    
    # 检查具体错误类型
    if "noise type" in str(e).lower():
        print("错误: 无效的噪声类型")
    elif "frequency" in str(e).lower():
        print("错误: 无效的频率范围")
    elif "psd" in str(e).lower():
        print("错误: PSD 数据不匹配")
    elif "parameter" in str(e).lower():
        print("错误: 参数超出范围")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **噪声类型匹配**：确保噪声类型与应用场景匹配（热噪声、散粒噪声等）
2. **单位一致性**：注意噪声密度单位（A²/Hz, V²/Hz, W/Hz 等）
3. **频率范围**：设置合理的频率范围覆盖感兴趣频段
4. **统计准确性**：蒙特卡洛仿真需要足够采样数获得准确统计
5. **计算复杂度**：复杂噪声模型和大量采样会增加仿真时间
6. **物理合理性**：噪声参数应在物理合理范围内

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 支持

## 相关命令

- `addoptical` - 添加光学端口
- `addevent` - 添加事件监视器
- `callsplitter` - 调用分路器模型
- `cascadedsmatrix` - 计算级联 S 矩阵
- `set` - 设置对象属性
- `getnoise` - 获取噪声数据
- `analyzenoise` - 分析噪声特性

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增光学噪声支持 |
| Lumerical 2019a | 增强自定义噪声谱功能 |
| Lumerical 2018a | 初始噪声源功能 |

## 参考

1. INTERCONNECT 噪声分析指南
2. 电子和光学噪声原理
3. 噪声系数和噪声温度测量

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*