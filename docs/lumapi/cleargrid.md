# `cleargrid` - 清除网格

## 概述

`cleargrid` 命令用于清除仿真中的自定义网格设置。在 Lumerical 仿真中，网格划分对计算精度和性能有重要影响。用户可以在特定区域设置精细网格（通过 `addmesh` 命令），而 `cleargrid` 命令则用于移除这些自定义网格设置，恢复全局网格设置。

该命令在需要重新配置网格设置或清除不必要的网格覆盖区时非常有用，有助于优化仿真设置和解决网格相关问题。

## 语法

### LSF 语法
```lumerical
cleargrid;                    # 清除所有自定义网格
cleargrid(mesh_name);         # 清除指定网格覆盖区
cleargrid(mesh_name1, mesh_name2, ...);  # 清除多个网格覆盖区
cleargrid("all");             # 清除所有自定义网格（显式指定）
```

### Python API
```python
session.cleargrid()                     # 清除所有自定义网格
session.cleargrid(mesh_name)            # 清除指定网格覆盖区
session.cleargrid(mesh_name1, mesh_name2, ...)  # 清除多个网格覆盖区
session.cleargrid("all")                # 清除所有自定义网格（显式指定）
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `mesh_name` | string | 要清除的网格覆盖区的名称。如果不提供参数，则清除所有自定义网格。 | 可选 |

## 配置属性

`cleargrid` 命令没有可配置属性。它直接移除网格覆盖区对象。

## 返回值

`cleargrid` 命令没有返回值。成功执行后，指定的网格覆盖区将从仿真中移除。如果命令失败（例如尝试清除不存在的网格覆盖区），Lumerical 可能会抛出错误或静默忽略。

在 Python API 中，`session.cleargrid()` 通常返回 `None`。成功清除不返回任何值，失败时可能抛出异常。

## 错误处理

### 常见错误

1. **网格覆盖区不存在错误**
   ```python
   # 错误：网格覆盖区 "nonexistent_mesh" 不存在
   fdtd.cleargrid("nonexistent_mesh")
   ```
   解决方案：使用 `?mesh` 命令先检查网格覆盖区是否存在，或使用安全清除模式。

2. **网格被锁定错误**
   ```python
   # 错误：网格正在被仿真使用或被锁定
   fdtd.cleargrid("active_mesh")
   ```
   解决方案：停止仿真运行，或等待仿真完成后再清除网格。

3. **参数类型错误**
   ```python
   # 错误：参数类型不正确
   fdtd.cleargrid(123)  # 参数必须是字符串
   ```
   解决方案：确保参数是字符串类型的网格名称。

4. **内存释放错误**
   ```python
   # 错误：清除网格时内存释放失败
   fdtd.cleargrid("large_mesh")
   ```
   解决方案：尝试分步清除，或重启 Lumerical 会话。

### Python 错误处理示例
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 添加一些网格覆盖区
    fdtd.addmesh("mesh1", x=0, y=0, z=0, x_span=1, y_span=1, z_span=1)
    fdtd.addmesh("mesh2", x=1, y=1, z=0, x_span=0.5, y_span=0.5, z_span=0.5)
    
    # 成功清除
    fdtd.cleargrid("mesh1")
    print("网格 mesh1 清除成功")
    
    # 清除不存在的网格
    fdtd.cleargrid("nonexistent_mesh")
    
    # 清除所有网格
    fdtd.cleargrid()
    print("所有网格清除成功")
    
except lumapi.LumApiError as e:
    error_str = str(e).lower()
    
    if "mesh" in error_str and "not found" in error_str:
        print("错误: 网格覆盖区不存在")
    elif "locked" in error_str or "active" in error_str:
        print("错误: 网格被锁定或正在使用")
    elif "argument" in error_str or "parameter" in error_str:
        print("错误: 参数类型错误")
    elif "memory" in error_str:
        print("错误: 内存释放失败")
    else:
        print(f"Lumerical API 错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 使用示例

### 示例 1：清除所有自定义网格

#### LSF 脚本
```lumerical
# 添加 FDTD 求解器
addfdtd("FDTD_solver", 
        x span: 5, 
        y span: 5, 
        z span: 2);

# 添加多个自定义网格覆盖区
addmesh("fine_mesh_1", 
        x: 0, y: 0, z: 0, 
        x span: 1, y span: 1, z span: 1,
        dx: 0.01, dy: 0.01, dz: 0.01);  # 精细网格

addmesh("fine_mesh_2", 
        x: 2, y: 1, z: 0,
        x span: 0.5, y span: 0.5, z span: 0.5,
        dx: 0.005, dy: 0.005, dz: 0.005);  # 超精细网格

?"添加自定义网格后:";
?"mesh";  # 列出所有网格覆盖区

# 清除所有自定义网格
cleargrid;

?"清除所有自定义网格后:";
?"mesh";  # 应该没有网格覆盖区

# 验证网格已清除
if (hasexisting("fine_mesh_1")) {
    ?"网格 fine_mesh_1 仍然存在";
} else {
    ?"所有自定义网格已被成功清除";
}
```

#### Python API
```python
import lumapi

# 创建 FDTD 会话
fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd("FDTD_solver", x_span=5, y_span=5, z_span=2)

# 添加多个自定义网格覆盖区
fdtd.addmesh("fine_mesh_1", x=0, y=0, z=0, 
             x_span=1, y_span=1, z_span=1,
             dx=0.01, dy=0.01, dz=0.01)  # 精细网格

fdtd.addmesh("fine_mesh_2", x=2, y=1, z=0,
             x_span=0.5, y_span=0.5, z_span=0.5,
             dx=0.005, dy=0.005, dz=0.005)  # 超精细网格

print("添加自定义网格后:")
fdtd.eval("?mesh;")  # 列出所有网格覆盖区

# 清除所有自定义网格
fdtd.cleargrid()

print("\n清除所有自定义网格后:")
fdtd.eval("?mesh;")  # 应该没有网格覆盖区

# 验证网格已清除
try:
    mesh_props = fdtd.get("fine_mesh_1")
    print(f"网格 fine_mesh_1 仍然存在: {mesh_props}")
except:
    print("所有自定义网格已被成功清除")
```

### 示例 2：清除特定网格覆盖区

#### LSF 脚本
```lumerical
# 添加 FDTD 求解器
addfdtd("solver", 
        x span: 10, 
        y span: 10, 
        z span: 2);

# 在不同区域添加不同精度的网格
addmesh("waveguide_mesh", 
        x: 0, y: 0, z: 0,
        x span: 0.5, y span: 0.22, z span: 10,
        dx: 0.005, dy: 0.005, dz: 0.02);  # 波导区域精细网格

addmesh("source_mesh", 
        x: -2, y: 0, z: 0,
        x span: 0.3, y span: 0.3, z span: 0.3,
        dx: 0.002, dy: 0.002, dz: 0.002);  # 光源区域超精细网格

addmesh("monitor_mesh", 
        x: 2, y: 0, z: 0,
        x span: 0.4, y span: 0.4, z span: 0.4,
        dx: 0.01, dy: 0.01, dz: 0.01);  # 监视器区域中等网格

?"初始网格覆盖区:";
?"mesh";

# 清除特定网格
cleargrid("source_mesh");  # 只清除光源区域的网格
?"清除 source_mesh 后:";
?"mesh";

# 清除多个网格
cleargrid("waveguide_mesh", "monitor_mesh");
?"清除所有自定义网格后:";
?"mesh";
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd("solver", x_span=10, y_span=10, z_span=2)

# 在不同区域添加不同精度的网格
fdtd.addmesh("waveguide_mesh", x=0, y=0, z=0,
             x_span=0.5, y_span=0.22, z_span=10,
             dx=0.005, dy=0.005, dz=0.02)  # 波导区域精细网格

fdtd.addmesh("source_mesh", x=-2, y=0, z=0,
             x_span=0.3, y_span=0.3, z_span=0.3,
             dx=0.002, dy=0.002, dz=0.002)  # 光源区域超精细网格

fdtd.addmesh("monitor_mesh", x=2, y=0, z=0,
             x_span=0.4, y_span=0.4, z_span=0.4,
             dx=0.01, dy=0.01, dz=0.01)  # 监视器区域中等网格

print("初始网格覆盖区:")
fdtd.eval("?mesh;")

# 清除特定网格
fdtd.cleargrid("source_mesh")  # 只清除光源区域的网格
print("\n清除 source_mesh 后:")
fdtd.eval("?mesh;")

# 清除多个网格
fdtd.cleargrid("waveguide_mesh", "monitor_mesh")
print("\n清除所有自定义网格后:")
fdtd.eval("?mesh;")
```

### 示例 3：在优化过程中动态管理网格
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def run_simulation_with_adaptive_mesh(device_width, use_fine_mesh=True):
    """根据设备尺寸和需要运行仿真"""
    
    # 清除之前的网格设置
    fdtd.cleargrid()  # 清除所有自定义网格
    
    # 设置基本仿真
    fdtd.addfdtd("solver", x_span=8, y_span=8, z_span=2,
                 mesh_accuracy=2)  # 中等全局网格精度
    
    # 添加波导结构
    fdtd.addrect("waveguide", x=0, y=0, z=0,
                 x_span=device_width, y_span=0.22, z_span=10,
                 material="Si")
    
    # 根据需要添加精细网格
    if use_fine_mesh and device_width < 0.5:
        # 对于窄波导，添加精细网格
        fdtd.addmesh("fine_waveguide_mesh", 
                     x=0, y=0, z=0,
                     x_span=device_width*1.5,  # 稍大于波导宽度
                     y_span=0.3, z_span=10,
                     dx=0.003, dy=0.003, dz=0.02)
        print(f"为 {device_width:.3f} μm 波导添加了精细网格")
    
    # 运行仿真
    fdtd.run()
    
    # 获取结果
    T = fdtd.getresult("monitor", "T")
    
    # 清除自定义网格以进行下一次迭代
    fdtd.cleargrid()
    
    return np.mean(T)

# 测试不同宽度
widths = [0.4, 0.45, 0.5, 0.55, 0.6]
results = []

for width in widths:
    # 窄波导使用精细网格，宽波导不使用
    use_fine = width < 0.5
    transmission = run_simulation_with_adaptive_mesh(width, use_fine)
    results.append(transmission)
    print(f"宽度 {width:.3f} μm: 传输率 = {transmission:.4f}")

print(f"\n最终结果: {results}")
```

### 示例 4：解决网格冲突问题
```python
import lumapi

fdtd = lumapi.FDTD()

def diagnose_mesh_issues():
    """诊断和解决网格相关问题"""
    
    # 设置仿真
    fdtd.addfdtd("solver", x_span=6, y_span=6, z_span=2)
    
    # 添加重叠的网格覆盖区（可能导致冲突）
    fdtd.addmesh("mesh1", x=0, y=0, z=0,
                 x_span=2, y_span=2, z_span=2,
                 dx=0.01, dy=0.01, dz=0.01)
    
    fdtd.addmesh("mesh2", x=0.5, y=0.5, z=0,
                 x_span=1, y_span=1, z_span=1,
                 dx=0.005, dy=0.005, dz=0.005)  # 与 mesh1 重叠
    
    print("当前网格覆盖区:")
    fdtd.eval("?mesh;")
    
    # 检查网格统计
    fdtd.eval("?solver::mesh;")
    
    # 尝试运行仿真（可能会因网格冲突而失败）
    try:
        fdtd.run()
        print("仿真成功运行")
    except Exception as e:
        print(f"仿真失败: {e}")
        print("尝试清除重叠的网格...")
        
        # 清除所有网格
        fdtd.cleargrid()
        print("所有网格已清除")
        
        # 重新添加非重叠网格
        fdtd.addmesh("new_mesh1", x=-1, y=0, z=0,
                     x_span=1, y_span=1, z_span=1,
                     dx=0.01, dy=0.01, dz=0.01)
        
        fdtd.addmesh("new_mesh2", x=1, y=0, z=0,
                     x_span=1, y_span=1, z_span=1,
                     dx=0.005, dy=0.005, dz=0.005)
        
        print("\n重新配置后的网格:")
        fdtd.eval("?mesh;")
        
        # 再次尝试运行
        fdtd.run()
        print("仿真现在成功运行")

# 运行诊断
diagnose_mesh_issues()
```

### 示例 5：批量清除网格模式
```python
import lumapi
import re

fdtd = lumapi.FDTD()

class MeshManager:
    """网格管理器，提供高级网格操作"""
    
    def __init__(self, session):
        self.session = session
    
    def list_meshes(self):
        """列出所有网格覆盖区"""
        self.session.eval("mesh_list = ?mesh;")
        meshes = self.session.get("mesh_list")
        self.session.clear("mesh_list")
        return meshes if meshes else []
    
    def clear_by_pattern(self, pattern):
        """使用正则表达式模式清除网格"""
        meshes = self.list_meshes()
        cleared = []
        
        for mesh in meshes:
            if re.search(pattern, mesh):
                self.session.cleargrid(mesh)
                cleared.append(mesh)
        
        return cleared
    
    def clear_temporary_meshes(self):
        """清除所有临时网格（名称以 'temp_' 开头）"""
        return self.clear_by_pattern(r'^temp_')
    
    def clear_old_meshes(self, keep_recent=2):
        """清除旧的网格，只保留最近创建的"""
        meshes = self.list_meshes()
        
        if len(meshes) <= keep_recent:
            return []
        
        # 假设网格按创建顺序列出（实际中可能需要更复杂的逻辑）
        to_clear = meshes[:-keep_recent] if keep_recent > 0 else meshes
        
        for mesh in to_clear:
            self.session.cleargrid(mesh)
        
        return to_clear

# 使用示例
manager = MeshManager(fdtd)

# 添加 FDTD 求解器
fdtd.addfdtd("solver", x_span=5, y_span=5, z_span=2)

# 添加各种网格
fdtd.addmesh("temp_mesh1", x=0, y=0, z=0, x_span=1, y_span=1, z_span=1)
fdtd.addmesh("perm_mesh_waveguide", x=0, y=0, z=0, x_span=0.5, y_span=0.22, z_span=10)
fdtd.addmesh("temp_mesh2", x=1, y=1, z=0, x_span=0.5, y_span=0.5, z_span=0.5)
fdtd.addmesh("mesh_optimization_1", x=-1, y=0, z=0, x_span=0.8, y_span=0.8, z_span=0.8)

print("初始网格:")
print(manager.list_meshes())

# 清除临时网格
cleared = manager.clear_temporary_meshes()
print(f"\n清除的临时网格: {cleared}")
print("剩余网格:")
print(manager.list_meshes())

# 清除所有网格
fdtd.cleargrid()
print(f"\n清除所有网格后: {manager.list_meshes()}")
```

## 注意事项

1. **网格覆盖区**：`cleargrid` 只清除通过 `addmesh` 命令添加的自定义网格覆盖区，不影响全局网格设置。

2. **不可恢复性**：清除的网格无法自动恢复。如果需要再次使用相同的网格设置，需要重新使用 `addmesh` 命令添加。

3. **仿真状态**：如果仿真正在运行或已经运行，清除网格不会自动重新运行仿真。需要手动重新运行仿真以应用新的网格设置。

4. **网格冲突**：当多个网格覆盖区重叠时，Lumerical 使用最精细的网格设置。清除其中一个可能影响其他重叠区域的网格分辨率。

5. **性能影响**：清除不必要的网格覆盖区可以减少内存使用和仿真准备时间，特别是对于包含大量网格覆盖区的复杂仿真。

6. **与网格精度的关系**：全局网格精度（通过求解器的 `mesh accuracy` 属性设置）不受 `cleargrid` 影响。`cleargrid` 只影响自定义的网格覆盖区。

7. **对象依赖性**：网格覆盖区通常与几何结构关联。清除网格覆盖区不会删除关联的几何结构，但可能影响该区域的网格质量。

8. **批量操作**：可以一次性清除多个网格覆盖区，只需在命令中列出它们的名称。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 主要用于 FDTD 仿真中的自定义网格 |
| MODE Solutions | ✅ 完全支持 | 用于 FDE 和 EME 求解器 |
| DEVICE | ✅ 完全支持 | 用于热和电仿真 |
| INTERCONNECT | ❌ 不支持 | INTERCONNECT 不使用相同的网格系统 |

## 相关命令

- `addmesh` - 添加网格覆盖区
- `set` - 设置网格属性（如 `dx`、`dy`、`dz`）
- `get` - 获取网格属性
- `?mesh` - 列出所有网格覆盖区
- `meshaccuracy` - 设置全局网格精度
- `meshorder` - 设置网格划分顺序

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本语法和示例 |
| 1.1 | 2026-01-31 | 添加返回值、错误处理章节、LSF脚本示例、版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - cleargrid 命令
2. Lumerical Python API Documentation - session.cleargrid() 方法
3. Lumerical Mesh Generation Guide - 网格管理和优化最佳实践

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*