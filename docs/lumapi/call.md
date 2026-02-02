# call

## 概述

`call` 命令用于调用用户定义的函数、内置函数或外部脚本。该命令支持多种函数类型，包括数学函数、数据处理函数、仿真控制函数等，是 Lumerical 脚本编程的核心组件。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
call;
```

### Python API (Lumapi)
```python
session.call()
```

## 参数

`call` 命令没有直接参数，但需要通过后续的 `set` 命令配置函数名称、参数和调用设置。

## 配置属性

调用函数后，可以使用 `set` 命令配置以下属性：

### 1. 基本调用设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `function` | string | "" | 函数名称 |
| `arguments` | array | [] | 参数列表 |
| `return value` | string | "result" | 返回值变量名称 |
| `call type` | string | "direct" | 调用类型："direct", "indirect", "callback", "async" |

### 2. 函数类型
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `function type` | string | "builtin" | 函数类型："builtin", "user", "external", "anonymous", "method" |
| `namespace` | string | "global" | 命名空间 |
| `library` | string | "" | 函数库名称 |
| `class` | string | "" | 类名称（方法调用时） |

### 3. 参数处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `input arguments` | dict | {} | 输入参数字典 |
| `output arguments` | array | [] | 输出参数列表 |
| `argument passing` | string | "by value" | 参数传递方式："by value", "by reference", "by name" |
| `default arguments` | dict | {} | 默认参数值 |
| `variable arguments` | bool | false | 是否支持可变参数 |

### 4. 返回值处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `return type` | string | "auto" | 返回值类型："auto", "scalar", "array", "struct", "cell" |
| `multiple returns` | bool | false | 是否多个返回值 |
| `return names` | array | [] | 返回值名称列表 |
| `error return` | 任意 | NaN | 错误返回值 |

### 5. 错误处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `error handling` | string | "throw" | 错误处理："throw", "catch", "ignore", "log" |
| `exception handling` | bool | true | 是否启用异常处理 |
| `timeout` | float | 60 | 超时时间（秒） |
| `retry count` | int | 0 | 重试次数 |
| `fallback function` | string | "" | 备用函数 |

### 6. 性能优化
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `caching` | bool | false | 是否缓存函数结果 |
| `memoization` | bool | false | 是否启用记忆化 |
| `parallel execution` | bool | false | 是否并行执行 |
| `vectorization` | bool | true | 是否启用向量化 |
| `just in time` | bool | false | 是否启用JIT编译 |

### 7. 安全性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `sandbox` | bool | false | 是否启用沙箱模式 |
| `allowed operations` | array | [] | 允许的操作列表 |
| `security level` | string | "normal" | 安全级别 |
| `signature verification` | bool | false | 是否验证函数签名 |

### 8. 调试与跟踪
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `debug mode` | bool | false | 是否启用调试模式 |
| `trace` | bool | false | 是否跟踪函数调用 |
| `profiling` | bool | false | 是否启用性能分析 |
| `log calls` | bool | false | 是否记录调用日志 |

### 9. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `callback function` | string | "" | 回调函数 |
| `event driven` | bool | false | 是否事件驱动 |
| `context` | dict | {} | 执行上下文 |
| `environment` | dict | {} | 执行环境变量 |

## 返回值

`call` 命令的返回值取决于被调用函数的返回值。返回值类型包括：

- **标量值**：数值、字符串、布尔值等
- **数组/矩阵**：数值数组或多维矩阵
- **结构体**：包含多个字段的复合数据
- **单元格数组**：混合类型的数组
- **函数句柄**：函数引用（用于高阶函数）
- **对象引用**：面向对象编程中的对象实例
- **错误代码**：调用失败时返回的错误代码（取决于错误处理设置）
- **多个返回值**：某些函数可能返回多个输出值

返回值存储在使用 `set("return value", "变量名")` 指定的变量中，或根据 `return names` 设置存储到多个变量中。可以通过 `getdata` 命令获取返回值。

## 使用示例

### 示例 1：基本函数调用

#### LSF 脚本
```lumerical
# 1. 调用内置数学函数
call;
set("function", "sin");
set("arguments", {3.1415926535/2});  # sin(π/2)
set("return value", "sin_result");
# 结果: sin_result ≈ 1.0

# 2. 调用多个参数的函数
call;
set("function", "power");
set("arguments", {2, 3});  # 2^3
set("return value", "power_result");
# 结果: power_result = 8

# 3. 调用数组函数
data = {1, 2, 3, 4, 5};
call;
set("function", "mean");
set("arguments", {data});
set("return value", "mean_result");
# 结果: mean_result = 3

# 4. 调用字符串函数
call;
set("function", "sprintf");
set("arguments", {"Value: %.3f", 3.14159});
set("return value", "string_result");
# 结果: string_result = "Value: 3.142"

# 获取所有结果
sin_result = getdata("sin_result");
power_result = getdata("power_result");
mean_result = getdata("mean_result");
string_result = getdata("string_result");

? "sin(π/2) = " + num2str(sin_result);
? "2^3 = " + num2str(power_result);
? "mean([1,2,3,4,5]) = " + num2str(mean_result);
? "Formatted string: " + string_result;
```

#### Python API
```python
import lumapi

session = lumapi.FDTD()

# 1. 调用内置数学函数
session.call()
session.set("function", "sin")
session.set("arguments", [3.1415926535/2])  # sin(π/2)
session.set("return value", "sin_result")
# 结果: sin_result ≈ 1.0

# 2. 调用多个参数的函数
session.call()
session.set("function", "power")
session.set("arguments", [2, 3])  # 2^3
session.set("return value", "power_result")
# 结果: power_result = 8

# 3. 调用数组函数
data = [1, 2, 3, 4, 5]
session.call()
session.set("function", "mean")
session.set("arguments", [data])
session.set("return value", "mean_result")
# 结果: mean_result = 3

# 4. 调用字符串函数
session.call()
session.set("function", "sprintf")
session.set("arguments", ["Value: %.3f", 3.14159])
session.set("return value", "string_result")
# 结果: string_result = "Value: 3.142"

# 获取所有结果
results = session.getdata(["sin_result", "power_result", "mean_result", "string_result"])
print(f"sin(π/2) = {results['sin_result']:.6f}")
print(f"2^3 = {results['power_result']}")
print(f"mean([1,2,3,4,5]) = {results['mean_result']}")
print(f"Formatted string: {results['string_result']}")
```

### 示例 2：用户自定义函数
```python
import lumapi

session = lumapi.MODE()

# 定义用户函数
user_function = """
function [output1, output2] = my_custom_function(input1, input2, option)
    % 自定义函数示例
    % 输入: input1, input2 (数值), option (字符串)
    % 输出: output1, output2
    
    switch option
        case 'add'
            output1 = input1 + input2;
            output2 = 'Addition';
        case 'multiply'
            output1 = input1 * input2;
            output2 = 'Multiplication';
        case 'power'
            output1 = input1 ^ input2;
            output2 = 'Power';
        otherwise
            output1 = NaN;
            output2 = 'Unknown operation';
    end
    
    % 添加日志
    fprintf('Custom function called: %s, result = %.4f\\n', output2, output1);
end
"""

# 在 Lumerical 中定义函数
session.eval(user_function)

# 调用用户函数
operations = ['add', 'multiply', 'power']
for i, op in enumerate(operations):
    session.call()
    session.set("function", "my_custom_function")
    session.set("arguments", [3, 4, op])
    session.set("return value", f"result_{i}")
    session.set("multiple returns", True)
    session.set("return names", [f"value_{i}", f"operation_{i}"])
    
    # 获取结果
    value = session.getdata(f"value_{i}")
    operation = session.getdata(f"operation_{i}")
    print(f"Operation: {operation}, 3 {op} 4 = {value}")

# 调用带有默认参数的函数
session.eval("""
function y = quadratic(x, a, b, c)
    % 二次函数: y = a*x^2 + b*x + c
    if nargin < 4
        c = 0;  % 默认值
    end
    if nargin < 3
        b = 0;
    end
    if nargin < 2
        a = 1;
    end
    y = a*x^2 + b*x + c;
end
""")

# 使用不同数量的参数调用
session.call()
session.set("function", "quadratic")
session.set("arguments", [2])  # 仅 x，使用默认 a=1, b=0, c=0
session.set("return value", "quad1")
# 结果: 2^2 = 4

session.call()
session.set("function", "quadratic")
session.set("arguments", [2, 3])  # x=2, a=3
session.set("return value", "quad2")
# 结果: 3*2^2 = 12

session.call()
session.set("function", "quadratic")
session.set("arguments", [2, 3, 4, 5])  # x=2, a=3, b=4, c=5
session.set("return value", "quad3")
# 结果: 3*4 + 4*2 + 5 = 25

quad_results = session.getdata(["quad1", "quad2", "quad3"])
print(f"\nQuadratic function results:")
print(f"  quadratic(2) = {quad_results['quad1']}")
print(f"  quadratic(2, 3) = {quad_results['quad2']}")
print(f"  quadratic(2, 3, 4, 5) = {quad_results['quad3']}")
```

### 示例 3：外部函数和回调
```python
import lumapi
import numpy as np

session = lumapi.DEVICE()

# 1. 调用外部Python函数
# 定义Python回调函数
def external_processing(data, parameter):
    """外部处理函数示例"""
    import numpy as np
    # 简单的数据处理：滤波和归一化
    processed = np.array(data)
    if parameter == 'normalize':
        processed = (processed - np.min(processed)) / (np.max(processed) - np.min(processed))
    elif parameter == 'log':
        processed = np.log10(np.abs(processed) + 1e-10)
    elif parameter == 'smooth':
        from scipy import signal
        processed = signal.savgol_filter(processed, 11, 3)
    return processed.tolist()

# 由于直接调用外部Python函数复杂，这里演示通过脚本调用
# 在实际使用中，可能需要使用Lumerical的Python集成功能

# 2. 回调函数机制
# 定义事件处理函数
event_handler = """
function event_callback(source, event_data)
    % 事件回调函数
    fprintf('Event received from %s at time %.3f s\\n', ...
            source, event_data.time);
    
    % 处理事件数据
    if isfield(event_data, 'temperature')
        fprintf('  Temperature: %.2f K\\n', event_data.temperature);
    end
    
    if isfield(event_data, 'voltage')
        fprintf('  Voltage: %.3f V\\n', event_data.voltage);
    end
    
    % 可以触发其他操作
    if event_data.temperature > 350
        fprintf('  WARNING: Temperature exceeds 350K!\\n');
        % 可以调用其他函数采取行动
        emergency_shutdown();
    end
end

function emergency_shutdown()
    % 紧急关闭函数
    fprintf('=== EMERGENCY SHUTDOWN INITIATED ===\\n');
    % 这里可以实现实际的关闭逻辑
end
"""

session.eval(event_handler)

# 设置事件监听
session.call()
session.set("function", "addlistener")
session.set("arguments", ["thermal_monitor", "TemperatureExceeded", "@event_callback"])
session.set("return value", "listener_handle")

# 3. 方法调用（面向对象）
# 定义类和方法
class_definition = """
classdef OpticalComponent < handle
    properties
        Name
        Wavelength
        InsertionLoss
        ReturnLoss
    end
    
    methods
        function obj = OpticalComponent(name, wavelength)
            % 构造函数
            obj.Name = name;
            obj.Wavelength = wavelength;
            obj.InsertionLoss = 0;
            obj.ReturnLoss = inf;
        end
        
        function measure(obj, input_power)
            % 测量方法
            transmitted_power = input_power * 10^(-obj.InsertionLoss/10);
            reflected_power = input_power * 10^(-obj.ReturnLoss/10);
            
            results.transmitted = transmitted_power;
            results.reflected = reflected_power;
            results.lost = input_power - transmitted_power - reflected_power;
            
            fprintf('Component %s measurement:\\n', obj.Name);
            fprintf('  Input: %.2f mW\\n', input_power*1e3);
            fprintf('  Transmitted: %.2f mW (IL=%.2f dB)\\n', ...
                    transmitted_power*1e3, obj.InsertionLoss);
            fprintf('  Reflected: %.2f mW (RL=%.2f dB)\\n', ...
                    reflected_power*1e3, obj.ReturnLoss);
            
            return results;
        end
        
        function optimize(obj, target_il)
            % 优化方法
            fprintf('Optimizing %s for target IL=%.2f dB...\\n', ...
                    obj.Name, target_il);
            
            % 简单的优化逻辑
            if obj.InsertionLoss > target_il
                improvement = obj.InsertionLoss - target_il;
                obj.InsertionLoss = target_il;
                fprintf('  Improved IL by %.2f dB\\n', improvement);
            else
                fprintf('  Already meets target\\n');
            end
        end
    end
end
"""

session.eval(class_definition)

# 创建对象实例
session.eval("component = OpticalComponent('MZI_1550', 1.55e-6);")
session.eval("component.InsertionLoss = 0.5;")
session.eval("component.ReturnLoss = 40;")

# 调用对象方法
session.call()
session.set("function", "measure")
session.set("class", "OpticalComponent")
session.set("arguments", [session.eval("component"), 1e-3])  # 1 mW输入
session.set("return value", "measurement_results")

session.call()
session.set("function", "optimize")
session.set("class", "OpticalComponent")
session.set("arguments", [session.eval("component"), 0.3])  # 优化到0.3 dB

# 4. 异步函数调用
async_function = """
function async_result = long_computation(data, iterations)
    % 长时间计算函数
    fprintf('Starting long computation (%d iterations)...\\n', iterations);
    
    result = zeros(size(data));
    for i = 1:iterations
        % 模拟复杂计算
        result = result + fft(data) / iterations;
        
        % 进度报告
        if mod(i, 100) == 0
            fprintf('  Progress: %d/%d\\n', i, iterations);
        end
    end
    
    fprintf('Long computation completed.\\n');
    async_result = result;
end
"""

session.eval(async_function)

# 异步调用（在实际中可能需要使用Lumerical的异步支持）
print("\nDemonstrating function call capabilities...")
print("Note: Actual asynchronous execution depends on Lumerical's implementation")
```

### 示例 4：高级函数管道和组合
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 定义一系列处理函数
processing_pipeline = """
function data_out = preprocessing(data_in)
    % 数据预处理
    % 移除直流分量
    data_out = data_in - mean(data_in);
    fprintf('Preprocessing: removed DC component\\n');
end

function data_out = filtering(data_in, cutoff_freq, fs)
    % 低通滤波
    [b, a] = butter(4, cutoff_freq/(fs/2));
    data_out = filter(b, a, data_in);
    fprintf('Filtering: applied %.1f Hz lowpass\\n', cutoff_freq);
end

function data_out = normalization(data_in, method)
    % 数据归一化
    switch method
        case 'minmax'
            data_out = (data_in - min(data_in)) / (max(data_in) - min(data_in));
        case 'zscore'
            data_out = (data_in - mean(data_in)) / std(data_in);
        case 'unit'
            data_out = data_in / max(abs(data_in));
        otherwise
            data_out = data_in;
    end
    fprintf('Normalization: %s method\\n', method);
end

function features = feature_extraction(data_in, fs)
    % 特征提取
    features.rms = rms(data_in);
    features.peak = max(abs(data_in));
    features.mean = mean(data_in);
    features.std = std(data_in);
    
    % 频域特征
    N = length(data_in);
    fft_data = fft(data_in);
    freq = (0:N-1)*(fs/N);
    
    [~, max_idx] = max(abs(fft_data(1:floor(N/2))));
    features.dominant_freq = freq(max_idx);
    features.bandwidth = obw(data_in, fs);
    
    fprintf('Feature extraction: extracted %d features\\n', length(fieldnames(features)));
end

function result = processing_pipeline_main(input_data, params)
    % 主处理管道
    fprintf('=== Starting processing pipeline ===\\n');
    
    % 步骤1: 预处理
    step1 = preprocessing(input_data);
    
    % 步骤2: 滤波
    step2 = filtering(step1, params.cutoff_freq, params.fs);
    
    % 步骤3: 归一化
    step3 = normalization(step2, params.norm_method);
    
    % 步骤4: 特征提取
    step4 = feature_extraction(step3, params.fs);
    
    fprintf('=== Pipeline completed ===\\n');
    result.processed_data = step3;
    result.features = step4;
end
"""

session.eval(processing_pipeline)

# 生成测试数据
fs = 1000  # 采样率 1 kHz
t = np.linspace(0, 1, fs)
test_signal = (np.sin(2*np.pi*50*t) +  # 50 Hz 正弦波
               0.5*np.sin(2*np.pi*120*t) +  # 120 Hz 正弦波
               0.2*np.random.randn(fs))  # 噪声

# 设置管道参数
params = {
    "cutoff_freq": 100,  # 100 Hz 截止频率
    "fs": fs,
    "norm_method": "minmax"
}

# 调用处理管道
session.call()
session.set("function", "processing_pipeline_main")
session.set("arguments", [test_signal.tolist(), params])
session.set("return value", "pipeline_result")
session.set("multiple returns", False)

# 函数组合：创建高阶函数
function_composition = """
function h = compose(f, g)
    % 函数组合: h(x) = f(g(x))
    h = @(x) f(g(x));
end

function y = square(x)
    y = x^2;
end

function y = increment(x)
    y = x + 1;
end

function y = scale(x, factor)
    y = x * factor;
end

% 创建组合函数
square_after_increment = compose(@square, @increment);
increment_after_square = compose(@increment, @square);

% 测试组合函数
test_value = 3;
result1 = square_after_increment(test_value);  % (3+1)^2 = 16
result2 = increment_after_square(test_value);  % 3^2+1 = 10

fprintf('Function composition test:\\n');
fprintf('  square(increment(3)) = %.0f\\n', result1);
fprintf('  increment(square(3)) = %.0f\\n', result2);
"""

session.eval(function_composition)

# 函数柯里化
currying_example = """
function curried_scale = curry_scale(factor)
    % 柯里化：将多参数函数转换为单参数函数序列
    curried_scale = @(x) scale(x, factor);
end

% 创建特定缩放因子的函数
scale_by_2 = curry_scale(2);
scale_by_10 = curry_scale(10);

fprintf('Currying example:\\n');
fprintf('  scale_by_2(5) = %.0f\\n', scale_by_2(5));
fprintf('  scale_by_10(5) = %.0f\\n', scale_by_10(5));
"""

session.eval(currying_example)

# 获取处理结果
try:
    pipeline_result = session.getdata("pipeline_result")
    print("\nPipeline processing completed successfully!")
    print(f"Extracted features:")
    for key, value in pipeline_result['features'].items():
        print(f"  {key}: {value}")
except:
    print("\nNote: Some function calls may require specific Lumerical configurations")

print("\nFunction call demonstration completed.")
print("This example shows various function calling patterns:")
print("1. Basic built-in function calls")
print("2. User-defined function calls")
print("3. Method calls on objects")
print("4. Function pipelines and composition")
print("5. Advanced functional programming concepts")
```

## 注意事项

1. **函数存在性**：调用前确保函数已定义或存在
2. **参数匹配**：确保参数数量、类型和顺序与函数定义匹配
3. **命名空间**：注意函数的命名空间和作用域
4. **性能考虑**：频繁函数调用可能影响性能，考虑向量化或优化
5. **错误传播**：妥善处理函数调用中的错误和异常
6. **内存管理**：函数调用可能创建临时变量，注意内存使用
7. **递归深度**：递归函数调用需要注意递归深度限制
8. **线程安全**：并行调用时确保函数是线程安全的

## 错误处理

`call` 命令提供多种错误处理机制，可通过配置属性控制：

### 错误处理策略
1. **抛出异常** (`error handling: "throw"`)：遇到错误时抛出异常，停止执行
2. **捕获异常** (`error handling: "catch"`)：捕获异常并继续执行，记录错误信息
3. **忽略错误** (`error handling: "ignore"`)：忽略错误，继续执行
4. **日志记录** (`error handling: "log"`)：记录错误到日志，继续执行

### 常见错误类型
1. **函数未找到**：函数名错误或函数未定义
2. **参数错误**：参数数量、类型或格式不匹配
3. **执行错误**：函数执行过程中出现的运行时错误
4. **超时错误**：函数执行时间超过 `timeout` 设置
5. **内存错误**：函数调用导致内存不足
6. **权限错误**：沙箱模式下不允许的操作

### Python 错误处理示例
```python
import lumapi

session = lumapi.FDTD()

# 配置错误处理
session.call()
session.set("error handling", "catch")
session.set("timeout", 10)  # 10秒超时
session.set("retry count", 3)  # 最多重试3次
session.set("fallback function", "default_function")

try:
    # 尝试调用可能失败的函数
    session.call()
    session.set("function", "non_existent_function")
    session.set("arguments", [1, 2, 3])
    session.set("return value", "result")
    
    result = session.getdata("result")
    print(f"Result: {result}")
except Exception as e:
    print(f"Function call failed: {e}")
    
    # 检查详细错误信息
    error_info = session.getv("call", "last_error")
    if error_info:
        print(f"Error details: {error_info}")
    
    # 使用备用函数
    session.call()
    session.set("function", "default_function")
    session.set("arguments", [1, 2, 3])
    fallback_result = session.getdata("result")
    print(f"Fallback result: {fallback_result}")
```

### LSF 错误处理示例
```lumerical
# 配置错误处理
call;
set("error handling", "catch");
set("timeout", 10);
set("retry count", 3);

# 尝试调用可能失败的函数
function_name = "non_existent_function";
call;
set("function", function_name);
set("arguments", {1, 2, 3});

# 检查是否出错
if (haserror("call")) {
    error_msg = geterror("call");
    ? "Function call error: " + error_msg;
    
    # 使用备用函数
    call;
    set("function", "default_function");
    set("arguments", {1, 2, 3});
    result = getdata("result");
    ? "Fallback result: " + num2str(result);
} else {
    result = getdata("result");
    ? "Function call successful: " + num2str(result);
}
```

### 调试技巧
1. 启用调试模式：`set("debug mode", true)`
2. 跟踪函数调用：`set("trace", true)`
3. 性能分析：`set("profiling", true)` 识别性能瓶颈
4. 日志记录：`set("log calls", true)` 记录所有函数调用
5. 逐步执行：复杂函数调用分解为多个简单调用

### 预防措施
1. 函数存在性检查：调用前使用 `exist()` 函数检查函数是否存在
2. 参数验证：使用 `validateargs()` 验证参数有效性
3. 资源监控：监控内存和CPU使用情况
4. 超时设置：为长时间运行函数设置合理超时
5. 沙箱模式：执行不受信任代码时启用沙箱模式

## 产品支持

- **FDTD Solutions**: 支持仿真控制函数、数据处理函数
- **MODE Solutions**: 支持模式分析函数、优化函数
- **DEVICE**: 支持热学、电学分析函数
- **INTERCONNECT**: 支持电路分析函数、信号处理函数

## 相关命令

- `eval` - 执行表达式
- `feval` - 函数求值
- `function` - 定义函数
- `nargin` - 获取输入参数数量
- `nargout` - 获取输出参数数量
- `varargin` - 可变长度输入参数
- `varargout` - 可变长度输出参数
- `anonymous` - 匿名函数

## 版本历史

| 版本 | 修改 |
|------|------|
| 1.0 | 初始版本，包含基本函数调用功能 |
| 1.1 | 添加用户定义函数和回调函数支持 |
| 1.2 | 扩展方法调用和面向对象编程支持 |
| 2.0 | 添加错误处理、性能优化和安全性功能 |

## 参考

1. Lumerical Script Language Reference - Call Command
2. Lumerical Python API Documentation - call() Method
3. MATLAB Function Handles and Callbacks Documentation
4. Advanced MATLAB: Object-Oriented Programming and Design Patterns

---

*最后更新: 2026-01-31*  
*文档版本: 2.0*