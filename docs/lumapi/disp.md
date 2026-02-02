# `disp` - 显示变量值

## 概述

`disp` 命令用于在 Lumerical 脚本环境中显示变量、表达式或文本的值。它是调试脚本、查看仿真结果和交互式探索数据的基本工具。该命令将内容输出到脚本编辑器输出窗口、MATLAB 命令窗口或 Python 控制台，具体取决于运行环境。

主要功能：
- **变量显示**：显示变量的值和属性
- **表达式求值**：计算并显示表达式的值
- **格式化输出**：控制输出的格式和精度
- **调试辅助**：在脚本中插入调试输出
- **结果查看**：查看仿真计算结果

典型应用：
- 调试脚本中的变量值
- 查看仿真参数和结果
- 格式化输出报告
- 交互式数据探索
- 验证计算正确性

## 语法

### LSF 语法
```lumerical
disp;                          # 显示空行
disp(value);                   # 显示值
disp(value1, value2, ...);     # 显示多个值
disp("text");                  # 显示文本
disp("text", value);           # 显示文本和值
disp("format", value);         # 格式化显示
```

### Python API
```python
session.disp()                          # 显示空行
session.disp(value)                     # 显示值
session.disp(value1, value2, ...)       # 显示多个值
session.disp("text")                    # 显示文本
session.disp("text", value)             # 显示文本和值
session.disp("format", value)           # 格式化显示
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `value` | any | 要显示的值（变量、表达式、常数等）。 | 可选 |
| `"text"` | string | 要显示的文本字符串。 | 可选 |
| `"format"` | string | 格式化字符串（如 "%.3f", "%e" 等）。 | 可选 |

## 配置属性

`disp` 命令通常不通过 `set` 命令配置属性，但可以通过以下方式控制输出：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `format` | string | "%g" | 数字显示格式。 |
| `precision` | number | 6 | 显示精度（小数位数）。 |
| `scientific` | bool | false | 是否使用科学计数法。 |
| `compact` | bool | true | 是否使用紧凑格式。 |
| `max display size` | number | 100 | 最大显示元素数（对于数组）。 |
| `display mode` | string | "auto" | 显示模式："auto", "full", "compact"。 |

## 返回值

`disp` 命令没有返回值。它主要用于在输出窗口中显示信息，不返回任何数据。在 Python API 中，`session.disp()` 返回 `None`。

## 错误处理

### 常见错误

1. **格式化字符串错误**
   ```python
   # 错误：格式化字符串不匹配
   fdtd.disp("值: %d", 3.14)  # %d 期望整数，但提供了浮点数
   ```
   解决方案：确保格式化字符串与值类型匹配。

2. **变量不存在错误**
   ```python
   # 错误：尝试显示不存在的变量
   fdtd.disp(nonexistent_var)
   ```
   解决方案：在显示前检查变量是否存在。

3. **输出缓冲区溢出**
   ```python
   # 错误：输出过大导致缓冲区溢出
   large_data = np.ones((1000, 1000))
   fdtd.disp(large_data)  # 可能产生大量输出
   ```
   解决方案：限制输出大小，或使用摘要模式显示。

### Python 错误处理示例
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 正常显示
    fdtd.disp("正常输出")
    
    # 尝试格式化错误
    fdtd.disp("值: %d", 3.14)
    
except lumapi.LumApiError as e:
    error_str = str(e).lower()
    
    if "format" in error_str or "%" in error_str:
        print("错误: 格式化字符串不匹配")
    elif "variable" in error_str or "name" in error_str:
        print("错误: 变量不存在")
    elif "buffer" in error_str or "overflow" in error_str:
        print("警告: 输出缓冲区受限")
    else:
        print(f"Lumerical API 错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 使用示例

### 示例 1：基本显示功能

#### LSF 脚本
```lumerical
# 基本显示功能演示
?echo("基本显示功能演示...");

# 显示空行（分隔输出）
disp;
?echo("空行显示完成");

# 显示文本
disp("=== 仿真参数设置 ===");
disp("开始仿真配置...");

# 显示变量
wavelength = 1.55;
disp("波长:", wavelength, "μm");

# 显示多个值
x = 1.0;
y = 2.0;
z = 3.0;
disp("位置坐标:", x, y, z);

# 显示表达式结果
area = x * y;
disp("面积计算:", x, "*", y, "=", area);

# 显示数组
array_data = [1.0, 2.0, 3.0, 4.0, 5.0];
disp("数组数据:", array_data);

# 显示矩阵
matrix = matrix(3,3);
for (i=1:3) {
    for (j=1:3) {
        matrix(i,j) = i*j;
    }
}
disp("矩阵:");
disp(matrix);

# 显示布尔值
simulation_complete = 1;  # 1 表示 true
disp("仿真状态:", "完成");

# 显示空值
disp("空值:", "");
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本显示功能演示...")

# 显示空行（分隔输出）
fdtd.disp()
print("空行显示完成")

# 显示文本
fdtd.disp("=== 仿真参数设置 ===")
fdtd.disp("开始仿真配置...")

# 显示变量
wavelength = 1.55
fdtd.disp("波长:", wavelength, "μm")

# 显示多个值
x = 1.0
y = 2.0
z = 3.0
fdtd.disp("位置坐标:", x, y, z)

# 显示表达式结果
area = x * y
fdtd.disp("面积计算:", x, "*", y, "=", area)

# 显示数组
array_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
fdtd.disp("数组数据:", array_data)

# 显示矩阵
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
fdtd.disp("矩阵:")
fdtd.disp(matrix)

# 显示布尔值
simulation_complete = True
fdtd.disp("仿真状态:", "完成" if simulation_complete else "进行中")

# 显示 None/空值
empty_value = None
fdtd.disp("空值:", empty_value)
```

### 示例 2：格式化输出

#### LSF 脚本
```lumerical
# 格式化输出演示
?echo("格式化输出演示...");

# 创建测试数据
wavelength = 1.55023;
power = 0.00123456;
efficiency = 0.87654321;
temperature = 298.15;
error_value = 0.0000123456;

# 基本格式化
?echo("基本格式化:");
disp("波长: " + num2str(wavelength, 3) + " μm");
disp("功率: " + num2str(power, 2, 'e') + " W");
disp("效率: " + num2str(efficiency * 100, 1) + "%");

# 多值格式化
?echo("多值格式化:");
disp("参数: λ=" + num2str(wavelength, 3) + " μm, P=" + num2str(power, 2, 'e') + " W, η=" + num2str(efficiency * 100, 1) + "%");

# 控制精度
?echo("不同精度:");
for (precision=[1, 3, 6, 9]) {
    disp("精度 " + num2str(precision) + ": " + num2str(wavelength, precision));
}

# 科学计数法
?echo("科学计数法:");
disp("标准: " + num2str(error_value));
disp("科学: " + num2str(error_value, 6, 'e'));
disp("自动: " + num2str(error_value, 6, 'g'));

# 对齐和宽度
?echo("对齐和宽度:");
values = [1.23, 45.678, 0.123456];
for (i=1:length(values)) {
    val = values(i);
    # LSF 中没有直接的宽度控制，但可以手动填充
    disp("值: " + num2str(val, 3));
}

# 显示表格数据
?echo("表格数据:");
disp("参数表:");
disp("名称       单位    值        误差");
disp("----------------------------------------");

parameters = {
    {"波长", "μm", 1.55, 0.01},
    {"功率", "W", 0.001, 0.0001},
    {"效率", "%", 87.65, 0.5},
    {"温度", "K", 298.15, 0.1}
};

for (i=1:length(parameters)) {
    param = parameters{i};
    name = param{1};
    unit = param{2};
    value = param{3};
    error = param{4};
    
    # 构建格式化字符串
    if (unit == "%") {
        display_value = value;
    } else {
        display_value = value;
    }
    
    disp(name + "        " + unit + "    " + num2str(display_value, 3) + "    ±" + num2str(error, 3));
}
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("格式化输出演示...")

# 创建测试数据
data = {
    'wavelength': 1.55023,
    'power': 0.00123456,
    'efficiency': 0.87654321,
    'temperature': 298.15,
    'error': 0.0000123456
}

# 基本格式化
print("\n基本格式化:")
fdtd.disp("波长: %.3f μm" % data['wavelength'])
fdtd.disp("功率: %.2e W" % data['power'])
fdtd.disp("效率: %.1f%%" % (data['efficiency'] * 100))

# 多值格式化
print("\n多值格式化:")
fdtd.disp("参数: λ=%.3f μm, P=%.2e W, η=%.1f%%" % 
         (data['wavelength'], data['power'], data['efficiency'] * 100))

# 控制精度
print("\n不同精度:")
for precision in [1, 3, 6, 9]:
    fdtd.disp(f"精度 {precision}: %.{precision}f" % data['wavelength'])

# 科学计数法
print("\n科学计数法:")
fdtd.disp("标准: %f" % data['error'])
fdtd.disp("科学: %e" % data['error'])
fdtd.disp("自动: %g" % data['error'])

# 对齐和宽度
print("\n对齐和宽度:")
values = [1.23, 45.678, 0.123456]
for val in values:
    fdtd.disp("值: %8.3f" % val)  # 宽度8，精度3

# 显示表格数据
print("\n表格数据:")
parameters = [
    ("波长", "μm", 1.55, 0.01),
    ("功率", "W", 0.001, 0.0001),
    ("效率", "%", 87.65, 0.5),
    ("温度", "K", 298.15, 0.1)
]

fdtd.disp("参数表:")
fdtd.disp("名称       单位    值        误差")
fdtd.disp("-" * 40)

for name, unit, value, error in parameters:
    if unit == "%":
        display_value = value
    else:
        display_value = value
    
    fdtd.disp(f"{name:10} {unit:4} {display_value:8.3f}  ±{error:.3f}")

# 复杂数据结构
print("\n复杂数据结构:")
simulation_config = {
    'general': {
        'simulation_time': 1000,
        'mesh_accuracy': 2,
        'boundary_conditions': 'PML'
    },
    'geometry': {
        'width': 0.5,
        'height': 0.22,
        'length': 10.0
    },
    'materials': ['Si', 'SiO2', 'Air'],
    'monitors': ['power', 'field', 'index']
}

fdtd.disp("仿真配置:")
for category, config in simulation_config.items():
    fdtd.disp(f"  {category}: {config}")
```

### 示例 3：调试和验证
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("调试和验证演示...")

class SimulationDebugger:
    """仿真调试工具"""
    
    def __init__(self, session, verbose=True):
        self.session = session
        self.verbose = verbose
        self.debug_history = []
    
    def log(self, message, *args, level="INFO"):
        """记录日志消息"""
        
        timestamp = np.datetime64('now')
        log_entry = {
            'timestamp': timestamp,
            'level': level,
            'message': message,
            'args': args
        }
        
        self.debug_history.append(log_entry)
        
        if self.verbose:
            # 添加级别前缀
            if level == "ERROR":
                prefix = "[ERROR] "
            elif level == "WARNING":
                prefix = "[WARN]  "
            elif level == "DEBUG":
                prefix = "[DEBUG] "
            else:
                prefix = "[INFO]  "
            
            # 构建完整消息
            full_message = prefix + message
            if args:
                full_message += " " + " ".join(str(arg) for arg in args)
            
            self.session.disp(full_message)
    
    def display_variable(self, var_name, description=None):
        """显示变量值"""
        
        try:
            # 获取变量值
            value = self.session.get(var_name)
            
            if description:
                self.log(f"{description}: {var_name} = {value}")
            else:
                self.log(f"{var_name} = {value}")
            
            return value
        except Exception as e:
            self.log(f"无法获取变量 {var_name}: {e}", level="ERROR")
            return None
    
    def check_condition(self, condition, message):
        """检查条件并显示结果"""
        
        result = bool(condition)
        status = "通过" if result else "失败"
        
        self.log(f"检查: {message} - {status}", 
                level="DEBUG" if result else "WARNING")
        
        return result
    
    def display_array_info(self, array_name):
        """显示数组信息"""
        
        try:
            array = self.session.get(array_name)
            
            if isinstance(array, np.ndarray):
                self.log(f"数组 '{array_name}':")
                self.log(f"  形状: {array.shape}")
                self.log(f"  数据类型: {array.dtype}")
                self.log(f"  大小: {array.size}")
                self.log(f"  最小值: {np.min(array):.6g}")
                self.log(f"  最大值: {np.max(array):.6g}")
                self.log(f"  平均值: {np.mean(array):.6g}")
                self.log(f"  标准差: {np.std(array):.6g}")
                
                # 显示部分数据（防止过大数组）
                if array.size <= 10:
                    self.log(f"  数据: {array}")
                else:
                    self.log(f"  前5个元素: {array.flat[:5]}")
                    self.log(f"  后5个元素: {array.flat[-5:]}")
            else:
                self.log(f"'{array_name}' 不是数组: {type(array)}")
                
        except Exception as e:
            self.log(f"无法分析数组 {array_name}: {e}", level="ERROR")
    
    def compare_variables(self, var1_name, var2_name, tolerance=1e-6):
        """比较两个变量"""
        
        try:
            var1 = self.session.get(var1_name)
            var2 = self.session.get(var2_name)
            
            self.log(f"比较: {var1_name} vs {var2_name}")
            
            if isinstance(var1, np.ndarray) and isinstance(var2, np.ndarray):
                # 数组比较
                if var1.shape != var2.shape:
                    self.log(f"  形状不同: {var1.shape} != {var2.shape}", 
                            level="ERROR")
                    return False
                
                diff = np.abs(var1 - var2)
                max_diff = np.max(diff)
                avg_diff = np.mean(diff)
                
                self.log(f"  最大差异: {max_diff:.6g}")
                self.log(f"  平均差异: {avg_diff:.6g}")
                
                if max_diff < tolerance:
                    self.log(f"  在容差范围内 (±{tolerance})", level="DEBUG")
                    return True
                else:
                    self.log(f"  超出容差范围", level="WARNING")
                    return False
            else:
                # 标量比较
                diff = abs(var1 - var2)
                self.log(f"  差异: {diff:.6g}")
                
                if diff < tolerance:
                    self.log(f"  在容差范围内 (±{tolerance})", level="DEBUG")
                    return True
                else:
                    self.log(f"  超出容差范围", level="WARNING")
                    return False
                    
        except Exception as e:
            self.log(f"比较失败: {e}", level="ERROR")
            return False
    
    def display_summary(self):
        """显示调试摘要"""
        
        self.log("=" * 50)
        self.log("调试摘要")
        self.log("=" * 50)
        
        # 统计各级别消息
        levels = {}
        for entry in self.debug_history:
            level = entry['level']
            levels[level] = levels.get(level, 0) + 1
        
        self.log(f"总日志条目: {len(self.debug_history)}")
        for level, count in levels.items():
            self.log(f"  {level}: {count}")
        
        # 显示最后几条消息
        self.log("\n最近消息:")
        for entry in self.debug_history[-5:]:
            time_str = str(entry['timestamp'])[11:19]  # 提取时间部分
            self.log(f"  {time_str} {entry['level']}: {entry['message']}")

# 使用调试器
print("创建调试器...")
debugger = SimulationDebugger(fdtd, verbose=True)

# 创建测试变量
fdtd.eval("test_scalar = 3.14159;")
fdtd.eval("test_array = linspace(0, 10, 11);")
fdtd.eval("test_matrix = matrix(3,3); for(i=1:3){for(j=1:3){test_matrix(i,j)=i*j;}};")

# 显示变量
debugger.log("开始变量检查")
debugger.display_variable("test_scalar", "测试标量")
debugger.display_variable("test_array", "测试数组")
debugger.display_variable("test_matrix", "测试矩阵")

# 检查条件
debugger.check_condition(3.14 < 3.14159 < 3.142, "π值范围检查")
debugger.check_condition(len(fdtd.get("test_array")) == 11, "数组长度检查")

# 显示数组信息
debugger.display_array_info("test_array")
debugger.display_array_info("test_matrix")

# 创建比较变量
fdtd.eval("test_copy = test_scalar;")
fdtd.eval("test_array2 = test_array + 0.001;")

# 比较变量
debugger.compare_variables("test_scalar", "test_copy", tolerance=1e-10)
debugger.compare_variables("test_array", "test_array2", tolerance=0.001)

# 显示摘要
debugger.display_summary()

# 错误处理测试
debugger.display_variable("non_existent_variable")
debugger.compare_variables("test_scalar", "non_existent_variable")
```

### 示例 4：仿真结果报告
```python
import lumapi
import numpy as np
from datetime import datetime

fdtd = lumapi.FDTD()

print("仿真结果报告演示...")

class SimulationReporter:
    """仿真结果报告工具"""
    
    def __init__(self, session):
        self.session = session
        self.report_data = {}
        self.start_time = datetime.now()
    
    def add_section(self, title):
        """添加报告章节"""
        
        self.session.disp()
        self.session.disp("=" * 60)
        self.session.disp(f"  {title}")
        self.session.disp("=" * 60)
        self.session.disp()
        
        if title not in self.report_data:
            self.report_data[title] = {}
    
    def add_parameter(self, section, name, value, unit="", format_spec="%g"):
        """添加参数到报告"""
        
        if section not in self.report_data:
            self.report_data[section] = {}
        
        # 格式化值
        if isinstance(value, (int, np.integer)):
            formatted = f"{value}"
        elif isinstance(value, (float, np.floating)):
            formatted = format_spec % value
        else:
            formatted = str(value)
        
        # 添加单位
        if unit:
            display_value = f"{formatted} {unit}"
        else:
            display_value = formatted
        
        # 存储并显示
        self.report_data[section][name] = {
            'value': value,
            'display': display_value,
            'unit': unit
        }
        
        self.session.disp(f"{name:20}: {display_value}")
    
    def add_table(self, section, table_name, headers, rows, formats=None):
        """添加表格到报告"""
        
        if section not in self.report_data:
            self.report_data[section] = {}
        
        self.session.disp()
        self.session.disp(f"{table_name}:")
        
        # 确定列宽
        col_widths = []
        for i, header in enumerate(headers):
            # 初始宽度基于标题
            width = len(str(header))
            
            # 检查数据行
            for row in rows:
                if i < len(row):
                    cell_len = len(str(row[i]))
                    width = max(width, cell_len)
            
            col_widths.append(width + 2)  # 加一些填充
        
        # 打印标题
        header_line = ""
        for i, header in enumerate(headers):
            header_line += f"{header:{col_widths[i]}}"
        self.session.disp(header_line)
        
        # 打印分隔线
        separator = "-" * sum(col_widths)
        self.session.disp(separator)
        
        # 打印数据行
        for row in rows:
            row_line = ""
            for i, cell in enumerate(row):
                if formats and i < len(formats):
                    # 应用格式化
                    if isinstance(cell, (int, np.integer)):
                        formatted = str(cell)
                    elif isinstance(cell, (float, np.floating)):
                        formatted = formats[i] % cell
                    else:
                        formatted = str(cell)
                else:
                    formatted = str(cell)
                
                row_line += f"{formatted:{col_widths[i]}}"
            
            self.session.disp(row_line)
        
        # 存储表格数据
        self.report_data[section][table_name] = {
            'headers': headers,
            'rows': rows,
            'formats': formats
        }
    
    def add_analysis(self, section, analysis_name, data, analysis_func):
        """添加分析结果"""
        
        if section not in self.report_data:
            self.report_data[section] = {}
        
        self.session.disp()
        self.session.disp(f"{analysis_name}:")
        
        # 执行分析
        results = analysis_func(data)
        
        # 显示结果
        for key, value in results.items():
            if isinstance(value, (int, np.integer)):
                display = f"{value}"
            elif isinstance(value, (float, np.floating)):
                display = f"{value:.6g}"
            else:
                display = str(value)
            
            self.session.disp(f"  {key:15}: {display}")
        
        # 存储分析结果
        self.report_data[section][analysis_name] = results
    
    def generate_summary(self):
        """生成报告摘要"""
        
        self.add_section("仿真摘要")
        
        # 计算运行时间
        end_time = datetime.now()
        run_time = end_time - self.start_time
        
        self.add_parameter("仿真摘要", "开始时间", 
                          self.start_time.strftime("%Y-%m-%d %H:%M:%S"))
        self.add_parameter("仿真摘要", "结束时间", 
                          end_time.strftime("%Y-%m-%d %H:%M:%S"))
        self.add_parameter("仿真摘要", "运行时间", 
                          str(run_time).split('.')[0])  # 移除微秒部分
        
        # 统计报告内容
        total_sections = len(self.report_data)
        total_parameters = 0
        total_tables = 0
        total_analyses = 0
        
        for section, content in self.report_data.items():
            for key, value in content.items():
                if isinstance(value, dict):
                    if 'headers' in value:
                        total_tables += 1
                    elif 'value' in value:
                        total_parameters += 1
                    else:
                        total_analyses += 1
        
        self.add_parameter("仿真摘要", "报告章节", total_sections)
        self.add_parameter("仿真摘要", "参数数量", total_parameters)
        self.add_parameter("仿真摘要", "表格数量", total_tables)
        self.add_parameter("仿真摘要", "分析数量", total_analyses)
        
        # 显示各章节概览
        self.session.disp()
        self.session.disp("报告章节概览:")
        for section in self.report_data.keys():
            item_count = len(self.report_data[section])
            self.session.disp(f"  {section:20}: {item_count} 个项目")
    
    def save_report(self, filename):
        """保存报告到文件（概念性）"""
        
        self.session.disp()
        self.session.disp(f"报告已保存到: {filename}")
        self.session.disp("（在实际实现中，这里会将报告写入文件）")

# 使用报告器
print("创建仿真报告器...")
reporter = SimulationReporter(fdtd)

# 添加仿真设置章节
reporter.add_section("仿真设置")

reporter.add_parameter("仿真设置", "仿真类型", "FDTD", "")
reporter.add_parameter("仿真设置", "网格精度", 2, "")
reporter.add_parameter("仿真设置", "边界条件", "PML", "")
reporter.add_parameter("仿真设置", "仿真时间", 1000, "fs")
reporter.add_parameter("仿真设置", "波长", 1.55, "μm")

# 添加几何参数表格
reporter.add_section("几何参数")

geometry_headers = ["部件", "材料", "宽度(μm)", "高度(μm)", "长度(μm)"]
geometry_rows = [
    ["波导核心", "Si", 0.5, 0.22, 10.0],
    ["上包层", "SiO2", 2.0, 1.0, 10.0],
    ["下包层", "SiO2", 2.0, 1.0, 10.0],
    ["侧包层", "Air", 1.0, 0.22, 10.0]
]
geometry_formats = ["%s", "%s", "%.2f", "%.2f", "%.1f"]

reporter.add_table("几何参数", "几何结构", geometry_headers, 
                  geometry_rows, geometry_formats)

# 添加材料参数
reporter.add_section("材料参数")

material_headers = ["材料", "折射率@1.55μm", "损耗(dB/cm)", "温度系数(/K)"]
material_rows = [
    ["Si", 3.476, 0.5, 1.8e-4],
    ["SiO2", 1.444, 0.01, 1.0e-5],
    ["Air", 1.000, 0.0, 0.0]
]
material_formats = ["%s", "%.3f", "%.2f", "%.1e"]

reporter.add_table("材料参数", "材料属性", material_headers, 
                  material_rows, material_formats)

# 添加光源设置
reporter.add_section("光源设置")

reporter.add_parameter("光源设置", "光源类型", "模式源", "")
reporter.add_parameter("光源设置", "注入模式", "TE0", "")
reporter.add_parameter("光源设置", "中心波长", 1.55, "μm")
reporter.add_parameter("光源设置", "波长范围", 0.1, "μm")
reporter.add_parameter("光源设置", "功率", 0.001, "W")

# 添加监视器设置
reporter.add_section("监视器设置")

monitor_headers = ["监视器", "类型", "位置(μm)", "尺寸(μm)", "数据点"]
monitor_rows = [
    ["频域监视器1", "2D", "(0,0,0)", "(2,2,0)", "100x100"],
    ["频域监视器2", "2D", "(5,0,0)", "(2,2,0)", "100x100"],
    ["时域监视器", "点", "(2.5,0,0)", "N/A", "1000"],
    ["模式扩展", "线", "(0,-1,0) to (0,1,0)", "N/A", "200"]
]

reporter.add_table("监视器设置", "监视器配置", monitor_headers, monitor_rows)

# 添加仿真结果（模拟数据）
reporter.add_section("仿真结果")

# 模拟一些结果数据
simulation_data = {
    'transmission': 0.8765,
    'reflection': 0.1234,
    'loss': 0.0001,
    'efficiency': 87.65,
    'Q_factor': 12500,
    'mode_area': 0.15,
    'group_index': 4.23
}

def analyze_simulation(data):
    """分析仿真数据"""
    
    results = {}
    
    # 基本指标
    results['传输效率'] = data['transmission']
    results['反射率'] = data['reflection']
    results['损耗'] = data['loss']
    results['总效率'] = data['efficiency']
    
    # 派生指标
    results['插入损耗'] = -10 * np.log10(data['transmission'])
    results['回波损耗'] = -10 * np.log10(data['reflection'])
    results['消光比'] = 10 * np.log10(data['transmission'] / data['reflection'])
    
    # 品质因子相关
    results['品质因子Q'] = data['Q_factor']
    results['光子寿命'] = data['Q_factor'] * 1.55 / (2 * np.pi * 300)  # 简化计算
    
    # 模式特性
    results['模式面积'] = data['mode_area']
    results['群折射率'] = data['group_index']
    results['有效折射率'] = 2.95  # 假设值
    
    return results

reporter.add_analysis("仿真结果", "性能指标", simulation_data, analyze_simulation)

# 添加性能评估表格
reporter.add_section("性能评估")

performance_headers = ["指标", "值", "单位", "目标", "状态"]
performance_rows = [
    ["传输效率", 87.65, "%", ">85%", "✓ 达标"],
    ["插入损耗", 0.57, "dB", "<1.0dB", "✓ 达标"],
    ["回波损耗", 9.08, "dB", ">10dB", "⚠️ 接近"],
    ["消光比", 8.51, "dB", ">8dB", "✓ 达标"],
    ["品质因子", 12500, "", ">10000", "✓ 达标"],
    ["模式面积", 0.15, "μm²", "<0.2μm²", "✓ 达标"]
]

reporter.add_table("性能评估", "性能指标", performance_headers, performance_rows)

# 生成摘要
reporter.generate_summary()

# 保存报告
reporter.save_report("simulation_report.txt")

print("\n仿真报告生成完成!")
```

### 示例 5：高级显示和可视化工具
```python
import lumapi
import numpy as np
import textwrap

fdtd = lumapi.FDTD()

print("高级显示和可视化工具演示...")

class AdvancedDisplay:
    """高级显示工具"""
    
    def __init__(self, session):
        self.session = session
    
    def display_progress_bar(self, iteration, total, prefix='', suffix='', 
                            length=50, fill='█'):
        """显示进度条"""
        
        percent = 100 * (iteration / float(total))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        
        # 构建进度条字符串
        progress_str = f'\r{prefix} |{bar}| {percent:.1f}% {suffix}'
        
        # 使用 disp 显示（注意：可能需要特殊处理回车符）
        # 在实际控制台中，\r 会回到行首
        self.session.disp(progress_str, newline=False)
        
        # 完成后换行
        if iteration == total:
            self.session.disp()
    
    def display_matrix_pretty(self, matrix, title="", precision=4, max_rows=10, max_cols=10):
        """漂亮地显示矩阵"""
        
        self.session.disp()
        if title:
            self.session.disp(f"{title}:")
        
        # 转换为 numpy 数组（如果还不是）
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        
        # 获取矩阵形状
        rows, cols = matrix.shape
        
        # 限制显示大小
        display_rows = min(rows, max_rows)
        display_cols = min(cols, max_cols)
        
        # 构建格式字符串
        if np.iscomplexobj(matrix):
            # 复数矩阵
            format_str = f"{{:>{precision+8}.{precision}f}}"
        else:
            # 实数矩阵
            format_str = f"{{:>{precision+4}.{precision}f}}"
        
        # 显示列号
        col_header = "     " + " ".join(f"{j+1:>{precision+4}}" 
                                       for j in range(display_cols))
        self.session.disp(col_header)
        
        # 显示分隔线
        separator = "    " + "-" * (display_cols * (precision+5))
        self.session.disp(separator)
        
        # 显示数据行
        for i in range(display_rows):
            row_str = f"{i+1:3} |"
            for j in range(display_cols):
                value = matrix[i, j]
                
                if np.iscomplexobj(value):
                    # 复数：显示实部和虚部
                    real_part = format_str.format(value.real)
                    imag_part = format_str.format(value.imag)
                    cell_str = f"{real_part}+{imag_part}j"
                else:
                    # 实数
                    cell_str = format_str.format(value)
                
                row_str += " " + cell_str
            
            # 如果被截断，添加指示符
            if display_cols < cols:
                row_str += " ..."
            
            self.session.disp(row_str)
        
        # 如果行被截断，添加指示符
        if display_rows < rows:
            self.session.disp("   ...")
        
        # 显示统计信息
        self.session.disp()
        self.session.disp(f"矩阵大小: {rows} × {cols}")
        if rows > 0 and cols > 0:
            self.session.disp(f"最小值: {np.min(matrix):.{precision}f}")
            self.session.disp(f"最大值: {np.max(matrix):.{precision}f}")
            self.session.disp(f"平均值: {np.mean(matrix):.{precision}f}")
            self.session.disp(f"条件数: {np.linalg.cond(matrix):.{precision}g}")
    
    def display_text_box(self, text, title="", width=60, border_char="#"):
        """在文本框中显示文本"""
        
        self.session.disp()
        
        # 创建边框
        border = border_char * width
        
        # 显示上边框
        self.session.disp(border)
        
        # 显示标题（如果提供）
        if title:
            title_line = border_char + " " + title.center(width-4) + " " + border_char
            self.session.disp(title_line)
            self.session.disp(border)
        
        # 换行显示文本
        wrapped_lines = textwrap.wrap(text, width=width-4)
        
        for line in wrapped_lines:
            padded_line = border_char + " " + line.ljust(width-4) + " " + border_char
            self.session.disp(padded_line)
        
        # 显示下边框
        self.session.disp(border)
    
    def display_tree(self, data, indent=0, max_depth=3, current_depth=0):
        """树状显示数据结构"""
        
        if current_depth >= max_depth:
            self.session.disp("  " * indent + "...")
            return
        
        if isinstance(data, dict):
            for key, value in data.items():
                self.session.disp("  " * indent + f"├─ {key}:")
                
                if isinstance(value, (dict, list, tuple)):
                    self.display_tree(value, indent+2, max_depth, current_depth+1)
                else:
                    self.session.disp("  " * (indent+2) + f"└─ {value}")
        elif isinstance(data, (list, tuple)):
            for i, item in enumerate(data):
                if i == len(data) - 1:
                    prefix = "└─"
                else:
                    prefix = "├─"
                
                self.session.disp("  " * indent + f"{prefix} [{i}]:")
                
                if isinstance(item, (dict, list, tuple)):
                    self.display_tree(item, indent+2, max_depth, current_depth+1)
                else:
                    self.session.disp("  " * (indent+2) + f"└─ {item}")
        else:
            self.session.disp("  " * indent + f"└─ {data}")
    
    def display_comparison_chart(self, data1, data2, labels=None, 
                                chart_width=50, title=""):
        """显示比较图表"""
        
        self.session.disp()
        if title:
            self.session.disp(title)
        
        # 确定数据对
        if labels is None:
            if isinstance(data1, dict) and isinstance(data2, dict):
                labels = list(data1.keys())
                values1 = list(data1.values())
                values2 = list(data2.values())
            else:
                labels = [f"项{i+1}" for i in range(len(data1))]
                values1 = data1
                values2 = data2
        
        # 找到最大值用于归一化
        all_values = list(values1) + list(values2)
        max_value = max(all_values) if all_values else 1
        
        # 显示图表
        for i, (label, val1, val2) in enumerate(zip(labels, values1, values2)):
            # 计算条形长度
            bar1_len = int(chart_width * val1 / max_value)
            bar2_len = int(chart_width * val2 / max_value)
            
            # 创建条形
            bar1 = "█" * bar1_len
            bar2 = "░" * bar2_len
            
            # 显示
            row = f"{label:15} | {bar1:<{chart_width}} | {val1:.3f}"
            self.session.disp(row)
            
            row = f"{'':15} | {bar2:<{chart_width}} | {val2:.3f}"
            self.session.disp(row)
            
            # 显示差异（如果不是最后一行）
            if i < len(labels) - 1:
                diff = val1 - val2
                diff_str = f"差异: {diff:+.3f}"
                self.session.disp(f"{'':15}   {diff_str:^{chart_width}}")
                self.session.disp()  # 空行分隔
    
    def display_color_coded(self, values, thresholds, colors=None, title=""):
        """颜色编码显示数值"""
        
        if colors is None:
            colors = {
                'low': '\033[92m',    # 绿色
                'medium': '\033[93m', # 黄色
                'high': '\033[91m',   # 红色
                'reset': '\033[0m'    # 重置
            }
        
        self.session.disp()
        if title:
            self.session.disp(title)
        
        low_thresh, high_thresh = thresholds
        
        for i, value in enumerate(values):
            # 确定颜色
            if value < low_thresh:
                color = colors['low']
                level = "低"
            elif value < high_thresh:
                color = colors['medium']
                level = "中"
            else:
                color = colors['high']
                level = "高"
            
            # 构建显示字符串
            # 注意：颜色代码在 Lumerical 中可能不起作用，这里作为概念展示
            display_str = f"{color}[{level}] {value:.4f}{colors['reset']}"
            self.session.disp(f"值 {i+1}: {display_str}")

# 使用高级显示工具
print("创建高级显示工具...")
display = AdvancedDisplay(fdtd)

# 进度条演示
print("\n进度条演示:")
total_steps = 20
for i in range(total_steps + 1):
    display.display_progress_bar(i, total_steps, 
                                prefix='进度:', 
                                suffix=f'完成 {i}/{total_steps}',
                                length=30)
    # 模拟耗时操作
    import time
    time.sleep(0.05)

# 矩阵显示演示
print("\n矩阵显示演示:")
# 创建测试矩阵
test_matrix = np.array([[1.234567, 2.345678, 3.456789],
                        [4.567890, 5.678901, 6.789012],
                        [7.890123, 8.901234, 9.012345]])

complex_matrix = test_matrix + 0.1j * test_matrix

display.display_matrix_pretty(test_matrix, "实数矩阵", precision=3)
display.display_matrix_pretty(complex_matrix, "复数矩阵", precision=2)

# 大矩阵显示（截断）
big_matrix = np.random.rand(15, 8)
display.display_matrix_pretty(big_matrix, "大矩阵（截断显示）", 
                             precision=2, max_rows=5, max_cols=4)

# 文本框演示
print("\n文本框演示:")
lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
"""

display.display_text_box(lorem_ipsum, "示例文本", width=50)
display.display_text_box("重要警告：仿真参数超出推荐范围！", 
                        "警告", width=40, border_char="!")

# 树状结构演示
print("\n树状结构演示:")
simulation_structure = {
    'FDTD仿真': {
        '设置': {
            '网格精度': 2,
            '边界条件': 'PML',
            '仿真时间': '1000fs'
        },
        '几何': {
            '波导': {
                '材料': 'Si',
                '尺寸': '0.5x0.22μm'
            },
            '包层': ['SiO2', 'Air']
        },
        '光源': [
            {'类型': '模式源', '波长': '1.55μm'},
            {'类型': '偶极子', '位置': '(0,0,0)'}
        ]
    }
}

display.display_tree(simulation_structure, max_depth=4)

# 比较图表演示
print("\n比较图表演示:")
data1 = {'传输': 0.85, '反射': 0.10, '损耗': 0.05, '效率': 0.95}
data2 = {'传输': 0.92, '反射': 0.05, '损耗': 0.03, '效率': 0.98}

display.display_comparison_chart(data1, data2, 
                                title="仿真结果比较")

# 数组比较
array1 = [0.1, 0.3, 0.5, 0.7, 0.9]
array2 = [0.15, 0.25, 0.55, 0.65, 0.95]

display.display_comparison_chart(array1, array2,
                                labels=['点1', '点2', '点3', '点4', '点5'],
                                title="数组值比较")

# 颜色编码显示
print("\n颜色编码显示:")
test_values = [0.1, 0.4, 0.7, 0.9, 1.2]
display.display_color_coded(test_values, thresholds=(0.3, 0.8),
                           title="阈值分析")

print("\n高级显示演示完成!")
```

## 注意事项

1. **输出位置**：`disp` 的输出位置取决于运行环境（Lumerical 脚本编辑器、MATLAB、Python 等）。

2. **性能影响**：在循环中大量使用 `disp` 可能影响脚本性能。对于生产代码，考虑减少输出或使用日志级别控制。

3. **格式化兼容性**：格式化字符串的语法可能因 Lumerical 版本和运行环境而异。

4. **数组显示**：对于大型数组，`disp` 可能只显示部分内容以防止输出过载。

5. **特殊字符**：某些特殊字符（如颜色代码、Unicode）可能在某些环境中不被支持。

6. **实时更新**：在长时间运行的脚本中，`disp` 输出可能不会实时显示，具体取决于缓冲设置。

7. **错误处理**：`disp` 命令本身通常不会引发错误，但格式化错误的值可能导致意外输出。

8. **与 `echo` 的区别**：`echo` 命令也用于输出，但语义可能略有不同。`disp` 通常更侧重于显示值，而 `echo` 更侧重于输出文本。

9. **输出重定向**：在某些环境中，`disp` 输出可以被重定向到文件或其他输出流。

10. **国际化**：对于多语言支持，注意文本编码和本地化设置。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有脚本环境 |
| MODE Solutions | ✅ 完全支持 | 所有脚本环境 |
| DEVICE | ✅ 完全支持 | 所有脚本环境 |
| INTERCONNECT | ✅ 完全支持 | 所有脚本环境 |

## 相关命令

- [echo](./echo.md) - 回显文本（功能相似）
- [printf](./printf.md) - 格式化输出（类似 C 语言的 printf）
- [sprintf](./sprintf.md) - 格式化字符串（不直接输出）
- [fprintf](./fprintf.md) - 格式化输出到文件
- [write](./write.md) - 写入数据到文件
- [get](./get.md) - 获取变量值（常用于 `disp` 的参数）
- [eval](./eval.md) - 执行表达式（结果可用于 `disp`）
- [clear](./clear.md) - 清除输出窗口
- [clc](./clc.md) - 清除命令窗口（MATLAB 风格）

## 版本历史

| 版本 | 修改 |
|------|------|
| 1.0 | 初始版本，包含基本语法、参数、示例和注意事项 |
| 1.1 | 添加返回值、错误处理章节、LSF脚本示例、版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - disp 命令
2. Lumerical Python API Documentation - session.disp() 方法
3. Lumerical Scripting Guide - 输出和调试技巧

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*