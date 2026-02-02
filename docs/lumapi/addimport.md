# addimport

## 概述

`addimport` 命令用于在仿真中添加导入对象。导入对象允许将外部文件（如 CAD 文件、几何数据、材料数据等）导入到 Lumerical 仿真环境中，支持多种文件格式，实现与其他 CAD/CAE 工具的数据交换和协同设计。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addimport;
```

### Python API (Lumapi)
```python
session.addimport()
```

## 参数

`addimport` 命令没有直接参数，但需要通过后续的 `set` 命令配置导入对象属性。

## 配置属性

添加导入对象后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "import" | 导入对象名称 |
| `enabled` | bool | true | 是否启用对象 |
| `visible` | bool | true | 是否可见 |
| `type` | string | "geometry" | 导入类型："geometry", "material", "data", "script" |

### 2. 文件设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `filename` | string | "" | 源文件路径 |
| `file format` | string | "gds" | 文件格式 |
| `import units` | string | "m" | 导入单位："m", "um", "nm", "mm" |
| `scale factor` | float | 1.0 | 缩放因子 |
| `invert` | bool | false | 是否反转（对于布尔运算） |
| `merge tolerance` | float | 1e-12 | 合并容差 (m) |

### 支持的文件格式：
- **GDSII**: `"gds"`, `"gdsii"` - 光刻掩模版文件
- **OASIS**: `"oasis"` - 高级版图文件
- **DXF**: `"dxf"` - AutoCAD 绘图交换格式
- **STL**: `"stl"` - 三维网格文件
- **OBJ**: `"obj"` - 三维对象文件
- **STEP**: `"step"`, `"stp"` - 三维 CAD 文件
- **IGES**: `"iges"`, `"igs"` - 三维 CAD 文件
- **CSV**: `"csv"` - 逗号分隔值数据
- **MAT**: `"mat"` - MATLAB 数据文件

### 3. 几何变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 导入对象中心坐标 (m) |
| `rotation x` | float | 0 | X 轴旋转角度 (度) |
| `rotation y` | float | 0 | Y 轴旋转角度 (度) |
| `rotation z` | float | 0 | Z 轴旋转角度 (度) |
| `flip x` | bool | false | 是否沿 X 轴翻转 |
| `flip y` | bool | false | 是否沿 Y 轴翻转 |
| `flip z` | bool | false | 是否沿 Z 轴翻转 |
| `transform matrix` | matrix | 单位矩阵 | 4×4 变换矩阵 |

### 4. 层映射（用于版图文件）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `layer map` | matrix | [] | 层映射表 |
| `source layer` | int | 0 | 源层编号 |
| `target layer` | int | 1 | 目标层编号 |
| `import layers` | string | "all" | 导入层："all", "selected" |
| `layer filter` | matrix | [] | 层过滤器 |
| `datatype` | int | 0 | 数据类型（GDSII/OASIS） |

### 5. 材料设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material` | string | "<Object defined dielectric>" | 材料名称 |
| `index` | float | 1.0 | 折射率（当 material 为 "<Object defined dielectric>" 时使用） |
| `material mapping` | matrix | [] | 材料映射表 |
| `layer to material` | bool | false | 是否按层分配材料 |
| `default material` | string | "SiO2" | 默认材料 |

### 6. 网格与渲染
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh order` | int | 2 | 网格顺序 |
| `override mesh order from material database` | bool | false | 是否覆盖材料数据库中的网格顺序 |
| `render type` | string | "detailed" | 渲染类型："detailed", "wireframe", "bounding box" |
| `simplify geometry` | bool | false | 是否简化几何 |
| `simplification tolerance` | float | 1e-9 | 简化容差 (m) |
| `smoothing` | bool | true | 是否平滑处理 |

### 7. 数据导入设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `data type` | string | "scalar" | 数据类型："scalar", "vector", "matrix" |
| `data variable` | string | "" | 数据变量名 |
| `interpolation` | string | "linear" | 插值方法："linear", "nearest", "cubic" |
| `sampling` | string | "uniform" | 采样方式 |
 | `normalize` | bool | false | 是否归一化数据 |

## 返回值

`addimport` 命令没有直接的返回值。成功执行后，会在仿真中添加一个导入对象，该对象可以通过 `set` 命令配置导入属性和文件设置。

## 示例

### 示例 1：导入 GDSII 版图文件
```python
import lumapi

# 创建会话
session = lumapi.FDTD()

# 添加导入对象
session.addimport()

# 配置导入属性
session.set("name", "photonics_circuit")
session.set("filename", "C:/designs/circuit.gds")
session.set("file format", "gds")
session.set("import units", "um")  # GDS 文件通常使用微米

# 设置几何变换
session.set("x", 0)
session.set("y", 0)
session.set("z", 0)
session.set("scale factor", 1e-6)  # 将微米转换为米

# 配置层映射（将 GDS 层 1 映射到材料 Si）
session.set("layer map", [[1, 1]])  # [源层, 目标层]
session.set("material", "Si (Silicon) - Palik")
session.set("layer to material", True)
```

### 示例 2：导入 STL 三维模型
```python
import lumapi

session = lumapi.FDTD()

# 添加导入对象
session.addimport()
session.set("name", "3d_structure")
session.set("filename", "C:/models/waveguide.stl")
session.set("file format", "stl")
session.set("import units", "m")

# 设置变换
session.set("rotation x", 90)  # 旋转90度
session.set("rotation y", 0)
session.set("rotation z", 45)  # 旋转45度
session.set("scale factor", 0.5)  # 缩放50%

# 配置材料
session.set("material", "<Object defined dielectric>")
session.set("index", 3.45)  # 硅的折射率

# 配置网格设置
session.set("mesh order", 3)
session.set("render type", "detailed")
session.set("simplify geometry", True)
session.set("simplification tolerance", 1e-8)
```

### 示例 3：导入材料数据文件
```python
import lumapi

session = lumapi.FDTD()

# 添加导入对象用于材料数据
session.addimport()
session.set("name", "material_data")
session.set("type", "material")
session.set("filename", "C:/materials/silicon_nk.csv")
session.set("file format", "csv")

# 配置数据导入设置
session.set("data type", "matrix")
session.set("data variable", "nk_data")
session.set("interpolation", "cubic")

# 创建自定义材料基于导入数据
session.addmaterial()
session.set("name", "custom_silicon")
session.set("type", "dielectric")
session.set("model", "sampled data")
session.set("sampled data", "nk_data")  # 使用导入的数据

# 将导入对象与材料关联
session.set("reference material", "custom_silicon")
```

## 注意事项

1. **单位一致性**：注意源文件单位与 Lumerical 单位（米）的转换
2. **文件路径**：使用绝对路径或确保文件在可访问位置
3. **内存使用**：复杂三维模型可能占用大量内存
4. **网格质量**：导入的几何可能需要修复以获得良好网格
5. **版本兼容性**：确保文件格式与 Lumerical 版本兼容
6. **层映射**：对于版图文件，正确设置层映射至关重要

## 错误处理

### 常见错误
1. **文件未找到**
   - 错误信息：`File not found`
   - 解决方案：检查文件路径和权限

2. **不支持的格式**
   - 错误信息：`Unsupported file format`
   - 解决方案：检查文件格式是否受支持

3. **内存不足**
   - 错误信息：`Insufficient memory`
   - 解决方案：简化几何或使用较小文件

4. **无效的层映射**
   - 错误信息：`Invalid layer mapping`
   - 解决方案：检查层映射表格式

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加导入对象
    fdtd.addimport()
    fdtd.set("name", "imported_geometry")
    fdtd.set("filename", "nonexistent.gds")  # 可能引发错误
    fdtd.set("file format", "gds")
    
except lumapi.LumApiError as e:
    print(f"导入失败: {e}")
    
    # 检查具体错误类型
    if "file not found" in str(e).lower():
        print("错误: 文件未找到")
    elif "unsupported format" in str(e).lower():
        print("错误: 不支持的格式")
    elif "memory" in str(e).lower():
        print("错误: 内存不足")
    elif "layer" in str(e).lower():
        print("错误: 无效的层映射")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持
- **MODE Solutions**: 支持
- **DEVICE**: 支持
- **INTERCONNECT**: 支持（有限）

## 相关命令

- `addmaterial` - 添加材料
- `addrect` - 添加矩形
- `addcylinder` - 添加圆柱体
- `set` - 设置对象属性
- `import` - 导入数据（函数）
- `export` - 导出数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 OASIS 格式支持 |
| Lumerical 2019a | 改进三维网格导入性能 |
| Lumerical 2018a | 新增 STEP/IGES 格式支持 |

## 参考

1. Lumerical 导入/导出指南
2. Lumerical 支持的文件格式文档
3. GDSII/OASIS 格式规范

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*