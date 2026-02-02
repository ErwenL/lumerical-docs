# `chdir` - 改变目录

## 概述

`chdir` 命令用于改变当前工作目录。这是 Lumerical 脚本环境中的一个基本文件系统操作命令，允许用户在脚本执行过程中切换工作目录，以便于组织项目文件、加载外部数据、保存结果等。

该命令与标准操作系统中的 `cd`（change directory）命令功能相同，但在 Lumerical 脚本环境中使用。它影响后续文件操作（如 `load`、`save`、`import` 等）的默认路径。

## 语法

### LSF 语法
```lumerical
chdir(path);
```

### Python API
```python
session.chdir(path)
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `path` | string | 要切换到的目录路径。可以是绝对路径或相对路径。 | 是 |

## 配置属性

`chdir` 命令没有可配置属性。它是一个简单的目录切换操作。
## 返回值

`chdir` 命令没有返回值。成功执行后，当前工作目录会改变为指定的路径。

## 使用示例

### 示例 1：切换到绝对路径
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 切换到绝对路径
fdtd.chdir("C:/Users/username/Lumerical/Projects")

# 验证当前目录
current_dir = fdtd.pwd()  # 获取当前工作目录
print(f"当前工作目录: {current_dir}")

# 在当前目录保存项目
fdtd.save("project_1.lms")
```

### 示例 2：切换到相对路径
```python
import lumapi
import os

fdtd = lumapi.FDTD()

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 切换到脚本目录的子目录
fdtd.chdir(os.path.join(script_dir, "data"))

# 加载数据文件
fdtd.load("simulation_data.mat")

# 切换到上一级目录
fdtd.chdir("..")

# 创建结果目录（如果不存在）
if not os.path.exists("results"):
    os.makedirs("results")
    
fdtd.chdir("results")

# 保存仿真结果
fdtd.save("simulation_results.lms")
```

### 示例 3：在自动化工作流中使用
```python
import lumapi
import os
import datetime

def run_simulation_with_organized_output():
    """运行仿真并将结果组织到按日期命名的目录中"""
    
    fdtd = lumapi.FDTD()
    
    # 创建基于日期的目录结构
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    base_dir = "C:/SimulationResults"
    
    # 切换到基础目录
    fdtd.chdir(base_dir)
    
    # 创建今天的目录
    if not os.path.exists(today):
        os.makedirs(today)
    
    fdtd.chdir(today)
    
    # 创建仿真特定目录
    sim_id = "waveguide_sweep_001"
    sim_dir = os.path.join(os.getcwd(), sim_id)
    if not os.path.exists(sim_dir):
        os.makedirs(sim_dir)
    
    fdtd.chdir(sim_dir)
    
    print(f"工作目录已设置为: {fdtd.pwd()}")
    
    # 在此处设置和运行仿真
    fdtd.addfdtd("solver", x_span=5, y_span=5, z_span=2)
    fdtd.addrect("waveguide", material="Si", x_span=0.5, y_span=0.22, z_span=10)
    
    # 运行仿真
    fdtd.run()
    
    # 保存结果
    fdtd.save("simulation.lms")
    
    # 导出数据到当前目录
    fdtd.export("monitor_data", "T.csv")
    
    return fdtd.pwd()

# 运行工作流
final_dir = run_simulation_with_organized_output()
print(f"最终工作目录: {final_dir}")
```

### 示例 4：处理路径错误
```python
import lumapi

fdtd = lumapi.FDTD()

def safe_chdir(path):
    """安全切换目录，处理路径不存在的情况"""
    import os
    
    if os.path.exists(path) and os.path.isdir(path):
        fdtd.chdir(path)
        print(f"成功切换到目录: {path}")
        return True
    else:
        print(f"警告: 目录不存在: {path}")
        # 尝试创建目录
        try:
            os.makedirs(path, exist_ok=True)
            fdtd.chdir(path)
            print(f"已创建并切换到目录: {path}")
            return True
        except Exception as e:
            print(f"错误: 无法创建目录 {path}: {e}")
            return False

# 使用安全切换
safe_chdir("C:/Valid/Path")
safe_chdir("NonExistent/Path")  # 将尝试创建
safe_chdir("")  # 空路径 - 可能切换到默认目录
```

### 示例 5：与文件操作结合使用
```python
import lumapi
import glob

fdtd = lumapi.FDTD()

# 设置工作目录到数据文件夹
data_dir = "C:/ExperimentalData"
fdtd.chdir(data_dir)

# 列出所有数据文件
data_files = glob.glob("*.mat")
print(f"找到 {len(data_files)} 个数据文件")

# 处理每个数据文件
for i, file in enumerate(data_files):
    print(f"处理文件 {i+1}/{len(data_files)}: {file}")
    
    # 加载数据
    fdtd.load(file)
    
    # 切换到结果目录
    result_dir = "C:/AnalysisResults"
    fdtd.chdir(result_dir)
    
    # 进行分析
    # ... 分析代码 ...
    
    # 保存分析结果
    result_file = f"analysis_{file.replace('.mat', '.lms')}"
    fdtd.save(result_file)
    
    # 切换回数据目录处理下一个文件
    fdtd.chdir(data_dir)
```

## 注意事项

1. **路径格式**：在 Windows 系统中，路径可以使用正斜杠 (`/`) 或反斜杠 (`\\`)。建议使用正斜杠以避免转义问题。在 LSF 脚本中，路径字符串应使用双反斜杠 (`\\`) 或正斜杠。

2. **相对路径**：相对路径是相对于当前工作目录的。可以使用 `..` 表示上一级目录，`.` 表示当前目录。

3. **目录存在性**：如果目标目录不存在，`chdir` 命令将失败并抛出错误。建议在切换目录前检查目录是否存在。

4. **跨平台兼容性**：如果脚本需要在不同操作系统上运行，建议使用 `os.path` 模块处理路径，以确保兼容性。

5. **与 `cd` 命令的关系**：`chdir` 和 `cd` 命令功能完全相同。`cd` 是 `chdir` 的别名，两者可以互换使用。

6. **作用范围**：`chdir` 命令只影响当前 Lumerical 会话的工作目录，不会影响操作系统或其他应用程序的工作目录。

7. **持久性**：工作目录更改在会话期间保持有效，直到再次更改或会话结束。

8. **默认目录**：新会话的初始工作目录通常是用户的主目录或 Lumerical 的安装目录。
## 错误处理

### 常见错误
1. **目录不存在错误**: 尝试切换到不存在的目录
   - 错误信息: "Directory does not exist" 或类似信息
   - 解决方案: 使用 `os.path.exists()` 检查目录是否存在，或使用 `os.makedirs()` 创建目录

2. **权限拒绝错误**: 没有访问目录的权限
   - 错误信息: "Permission denied" 或 "Access is denied"
   - 解决方案: 检查目录权限，以管理员身份运行，或选择其他目录

3. **路径格式错误**: 路径包含非法字符或语法错误
   - 错误信息: "Invalid path" 或 "Path syntax error"
   - 解决方案: 验证路径格式，避免使用非法字符

4. **网络路径错误**: 访问网络共享失败
   - 错误信息: "Network path not found" 或 "Connection refused"
   - 解决方案: 检查网络连接和共享权限

### Python 错误处理示例
```python
import lumapi
import os

def safe_chdir(session, path):
    """
    安全切换目录，包含错误处理
    
    参数:
        session: Lumerical 会话对象
        path: 目标目录路径
    
    返回:
        bool: 是否成功切换目录
    """
    try:
        # 规范化路径
        if not os.path.isabs(path):
            # 如果是相对路径，转换为绝对路径
            current = session.pwd()
            path = os.path.join(current, path) if current else path
        
        # 检查路径是否存在
        if not os.path.exists(path):
            print(f"目录不存在: {path}")
            
            # 询问是否创建目录
            response = input(f"目录不存在，是否创建? (y/n): ")
            if response.lower() == 'y':
                try:
                    os.makedirs(path, exist_ok=True)
                    print(f"已创建目录: {path}")
                except PermissionError:
                    print(f"权限不足，无法创建目录: {path}")
                    return False
                except Exception as e:
                    print(f"创建目录失败: {e}")
                    return False
            else:
                print("放弃切换目录")
                return False
        
        # 检查是否为目录
        if not os.path.isdir(path):
            print(f"路径不是目录: {path}")
            return False
        
        # 检查访问权限
        if not os.access(path, os.R_OK | os.W_OK):
            print(f"权限不足，无法访问目录: {path}")
            
            # 尝试以只读方式访问
            if os.access(path, os.R_OK):
                print("警告: 目录只读，可能影响文件保存")
            else:
                return False
        
        # 执行目录切换
        session.chdir(path)
        print(f"成功切换到目录: {path}")
        return True
        
    except PermissionError as e:
        print(f"权限错误: {e}")
        print("建议: 以管理员身份运行，或选择其他目录")
        return False
        
    except FileNotFoundError as e:
        print(f"文件未找到错误: {e}")
        print("建议: 检查路径拼写和目录是否存在")
        return False
        
    except RuntimeError as e:
        # Lumerical 运行时错误
        error_msg = str(e)
        if "directory" in error_msg.lower() or "path" in error_msg.lower():
            print(f"目录操作错误: {error_msg}")
            
            # 尝试使用备用路径
            home_dir = os.path.expanduser("~")
            print(f"将切换到用户目录: {home_dir}")
            
            try:
                session.chdir(home_dir)
                return True
            except:
                return False
        else:
            print(f"Lumerical 运行时错误: {error_msg}")
            return False
            
    except Exception as e:
        print(f"意外的目录切换错误: {e}")
        return False

# 使用示例
fdtd = lumapi.FDTD()
success = safe_chdir(fdtd, "C:/Some/Path")
if success:
    print(f"当前目录: {fdtd.pwd()}")
else:
    print("目录切换失败，使用当前目录")
```

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有版本 |
| MODE Solutions | ✅ 完全支持 | 所有版本 |
| DEVICE | ✅ 完全支持 | 所有版本 |
| INTERCONNECT | ✅ 完全支持 | 所有版本 |

## 相关命令

- `cd` - 改变工作目录（`chdir` 的别名）
- `pwd` - 打印当前工作目录
- `dir` - 列出目录内容
- `mkdir` - 创建目录
- `rmdir` - 删除目录
- `load` - 加载文件（受工作目录影响）
- `save` - 保存文件（受工作目录影响）

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 与 `cd` 命令功能完全统一 |
| Lumerical 2019a | 改进错误消息，提供更详细的路径错误信息 |
| Lumerical 2018a | 首次引入，作为 `cd` 的替代命令 |
| 1.1 | 更新日期，完善文档格式，添加错误处理章节 |

## 参考

1. Lumerical 脚本语言参考手册 - 文件系统命令章节
2. Python os.path 模块文档
3. 跨平台路径处理最佳实践指南

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*