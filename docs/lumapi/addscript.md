# addscript

## 概述

`addscript` 命令用于在仿真中添加脚本对象。脚本对象允许用户嵌入自定义脚本代码，在仿真过程中执行特定操作，如参数扫描、结果处理、实时监控、自动化控制等。该命令支持多种脚本语言，包括 Lumerical 脚本语言 (LSF)、Python、MATLAB 等。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addscript;
```

### Python API (Lumapi)
```python
session.addscript()
```

## 参数

`addscript` 命令没有直接参数，但需要通过后续的 `set` 命令配置脚本类型、内容和执行条件。

## 配置属性

添加脚本对象后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "script" | 脚本对象名称 |
| `enabled` | bool | true | 是否启用脚本 |
| `script type` | string | "lsf" | 脚本类型："lsf", "python", "matlab", "javascript", "custom" |
| `execution mode` | string | "manual" | 执行模式："manual", "auto", "on event", "periodic" |

### 2. 脚本内容
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `script` | string | "" | 脚本代码内容 |
| `script file` | string | "" | 脚本文件路径（替代直接代码） |
| `encoding` | string | "utf-8" | 脚本编码 |
| `line ending` | string | "unix" | 行结束符："unix", "windows", "mac" |
| `indentation` | int | 4 | 缩进空格数 |

### 3. 执行控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `trigger event` | string | "simulation start" | 触发事件："simulation start", "simulation end", "iteration complete", "parameter change" |
| `execution order` | int | 0 | 执行顺序（数值越小越先执行） |
| `execution count` | int | 1 | 执行次数（0 表示无限） |
| `execution interval` | float | 1 | 执行间隔（秒，仅限 periodic 模式） |
| `timeout` | float | 60 | 超时时间（秒） |
| `run in background` | bool | false | 是否在后台运行 |

### 4. 输入输出
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `input variables` | array | [] | 输入变量列表 |
| `output variables` | array | [] | 输出变量列表 |
| `input data` | 任意 | null | 输入数据 |
| `output data` | 任意 | null | 输出数据（只读） |
| `save results` | bool | true | 是否保存结果 |
| `result format` | string | "mat" | 结果格式："mat", "txt", "csv", "json" |

### 5. 错误处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `error handling` | string | "stop" | 错误处理："stop", "continue", "ignore", "log" |
| `max errors` | int | 10 | 最大错误数（超过则停止） |
| `error log file` | string | "" | 错误日志文件路径 |
| `warning level` | string | "normal" | 警告级别："none", "normal", "strict" |

### 6. 调试与监控
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `debug mode` | bool | false | 是否启用调试模式 |
| `breakpoints` | array | [] | 断点行号列表 |
| `monitor variables` | array | [] | 监视变量列表 |
| `log level` | string | "info" | 日志级别："debug", "info", "warning", "error" |
| `log file` | string | "" | 日志文件路径 |
| `progress reporting` | bool | true | 是否报告进度 |

### 7. 资源控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `memory limit` | float | 1024 | 内存限制 (MB) |
| `cpu cores` | int | 1 | 使用的 CPU 核心数 |
| `priority` | string | "normal" | 优先级："low", "normal", "high" |
| `parallel execution` | bool | false | 是否并行执行 |
| `gpu acceleration` | bool | false | 是否使用 GPU 加速 |

### 8. 安全设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `sandbox mode` | bool | true | 是否启用沙箱模式（限制文件系统访问） |
| `allowed operations` | array | ["read", "write", "execute"] | 允许的操作列表 |
| `allowed paths` | array | [] | 允许访问的路径列表 |
| `security level` | string | "medium" | 安全级别："low", "medium", "high" |
| `signature verification` | bool | false | 是否验证脚本签名 |

### 9. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `custom interpreter` | string | "" | 自定义解释器路径 |
| `environment variables` | dict | {} | 环境变量字典 |
| `working directory` | string | "" | 工作目录 |
| `import paths` | array | [] | 导入路径列表 |
 | `module dependencies` | array | [] | 模块依赖列表 |

## 返回值

`addscript` 命令没有直接的返回值。成功执行后，会在仿真中添加一个脚本对象，该对象可以通过 `set` 命令配置脚本内容、执行条件和其他属性。

## 示例

### 示例 1：简单参数扫描脚本

#### LSF 脚本
```lumerical
// 简单参数扫描脚本示例
addscript;
set("name", "parameter_sweep");
set("script type", "python");
set("script file", "parameter_sweep.py"); // 从文件加载脚本
set("execution mode", "auto");
set("trigger event", "simulation start");
set("execution order", 10);
set("save results", true);
set("result format", "csv");
```

#### Python API
```python
import lumapi

session = lumapi.MODE()

# 添加实时监控脚本
session.addscript()
session.set("name", "real_time_monitor")
session.set("script type", "lsf")

# LSF 脚本内容
lsf_script = """
# 实时监控脚本
monitor_interval = 0.5;  # 每 0.5 秒检查一次
max_iterations = 1000;

for (i = 1:max_iterations) {
    # 检查收敛状态
    converged = getsweepdata("sweep", "converged");
    
    if (converged) {
        # 收敛后保存数据
        T = transmission("output");
        save("convergence_data.mat", T);
        print("Simulation converged at iteration " + num2str(i));
        break;
    }
    
    # 获取当前场分布
    E = getelectric("field_monitor");
    
    # 计算场强最大值
    maxE = max(abs(E));
    
    # 更新监控图
    plot(maxE, "b-", "LineWidth", 2);
    xlabel("Iteration");
    ylabel("Max Electric Field (V/m)");
    title("Convergence Monitor");
    refresh;
    
    # 等待
    sleep(monitor_interval);
}

if (!converged) {
    warning("Simulation did not converge within " + num2str(max_iterations) + " iterations");
}
"""

session.set("script", lsf_script)

# 配置执行设置
session.set("execution mode", "periodic")
session.set("execution interval", 0.5)  # 每 0.5 秒执行一次
session.set("run in background", True)
session.set("log level", "info")
session.set("monitor variables", ["converged", "electric_field"])
```

### 示例 3：结果后处理脚本
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加结果后处理脚本
session.addscript()
session.set("name", "post_processing")
session.set("script type", "python")

# Python 后处理脚本
post_script = """
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 获取原始数据
s_params = session.getresult("s_matrix", "S")
frequencies = s_params["f"]

# 计算幅度和相位
S21_mag = 20 * np.log10(np.abs(s_params["S"][1, 0, :]))
S21_phase = np.angle(s_params["S"][1, 0, :])

# 平滑处理
window_size = 11
S21_mag_smooth = signal.savgol_filter(S21_mag, window_size, 3)

# 查找 3dB 带宽
max_mag = np.max(S21_mag_smooth)
threshold = max_mag - 3
above_threshold = S21_mag_smooth > threshold

if np.any(above_threshold):
    idx = np.where(above_threshold)[0]
    f_low = frequencies[idx[0]]
    f_high = frequencies[idx[-1]]
    bandwidth = f_high - f_low
    center_freq = (f_low + f_high) / 2
    
    print(f"3dB Bandwidth: {bandwidth/1e9:.2f} GHz")
    print(f"Center Frequency: {center_freq/1e9:.2f} GHz")
    print(f"Low Frequency: {f_low/1e9:.2f} GHz")
    print(f"High Frequency: {f_high/1e9:.2f} GHz")
else:
    print("No 3dB bandwidth found")

# 创建图形
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(frequencies/1e9, S21_mag, 'b-', alpha=0.5, label='Raw')
ax1.plot(frequencies/1e9, S21_mag_smooth, 'r-', linewidth=2, label='Smoothed')
ax1.axhline(y=threshold, color='g', linestyle='--', label='3dB threshold')
ax1.set_xlabel('Frequency (GHz)')
ax1.set_ylabel('|S21| (dB)')
ax1.set_title('Transmission Response')
ax1.legend()
ax1.grid(True)

ax2.plot(frequencies/1e9, S21_phase, 'b-')
ax2.set_xlabel('Frequency (GHz)')
ax2.set_ylabel('Phase (rad)')
ax2.set_title('Phase Response')
ax2.grid(True)

plt.tight_layout()
plt.savefig('post_processing_results.png', dpi=300)
plt.close()

# 保存处理后的数据
results = {
    'frequencies': frequencies,
    'S21_magnitude': S21_mag,
    'S21_magnitude_smooth': S21_mag_smooth,
    'S21_phase': S21_phase,
    'bandwidth_3dB': bandwidth if 'bandwidth' in locals() else None,
    'center_frequency': center_freq if 'center_freq' in locals() else None
}

np.savez('processed_results.npz', **results)
"""

session.set("script", post_script)

# 配置执行设置
session.set("execution mode", "on event")
session.set("trigger event", "simulation end")
session.set("execution order", 100)  # 最后执行
session.set("save results", True)
session.set("result format", "png,npz")
session.set("output variables", ["bandwidth_3dB", "center_frequency"])
```

### 示例 4：自动化优化脚本
```python
import lumapi

session = lumapi.DEVICE()

# 添加优化脚本
session.addscript()
session.set("name", "genetic_optimization")
session.set("script type", "python")

# 遗传优化算法脚本
optimization_script = """
import numpy as np
import random

# 优化参数定义
params = {
    'width': {'min': 0.2e-6, 'max': 1.0e-6, 'current': 0.5e-6},
    'height': {'min': 0.2e-6, 'max': 0.5e-6, 'current': 0.22e-6},
    'length': {'min': 5e-6, 'max': 50e-6, 'current': 10e-6}
}

# 遗传算法参数
population_size = 20
generations = 50
mutation_rate = 0.1
crossover_rate = 0.7
elite_size = 2

# 初始化种群
def initialize_population():
    population = []
    for _ in range(population_size):
        individual = {}
        for param, bounds in params.items():
            individual[param] = random.uniform(bounds['min'], bounds['max'])
        population.append(individual)
    return population

# 评估适应度（目标：最小化热阻）
def evaluate_fitness(individual):
    # 更新几何参数
    for param, value in individual.items():
        session.setnamed("heater", param, value)
    
    # 运行热仿真
    session.runthermal()
    
    # 获取热阻
    thermal_resistance = session.getresult("thermal", "R_th")
    
    # 目标：最小化热阻
    fitness = 1.0 / (thermal_resistance + 1e-12)
    return fitness

# 选择操作（轮盘赌选择）
def select_parents(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f/total_fitness for f in fitness_values]
    
    parents = []
    for _ in range(2):
        r = random.random()
        cumulative = 0
        for i, prob in enumerate(probabilities):
            cumulative += prob
            if r <= cumulative:
                parents.append(population[i])
                break
    return parents

# 交叉操作
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1.copy()
    
    child = {}
    for param in params.keys():
        alpha = random.random()
        child[param] = alpha * parent1[param] + (1-alpha) * parent2[param]
    return child

# 变异操作
def mutate(individual):
    mutated = individual.copy()
    for param in params.keys():
        if random.random() < mutation_rate:
            # 高斯变异
            bounds = params[param]
            std = (bounds['max'] - bounds['min']) * 0.1
            mutated[param] += random.gauss(0, std)
            # 边界检查
            mutated[param] = max(bounds['min'], min(bounds['max'], mutated[param]))
    return mutated

# 主优化循环
print("Starting genetic optimization...")
population = initialize_population()
best_individual = None
best_fitness = -np.inf

for gen in range(generations):
    # 评估种群
    fitness_values = []
    for individual in population:
        fitness = evaluate_fitness(individual)
        fitness_values.append(fitness)
    
    # 更新最佳个体
    max_fitness = max(fitness_values)
    if max_fitness > best_fitness:
        best_fitness = max_fitness
        best_idx = fitness_values.index(max_fitness)
        best_individual = population[best_idx].copy()
    
    # 选择精英
    elite_indices = np.argsort(fitness_values)[-elite_size:]
    elites = [population[i].copy() for i in elite_indices]
    
    # 生成新种群
    new_population = elites.copy()
    
    while len(new_population) < population_size:
        # 选择父母
        parent_indices = random.sample(range(len(population)), 2)
        parent1 = population[parent_indices[0]]
        parent2 = population[parent_indices[1]]
        
        # 交叉
        child = crossover(parent1, parent2)
        
        # 变异
        child = mutate(child)
        
        new_population.append(child)
    
    population = new_population
    
    # 报告进度
    print(f"Generation {gen+1}/{generations}: Best fitness = {best_fitness:.6f}")
    if best_individual:
        print(f"  Best params: {best_individual}")

print("Optimization completed!")
print(f"Best thermal resistance: {1.0/best_fitness:.6f} K/W")
print(f"Optimal parameters: {best_individual}")

# 应用最优参数
if best_individual:
    for param, value in best_individual.items():
        session.setnamed("heater", param, value)
"""

session.set("script", optimization_script)

# 配置执行设置
session.set("execution mode", "manual")  # 手动触发
session.set("timeout", 3600)  # 1小时超时
session.set("memory limit", 4096)  # 4GB 内存
session.set("cpu cores", 4)  # 使用 4 个 CPU 核心
session.set("log level", "debug")
session.set("progress reporting", True)
```

## 注意事项

1. **脚本安全**：谨慎执行来自不可信来源的脚本，建议启用沙箱模式
2. **性能影响**：复杂脚本可能显著影响仿真性能，合理设置执行频率
3. **错误处理**：配置适当的错误处理策略，避免脚本错误导致仿真失败
4. **资源管理**：为脚本分配适当的计算资源，避免资源冲突
5. **依赖管理**：确保脚本所需的模块和库已正确安装
6. **调试技巧**：使用调试模式和断点功能逐步排查脚本问题
7. **版本兼容性**：注意脚本语言版本与 Lumerical 版本的兼容性
8. **数据一致性**：确保脚本输入输出数据格式与预期一致

## 错误处理

### 常见错误
1. **脚本语法错误**
   - 错误信息：`Script syntax error`
   - 解决方案：检查脚本语法，使用调试模式

2. **超时错误**
   - 错误信息：`Script execution timeout`
   - 解决方案：增加超时时间或优化脚本性能

3. **内存不足**
   - 错误信息：`Insufficient memory`
   - 解决方案：增加内存限制或优化脚本内存使用

4. **模块未找到**
   - 错误信息：`Module not found`
   - 解决方案：安装所需模块或添加导入路径

5. **安全限制**
   - 错误信息：`Security violation`
   - 解决方案：调整安全设置或启用沙箱模式

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加脚本对象
    fdtd.addscript()
    fdtd.set("name", "test_script")
    fdtd.set("script type", "python")
    
    # 配置脚本内容（包含潜在错误）
    fdtd.set("script", "print('Hello World')")
    
    # 设置执行模式
    fdtd.set("execution mode", "auto")
    
except lumapi.LumApiError as e:
    print(f"脚本创建失败: {e}")
    
    # 检查具体错误类型
    if "syntax" in str(e).lower():
        print("错误: 脚本语法错误")
    elif "timeout" in str(e).lower():
        print("错误: 脚本执行超时")
    elif "memory" in str(e).lower():
        print("错误: 内存不足")
    elif "security" in str(e).lower():
        print("错误: 安全限制")
    elif "module" in str(e).lower():
        print("错误: 模块未找到")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持 LSF、Python 脚本，用于参数扫描、结果处理
- **MODE Solutions**: 支持 LSF、Python 脚本，用于模式分析、优化
- **DEVICE**: 支持 Python 脚本，用于热学、电学优化
- **INTERCONNECT**: 支持 LSF、Python 脚本，用于电路分析、系统优化

## 相关命令

- `addcustom` - 添加自定义监视器
- `addproperty` - 添加自定义属性
- `set` - 设置脚本属性
- `runscript` - 运行脚本
- `eval` - 评估表达式
- `exec` - 执行命令

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 Python 脚本支持 |
| Lumerical 2019a | 增强安全设置和沙箱模式 |
| Lumerical 2018a | 新增脚本对象功能 |

## 参考

1. Lumerical 脚本编程指南
2. Lumerical Python API 文档
3. Python 官方文档

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*