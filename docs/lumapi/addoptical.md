# addoptical

## 概述

`addoptical` 命令用于在 INTERCONNECT 仿真中添加光学端口。光学端口是光学器件与外部光路的接口，用于定义光信号的输入输出、模式匹配、功率耦合等，是光子集成电路仿真的关键组件。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addoptical;
```

### Python API (Lumapi)
```python
session.addoptical()
```

## 参数

`addoptical` 命令没有直接参数，但需要通过后续的 `set` 命令配置光学端口属性。

## 配置属性

添加光学端口后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "optical port" | 光学端口名称 |
| `enabled` | bool | true | 是否启用端口 |
| `port type` | string | "input" | 端口类型："input", "output", "bidirectional" |
| `port number` | int | 1 | 端口编号 |
| `group` | string | "default" | 端口组名 |

### 2. 几何与位置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 端口中心坐标 (m) |
| `rotation x` | float | 0 | X 轴旋转角度 (度) |
| `rotation y` | float | 0 | Y 轴旋转角度 (度) |
| `rotation z` | float | 0 | Z 轴旋转角度 (度) |
| `normal` | vector | [1,0,0] | 法线方向向量 |
| `tangent` | vector | [0,1,0] | 切线方向向量 |
| `aperture` | string | "circular" | 孔径形状："circular", "rectangular" |

### 3. 光学模式设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mode` | string | "fundamental" | 模式类型 |
| `mode number` | int | 1 | 模式编号 |
| `polarization` | string | "TE" | 偏振："TE", "TM", "both", "custom" |
| `effective index` | float | 自动计算 | 有效折射率 |
| `overlap integral` | float | 1 | 重叠积分（模式匹配度） |
| `mode field diameter` | float | 10e-6 | 模场直径 (m) |
| `numerical aperture` | float | 0.14 | 数值孔径 |

### 4. 波长与频谱
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `wavelength range` | vector | [1.5e-6, 1.6e-6] | 波长范围 [min, max] (m) |
| `frequency` | float | 自动计算 | 频率 (Hz) |
| `frequency range` | vector | 自动计算 | 频率范围 [min, max] (Hz) |
| `spectrum type` | string | "monochromatic" | 频谱类型 |
| `bandwidth` | float | 0 | 带宽 (Hz) |
| `center wavelength` | float | 1.55e-6 | 中心波长 (m) |

### 5. 功率与信号
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `optical power` | float | 1e-3 | 光功率 (W) |
| `input power` | float | 1e-3 | 输入功率 (W) |
| `output power` | float | 自动计算 | 输出功率 (W) |
| `insertion loss` | float | 0 | 插入损耗 (dB) |
| `return loss` | float | 自动计算 | 回波损耗 (dB) |
- `return loss` | float | 自动计算 | 回波损耗 (dB) |
| `signal type` | string | "cw" | 信号类型："cw", "pulse", "modulated" |
| `modulation format` | string | "none" | 调制格式 |

### 6. 耦合与匹配
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `coupling coefficient` | float | 1 | 耦合系数 |
| `mismatch loss` | float | 0 | 失配损耗 (dB) |
| `alignment tolerance` | float | 0.1e-6 | 对准容差 (m) |
| `angular tolerance` | float | 1 | 角度容差 (度) |
- `angular tolerance` | float | 1 | 角度容差 (度) |
| `reflection coefficient` | float | 0 | 反射系数 |
| `transmission coefficient` | float | 1 | 传输系数 |
| `s parameter` | matrix | 单位矩阵 | S 参数矩阵 |

### 7. 光纤参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `fiber type` | string | "smf28" | 光纤类型 |
| `core diameter` | float | 8.2e-6 | 纤芯直径 (m) |
| `cladding diameter` | float | 125e-6 | 包层直径 (m) |
| `core index` | float | 1.45 | 纤芯折射率 |
| `cladding index` | float | 1.444 | 包层折射率 |
| `cutoff wavelength` | float | 1.26e-6 | 截止波长 (m) |
| `dispersion` | float | 17 | 色散 (ps/nm·km) |

### 8. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `noise enabled` | bool | false | 是否启用噪声 |
| `noise figure` | float | 3 | 噪声系数 (dB) |
| `nonlinear effects` | bool | false | 是否考虑非线性效应 |
| `thermal effects` | bool | false | 是否考虑热效应 |
| `monitor` | bool | true | 是否监视端口信号 |
| `data logging` | bool | true | 是否记录数据 |

## 示例

### 示例 1：添加基本光学输入端口

#### LSF 脚本
```lumerical
// 添加光学输入端口
addoptical;

// 配置端口属性
set("name", "optical_input");
set("port type", "input");
set("optical power", 1e-3);  // 1 mW
set("wavelength", 1.55e-6);  // 1550 nm

// 配置模式设置
set("mode", "fundamental");
set("polarization", "TE");
set("mode field diameter", 10.4e-6);  // 单模光纤模场直径

// 配置几何位置
set("x", 0);
set("y", 0);
set("normal", [1, 0, 0]);  // 沿 X 轴方向
set("aperture", "circular");
```

#### Python API
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加光学输出端口
session.addoptical()
session.set("name", "wdm_output")
session.set("port type", "output")

# 配置多波长操作
session.set("wavelength range", [1.53e-6, 1.57e-6])  # C-band
session.set("spectrum type", "multiwavelength")
session.set("center wavelength", 1.55e-6)
session.set("bandwidth", 4e-9)  # 4 nm 带宽

# 配置光纤耦合
session.set("fiber type", "smf28")
session.set("core diameter", 8.2e-6)
session.set("coupling coefficient", 0.8)  # 80% 耦合效率
session.set("mismatch loss", 0.5)  # 0.5 dB 失配损耗

# 配置监控
session.set("monitor", True)
session.set("data logging", True)
```

### 示例 3：双向光学端口用于环形谐振器
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加双向光学端口
session.addoptical()
session.set("name", "ring_resonator_port")
session.set("port type", "bidirectional")
session.set("port number", 1)

# 配置环形谐振器特定设置
session.set("effective index", 2.4)  # 硅波导有效折射率
session.set("mode field diameter", 0.5e-6)  # 纳米波导小模场

# 配置 S 参数（环形谐振器特性）
import numpy as np
# 创建环形谐振器的 S 参数矩阵（2×2）
s11 = 0.1  # 反射
s12 = 0.9  # 直通
s21 = 0.9  # 直通  
s22 = 0.1  # 反射
session.set("s parameter", [[s11, s12], [s21, s22]])

# 配置波长相关响应
wavelengths = np.linspace(1.54e-6, 1.56e-6, 1001)
# 创建环形谐振器的洛伦兹型响应
fsr = 1e-9  # 自由光谱范围 1 nm
transmission = 1 - 0.8 / (1 + ((wavelengths - 1.55e-6) / (fsr/2))**2)
session.set("wavelength dependent s", transmission)

# 配置高级特性
session.set("noise enabled", True)
session.set("noise figure", 5)  # 5 dB 噪声系数
session.set("thermal effects", True)
```

## 返回值

`addoptical` 命令没有直接的返回值。成功执行后，会在 INTERCONNECT 仿真中添加一个光学端口对象，该对象可以通过 `set` 命令配置各种光学属性。

## 错误处理

### 常见错误
1. **无效的波长值**
   - 错误信息：`Invalid wavelength value`
   - 解决方案：确保波长在合理范围内（通常 0.1-10 μm）

2. **模式不支持**
   - 错误信息：`Mode not supported`
   - 解决方案：检查模式类型是否受支持

3. **功率超出范围**
   - 错误信息：`Optical power out of range`
   - 解决方案：调整功率值到合理范围

4. **端口冲突**
   - 错误信息：`Port conflict`
   - 解决方案：确保端口名称或编号唯一

### Python 错误处理示例
```python
import lumapi

try:
    # 创建 INTERCONNECT 会话
    ic = lumapi.INTERCONNECT()
    
    # 添加光学端口
    ic.addoptical()
    ic.set("name", "test_port")
    ic.set("port type", "input")
    ic.set("optical power", 1e-3)
    ic.set("wavelength", -1e-6)  # 无效的负波长
    
except lumapi.LumApiError as e:
    print(f"光学端口创建失败: {e}")
    
    # 检查具体错误类型
    if "wavelength" in str(e).lower():
        print("错误: 无效的波长值")
    elif "mode" in str(e).lower():
        print("错误: 不支持的模式")
    elif "power" in str(e).lower():
        print("错误: 功率超出范围")
    elif "conflict" in str(e).lower():
        print("错误: 端口冲突")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **模式匹配**：确保端口模式与连接波导模式匹配以减少插入损耗
2. **偏振处理**：正确设置偏振以避免偏振相关损耗
3. **波长范围**：设置合理的波长范围覆盖仿真需求
4. **功率单位**：光学功率通常使用瓦特 (W) 或分贝毫瓦 (dBm)
5. **物理合理性**：端口参数应在物理合理范围内
6. **仿真效率**：过多端口或复杂波长设置可能降低仿真速度

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 支持

## 相关命令

- `addnoise` - 添加噪声源
- `addevent` - 添加事件监视器
- `addport` - 添加通用端口（电学/光学）
- `callsplitter` - 调用分路器模型
- `cascadedsmatrix` - 计算级联 S 矩阵
- `set` - 设置对象属性
- `getoptical` - 获取光学数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增多波长端口支持 |
| Lumerical 2019a | 增强光纤耦合参数配置 |
| Lumerical 2018a | 初始光学端口功能 |

## 参考

1. INTERCONNECT 光学端口用户指南
2. 光纤耦合和模式匹配原理
3. 光子集成电路设计基础

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*