# eval - 执行脚本字符串

## 概述

`eval` 命令用于动态执行 Lumerical 脚本语言（LSF）代码字符串。它是连接 Python/Lumapi 与 Lumerical 脚本引擎的桥梁，允许在 Python 环境中灵活地执行任意 Lumerical 脚本代码。

### 主要功能
- 执行字符串形式的 Lumerical 脚本代码
- 动态生成和执行脚本
- 在 Python 和 Lumerical 脚本之间传递数据和逻辑
- 实现复杂的控制流和条件执行

### 关键特性
1. **动态代码执行** - 运行时构建和执行脚本
2. **无缝集成** - 在 Python 中混合使用 Lumerical 脚本
3. **灵活性** - 处理复杂的、条件性的脚本逻辑
4. **调试工具** - 用于测试和验证脚本片段

### 典型应用场景
1. **动态参数化仿真** - 根据输入参数动态生成仿真脚本
2. **批量处理** - 循环执行相似的脚本操作
3. **条件执行** - 根据仿真结果动态决定下一步操作
4. **脚本模板** - 使用模板生成特定仿真脚本
5. **调试和测试** - 快速测试脚本片段

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
eval("script_string");

# 执行多行脚本
eval("
    addrect;
    set('name', 'structure');
    set('material', 'Si');
    set('x span', 500e-9);
");

# 使用变量
script = "addcircle; set('radius', 200e-9);";
eval(script);
```

### Python API (Lumapi)
```python
# 基本调用
session.eval("script_string")

# 执行多行脚本（使用三引号）
session.eval("""
    addrect;
    set('name', 'structure');
    set('material', 'Si (Silicon) - Palik');
    set('x span', 500e-9);
""")

# 使用 Python 字符串变量
script = "addcircle; set('radius', 200e-9);"
session.eval(script)

# 带返回值的执行
result = session.eval("2 + 3 * 4")  # 返回计算结果
print(f"计算结果: {result}")
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `script_string` | 字符串 | 是 | 无 | 要执行的 Lumerical 脚本代码 |
| `返回值` | 多种 | 否 | 无 | 脚本最后一条语句的结果 |

## 配置属性

`eval` 命令本身没有可通过 `set` 命令配置的属性，因为它直接执行脚本字符串。然而，可以通过脚本字符串中的命令参数控制执行行为：

| 相关参数 | 类型 | 描述 | 示例 |
|----------|------|------|------|
| `script_string` | 字符串 | 要执行的 Lumerical 脚本代码 | `"addrect; set('x span', 500e-9);"` |
| `timeout` | 数值 | 执行超时时间（通过外部封装控制） | `session.eval(script, timeout=10)` |
| `error_handling` | 布尔 | 错误处理模式（Python 层控制） | `try: session.eval(script)` |

### 执行上下文配置
虽然 `eval` 没有直接属性，但可以通过以下方式影响执行环境：

1. **会话状态**: 当前会话中的变量和对象会影响脚本执行
2. **全局设置**: 通过 `set` 命令配置的全局参数（如网格精度、仿真时间）
3. **Python 封装**: 在 Python 层添加超时、错误处理等控制

## 返回值

`eval` 命令返回脚本中最后一条可执行语句的结果：

| 脚本最后语句 | 返回值 | 示例 |
|-------------|--------|------|
| 赋值语句 | 右侧表达式的值 | `eval("x = 5 + 3;")` 返回 `8` |
| 表达式 | 表达式结果 | `eval("2 * pi;")` 返回 `6.283185307179586` |
| 函数调用 | 函数返回值 | `eval("sin(pi/2);")` 返回 `1.0` |
| 命令调用 | 命令返回值 | `eval("addrect;")` 返回新对象的句柄 |
| 无返回值语句 | `None` 或空值 | `eval("?"Hello";")` 返回 `None` |

## 使用示例

### 示例 1：基本几何创建
```python
import lumapi

# 创建 FDTD 会话
fdtd = lumapi.FDTD()

# 使用 eval 创建简单结构
fdtd.eval("""
    # 创建矩形波导
    addrect;
    set("name", "waveguide");
    set("material", "Si (Silicon) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", 500e-9);
    set("y span", 220e-9);
    
    # 创建仿真区域
    addfdtd;
    set("dimension", "3D");
    set("x span", 2e-6);
    set("y span", 2e-6);
    set("z span", 1e-6);
    
    # 添加光源
    addmode;
    set("injection axis", "z");
    set("direction", "forward");
    
    # 添加监视器
    addpower;
    set("monitor type", "linear x");
    set("x", 0);
    
    ?"基本结构创建完成";
""")

# 验证创建的对象
objects = fdtd.eval("get(\"objecttype\");")
print(f"创建的对象类型: {objects}")

# 获取波导属性
waveguide_material = fdtd.eval('getnamed("waveguide", "material");')
print(f"波导材料: {waveguide_material}")
```

### 示例 2：动态参数化设计
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 参数化波导设计
waveguide_widths = [400e-9, 450e-9, 500e-9, 550e-9]
waveguide_thickness = 220e-9
wavelength = 1.55e-6

results = []
for i, width in enumerate(waveguide_widths):
    # 动态生成脚本
    script = f"""
    # 清理之前的对象（如果存在）
    if (exist("waveguide_{i}")) {{
        delete("waveguide_{i}");
    }}
    if (exist("fde_solver_{i}")) {{
        delete("fde_solver_{i}");
    }}
    
    # 创建波导
    addrect;
    set("name", "waveguide_{i}");
    set("material", "Si (Silicon) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", {width});
    set("y span", {waveguide_thickness});
    
    # 创建 FDE 求解器
    addfde;
    set("name", "fde_solver_{i}");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("z span", 2e-6);
    set("wavelength", {wavelength});
    set("number of trial modes", 5);
    
    # 运行求解
    findmodes;
    
    # 获取结果
    neff_data = getresult("fde_solver_{i}", "neff");
    if (length(neff_data) > 0) {{
        neff = neff_data(1);
    }} else {{
        neff = 0;
    }}
    
    # 返回结果
    neff;
    """
    
    # 执行脚本并获取结果
    neff = mode.eval(script)
    results.append(neff)
    
    print(f"波导宽度: {width*1e9:.0f} nm, 有效折射率: {neff:.6f}")

# 分析结果
print(f"\n波导宽度扫描结果 (厚度: {waveguide_thickness*1e9:.0f}nm, λ: {wavelength*1e9:.1f}nm):")
for width, neff in zip(waveguide_widths, results):
    print(f"  宽度 {width*1e9:.0f}nm: n_eff = {neff:.6f}")

# 找出最佳宽度（最高有效折射率）
best_idx = np.argmax(results)
print(f"\n最佳宽度: {waveguide_widths[best_idx]*1e9:.0f} nm")
print(f"最高有效折射率: {results[best_idx]:.6f}")
```

### 示例 3：条件脚本执行
```python
import lumapi

fdtd = lumapi.FDTD()

# 根据条件执行不同的仿真设置
simulation_type = "fast"  # 可选项: "fast", "accurate", "high_precision"

# 动态生成基于条件的脚本
if simulation_type == "fast":
    script = """
    # 快速仿真设置
    addfdtd;
    set("dimension", "2D");
    set("x span", 5e-6);
    set("y span", 3e-6);
    set("mesh accuracy", 2);
    set("simulation time", 1000e-15);
    set("auto shutoff min", 1e-5);
    ?"使用快速仿真设置";
    """
elif simulation_type == "accurate":
    script = """
    # 精确仿真设置
    addfdtd;
    set("dimension", "3D");
    set("x span", 5e-6);
    set("y span", 3e-6);
    set("z span", 1e-6);
    set("mesh accuracy", 3);
    set("simulation time", 2000e-15);
    set("auto shutoff min", 1e-6);
    ?"使用精确仿真设置";
    """
else:  # high_precision
    script = """
    # 高精度仿真设置
    addfdtd;
    set("dimension", "3D");
    set("x span", 5e-6);
    set("y span", 3e-6);
    set("z span", 1e-6);
    set("mesh accuracy", 4);
    set("simulation time", 5000e-15);
    set("auto shutoff min", 1e-7);
    set("pml layers", 16);
    ?"使用高精度仿真设置";
    """

# 执行条件脚本
fdtd.eval(script)

# 根据仿真类型创建不同的结构
structure_script = f"""
# 创建结构
addrect;
set("name", "device");
set("material", "Si (Silicon) - Palik");

# 根据仿真类型调整结构尺寸
if ("{simulation_type}" == "fast") {{
    set("x span", 1e-6);
    set("y span", 500e-9);
    set("z span", 220e-9);
}} elseif ("{simulation_type}" == "accurate") {{
    set("x span", 2e-6);
    set("y span", 500e-9);
    set("z span", 220e-9);
}} else {{
    set("x span", 2e-6);
    set("y span", 500e-9);
    set("z span", 220e-9);
    # 高精度模式下添加更多细节
    addcircle;
    set("name", "hole");
    set("material", "Air");
    set("radius", 100e-9);
    set("x", 500e-9);
    set("y", 0);
    set("z", 0);
}}
?"结构创建完成，仿真类型: {simulation_type}";
"""

fdtd.eval(structure_script)

# 获取实际设置
mesh_accuracy = fdtd.eval('getnamed("FDTD", "mesh accuracy");')
simulation_time = fdtd.eval('getnamed("FDTD", "simulation time");')
print(f"\n仿真配置:")
print(f"  类型: {simulation_type}")
print(f"  网格精度: {mesh_accuracy}")
print(f"  仿真时间: {simulation_time*1e15:.0f} fs")
```

### 示例 4：批量数据处理
```python
import lumapi
import numpy as np

mode = lumapi.MODE()

# 批量创建和分析多个结构
num_structures = 5
base_width = 400e-9
width_step = 50e-9

print("批量波导分析:")
print("=" * 70)

# 使用单个 eval 执行批量操作
batch_script = """
# 初始化结果数组
neff_results = matrix({num_structures}, 1);
width_results = matrix({num_structures}, 1);

# 批量创建和分析
for (i = 1:{num_structures}) {{
    width = {base_width} + (i-1)*{width_step};
    
    # 创建波导
    addrect;
    set("name", "waveguide_batch_" + num2str(i));
    set("material", "Si (Silicon) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", width);
    set("y span", 220e-9);
    
    # 创建 FDE 求解器
    addfde;
    set("name", "fde_batch_" + num2str(i));
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("z span", 2e-6);
    set("wavelength", 1.55e-6);
    set("number of trial modes", 5);
    
    # 运行求解
    findmodes;
    
    # 获取结果
    neff_data = getresult("fde_batch_" + num2str(i), "neff");
    if (length(neff_data) > 0) {{
        neff_results(i) = neff_data(1);
    }} else {{
        neff_results(i) = 0;
    }}
    width_results(i) = width;
    
    ?"完成结构 " + num2str(i) + ": 宽度 = " + num2str(width*1e9) + " nm";
}}

# 清理临时对象
for (i = 1:{num_structures}) {{
    delete("waveguide_batch_" + num2str(i));
    delete("fde_batch_" + num2str(i));
}}

# 返回结果
[neff_results, width_results];
""".format(num_structures=num_structures, base_width=base_width, width_step=width_step)

# 执行批量脚本
results = mode.eval(batch_script)

if results and len(results) == 2:
    neff_results = results[0]
    width_results = results[1]
    
    print("\n批量分析结果:")
    print("-" * 70)
    print("序号 | 宽度 (nm) | 有效折射率 | 备注")
    print("-" * 70)
    
    for i in range(num_structures):
        width = width_results[i] * 1e9
        neff = neff_results[i]
        
        if neff > 0:
            status = "成功"
        else:
            status = "失败"
            
        print(f"{i+1:4d} | {width:9.1f} | {neff:11.6f} | {status}")
    
    # 计算趋势
    valid_indices = neff_results > 0
    if np.any(valid_indices):
        valid_neff = neff_results[valid_indices]
        valid_widths = width_results[valid_indices]
        
        # 简单线性拟合（实际关系可能非线性）
        if len(valid_neff) > 1:
            coeff = np.polyfit(valid_widths, valid_neff, 1)
            slope = coeff[0]  # dn_eff/dwidth
            
            print(f"\n趋势分析:")
            print(f"  有效折射率随宽度变化斜率: {slope*1e9:.6f} /μm")
            print(f"  宽度增加 100nm 时 n_eff 变化: {slope*100e-9:.6f}")
    
    print("=" * 70)
else:
    print("批量分析失败")
```

### 示例 5：复杂算法实现
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 实现优化算法（简单网格搜索）
def optimize_waveguide():
    """优化波导宽度以获得最大传输效率"""
    
    # 参数范围
    min_width = 300e-9
    max_width = 700e-9
    num_points = 9
    
    widths = np.linspace(min_width, max_width, num_points)
    transmissions = []
    
    print("波导宽度优化:")
    print("=" * 70)
    
    for i, width in enumerate(widths):
        # 动态生成完整仿真脚本
        script = f"""
        # 清理之前的仿真
        if (exist("FDTD")) {{
            delete("FDTD");
        }}
        if (exist("waveguide_opt")) {{
            delete("waveguide_opt");
        }}
        if (exist("source_opt")) {{
            delete("source_opt");
        }}
        if (exist("monitor_opt")) {{
            delete("monitor_opt");
        }}
        
        # 创建 FDTD 求解器
        addfdtd;
        set("dimension", "2D");
        set("x span", 4e-6);
        set("y span", 2e-6);
        set("mesh accuracy", 3);
        set("simulation time", 1000e-15);
        
        # 创建波导
        addrect;
        set("name", "waveguide_opt");
        set("material", "Si (Silicon) - Palik");
        set("x", 0);
        set("y", 0);
        set("x span", {width});
        set("y span", 220e-9);
        
        # 创建模式源
        addmode;
        set("name", "source_opt");
        set("injection axis", "x");
        set("mode selection", "fundamental TE mode");
        set("x", -1.5e-6);
        
        # 创建功率监视器
        addpower;
        set("name", "monitor_opt");
        set("monitor type", "linear x");
        set("x", 1.5e-6);
        
        # 运行仿真
        run;
        
        # 获取传输效率
        T_data = transmission("monitor_opt");
        if (length(T_data) > 0) {{
            T = T_data(1);  # 基频传输
        }} else {{
            T = 0;
        }}
        
        # 返回结果
        T;
        """
        
        # 执行仿真
        transmission_value = fdtd.eval(script)
        transmissions.append(transmission_value)
        
        print(f"宽度 {width*1e9:.0f} nm: 传输效率 = {transmission_value*100:.2f}%")
    
    # 找出最佳宽度
    best_idx = np.argmax(transmissions)
    best_width = widths[best_idx]
    best_transmission = transmissions[best_idx]
    
    print("=" * 70)
    print(f"优化结果:")
    print(f"  最佳宽度: {best_width*1e9:.1f} nm")
    print(f"  最大传输效率: {best_transmission*100:.2f}%")
    
    # 绘制结果
    plot_script = f"""
    # 绘制优化结果
    widths = {list(widths)};
    transmissions = {list(transmissions)};
    
    # 创建图形
    figure;
    plot(widths*1e9, transmissions*100, 'o-', 'LineWidth', 2);
    xlabel('波导宽度 (nm)');
    ylabel('传输效率 (%)');
    title('波导宽度优化结果');
    grid on;
    
    # 标记最佳点
    hold on;
    plot({best_width}*1e9, {best_transmission}*100, 'r*', 'MarkerSize', 15, 'LineWidth', 2);
    text({best_width}*1e9 + 10, {best_transmission}*100, 
         sprintf('最佳: %.1f nm, %.1f%%', {best_width}*1e9, {best_transmission}*100),
         'VerticalAlignment', 'bottom', 'FontSize', 10);
    hold off;
    
    # 保存结果
    savefig('waveguide_optimization.png');
    ?"优化结果图已保存为 waveguide_optimization.png";
    """
    
    fdtd.eval(plot_script)
    
    return best_width, best_transmission

# 运行优化
best_width, best_transmission = optimize_waveguide()

# 使用最佳参数创建最终设计
final_design_script = f"""
# 使用优化结果创建最终设计
?"创建最终波导设计:";
?"宽度: {best_width*1e9:.1f} nm";
?"预期传输效率: {best_transmission*100:.2f}%";

# 创建最终结构
addrect;
set("name", "optimized_waveguide");
set("material", "Si (Silicon) - Palik");
set("x", 0);
set("y", 0);
set("x span", {best_width});
set("y span", 220e-9);

# 保存设计
save("optimized_design.fsp");
?"设计已保存为 optimized_design.fsp";
"""

fdtd.eval(final_design_script)
```

## 注意事项

### 1. 脚本字符串转义
- 字符串中的引号需要正确转义
- 多行字符串注意换行符处理
- 特殊字符（如反斜杠）需要转义

### 2. 性能考虑
- 频繁调用 `eval` 可能影响性能
- 复杂脚本可以合并到单个 `eval` 调用中
- 避免在循环中重复执行相同脚本

### 3. 错误处理
- `eval` 中的错误会抛出异常
- 使用 try-except 块捕获和处理错误
- 在脚本中添加错误检查代码

### 4. 安全性
- 不要执行不可信的脚本字符串
- 避免从外部源直接执行未验证的脚本
- 对用户输入进行验证和清理

### 5. 变量作用域
- `eval` 中创建的变量在会话中保持
- 注意变量名冲突
- 及时清理临时变量

## 错误处理

`eval` 命令执行过程中可能遇到多种错误，包括脚本语法错误、运行时错误、超时错误等。正确处理这些错误对于构建健壮的自动化流程至关重要。

### 常见错误类型

#### 1. 脚本语法错误
**问题描述**: Lumerical 脚本语法不正确。
**错误示例**:
```python
import lumapi
fdtd = lumapi.FDTD()
try:
    # 缺少分号导致语法错误
    fdtd.eval("addrect set('name', 'test')")
except Exception as e:
    print(f"语法错误: {e}")
```
**解决方案**: 
- 使用 Lumerical 脚本编辑器验证语法
- 逐步构建复杂脚本
- 在脚本中添加语法检查

#### 2. 运行时错误
**问题描述**: 脚本语法正确，但执行时出现问题（如未定义变量、无效参数）。
**错误示例**:
```python
import lumapi
fdtd = lumapi.FDTD()
try:
    # 引用不存在的对象
    fdtd.eval("setnamed('nonexistent', 'x', 0)")
except Exception as e:
    print(f"运行时错误: {e}")
```
**解决方案**:
- 在执行前检查对象是否存在
- 使用条件语句包装可能失败的操作
- 添加错误恢复逻辑

#### 3. 超时错误
**问题描述**: 脚本执行时间过长，可能导致会话无响应。
**错误示例**:
```python
import lumapi
import threading
import time

fdtd = lumapi.FDTD()

def execute_with_timeout(script, timeout=5):
    """带超时保护的 eval 执行"""
    result = [None]
    error = [None]
    
    def worker():
        try:
            result[0] = fdtd.eval(script)
        except Exception as e:
            error[0] = e
    
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        # 超时处理
        print(f"脚本执行超时（{timeout}秒）")
        return None
    elif error[0]:
        raise error[0]
    else:
        return result[0]

# 测试超时保护
long_script = """
# 可能耗时的操作
for (i = 1:1000000) {
    # 复杂计算
    x = sin(i) * cos(i);
}
"""
result = execute_with_timeout(long_script, timeout=2)
```

#### 4. 内存和资源错误
**问题描述**: 脚本消耗过多内存或资源。
**解决方案**:
- 监控内存使用
- 定期清理临时对象
- 分块处理大数据

### Python 错误处理模式

#### 模式 1: 基本 try-except
```python
import lumapi
from loguru import logger

fdtd = lumapi.FDTD()

def safe_eval(script, default=None):
    """安全的 eval 执行"""
    try:
        return fdtd.eval(script)
    except SyntaxError as e:
        logger.error(f"脚本语法错误: {e}")
        return default
    except RuntimeError as e:
        logger.error(f"脚本运行时错误: {e}")
        return default
    except Exception as e:
        logger.error(f"未知错误: {e}")
        return default

# 使用安全封装
result = safe_eval("addrect; set('name', 'test');")
```

#### 模式 2: 重试机制
```python
import lumapi
import time

def eval_with_retry(session, script, max_retries=3, delay=1):
    """带重试机制的 eval 执行"""
    for attempt in range(max_retries):
        try:
            return session.eval(script)
        except Exception as e:
            if attempt == max_retries - 1:
                raise  # 最后一次重试仍失败，抛出异常
            print(f"尝试 {attempt + 1} 失败，{delay} 秒后重试: {e}")
            time.sleep(delay)
    return None

# 使用重试机制
fdtd = lumapi.FDTD()
script = "addrect; set('name', 'test_retry');"
result = eval_with_retry(fdtd, script, max_retries=3)
```

#### 模式 3: 验证和清理
```python
import lumapi

def validated_eval(session, script):
    """验证脚本并确保资源清理"""
    # 预验证脚本（简单检查）
    if not script or len(script.strip()) == 0:
        raise ValueError("脚本不能为空")
    
    if "delete" not in script and "add" in script:
        print("警告: 脚本创建对象但未包含清理代码")
    
    try:
        result = session.eval(script)
        return result
    finally:
        # 确保执行后清理临时变量（可选）
        cleanup_script = """
        # 清理临时变量（示例）
        temp_vars = who("temp_*");
        for (i = 1:length(temp_vars)) {
            clear(temp_vars{i});
        }
        """
        try:
            session.eval(cleanup_script)
        except:
            pass  # 清理失败不影响主逻辑

# 使用验证执行
fdtd = lumapi.FDTD()
script = """
temp_value = 42;
addrect;
set('name', 'validated_structure');
? "创建成功";
"""
result = validated_eval(fdtd, script)
```

### 调试技巧

#### 1. 脚本分段执行
```python
def debug_eval_script(session, script):
    """调试脚本执行"""
    lines = script.split(';')
    for i, line in enumerate(lines):
        line = line.strip()
        if line:  # 非空行
            print(f"执行第 {i+1} 行: {line}")
            try:
                result = session.eval(line + ";")
                print(f"  成功: {result}")
            except Exception as e:
                print(f"  失败: {e}")
                print(f"  问题行: {line}")
                break

# 调试脚本
fdtd = lumapi.FDTD()
complex_script = """
addrect;
set('name', 'debug_test');
set('x span', 500e-9);
set('y span', 220e-9);
invalid_command;
set('material', 'Si');
"""
debug_eval_script(fdtd, complex_script)
```

#### 2. 错误信息解析
```python
def parse_eval_error(error):
    """解析 eval 错误信息"""
    error_str = str(error)
    
    if "syntax" in error_str.lower():
        return "语法错误: 检查脚本语法（缺少分号、括号不匹配等）"
    elif "undefined" in error_str.lower():
        return "未定义错误: 变量或对象未定义"
    elif "parameter" in error_str.lower():
        return "参数错误: 命令参数无效"
    elif "memory" in error_str.lower():
        return "内存错误: 内存不足"
    else:
        return f"未知错误: {error_str}"

# 使用错误解析
try:
    fdtd.eval("invalid command;")
except Exception as e:
    diagnosis = parse_eval_error(e)
    print(f"错误诊断: {diagnosis}")
```

#### 3. 脚本验证工具
```python
import re

def validate_script(script):
    """简单脚本验证"""
    issues = []
    
    # 检查基本语法
    if not script.endswith(';') and not script.strip().endswith('}'):
        issues.append("警告: 脚本可能缺少结束分号")
    
    # 检查括号匹配
    open_braces = script.count('{')
    close_braces = script.count('}')
    if open_braces != close_braces:
        issues.append(f"错误: 括号不匹配（{{:{open_braces}, }}:{close_braces}）")
    
    # 检查常见问题
    if re.search(r'set\s*\([^)]*$', script):
        issues.append("警告: set 命令可能缺少闭合括号")
    
    return issues

# 验证脚本
script = """
addrect;
set('name', 'test'
set('x span', 500e-9);
"""
issues = validate_script(script)
for issue in issues:
    print(issue)
```

### 预防措施

1. **脚本测试**: 在完整执行前先测试脚本片段
2. **版本控制**: 对常用脚本进行版本管理
3. **日志记录**: 记录所有 eval 执行和结果
4. **资源监控**: 监控内存和 CPU 使用情况
5. **超时设置**: 为长时间运行脚本设置超时

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 动态仿真控制 |
| **MODE Solutions** | 完全支持 | 模式分析和优化 |
| **DEVICE** | 完全支持 | 器件仿真脚本 |
| **INTERCONNECT** | 完全支持 | 电路仿真控制 |

## 相关命令

- [`exec`](./exec.md) - 执行脚本文件（如果存在）
- [`run`](./run.md) - 运行仿真
- [`script`](./script.md) - 脚本对象操作
- [`function`](./function.md) - 定义可重用函数

## 最佳实践

### 1. 脚本模板化
```python
# 使用模板减少重复代码
def create_waveguide_template(width, thickness, material):
    template = """
    addrect;
    set("name", "{name}");
    set("material", "{material}");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", {width});
    set("y span", {thickness});
    """
    return template.format(
        name="waveguide",
        material=material,
        width=width,
        thickness=thickness
    )

# 使用模板
script = create_waveguide_template(500e-9, 220e-9, "Si (Silicon) - Palik")
session.eval(script)
```

### 2. 错误处理封装
```python
def safe_eval(session, script, default_return=None):
    """安全的 eval 封装，提供错误处理"""
    try:
        return session.eval(script)
    except Exception as e:
        print(f"脚本执行错误: {e}")
        print(f"问题脚本: {script[:100]}...")
        return default_return

# 使用安全封装
result = safe_eval(fdtd, "addrect; set('name', 'test');", default_return=False)
```

### 3. 性能优化
```python
# 批量操作合并到单个 eval
def batch_create_structures(session, structures):
    """批量创建多个结构"""
    script_lines = []
    for i, (width, height, material) in enumerate(structures):
        script_lines.append(f"""
        addrect;
        set("name", "structure_{i}");
        set("material", "{material}");
        set("x span", {width});
        set("y span", {height});
        """)
    
    # 合并为单个脚本执行
    full_script = "\n".join(script_lines)
    return session.eval(full_script)
```

## 调试技巧

### 1. 逐步执行调试
```python
def debug_eval(script):
    """添加调试信息的 eval"""
    print(f"执行脚本长度: {len(script)} 字符")
    print(f"脚本前100字符: {script[:100]}...")
    
    try:
        result = session.eval(script)
        print(f"执行成功，返回值: {result}")
        return result
    except Exception as e:
        print(f"执行失败: {e}")
        # 尝试分割脚本以定位问题
        lines = script.split(';')
        for i, line in enumerate(lines[:10]):  # 检查前10行
            print(f"行 {i}: {line.strip()}")
        raise
```

### 2. 变量检查
```python
def check_variables(session):
    """检查当前会话中的变量"""
    script = """
    # 获取所有变量
    vars = who();
    vars;
    """
    variables = session.eval(script)
    print(f"当前变量: {variables}")
    return variables
```

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2025-01-31 | 初始版本 |
| 1.1 | 2025-02-01 | 增加优化算法和最佳实践 |
| 1.2 | 2026-01-31 | 添加配置属性、错误处理和参考章节，更新文档结构 |

## 扩展应用

### 1. 脚本生成器
```python
class ScriptGenerator:
    """Lumerical 脚本生成器"""
    
    def __init__(self):
        self.lines = []
    
    def add_command(self, command, **kwargs):
        """添加命令到脚本"""
        if kwargs:
            params = ", ".join([f"'{k}', {v}" for k, v in kwargs.items()])
            self.lines.append(f"{command}({params});")
        else:
            self.lines.append(f"{command};")
    
    def get_script(self):
        """获取完整脚本"""
        return "\n".join(self.lines)
    
    def execute(self, session):
        """执行生成的脚本"""
        return session.eval(self.get_script())

# 使用脚本生成器
generator = ScriptGenerator()
generator.add_command("addrect", name="waveguide", material="Si")
generator.add_command("set", x=0, y=0, z=0)
generator.add_command("set", x_span="500e-9", y_span="220e-9")

script = generator.get_script()
print("生成的脚本:")
print(script)
```

### 2. 条件脚本构建
```python
def build_conditional_script(condition, true_script, false_script):
    """构建条件脚本"""
    return f"""
    if ({condition}) {{
        {true_script}
    }} else {{
        {false_script}
    }}
    """

# 使用条件脚本构建
condition = "width > 400e-9"
true_script = "?\"宽度大于400nm\"; set('material', 'Si3N4');"
false_script = "?\"宽度小于等于400nm\"; set('material', 'SiO2');"

conditional_script = build_conditional_script(condition, true_script, false_script)
```

## 参考

1. Lumerical Script Language Reference - eval Command
2. Lumerical Python API Documentation: Session.eval() Method
3. Python Official Documentation: Exception Handling
4. ANSYS Lumerical Knowledge Base: Scripting Best Practices

---

*文档版本：1.2 | 最后更新：2026-01-31*