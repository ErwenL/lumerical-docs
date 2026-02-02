# apply

## 概述

`apply` 命令用于对仿真对象应用变换操作，包括平移、旋转、缩放、镜像等几何变换，以及材料属性变换、坐标变换等。该命令支持单个对象或对象组的批量变换，是几何建模和参数化设计的重要工具。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
apply;
```

### Python API (Lumapi)
```python
session.apply()
```

## 参数

`apply` 命令没有直接参数，但需要通过后续的 `set` 命令配置变换类型、参数和目标对象。

## 配置属性

应用变换后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `target` | string | "" | 目标对象名称（空表示选中对象） |
| `transform type` | string | "translate" | 变换类型："translate", "rotate", "scale", "mirror", "affine", "custom" |
| `coordinate system` | string | "global" | 坐标系："global", "local", "parent", "custom" |
| `apply to` | string | "geometry" | 应用目标："geometry", "material", "both", "properties" |
| `in place` | bool | false | 是否原位变换（true）或创建副本（false） |

### 2. 平移变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `translation vector` | vector | [0, 0, 0] | 平移向量 (x, y, z) (m) |
| `translation distance` | float | 0 | 平移距离 (m) |
| `translation direction` | vector | [1, 0, 0] | 平移方向向量（单位向量） |
| `step size` | float | 0 | 步长（用于动画） |
| `relative` | bool | false | 是否相对当前位置 |

### 3. 旋转变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `rotation axis` | string | "z" | 旋转轴："x", "y", "z", "custom" |
| `rotation angle` | float | 0 | 旋转角度 (度) |
| `rotation center` | vector | [0, 0, 0] | 旋转中心点 (m) |
| `rotation direction` | string | "ccw" | 旋转方向："cw"（顺时针）, "ccw"（逆时针） |
| `quaternion` | vector | [1, 0, 0, 0] | 四元数表示 (w, x, y, z) |
| `euler angles` | vector | [0, 0, 0] | 欧拉角 (α, β, γ) (度) |

### 4. 缩放变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `scale factors` | vector | [1, 1, 1] | 缩放因子 (x, y, z) |
| `scale center` | vector | [0, 0, 0] | 缩放中心点 (m) |
| `uniform scaling` | bool | true | 是否均匀缩放 |
| `scale type` | string | "multiply" | 缩放类型："multiply", "add", "set" |
| `preserve aspect ratio` | bool | true | 是否保持纵横比 |

### 5. 镜像变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mirror plane` | string | "xy" | 镜像平面："xy", "yz", "zx", "custom" |
| `mirror point` | vector | [0, 0, 0] | 镜像点 (m) |
| `mirror normal` | vector | [0, 0, 1] | 镜像法线向量 |
| `copy original` | bool | true | 是否保留原始对象 |

### 6. 仿射变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `transformation matrix` | matrix | 单位矩阵 | 4×4 仿射变换矩阵 |
| `linear part` | matrix | 单位矩阵 | 3×3 线性变换部分 |
| `translation part` | vector | [0, 0, 0] | 平移部分 |
| `deformation` | bool | false | 是否允许非刚体变形 |
| `shear factors` | vector | [0, 0, 0] | 剪切因子 |

### 7. 自定义变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `custom function` | string | "" | 自定义变换函数 |
| `parameter names` | array | [] | 参数名称列表 |
| `parameter values` | array | [] | 参数值列表 |
| `transform script` | string | "" | 变换脚本 |
| `interpolation` | string | "linear" | 插值方法 |

### 8. 材料变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material mapping` | dict | {} | 材料映射关系 |
| `property scaling` | dict | {} | 属性缩放因子 |
| `gradient material` | bool | false | 是否创建梯度材料 |
| `material interpolation` | string | "linear" | 材料插值方法 |

### 9. 批量变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `batch processing` | bool | false | 是否批量处理 |
| `object list` | array | [] | 对象列表 |
| `pattern type` | string | "linear" | 阵列类型："linear", "circular", "grid", "random" |
| `pattern parameters` | dict | {} | 阵列参数 |
| `instance count` | int | 1 | 实例数量 |

### 10. 坐标变换
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `source coordinate system` | string | "global" | 源坐标系 |
| `target coordinate system` | string | "global" | 目标坐标系 |
| `coordinate transformation` | matrix | 单位矩阵 | 坐标变换矩阵 |
| `convert units` | bool | false | 是否转换单位 |

### 11. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `constraints` | dict | {} | 变换约束 |
| `validation` | bool | true | 是否验证变换结果 |
| `tolerance` | float | 1e-9 | 容差 (m) |
| `max iterations` | int | 100 | 最大迭代次数（用于优化） |
| `optimization` | bool | false | 是否启用优化 |

### 12. 历史与撤销
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `undo enabled` | bool | true | 是否允许撤销 |
| `history depth` | int | 10 | 历史记录深度 |
| `snapshot` | bool | false | 是否创建快照 |
| `description` | string | "" | 变换描述 |

## 返回值

`apply` 命令不直接返回值，而是修改目标对象的几何或属性。操作结果通过目标对象的变化体现：

- **成功应用**：目标对象被变换，可以通过 `get` 命令检查新属性
- **错误情况**：如果变换失败，目标对象保持不变，错误信息可通过错误处理配置获取
- **状态信息**：可以通过 `getv("apply", "last_operation")` 获取最后一次变换操作的状态信息

变换操作的影响：
1. **几何变化**：对象的位置、方向、尺寸等几何属性改变
2. **材料变化**：如果应用材料变换，对象的材料属性改变
3. **属性更新**：对象的其他相关属性可能相应更新
4. **历史记录**：变换操作被记录到对象历史中（如果启用）

## 使用示例

### 示例 1：基本几何变换

#### LSF 脚本
```lumerical
// 创建一个立方体
addrect;
set("name", "cube");
set("x span", 1e-6);
set("y span", 1e-6);
set("z span", 1e-6);

// 1. 平移变换：向右移动 2 μm
apply;
set("target", "cube");
set("transform type", "translate");
set("translation vector", [2e-6, 0, 0]);
set("description", "Translate cube 2 μm along x-axis");

// 2. 旋转变换：绕 Z 轴旋转 45 度
apply;
set("target", "cube");
set("transform type", "rotate");
set("rotation axis", "z");
set("rotation angle", 45);
set("rotation center", [2e-6, 0, 0]);  # 围绕新位置旋转
set("description", "Rotate cube 45° around z-axis");

// 3. 缩放变换：放大 1.5 倍
apply;
set("target", "cube");
set("transform type", "scale");
set("scale factors", [1.5, 1.5, 1.5]);
set("scale center", [2e-6, 0, 0]);  # 以当前位置为中心缩放
set("uniform scaling", true);
set("description", "Scale cube by factor 1.5");

// 4. 镜像变换：关于 YZ 平面镜像
apply;
set("target", "cube");
set("transform type", "mirror");
set("mirror plane", "yz");
set("mirror point", [0, 0, 0]);
set("copy original", true);  # 保留原始对象
set("description", "Mirror cube about YZ plane");

// 验证变换结果
cube_pos = get("cube", "x");
? "Cube final position: x = " + num2str(cube_pos) + " m";
```

#### Python API
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

# 创建一个立方体
session.addrect()
session.set("name", "cube")
session.set("x span", 1e-6)
session.set("y span", 1e-6)
session.set("z span", 1e-6)

# 1. 平移变换：向右移动 2 μm
session.apply()
session.set("target", "cube")
session.set("transform type", "translate")
session.set("translation vector", [2e-6, 0, 0])
session.set("description", "Translate cube 2 μm along x-axis")

# 2. 旋转变换：绕 Z 轴旋转 45 度
session.apply()
session.set("target", "cube")
session.set("transform type", "rotate")
session.set("rotation axis", "z")
session.set("rotation angle", 45)
session.set("rotation center", [2e-6, 0, 0])  # 围绕新位置旋转
session.set("description", "Rotate cube 45° around z-axis")

# 3. 缩放变换：放大 1.5 倍
session.apply()
session.set("target", "cube")
session.set("transform type", "scale")
session.set("scale factors", [1.5, 1.5, 1.5])
session.set("scale center", [2e-6, 0, 0])  # 以当前位置为中心缩放
session.set("uniform scaling", True)
session.set("description", "Scale cube by factor 1.5")

# 4. 镜像变换：关于 YZ 平面镜像
session.apply()
session.set("target", "cube")
session.set("transform type", "mirror")
session.set("mirror plane", "yz")
session.set("mirror point", [0, 0, 0])
session.set("copy original", True)  # 保留原始对象
session.set("description", "Mirror cube about YZ plane")

# 验证变换结果
cube_pos = session.get("cube", "x")
print(f"Cube final position: x = {cube_pos} m")
```

### 示例 2：仿射变换（复杂变形）

#### LSF 脚本
```lumerical
// 创建一个波导
addrect;
set("name", "original_waveguide");
set("x span", 5e-6);
set("y span", 0.22e-6);
set("z span", 0);
set("material", "Si");

// 定义仿射变换矩阵
// 4×4 变换矩阵：[线性部分 平移部分; 0 0 0 1]
// 旋转 30 度 + 剪切 + 平移
theta = 30;  // 30度
cos_theta = cos(theta*pi/180);
sin_theta = sin(theta*pi/180);

// 变换矩阵：旋转 + 剪切 + 平移
// 格式：[行1; 行2; 行3; 行4]
T = [cos_theta, 0.2, 0, 3e-6;      # 旋转 + X方向剪切 + X平移
     sin_theta, 1.0, 0, 1e-6;      # 旋转 + Y方向拉伸 + Y平移
     0, 0, 1.0, 0;                # Z方向不变
     0, 0, 0, 1];                 # 齐次坐标

apply;
set("target", "original_waveguide");
set("transform type", "affine");
set("transformation matrix", T);
set("in place", true);  # 修改原始对象
set("deformation", true);  # 允许非刚体变形
set("description", "Apply affine transformation with shear and rotation");

// 创建变换后的副本（不同材料）
apply;
set("target", "original_waveguide");
set("transform type", "affine");
set("transformation matrix", T);
set("in place", false);  # 创建副本
set("name", "transformed_waveguide");
set("material", "SiO2");  # 新副本使用不同材料
set("description", "Create transformed copy with different material");

// 验证变换
original_vertices = get("original_waveguide", "vertices");
transformed_vertices = get("transformed_waveguide", "vertices");
? "Original vertices shape: " + num2str(length(original_vertices)) + " elements";
? "Transformed vertices shape: " + num2str(length(transformed_vertices)) + " elements";
```

#### Python API
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 创建一个波导
session.addrect()
session.set("name", "original_waveguide")
session.set("x span", 5e-6)
session.set("y span", 0.22e-6)
session.set("z span", 0)
session.set("material", "Si")

# 定义仿射变换矩阵
# 4×4 变换矩阵：[线性部分 平移部分; 0 0 0 1]
# 这里应用剪切变换和旋转
theta = np.radians(30)  # 30度
cos_theta, sin_theta = np.cos(theta), np.sin(theta)

# 变换矩阵：旋转 + 剪切 + 平移
T = np.array([
    [cos_theta, 0.2, 0, 3e-6],      # 旋转 + X方向剪切 + X平移
    [sin_theta, 1.0, 0, 1e-6],      # 旋转 + Y方向拉伸 + Y平移
    [0, 0, 1.0, 0],                # Z方向不变
    [0, 0, 0, 1]                   # 齐次坐标
])

session.apply()
session.set("target", "original_waveguide")
session.set("transform type", "affine")
session.set("transformation matrix", T.tolist())
session.set("in place", True)  # 修改原始对象
session.set("deformation", True)  # 允许非刚体变形
session.set("description", "Apply affine transformation with shear and rotation")

# 创建变换后的副本（不同材料）
session.apply()
session.set("target", "original_waveguide")
session.set("transform type", "affine")
session.set("transformation matrix", T.tolist())
session.set("in place", False)  # 创建副本
session.set("name", "transformed_waveguide")
session.set("material", "SiO2")  # 新副本使用不同材料
session.set("description", "Create transformed copy with different material")

# 验证变换
original_vertices = session.get("original_waveguide", "vertices")
transformed_vertices = session.get("transformed_waveguide", "vertices")
print(f"Original vertices shape: {original_vertices.shape}")
print(f"Transformed vertices shape: {transformed_vertices.shape}")
```

### 示例 3：批量阵列变换
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

# 创建一个基本单元（Y分支）
def create_y_branch(name, position):
    session.addrect()
    session.set("name", f"{name}_input")
    session.set("x span", 0.5e-6)
    session.set("y span", 0.22e-6)
    session.set("z span", 0)
    session.set("x", position[0])
    session.set("y", position[1])
    
    session.addrect()
    session.set("name", f"{name}_arm1")
    session.set("x span", 0.5e-6)
    session.set("y span", 0.22e-6)
    session.set("z span", 0)
    session.set("x", position[0] + 2e-6)
    session.set("y", position[1] + 1e-6)
    
    session.addrect()
    session.set("name", f"{name}_arm2")
    session.set("x span", 0.5e-6)
    session.set("y span", 0.22e-6)
    session.set("z span", 0)
    session.set("x", position[0] + 2e-6)
    session.set("y", position[1] - 1e-6)

# 创建第一个Y分支
create_y_branch("y_branch_1", [0, 0])

# 获取所有Y分支组件
y_branch_components = ["y_branch_1_input", "y_branch_1_arm1", "y_branch_1_arm2"]

# 1. 线性阵列：沿X方向复制4次
session.apply()
session.set("batch processing", True)
session.set("object list", y_branch_components)
session.set("pattern type", "linear")
session.set("pattern parameters", {
    "direction": [1, 0, 0],  # X方向
    "spacing": 10e-6,        # 10 μm 间距
    "count": 4,              # 4个副本（包括原始）
    "instance naming": "index"  # 使用索引命名
})
session.set("description", "Create linear array of Y-branches")

# 2. 圆形阵列：旋转复制
session.apply()
session.set("batch processing", True)
session.set("object list", y_branch_components)
session.set("pattern type", "circular")
session.set("pattern parameters", {
    "center": [20e-6, 0, 0],      # 圆心位置
    "radius": 15e-6,              # 半径 15 μm
    "count": 8,                   # 8个副本
    "start_angle": 0,             # 起始角度
    "total_angle": 360,           # 总角度 360度
    "rotate_copies": True         # 旋转副本以适应圆形
})
session.set("description", "Create circular array of Y-branches")

# 3. 网格阵列：2D网格
session.apply()
session.set("batch processing", True)
# 选择新创建的对象进行网格排列
new_components = [f"y_branch_1_input_{i}" for i in range(4)] + \
                 [f"y_branch_1_arm1_{i}" for i in range(4)] + \
                 [f"y_branch_1_arm2_{i}" for i in range(4)]

session.set("object list", new_components)
session.set("pattern type", "grid")
session.set("pattern parameters", {
    "rows": 2,                    # 2行
    "columns": 2,                 # 2列
    "row_spacing": 20e-6,         # 行间距 20 μm
    "column_spacing": 20e-6,      # 列间距 20 μm
    "grid_center": [0, 0, 0]      # 网格中心
})
session.set("description", "Arrange Y-branches in 2D grid")

# 统计创建的对象数量
all_objects = session.getall()
y_branch_objects = [obj for obj in all_objects if "y_branch" in obj]
print(f"Total Y-branch components created: {len(y_branch_objects)}")
```

### 示例 4：参数化扫描变换
```python
import lumapi
import numpy as np

session = lumapi.DEVICE()

# 创建热源阵列基础单元
session.addrect()
session.set("name", "base_heater")
session.set("x span", 2e-6)
session.set("y span", 2e-6)
session.set("z span", 0.1e-6)
session.set("material", "Pt")  # 铂加热器
session.set("heat power", 0.1)  # 0.1 W

# 参数化扫描：不同尺寸和功率的热源
widths = np.linspace(1e-6, 3e-6, 5)    # 5种宽度：1-3 μm
powers = np.linspace(0.05, 0.2, 5)     # 5种功率：50-200 mW

# 创建参数化变换函数
transform_script = """
function apply_parameterized_transform(object_name, params)
    % params 包含：width, power, position_x, position_y
    
    % 1. 缩放变换：调整宽度
    apply;
    set("target", object_name);
    set("transform type", "scale");
    set("scale factors", [params.width/2e-6, params.width/2e-6, 1]);
    set("scale center", get(object_name, "position"));
    set("uniform scaling", true);
    
    % 2. 平移变换：移动到指定位置
    apply;
    set("target", object_name);
    set("transform type", "translate");
    current_pos = get(object_name, "position");
    new_pos = [params.position_x, params.position_y, current_pos(3)];
    set("translation vector", new_pos - current_pos);
    
    % 3. 更新材料属性（功率）
    setnamed(object_name, "heat power", params.power);
    
    % 4. 重命名对象
    new_name = sprintf("heater_w%.0fnm_p%.0fmW_x%.0fum", 
                      params.width*1e9, params.power*1e3, params.position_x*1e6);
    setnamed(object_name, "name", new_name);
end
"""

session.eval(transform_script)

# 应用参数化变换创建热源阵列
heaters = []
for i, width in enumerate(widths):
    for j, power in enumerate(powers):
        # 复制基础热源
        session.copy()
        session.set("target", "base_heater")
        session.set("new name", f"heater_{i}_{j}_temp")
        
        # 计算位置
        position_x = i * 5e-6  # 5 μm 列间距
        position_y = j * 5e-6  # 5 μm 行间距
        
        # 应用参数化变换
        params = {
            "width": width,
            "power": power,
            "position_x": position_x,
            "position_y": position_y
        }
        
        session.eval(f"""
        params = {params};
        apply_parameterized_transform("heater_{i}_{j}_temp", params);
        """)
        
        # 获取最终名称
        final_name = session.get(f"heater_{i}_{j}_temp", "name")
        heaters.append(final_name)
        
        print(f"Created {final_name}: width={width*1e9:.0f}nm, power={power*1e3:.0f}mW")

# 删除原始基础热源
session.delete()
session.set("target", "base_heater")

# 创建热源组并应用全局变换
session.apply()
session.set("batch processing", True)
session.set("object list", heaters)
session.set("transform type", "translate")
session.set("translation vector", [10e-6, 10e-6, 0])  # 整体移动
session.set("description", "Translate entire heater array")

# 应用全局缩放（模拟制造偏差）
session.apply()
session.set("batch processing", True)
session.set("object list", heaters)
session.set("transform type", "scale")
session.set("scale factors", [0.95, 0.95, 1.0])  # 缩小 5%
session.set("scale center", [0, 0, 0])
session.set("uniform scaling", True)
session.set("description", "Apply global scaling to simulate process variation")

# 分析变换后的热源阵列
print(f"\nHeater array analysis:")
print(f"Total heaters: {len(heaters)}")
print(f"Array dimensions: {len(widths)} × {len(powers)}")
print(f"Total heating power: {sum(powers)*len(widths):.3f} W")

# 保存变换参数
transform_params = {
    "widths": widths.tolist(),
    "powers": powers.tolist(),
    "spacing": 5e-6,
    "global_scale": 0.95,
    "global_translation": [10e-6, 10e-6, 0]
}

session.eval(f"""
transform_parameters = {transform_params};
save("heater_array_transform_params.mat", "transform_parameters");
""")
```

## 注意事项

1. **变换顺序**：多个变换的顺序影响最终结果，注意变换的累积效应
2. **坐标系**：明确变换使用的坐标系（全局、局部等）
3. **数值精度**：复杂变换可能引入数值误差，注意容差设置
4. **性能考虑**：批量变换大量对象可能影响性能，合理分块处理
5. **撤销操作**：重要变换前确保启用撤销功能
6. **对象依赖**：变换可能影响对象的父子关系和依赖关系
7. **网格质量**：极端变换可能恶化网格质量，需要重新网格化
8. **物理合理性**：变换结果应在物理合理范围内

## 错误处理

使用 `apply` 命令时可能遇到的常见错误及其解决方案：

### 1. 目标对象不存在
- **错误信息**: `"Target object not found"`
- **原因**: `target` 属性指定的对象名称不存在或未正确设置
- **解决方案**: 
  ```lumerical
  // 检查对象是否存在
  if (!exists("cube")) {
      ? "Object 'cube' does not exist. Creating...";
      addrect;
      set("name", "cube");
  }
  apply;
  set("target", "cube");
  ```

### 2. 无效的变换类型
- **错误信息**: `"Invalid transform type"`
- **原因**: `transform type` 属性值不在允许的列表中
- **解决方案**:
  ```lumerical
  // 使用有效的变换类型
  valid_types = {"translate", "rotate", "scale", "mirror", "affine", "custom"};
  if (!find(valid_types, requested_type)) {
      ? "Invalid transform type. Using 'translate' instead.";
      requested_type = "translate";
  }
  apply;
  set("transform type", requested_type);
  ```

### 3. 变换矩阵维度错误
- **错误信息**: `"Transformation matrix must be 4×4"`
- **原因**: 仿射变换矩阵不是 4×4 矩阵
- **解决方案**:
  ```lumerical
  // 确保矩阵为 4×4
  if (size(T) != [4, 4]) {
      ? "Reshaping matrix to 4×4";
      T = reshape(T, [4, 4]);
  }
  apply;
  set("transformation matrix", T);
  ```

### 4. 数值溢出或下溢
- **错误信息**: `"Numerical overflow in transformation"`
- **原因**: 变换参数值过大或过小，超出数值范围
- **解决方案**:
  ```lumerical
  // 限制参数范围
  translation_vector = [2e-6, 0, 0];
  max_value = 1e-3;  // 1 mm
  translation_vector = min(max(translation_vector, -max_value), max_value);
  apply;
  set("translation vector", translation_vector);
  ```

### 5. 内存不足
- **错误信息**: `"Insufficient memory for batch transformation"`
- **原因**: 批量变换对象数量过多，超出可用内存
- **解决方案**:
  ```lumerical
  // 分块处理大量对象
  object_list = {"obj1", "obj2", "obj3", "obj4", "obj5"};
  chunk_size = 2;
  for (i = 1:chunk_size:length(object_list)) {
      chunk = object_list(i:min(i+chunk_size-1, length(object_list)));
      apply;
      set("batch processing", true);
      set("object list", chunk);
      set("transform type", "translate");
      set("translation vector", [i*1e-6, 0, 0]);
      ? "Processed chunk " + num2str(ceil(i/chunk_size));
  }
  ```

### 6. Python API 错误处理示例
```python
import lumapi
import traceback

session = lumapi.FDTD()

try:
    # 尝试应用变换
    session.apply()
    session.set("target", "non_existent_object")
    session.set("transform type", "translate")
    session.set("translation vector", [1e-6, 0, 0])
    
except lumapi.LumapiError as e:
    print(f"Lumerical API error: {e}")
    print(f"Error details: {e.details if hasattr(e, 'details') else 'No details'}")
    
    # 尝试恢复或创建对象
    if "not found" in str(e).lower():
        print("Creating missing object...")
        session.addrect()
        session.set("name", "non_existent_object")
        # 重试变换
        session.apply()
        session.set("target", "non_existent_object")
        session.set("transform type", "translate")
        session.set("translation vector", [1e-6, 0, 0])
        
except Exception as e:
    print(f"Unexpected error: {e}")
    traceback.print_exc()
    # 清理和恢复
    session.redo()  # 尝试撤销上次操作
```

### 7. 预防性措施
1. **验证输入参数**: 在应用变换前检查所有参数的有效性
2. **使用默认值**: 为可选参数提供合理的默认值
3. **逐步变换**: 复杂变换分解为多个简单步骤
4. **保存状态**: 重要变换前保存仿真状态
5. **异常处理**: 使用 try-catch 块包装关键操作

## 产品支持

- **FDTD Solutions**: 支持几何对象、材料、监视器的变换
- **MODE Solutions**: 支持波导、模式对象的变换
- **DEVICE**: 支持热源、结构、边界的变换
- **INTERCONNECT**: 支持电路元件、端口的变换

## 相关命令

- `move` - 移动对象
- `rotate` - 旋转对象
- `scale` - 缩放对象
- `copy` - 复制对象
- `mirror` - 镜像对象
- `array` - 创建对象阵列
- `set` - 设置对象属性
- `get` - 获取对象属性

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本变换和示例 |
| 1.1 | 2026-01-31 | 添加 LSF 脚本示例、错误处理章节、版本历史和参考 |
| 1.2 | 2026-01-31 | 完善配置属性表格，补充批量变换和参数化扫描示例 |

## 参考

1. Lumerical Script Language Reference - Transformation Commands
2. Lumerical Python API Documentation - `lumapi.FDTD.apply()` Method
3. Lumerical Knowledge Base - "How to Use the Apply Command for Geometric Transformations"
4. Lumerical Forum - "Advanced Transformation Techniques" Thread
5. Computer Graphics: Principles and Practice - Transformations and Matrices

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*