# `cellgroup` - 设置单元组

## 概述

`cellgroup` 命令用于在 MODE Solutions 中定义和配置单元组（cell group）。单元组通常用于周期性结构仿真，如光子晶体、光栅等，通过定义周期性边界条件来模拟无限扩展的结构。

该命令创建一个单元组对象，允许用户指定周期性方向、周期长度、网格设置等参数，用于在 MODE 的 FDE（本征模展开）或 EME（特征模展开）求解器中设置周期性边界条件。

## 语法

### LSF 语法
```lumerical
cellgroup(name);
cellgroup(name, property, value, ...);
```

### Python API
```python
session.cellgroup(name)
session.cellgroup(name, property1=value1, property2=value2, ...)
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `name` | string | 单元组的名称。如果名称已存在，则修改现有单元组；否则创建新单元组。 | 是 |
| `property` | string | 要设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

通过 `set` 命令可以配置以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | number | 0 | 单元组在 x 方向的位置（μm）。 |
| `y` | number | 0 | 单元组在 y 方向的位置（μm）。 |
| `z` | number | 0 | 单元组在 z 方向的位置（μm）。 |
| `x span` | number | 1 | 单元组在 x 方向的周期长度（μm）。 |
| `y span` | number | 1 | 单元组在 y 方向的周期长度（μm）。 |
| `z span` | number | 1 | 单元组在 z 方向的周期长度（μm）。 |
| `x min` | number | -0.5 | 单元组在 x 方向的最小边界（相对于 x 位置）。 |
| `x max` | number | 0.5 | 单元组在 x 方向的最大边界（相对于 x 位置）。 |
| `y min` | number | -0.5 | 单元组在 y 方向的最小边界（相对于 y 位置）。 |
| `y max` | number | 0.5 | 单元组在 y 方向的最大边界（相对于 y 位置）。 |
| `z min` | number | -0.5 | 单元组在 z 方向的最小边界（相对于 z 位置）。 |
| `z max` | number | 0.5 | 单元组在 z 方向的最大边界（相对于 z 位置）。 |
| `enabled` | bool | true | 是否启用该单元组。 |
| `mesh order` | number | 2 | 网格划分顺序。 |
| `override global mesh settings` | bool | false | 是否覆盖全局网格设置。 |
| `dx` | number | 0.02 | x 方向网格步长（μm）。 |
| `dy` | number | 0.02 | y 方向网格步长（μm）。 |
| `dz` | number | 0.02 | z 方向网格步长（μm）。 |
| `grid mesh cells per wavelength` | number | 20 | 每波长网格单元数。 |
| `use relative coordinates` | bool | false | 是否使用相对坐标。 |
| `color` | string | "custom" | 显示颜色（RGB 值或颜色名称）。 |

## 使用示例

### 示例 1：创建基本单元组
```python
import lumapi

# 创建 MODE 会话
mode = lumapi.MODE()

# 创建单元组
mode.cellgroup("cell_1")

# 设置周期长度
mode.set("cell_1", "x span", 1.0)  # 1 μm 周期
mode.set("cell_1", "y span", 1.0)
mode.set("cell_1", "z span", 0.5)

# 启用单元组
mode.set("cell_1", "enabled", True)

# 保存项目
mode.save("cellgroup_example.lms")
```

### 示例 2：创建单元组并配置网格设置
```python
import lumapi

mode = lumapi.MODE()

# 创建单元组并直接设置属性
mode.cellgroup("photonic_crystal", 
               x=0, y=0, z=0,
               x_span=0.5,  # 500 nm 周期
               y_span=0.5,
               z_span=0.22,  # 220 nm 厚度
               enabled=True,
               override_global_mesh_settings=True,
               dx=0.01,      # 10 nm 网格
               dy=0.01,
               dz=0.005)

# 查看单元组属性
props = mode.get("photonic_crystal")
print("单元组属性:", props)
```

### 示例 3：在 FDE 求解器中使用单元组
```python
import lumapi

mode = lumapi.MODE()

# 添加 FDE 求解器
mode.addfde("fde_solver")

# 创建单元组
mode.cellgroup("grating_cell",
               x_span=0.7,   # 700 nm 周期
               y_span=0.7,
               z_span=0.3)

# 设置 FDE 求解器使用单元组
mode.set("fde_solver", "x min", -0.35)  # 半个周期
mode.set("fde_solver", "x max", 0.35)
mode.set("fde_solver", "y min", -0.35)
mode.set("fde_solver", "y max", 0.35)

# 运行仿真
mode.run("fde_solver")
```

## 注意事项

1. **周期性方向**：单元组通常用于定义周期性结构，`x span`、`y span`、`z span` 定义了周期长度。在 FDE 或 EME 求解器中，需要将求解区域设置为单元组的一个周期。

2. **网格设置**：如果 `override global mesh settings` 为 `true`，则单元组内的网格设置将覆盖全局网格设置。这对于需要精细网格的区域特别有用。

3. **边界条件**：单元组通常与周期性边界条件一起使用。在 MODE 求解器中，需要正确设置边界条件类型为 "Periodic"。

4. **多个单元组**：可以创建多个单元组，用于模拟复杂的周期性结构或超表面。

5. **与求解器的配合**：单元组需要与 FDE 或 EME 求解器配合使用。确保求解器的区域设置与单元组的周期一致。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| MODE Solutions | ✅ 完全支持 | 主要用于 FDE 和 EME 求解器中的周期性结构 |
| FDTD Solutions | ❌ 不支持 | FDTD 使用不同的周期性边界设置方法 |
| DEVICE | ❌ 不支持 | |
| INTERCONNECT | ❌ 不支持 | |

## 相关命令

- `addfde` - 添加 FDE 求解器
- `addeme` - 添加 EME 求解器
- `set` - 设置对象属性
- `get` - 获取对象属性
- `addmesh` - 添加网格覆盖区
- `addimport` - 添加导入对象（可用于导入周期性结构）