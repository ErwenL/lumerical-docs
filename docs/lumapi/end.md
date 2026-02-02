# end - 结束代码块

## 概述

`end` 命令是 Lumerical 脚本语言中的控制结构终止符，用于标记代码块的结束。它与各种控制语句（如 `if`、`for`、`while`、`function`、`switch` 等）配对使用，定义代码块的边界。

### 主要功能
- 标记条件语句、循环语句、函数定义等代码块的结束
- 提供清晰的代码结构划分
- 确保控制结构的正确嵌套和范围界定
- 提高代码的可读性和可维护性

### 典型应用场景
1. **控制结构结束** - 结束 `if`、`else`、`elseif` 条件块
2. **循环终止** - 结束 `for`、`while` 循环块
3. **函数定义结束** - 标记函数定义的结束
4. **开关语句结束** - 结束 `switch` 语句块
5. **代码块组织** - 用于组织和结构化复杂脚本

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 结束 if 语句
if (condition) {
    # 代码块
} end

# 结束 for 循环
for (i = 1:10) {
    # 循环体
} end

# 结束 while 循环
while (condition) {
    # 循环体
} end

# 结束函数定义
function result = myFunction(x) {
    # 函数体
    result = x * 2;
} end

# 结束 switch 语句
switch (value) {
    case 1:
        # 代码
        break;
    case 2:
        # 代码
        break;
} end

# 嵌套结构
if (condition1) {
    for (i = 1:n) {
        if (condition2) {
            # 代码
        } end
    } end
} end
```

### Python API (Lumapi)
```python
# 在 Python 中，end 命令通常不需要显式调用
# Lumerical 脚本中的 end 在 Python 中通过缩进隐式处理

# 示例：在 Lumapi 中执行包含 end 的脚本字符串
script = """
# 定义函数
function y = square(x) {
    y = x * x;
} end

# 使用函数
result = square(5);
?"平方结果: " + num2str(result);
"""
session.eval(script)

# Python 中的等价代码
def square(x):
    return x * x

result = square(5)
print(f"平方结果: {result}")

# 复杂结构的 Python 实现
script = """
# 嵌套循环和条件
for (i = 1:3) {
    for (j = 1:3) {
        if (i == j) {
            ?"对角线元素: i=" + num2str(i) + ", j=" + num2str(j);
        } end
    } end
} end
"""
session.eval(script)
```

## 参数

`end` 语句本身不接收参数，它只是标记前面控制结构的结束：

| 相关结构 | 语法要求 | 描述 |
|----------|----------|------|
| `if` | `if (condition) { ... } end` | 结束条件语句块 |
| `for` | `for (init; condition; update) { ... } end` | 结束 for 循环块 |
| `while` | `while (condition) { ... } end` | 结束 while 循环块 |
| `function` | `function output = name(input) { ... } end` | 结束函数定义 |
| `switch` | `switch (value) { ... } end` | 结束 switch 语句块 |

## 配置属性

`end` 作为控制结构终止符，没有可通过 `set` 命令配置的属性。相关的代码组织参数包括：

| 相关参数 | 类型 | 描述 | 使用示例 |
|----------|------|------|----------|
| 代码块长度 | 整数 | 控制结构内的代码行数 | 建议不超过 50-100 行 |
| 嵌套深度 | 整数 | 控制结构的嵌套层数 | 建议不超过 3-4 层 |
| 缩进风格 | 字符串 | 代码缩进方式（空格或制表符） | 通常使用 2-4 个空格 |

## 返回值

`end` 语句本身不返回值，它仅作为控制结构的语法标记。当作为脚本命令执行时，`end` 不产生任何输出值，但确保控制结构正确终止，避免语法错误。

### LSF 脚本中的行为
- 在 Lumerical 脚本语言中，`end` 不返回任何值
- 如果 `end` 缺失或不匹配，脚本解释器会报告语法错误
- 正确使用 `end` 确保后续代码的正确执行

### Python API 中的行为
- 在 Lumapi Python API 中，`end` 通常不需要显式调用
- 当通过 `session.eval()` 执行包含 `end` 的脚本时，返回值取决于整个脚本的最后一个表达式
- `end` 本身不贡献任何返回值

### 返回值总结
| 上下文 | 返回值 | 说明 |
|--------|--------|------|
| LSF 脚本 | 无 | 不产生任何值，仅语法标记 |
| Python `eval()` | 无 | 不返回特定值，取决于脚本 |
| 直接使用 | 不适用 | `end` 不能独立使用 |

## 使用示例

### 示例 1：基本控制结构结束
```python
import lumapi

fdtd = lumapi.FDTD()

# 使用 end 结束各种控制结构
script = """
# if 语句
x = 5;
if (x > 0) {
    ?"x 是正数";
    category = "positive";
} end

# for 循环
sum = 0;
for (i = 1:10) {
    sum = sum + i;
} end
?"1到10的和: " + num2str(sum);

# while 循环
count = 0;
value = 10;
while (value > 1) {
    value = value / 2;
    count = count + 1;
} end
?"需要 " + num2str(count) + " 次除以2才能小于1";

# 函数定义
function area = circleArea(radius) {
    area = pi * radius * radius;
} end

# 使用函数
r = 2;
a = circleArea(r);
?"半径为 " + num2str(r) + " 的圆面积: " + num2str(a);
"""
fdtd.eval(script)

# 获取结果
sum_result = fdtd.get("sum")
count_result = fdtd.get("count")
print(f"1到10的和: {sum_result}")
print(f"除以2的次数: {count_result}")
```

### 示例 2：嵌套控制结构
```python
import lumapi

mode = lumapi.MODE()

# 复杂的嵌套控制结构
script = """
# 生成矩阵并处理
matrix_size = 5;
result_matrix = zeros(matrix_size, matrix_size);

for (i = 1:matrix_size) {
    for (j = 1:matrix_size) {
        # 根据位置决定值
        if (i == j) {
            # 对角线元素
            result_matrix(i,j) = 1;
        } elseif (abs(i-j) == 1) {
            # 次对角线元素
            result_matrix(i,j) = 0.5;
        } else {
            # 其他元素
            result_matrix(i,j) = 0;
        } end
    } end
} end

# 显示矩阵
?"生成的矩阵:";
for (i = 1:matrix_size) {
    row_str = "";
    for (j = 1:matrix_size) {
        row_str = row_str + num2str(result_matrix(i,j)) + " ";
    } end
    ?row_str;
} end

# 计算矩阵特征
trace = 0;
for (i = 1:matrix_size) {
    trace = trace + result_matrix(i,i);
} end
?"矩阵迹: " + num2str(trace);
"""
mode.eval(script)

# 获取生成的矩阵
matrix = mode.get("result_matrix")
print(f"生成的 {matrix.shape[0]}x{matrix.shape[1]} 矩阵:")
print(matrix)
```

### 示例 3：函数库定义
```python
import lumapi

fdtd = lumapi.FDTD()

# 定义数学函数库
script = """
# 几何函数库
function area = rectangleArea(width, height) {
    area = width * height;
} end

function volume = boxVolume(length, width, height) {
    volume = length * width * height;
} end

function hypotenuse = pythagorean(a, b) {
    hypotenuse = sqrt(a*a + b*b);
} end

# 物理光学函数
function neff = waveguideNeff(width, thickness, wavelength, material) {
    # 简化的有效折射率计算（实际应使用模式求解器）
    n_si = 3.48;  # 硅的折射率
    n_air = 1.00; # 空气的折射率
    
    # 近似公式（仅用于演示）
    confinement = 1 - exp(-width/(2*wavelength));
    neff = n_air + (n_si - n_air) * confinement;
} end

function loss = waveguideLoss(width, roughness) {
    # 简化的波导损耗计算
    # 基于侧壁粗糙度的散射损耗模型
    loss_per_meter = 100 * roughness / width;  # dB/m
    loss = loss_per_meter;
} end

# 使用函数库
?"几何计算示例:";
rect_area = rectangleArea(3, 4);
?"矩形面积 (3x4): " + num2str(rect_area);

box_vol = boxVolume(2, 3, 4);
?"长方体体积 (2x3x4): " + num2str(box_vol);

hyp = pythagorean(3, 4);
?"直角三角形斜边 (3-4-?): " + num2str(hyp);

?"光学计算示例:";
wg_neff = waveguideNeff(500e-9, 220e-9, 1.55e-6, "Si");
?"波导有效折射率: " + num2str(wg_neff);

wg_loss = waveguideLoss(500e-9, 5e-9);
?"波导损耗: " + num2str(wg_loss) + " dB/m";
"""
fdtd.eval(script)

# 在 Python 中也可以调用这些函数
rect_area = fdtd.get("rect_area")
box_vol = fdtd.get("box_vol")
print(f"矩形面积: {rect_area}")
print(f"长方体体积: {box_vol}")
```

### 示例 4：仿真流程控制
```python
import lumapi

mode = lumapi.MODE()

# 自动化仿真流程控制
script = """
# 仿真参数
wavelengths = linspace(1.5e-6, 1.6e-6, 11);  # 11个波长点
widths = [400e-9, 450e-9, 500e-9, 550e-9];   # 4种宽度
results = matrix(length(wavelengths), length(widths));

# 外层循环：波长扫描
for (w_idx = 1:length(wavelengths)) {
    wavelength = wavelengths(w_idx);
    ?"分析波长: " + num2str(wavelength*1e9) + " nm";
    
    # 内层循环：宽度扫描
    for (wdt_idx = 1:length(widths)) {
        width = widths(wdt_idx);
        
        # 创建波导结构
        addrect;
        set("name", "temp_waveguide");
        set("material", "Si (Silicon) - Palik");
        set("x", 0);
        set("y", 0);
        set("z", 0);
        set("x span", width);
        set("y span", 220e-9);
        set("z span", 10e-6);
        
        # 添加 FDE 求解器
        addfde;
        set("name", "temp_solver");
        set("x", 0);
        set("y", 0);
        set("z", 0);
        set("z span", 2e-6);
        
        # 配置求解器
        setnamed("temp_solver", "wavelength", wavelength);
        setnamed("temp_solver", "number of trial modes", 5);
        
        # 运行求解
        findmodes;
        
        # 获取结果
        neff_data = getresult("temp_solver", "neff");
        if (length(neff_data) > 0) {
            results(w_idx, wdt_idx) = neff_data(1);  # 基模有效折射率
        } else {
            results(w_idx, wdt_idx) = 0;
        } end
        
        # 清理临时对象
        delete("temp_waveguide");
        delete("temp_solver");
        
        ?"  宽度 " + num2str(width*1e9) + " nm: neff = " + num2str(results(w_idx, wdt_idx));
    } end
} end

?"扫描完成，结果矩阵:";
for (i = 1:size(results,1)) {
    row_str = "";
    for (j = 1:size(results,2)) {
        row_str = row_str + num2str(results(i,j), "%.4f") + " ";
    } end
    ?row_str;
} end
"""
mode.eval(script)

# 获取扫描结果
results = mode.get("results")
wavelengths = mode.get("wavelengths")
widths = mode.get("widths")

print(f"波长扫描范围: {wavelengths[0]*1e9:.1f} - {wavelengths[-1]*1e9:.1f} nm")
print(f"宽度扫描值: {[w*1e9 for w in widths]} nm")
print(f"结果矩阵形状: {results.shape}")
```

### 示例 5：错误处理和资源清理
```python
import lumapi

fdtd = lumapi.FDTD()

# 使用 end 确保资源正确清理
script = """
# 资源管理函数
function success = simulateWithCleanup(sim_params) {
    success = 0;  # 默认失败
    
    try {
        # 创建仿真结构
        addfdtd;
        set("dimension", "3D");
        set("x span", sim_params.x_span);
        set("y span", sim_params.y_span);
        set("z span", sim_params.z_span);
        
        # 添加结构
        addrect;
        set("name", "device");
        set("material", sim_params.material);
        set("x span", sim_params.device_width);
        set("y span", sim_params.device_height);
        set("z span", sim_params.device_length);
        
        # 添加源和监视器
        addmode;
        set("name", "source");
        
        addpower;
        set("name", "monitor");
        
        # 运行仿真
        run;
        
        # 获取结果
        transmission = getresult("monitor", "T");
        
        if (transmission > 0) {
            success = 1;
            ?"仿真成功，传输: " + num2str(transmission*100) + "%";
        } else {
            ?"仿真完成但传输为0";
        } end
        
    } catch (error_msg) {
        ?"仿真失败: " + error_msg;
        success = 0;
    } end
    
    # 清理资源（无论成功与否）
    try {
        delete("FDTD");
        delete("device");
        delete("source");
        delete("monitor");
        ?"资源已清理";
    } catch (cleanup_error) {
        ?"清理警告: " + cleanup_error;
    } end
    
    return success;
} end

# 使用函数
params.x_span = 2e-6;
params.y_span = 2e-6;
params.z_span = 1e-6;
params.material = "Si (Silicon) - Palik";
params.device_width = 500e-9;
params.device_height = 220e-9;
params.device_length = 10e-6;

?"开始仿真...";
result = simulateWithCleanup(params);

if (result) {
    ?"仿真流程成功完成";
} else {
    ?"仿真流程失败";
} end
"""
fdtd.eval(script)

# 检查仿真结果
success = fdtd.get("result")
if success:
    print("仿真成功完成")
else:
    print("仿真失败，已清理资源")
```

## 注意事项

### 1. 语法正确性
- 每个开始的控制结构必须有对应的 `end` 语句
- `end` 必须与正确的控制结构匹配
- 避免缺少 `end` 或多余 `end` 导致的语法错误

### 2. 嵌套匹配
```lumerical
// 正确：清晰的嵌套
if (condition1) {
    for (i = 1:n) {
        if (condition2) {
            // 代码
        } end  // 结束内层 if
    } end      // 结束 for
} end          // 结束外层 if

// 错误：end 不匹配
if (condition1) {
    for (i = 1:n) {
        // 代码
    } end  // 正确
}          // 错误：缺少 end
```

### 3. 代码可读性
- 使用一致的缩进风格
- 在复杂的嵌套结构中添加注释
- 避免过深的嵌套（建议不超过 3-4 层）

### 4. 作用域规则
- 在控制结构内定义的变量通常在该结构外不可见
- `end` 标记变量作用域的结束
- 需要跨作用域访问的变量应在外部定义

### 5. 性能考虑
- 过多的嵌套可能影响代码性能
- 在循环内部的复杂控制结构可能显著增加执行时间
- 考虑重构深层嵌套的代码

## 错误处理

`end` 语句的常见错误主要涉及语法不匹配和嵌套错误。正确使用 `end` 可以避免脚本执行失败。

### 常见错误类型

#### 1. 缺少 `end` 语句
**问题描述**: 控制结构缺少对应的 `end` 终止符。
**错误示例**:
```lumerical
if (x > 0) {
    ?"x is positive";
// 缺少 } end
```
**解决方案**: 确保每个控制结构都有对应的 `end`。
**Python 错误处理**:
```python
import lumapi

fdtd = lumapi.FDTD()
script = """
if (x > 0) {
    ?"x is positive";
// 缺少 } end
"""
try:
    fdtd.eval(script)
    print("脚本执行成功")
except Exception as e:
    print(f"脚本错误: {e}")
    print("错误原因: 缺少 end 语句")
    # 修复脚本
    fixed_script = """
if (x > 0) {
    ?"x is positive";
} end
"""
    fdtd.eval(fixed_script)
    print("修复后脚本执行成功")
```

#### 2. 多余 `end` 语句
**问题描述**: 控制结构后有额外的 `end`。
**错误示例**:
```lumerical
if (condition) {
    // 代码
} end
} end  // 多余
```
**解决方案**: 检查控制结构嵌套，确保每个 `end` 都有匹配的开始。
**Python 检测方法**:
```python
import re

def validate_end_statements(script):
    """验证 Lumerical 脚本中 end 语句的匹配性"""
    lines = script.split('\n')
    stack = []
    for i, line in enumerate(lines, 1):
        # 检测控制结构开始
        if re.search(r'\b(if|for|while|function|switch)\s*\(', line):
            stack.append((line.strip(), i))
        # 检测 end 语句
        if re.search(r'\}?\s*end\b', line):
            if not stack:
                return False, f"第 {i} 行: 多余的 end 语句"
            stack.pop()
    if stack:
        return False, f"未匹配的控制结构: {stack}"
    return True, "所有 end 语句匹配正确"

script = """
if (x > 0) {
    ?"positive";
} end
} end
"""
is_valid, message = validate_end_statements(script)
print(f"脚本验证: {is_valid}, {message}")
```

#### 3. 嵌套错误
**问题描述**: `end` 语句与控制结构不匹配，导致交叉嵌套。
**错误示例**:
```lumerical
if (condition1) {
    for (i = 1:10) {
        // 代码
} end      // 错误：这个 end 应该结束 for，但前面没有匹配的 for
    // 代码
} end      // 错误：这个 end 没有匹配的 if
```
**解决方案**: 使用一致的缩进和代码编辑器语法高亮来识别嵌套问题。

### 错误预防策略

#### 1. 使用代码编辑器功能
- 启用 Lumerical 脚本语法高亮
- 使用代码折叠功能可视化代码块
- 配置自动缩进设置

#### 2. 逐步开发方法
```python
# 逐步构建复杂脚本
def build_complex_script():
    script_parts = []
    
    # 添加外层结构
    script_parts.append("if (global_condition) {")
    script_parts.append("    // 外层代码")
    
    # 添加内层结构
    script_parts.append("    for (i = 1:10) {")
    script_parts.append("        // 内层代码")
    script_parts.append("    } end  // 结束 for")
    
    # 关闭外层结构
    script_parts.append("} end  // 结束 if")
    
    return '\n'.join(script_parts)

script = build_complex_script()
print("逐步构建的脚本:")
print(script)
```

#### 3. 自动化测试
```python
import lumapi

def test_script_with_end(script, session):
    """测试包含 end 语句的脚本"""
    try:
        session.eval(script)
        return True, "脚本执行成功"
    except Exception as e:
        error_msg = str(e)
        if "missing" in error_msg.lower() and "end" in error_msg.lower():
            return False, "错误: 缺少 end 语句"
        elif "unexpected" in error_msg.lower() and "end" in error_msg.lower():
            return False, "错误: 意外的 end 语句"
        else:
            return False, f"其他错误: {error_msg}"

# 测试用例
test_cases = [
    ("if (x>0) { ?'positive'; } end", "正确脚本"),
    ("if (x>0) { ?'positive'; }", "缺少 end"),
    ("if (x>0) { ?'positive'; } end } end", "多余 end"),
]

fdtd = lumapi.FDTD()
for script, description in test_cases:
    success, message = test_script_with_end(script, fdtd)
    print(f"{description}: {success} - {message}")
```

### 调试技巧

1. **添加调试输出**: 在控制结构前后添加 `?` 输出语句
2. **使用注释标记**: 在每个 `end` 后添加注释说明结束的控制结构
3. **逐步执行**: 将复杂脚本分解为小段逐步测试

### 参考现有错误模式
更多详细的错误示例和解决方案，请参阅本文档的 [## 常见错误模式](#常见错误模式) 章节。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 脚本控制流 |
| **MODE Solutions** | 完全支持 | 脚本控制流 |
| **DEVICE** | 完全支持 | 脚本控制流 |
| **INTERCONNECT** | 完全支持 | 脚本控制流 |

`end` 是 Lumerical 脚本语言的基本控制结构终止符，在所有产品中均可用。

## 相关命令

- [`if`](./if.md) - 条件语句开始
- [`for`](./for.md) - 循环语句开始
- [`while`](./while.md) - 循环语句开始
- [`function`](./function.md) - 函数定义开始
- [`switch`](./switch.md) - 开关语句开始

## 最佳实践

### 1. 一致的缩进
```lumerical
// 良好：一致的 2 空格缩进
if (condition) {
  for (i = 1:10) {
    if (sub_condition) {
      // 代码
    } end
  } end
} end

// 良好：一致的 4 空格缩进
if (condition) {
    for (i = 1:10) {
        if (sub_condition) {
            // 代码
        } end
    } end
} end
```

### 2. 注释复杂结构
```lumerical
// 复杂嵌套结构添加注释
if (global_condition) {  // 主要条件检查
    for (i = 1:num_iterations) {  // 主循环
        // 计算中间值
        intermediate = calculate(i);
        
        if (intermediate > threshold) {  // 阈值检查
            // 处理高值情况
            processHighValue(intermediate);
        } else {  // 低值情况
            // 处理低值情况
            processLowValue(intermediate);
        } end  // 结束阈值检查
        
    } end  // 结束主循环
    
    // 后处理
    postProcess();
} end  // 结束主要条件
```

### 3. 重构深层嵌套
```lumerical
// 重构前：深层嵌套
if (condition1) {
    if (condition2) {
        if (condition3) {
            if (condition4) {
                // 复杂代码
            } end
        } end
    } end
} end

// 重构后：使用函数和早期返回
function result = processConditions(c1, c2, c3, c4) {
    if (!c1) { return 0; } end
    if (!c2) { return 0; } end
    if (!c3) { return 0; } end
    if (!c4) { return 0; } end
    
    // 所有条件满足时的代码
    result = 1;
} end
```

## 调试技巧

### 1. 匹配检查
```lumerical
// 临时添加调试输出检查 end 匹配
?"开始 if 块";
if (condition) {
    ?"if 块内部";
    // 代码
} end
?"结束 if 块";

?"开始 for 循环";
for (i = 1:5) {
    ?"循环迭代: " + num2str(i);
    // 代码
} end
?"结束 for 循环";
```

### 2. 语法高亮
- 使用支持 Lumerical 脚本的编辑器
- 启用语法高亮以可视化代码结构
- 检查颜色编码的匹配开始/结束标记

### 3. 逐步执行
```lumerical
// 在复杂结构中添加逐步输出
for (outer = 1:3) {
    ?"外层循环: " + num2str(outer);
    
    for (inner = 1:3) {
        ?"  内层循环: " + num2str(inner);
        
        if (outer == inner) {
            ?"    条件满足: outer == inner";
            // 处理代码
        } else {
            ?"    条件不满足";
        } end  // if-else 结束
        
    } end  // 内层 for 结束
    
} end  // 外层 for 结束
```

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2025-01-31 | 初始版本 |
| 1.1 | 2025-02-01 | 增加最佳实践和调试技巧 |
| 1.2 | 2026-01-31 | 添加返回值、错误处理和参考章节，更新文档结构 |

## 常见错误模式

### 1. 缺少 end
```lumerical
// 错误：缺少 end
if (condition) {
    // 代码
// 缺少 } end

// 错误：缺少多个 end
for (i = 1:10) {
    if (condition) {
        // 代码
    // 缺少 } end for if
// 缺少 } end for for
```

### 2. 多余 end
```lumerical
// 错误：多余 end
if (condition) {
    // 代码
} end
} end  // 多余

// 错误：end 不匹配
if (condition) {
    // 代码
} end end  // 重复
```

### 3. 嵌套错误
```lumerical
// 错误：交叉嵌套
if (condition1) {
    for (i = 1:10) {
        // 代码
} end      // 错误：这个 end 应该结束 for，但前面没有匹配的 for
    // 代码
} end      // 错误：这个 end 没有匹配的 if
```

## 参考

1. Lumerical Script Language Reference - Control Structures
2. Lumerical Knowledge Base: Scripting Best Practices  
3. Lumerical Python API Documentation: Session.eval() Method
4. Python Official Documentation: Error Handling and Exceptions

---

*文档版本：1.2 | 最后更新：2026-01-31*