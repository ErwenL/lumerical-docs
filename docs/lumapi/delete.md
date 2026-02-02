# `delete` - 删除对象

## 概述

`delete` 命令用于从仿真项目中删除对象。在 Lumerical 仿真中，对象可以是几何结构、光源、监视器、网格覆盖、材料定义、分析组、优化对象等。该命令是仿真清理和动态结构修改的重要工具。

删除操作是永久性的，但可以通过 `undo` 命令撤销最近的删除操作（如果支持）。正确使用 `delete` 命令可以帮助管理复杂的仿真场景，移除不需要的结构以简化模型或替换为更新的设计。

## 语法

### LSF 语法
```lumerical
delete;                     # 删除当前选择的对象
delete("object_name");      # 删除指定名称的对象
delete("all");              # 删除所有对象
delete("pattern");          # 删除匹配模式的对象
delete("type", "type_name"); # 删除指定类型的所有对象
```

### Python API
```python
session.delete()                           # 删除当前选择的对象
session.delete("object_name")              # 删除指定名称的对象
session.delete("all")                      # 删除所有对象
session.delete("pattern")                  # 删除匹配模式的对象
session.delete("type", "type_name")        # 删除指定类型的所有对象
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `object_name` | string | 要删除的对象的名称。 | 可选 |
| `"all"` | string | 特殊参数，删除所有对象。 | 可选 |
| `"pattern"` | string | 通配符模式，匹配要删除的对象名称。 | 可选 |
| `"type"` | string | 类型筛选参数，后跟对象类型名称。 | 可选 |
| `type_name` | string | 对象类型名称，如 "rect", "circle", "source", "monitor" 等。 | 可选 |

## 配置属性

`delete` 命令通常不通过 `set` 命令配置属性，但可以通过以下方式控制删除行为：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `selected` | bool | false | 对象是否被选中（通过 `select` 命令）。 |
| `visible` | bool | true | 对象是否可见（影响选择）。 |
| `locked` | bool | false | 对象是否被锁定（防止意外删除）。 |

## 返回值

`delete` 命令没有返回值。成功执行后，指定的对象被从仿真中删除。如果命令失败（例如对象不存在或权限不足），Lumerical 会抛出错误。

在 Python API 中，`session.delete()` 通常返回 `None`。成功删除不返回任何值，失败时抛出异常。

## 错误处理

### 常见错误

1. **对象不存在错误**
   ```python
   # 错误：对象 "nonexistent" 不存在
   fdtd.delete("nonexistent")
   ```
   解决方案：使用 `hastag` 或 `hasexisting` 命令先检查对象是否存在。

2. **权限不足错误**
   ```python
   # 错误：对象被锁定，无法删除
   fdtd.delete("locked_object")
   ```
   解决方案：先解锁对象或检查对象状态。

3. **类型不匹配错误**
   ```python
   # 错误：类型名称无效
   fdtd.delete("type", "invalid_type")
   ```
   解决方案：使用正确的对象类型名称。

4. **模式匹配错误**
   ```python
   # 错误：通配符模式没有匹配任何对象
   fdtd.delete("nonexistent_*")
   ```
   解决方案：检查模式拼写或使用 `get("all")` 查看可用对象。

### Python 错误处理示例

```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addrect("test_rect", x=0, y=0, z=0, x_span=1e-6, material="Si")
    
    # 成功删除
    fdtd.delete("test_rect")
    print("对象删除成功")
    
    # 尝试删除不存在的对象
    fdtd.delete("nonexistent")
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
    # 检查错误类型
    error_str = str(e).lower()
    if "object" in error_str and "not found" in error_str:
        print("错误: 对象不存在")
    elif "locked" in error_str or "permission" in error_str:
        print("错误: 对象被锁定或权限不足")
    elif "type" in error_str and "not found" in error_str:
        print("错误: 对象类型无效")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
    
finally:
    # 清理
    try:
        fdtd.delete("test_rect")
    except:
        pass
```

## 使用示例

### 示例 1：删除单个对象

#### LSF 脚本
```lumerical
// 创建几个测试对象
addrect;
set("name", "rect1");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 1);
set("y span", 1);
set("material", "Si");

addcircle;
set("name", "circle1");
set("x", 2);
set("y", 0);
set("z", 0);
set("radius", 0.5);
set("material", "SiO2");

addrect;
set("name", "rect2");
set("x", 4);
set("y", 0);
set("z", 0);
set("x span", 1.5);
set("y span", 0.5);
set("material", "Au");

? "创建的对象:";
?all;  // 列出所有对象

// 删除单个对象
? "删除 'rect1'...";
delete("rect1");

? "删除后的对象:";
?all;

// 验证删除
if (hastag("rect1")) {
    ? "错误: rect1 仍然存在!";
} else {
    ? "正确: rect1 已被删除";
}

// 删除另一个对象
? "删除 'circle1'...";
delete("circle1");

? "最终对象列表:";
?all;
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建几个测试对象
fdtd.addrect("rect1", x=0, y=0, z=0, x_span=1, y_span=1, material="Si")
fdtd.addcircle("circle1", x=2, y=0, z=0, radius=0.5, material="SiO2")
fdtd.addrect("rect2", x=4, y=0, z=0, x_span=1.5, y_span=0.5, material="Au")

print("创建的对象:")
fdtd.eval("?all;")  # 列出所有对象

# 删除单个对象
print("\n删除 'rect1'...")
fdtd.delete("rect1")

print("删除后的对象:")
fdtd.eval("?all;")

# 验证删除
try:
    rect1_props = fdtd.get("rect1")
    print("错误: rect1 仍然存在!")
except Exception as e:
    print("正确: rect1 已被删除")

# 删除另一个对象
print("\n删除 'circle1'...")
fdtd.delete("circle1")

print("最终对象列表:")
fdtd.eval("?all;")
```

### 示例 2：使用通配符模式删除多个对象
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建一组具有相似名称的对象
for i in range(5):
    fdtd.addrect(f"waveguide_{i}", 
                 x=i*2, y=0, z=0, 
                 x_span=0.5, y_span=0.22, 
                 material="Si")
    
for i in range(3):
    fdtd.addcircle(f"hole_{i}",
                   x=i*2 + 1, y=0, z=0,
                   radius=0.1,
                   material="Air")

print("创建的对象:")
fdtd.eval("?all;")

# 删除所有 waveguide_* 对象
print("\n删除所有 waveguide_* 对象...")
fdtd.delete("waveguide_*")  # 通配符模式

print("删除后的对象:")
fdtd.eval("?all;")

# 删除所有 hole_* 对象
print("\n删除所有 hole_* 对象...")
fdtd.delete("hole*")  # 另一种通配符格式

print("最终对象列表:")
fdtd.eval("?all;")

# 测试更复杂的模式
fdtd.addrect("test_1_a", x=0, y=0, material="Si")
fdtd.addrect("test_2_b", x=2, y=0, material="Si")
fdtd.addrect("other_3_c", x=4, y=0, material="Si")

print("\n创建测试对象:")
fdtd.eval("?rect;")

# 删除匹配 test_* 的对象
print("\n删除 test_* 对象...")
fdtd.delete("test_*")

print("剩余矩形对象:")
fdtd.eval("?rect;")
```

### 示例 3：按类型删除对象
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建各种类型的对象
fdtd.addrect("Si_wg", x=0, y=0, material="Si")          # 矩形
fdtd.addcircle("Air_hole", x=2, y=0, material="Air")    # 圆形
fdtd.adddipole("dipole_source", x=1, y=1)               # 偶极子源
fdtd.addindex("index_monitor", x=0, y=0)                # 折射率监视器
fdtd.addtime("time_monitor", x=2, y=2)                  # 时域监视器
fdtd.addmesh("custom_mesh", x=1, y=0)                   # 自定义网格

print("所有对象类型:")
fdtd.eval("?all;")

# 只删除矩形对象
print("\n删除所有矩形对象...")
fdtd.delete("type", "rect")

print("删除矩形后的对象:")
fdtd.eval("?all;")

# 只删除监视器对象
print("\n删除所有监视器对象...")
# 注意：需要知道监视器的具体类型名称
fdtd.delete("type", "index")
fdtd.delete("type", "time")

print("删除监视器后的对象:")
fdtd.eval("?all;")

# 删除光源
print("\n删除所有光源...")
fdtd.delete("type", "dipole")

print("最终对象列表:")
fdtd.eval("?all;")

# 按类型删除的通用函数
def delete_by_type(session, object_type):
    """删除指定类型的所有对象"""
    
    # 获取所有对象
    session.eval(f"list = get(\"all\");")
    all_objects = session.get("list")
    
    if not all_objects:
        return 0
    
    deleted_count = 0
    for obj_name in all_objects:
        # 获取对象类型
        session.eval(f"obj_type = get(\"{obj_name}\", \"type\");")
        obj_type = session.get("obj_type")
        
        if obj_type == object_type:
            session.delete(obj_name)
            deleted_count += 1
            print(f"  删除 {obj_name} ({obj_type})")
    
    return deleted_count

print("\n使用通用函数删除网格对象...")
deleted = delete_by_type(fdtd, "mesh")
print(f"删除了 {deleted} 个网格对象")
```

### 示例 4：删除所有对象和清理场景
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建复杂场景
print("创建复杂仿真场景...")

# 创建波导结构
fdtd.addrect("main_wg", x=0, y=0, x_span=10, y_span=0.22, material="Si")

# 创建光栅耦合器
for i in range(20):
    fdtd.addrect(f"grating_{i}", 
                 x=i*0.5 - 5, y=0.3, 
                 x_span=0.25, y_span=0.1,
                 material="Si")

# 创建光源和监视器
fdtd.addmode("source", x=-4.5, y=0)
fdtd.addtime("monitor1", x=0, y=0)
fdtd.addfrequency("monitor2", x=4, y=0)

# 创建网格覆盖
fdtd.addmesh("mesh_override", x=0, y=0, dx=0.01, dy=0.01)

print("场景中的对象:")
object_count = fdtd.eval("return length(get(\"all\"));")
print(f"  对象总数: {object_count}")

# 按类别显示对象
print("\n对象分类统计:")
for obj_type in ["rect", "mode", "time", "frequency", "mesh"]:
    count = fdtd.eval(f"objects = get(\"all\"); count = 0; "
                     f"for(i=1:length(objects)){{"
                     f"  if(get(objects{i}, \"type\") == \"{obj_type}\"){{"
                     f"    count = count + 1;"
                     f"  }}"
                     f"}};"
                     f"return count;")
    print(f"  {obj_type}: {count}")

# 选择性清理：只删除几何结构
print("\n只删除几何结构（矩形）...")
fdtd.delete("type", "rect")

remaining = fdtd.eval("return length(get(\"all\"));")
print(f"  剩余对象: {remaining}")

# 删除所有监视器
print("\n删除所有监视器...")
fdtd.delete("type", "time")
fdtd.delete("type", "frequency")

remaining = fdtd.eval("return length(get(\"all\"));")
print(f"  剩余对象: {remaining}")

# 最后，删除所有对象
print("\n删除所有对象...")
fdtd.delete("all")

remaining = fdtd.eval("return length(get(\"all\"));")
print(f"  最终对象数: {remaining}")

# 验证场景为空
if remaining == 0:
    print("场景已完全清空")
else:
    print(f"警告: 仍有 {remaining} 个对象未删除")
    fdtd.eval("?all;")
```

### 示例 5：高级对象管理和安全删除
```python
import lumapi
import re

class ObjectManager:
    """高级对象管理工具"""
    
    def __init__(self, session):
        self.session = session
        self.deletion_history = []
    
    def get_all_objects(self):
        """获取所有对象列表"""
        self.session.eval("object_list = get(\"all\");")
        objects = self.session.get("object_list")
        return objects if objects else []
    
    def get_objects_by_type(self, object_type):
        """获取指定类型的所有对象"""
        all_objects = self.get_all_objects()
        filtered = []
        
        for obj_name in all_objects:
            self.session.eval(f"obj_type = get(\"{obj_name}\", \"type\");")
            obj_type = self.session.get("obj_type")
            
            if obj_type == object_type:
                filtered.append((obj_name, obj_type))
        
        return filtered
    
    def get_objects_by_pattern(self, pattern):
        """使用正则表达式获取匹配的对象"""
        all_objects = self.get_all_objects()
        filtered = []
        
        regex = re.compile(pattern)
        
        for obj_name in all_objects:
            if regex.match(obj_name):
                self.session.eval(f"obj_type = get(\"{obj_name}\", \"type\");")
                obj_type = self.session.get("obj_type")
                filtered.append((obj_name, obj_type))
        
        return filtered
    
    def safe_delete(self, object_name, require_confirmation=False):
        """安全删除对象（记录历史）"""
        
        # 检查对象是否存在
        try:
            self.session.eval(f"exists = hastag(\"{object_name}\");")
            exists = self.session.get("exists")
            
            if not exists:
                print(f"对象 '{object_name}' 不存在")
                return False
            
            # 获取对象信息（用于历史记录）
            self.session.eval(f"obj_type = get(\"{object_name}\", \"type\");")
            obj_type = self.session.get("obj_type")
            
            # 可选：要求确认
            if require_confirmation:
                print(f"将要删除: {object_name} ({obj_type})")
                # 在实际应用中，这里可以添加用户确认逻辑
            
            # 执行删除
            self.session.delete(object_name)
            
            # 记录删除历史
            self.deletion_history.append({
                'name': object_name,
                'type': obj_type,
                'timestamp': lumapi.gettime()  # 假设有这个函数
            })
            
            print(f"已删除: {object_name} ({obj_type})")
            return True
            
        except Exception as e:
            print(f"删除失败: {e}")
            return False
    
    def batch_delete_by_type(self, object_type, dry_run=False):
        """批量删除指定类型的所有对象"""
        
        objects = self.get_objects_by_type(object_type)
        
        if not objects:
            print(f"没有找到类型为 '{object_type}' 的对象")
            return 0
        
        print(f"找到 {len(objects)} 个类型为 '{object_type}' 的对象:")
        for obj_name, obj_type in objects:
            print(f"  {obj_name}")
        
        if dry_run:
            print("（干运行模式，不会实际删除）")
            return len(objects)
        
        deleted_count = 0
        for obj_name, obj_type in objects:
            if self.safe_delete(obj_name):
                deleted_count += 1
        
        print(f"成功删除 {deleted_count} 个对象")
        return deleted_count
    
    def batch_delete_by_pattern(self, pattern, dry_run=False):
        """批量删除匹配模式的所有对象"""
        
        objects = self.get_objects_by_pattern(pattern)
        
        if not objects:
            print(f"没有匹配模式 '{pattern}' 的对象")
            return 0
        
        print(f"找到 {len(objects)} 个匹配模式 '{pattern}' 的对象:")
        for obj_name, obj_type in objects:
            print(f"  {obj_name} ({obj_type})")
        
        if dry_run:
            print("（干运行模式，不会实际删除）")
            return len(objects)
        
        deleted_count = 0
        for obj_name, obj_type in objects:
            if self.safe_delete(obj_name):
                deleted_count += 1
        
        print(f"成功删除 {deleted_count} 个对象")
        return deleted_count
    
    def undo_last_deletion(self):
        """撤销最后一次删除（概念性，实际需要更复杂实现）"""
        
        if not self.deletion_history:
            print("没有删除历史")
            return False
        
        last_deletion = self.deletion_history[-1]
        print(f"最后一次删除: {last_deletion['name']} ({last_deletion['type']})")
        
        # 注意：实际撤销需要重新创建对象，这通常需要保存对象的所有属性
        print("警告: 完全撤销需要保存对象的完整状态信息")
        print("建议使用 Lumerical 的内置 undo 功能或提前备份重要对象")
        
        return False  # 简化实现
    
    def cleanup_orphaned_objects(self):
        """清理孤立对象（没有引用的对象）"""
        
        all_objects = self.get_all_objects()
        
        # 这里可以添加逻辑来识别孤立对象
        # 例如：检查对象是否在组中、是否有父对象等
        
        print(f"总对象数: {len(all_objects)}")
        # 简化实现：显示所有对象
        for obj in all_objects:
            print(f"  {obj}")
        
        return len(all_objects)

# 使用示例
fdtd = lumapi.FDTD()
manager = ObjectManager(fdtd)

# 创建测试对象
print("创建测试对象...")
for i in range(3):
    fdtd.addrect(f"structure_{i}", x=i*2, y=0, material="Si")
    fdtd.addcircle(f"feature_{i}", x=i*2 + 1, y=0, material="Air")

fdtd.addmode("optical_source", x=0, y=1)
fdtd.addtime("time_monitor_1", x=2, y=1)

print("\n所有对象:")
print(manager.get_all_objects())

# 按类型批量删除
print("\n批量删除所有矩形对象...")
deleted = manager.batch_delete_by_type("rect", dry_run=True)  # 先干运行
print(f"将删除 {deleted} 个矩形对象")

# 实际删除
deleted = manager.batch_delete_by_type("rect", dry_run=False)
print(f"实际删除 {deleted} 个矩形对象")

print("\n剩余对象:")
print(manager.get_all_objects())

# 按模式批量删除
print("\n批量删除所有 feature_* 对象...")
deleted = manager.batch_delete_by_pattern(r"feature_\d+", dry_run=False)
print(f"删除 {deleted} 个对象")

print("\n最终对象列表:")
print(manager.get_all_objects())

# 查看删除历史
print("\n删除历史:")
for hist in manager.deletion_history:
    print(f"  {hist['name']} ({hist['type']})")

# 安全删除单个对象
print("\n安全删除测试...")
manager.safe_delete("optical_source", require_confirmation=False)

print("\n最终状态:")
remaining = manager.get_all_objects()
if remaining:
    print(f"剩余对象: {remaining}")
else:
    print("没有剩余对象")
```

## 注意事项

1. **不可逆操作**：删除操作是永久性的（除非使用 `undo`）。在删除重要对象前建议先保存项目。

2. **依赖关系**：删除父对象可能会影响子对象。例如，删除一个组可能会删除组内的所有对象。

3. **撤销限制**：`undo` 命令只能撤销有限步数的操作。复杂的批量删除可能无法完全撤销。

4. **名称匹配**：通配符模式匹配遵循 Lumerical 的规则。`*` 匹配任意字符序列，`?` 匹配单个字符。

5. **类型名称**：对象类型名称是内部标识符，可能因 Lumerical 版本而异。常见类型包括："rect", "circle", "poly", "sphere", "cylinder", "source", "monitor", "mesh" 等。

6. **性能考虑**：删除大量对象可能影响性能。对于大规模清理，考虑使用批量删除或脚本操作。

7. **错误处理**：尝试删除不存在的对象通常会导致错误。使用 `hastag` 命令先检查对象是否存在。

8. **与 `remove` 的区别**：某些情况下 `remove` 命令也用于删除对象，但语义可能略有不同。`delete` 是更通用的删除命令。

9. **锁定对象**：被锁定（locked）的对象可能无法直接删除。需要先解锁或使用强制删除选项（如果可用）。

10. **脚本兼容性**：在脚本中大量使用删除操作时，确保脚本的健壮性，处理对象不存在的情况。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 可删除所有类型的对象 |
| MODE Solutions | ✅ 完全支持 | 可删除所有类型的对象 |
| DEVICE | ✅ 完全支持 | 可删除所有类型的对象 |
| INTERCONNECT | ✅ 完全支持 | 可删除元件、端口、连接等 |

## 相关命令

- `addrect` - 添加矩形（创建对象）
- `addcircle` - 添加圆形（创建对象）
- `select` - 选择对象（为删除做准备）
- `get` - 获取对象属性（检查对象）
- `set` - 设置对象属性（修改而非删除）
- `copy` - 复制对象（备份重要对象）
- `undo` - 撤销操作（包括删除）
- `hastag` - 检查对象是否存在
- `cleargrid` - 清除网格（特定类型的删除）
- `clear` - 清除变量（不同于删除对象）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2024-01-01 | 初始版本，包含基本语法和示例 |
| 1.1 | 2025-12-01 | 添加详细配置属性表格和Python API示例 |
| 1.2 | 2026-01-31 | 完善错误处理章节，补充LSF脚本示例，添加版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - Delete Command
2. Lumerical Python API Documentation - session.delete() Method
3. Lumerical Knowledge Base: "Object Management and Cleanup"
4. Lumerical User Guide: "Working with Simulation Objects"

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*