# cd

## 概述

`cd` 命令用于改变当前工作目录。工作目录是文件操作的默认路径，影响文件的读取、保存和相对路径解析。该命令支持绝对路径、相对路径、环境变量和特殊目录符号，是文件管理和脚本可移植性的基础工具。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
cd;
```

### Python API (Lumapi)
```python
session.cd()
```

## 参数

`cd` 命令没有直接参数，但需要通过后续的 `set` 命令配置目标路径和操作选项。

## 配置属性

改变目录后，可以使用 `set` 命令配置以下属性：

### 1. 基本路径设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `path` | string | "" | 目标目录路径 |
| `operation` | string | "change" | 操作类型："change", "push", "pop", "query" |
| `directory type` | string | "normal" | 目录类型："normal", "temporary", "workspace", "project" |
| `create if missing` | bool | false | 如果目录不存在则创建 |
| `verify existence` | bool | true | 是否验证目录存在 |

### 2. 路径解析
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `path type` | string | "absolute" | 路径类型："absolute", "relative", "environment", "alias" |
| `base directory` | string | "" | 基准目录（用于相对路径） |
| `environment variables` | dict | {} | 环境变量字典 |
| `alias mappings` | dict | {} | 别名映射字典 |
| `path expansion` | bool | true | 是否展开路径（~, $VAR等） |

### 3. 目录堆栈管理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `stack enabled` | bool | false | 是否启用目录堆栈 |
| `stack depth` | int | 20 | 堆栈深度 |
| `stack operation` | string | "none" | 堆栈操作："push", "pop", "clear", "list" |
| `stack name` | string | "default" | 堆栈名称 |
| `persistent stack` | bool | false | 是否持久化堆栈 |

### 4. 权限与访问控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `permission check` | bool | true | 是否检查权限 |
| `required permissions` | array | ["read"] | 所需权限列表 |
| `access mode` | string | "normal" | 访问模式："normal", "readonly", "writeonly", "execute" |
| `user impersonation` | bool | false | 是否用户模拟 |
| `security context` | dict | {} | 安全上下文 |

### 5. 错误处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `error handling` | string | "throw" | 错误处理："throw", "warn", "ignore", "retry" |
| `max retries` | int | 0 | 最大重试次数 |
| `fallback directory` | string | "" | 回退目录 |
| `error message` | string | "" | 自定义错误消息 |

### 6. 路径验证
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `path validation` | bool | true | 是否路径验证 |
| `validation rules` | array | [] | 验证规则列表 |
| `max path length` | int | 260 | 最大路径长度 |
| `allowed characters` | string | "" | 允许的字符集 |
| `forbidden patterns` | array | [] | 禁止的模式列表 |

### 7. 目录内容
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `list contents` | bool | false | 是否列出目录内容 |
| `content filter` | dict | {} | 内容过滤器 |
| `sort order` | string | "name" | 排序方式："name", "date", "size", "type" |
| `show hidden` | bool | false | 是否显示隐藏文件 |
| `recursive` | bool | false | 是否递归列出 |

### 8. 平台特定设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `platform` | string | "auto" | 平台："auto", "windows", "linux", "mac" |
| `path separator` | string | "/" | 路径分隔符 |
| `case sensitive` | bool | 自动 | 是否大小写敏感 |
| `unicode support` | bool | true | 是否支持Unicode路径 |

### 9. 性能优化
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `caching` | bool | true | 是否缓存目录信息 |
| `cache timeout` | float | 60 | 缓存超时时间（秒） |
| `async operation` | bool | false | 是否异步操作 |
| `background` | bool | false | 是否在后台执行 |

### 10. 日志与跟踪
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `logging` | bool | false | 是否记录日志 |
| `log level` | string | "info" | 日志级别 |
| `audit trail` | bool | false | 是否审计跟踪 |
| `history tracking` | bool | false | 是否跟踪历史 |

### 11. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `virtual directory` | bool | false | 是否虚拟目录 |
| `redirect rules` | dict | {} | 重定向规则 |
| `mount points` | array | [] | 挂载点列表 |
| `symbolic links` | bool | true | 是否跟随符号链接 |

### 12. 脚本集成
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `script context` | dict | {} | 脚本上下文 |
| `callback function` | string | "" | 回调函数 |
| `pre hook` | string | "" | 前置钩子脚本 |
| `post hook` | string | "" | 后置钩子脚本 |
## 返回值

`cd` 命令没有返回值。成功执行后，会改变当前工作目录，可以通过后续的 `getdata` 命令获取当前目录信息。

## 使用示例

### 示例 1：基本目录操作
```python
import lumapi
import os

session = lumapi.FDTD()

# 1. 改变到绝对路径
session.cd()
session.set("path", "C:/Users/username/Documents/Simulations")
session.set("verify existence", True)
print(f"Changed to: {session.getdata('current_directory')}")

# 2. 使用相对路径
session.cd()
session.set("path", "../Data")
session.set("path type", "relative")
session.set("base directory", "C:/Users/username/Documents/Simulations")
print(f"Changed to: {session.getdata('current_directory')}")

# 3. 使用环境变量
session.cd()
session.set("path", "$HOME/Documents")
session.set("path type", "environment")
session.set("environment variables", {"HOME": "C:/Users/username"})
session.set("path expansion", True)
print(f"Changed to: {session.getdata('current_directory')}")

# 4. 创建不存在的目录
session.cd()
session.set("path", "C:/Users/username/Documents/NewFolder")
session.set("create if missing", True)
session.set("permission check", True)
session.set("required permissions", ["read", "write"])
print(f"Created and changed to: {session.getdata('current_directory')}")

# 5. 获取当前目录
session.cd()
session.set("operation", "query")
current_dir = session.getdata("current_directory")
print(f"Current directory: {current_dir}")
```

### 示例 2：目录堆栈管理
```python
import lumapi

session = lumapi.MODE()

# 启用目录堆栈
session.cd()
session.set("stack enabled", True)
session.set("stack depth", 10)
session.set("stack name", "simulation_stack")

# 初始目录
start_dir = "C:/Projects/Photonics"
session.cd()
session.set("path", start_dir)
session.set("stack operation", "push")
print(f"Started at: {start_dir}")

# 遍历多个工作目录
directories = [
    "C:/Projects/Photonics/Designs",
    "C:/Projects/Photonics/Simulations",
    "C:/Projects/Photonics/Results",
    "C:/Projects/Photonics/Documentation"
]

for i, dir_path in enumerate(directories):
    # 改变目录并推入堆栈
    session.cd()
    session.set("path", dir_path)
    session.set("create if missing", i > 1)  # 结果和文档目录可能不存在
    session.set("stack operation", "push")
    
    # 在目录中执行操作
    session.cd()
    session.set("operation", "query")
    current = session.getdata("current_directory")
    print(f"Working in: {current}")
    
    # 列出目录内容
    session.cd()
    session.set("list contents", True)
    session.set("content filter", {"type": "file", "extension": [".lsf", ".py", ".mat"]})
    session.set("sort order", "date")
    contents = session.getdata("directory_contents")
    
    if contents:
        print(f"  Found {len(contents)} relevant files")
        for item in contents[:3]:  # 显示前3个
            print(f"    - {item['name']}")

# 使用堆栈返回历史目录
print("\nNavigating back through stack:")
for i in range(len(directories)):
    session.cd()
    session.set("stack operation", "pop")
    session.set("operation", "query")
    current = session.getdata("current_directory")
    print(f"  Popped back to: {current}")

# 最终应该回到起始目录
session.cd()
session.set("operation", "query")
final_dir = session.getdata("current_directory")
print(f"\nFinal directory: {final_dir}")
print(f"Back to start: {final_dir == start_dir}")
```

### 示例 3：跨平台脚本的目录管理
```python
import lumapi
import sys

session = lumapi.DEVICE()

# 检测当前平台
platform = sys.platform
print(f"Detected platform: {platform}")

# 配置平台特定设置
platform_configs = {
    "win32": {
        "path_separator": "\\",
        "case_sensitive": False,
        "home_var": "USERPROFILE",
        "temp_dir": "C:/Windows/Temp"
    },
    "linux": {
        "path_separator": "/",
        "case_sensitive": True,
        "home_var": "HOME",
        "temp_dir": "/tmp"
    },
    "darwin": {
        "path_separator": "/",
        "case_sensitive": False,  # macOS通常不区分大小写
        "home_var": "HOME",
        "temp_dir": "/tmp"
    }
}

config = platform_configs.get(platform, platform_configs["linux"])

# 设置跨平台目录路径
base_dirs = {
    "home": f"${config['home_var']}",
    "temp": config["temp_dir"],
    "project": "${HOME}/Projects/Photonics",
    "data": "${HOME}/Data/Simulations"
}

# 创建平台独立的目录结构
for dir_name, dir_path in base_dirs.items():
    session.cd()
    session.set("path", dir_path)
    session.set("path type", "environment")
    session.set("environment variables", {"HOME": "C:/Users/username"})  # Windows示例
    session.set("platform", platform)
    session.set("path separator", config["path_separator"])
    session.set("case sensitive", config["case_sensitive"])
    session.set("create if missing", True)
    session.set("unicode support", True)
    
    # 验证目录
    session.cd()
    session.set("operation", "query")
    actual_path = session.getdata("current_directory")
    print(f"{dir_name}: {actual_path}")
    
    # 检查权限
    session.cd()
    session.set("permission check", True)
    session.set("required permissions", ["read", "write"])
    permissions_ok = session.getdata("permissions_ok")
    print(f"  Permissions: {'OK' if permissions_ok else 'INSUFFICIENT'}")

# 处理路径中的特殊字符（测试Unicode支持）
test_paths = [
    "C:/Test/Normal Path",
    "C:/Test/Path with spaces",
    "C:/Test/Unicode_路径_测试",  # 中文字符
    "C:/Test/Special@Characters#",
]

for test_path in test_paths:
    try:
        session.cd()
        session.set("path", test_path)
        session.set("create if missing", True)
        session.set("unicode support", True)
        session.set("path validation", True)
        session.set("allowed characters", "a-zA-Z0-9_\-\.@#\s\u4e00-\u9fff")  # 允许Unicode中文
        
        session.cd()
        session.set("operation", "query")
        created_path = session.getdata("current_directory")
        print(f"Successfully created: {created_path}")
        
        # 清理测试目录
        import shutil
        shutil.rmtree(test_path, ignore_errors=True)
        
    except Exception as e:
        print(f"Failed to create {test_path}: {e}")

print("\nCross-platform directory management completed successfully.")
```

### 示例 4：高级目录管理与监控
```python
import lumapi
import time
import threading

session = lumapi.INTERCONNECT()

# 配置虚拟工作空间
workspace_config = {
    "name": "Photonics_Workspace",
    "root": "C:/Workspaces/Photonics",
    "subdirectories": [
        "Designs",
        "Simulations/FDTD",
        "Simulations/MODE", 
        "Simulations/INTERCONNECT",
        "Results/Raw",
        "Results/Processed",
        "Data/Input",
        "Data/Output",
        "Scripts/Python",
        "Scripts/LSF",
        "Documentation",
        "Temporary"
    ],
    "permissions": {
        "Designs": ["read", "write"],
        "Simulations": ["read", "write", "execute"],
        "Results": ["read", "write"],
        "Data": ["read", "write"],
        "Scripts": ["read", "write", "execute"],
        "Documentation": ["read"],
        "Temporary": ["read", "write", "delete"]
    }
}

# 创建工作空间目录结构
print(f"Creating workspace: {workspace_config['name']}")
print(f"Root: {workspace_config['root']}")

session.cd()
session.set("path", workspace_config["root"])
session.set("create if missing", True)
session.set("directory type", "workspace")

# 创建子目录结构
for subdir in workspace_config["subdirectories"]:
    full_path = f"{workspace_config['root']}/{subdir}"
    session.cd()
    session.set("path", full_path)
    session.set("create if missing", True)
    
    # 设置目录权限
    dir_type = subdir.split("/")[0]
    if dir_type in workspace_config["permissions"]:
        session.set("required permissions", workspace_config["permissions"][dir_type])
    
    session.cd()
    session.set("operation", "query")
    created_dir = session.getdata("current_directory")
    print(f"  Created: {created_dir}")

# 目录监控系统
class DirectoryMonitor:
    def __init__(self, session, directory, interval=5):
        self.session = session
        self.directory = directory
        self.interval = interval
        self.running = False
        self.last_state = {}
        
    def get_directory_state(self):
        """获取目录当前状态"""
        self.session.cd()
        self.session.set("path", self.directory)
        self.session.set("list contents", True)
        self.session.set("recursive", True)
        self.session.set("content filter", {"type": "all"})
        
        contents = self.session.getdata("directory_contents", [])
        state = {
            "file_count": len([c for c in contents if c.get("type") == "file"]),
            "dir_count": len([c for c in contents if c.get("type") == "dir"]),
            "total_size": sum(c.get("size", 0) for c in contents if c.get("type") == "file"),
            "last_modified": max(c.get("modified", 0) for c in contents) if contents else 0,
            "files": {c["name"]: c for c in contents if c.get("type") == "file"}
        }
        return state
    
    def detect_changes(self, old_state, new_state):
        """检测目录变化"""
        changes = []
        
        # 检测新文件
        new_files = set(new_state["files"].keys()) - set(old_state["files"].keys())
        for file in new_files:
            changes.append(("created", file, new_state["files"][file]))
        
        # 检测删除的文件
        deleted_files = set(old_state["files"].keys()) - set(new_state["files"].keys())
        for file in deleted_files:
            changes.append(("deleted", file, old_state["files"][file]))
        
        # 检测修改的文件
        common_files = set(old_state["files"].keys()) & set(new_state["files"].keys())
        for file in common_files:
            old_file = old_state["files"][file]
            new_file = new_state["files"][file]
            if old_file.get("modified") != new_file.get("modified") or \
               old_file.get("size") != new_file.get("size"):
                changes.append(("modified", file, new_file))
        
        return changes
    
    def monitor_loop(self):
        """监控循环"""
        print(f"Starting directory monitor for: {self.directory}")
        self.last_state = self.get_directory_state()
        print(f"Initial state: {self.last_state['file_count']} files, "
              f"{self.last_state['dir_count']} directories")
        
        while self.running:
            time.sleep(self.interval)
            
            try:
                current_state = self.get_directory_state()
                changes = self.detect_changes(self.last_state, current_state)
                
                if changes:
                    print(f"\n[{time.strftime('%H:%M:%S')}] Changes detected:")
                    for change_type, filename, info in changes:
                        size_mb = info.get("size", 0) / (1024*1024)
                        mod_time = time.strftime('%Y-%m-%d %H:%M:%S', 
                                                time.localtime(info.get("modified", 0)))
                        print(f"  {change_type.upper():8} {filename:30} "
                              f"({size_mb:.2f} MB, {mod_time})")
                
                self.last_state = current_state
                
            except Exception as e:
                print(f"Monitor error: {e}")
                if not self.running:
                    break
    
    def start(self):
        """启动监控"""
        self.running = True
        self.thread = threading.Thread(target=self.monitor_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """停止监控"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=self.interval * 2)

# 启动目录监控
results_dir = f"{workspace_config['root']}/Results/Raw"
monitor = DirectoryMonitor(session, results_dir, interval=3)
monitor.start()

# 模拟文件操作（在真实场景中，这些操作来自仿真运行）
print(f"\nSimulating file operations in {results_dir}...")
time.sleep(2)

# 创建一些测试文件
test_files = [
    "simulation_results_001.mat",
    "parameter_sweep.csv", 
    "field_distribution.png",
    "convergence_log.txt"
]

for i, filename in enumerate(test_files):
    # 模拟文件创建
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(dir=results_dir, prefix=filename, delete=False)
    temp_file.write(b"Test data " * 1000)  # 写入测试数据
    temp_file.close()
    
    time.sleep(1)  # 等待监控检测
    
    # 模拟文件修改
    if i == 1:
        with open(temp_file.name, 'ab') as f:
            f.write(b"Additional data " * 500)
        time.sleep(1)
    
    # 模拟文件删除
    if i == 3:
        import os
        os.unlink(temp_file.name)
        time.sleep(1)

# 停止监控
time.sleep(2)
monitor.stop()

print("\nDirectory monitoring demonstration completed.")
print(f"Final workspace structure created at: {workspace_config['root']}")
```

## 注意事项

1. **路径分隔符**：注意不同操作系统使用不同的路径分隔符（Windows: `\`, Unix: `/`）
2. **权限问题**：确保脚本有足够的权限访问目标目录
3. **路径长度限制**：Windows 有最大路径长度限制（通常 260 字符）
4. **符号链接**：注意符号链接可能导致意外行为
5. **网络路径**：访问网络共享路径时注意连接稳定性和权限
6. **Unicode 支持**：处理非 ASCII 字符路径时确保正确编码
7. **并发访问**：多线程/多进程访问同一目录时注意锁和同步
8. **性能考虑**：频繁的目录操作可能影响性能，考虑缓存机制
## 错误处理

### 常见错误
1. **目录不存在**: `path` 属性指定的目录不存在且 `create if missing` 为 false
   - 解决方案：检查路径拼写，确保目录存在，或启用 `create if missing`

2. **权限不足**: 脚本没有访问目标目录的足够权限
   - 解决方案：检查目录权限，以管理员身份运行，或更改目录所有权

3. **路径无效**: 路径包含非法字符或格式错误
   - 解决方案：验证路径格式，避免使用非法字符，确保路径长度在限制内

4. **环境变量未定义**: 使用环境变量路径但变量未定义
   - 解决方案：定义环境变量，或使用绝对路径

5. **磁盘空间不足**: 创建目录时磁盘空间不足
   - 解决方案：清理磁盘空间，或选择其他磁盘位置

6. **网络路径不可达**: 访问网络共享路径时连接失败
   - 解决方案：检查网络连接，确保共享路径可访问

### Python 错误处理
```python
import lumapi
import os

try:
    session = lumapi.FDTD()
    
    # 尝试改变目录
    target_path = "C:/Some/Path/That/May/Not/Exist"
    session.cd()
    session.set("path", target_path)
    session.set("verify existence", True)
    session.set("error handling", "throw")
    
    # 执行目录改变
    session.execute("cd")
    
    # 验证目录改变成功
    session.cd()
    session.set("operation", "query")
    current_dir = session.getdata("current_directory")
    print(f"Successfully changed to: {current_dir}")
    
except RuntimeError as e:
    print(f"目录操作错误: {e}")
    
    # 根据错误类型处理
    error_msg = str(e).lower()
    if "not exist" in error_msg or "找不到" in error_msg:
        print("目录不存在，尝试创建...")
        session.cd()
        session.set("path", target_path)
        session.set("create if missing", True)
        session.set("verify existence", False)
        session.execute("cd")
        
    elif "permission" in error_msg or "权限" in error_msg:
        print("权限不足，尝试其他目录...")
        # 回退到用户目录
        session.cd()
        session.set("path", os.path.expanduser("~"))
        session.set("verify existence", True)
        session.execute("cd")
        
    elif "invalid" in error_msg or "无效" in error_msg:
        print("路径无效，检查路径格式...")
        # 清理路径
        import re
        cleaned_path = re.sub(r'[<>:"|?*]', '', target_path)
        session.cd()
        session.set("path", cleaned_path)
        session.execute("cd")
        
    else:
        print(f"未知目录错误: {e}")
        # 使用回退目录
        if "fallback directory" in session.getproperties("cd"):
            session.cd()
            session.set("operation", "change")
            session.set("path", session.get("fallback directory"))
            session.execute("cd")
            
except Exception as e:
    print(f"意外的目录操作错误: {e}")
    
finally:
    # 确保有有效的当前目录
    session.cd()
    session.set("operation", "query")
    final_dir = session.getdata("current_directory")
    print(f"当前工作目录: {final_dir}")
```

## 产品支持

- **FDTD Solutions**: 支持（用于管理仿真文件）
- **MODE Solutions**: 支持（用于管理模式分析文件）
- **DEVICE**: 支持（用于管理热学、电学数据）
- **INTERCONNECT**: 支持（用于管理电路文件）

## 相关命令

- `pwd` - 打印当前工作目录
- `ls` - 列出目录内容
- `mkdir` - 创建目录
- `rmdir` - 删除目录
- `chdir` - 改变目录（同义命令）
- `pushd` - 推入目录堆栈
- `popd` - 弹出目录堆栈
- `dir` - 目录信息

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `stack enabled` 属性支持目录堆栈管理 |
| Lumerical 2019a | 改进跨平台路径处理，增强 Unicode 支持 |
| Lumerical 2018a | 新增 `environment variables` 属性支持环境变量扩展 |
| 1.1 | 更新日期，完善文档格式，添加错误处理章节 |

## 参考

1. Lumerical 脚本语言参考手册
2. Lumerical 文件系统操作指南
3. Python os 模块文档（用于路径操作）

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*