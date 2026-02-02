# Lumapi Python API 使用原则

## 概述

Lumapi 是 Ansys Lumerical 提供的 Python 接口，允许用户通过 Python 脚本调用 Lumerical 软件（如 FDTD Solutions, MODE Solutions, DEVICE 等）的功能。Lumapi 将 Lumerical 脚本语言（LSF）命令映射为 Python 方法，提供了在 Python 环境中控制仿真、设置参数、运行分析和处理结果的能力。

## 核心原则

### 1. 命令映射原则

Lumerical 脚本语言的每个命令都对应一个 Python 方法。映射规则如下：

- **基本映射**: LSF 命令 `commandname` 对应 Python 方法 `lumapi.commandname()`
- **参数传递**: LSF 参数通过 Python 函数参数传递
- **返回值**: LSF 命令的返回值成为 Python 方法的返回值

**示例**:
```python
# LSF: addfdtd;
# Python:
import lumapi
fdtd = lumapi.FDTD()
fdtd.addfdtd()

# LSF: set("x", 0);
# Python:
fdtd.set("x", 0)

# LSF: result = getresult("FDTD", "transmission");
# Python:
result = fdtd.getresult("FDTD", "transmission")
```

### 2. 对象句柄原则

在 Lumapi 中，仿真对象通过句柄进行管理：

- **会话对象**: `lumapi.FDTD()`, `lumapi.MODE()`, `lumapi.DEVICE()` 创建仿真会话
- **对象引用**: 大多数命令在特定对象上下文中执行
- **方法链**: 支持方法链式调用，提高代码可读性

**示例**:
```python
import lumapi

# 创建 FDTD 会话
fdtd = lumapi.FDTD()

# 链式调用设置仿真参数
fdtd.addfdtd() \
    .set("x", 0) \
    .set("y", 0) \
    .set("z", 0) \
    .set("x span", 2e-6) \
    .set("y span", 2e-6) \
    .set("z span", 2e-6)
```

### 3. 数据类型转换原则

Python 和 Lumerical 之间的数据类型自动转换：

| Python 类型 | Lumerical 类型 | 说明 |
|------------|----------------|------|
| `int`, `float` | 数值 | 自动转换 |
| `str` | 字符串 | 自动转换 |
| `list`, `tuple` | 数组 | 转换为行向量 |
| `numpy.ndarray` | 矩阵 | 保持形状和数据类型 |
| `bool` | 布尔值 | `True` → `1`, `False` → `0` |
| `complex` | 复数 | 支持实部和虚部 |

**示例**:
```python
import numpy as np

# Python 列表自动转换为 Lumerical 数组
points = [0, 1e-6, 2e-6, 3e-6]
fdtd.set("points", points)

# NumPy 数组保持形状
mesh = np.linspace(0, 1e-6, 100)
fdtd.set("mesh", mesh)

# 复数参数
fdtd.set("index", 3.5 + 0.1j)
```

### 4. 错误处理原则

Lumapi 使用异常机制处理错误：

- **命令错误**: 无效命令或参数会抛出 `Exception`
- **语法检查**: 部分错误在命令执行时检查，部分在仿真运行时检查
- **错误消息**: 错误信息来自 Lumerical 引擎，包含具体错误位置和原因

**示例**:
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 无效命令会抛出异常
    fdtd.invalidcommand()
except Exception as e:
    print(f"命令错误: {e}")

try:
    # 无效参数会抛出异常
    fdtd.addfdtd()
    fdtd.set("invalid_property", 0)
except Exception as e:
    print(f"参数错误: {e}")
```

### 5. 性能优化原则

- **批量操作**: 尽量减少 Python 和 Lumerical 之间的往返调用
- **向量化**: 使用 NumPy 数组进行批量数据操作
- **缓存结果**: 重复使用的计算结果应缓存到 Python 变量中
- **内存管理**: 及时清理不再需要的大型数据数组

**示例**:
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 不推荐：多次单独设置
# fdtd.set("x", 0)
# fdtd.set("y", 0)
# fdtd.set("z", 0)

# 推荐：批量设置（如果支持）
fdtd.setmultiple([
    ("x", 0),
    ("y", 0),
    ("z", 0)
])

# 或者使用字典参数（如果命令支持）
fdtd.addfdtd(
    x=0,
    y=0,
    z=0,
    x_span=2e-6,
    y_span=2e-6,
    z_span=2e-6
)
```

### 6. 脚本与 Python 混合原则

可以在 LSF 脚本中嵌入 Python 代码，或在 Python 中执行 LSF 脚本字符串：

- **`eval` 方法**: 执行 LSF 脚本字符串
- **`run` 方法**: 执行 LSF 脚本文件
- **混合编程**: 复杂逻辑用 Python，简单操作用 LSF

**示例**:
```python
import lumapi

fdtd = lumapi.FDTD()

# 执行 LSF 脚本字符串
lsf_script = """
addfdtd;
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 2e-6);
set("y span", 2e-6);
set("z span", 2e-6);
"""
fdtd.eval(lsf_script)

# 执行 LSF 脚本文件
fdtd.run("simulation_setup.lsf")
```

## 常用模式

### 模式 1: 创建-配置-运行-分析
```python
import lumapi
import numpy as np

def run_simulation():
    # 1. 创建会话
    fdtd = lumapi.FDTD()
    
    # 2. 配置仿真
    fdtd.addfdtd()
    fdtd.set("x span", 2e-6)
    fdtd.set("y span", 2e-6)
    fdtd.set("z span", 2e-6)
    fdtd.set("mesh accuracy", 2)
    
    # 3. 添加结构
    fdtd.addrect()
    fdtd.set("name", "waveguide")
    fdtd.set("material", "Si (Silicon) - Palik")
    fdtd.set("x span", 0.5e-6)
    fdtd.set("y span", 0.22e-6)
    
    # 4. 添加光源
    fdtd.addmode()
    fdtd.set("injection axis", "x-axis")
    fdtd.set("wavelength start", 1.5e-6)
    fdtd.set("wavelength stop", 1.6e-6)
    
    # 5. 添加监视器
    fdtd.addpower()
    fdtd.set("name", "transmission")
    fdtd.set("monitor type", "2D X-normal")
    
    # 6. 运行仿真
    fdtd.run()
    
    # 7. 获取结果
    transmission = fdtd.getresult("transmission", "T")
    
    # 8. 清理
    fdtd.close()
    
    return transmission
```

### 模式 2: 参数扫描
```python
import lumapi
import numpy as np

def parameter_sweep():
    fdtd = lumapi.FDTD()
    results = []
    
    widths = np.linspace(0.4e-6, 0.6e-6, 5)
    
    for width in widths:
        fdtd.newproject()  # 开始新仿真
        
        # 基本设置
        fdtd.addfdtd()
        fdtd.set("x span", 2e-6)
        
        # 扫描参数
        fdtd.addrect()
        fdtd.set("x span", width)
        fdtd.set("y span", 0.22e-6)
        
        # 运行
        fdtd.run()
        
        # 获取结果
        T = fdtd.getresult("transmission", "T")
        results.append((width, T))
    
    fdtd.close()
    return results
```

### 模式 3: 结果后处理
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

def analyze_results():
    fdtd = lumapi.FDTD()
    
    # ... 运行仿真 ...
    
    # 获取多个结果
    T = fdtd.getresult("transmission", "T")
    R = fdtd.getresult("reflection", "R")
    wavelengths = T["lambda"]  # 获取波长数据
    
    # 计算性能指标
    avg_transmission = np.mean(T["T"])
    max_transmission = np.max(T["T"])
    bandwidth = np.trapz(T["T"], wavelengths)
    
    # 可视化
    plt.figure()
    plt.plot(wavelengths * 1e6, T["T"], label="Transmission")
    plt.plot(wavelengths * 1e6, R["R"], label="Reflection")
    plt.xlabel("Wavelength (μm)")
    plt.ylabel("Response")
    plt.legend()
    plt.grid(True)
    
    fdtd.close()
    
    return {
        "wavelengths": wavelengths,
        "transmission": T["T"],
        "reflection": R["R"],
        "avg_transmission": avg_transmission,
        "max_transmission": max_transmission,
        "bandwidth": bandwidth
    }
```

## 最佳实践

### 1. 代码组织
```python
# 推荐结构
class FDTDSimulation:
    def __init__(self):
        self.fdtd = lumapi.FDTD()
        self.results = {}
    
    def setup_geometry(self):
        """设置几何结构"""
        pass
    
    def setup_sources(self):
        """设置光源"""
        pass
    
    def setup_monitors(self):
        """设置监视器"""
        pass
    
    def run(self):
        """运行仿真"""
        pass
    
    def analyze(self):
        """分析结果"""
        pass
    
    def close(self):
        """清理资源"""
        self.fdtd.close()
```

### 2. 错误恢复
```python
def robust_simulation():
    fdtd = lumapi.FDTD()
    
    try:
        # 仿真设置
        fdtd.addfdtd()
        # ...
        
        # 运行仿真
        fdtd.run()
        
        # 获取结果
        results = fdtd.getresult("monitor", "data")
        
    except Exception as e:
        print(f"仿真失败: {e}")
        # 保存当前状态以供调试
        fdtd.save("error_state.fsp")
        raise
    
    finally:
        # 确保资源被释放
        if 'fdtd' in locals():
            fdtd.close()
```

### 3. 性能监控
```python
import time
import psutil  # 需要安装 psutil

def monitored_simulation():
    start_time = time.time()
    
    fdtd = lumapi.FDTD()
    
    # 监控内存使用
    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    # 运行仿真
    fdtd.run()
    
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    elapsed_time = time.time() - start_time
    
    print(f"仿真时间: {elapsed_time:.2f} 秒")
    print(f"内存使用: {final_memory - initial_memory:.2f} MB")
    
    fdtd.close()
```

## 常见问题与解决方案

### 问题 1: 命令不存在
**症状**: `AttributeError: 'FDTD' object has no attribute 'commandname'`
**原因**: 命令拼写错误或该版本不支持
**解决**: 检查命令拼写，查阅对应版本的文档

### 问题 2: 参数类型错误
**症状**: `Exception: Invalid parameter type`
**原因**: 参数类型不匹配
**解决**: 检查参数类型，使用正确的数据类型

### 问题 3: 内存不足
**症状**: 仿真崩溃或无响应
**原因**: 网格太密或仿真区域太大
**解决**: 减小网格密度，使用对称边界条件，增加系统内存

### 问题 4: 结果不一致
**症状**: 相同设置下结果不同
**原因**: 随机数种子未设置，网格设置不同
**解决**: 设置随机数种子，确保网格设置一致

## 扩展资源

1. **官方文档**: https://optics.ansys.com/hc/en-us/articles/360041579954
2. **脚本命令列表**: https://optics.ansys.com/hc/en-us/articles/360034923553
3. **示例库**: Ansys Optics 示例和教程
4. **社区论坛**: Ansys Learning Forum

## 更新记录

| 版本 | 日期 | 修改内容 |
|------|------|----------|
| 1.0 | 2025-01-30 | 初始版本，基于 Lumapi 通用原则 |

---

*注意: 本文档基于 Lumapi 通用使用原则编写，具体命令和参数请参考对应版本的官方文档。*