# `echo` - 回显文本

## 概述

`echo` 命令用于在 Lumerical 脚本窗口、输出面板或日志文件中输出文本信息。它是脚本调试、状态报告和用户交互的基本工具，类似于其他编程语言中的 `print` 或 `printf` 函数。

主要功能：
- **文本输出**：向脚本窗口输出文本消息
- **变量显示**：显示变量值和表达式结果
- **调试输出**：输出调试信息和脚本状态
- **进度报告**：在长时间运行脚本中报告进度
- **日志记录**：创建脚本执行日志
- **格式化输出**：支持格式化字符串和数值

典型应用：
- 脚本调试和状态跟踪
- 计算结果输出和验证
- 用户提示和交互
- 脚本执行日志记录
- 进度指示和估计
- 错误和警告消息
- 数据导出前的预览

## 语法

### LSF 语法
```lumerical
echo;                      # 输出空行
echo("message");           # 输出字符串
echo("format", arg1, arg2); # 格式化输出
echo(variable);            # 输出变量值
echo(expression);          # 输出表达式结果
```

### Python API
```python
session.echo()                      # 输出空行
session.echo("message")             # 输出字符串
session.echo("format", arg1, arg2)  # 格式化输出
session.echo(variable)              # 输出变量值
session.echo(expression)            # 输出表达式结果
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `message` | string | 要输出的文本消息。 | 否 |
| `format` | string | 格式化字符串（类似 C 语言的 printf）。 | 否 |
| `arg1`, `arg2`, ... | any | 格式化字符串的参数。 | 否 |
| `variable` | any | 要输出的变量或表达式。 | 否 |

## 配置属性

`echo` 命令本身没有可配置属性，但输出行为受以下相关设置影响：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `echo to script window` | bool | true | 是否输出到脚本窗口。 |
| `echo to output window` | bool | true | 是否输出到输出面板。 |
| `echo to file` | bool | false | 是否输出到文件。 |
| `echo file path` | string | "" | 输出文件路径（如果启用文件输出）。 |
| `echo timestamp` | bool | false | 是否在输出中包含时间戳。 |
| `echo verbosity` | string | "normal" | 详细级别："quiet"（安静）、"normal"（正常）、"verbose"（详细）、"debug"（调试）。 |
| `echo max lines` | number | 1000 | 输出窗口最大行数（防止溢出）。 |
| `echo buffer size` | number | 10000 | 输出缓冲区大小（字符数）。 |
| `echo color coding` | bool | true | 是否使用颜色编码（错误/警告/信息）。 |
## 返回值

`echo` 命令没有返回值。成功执行后，指定的文本会输出到脚本窗口、输出面板或日志文件。

## 使用示例

### 示例 1：基本文本输出
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本文本输出演示...")

# 1. 简单文本输出
fdtd.echo("=== Lumerical 脚本输出演示 ===")
fdtd.echo()  # 空行

# 2. 变量输出
x = 42
y = 3.14159
name = "Lumerical"
fdtd.echo(f"变量输出演示:")
fdtd.echo(f"  整数 x = {x}")
fdtd.echo(f"  浮点数 y = {y}")
fdtd.echo(f"  字符串 name = '{name}'")
fdtd.echo()

# 3. 表达式输出
a = 10
b = 20
fdtd.echo("表达式输出演示:")
fdtd.echo(f"  a + b = {a + b}")
fdtd.echo(f"  a * b = {a * b}")
fdtd.echo(f"  sqrt(a^2 + b^2) = {np.sqrt(a**2 + b**2)}")
fdtd.echo()

# 4. 数组输出
arr = np.array([1, 2, 3, 4, 5])
fdtd.echo("数组输出演示:")
fdtd.echo(f"  数组 arr = {arr}")
fdtd.echo(f"  形状: {arr.shape}")
fdtd.echo(f"  数据类型: {arr.dtype}")
fdtd.echo(f"  平均值: {np.mean(arr)}")
fdtd.echo()

# 5. 布尔值和 None 输出
flag = True
null_value = None
fdtd.echo("特殊值输出演示:")
fdtd.echo(f"  布尔值 flag = {flag}")
fdtd.echo(f"  None 值 null_value = {null_value}")
fdtd.echo()

# 6. 多行输出
fdtd.echo("多行文本输出:")
fdtd.echo("  第一行文本")
fdtd.echo("  第二行文本")
fdtd.echo("  第三行文本")
fdtd.echo()

# 7. 特殊字符
fdtd.echo("特殊字符输出:")
fdtd.echo("  制表符: \t 文本")
fdtd.echo("  换行符: \n 新行")
fdtd.echo("  双引号: \"")
fdtd.echo("  反斜杠: \\")
fdtd.echo()

# 8. 格式化输出（类 printf）
fdtd.echo("格式化输出演示:")
fdtd.echo("  整数: %d, 八进制: %o, 十六进制: %x" % (255, 255, 255))
fdtd.echo("  浮点数: %.3f, 科学计数法: %.2e" % (3.14159, 299792458))
fdtd.echo("  字符串: %s, 字符: %c" % ("hello", 65))  # 65 = 'A'
fdtd.echo()

# 9. 复杂数据结构
data = {
    "name": "仿真结果",
    "values": [1.2, 3.4, 5.6],
    "metadata": {
        "author": "张三",
        "date": "2024-01-01"
    }
}
fdtd.echo("复杂数据结构输出:")
fdtd.echo(f"  字典数据: {data}")
fdtd.echo()

# 10. 输出控制演示
fdtd.echo("输出控制演示:")
fdtd.echo("正常消息")
fdtd.echo("警告: 这是一个警告消息")
fdtd.echo("错误: 这是一个错误消息")
fdtd.echo("信息: 这是一个信息消息")

print("基本文本输出演示完成!")
```

### 示例 2：脚本调试和日志记录
```python
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("脚本调试和日志记录演示...")

class ScriptDebugger:
    """脚本调试工具"""
    
    def __init__(self, session, log_file=None):
        self.session = session
        self.log_file = log_file
        self.start_time = time.time()
        self.message_count = 0
        self.error_count = 0
        self.warning_count = 0
        
        # 初始化日志
        self.session.echo("=" * 60)
        self.session.echo("脚本调试日志初始化")
        self.session.echo(f"开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        self.session.echo(f"日志文件: {log_file if log_file else '无'}")
        self.session.echo("=" * 60)
    
    def log(self, message, level="INFO"):
        """记录日志消息"""
        
        timestamp = time.strftime("%H:%M:%S")
        elapsed = time.time() - self.start_time
        
        # 构建日志条目
        log_entry = f"[{timestamp} | +{elapsed:.3f}s | {level}] {message}"
        
        # 输出到会话
        self.session.echo(log_entry)
        
        # 输出到文件（如果启用）
        if self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(log_entry + "\n")
            except Exception as e:
                self.session.echo(f"警告: 无法写入日志文件: {e}")
        
        # 更新统计
        self.message_count += 1
        if level == "ERROR":
            self.error_count += 1
        elif level == "WARNING":
            self.warning_count += 1
    
    def log_debug(self, message):
        """记录调试消息"""
        self.log(message, "DEBUG")
    
    def log_info(self, message):
        """记录信息消息"""
        self.log(message, "INFO")
    
    def log_warning(self, message):
        """记录警告消息"""
        self.log(message, "WARNING")
    
    def log_error(self, message):
        """记录错误消息"""
        self.log(message, "ERROR")
    
    def log_section(self, title):
        """记录章节标题"""
        self.session.echo()
        self.session.echo("=" * 60)
        self.session.echo(f"  {title}")
        self.session.echo("=" * 60)
        self.session.echo()
    
    def log_variable(self, name, value, level="INFO"):
        """记录变量值"""
        
        if isinstance(value, np.ndarray):
            # 数组处理
            shape = value.shape
            dtype = value.dtype
            summary = f"数组[{shape}], dtype={dtype}"
            if value.size <= 10:
                summary += f", 值={value}"
            else:
                summary += f", 范围=[{value.min():.3g}, {value.max():.3g}]"
            self.log(f"{name} = {summary}", level)
        elif isinstance(value, (list, tuple)):
            # 列表/元组处理
            length = len(value)
            summary = f"{type(value).__name__}[{length}]"
            if length <= 5:
                summary += f", 值={value}"
            self.log(f"{name} = {summary}", level)
        elif isinstance(value, dict):
            # 字典处理
            keys = list(value.keys())
            summary = f"dict[{len(keys)} keys]"
            if len(keys) <= 3:
                summary += f", 键={keys}"
            self.log(f"{name} = {summary}", level)
        else:
            # 其他类型
            self.log(f"{name} = {value} ({type(value).__name__})", level)
    
    def log_function_call(self, func_name, args=None, kwargs=None):
        """记录函数调用"""
        
        call_str = f"{func_name}("
        if args:
            call_str += ", ".join([str(arg) for arg in args])
        if kwargs:
            if args:
                call_str += ", "
            call_str += ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        call_str += ")"
        
        self.log(f"调用: {call_str}", "DEBUG")
    
    def log_progress(self, current, total, message=""):
        """记录进度"""
        
        if total > 0:
            percent = 100.0 * current / total
            progress_bar = self._create_progress_bar(current, total)
            self.log(f"{message} {progress_bar} {percent:.1f}% ({current}/{total})", "INFO")
        else:
            self.log(f"{message} 进度: {current}", "INFO")
    
    def _create_progress_bar(self, current, total, width=20):
        """创建进度条"""
        
        if total == 0:
            return "[?]" * width
        
        filled = int(width * current / total)
        bar = "[" + "=" * filled + " " * (width - filled) + "]"
        return bar
    
    def log_performance(self, operation_name, start_time):
        """记录性能信息"""
        
        elapsed = time.time() - start_time
        self.log(f"{operation_name} 完成，用时 {elapsed:.3f}s", "INFO")
    
    def summary(self):
        """输出摘要统计"""
        
        total_time = time.time() - self.start_time
        
        self.log_section("脚本执行摘要")
        self.log(f"总执行时间: {total_time:.3f}s")
        self.log(f"总消息数: {self.message_count}")
        self.log(f"错误数: {self.error_count}")
        self.log(f"警告数: {self.warning_count}")
        self.log(f"平均消息率: {self.message_count/total_time:.1f} 消息/秒")
        
        if self.error_count > 0:
            self.log("状态: 完成（有错误）", "ERROR")
        elif self.warning_count > 0:
            self.log("状态: 完成（有警告）", "WARNING")
        else:
            self.log("状态: 成功完成", "INFO")

# 创建调试器
debugger = ScriptDebugger(fdtd, "script_debug.log")

# 模拟脚本执行
debugger.log_section("仿真参数设置")

# 记录参数
parameters = {
    "波长范围": "1.5-1.6 μm",
    "网格精度": 0.02,
    "仿真时间": "1000 fs",
    "边界条件": "PML",
    "材料": "Si (Silicon)"
}

for key, value in parameters.items():
    debugger.log_variable(key, value)

# 模拟结构创建
debugger.log_section("几何结构创建")

debugger.log_info("创建波导结构...")
debugger.log_function_call("addrect", args=[], kwargs={"name": "waveguide"})

# 模拟参数设置
fdtd.addrect()
fdtd.set("name", "waveguide")
fdtd.set("x span", 5e-6)
fdtd.set("y span", 0.5e-6)
fdtd.set("material", "Si (Silicon) - Palik")

debugger.log_variable("波导长度", 5e-6)
debugger.log_variable("波导宽度", 0.5e-6)

# 模拟仿真设置
debugger.log_section("仿真设置")

debugger.log_info("添加 FDTD 区域...")
fdtd.addfdtd()
fdtd.set("x span", 6e-6)
fdtd.set("y span", 2e-6)

debugger.log_info("添加光源...")
fdtd.adddipole()
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)

# 模拟仿真运行
debugger.log_section("仿真运行")

# 模拟进度更新
total_steps = 100
for step in range(total_steps):
    # 模拟计算
    time.sleep(0.01)  # 短暂延迟模拟计算
    
    # 每10步报告进度
    if step % 10 == 0 or step == total_steps - 1:
        debugger.log_progress(step + 1, total_steps, "仿真进度:")
        
        # 模拟中间结果
        if step == 50:
            debugger.log_info("仿真过半，中间检查...")
            debugger.log_variable("当前场能量", np.random.rand())
            
            # 模拟警告
            if np.random.rand() > 0.7:
                debugger.log_warning("场能量略高于预期")

# 模拟结果收集
debugger.log_section("结果收集")

debugger.log_info("收集电场数据...")
E_field = np.random.rand(100, 100)  # 模拟场数据
debugger.log_variable("电场数据", E_field)

debugger.log_info("计算传输光谱...")
transmission = np.random.rand(50)  # 模拟传输谱
debugger.log_variable("传输谱", transmission)

# 模拟错误处理
debugger.log_section("错误处理测试")

try:
    debugger.log_info("测试正常操作...")
    result = 10 / 2  # 正常操作
    debugger.log_variable("正常结果", result)
    
    debugger.log_info("测试除零错误...")
    result = 10 / 0  # 这会引发错误
except ZeroDivisionError as e:
    debugger.log_error(f"除零错误: {e}")
    
    # 错误恢复
    debugger.log_info("执行错误恢复...")
    result = float('inf')
    debugger.log_variable("恢复后的结果", result)

# 模拟数据分析
debugger.log_section("数据分析")

debugger.log_info("执行数据分析...")
start_time = time.time()

# 模拟分析操作
data = np.random.randn(1000)
mean_val = np.mean(data)
std_val = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

debugger.log_performance("数据分析", start_time)

debugger.log_variable("数据大小", data.shape)
debugger.log_variable("平均值", mean_val)
debugger.log_variable("标准差", std_val)
debugger.log_variable("最小值", min_val)
debugger.log_variable("最大值", max_val)

# 模拟数据验证
debugger.log_section("数据验证")

debugger.log_info("验证数据范围...")
if max_val > 3.0:
    debugger.log_warning(f"最大值 {max_val:.3f} 超过 3σ 范围")
if min_val < -3.0:
    debugger.log_warning(f"最小值 {min_val:.3f} 低于 -3σ 范围")

debugger.log_info("验证统计特性...")
if abs(mean_val) > 0.1:
    debugger.log_warning(f"平均值 {mean_val:.3f} 偏离零较远")

# 输出最终摘要
debugger.summary()

# 清理
debugger.log_section("清理")
debugger.log_info("清理临时对象...")
try:
    fdtd.delete("waveguide")
    debugger.log_info("波导对象已删除")
except:
    debugger.log_warning("无法删除波导对象")

debugger.log_info("脚本执行完成")

print("脚本调试和日志记录演示完成!")
```

### 示例 3：进度报告和用户交互
```python
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("进度报告和用户交互演示...")

class ProgressReporter:
    """进度报告器"""
    
    def __init__(self, session):
        self.session = session
        self.progress_bars = {}
        self.start_times = {}
        
        # 输出欢迎信息
        self.session.echo("=" * 60)
        self.session.echo("        Lumerical 仿真进度监控系统")
        self.session.echo("=" * 60)
        self.session.echo()
    
    def start_task(self, task_name, total_steps):
        """开始新任务"""
        
        self.session.echo(f"[{time.strftime('%H:%M:%S')}] 开始任务: {task_name}")
        self.session.echo(f"  总步骤: {total_steps}")
        
        self.progress_bars[task_name] = {
            'total': total_steps,
            'current': 0,
            'start_time': time.time(),
            'last_update': time.time()
        }
        
        # 显示初始进度条
        self._update_progress(task_name, 0)
    
    def update_task(self, task_name, steps_completed=None, message=""):
        """更新任务进度"""
        
        if task_name not in self.progress_bars:
            self.session.echo(f"警告: 未知任务 '{task_name}'")
            return
        
        bar = self.progress_bars[task_name]
        
        if steps_completed is not None:
            bar['current'] = steps_completed
        else:
            bar['current'] += 1
        
        # 检查是否需要更新显示（避免更新太频繁）
        current_time = time.time()
        if current_time - bar['last_update'] > 0.1 or bar['current'] == bar['total']:
            self._update_progress(task_name, bar['current'], message)
            bar['last_update'] = current_time
    
    def _update_progress(self, task_name, current, message=""):
        """更新进度显示"""
        
        bar = self.progress_bars[task_name]
        total = bar['total']
        
        # 计算百分比
        percent = 100.0 * current / total if total > 0 else 0
        
        # 计算已用时间和估计剩余时间
        elapsed = time.time() - bar['start_time']
        if current > 0 and elapsed > 0:
            rate = current / elapsed  # 步骤/秒
            if rate > 0 and current < total:
                remaining = (total - current) / rate
                time_str = f"已用: {elapsed:.1f}s, 剩余: ~{remaining:.1f}s"
            else:
                time_str = f"已用: {elapsed:.1f}s"
        else:
            time_str = f"已用: {elapsed:.1f}s"
        
        # 创建进度条
        bar_width = 30
        filled = int(bar_width * current / total) if total > 0 else 0
        progress_bar = "[" + "=" * filled + " " * (bar_width - filled) + "]"
        
        # 输出进度
        if message:
            status_line = f"{task_name}: {progress_bar} {percent:5.1f}% | {time_str} | {message}"
        else:
            status_line = f"{task_name}: {progress_bar} {percent:5.1f}% | {time_str}"
        
        # 使用回车符实现原地更新
        if current < total:
            # 进度更新，使用回车符
            self.session.echo(status_line, end="\r")
        else:
            # 任务完成，换行
            self.session.echo(status_line)
    
    def complete_task(self, task_name, message=""):
        """标记任务完成"""
        
        if task_name not in self.progress_bars:
            return
        
        bar = self.progress_bars[task_name]
        self.update_task(task_name, bar['total'], message)
        
        # 输出完成消息
        elapsed = time.time() - bar['start_time']
        self.session.echo(f"[{time.strftime('%H:%M:%S')}] 任务完成: {task_name} (用时: {elapsed:.1f}s)")
        self.session.echo()
        
        # 清理
        del self.progress_bars[task_name]
    
    def user_prompt(self, question, options=None, default=None):
        """用户提示"""
        
        self.session.echo()
        self.session.echo(f"用户交互: {question}")
        
        if options:
            for i, option in enumerate(options):
                self.session.echo(f"  {i+1}. {option}")
            
            # 模拟用户输入（实际应用中可能使用 GUI 对话框）
            # 这里简化：返回第一个选项
            choice = 1
            self.session.echo(f"选择: {choice} ({options[choice-1]})")
            return options[choice-1]
        else:
            # 是/否问题
            self.session.echo(f"  是(Y) / 否(N)")
            # 简化：返回默认值或 True
            result = default if default is not None else True
            self.session.echo(f"选择: {'是' if result else '否'}")
            return result
    
    def report_result(self, title, results, format="table"):
        """报告结果"""
        
        self.session.echo()
        self.session.echo(f"结果报告: {title}")
        self.session.echo("-" * 50)
        
        if format == "table":
            # 表格格式
            if isinstance(results, dict):
                for key, value in results.items():
                    if isinstance(value, (int, float)):
                        self.session.echo(f"  {key:20s}: {value:12.6g}")
                    else:
                        self.session.echo(f"  {key:20s}: {value}")
            elif isinstance(results, list):
                for i, item in enumerate(results):
                    self.session.echo(f"  [{i+1}] {item}")
        
        elif format == "list":
            # 列表格式
            for item in results:
                self.session.echo(f"  • {item}")
        
        self.session.echo("-" * 50)
    
    def warning(self, message):
        """输出警告"""
        
        self.session.echo(f"[警告] {message}")
    
    def error(self, message):
        """输出错误"""
        
        self.session.echo(f"[错误] {message}")
    
    def info(self, message):
        """输出信息"""
        
        self.session.echo(f"[信息] {message}")

# 创建进度报告器
reporter = ProgressReporter(fdtd)

# 模拟多任务仿真流程
print("\n模拟仿真流程...")

# 任务1: 几何创建
reporter.start_task("几何结构创建", 5)

reporter.update_task("几何结构创建", 1, "创建基板...")
time.sleep(0.5)
fdtd.addrect()
fdtd.set("name", "substrate")
fdtd.set("material", "SiO2 (Glass) - Palik")

reporter.update_task("几何结构创建", 2, "创建波导...")
time.sleep(0.5)
fdtd.addrect()
fdtd.set("name", "waveguide")
fdtd.set("material", "Si (Silicon) - Palik")

reporter.update_task("几何结构创建", 3, "创建光栅耦合器...")
time.sleep(0.5)

reporter.update_task("几何结构创建", 4, "优化结构参数...")
time.sleep(0.5)

reporter.update_task("几何结构创建", 5, "验证几何完整性...")
time.sleep(0.5)

reporter.complete_task("几何结构创建", "几何结构创建完成")

# 任务2: 仿真设置
reporter.start_task("仿真参数设置", 8)

sim_steps = [
    "设置网格精度",
    "定义边界条件",
    "添加光源",
    "添加监视器",
    "设置仿真时间",
    "配置材料模型",
    "验证设置",
    "保存仿真文件"
]

for i, step in enumerate(sim_steps):
    reporter.update_task("仿真参数设置", i+1, step)
    time.sleep(0.3)

reporter.complete_task("仿真参数设置", "仿真参数设置完成")

# 用户交互示例
user_choice = reporter.user_prompt(
    "请选择仿真模式:",
    ["快速仿真（低精度）", "标准仿真（平衡）", "精确仿真（高精度）"],
    default="标准仿真（平衡）"
)

reporter.info(f"用户选择: {user_choice}")

# 任务3: 仿真运行
reporter.start_task("FDTD仿真运行", 100)

for i in range(100):
    # 模拟仿真步骤
    time.sleep(0.02)
    
    # 更新进度
    reporter.update_task("FDTD仿真运行", i+1)
    
    # 模拟中间报告
    if i == 25:
        reporter.info("仿真进行到25%，场分布稳定")
    elif i == 50:
        reporter.info("仿真进行到50%，检查收敛性")
    elif i == 75:
        reporter.info("仿真进行到75%，即将完成")

reporter.complete_task("FDTD仿真运行", "FDTD仿真运行完成")

# 任务4: 数据分析
reporter.start_task("数据分析与后处理", 6)

analysis_steps = [
    "收集场数据",
    "计算传输谱",
    "分析模式特性",
    "提取Q因子",
    "生成图表",
    "保存结果"
]

for i, step in enumerate(analysis_steps):
    reporter.update_task("数据分析与后处理", i+1, step)
    
    # 模拟数据处理时间
    if step == "计算传输谱":
        time.sleep(0.8)
    elif step == "分析模式特性":
        time.sleep(0.6)
    else:
        time.sleep(0.2)

reporter.complete_task("数据分析与后处理", "数据分析完成")

# 报告结果
results = {
    "中心波长": 1.55e-6,
    "Q因子": 12500,
    "传输效率": 0.85,
    "插入损耗": 1.2,
    "带宽": 12.5e-9,
    "仿真时间": 356.2
}

reporter.report_result("仿真结果摘要", results, "table")

# 输出警告和错误示例
reporter.warning("传输效率略低于设计目标（目标>0.9）")
reporter.warning("建议优化光栅耦合器设计以提高效率")

# 最终总结
reporter.info("仿真流程完成")
reporter.info("结果已保存到输出文件")

print("\n进度报告和用户交互演示完成!")
```

### 示例 4：数据输出和格式化
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("数据输出和格式化演示...")

class DataFormatter:
    """数据格式化工具"""
    
    def __init__(self, session):
        self.session = session
    
    def echo_table(self, data, title="", headers=None, format_spec=None):
        """输出表格数据"""
        
        if title:
            self.session.echo()
            self.session.echo(title)
            self.session.echo("-" * 60)
        
        if isinstance(data, dict):
            # 字典转表格
            if headers is None:
                headers = ["键", "值", "类型", "描述"]
            
            # 确定列宽
            col_widths = [len(h) for h in headers]
            
            rows = []
            for key, value in data.items():
                if isinstance(value, np.ndarray):
                    val_str = f"数组{value.shape}"
                else:
                    val_str = str(value)
                
                type_str = type(value).__name__
                desc = self._infer_description(key, value)
                
                row = [str(key), val_str, type_str, desc]
                rows.append(row)
                
                # 更新列宽
                for i, cell in enumerate(row):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
            
            # 输出表头
            header_line = " | ".join([h.ljust(col_widths[i]) for i, h in enumerate(headers)])
            self.session.echo(header_line)
            self.session.echo("-" * len(header_line))
            
            # 输出数据行
            for row in rows:
                row_line = " | ".join([str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)])
                self.session.echo(row_line)
        
        elif isinstance(data, list):
            # 列表输出
            if headers and len(headers) == 2:
                # 两列列表
                col_width = max(len(str(item)) for item in data)
                for i, item in enumerate(data):
                    self.session.echo(f"  {i+1:3d}. {str(item).ljust(col_width)}")
            else:
                # 简单列表
                for i, item in enumerate(data):
                    self.session.echo(f"  [{i+1}] {item}")
        
        elif isinstance(data, np.ndarray):
            # 数组输出
            self._echo_array(data, title, format_spec)
        
        else:
            # 其他类型
            self.session.echo(str(data))
    
    def _echo_array(self, array, title="", format_spec=None):
        """输出数组"""
        
        self.session.echo(f"数组: {array.shape}, dtype={array.dtype}")
        
        if array.ndim == 1:
            # 一维数组
            if len(array) <= 20:
                # 显示所有元素
                for i, val in enumerate(array):
                    if format_spec:
                        val_str = format_spec % val
                    else:
                        val_str = f"{val:.6g}"
                    self.session.echo(f"  [{i:3d}] {val_str}")
            else:
                # 显示摘要
                self.session.echo(f"  前5个: {array[:5]}")
                self.session.echo(f"  后5个: {array[-5:]}")
                self.session.echo(f"  最小值: {array.min():.6g}, 最大值: {array.max():.6g}")
                self.session.echo(f"  平均值: {array.mean():.6g}, 标准差: {array.std():.6g}")
        
        elif array.ndim == 2:
            # 二维数组（矩阵）
            rows, cols = array.shape
            
            if rows <= 10 and cols <= 10:
                # 显示完整矩阵
                for i in range(rows):
                    row_vals = []
                    for j in range(cols):
                        val = array[i, j]
                        if format_spec:
                            val_str = format_spec % val
                        else:
                            val_str = f"{val:.6g}"
                        row_vals.append(val_str)
                    self.session.echo("  [" + "  ".join(row_vals) + "]")
            else:
                # 显示摘要
                self.session.echo(f"  矩阵 {rows}×{cols}")
                self.session.echo(f"  范围: [{array.min():.6g}, {array.max():.6g}]")
                self.session.echo(f"  范数: {np.linalg.norm(array):.6g}")
                self.session.echo(f"  迹: {np.trace(array) if rows == cols else 'N/A'}")
        
        else:
            # 高维数组
            self.session.echo(f"  {array.ndim}维数组，形状: {array.shape}")
            self.session.echo(f"  大小: {array.size} 元素")
            self.session.echo(f"  范围: [{array.min():.6g}, {array.max():.6g}]")
    
    def _infer_description(self, key, value):
        """根据键名推断描述"""
        
        key_lower = key.lower()
        
        if any(word in key_lower for word in ['wavelength', 'lambda']):
            return "波长相关参数"
        elif any(word in key_lower for word in ['frequency', 'freq']):
            return "频率相关参数"
        elif any(word in key_lower for word in ['power', 'energy']):
            return "功率或能量"
        elif any(word in key_lower for word in ['efficiency', 'loss']):
            return "效率或损耗"
        elif any(word in key_lower for word in ['q', 'quality']):
            return "品质因子"
        elif any(word in key_lower for word in ['size', 'span', 'length']):
            return "尺寸参数"
        elif any(word in key_lower for word in ['position', 'x', 'y', 'z']):
            return "位置坐标"
        elif any(word in key_lower for word in ['material', 'epsilon', 'index']):
            return "材料属性"
        elif isinstance(value, np.ndarray):
            return "数值数组"
        elif isinstance(value, (int, float)):
            return "数值"
        elif isinstance(value, str):
            return "字符串"
        elif isinstance(value, bool):
            return "布尔值"
        else:
            return "数据"
    
    def echo_matrix(self, matrix, name="矩阵", precision=6):
        """输出矩阵（专业格式）"""
        
        self.session.echo()
        self.session.echo(f"{name} ({matrix.shape[0]}×{matrix.shape[1]})")
        self.session.echo("-" * 60)
        
        if matrix.shape[0] <= 10 and matrix.shape[1] <= 10:
            # 完整输出
            for i in range(matrix.shape[0]):
                row_str = "  "
                for j in range(matrix.shape[1]):
                    val = matrix[i, j]
                    
                    if np.iscomplexobj(val):
                        # 复数
                        if abs(val.imag) < 10**(-precision):
                            # 纯实数
                            row_str += f"{val.real:{precision+8}.{precision}f}  "
                        else:
                            # 复数
                            row_str += f"{val.real:{precision+4}.{precision}f}+{val.imag:{precision+4}.{precision}f}j  "
                    else:
                        # 实数
                        row_str += f"{val:{precision+8}.{precision}f}  "
                
                self.session.echo(row_str)
        else:
            # 摘要输出
            self.session.echo("  [显示摘要，矩阵过大]")
            
            # 显示角子矩阵
            sub_size = min(3, matrix.shape[0], matrix.shape[1])
            self.session.echo(f"  左上角 {sub_size}×{sub_size} 子矩阵:")
            
            for i in range(sub_size):
                row_str = "  "
                for j in range(sub_size):
                    val = matrix[i, j]
                    row_str += f"{val:{precision+8}.{precision}f}  "
                self.session.echo(row_str)
            
            # 统计信息
            self.session.echo(f"  范数: {np.linalg.norm(matrix):.{precision}f}")
            self.session.echo(f"  条件数: {np.linalg.cond(matrix):.{precision}f}")
        
        self.session.echo("-" * 60)
    
    def echo_complex(self, z, name="复数"):
        """输出复数（极坐标和笛卡尔坐标）"""
        
        magnitude = abs(z)
        phase = np.angle(z)
        phase_deg = np.degrees(phase)
        
        self.session.echo(f"{name}:")
        self.session.echo(f"  笛卡尔坐标: {z.real:.6f} + {z.imag:.6f}j")
        self.session.echo(f"  极坐标: {magnitude:.6f} ∠ {phase_deg:.2f}°")
        self.session.echo(f"  幅度: {magnitude:.6f}, 相位: {phase:.6f} rad ({phase_deg:.2f}°)")
    
    def echo_statistics(self, data, name="数据"):
        """输出统计信息"""
        
        data_array = np.asarray(data)
        
        self.session.echo(f"{name}统计:")
        self.session.echo(f"  数量: {data_array.size}")
        self.session.echo(f"  最小值: {data_array.min():.6g}")
        self.session.echo(f"  最大值: {data_array.max():.6g}")
        self.session.echo(f"  范围: {data_array.max() - data_array.min():.6g}")
        self.session.echo(f"  平均值: {data_array.mean():.6g}")
        self.session.echo(f"  中位数: {np.median(data_array):.6g}")
        self.session.echo(f"  标准差: {data_array.std():.6g}")
        self.session.echo(f"  方差: {data_array.var():.6g}")
        
        if data_array.size >= 4:
            q1 = np.percentile(data_array, 25)
            q3 = np.percentile(data_array, 75)
            iqr = q3 - q1
            self.session.echo(f"  四分位距: {iqr:.6g} (Q1={q1:.6g}, Q3={q3:.6g})")
    
    def echo_scientific(self, value, name="值", unit=""):
        """科学计数法输出"""
        
        self.session.echo(f"{name}:")
        self.session.echo(f"  十进制: {value}")
        self.session.echo(f"  科学计数法: {value:.6e}")
        
        # 工程表示法（10³的倍数）
        prefixes = {
            24: "Y", 21: "Z", 18: "E", 15: "P", 12: "T",
            9: "G", 6: "M", 3: "k", 0: "", -3: "m",
            -6: "μ", -9: "n", -12: "p", -15: "f",
            -18: "a", -21: "z", -24: "y"
        }
        
        if value != 0:
            exponent = np.floor(np.log10(abs(value)) / 3) * 3
            if exponent in prefixes:
                scaled = value / (10 ** exponent)
                prefix = prefixes[exponent]
                self.session.echo(f"  工程表示法: {scaled:.3f} {prefix}{unit}")
    
    def echo_comparison(self, actual, expected, name="比较", tolerance=1e-6):
        """输出比较结果"""
        
        actual_arr = np.asarray(actual)
        expected_arr = np.asarray(expected)
        
        if actual_arr.shape != expected_arr.shape:
            self.session.echo(f"形状不匹配: 实际{actual_arr.shape} vs 预期{expected_arr.shape}")
            return
        
        diff = actual_arr - expected_arr
        abs_diff = np.abs(diff)
        rel_diff = abs_diff / np.abs(expected_arr)
        
        # 处理除以零
        rel_diff = np.where(expected_arr == 0, abs_diff, rel_diff)
        
        self.session.echo(f"{name}比较:")
        self.session.echo(f"  最大绝对误差: {abs_diff.max():.6e}")
        self.session.echo(f"  平均绝对误差: {abs_diff.mean():.6e}")
        self.session.echo(f"  最大相对误差: {rel_diff.max():.6e}")
        self.session.echo(f"  平均相对误差: {rel_diff.mean():.6e}")
        
        if np.all(abs_diff < tolerance):
            self.session.echo(f"  通过: 所有误差 < {tolerance}")
        else:
            self.session.echo(f"  失败: 有些误差 ≥ {tolerance}")
            
            # 显示失败位置
            fail_indices = np.where(abs_diff >= tolerance)
            if len(fail_indices[0]) <= 10:
                for idx in zip(*fail_indices):
                    idx_str = "[" + "][".join(str(i) for i in idx) + "]"
                    self.session.echo(f"    位置{idx_str}: 实际={actual_arr[idx]:.6e}, 预期={expected_arr[idx]:.6e}, 误差={abs_diff[idx]:.6e}")

# 创建数据格式化器
formatter = DataFormatter(fdtd)

# 演示各种数据输出
print("\n数据输出和格式化演示...")

# 1. 表格输出
fdtd.echo("\n1. 表格数据输出")
fdtd.echo("=" * 60)

sample_data = {
    "波长": 1.55e-6,
    "频率": 193.414e12,
    "折射率": 3.45,
    "Q因子": 12500,
    "传输效率": 0.85,
    "仿真时间": 356.2,
    "材料": "Si (Silicon)",
    "有效模式面积": np.array([0.1, 0.2, 0.3])
}

formatter.echo_table(sample_data, "仿真参数表")

# 2. 数组输出
fdtd.echo("\n2. 数组数据输出")
fdtd.echo("=" * 60)

# 一维数组
vector = np.linspace(1.5e-6, 1.6e-6, 15)
formatter.echo_table(vector, "波长扫描点", ["索引", "波长(m)", "波长(nm)"])

# 二维数组
matrix = np.random.randn(4, 4)
formatter.echo_matrix(matrix, "随机矩阵")

# 3. 复数输出
fdtd.echo("\n3. 复数数据输出")
fdtd.echo("=" * 60)

complex_val = 3 + 4j
formatter.echo_complex(complex_val, "测试复数")

# 复数数组
complex_array = np.array([1+2j, 3+4j, 5+6j])
fdtd.echo("\n复数数组:")
for i, z in enumerate(complex_array):
    formatter.echo_complex(z, f"元素[{i}]")

# 4. 统计输出
fdtd.echo("\n4. 统计信息输出")
fdtd.echo("=" * 60)

# 生成测试数据
np.random.seed(42)
normal_data = np.random.normal(0, 1, 1000)
formatter.echo_statistics(normal_data, "正态分布数据")

# 5. 科学计数法输出
fdtd.echo("\n5. 科学计数法输出")
fdtd.echo("=" * 60)

test_values = [
    299792458,      # 光速 (m/s)
    1.602176634e-19,  # 电子电荷 (C)
    6.62607015e-34,   # 普朗克常数 (J·s)
    1.380649e-23,     # 玻尔兹曼常数 (J/K)
    6.02214076e23,    # 阿伏伽德罗常数 (mol⁻¹)
    9.1093837015e-31, # 电子质量 (kg)
    1.67262192369e-27 # 质子质量 (kg)
]

for val in test_values:
    formatter.echo_scientific(val, "物理常数", unit="")

# 6. 比较输出
fdtd.echo("\n6. 数据比较输出")
fdtd.echo("=" * 60)

# 生成测试数据
x = np.linspace(0, 2*np.pi, 50)
y_actual = np.sin(x)
y_expected = x - x**3/6 + x**5/120  # 泰勒展开近似

formatter.echo_comparison(y_actual, y_expected, "sin(x)与泰勒展开比较", tolerance=0.01)

# 7. 格式化数字
fdtd.echo("\n7. 数字格式化")
fdtd.echo("=" * 60)

numbers = [1234.5678, 0.000123456, 987654321.123, 3.141592653589793]

fdtd.echo("不同格式的数字:")
for num in numbers:
    fdtd.echo(f"  原始: {num}")
    fdtd.echo(f"  固定点: {num:.4f}")
    fdtd.echo(f"  科学计数法: {num:.4e}")
    fdtd.echo(f"  通用格式: {num:.4g}")
    fdtd.echo()

# 8. 输出仿真结果
fdtd.echo("\n8. 仿真结果报告")
fdtd.echo("=" * 60)

# 模拟仿真结果
sim_results = {
    "参数": {
        "波长范围": "1.5-1.6 μm",
        "网格精度": 0.02,
        "边界条件": "PML",
        "仿真时间": "1000 fs"
    },
    "性能指标": {
        "最高效率": 0.92,
        "最低损耗": 0.08,
        "平均Q因子": 15000,
        "带宽": 15.3e-9
    },
    "计算统计": {
        "网格点数": 1250000,
        "时间步数": 5000,
        "内存使用": "2.3 GB",
        "计算时间": "356秒"
    }
}

for category, data in sim_results.items():
    formatter.echo_table(data, f"{category}")

print("\n数据输出和格式化演示完成!")
```

### 示例 5：高级输出控制和集成
```python
import lumapi
import numpy as np
import time
import sys

fdtd = lumapi.FDTD()

print("高级输出控制和集成演示...")

class AdvancedOutputController:
    """高级输出控制器"""
    
    def __init__(self, session):
        self.session = session
        self.output_history = []
        self.output_filters = []
        self.output_handlers = []
        
        # 默认输出配置
        self.config = {
            'timestamp': True,
            'level_prefix': True,
            'color_coding': True,
            'max_history': 1000,
            'auto_flush': True,
            'log_to_file': False,
            'log_file': 'lumerical_output.log'
        }
    
    def configure(self, **kwargs):
        """配置输出参数"""
        
        self.config.update(kwargs)
        
        # 应用配置
        if self.config['log_to_file']:
            self._setup_log_file()
        
        # 输出配置信息
        self.echo("输出配置已更新", "CONFIG")
        for key, value in self.config.items():
            self.echo(f"  {key}: {value}", "CONFIG")
    
    def _setup_log_file(self):
        """设置日志文件"""
        
        try:
            # 清空或创建日志文件
            with open(self.config['log_file'], 'w', encoding='utf-8') as f:
                f.write(f"Lumerical 输出日志 - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n")
            self.echo(f"日志文件已创建: {self.config['log_file']}", "CONFIG")
        except Exception as e:
            self.echo(f"无法创建日志文件: {e}", "ERROR")
            self.config['log_to_file'] = False
    
    def echo(self, message, level="INFO", **kwargs):
        """增强的echo命令"""
        
        # 构建输出消息
        output_msg = self._format_message(message, level)
        
        # 应用过滤器
        if not self._apply_filters(output_msg, level):
            return
        
        # 输出到会话
        self.session.echo(output_msg)
        
        # 输出到文件
        if self.config['log_to_file']:
            self._write_to_log(output_msg)
        
        # 添加到历史
        self.output_history.append({
            'timestamp': time.time(),
            'message': message,
            'level': level,
            'formatted': output_msg
        })
        
        # 限制历史大小
        if len(self.output_history) > self.config['max_history']:
            self.output_history.pop(0)
        
        # 调用处理器
        self._call_handlers(output_msg, level, kwargs)
    
    def _format_message(self, message, level):
        """格式化消息"""
        
        parts = []
        
        # 时间戳
        if self.config['timestamp']:
            timestamp = time.strftime("%H:%M:%S")
            parts.append(f"[{timestamp}]")
        
        # 级别前缀
        if self.config['level_prefix']:
            level_map = {
                "DEBUG": "DBG",
                "INFO": "INF",
                "WARNING": "WRN",
                "ERROR": "ERR",
                "CRITICAL": "CRT",
                "CONFIG": "CFG"
            }
            level_short = level_map.get(level, level[:3])
            parts.append(f"[{level_short}]")
        
        # 消息内容
        parts.append(str(message))
        
        # 组合
        formatted = " ".join(parts)
        
        # 颜色编码（如果启用且支持）
        if self.config['color_coding']:
            formatted = self._add_color_coding(formatted, level)
        
        return formatted
    
    def _add_color_coding(self, text, level):
        """添加颜色编码（ANSI转义序列）"""
        
        # 注意：Lumerical脚本窗口可能不支持ANSI颜色
        # 这里提供兼容性实现
        
        color_map = {
            "ERROR": "\033[91m",     # 红色
            "WARNING": "\033[93m",   # 黄色
            "INFO": "\033[92m",      # 绿色
            "DEBUG": "\033[94m",     # 蓝色
            "CONFIG": "\033[95m",    # 洋红色
            "CRITICAL": "\033[41m",  # 红底白字
        }
        
        reset = "\033[0m"
        
        if level in color_map:
            # 添加颜色（如果输出支持）
            try:
                # 检查是否在支持颜色的环境中
                if sys.platform != "win32" or hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
                    return f"{color_map[level]}{text}{reset}"
            except:
                pass
        
        return text
    
    def _apply_filters(self, message, level):
        """应用输出过滤器"""
        
        for filter_func in self.output_filters:
            try:
                if not filter_func(message, level):
                    return False
            except:
                pass
        
        return True
    
    def _write_to_log(self, message):
        """写入日志文件"""
        
        try:
            with open(self.config['log_file'], 'a', encoding='utf-8') as f:
                f.write(message + "\n")
        except Exception as e:
            # 避免递归错误
            self.config['log_to_file'] = False
            self.session.echo(f"[ERROR] 无法写入日志文件: {e}")
    
    def _call_handlers(self, message, level, kwargs):
        """调用输出处理器"""
        
        for handler in self.output_handlers:
            try:
                handler(message, level, kwargs)
            except Exception as e:
                # 处理器错误，但不中断主流程
                self.session.echo(f"[ERROR] 输出处理器错误: {e}")
    
    def add_filter(self, filter_func):
        """添加输出过滤器"""
        
        self.output_filters.append(filter_func)
        self.echo(f"添加了输出过滤器: {filter_func.__name__}", "CONFIG")
    
    def add_handler(self, handler_func):
        """添加输出处理器"""
        
        self.output_handlers.append(handler_func)
        self.echo(f"添加了输出处理器: {handler_func.__name__}", "CONFIG")
    
    def get_history(self, level=None, limit=None, since=None):
        """获取输出历史"""
        
        filtered = self.output_history
        
        # 按级别过滤
        if level is not None:
            if isinstance(level, str):
                filtered = [entry for entry in filtered if entry['level'] == level]
            else:
                filtered = [entry for entry in filtered if entry['level'] in level]
        
        # 按时间过滤
        if since is not None:
            filtered = [entry for entry in filtered if entry['timestamp'] >= since]
        
        # 限制数量
        if limit is not None:
            filtered = filtered[-limit:]
        
        return filtered
    
    def clear_history(self):
        """清空输出历史"""
        
        count = len(self.output_history)
        self.output_history.clear()
        self.echo(f"已清空输出历史（{count}条记录）", "CONFIG")
    
    def statistics(self):
        """输出统计信息"""
        
        total = len(self.output_history)
        
        if total == 0:
            self.echo("无输出历史", "INFO")
            return
        
        # 按级别统计
        level_counts = {}
        for entry in self.output_history:
            level = entry['level']
            level_counts[level] = level_counts.get(level, 0) + 1
        
        # 时间范围
        if total > 0:
            first_time = self.output_history[0]['timestamp']
            last_time = self.output_history[-1]['timestamp']
            time_span = last_time - first_time
            
            self.echo("输出统计:", "INFO")
            self.echo(f"  总消息数: {total}", "INFO")
            self.echo(f"  时间范围: {time_span:.1f}秒", "INFO")
            self.echo(f"  消息频率: {total/time_span:.1f}条/秒", "INFO")
            
            self.echo("  级别分布:", "INFO")
            for level, count in sorted(level_counts.items()):
                percentage = 100.0 * count / total
                self.echo(f"    {level}: {count} ({percentage:.1f}%)", "INFO")
    
    def save_history(self, filename="output_history.json"):
        """保存输出历史到文件"""
        
        try:
            import json
            
            # 准备可序列化的数据
            serializable_history = []
            for entry in self.output_history:
                serializable_entry = {
                    'timestamp': entry['timestamp'],
                    'message': entry['message'],
                    'level': entry['level'],
                    'formatted': entry['formatted']
                }
                serializable_history.append(serializable_entry)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(serializable_history, f, indent=2, ensure_ascii=False)
            
            self.echo(f"输出历史已保存到: {filename}", "INFO")
            return True
            
        except Exception as e:
            self.echo(f"无法保存历史: {e}", "ERROR")
            return False
    
    def monitor_performance(self, operation_name):
        """性能监控装饰器"""
        
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                self.echo(f"开始操作: {operation_name}", "INFO")
                
                try:
                    result = func(*args, **kwargs)
                    elapsed = time.time() - start_time
                    self.echo(f"操作完成: {operation_name} (用时: {elapsed:.3f}s)", "INFO")
                    return result
                except Exception as e:
                    elapsed = time.time() - start_time
                    self.echo(f"操作失败: {operation_name} (用时: {elapsed:.3f}s, 错误: {e})", "ERROR")
                    raise
            
            return wrapper
        return decorator

# 创建高级输出控制器
output_ctrl = AdvancedOutputController(fdtd)

# 配置输出
output_ctrl.configure(
    timestamp=True,
    level_prefix=True,
    color_coding=True,
    max_history=500,
    log_to_file=True,
    log_file="advanced_output.log"
)

# 定义过滤器：只显示INFO及以上级别
def level_filter(message, level):
    """过滤DEBUG级别消息"""
    return level != "DEBUG"

output_ctrl.add_filter(level_filter)

# 定义处理器：重要消息额外通知
def important_message_handler(message, level, kwargs):
    """处理重要消息"""
    if level in ["ERROR", "CRITICAL"]:
        # 在实际应用中，这里可以发送邮件、短信等
        output_ctrl.echo(f"重要消息需要关注: {message}", "INFO")

output_ctrl.add_handler(important_message_handler)

# 演示各种输出
print("\n高级输出控制演示...")

# 1. 不同级别消息
output_ctrl.echo("调试信息（通常被过滤）", "DEBUG")
output_ctrl.echo("普通信息", "INFO")
output_ctrl.echo("警告信息", "WARNING")
output_ctrl.echo("错误信息", "ERROR")
output_ctrl.echo("关键错误", "CRITICAL")
output_ctrl.echo("配置信息", "CONFIG")

# 2. 使用性能监控装饰器
@output_ctrl.monitor_performance("数据生成")
def generate_data(size):
    """生成测试数据"""
    output_ctrl.echo(f"生成 {size} 个数据点...", "INFO")
    time.sleep(0.5)  # 模拟计算
    data = np.random.randn(size)
    output_ctrl.echo(f"数据生成完成，形状: {data.shape}", "INFO")
    return data

@output_ctrl.monitor_performance("数据分析")
def analyze_data(data):
    """分析数据"""
    output_ctrl.echo("执行数据分析...", "INFO")
    time.sleep(0.3)  # 模拟计算
    
    stats = {
        'mean': np.mean(data),
        'std': np.std(data),
        'min': np.min(data),
        'max': np.max(data)
    }
    
    for key, value in stats.items():
        output_ctrl.echo(f"  {key}: {value:.6f}", "INFO")
    
    return stats

# 执行带监控的操作
output_ctrl.echo("\n执行带性能监控的操作...", "INFO")
data = generate_data(10000)
stats = analyze_data(data)

# 3. 输出历史查询
output_ctrl.echo("\n查询输出历史...", "INFO")

# 获取最近5条INFO消息
recent_info = output_ctrl.get_history(level="INFO", limit=5)
output_ctrl.echo(f"最近5条INFO消息:", "INFO")
for entry in recent_info:
    output_ctrl.echo(f"  {entry['formatted']}", "INFO")

# 4. 统计信息
output_ctrl.echo("\n输出统计:", "INFO")
output_ctrl.statistics()

# 5. 模拟错误和恢复
output_ctrl.echo("\n模拟错误处理...", "INFO")

try:
    # 模拟可能失败的操作
    output_ctrl.echo("尝试危险操作...", "WARNING")
    result = 10 / 0  # 这会引发错误
except ZeroDivisionError as e:
    output_ctrl.echo(f"操作失败: {e}", "ERROR")
    
    # 错误恢复
    output_ctrl.echo("执行错误恢复...", "INFO")
    result = float('inf')
    output_ctrl.echo(f"恢复结果: {result}", "INFO")

# 6. 保存输出历史
output_ctrl.echo("\n保存输出历史...", "INFO")
output_ctrl.save_history("demo_output_history.json")

# 7. 演示过滤器效果
output_ctrl.echo("\n演示过滤器效果...", "INFO")

# 临时添加显示DEBUG的过滤器
def allow_debug_filter(message, level):
    """允许DEBUG消息"""
    return True

output_ctrl.add_filter(allow_debug_filter)
output_ctrl.echo("现在DEBUG消息应该可见了", "DEBUG")

# 8. 最终清理
output_ctrl.echo("\n执行清理...", "INFO")
output_ctrl.clear_history()
output_ctrl.statistics()

output_ctrl.echo("\n高级输出控制演示完成!", "INFO")

print("\n高级输出控制和集成演示完成!")
```

## 注意事项

1. **输出性能**：频繁调用 `echo` 命令可能影响脚本性能，特别是在循环中。对于大量输出，考虑批量输出或使用更高效的方法。

2. **输出缓冲区**：Lumerical 有输出缓冲区限制。过多的输出可能导致缓冲区溢出或性能下降。定期清除或管理输出历史。

3. **格式化兼容性**：格式化字符串语法可能因 Lumerical 版本而异。建议使用简单的格式或检查版本兼容性。

4. **特殊字符处理**：某些特殊字符（如控制字符、Unicode 字符）可能在输出中表现不同。测试以确保正确显示。

5. **输出重定向**：`echo` 输出可以重定向到文件或其他目标。了解如何配置输出目标以满足特定需求。

6. **错误输出**：对于错误消息，考虑使用专门的错误报告机制，而不仅仅是 `echo`。这有助于错误追踪和调试。

7. **国际化**：如果脚本需要多语言支持，考虑将消息外部化或提供本地化选项。

8. **安全性**：避免输出敏感信息（如密码、密钥）到日志或输出窗口。

9. **日志管理**：对于长期运行的脚本，实现日志轮转或大小限制，防止日志文件过大。

10. **用户体验**：对于交互式脚本，提供清晰、有信息量的输出，帮助用户理解脚本状态和进度。
## 错误处理

### 常见错误
1. **输出缓冲区溢出**: 输出过多导致缓冲区溢出
   - 症状: 输出丢失、脚本变慢或崩溃
   - 解决方案: 减少输出频率，使用 `clearoutput` 定期清除缓冲区，或增加缓冲区大小

2. **格式化字符串错误**: 格式化字符串与参数不匹配
   - 症状: 输出格式错误、类型错误或脚本错误
   - 解决方案: 检查格式化字符串和参数类型，使用简单的字符串拼接作为替代

3. **文件输出错误**: 无法写入日志文件
   - 症状: 文件权限错误、磁盘空间不足或路径无效
   - 解决方案: 检查文件权限和磁盘空间，确保目录存在，使用绝对路径

4. **特殊字符问题**: 特殊字符导致输出乱码
   - 症状: Unicode字符显示不正确，控制字符引起格式混乱
   - 解决方案: 避免使用控制字符，对Unicode字符进行适当编码

5. **性能问题**: 大量输出导致脚本性能下降
   - 症状: 脚本运行缓慢，响应延迟
   - 解决方案: 减少输出量，批量输出，或仅在调试时输出

### Python 错误处理示例
```python
import lumapi

class SafeEcho:
    """安全的echo输出类"""
    
    def __init__(self, session, max_messages=1000, enable_file_logging=False):
        self.session = session
        self.max_messages = max_messages
        self.message_count = 0
        self.enable_file_logging = enable_file_logging
        self.log_file = None
        
        if enable_file_logging:
            self._setup_log_file()
    
    def _setup_log_file(self):
        """设置日志文件"""
        import os
        import datetime
        
        try:
            # 创建日志目录
            log_dir = "logs"
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            
            # 创建时间戳日志文件
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.log_file = os.path.join(log_dir, f"lumerical_log_{timestamp}.txt")
            
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write(f"Lumerical 脚本日志 - {timestamp}\n")
                f.write("=" * 60 + "\n")
            
            self.echo(f"日志文件已创建: {self.log_file}", "INFO")
            
        except Exception as e:
            self.enable_file_logging = False
            self.echo(f"无法创建日志文件: {e}", "ERROR")
    
    def echo(self, message, level="INFO"):
        """安全的echo输出"""
        
        # 检查消息数量限制
        if self.message_count >= self.max_messages:
            self._handle_message_limit()
            return
        
        try:
            # 格式化消息
            formatted_message = self._format_message(message, level)
            
            # 输出到Lumerical
            self.session.echo(formatted_message)
            
            # 输出到文件
            if self.enable_file_logging and self.log_file:
                self._write_to_log(formatted_message)
            
            # 更新计数
            self.message_count += 1
            
            # 定期清理建议
            if self.message_count % 100 == 0:
                self._suggest_cleanup()
                
        except RuntimeError as e:
            # Lumerical运行时错误
            self._handle_runtime_error(e, message)
            
        except Exception as e:
            # 其他错误
            self._handle_general_error(e, message)
    
    def _format_message(self, message, level):
        """格式化消息"""
        import datetime
        
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # 添加级别前缀
        level_prefix = {
            "INFO": "[INFO]",
            "WARNING": "[WARN]",
            "ERROR": "[ERR]",
            "DEBUG": "[DBG]"
        }.get(level, "[INFO]")
        
        return f"[{timestamp}] {level_prefix} {message}"
    
    def _write_to_log(self, message):
        """写入日志文件"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(message + "\n")
        except Exception as e:
            # 文件写入错误，禁用文件日志
            self.enable_file_logging = False
            self.session.echo(f"[ERROR] 无法写入日志文件: {e}")
    
    def _handle_message_limit(self):
        """处理消息数量限制"""
        import warnings
        
        warning_msg = f"达到输出消息限制 ({self.max_messages})，后续输出将被抑制"
        
        # 使用Python警告
        warnings.warn(warning_msg, RuntimeWarning)
        
        # 输出一次警告
        self.session.echo(f"[WARNING] {warning_msg}")
        
        # 暂停一段时间后重置计数（避免完全阻塞）
        import time
        time.sleep(0.1)
        self.message_count = 0
    
    def _handle_runtime_error(self, error, original_message):
        """处理Lumerical运行时错误"""
        error_msg = str(error)
        
        if "buffer" in error_msg.lower():
            # 缓冲区相关错误
            self.session.echo("[ERROR] 输出缓冲区错误，尝试清理...")
            try:
                # 尝试清理输出
                self.session.clearoutput()
                self.session.echo("[INFO] 输出缓冲区已清理")
                
                # 重试原始消息
                self.session.echo(f"[RETRY] {original_message}")
                
            except:
                self.session.echo("[ERROR] 无法清理输出缓冲区")
        
        elif "memory" in error_msg.lower():
            # 内存相关错误
            self.session.echo("[ERROR] 内存不足，减少输出...")
            self.max_messages = self.max_messages // 2
        
        else:
            # 其他运行时错误
            self.session.echo(f"[ERROR] Lumerical运行时错误: {error_msg}")
            self.session.echo(f"[INFO] 原始消息: {original_message}")
    
    def _handle_general_error(self, error, original_message):
        """处理一般错误"""
        error_msg = str(error)
        
        self.session.echo(f"[ERROR] 输出错误: {error_msg}")
        self.session.echo(f"[INFO] 原始消息: {original_message}")
        
        # 尝试简化消息重试
        try:
            simplified = str(original_message)[:100]  # 截断长消息
            self.session.echo(f"[RETRY] {simplified}")
        except:
            pass
    
    def _suggest_cleanup(self):
        """建议清理输出"""
        if self.message_count % 500 == 0:
            self.session.echo(f"[INFO] 已输出 {self.message_count} 条消息，考虑使用 clearoutput 清理缓冲区")
    
    def summary(self):
        """输出摘要"""
        self.echo(f"输出统计: {self.message_count} 条消息已处理", "INFO")
        if self.enable_file_logging:
            self.echo(f"日志文件: {self.log_file}", "INFO")

# 使用示例
fdtd = lumapi.FDTD()

# 创建安全输出器
safe_echo = SafeEcho(fdtd, max_messages=2000, enable_file_logging=True)

# 批量输出
for i in range(1500):
    safe_echo.echo(f"消息 {i+1}: 仿真进度 {i/1500*100:.1f}%", "INFO")

# 测试错误情况
safe_echo.echo("正常消息", "INFO")
safe_echo.echo("警告消息", "WARNING")
safe_echo.echo("错误消息", "ERROR")

# 输出摘要
safe_echo.summary()
```

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有输出功能 |
| MODE Solutions | ✅ 完全支持 | 所有输出功能 |
| DEVICE | ✅ 完全支持 | 所有输出功能 |
| INTERCONNECT | ✅ 完全支持 | 所有输出功能 |

## 相关命令

- `print` - 打印变量值（类似 `echo`，但有时有细微差别）
- `printf` - 格式化输出（更接近 C 语言的 printf）
- `warning` - 输出警告消息（可能触发警告计数）
- `error` - 输出错误消息（可能触发错误处理）
- `clearoutput` - 清除输出窗口
- `redirectoutput` - 重定向输出到文件
- `getoutput` - 获取输出窗口内容
- `setoutput` - 设置输出选项

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增格式化字符串支持，增强输出控制选项 |
| Lumerical 2019a | 改进输出缓冲区管理，提高大量输出性能 |
| Lumerical 2018a | 新增 `echo to file` 属性支持文件日志记录 |
| 1.1 | 更新日期，完善文档格式，添加错误处理章节 |

## 参考

1. Lumerical 脚本语言参考手册 - 输出命令章节
2. Python 格式化字符串语法文档
3. 日志记录最佳实践指南

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*