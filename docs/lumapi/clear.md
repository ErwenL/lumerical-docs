# `clear` - 清除变量

## 概述

`clear` 命令用于从 Lumerical 脚本工作空间中移除变量。它可以清除单个变量、多个变量或所有变量，帮助管理内存使用、避免命名冲突，并在调试或重复执行脚本时提供干净的工作空间。

该命令类似于 MATLAB 或 Python 中的 `clear` 命令，是脚本开发和调试过程中的重要工具。

## 语法

### LSF 语法
```lumerical
clear;                    # 清除所有变量
clear(var1);              # 清除指定变量
clear(var1, var2, ...);   # 清除多个变量
clear("var1", "var2");    # 使用字符串参数清除变量
```

### Python API
```python
session.clear()                     # 清除所有变量
session.clear(var1)                 # 清除指定变量
session.clear(var1, var2, ...)      # 清除多个变量
session.clear("var1", "var2")       # 使用字符串参数清除变量
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `variable` | string 或 variable | 要清除的变量名称。可以是变量名本身或包含变量名的字符串。 | 可选 |

*注意：如果不提供任何参数，`clear` 将清除所有变量。*

## 配置属性

`clear` 命令没有可配置属性。

## 返回值

`clear` 命令没有返回值。成功执行后，指定的变量将从工作空间中移除。如果命令失败（例如尝试清除不存在的变量），Lumerical 可能会抛出错误或静默忽略。

在 Python API 中，`session.clear()` 通常返回 `None`。成功清除不返回任何值，失败时可能抛出异常或返回错误代码。

## 错误处理

### 常见错误

1. **变量不存在错误**
   ```python
   # 错误：变量 "nonexistent" 不存在
   fdtd.clear("nonexistent")
   ```
   解决方案：使用 `?all` 或 `exist` 命令先检查变量是否存在，或使用安全清除模式。

2. **系统变量保护错误**
   ```python
   # 错误：尝试清除受保护的系统变量
   fdtd.clear("_system_var")
   ```
   解决方案：避免清除以下划线开头的变量，这些通常是系统变量。

3. **内存释放错误**
   ```python
   # 错误：清除变量时内存释放失败
   fdtd.clear("large_array")
   ```
   解决方案：尝试分块清除大型变量，或使用 `purge` 命令彻底清理内存。

4. **语法错误**
   ```python
   # 错误：参数格式不正确
   fdtd.clear(123)  # 参数必须是字符串或变量名
   ```
   解决方案：确保参数是字符串或有效的变量名。

### Python 错误处理示例
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 创建一些变量
    fdtd.eval("x = 10;")
    fdtd.eval("y = 20;")
    
    # 成功清除
    fdtd.clear("x")
    print("变量 x 清除成功")
    
    # 清除不存在的变量（可能静默失败或抛出异常）
    fdtd.clear("nonexistent")
    
    # 清除所有变量
    fdtd.clear()
    print("所有变量清除成功")
    
except lumapi.LumApiError as e:
    error_str = str(e).lower()
    
    if "variable" in error_str and "not found" in error_str:
        print("错误: 变量不存在")
    elif "protected" in error_str or "system" in error_str:
        print("错误: 无法清除受保护的系统变量")
    elif "memory" in error_str:
        print("错误: 内存释放失败")
    elif "syntax" in error_str or "argument" in error_str:
        print("错误: 参数语法错误")
    else:
        print(f"Lumerical API 错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 使用示例

### 示例 1：清除所有变量
```python
import lumapi
import numpy as np

# 创建会话
fdtd = lumapi.FDTD()

# 创建一些变量
fdtd.eval("x = 10;")
fdtd.eval("y = 20;")
fdtd.eval("data = matrix(100, 100);")  # 创建大型矩阵

# 显示当前变量
print("清除前变量:")
fdtd.eval("?all;")  # 列出所有变量

# 清除所有变量
fdtd.clear()

print("\n清除后变量:")
fdtd.eval("?all;")  # 变量列表应为空

# 验证变量已被清除
try:
    value = fdtd.get("x")
    print(f"变量 x 仍然存在: {value}")
except:
    print("变量 x 已被成功清除")
```

### 示例 2：清除特定变量
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建多个变量
fdtd.eval("temp_data = linspace(0, 10, 1000);")
fdtd.eval("simulation_result = matrix(50, 50);")
fdtd.eval("config = struct('wavelength', 1.55, 'power', 1.0);")
fdtd.eval("intermediate_calc = 42;")

print("初始变量:")
fdtd.eval("?all;")

# 清除特定变量
fdtd.clear("temp_data")  # 清除临时数据
print("\n清除 temp_data 后:")
fdtd.eval("?all;")

# 清除多个变量
fdtd.clear("intermediate_calc", "config")
print("\n清除多个变量后:")
fdtd.eval("?all;")

# 使用变量引用（而不是字符串）
fdtd.eval("to_delete = 'simulation_result';")
fdtd.clear("to_delete")  # 清除 simulation_result
print("\n清除 simulation_result 后:")
fdtd.eval("?all;")
```

### 示例 3：在循环中管理内存
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 模拟参数扫描，每次迭代生成大量数据
wavelengths = np.linspace(1.3, 1.6, 10)
results = []

for i, wl in enumerate(wavelengths):
    print(f"迭代 {i+1}/{len(wavelengths)}: λ = {wl:.3f} μm")
    
    # 设置仿真参数
    fdtd.eval(f"wavelength = {wl};")
    fdtd.eval("source_wavelength = wavelength;")
    
    # 运行仿真（模拟）
    fdtd.eval(f"sim_data = matrix(1000, 1000) * {wl};")  # 模拟大型数据矩阵
    
    # 提取需要的结果
    fdtd.eval("transmission = sim_data(500, 500);")  # 示例：提取中心点值
    T = fdtd.get("transmission")
    results.append(T)
    
    # 清除临时变量以释放内存
    fdtd.clear("sim_data", "transmission")
    
    # 保留必要的变量
    # wavelength 和 source_wavelength 保留用于下一次迭代
    
    # 显示内存使用情况
    fdtd.eval("?memory;")

print(f"\n完成扫描。结果: {results}")

# 最终清理
fdtd.clear()
```

### 示例 4：防止变量冲突
```python
import lumapi

def run_simulation_1(fdtd):
    """第一个仿真函数"""
    fdtd.eval("x = 1;")
    fdtd.eval("y = 2;")
    fdtd.eval("result1 = x + y;")
    return fdtd.get("result1")

def run_simulation_2(fdtd):
    """第二个仿真函数，使用相同的变量名"""
    fdtd.eval("x = 10;")  # 可能意外覆盖第一个函数的 x
    fdtd.eval("y = 20;")
    fdtd.eval("result2 = x * y;")
    return fdtd.get("result2")

# 创建会话
fdtd = lumapi.FDTD()

# 运行第一个仿真
result1 = run_simulation_1(fdtd)
print(f"仿真1结果: {result1}")

# 清除第一个仿真的变量以避免冲突
fdtd.clear("x", "y", "result1")

# 运行第二个仿真
result2 = run_simulation_2(fdtd)
print(f"仿真2结果: {result2}")

# 验证变量独立性
fdtd.eval("?x;")  # 应该显示 10，而不是 1
fdtd.eval("?y;")  # 应该显示 20，而不是 2

# 清理
fdtd.clear()
```

### 示例 5：安全的变量清除模式
```python
import lumapi

class SafeVariableManager:
    """安全的变量管理器，避免意外清除重要变量"""
    
    def __init__(self, session):
        self.session = session
        self.protected_vars = []
    
    def add_protected(self, var_name):
        """添加受保护的变量"""
        self.protected_vars.append(var_name)
    
    def clear_all_except_protected(self):
        """清除除受保护变量外的所有变量"""
        # 获取所有变量
        self.session.eval("vars = ?all;")
        all_vars = self.session.get("vars")
        
        if all_vars:
            for var in all_vars:
                if var not in self.protected_vars:
                    self.session.clear(var)
        
        # 清除临时变量
        self.session.clear("vars")
    
    def clear_safe(self, *vars_to_clear):
        """安全清除变量，跳过受保护变量"""
        for var in vars_to_clear:
            if var in self.protected_vars:
                print(f"警告: 跳过受保护变量 {var}")
            else:
                self.session.clear(var)

# 使用示例
fdtd = lumapi.FDTD()
manager = SafeVariableManager(fdtd)

# 设置一些变量
fdtd.eval("important_config = struct('version', '1.0');")
fdtd.eval("temp_data1 = 100;")
fdtd.eval("temp_data2 = 200;")
fdtd.eval("temp_data3 = 300;")

# 标记重要变量为受保护
manager.add_protected("important_config")

print("清除前变量:")
fdtd.eval("?all;")

# 安全清除
manager.clear_safe("temp_data1", "temp_data2", "important_config")  # 跳过 important_config

print("\n安全清除后变量:")
fdtd.eval("?all;")

# 清除除受保护变量外的所有变量
manager.clear_all_except_protected()

print("\n清除除受保护变量外的所有变量后:")
fdtd.eval("?all;")
```

## 注意事项

1. **不可恢复性**：`clear` 命令永久移除变量，无法撤销。确保在清除前保存重要数据。

2. **系统变量**：某些 Lumerical 内部系统变量可能无法清除，或清除后可能影响软件功能。通常不建议清除以下划线 (`_`) 开头的变量。

3. **内存管理**：清除大型数组或矩阵可以立即释放内存。这对于处理大型数据集时防止内存不足错误非常重要。

4. **变量名称**：变量名称区分大小写。`clear("Data")` 和 `clear("data")` 清除不同的变量。

5. **字符串参数**：当使用字符串参数时，确保字符串包含确切的变量名。使用 `clear("var")` 而不是 `clear(var)`，除非 `var` 本身是包含变量名的字符串变量。

6. **与 `purge` 的区别**：Lumerical 中可能还有 `purge` 命令，用于更彻底地清理内存和资源。`clear` 只移除变量，而 `purge` 可能还清除缓存、临时文件等。

7. **脚本调试**：在调试脚本时，经常使用 `clear` 来确保每次运行都从干净状态开始，避免之前运行的残留变量影响结果。

8. **性能影响**：频繁调用 `clear` 可能对性能有轻微影响，但在内存受限的情况下，清除不再需要的大型变量可以显著提高性能。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有版本 |
| MODE Solutions | ✅ 完全支持 | 所有版本 |
| DEVICE | ✅ 完全支持 | 所有版本 |
| INTERCONNECT | ✅ 完全支持 | 所有版本 |

## 相关命令

- `?all` - 列出所有变量
- `?memory` - 显示内存使用情况
- `purge` - 彻底清理内存和资源
- `save` - 保存变量到文件（在清除前保存重要数据）
- `load` - 从文件加载变量（在清除后恢复数据）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本语法和示例 |
| 1.1 | 2026-01-31 | 添加返回值、错误处理章节、版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - clear 命令
2. Lumerical Python API Documentation - session.clear() 方法
3. Lumerical Memory Management Guide - 变量和内存管理最佳实践

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*