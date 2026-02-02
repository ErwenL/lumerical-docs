# addpath

## 概述

`addpath` 命令用于向 Lumerical 脚本搜索路径中添加目录。该命令扩展了 Lumerical 脚本环境的文件搜索范围，允许从自定义目录加载脚本、函数、材料数据和其他资源文件，支持模块化和可重用的脚本开发。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addpath;
```

### Python API (Lumapi)
```python
session.addpath()
```

## 参数

`addpath` 命令需要指定要添加的路径作为参数。

## 参数说明

| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `path` | string | 是 | 要添加到搜索路径的目录路径 |
| `position` | string | 否 | 添加位置："beginning"（开头）或 "end"（结尾），默认 "end" |

## 配置属性

`addpath` 命令主要作为函数调用，不通过 `set` 命令配置属性。但可以通过相关命令管理路径。

## 返回值

`addpath` 命令没有直接的返回值。成功执行后，指定的目录将被添加到 Lumerical 脚本搜索路径中，后续的文件搜索操作将包含该目录。

## 相关路径管理命令

### 1. 路径操作命令
| 命令 | 描述 | Python API |
|------|------|------------|
| `rmpath` | 从搜索路径中移除目录 | `session.rmpath()` |
| `path` | 显示当前搜索路径 | `session.path()` |
| `pathtool` | 打开路径管理工具 | `session.pathtool()` |
| `savepath` | 保存当前路径设置 | `session.savepath()` |
| `restoredefaultpath` | 恢复默认路径 | `session.restoredefaultpath()` |

### 2. 路径状态命令
| 命令 | 描述 | Python API |
|------|------|------------|
| `which` | 查找函数或文件位置 | `session.which()` |
| `exist` | 检查文件或变量是否存在 | `session.exist()` |
| `what` | 列出目录内容 | `session.what()` |

## 示例

### 示例 1：添加单个目录到搜索路径

#### LSF 脚本
```lumerical
// 添加单个目录到搜索路径
addpath("C:/my_scripts/lumerical");

// 现在可以从该目录加载脚本
runscript("my_custom_function.lsf");

// 显示当前路径
path;
```

#### Python API
```python
import lumapi
import os

session = lumapi.MODE()

# 定义要添加的目录列表
script_dirs = [
    "C:/projects/photonics/scripts",
    "C:/projects/photonics/materials",
    "C:/projects/photonics/functions",
    "C:/shared/lumerical_libraries"
]

# 添加所有目录到搜索路径开头（优先搜索）
for dir_path in script_dirs:
    if os.path.exists(dir_path):
        session.addpath(dir_path, "beginning")
        print(f"Added to path: {dir_path}")
    else:
        print(f"Warning: Directory not found: {dir_path}")

# 显示当前搜索路径
current_path = session.path()
print("Current search path:")
for i, path_item in enumerate(current_path):
    print(f"{i+1}: {path_item}")

# 检查特定函数是否存在
if session.exist("calculate_coupling", "file"):
    print("Coupling calculation function found in path")
else:
    print("Function not found in current path")
```

### 示例 3：路径管理与工具使用
```python
import lumapi

session = lumapi.DEVICE()

# 添加工作目录到路径
import os
current_dir = os.getcwd()
session.addpath(current_dir)

# 添加子目录
session.addpath(os.path.join(current_dir, "scripts"))
session.addpath(os.path.join(current_dir, "data"))
session.addpath(os.path.join(current_dir, "utils"))

# 使用 which 命令查找文件
file_location = session.which("thermal_analysis.lsf")
if file_location:
    print(f"Thermal analysis script found at: {file_location}")
else:
    print("Script not found in search path")

# 列出目录内容
dir_contents = session.what("scripts")
print("Contents of scripts directory:")
for item in dir_contents:
    print(f"  {item}")

# 保存路径配置供以后使用
session.savepath()
print("Path configuration saved")

# 可以打开路径管理工具进行可视化管理
# session.pathtool()
```

### 示例 4：模块化脚本开发
```python
import lumapi

# 假设项目结构：
# project/
#   ├── main_simulation.lsf
#   ├── utils/
#   │   ├── geometry_utils.lsf
#   │   ├── material_utils.lsf
#   │   └── analysis_utils.lsf
#   └── libs/
#       ├── waveguide_lib.lsf
#       └── detector_lib.lsf

session = lumapi.FDTD()

# 添加项目库路径
project_root = "C:/projects/si_photonics"
session.addpath(project_root)
session.addpath(project_root + "/utils")
session.addpath(project_root + "/libs")

# 现在可以调用各个模块中的函数
session.runscript("utils/geometry_utils.lsf")
session.runscript("libs/waveguide_lib.lsf")

# 或者在脚本中直接使用定义的函数
# 注意：需要确保函数已定义在全局命名空间
# session.create_waveguide(width=500e-9, height=220e-9, length=10e-6)
# session.analyze_transmission(frequencies)

# 移除不再需要的路径
session.rmpath("C:/old_scripts/deprecated")  # 移除旧脚本路径

# 恢复默认路径（移除所有自定义路径）
# session.restoredefaultpath()
```

## 路径搜索顺序

Lumerical 按照以下顺序搜索文件：

1. **当前工作目录**：脚本执行的当前目录
2. **用户添加路径**：通过 `addpath` 添加的目录（按添加顺序）
3. **Lumerical 安装目录**：软件安装的标准库目录
4. **MATLAB 路径**（如果集成）：连接的 MATLAB 路径

使用 `"beginning"` 参数添加的目录会优先搜索，使用 `"end"` 参数（默认）添加的目录会在现有路径之后搜索。

## 注意事项

1. **路径存在性**：确保添加的目录实际存在，否则会被忽略
2. **路径重复**：同一目录多次添加不会产生错误，但可能影响搜索效率
3. **相对路径**：可以使用相对路径，但基于当前工作目录解析
4. **网络路径**：支持网络路径（如 `\\server\share\scripts`）
5. **性能影响**：过多路径可能略微减慢文件搜索速度
6. **跨平台兼容性**：注意 Windows 和 Unix 路径分隔符差异（`\` vs `/`）

## 错误处理

### 常见错误
1. **路径不存在**
   - 错误信息：`Path does not exist`
   - 解决方案：检查目录路径是否正确

2. **权限不足**
   - 错误信息：`Permission denied`
   - 解决方案：检查目录访问权限

3. **无效路径格式**
   - 错误信息：`Invalid path format`
   - 解决方案：使用正确的路径格式

4. **路径过长**
   - 错误信息：`Path too long`
   - 解决方案：缩短路径或使用相对路径

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加路径（可能引发错误）
    fdtd.addpath("C:/nonexistent/directory")
    
except lumapi.LumApiError as e:
    print(f"路径添加失败: {e}")
    
    # 检查具体错误类型
    if "does not exist" in str(e).lower():
        print("错误: 路径不存在")
    elif "permission" in str(e).lower():
        print("错误: 权限不足")
    elif "invalid" in str(e).lower():
        print("错误: 无效路径格式")
    elif "too long" in str(e).lower():
        print("错误: 路径过长")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持
- **MODE Solutions**: 支持
- **DEVICE**: 支持
- **INTERCONNECT**: 支持

## 相关命令

- `rmpath` - 从搜索路径移除目录
- `path` - 显示当前搜索路径
- `which` - 查找函数或文件位置
- `exist` - 检查文件是否存在
- `runscript` - 运行脚本文件
- `cd` - 改变当前工作目录
- `pwd` - 显示当前工作目录

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增路径管理工具集成 |
| Lumerical 2019a | 增强跨平台路径支持 |
| Lumerical 2018a | 初始路径管理功能 |

## 参考

1. Lumerical 脚本开发指南
2. 文件系统路径管理最佳实践
3. 跨平台文件路径处理

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*