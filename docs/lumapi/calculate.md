# calculate

## 概述

`calculate` 命令用于执行各种计算操作，包括数学运算、物理量计算、数据分析和结果处理。该命令是 Lumerical 脚本中的通用计算引擎，支持表达式求值、函数调用、单位转换等高级功能。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
calculate;
```

### Python API (Lumapi)
```python
session.calculate()
```

## 参数

`calculate` 命令没有直接参数，但需要通过后续的 `set` 命令配置计算表达式、变量和输出设置。

## 配置属性

执行计算后，可以使用 `set` 命令配置以下属性：

### 1. 基本计算设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `expression` | string | "" | 计算表达式 |
| `variables` | dict | {} | 变量字典（名称-值对） |
| `output` | string | "result" | 输出变量名称 |
| `evaluate` | bool | true | 是否立即求值 |
| `save result` | bool | true | 是否保存结果 |

### 2. 数学运算支持
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `operation` | string | "evaluate" | 运算类型："evaluate", "solve", "integrate", "differentiate", "optimize" |
| `precision` | int | 16 | 计算精度（有效数字） |
| `numeric` | bool | true | 是否数值计算（vs 符号计算） |
| `complex` | bool | false | 是否支持复数运算 |

### 3. 物理量计算
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `physical quantity` | bool | false | 是否物理量计算 |
| `units` | string | "" | 单位系统 |
| `unit conversion` | bool | true | 是否自动单位转换 |
| `dimensional analysis` | bool | false | 是否进行量纲分析 |

### 4. 方程求解
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `equation` | string | "" | 方程式 |
| `unknowns` | array | [] | 未知数列表 |
| `initial guess` | array | [] | 初始猜测值 |
| `solver` | string | "newton" | 求解器："newton", "fsolve", "lsq", "eigen" |
| `tolerance` | float | 1e-9 | 求解容差 |

### 5. 积分与微分
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `integrand` | string | "" | 被积函数 |
| `variable` | string | "x" | 积分/微分变量 |
| `limits` | vector | [0, 1] | 积分上下限 |
| `method` | string | "quad" | 积分方法："quad", "trapz", "simpson", "montecarlo" |
| `order` | int | 1 | 微分阶数 |

### 6. 优化计算
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `objective` | string | "" | 目标函数 |
| `constraints` | array | [] | 约束条件列表 |
| `algorithm` | string | "fmincon" | 优化算法 |
| `max iterations` | int | 1000 | 最大迭代次数 |
| `optimality tolerance` | float | 1e-6 | 最优性容差 |

### 7. 统计分析
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `data` | array | [] | 输入数据 |
| `statistic` | string | "mean" | 统计量："mean", "std", "var", "median", "mode" |
| `distribution` | string | "normal" | 概率分布 |
| `confidence level` | float | 0.95 | 置信水平 |
| `hypothesis test` | bool | false | 是否进行假设检验 |

### 8. 矩阵运算
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `matrix operation` | string | "multiply" | 矩阵运算："multiply", "invert", "transpose", "eigen", "svd" |
| `matrix A` | matrix | [] | 矩阵A |
| `matrix B` | matrix | [] | 矩阵B |
| `decomposition` | string | "none" | 矩阵分解："LU", "QR", "Cholesky", "SVD" |

### 9. 信号处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `signal` | array | [] | 输入信号 |
| `operation` | string | "fft" | 信号处理操作："fft", "filter", "convolve", "correlate" |
| `sampling rate` | float | 1 | 采样率 |
| `window function` | string | "hann" | 窗函数 |

### 10. 单位系统
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `input units` | dict | {} | 输入单位字典 |
| `output units` | dict | {} | 输出单位字典 |
| `unit system` | string | "SI" | 单位系统："SI", "cgs", "natural", "custom" |
| `auto convert` | bool | true | 是否自动转换单位 |

### 11. 错误处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `error handling` | string | "warn" | 错误处理："stop", "warn", "ignore" |
| `check validity` | bool | true | 是否检查计算有效性 |
| `validation rules` | array | [] | 验证规则列表 |
| `fallback value` | 任意 | NaN | 计算失败时的回退值 |

### 12. 性能优化
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parallel computing` | bool | false | 是否并行计算 |
| `cache results` | bool | true | 是否缓存结果 |
| `memory limit` | float | 1024 | 内存限制 (MB) |
| `timeout` | float | 60 | 超时时间 (秒) |

## 返回值

`calculate` 命令的执行结果存储在指定的输出变量中。返回值类型取决于计算类型和输入数据，可能包括：

- **标量值**：数值计算结果（整数、浮点数、复数）
- **向量/矩阵**：数组或矩阵运算结果
- **结构体**：包含多个字段的复合结果（如特征值分解结果）
- **物理量**：带单位的物理量结果（当启用物理量计算时）
- **错误代码**：计算失败时返回错误代码（取决于错误处理设置）

可以通过 `getdata` 命令获取计算结果，或通过 `set` 命令配置输出到指定变量。

## 使用示例

### 示例 1：基本数学计算

#### LSF 脚本
```lumerical
# 简单算术运算
calculate;
set("expression", "2 + 3 * 4");
set("output", "result1");
# 结果: result1 = 14

# 使用变量
a = 5.0;
b = 3.0;
c = 2.0;
calculate;
set("expression", "a^2 + b^2 - c^2");
set("variables", {"a": a, "b": b, "c": c});
set("output", "result2");
# 结果: result2 = 25 + 9 - 4 = 30

# 复数运算
calculate;
set("expression", "(3+4j) * exp(1j*pi/4)");
set("complex", true);
set("output", "complex_result");
# 结果: 复数计算

# 获取结果
result1 = getdata("result1");
result2 = getdata("result2");
complex_result = getdata("complex_result");

? "Result 1: " + num2str(result1);
? "Result 2: " + num2str(result2);
? "Complex result: " + num2str(complex_result);
```

#### Python API
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

# 简单算术运算
session.calculate()
session.set("expression", "2 + 3 * 4")
session.set("output", "result1")
# 结果: result1 = 14

# 使用变量
variables = {
    "a": 5.0,
    "b": 3.0,
    "c": 2.0
}
session.calculate()
session.set("expression", "a^2 + b^2 - c^2")
session.set("variables", variables)
session.set("output", "result2")
# 结果: result2 = 25 + 9 - 4 = 30

# 复数运算
session.calculate()
session.set("expression", "(3+4j) * exp(1j*pi/4)")
session.set("complex", True)
session.set("output", "complex_result")
# 结果: 复数计算

# 获取结果
result1 = session.getdata("result1")
result2 = session.getdata("result2")
complex_result = session.getdata("complex_result")

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Complex result: {complex_result}")
```

### 示例 2：物理量计算与单位转换
```python
import lumapi

session = lumapi.MODE()

# 定义物理量（带单位）
physical_vars = {
    "length": {"value": 1.0, "unit": "m"},
    "time": {"value": 2.0, "unit": "s"},
    "mass": {"value": 0.5, "unit": "kg"}
}

# 计算速度（自动单位转换）
session.calculate()
session.set("expression", "length / time")
session.set("variables", {
    "length": 100,  # 100 cm
    "time": 2       # 2 s
})
session.set("physical quantity", True)
session.set("input units", {"length": "cm", "time": "s"})
session.set("output units", {"result": "m/s"})
session.set("output", "velocity")
# 结果: velocity = 0.5 m/s (100 cm / 2 s = 0.5 m/s)

# 计算动能
session.calculate()
session.set("expression", "0.5 * mass * velocity^2")
session.set("variables", {
    "mass": 0.5,  # 0.5 kg
    "velocity": 10  # 10 m/s
})
session.set("physical quantity", True)
session.set("output units", {"result": "J"})
session.set("output", "kinetic_energy")
# 结果: kinetic_energy = 25 J

# 量纲分析
session.calculate()
session.set("expression", "force * distance / time")
session.set("variables", {
    "force": 10,  # 10 N
    "distance": 5, # 5 m
    "time": 2      # 2 s
})
session.set("physical quantity", True)
session.set("dimensional analysis", True)
session.set("output", "power")
# 结果: power = 25 W，同时验证量纲: N·m/s = W

# 单位系统转换
session.calculate()
session.set("expression", "energy")
session.set("variables", {"energy": 1.0})  # 1 J
session.set("physical quantity", True)
session.set("unit system", "cgs")  # 转换为CGS单位制
session.set("output", "energy_cgs")
# 结果: energy_cgs = 1e7 erg (1 J = 10^7 erg)

# 获取带单位的结果
velocity = session.getdata("velocity")
kinetic_energy = session.getdata("kinetic_energy")
power = session.getdata("power")
energy_cgs = session.getdata("energy_cgs")

print(f"Velocity: {velocity} m/s")
print(f"Kinetic energy: {kinetic_energy} J")
print(f"Power: {power} W")
print(f"Energy in CGS: {energy_cgs} erg")
```

### 示例 3：方程求解与优化
```python
import lumapi
import numpy as np

session = lumapi.DEVICE()

# 1. 非线性方程求解
# 求解: x^3 - 2x - 5 = 0
session.calculate()
session.set("operation", "solve")
session.set("equation", "x^3 - 2*x - 5 = 0")
session.set("unknowns", ["x"])
session.set("initial guess", [2.0])  # 初始猜测 x=2
session.set("solver", "newton")
session.set("tolerance", 1e-10)
session.set("output", "root")
# 结果: x ≈ 2.0945514815

# 2. 方程组求解
# 求解: 
#   x^2 + y^2 = 25
#   x - y = 1
session.calculate()
session.set("operation", "solve")
session.set("equation", ["x^2 + y^2 = 25", "x - y = 1"])
session.set("unknowns", ["x", "y"])
session.set("initial guess", [3.0, 2.0])
session.set("solver", "fsolve")
session.set("output", "solutions")
# 结果: x=4, y=3 或 x=-3, y=-4

# 3. 数值积分
# 计算 ∫₀¹ sin(x²) dx
session.calculate()
session.set("operation", "integrate")
session.set("integrand", "sin(x^2)")
session.set("variable", "x")
session.set("limits", [0, 1])
session.set("method", "quad")
session.set("precision", 12)
session.set("output", "integral_result")
# 结果: ≈ 0.310268301723

# 4. 数值微分
# 计算 f(x) = exp(-x²) 在 x=1 处的导数
session.calculate()
session.set("operation", "differentiate")
session.set("expression", "exp(-x^2)")
session.set("variable", "x")
session.set("point", 1.0)
session.set("order", 1)  # 一阶导数
session.set("output", "derivative")
# 结果: f'(1) ≈ -0.735758882343

# 5. 优化问题
# 最小化 f(x) = (x-3)^2 + sin(x) 在 [0, 5] 区间
session.calculate()
session.set("operation", "optimize")
session.set("objective", "(x-3)^2 + sin(x)")
session.set("constraints", ["x >= 0", "x <= 5"])
session.set("algorithm", "fmincon")
session.set("initial guess", [2.5])
session.set("optimality tolerance", 1e-8)
session.set("output", "optimum")
# 结果: x ≈ 2.819...

# 获取所有结果
root = session.getdata("root")
solutions = session.getdata("solutions")
integral = session.getdata("integral_result")
derivative = session.getdata("derivative")
optimum = session.getdata("optimum")

print(f"Root of x³ - 2x - 5 = 0: {root:.10f}")
print(f"Solutions to system: x={solutions[0]:.1f}, y={solutions[1]:.1f}")
print(f"Integral of sin(x²) from 0 to 1: {integral:.10f}")
print(f"Derivative of exp(-x²) at x=1: {derivative:.10f}")
print(f"Minimum of (x-3)² + sin(x): x={optimum:.6f}")
```

### 示例 4：高级矩阵与信号处理
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 1. 矩阵运算
# 创建两个矩阵
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# 矩阵乘法
session.calculate()
session.set("matrix operation", "multiply")
session.set("matrix A", A)
session.set("matrix B", B)
session.set("output", "matrix_product")
# 结果: A × B

# 矩阵求逆
session.calculate()
session.set("matrix operation", "invert")
session.set("matrix A", [[4, 7], [2, 6]])  # 可逆矩阵
session.set("output", "matrix_inverse")
# 结果: 逆矩阵

# 特征值分解
session.calculate()
session.set("matrix operation", "eigen")
session.set("matrix A", [[2, -1], [-1, 2]])
session.set("decomposition", "full")
session.set("output", "eigen_decomposition")
# 结果: 特征值和特征向量

# 2. 信号处理
# 生成测试信号
time = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*10*time) + 0.5*np.sin(2*np.pi*25*time) + 0.2*np.random.randn(1000)

# 傅里叶变换
session.calculate()
session.set("operation", "fft")
session.set("signal", signal.tolist())
session.set("sampling rate", 1000)  # 1 kHz
session.set("window function", "hann")
session.set("output", "spectrum")
# 结果: 频谱

# 滤波处理
session.calculate()
session.set("operation", "filter")
session.set("signal", signal.tolist())
session.set("filter type", "lowpass")
session.set("cutoff frequency", 15)  # 15 Hz
session.set("sampling rate", 1000)
session.set("output", "filtered_signal")
# 结果: 滤波后的信号

# 3. 统计分析
# 生成随机数据
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # 均值100, 标准差15

# 计算统计量
session.calculate()
session.set("data", data.tolist())
session.set("statistic", "all")  # 计算所有统计量
session.set("distribution", "normal")
session.set("confidence level", 0.95)
session.set("output", "statistics")
# 结果: 均值、标准差、置信区间等

# 4. 相关与卷积
signal1 = np.sin(2*np.pi*5*time)
signal2 = np.cos(2*np.pi*5*time)

# 互相关
session.calculate()
session.set("operation", "correlate")
session.set("signal", signal1.tolist())
session.set("reference", signal2.tolist())
session.set("output", "correlation")
# 结果: 互相关函数

# 卷积
session.calculate()
session.set("operation", "convolve")
session.set("signal", signal1.tolist())
kernel = np.exp(-time*10)  # 指数核
session.set("kernel", kernel.tolist())
session.set("output", "convolution")
# 结果: 卷积

# 获取结果
matrix_product = session.getdata("matrix_product")
matrix_inverse = session.getdata("matrix_inverse")
eigen_decomp = session.getdata("eigen_decomposition")
spectrum = session.getdata("spectrum")
filtered = session.getdata("filtered_signal")
stats = session.getdata("statistics")
correlation = session.getdata("correlation")
convolution = session.getdata("convolution")

print(f"Matrix product shape: {np.array(matrix_product).shape}")
print(f"Matrix inverse: {np.array(matrix_inverse)}")
print(f"Eigenvalues: {eigen_decomp['values']}")
print(f"Spectrum peak frequency: {np.argmax(np.abs(spectrum))} Hz")
print(f"Statistics - Mean: {stats['mean']:.2f}, Std: {stats['std']:.2f}")
print(f"Correlation max: {np.max(correlation):.3f}")
print(f"Convolution result length: {len(convolution)}")
```

## 注意事项

1. **表达式语法**：遵循 Lumerical 脚本语言的表达式语法
2. **变量作用域**：注意变量的定义域和生命周期
3. **数值稳定性**：复杂计算可能涉及数值稳定性问题
4. **单位一致性**：物理量计算时确保单位一致性
5. **内存使用**：大规模矩阵运算可能消耗大量内存
6. **计算精度**：根据需求设置适当的计算精度
7. **错误处理**：配置适当的错误处理策略
8. **性能优化**：复杂计算考虑使用并行计算或缓存

## 错误处理

`calculate` 命令支持多种错误处理机制，可以通过配置属性控制：

### 错误处理模式
1. **停止模式** (`error handling: "stop"`)：遇到错误立即停止计算，返回错误信息
2. **警告模式** (`error handling: "warn"`)：遇到错误发出警告，继续执行并返回 NaN 或回退值
3. **忽略模式** (`error handling: "ignore"`)：忽略错误，继续执行

### 常见错误及解决方案
1. **表达式语法错误**：检查表达式是否符合 Lumerical 语法规则
2. **未定义变量**：确保所有变量在计算前已正确定义
3. **数值计算错误**（除以零、溢出等）：检查输入数据的有效性
4. **内存不足**：减少计算规模或增加内存限制
5. **超时错误**：增加超时时间或优化计算算法

### Python 错误处理示例
```python
import lumapi

session = lumapi.FDTD()

try:
    session.calculate()
    session.set("expression", "1/0")  # 除以零错误
    session.set("error handling", "warn")
    session.set("fallback value", 0)
    session.set("output", "result")
    result = session.getdata("result")
    print(f"Result: {result}")
except Exception as e:
    print(f"Calculation error: {e}")
    # 检查错误详情
    error_info = session.getv("calculate", "error")
    if error_info:
        print(f"Error details: {error_info}")
```

### LSF 错误处理示例
```lumerical
# 设置错误处理模式
calculate;
set("error handling", "warn");
set("fallback value", 0);

# 可能出错的表达式
expression = "sqrt(-1)";  # 负数平方根
set("expression", expression);

# 执行计算
calculate;
result = getdata("result");
? "Result: " + num2str(result);

# 检查是否有警告
if (haswarning("calculate")) {
    ? "Warning: " + getwarning("calculate");
}
```

### 调试技巧
1. 启用详细日志：`set("verbose", true)`
2. 检查中间结果：使用 `set("save intermediate", true)`
3. 验证输入数据：使用 `set("check validity", true)`
4. 逐步执行：将复杂计算分解为多个简单步骤

## 相关命令

- `eval` - 表达式求值
- `solve` - 方程求解
- `integrate` - 数值积分
- `differentiate` - 数值微分
- `optimize` - 优化计算
- `fft` - 快速傅里叶变换
- `filter` - 信号滤波
- `correlate` - 相关分析

## 产品支持

- **FDTD Solutions**: 支持仿真结果的后处理计算
- **MODE Solutions**: 支持模式参数计算
- **DEVICE**: 支持热学、电学参数计算
- **INTERCONNECT**: 支持电路参数计算和信号处理

## 版本历史

| 版本 | 修改 |
|------|------|
| 1.0 | 初始版本，包含基本计算功能 |
| 1.1 | 添加物理量计算和单位转换支持 |
| 1.2 | 扩展矩阵运算和信号处理功能 |
| 2.0 | 统一错误处理接口，添加并行计算支持 |

## 参考

1. Lumerical Script Language Reference - Calculate Command
2. Lumerical Python API Documentation - calculate() Method
3. Numerical Recipes in C: The Art of Scientific Computing
4. Matrix Computations by Gene H. Golub and Charles F. Van Loan

---

*最后更新: 2026-01-31*  
*文档版本: 2.0*