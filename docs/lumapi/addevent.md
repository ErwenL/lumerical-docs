# addevent

## 概述

`addevent` 命令用于在 INTERCONNECT 仿真中添加事件监视器。事件监视器用于检测和记录仿真过程中的特定事件，如信号过零、阈值触发、状态变化等，适用于数字信号处理、时钟恢复、触发控制等应用。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addevent;
```

### Python API (Lumapi)
```python
session.addevent()
```

## 参数

`addevent` 命令没有直接参数，但需要通过后续的 `set` 命令配置事件监视器属性。

## 配置属性

添加事件监视器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "event" | 事件监视器名称 |
| `enabled` | bool | true | 是否启用监视器 |
| `description` | string | "" | 描述信息 |

### 2. 事件检测设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `event type` | string | "threshold" | 事件检测类型 |
| `input signal` | string | "" | 输入信号名称 |
| `threshold` | float | 0 | 触发阈值 |
| `hysteresis` | float | 0 | 迟滞值 |
| `edge direction` | string | "rising" | 边沿方向："rising", "falling", "both" |
| `debounce time` | float | 0 | 去抖时间 (s) |
| `minimum pulse width` | float | 0 | 最小脉冲宽度 (s) |
| `maximum pulse width` | float | inf | 最大脉冲宽度 (s) |

### 事件类型选项：
- **阈值触发**: `"threshold"` - 信号超过阈值时触发
- **边沿检测**: `"edge"` - 信号边沿触发
- **脉冲检测**: `"pulse"` - 脉冲宽度检测
- **窗口比较**: `"window"` - 信号在窗口内/外触发
- **状态机**: `"state"` - 状态机状态变化触发

### 3. 触发条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `trigger condition` | string | "immediate" | 触发条件 |
| `trigger delay` | float | 0 | 触发延迟 (s) |
| `trigger holdoff` | float | 0 | 触发保持时间 (s) |
| `retriggerable` | bool | true | 是否可重复触发 |
| `maximum events` | int | inf | 最大事件记录数 |

### 4. 动作设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `action type` | string | "record" | 动作类型 |
| `output signal` | string | "" | 输出信号名称 |
| `output value` | float | 1 | 输出值 |
| `output duration` | float | 0 | 输出持续时间 (s) |
| `execute script` | string | "" | 执行脚本代码 |

### 动作类型选项：
- **记录事件**: `"record"` - 记录事件时间和数据
- **输出信号**: `"output"` - 生成输出信号
- **执行脚本**: `"script"` - 执行自定义脚本
- **控制仿真**: `"control"` - 控制仿真流程（暂停、停止等）

### 5. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record time` | bool | true | 是否记录事件时间 |
| `record value` | bool | true | 是否记录事件值 |
| `record data` | bool | false | 是否记录完整数据 |
| `data buffer size` | int | 1000 | 数据缓冲区大小 |
| `time format` | string | "seconds" | 时间格式："seconds", "samples" |
| `timestamp` | bool | true | 是否添加时间戳 |

### 6. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `synchronization` | string | "none" | 同步方式 |
| `clock signal` | string | "" | 时钟信号名称 |
| `clock edge` | string | "rising" | 时钟边沿 |
| `setup time` | float | 0 | 建立时间 (s) |
| `hold time` | float | 0 | 保持时间 (s) |
| `jitter tolerance` | float | 0 | 抖动容限 (s) |

## 示例

### 示例 1：添加基本事件监视器

#### LSF 脚本
```lumerical
// 添加事件监视器
addevent;

// 配置监视器属性
set("name", "threshold_detector");
set("event type", "threshold");
set("input signal", "input_signal");
set("threshold", 0.5);
set("edge direction", "rising");
set("hysteresis", 0.1);

// 配置记录设置
set("record time", true);
set("record value", true);
set("maximum events", 100);
```

#### Python API
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加时钟恢复事件监视器
session.addevent()
session.set("name", "clock_recovery")
session.set("event type", "edge")
session.set("input signal", "data_signal")
session.set("threshold", 0.5)
session.set("edge direction", "both")

# 配置时钟恢复参数
session.set("debounce time", 10e-12)  # 10 ps 去抖
session.set("minimum pulse width", 20e-12)  # 最小脉冲宽度 20 ps
session.set("retriggerable", False)  # 不可重复触发

# 配置输出动作
session.set("action type", "output")
session.set("output signal", "recovered_clock")
session.set("output value", 1)
session.set("output duration", 50e-12)  # 50 ps 时钟脉冲
```

### 示例 3：状态机事件监视器
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加状态机事件监视器
session.addevent()
session.set("name", "state_machine_monitor")
session.set("event type", "state")
session.set("input signal", "control_signal")

# 配置状态转换条件
session.set("trigger condition", "state_transition")
session.set("from state", 0)  # 从状态 0
session.set("to state", 1)    # 转换到状态 1

# 配置脚本动作
custom_script = """
# 事件触发时执行的脚本
print("State transition detected at time: " + num2str(t));
# 可以执行更复杂的控制逻辑
log_data("state_change", t, value);
"""

session.set("action type", "script")
session.set("execute script", custom_script)
session.set("record data", True)
session.set("data buffer size", 10000)
```

## 返回值

`addevent` 命令没有直接的返回值。成功执行后，会在 INTERCONNECT 仿真中添加一个事件监视器对象，该对象可以通过 `set` 命令配置事件检测和动作设置。

## 错误处理

### 常见错误
1. **信号不存在**
   - 错误信息：`Input signal not found`
   - 解决方案：检查输入信号名称是否正确

2. **无效的事件类型**
   - 错误信息：`Invalid event type`
   - 解决方案：检查事件类型是否受支持

3. **触发条件冲突**
   - 错误信息：`Trigger condition conflict`
   - 解决方案：检查触发条件设置是否合理

4. **缓冲区溢出**
   - 错误信息：`Data buffer overflow`
   - 解决方案：增加数据缓冲区大小或减少事件数量

### Python 错误处理示例
```python
import lumapi

try:
    # 创建 INTERCONNECT 会话
    ic = lumapi.INTERCONNECT()
    
    # 添加事件监视器
    ic.addevent()
    ic.set("name", "test_event")
    ic.set("event type", "invalid_type")  # 无效的事件类型
    ic.set("input signal", "non_existent_signal")  # 不存在的信号
    
except lumapi.LumApiError as e:
    print(f"事件监视器创建失败: {e}")
    
    # 检查具体错误类型
    if "signal" in str(e).lower():
        print("错误: 信号不存在")
    elif "event type" in str(e).lower():
        print("错误: 无效的事件类型")
    elif "trigger" in str(e).lower():
        print("错误: 触发条件冲突")
    elif "buffer" in str(e).lower():
        print("错误: 缓冲区溢出")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **信号名称**：确保 input_signal 和 output_signal 指向有效的信号名称
2. **时间单位**：INTERCONNECT 中使用秒作为基本时间单位
3. **仿真性能**：复杂的事件检测可能影响仿真速度
4. **缓冲区大小**：根据预期事件数量合理设置数据缓冲区大小
5. **去抖设置**：对于噪声信号，适当的去抖时间可以防止误触发

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 支持

## 相关命令

- `addnoise` - 添加噪声源
- `addoptical` - 添加光学端口
- `callsplitter` - 调用分路器模型
- `cascadedsmatrix` - 计算级联 S 矩阵
- `set` - 设置对象属性
- `getevents` - 获取事件数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增状态机事件支持 |
| Lumerical 2019a | 增强事件动作功能 |
| Lumerical 2018a | 初始事件监视器功能 |

## 参考

1. INTERCONNECT 事件检测用户指南
2. 数字信号处理中的事件检测原理
3. 时钟恢复和触发技术

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*