# addtogroup

## 概述

`addtogroup` 命令用于将仿真对象添加到指定的组中。组是对象的逻辑集合，用于简化对象管理、批量操作、可见性控制和组织结构。该命令支持动态组管理，允许对象属于多个组，支持层次化组结构。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addtogroup;
```

### Python API (Lumapi)
```python
session.addtogroup()
```

## 参数

`addtogroup` 命令没有直接参数，但需要通过后续的 `set` 命令配置目标对象、组名和添加方式。

## 配置属性

使用 `addtogroup` 后，可以通过 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `operation` | string | "add" | 操作类型："add", "remove", "replace", "clear" |
| `target object` | string | "" | 目标对象名称（空表示选中对象） |
| `group name` | string | "default" | 组名称 |
| `create if missing` | bool | true | 如果组不存在则创建 |
| `recursive` | bool | false | 是否递归操作子对象 |

### 2. 对象选择
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `selection method` | string | "by name" | 选择方法："by name", "by type", "by property", "all" |
| `object type` | string | "" | 对象类型（如 "rectangle", "monitor", "source"） |
| `property filter` | dict | {} | 属性过滤器（键值对） |
| `selection pattern` | string | "*" | 名称匹配模式（支持通配符） |
| `max objects` | int | 1000 | 最大对象数（0 表示无限制） |

### 3. 组配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `group type` | string | "standard" | 组类型："standard", "smart", "dynamic", "hierarchical" |
| `group description` | string | "" | 组描述 |
| `group color` | string | "auto" | 组颜色（CSS 颜色或 "auto"） |
| `group visibility` | bool | true | 组可见性 |
| `group locked` | bool | false | 组是否锁定（防止修改） |
| `parent group` | string | "" | 父组名称（用于层次结构） |

### 4. 智能组设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `smart criteria` | dict | {} | 智能组条件（自动包含符合条件的对象） |
| `auto update` | bool | true | 是否自动更新（当对象变化时） |
| `update interval` | float | 1.0 | 更新间隔（秒） |
| `criteria logic` | string | "AND" | 条件逻辑："AND", "OR", "NOT" |

### 5. 动态组设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `dynamic query` | string | "" | 动态查询表达式 |
| `query language` | string | "lumerical" | 查询语言："lumerical", "python", "sql" |
| `refresh rate` | float | 5.0 | 刷新率（秒） |
| `caching` | bool | true | 是否缓存查询结果 |

### 6. 批量操作设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `batch size` | int | 100 | 批量操作大小 |
| `parallel processing` | bool | false | 是否并行处理 |
| `progress reporting` | bool | true | 是否报告进度 |
| `error handling` | string | "continue" | 错误处理："stop", "continue", "skip" |

### 7. 元数据
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `metadata` | dict | {} | 组元数据（自定义键值对） |
| `tags` | array | [] | 标签列表 |
| `categories` | array | [] | 分类列表 |
| `priority` | int | 0 | 优先级（数值越高优先级越高） |

### 8. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `validation rules` | array | [] | 验证规则列表 |
| `conflict resolution` | string | "merge" | 冲突解决："merge", "overwrite", "skip" |
| `history tracking` | bool | false | 是否跟踪历史记录 |
 | `audit log` | bool | false | 是否启用审计日志 |

## 返回值

`addtogroup` 命令没有直接的返回值。成功执行后，会将指定对象添加到指定的组中。如果操作成功，目标对象将成为组的一部分，可以通过组操作命令进行管理。

## 示例

### 示例 1：将选定对象添加到基本组

#### LSF 脚本
```lumerical
// 创建测试对象
addrect;
set("name", "waveguide1");
set("x span", 1e-6);
set("y span", 0.22e-6);

addrect;
set("name", "waveguide2");
set("x span", 1e-6);
set("y span", 0.22e-6);
set("x", 5e-6);

addcircle;
set("name", "disk_resonator");
set("radius", 5e-6);

// 将对象添加到组
addtogroup;
set("target object", "waveguide1");
set("group name", "waveguides");
set("create if missing", true);

addtogroup;
set("target object", "waveguide2");
set("group name", "waveguides");

addtogroup;
set("target object", "disk_resonator");
set("group name", "resonators");

// 配置组属性
set("group description", "Waveguide components for photonic circuit");
set("group color", "blue");
set("group visibility", true);
```

#### Python API
```python
import lumapi

session = lumapi.MODE()

# 创建多种类型的对象
for i in range(5):
    session.addrect()
    session.set("name", f"rect_{i}")
    session.set("x", i * 3e-6)

for i in range(3):
    session.addcircle()
    session.set("name", f"circle_{i}")
    session.set("x", i * 3e-6)
    session.set("y", 5e-6)

# 将所有矩形添加到 "rectangles" 组
session.addtogroup()
session.set("selection method", "by type")
session.set("object type", "rectangle")
session.set("group name", "rectangles")
session.set("create if missing", True)
session.set("batch size", 50)

# 将所有圆形添加到 "circles" 组
session.addtogroup()
session.set("selection method", "by type")
session.set("object type", "circle")
session.set("group name", "circles")

# 创建层次结构：将所有几何对象添加到 "geometry" 父组
session.addtogroup()
session.set("selection method", "by type")
session.set("object type", "rectangle")
session.set("group name", "geometry")
session.set("parent group", "")  # 顶层组

session.addtogroup()
session.set("selection method", "by type")
session.set("object type", "circle")
session.set("group name", "geometry")

# 配置层次组结构
session.set("group type", "hierarchical")
session.set("group description", "All geometric objects in the simulation")
```

### 示例 3：使用智能组（基于属性过滤）
```python
import lumapi

session = lumapi.INTERCONNECT()

# 创建多个光学端口，设置不同属性
port_configs = [
    {"name": "input_1550", "wavelength": 1.55e-6, "power": 1e-3},
    {"name": "output_1550", "wavelength": 1.55e-6, "power": 0},
    {"name": "input_1310", "wavelength": 1.31e-6, "power": 2e-3},
    {"name": "output_1310", "wavelength": 1.31e-6, "power": 0},
    {"name": "monitor", "wavelength": 1.55e-6, "power": 0},
]

for config in port_configs:
    session.addport()
    session.set("name", config["name"])
    session.set("wavelength", config["wavelength"])
    session.set("optical power", config["power"])

# 创建智能组：所有 1550nm 端口
session.addtogroup()
session.set("group name", "ports_1550nm")
session.set("group type", "smart")
session.set("smart criteria", {"wavelength": 1.55e-6})
session.set("auto update", True)

# 创建智能组：所有输入端口（功率 > 0）
session.addtogroup()
session.set("group name", "input_ports")
session.set("group type", "smart")
session.set("smart criteria", {"optical power": {"gt": 0}})
session.set("criteria logic", "AND")

# 创建智能组：所有监控端口（名称包含 "monitor"）
session.addtogroup()
session.set("group name", "monitor_ports")
session.set("group type", "smart")
session.set("selection pattern", "*monitor*")
session.set("auto update", True)

# 配置智能组高级设置
session.set("update interval", 2.0)  # 每 2 秒更新一次
session.set("caching", True)
```

### 示例 4：复杂组管理和批量操作
```python
import lumapi

session = lumapi.DEVICE()

# 创建大量热源对象
num_sources = 50
for i in range(num_sources):
    session.addrect()
    session.set("name", f"heater_{i:03d}")
    session.set("x", (i % 10) * 10e-6)
    session.set("y", (i // 10) * 10e-6)
    session.set("x span", 8e-6)
    session.set("y span", 8e-6)
    
    # 设置不同的热功率
    power = 0.1 + (i % 5) * 0.2  # 0.1 到 0.9 W
    session.set("heat power", power)
    
    # 设置温度限制
    max_temp = 80 + (i % 3) * 20  # 80 到 140°C
    session.set("maximum temperature", max_temp)

# 按功率范围分组
session.addtogroup()
session.set("group name", "low_power_heaters")
session.set("group type", "smart")
session.set("smart criteria", {"heat power": {"lt": 0.3}})
session.set("group color", "green")

session.addtogroup()
session.set("group name", "medium_power_heaters")
session.set("group type", "smart")
session.set("smart criteria", {"heat power": {"gte": 0.3, "lt": 0.6}})
session.set("group color", "yellow")

session.addtogroup()
session.set("group name", "high_power_heaters")
session.set("group type", "smart")
session.set("smart criteria", {"heat power": {"gte": 0.6}})
session.set("group color", "red")

# 按温度限制分组
session.addtogroup()
session.set("group name", "low_temp_heaters")
session.set("group type", "smart")
session.set("smart criteria", {"maximum temperature": {"lt": 100}})

session.addtogroup()
session.set("group name", "high_temp_heaters")
session.set("group type", "smart")
session.set("smart criteria", {"maximum temperature": {"gte": 100}})

# 创建复合组（同时满足多个条件）
session.addtogroup()
session.set("group name", "critical_heaters")
session.set("group type", "smart")
session.set("smart criteria", {
    "heat power": {"gte": 0.6},
    "maximum temperature": {"lt": 100}
})
session.set("criteria logic", "AND")
session.set("group color", "purple")

# 批量操作：对所有组应用设置
groups = ["low_power_heaters", "medium_power_heaters", "high_power_heaters"]
for group in groups:
    # 设置组可见性（仅显示高功率组）
    session.addtogroup()
    session.set("group name", group)
    session.set("group visibility", group == "high_power_heaters")
    
    # 设置组锁定状态
    session.set("group locked", group == "critical_heaters")
    
    # 添加元数据
    metadata = {
        "created_by": "auto_grouping_script",
        "creation_time": "2024-01-01",
        "object_count": num_sources // 3  # 估计值
    }
    session.set("metadata", metadata)

# 创建层次组结构
session.addtogroup()
session.set("group name", "all_heaters")
session.set("group type", "hierarchical")
session.set("parent group", "")

# 将子组添加到父组
for subgroup in groups:
    session.addtogroup()
    session.set("group name", subgroup)
    session.set("parent group", "all_heaters")
```

## 注意事项

1. **组名唯一性**：组名称在仿真中应唯一，避免冲突
2. **性能考虑**：大量对象或复杂智能组条件可能影响性能
3. **动态更新**：智能组的自动更新可能增加计算开销
4. **对象生命周期**：删除对象时不会自动从组中移除，需要手动清理
5. **层次结构深度**：过深的层次结构可能使导航复杂
6. **冲突解决**：当对象属于多个组时，注意属性冲突的解决策略
7. **内存使用**：大量组的元数据可能增加内存使用
8. **版本兼容性**：组结构可能在不同 Lumerical 版本间有变化

## 错误处理

### 常见错误
1. **组不存在**
   - 错误信息：`Group not found`
   - 解决方案：启用 `create if missing` 或先创建组

2. **对象不存在**
   - 错误信息：`Object not found`
   - 解决方案：检查对象名称和存在性

3. **组名冲突**
   - 错误信息：`Group name conflict`
   - 解决方案：使用唯一的组名或重命名现有组

4. **循环层次结构**
   - 错误信息：`Circular hierarchy detected`
   - 解决方案：检查父组设置，避免循环引用

5. **权限不足**
   - 错误信息：`Insufficient permissions`
   - 解决方案：检查对象锁定状态和用户权限

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加对象到组
    fdtd.addtogroup()
    fdtd.set("target object", "non_existent_object")  # 可能引发错误
    fdtd.set("group name", "test_group")
    fdtd.set("create if missing", True)
    
except lumapi.LumApiError as e:
    print(f"组操作失败: {e}")
    
    # 检查具体错误类型
    if "not found" in str(e).lower():
        print("错误: 对象或组未找到")
    elif "conflict" in str(e).lower():
        print("错误: 组名冲突")
    elif "circular" in str(e).lower():
        print("错误: 循环层次结构")
    elif "permission" in str(e).lower():
        print("错误: 权限不足")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持几何对象、监视器、光源等的分组
- **MODE Solutions**: 支持模式对象、波导、监视器的分组
- **DEVICE**: 支持热源、监视器、边界条件的分组
- **INTERCONNECT**: 支持电路元件、端口、监视器的分组

## 相关命令

- `selectgroup` - 选择组内对象
- `removefromgroup` - 从组中移除对象
- `deletegroup` - 删除组
- `renamegroup` - 重命名组
- `setgroup` - 设置组属性
- `getgroup` - 获取组信息
- `listgroups` - 列出所有组

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增智能组和动态组支持 |
| Lumerical 2019a | 增强层次组结构 |
| Lumerical 2018a | 初始组管理功能 |

## 参考

1. Lumerical 对象管理指南
2. Lumerical 组操作最佳实践
3. 数据组织和管理原则

---

 *最后更新: 2026-02-01*  
 *文档版本: 1.0*