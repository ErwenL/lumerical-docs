# `copy` - 复制对象

## 概述

`copy` 命令用于复制仿真中的现有对象。它可以复制几何结构、光源、监视器、求解器等任何仿真对象，创建具有相同属性但不同名称的新对象。该命令在需要创建相似对象或进行参数扫描时非常有用，可以避免重复设置相同的属性。

复制对象时，所有属性（位置、尺寸、材料、设置等）都会被复制到新对象，然后可以根据需要修改新对象的属性。

## 语法

### LSF 语法
```lumerical
copy(source_object);                     # 复制对象，使用自动生成的名称
copy(source_object, destination_name);   # 复制对象并指定新名称
copy(source_object, destination_name, property, value, ...);  # 复制并修改属性
```

### Python API
```python
session.copy(source_object)                     # 复制对象，使用自动生成的名称
session.copy(source_object, destination_name)   # 复制对象并指定新名称
session.copy(source_object, destination_name, property1=value1, ...)  # 复制并修改属性
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `source_object` | string | 要复制的源对象的名称。 | 是 |
| `destination_name` | string | 新对象的名称。如果省略，Lumerical 会自动生成一个名称（如 `source_object1`、`source_object2` 等）。 | 可选 |
| `property` | string | 要在新对象上设置的属性名称。 | 可选 |
| `value` | varies | 属性的值。 | 可选 |

## 配置属性

`copy` 命令可以复制源对象的所有可配置属性。复制后，可以使用 `set` 或 `change` 命令修改新对象的属性。

## 返回值

`copy` 命令没有返回值。成功执行后，会创建指定对象的副本。如果命令失败（例如源对象不存在或名称冲突），Lumerical 会抛出错误。

在 Python API 中，`session.copy()` 通常返回 `None`。成功复制不返回任何值，失败时抛出异常。

## 错误处理

### 常见错误

1. **源对象不存在错误**
   ```python
   # 错误：源对象 "nonexistent" 不存在
   fdtd.copy("nonexistent")
   ```
   解决方案：使用 `hastag` 或 `hasexisting` 命令先检查对象是否存在。

2. **名称冲突错误**
   ```python
   # 错误：目标名称 "existing_object" 已存在
   fdtd.copy("source_object", "existing_object")
   ```
   解决方案：使用不同的名称，或先删除现有对象。

3. **属性无效错误**
   ```python
   # 错误：属性 "invalid_property" 无效
   fdtd.copy("source_object", "new_object", invalid_property="value")
   ```
   解决方案：检查属性名称拼写，确保属性对目标对象有效。

4. **权限不足错误**
   ```python
   # 错误：对象被锁定或只读
   fdtd.copy("locked_object")
   ```
   解决方案：先解锁对象或检查对象状态。

### Python 错误处理示例

```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addrect("source_rect", x=0, y=0, z=0, x_span=1e-6, material="Si")
    
    # 成功复制
    fdtd.copy("source_rect", "copied_rect")
    print("对象复制成功")
    
    # 尝试复制不存在的对象
    fdtd.copy("nonexistent", "new_object")
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
    # 检查错误类型
    error_str = str(e).lower()
    if "source" in error_str and "not found" in error_str:
        print("错误: 源对象不存在")
    elif "name" in error_str and "already exists" in error_str:
        print("错误: 目标名称已存在")
    elif "property" in error_str and "not found" in error_str:
        print("错误: 属性无效")
    elif "locked" in error_str or "permission" in error_str:
        print("错误: 对象被锁定或权限不足")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
    
finally:
    # 清理
    try:
        fdtd.delete("source_rect")
        fdtd.delete("copied_rect")
    except:
        pass
```

## 使用示例

### 示例 1：基本对象复制

#### LSF 脚本
```lumerical
# 创建一个矩形结构
addrect("original_rect", 
        x: 0, y: 0, z: 0,
        x span: 1.0, y span: 0.22, z span: 10,
        material: "Si");

# 显示原始对象属性
?"original_rect";

# 复制对象（使用自动生成的名称）
copy("original_rect");
?"object";  # 列出所有对象

# 复制对象并指定名称
copy("original_rect", "copied_rect");
?"object";  # 列出所有对象

# 检查复制对象的属性
?"copied_rect";
# 或者获取特定属性
?material("copied_rect");
?x("copied_rect");
?y("copied_rect");
?z("copied_rect");
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建一个矩形结构
fdtd.addrect("original_rect", 
             x=0, y=0, z=0,
             x_span=1.0, y_span=0.22, z_span=10,
             material="Si")

print("原始对象属性:")
rect_props = fdtd.get("original_rect")
for key, value in rect_props.items():
    print(f"  {key}: {value}")

# 复制对象（使用自动生成的名称）
fdtd.copy("original_rect")
print("\n复制对象后，当前对象:")
fdtd.eval("?object;")

# 复制对象并指定名称
fdtd.copy("original_rect", "copied_rect")
print("\n指定名称复制后，当前对象:")
fdtd.eval("?object;")

# 检查复制对象的属性
copied_props = fdtd.get("copied_rect")
print(f"\n复制对象 'copied_rect' 的材料: {copied_props.get('material', '未知')}")
print(f"复制对象的位置: x={copied_props.get('x', '未知')}, y={copied_props.get('y', '未知')}, z={copied_props.get('z', '未知')}")
```

### 示例 2：复制并修改属性

#### LSF 脚本
```lumerical
# 创建一个波导结构
addrect("waveguide_template",
        x: 0, y: 0, z: 0,
        x span: 0.5, y span: 0.22, z span: 20,
        material: "Si",
        color: (0.5, 0.5, 1.0));  # 蓝色

# 复制并创建波导阵列
waveguide_count = 5;
spacing = 1.0;  # μm

for (i = 0; i < waveguide_count; i = i + 1) {
    # 计算新位置
    x_position = i * spacing - (waveguide_count - 1) * spacing / 2;
    
    # 复制波导并设置新位置
    new_name = "waveguide_" + num2str(i);
    copy("waveguide_template", new_name, x: x_position);
    
    # 可选：修改其他属性
    if (i % 2 == 0) {
        # 偶数索引的波导使用不同材料
        set(new_name, "material", "SiO2");
        set(new_name, "color", (1.0, 0.5, 0.5));  # 红色
    }
    
    ?"创建 " + new_name + " 在 x=" + num2str(x_position) + " μm";
}

# 验证创建的对象
?"总共创建了 " + num2str(waveguide_count) + " 个波导:";
?"rect";  # 列出所有矩形对象

# 计算总材料体积
total_si_volume = 0;
total_sio2_volume = 0;

for (i = 0; i < waveguide_count; i = i + 1) {
    name = "waveguide_" + num2str(i);
    material = material(name);
    x_span = get(name, "x span");
    y_span = get(name, "y span");
    z_span = get(name, "z span");
    volume = x_span * y_span * z_span;
    
    if (material == "Si") {
        total_si_volume = total_si_volume + volume;
    } else if (material == "SiO2") {
        total_sio2_volume = total_sio2_volume + volume;
    }
}

?"材料体积统计:";
?"  Si 总体积: " + num2str(total_si_volume) + " μm³";
?"  SiO2 总体积: " + num2str(total_sio2_volume) + " μm³";
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建一个波导结构
fdtd.addrect("waveguide_template",
             x=0, y=0, z=0,
             x_span=0.5, y_span=0.22, z_span=20,
             material="Si",
             color=(0.5, 0.5, 1.0))  # 蓝色

print("创建波导阵列:")

# 复制并创建波导阵列
waveguide_count = 5
spacing = 1.0  # μm

for i in range(waveguide_count):
    # 计算新位置
    x_position = i * spacing - (waveguide_count - 1) * spacing / 2
    
    # 复制波导并设置新位置
    new_name = f"waveguide_{i}"
    fdtd.copy("waveguide_template", new_name, x=x_position)
    
    # 可选：修改其他属性
    if i % 2 == 0:
        # 偶数索引的波导使用不同材料
        fdtd.set(new_name, "material", "SiO2")
        fdtd.set(new_name, "color", (1.0, 0.5, 0.5))  # 红色
    
    print(f"  创建 {new_name} 在 x={x_position:.1f} μm")

# 验证创建的对象
print(f"\n总共创建了 {waveguide_count} 个波导:")
fdtd.eval("?rect;")  # 列出所有矩形对象

# 计算总材料体积
total_si_volume = 0
total_sio2_volume = 0

for i in range(waveguide_count):
    name = f"waveguide_{i}"
    props = fdtd.get(name)
    material = props.get("material", "")
    volume = props.get("x span", 0) * props.get("y span", 0) * props.get("z span", 0)
    
    if material == "Si":
        total_si_volume += volume
    elif material == "SiO2":
        total_sio2_volume += volume

print(f"\n材料体积统计:")
print(f"  Si 总体积: {total_si_volume:.4f} μm³")
print(f"  SiO2 总体积: {total_sio2_volume:.4f} μm³")
```

### 示例 3：复制复杂对象（光源和监视器）

#### LSF 脚本
```lumerical
# 添加 FDTD 求解器
addfdtd("FDTD_solver",
        x: 0, y: 0, z: 0,
        x span: 10, y span: 10, z span: 2);

# 创建模板光源
addmode("source_template",
        x: -4, y: 0, z: 0,
        injection axis: "x",
        center wavelength: 1.55,
        wavelength span: 0.1,
        amplitude: 1.0);

# 创建模板监视器
addpower("monitor_template",
         x: 4, y: 0, z: 0,
         x span: 2, y span: 2, z span: 0,
         monitor type: "2D X-normal",
         frequency points: 50);

?"创建多波长仿真设置:";

# 定义要测试的波长
wavelengths = [1.3, 1.4, 1.55, 1.6];  # μm

for (i = 1; i <= length(wavelengths); i = i + 1) {
    wl = wavelengths(i);
    ?"设置波长 " + num2str(wl) + " μm:";
    
    # 复制光源
    source_name = "source_" + num2str(wl);
    copy("source_template", source_name,
         center wavelength: wl,
         name: "Source_" + num2str(wl) + "um");
    
    # 复制监视器
    monitor_name = "monitor_" + num2str(wl);
    copy("monitor_template", monitor_name,
         name: "Monitor_" + num2str(wl) + "um");
    
    # 设置监视器波长范围
    set(monitor_name, "wavelength center", wl);
    set(monitor_name, "wavelength span", 0.2);
    
    ?"  创建光源: " + source_name;
    ?"  创建监视器: " + monitor_name;
    
    # 运行仿真（这里只是示例，实际中需要分别运行）
    # run;
    
    # 获取结果（示例）
    # results = getresult(monitor_name, "T");
}

?"所有光源:";
?"source";

?"所有监视器:";
?"monitor";
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd("FDTD_solver",
             x=0, y=0, z=0,
             x_span=10, y_span=10, z_span=2)

# 创建模板光源
fdtd.addmode("source_template",
             x=-4, y=0, z=0,
             injection_axis="x",
             center_wavelength=1.55,
             wavelength_span=0.1,
             amplitude=1.0)

# 创建模板监视器
fdtd.addpower("monitor_template",
              x=4, y=0, z=0,
              x_span=2, y_span=2, z_span=0,
              monitor_type="2D X-normal",
              frequency_points=50)

print("创建多波长仿真设置:")

# 定义要测试的波长
wavelengths = [1.3, 1.4, 1.55, 1.6]  # μm

for i, wl in enumerate(wavelengths):
    print(f"\n设置波长 {wl} μm:")
    
    # 复制光源
    source_name = f"source_{wl}"
    fdtd.copy("source_template", source_name,
              center_wavelength=wl,
              name=f"Source_{wl}um")
    
    # 复制监视器
    monitor_name = f"monitor_{wl}"
    fdtd.copy("monitor_template", monitor_name,
              name=f"Monitor_{wl}um")
    
    # 设置监视器波长范围
    fdtd.set(monitor_name, "wavelength center", wl)
    fdtd.set(monitor_name, "wavelength span", 0.2)
    
    print(f"  创建光源: {source_name}")
    print(f"  创建监视器: {monitor_name}")
    
    # 运行仿真（这里只是示例，实际中需要分别运行）
    # fdtd.run()
    
    # 获取结果（示例）
    # results = fdtd.getresult(monitor_name, "T")

# 列出所有创建的对象
print("\n所有光源:")
fdtd.eval("?source;")

print("\n所有监视器:")
fdtd.eval("?monitor;")
```

### 示例 4：复制对象组

#### LSF 脚本
```lumerical
# 创建 MZI 结构的函数
function create_mzi_structure(base_name, x_offset) {
    # 创建输入波导
    addrect(base_name + "_input",
            x: x_offset, y: 0, z: 0,
            x span: 2, y span: 0.22, z span: 0.5,
            material: "Si");
    
    # 创建第一个分束器
    addrect(base_name + "_splitter1",
            x: x_offset + 2, y: 0, z: 0,
            x span: 1, y span: 1, z span: 0.5,
            material: "Si");
    
    # 创建上臂波导
    addrect(base_name + "_arm_top",
            x: x_offset + 2.5, y: 0.5, z: 0,
            x span: 0.22, y span: 5, z span: 0.5,
            material: "Si");
    
    # 创建下臂波导
    copy(base_name + "_arm_top", base_name + "_arm_bottom",
         y: -0.5);
    
    # 创建第二个分束器
    copy(base_name + "_splitter1", base_name + "_splitter2",
         x: x_offset + 2.5 + 5);
    
    # 创建输出波导
    copy(base_name + "_input", base_name + "_output",
         x: x_offset + 2.5 + 5 + 1);
    
    # 返回对象列表
    objects = [base_name + "_input", base_name + "_splitter1", 
               base_name + "_arm_top", base_name + "_arm_bottom",
               base_name + "_splitter2", base_name + "_output"];
    return objects;
}

# 创建第一个 MZI
?"创建第一个 MZI 结构...";
mzi1_objects = create_mzi_structure("mzi1", 0);
?"创建的对象: " + num2str(mzi1_objects);

# 复制整个 MZI 结构
?"复制整个 MZI 结构...";

# 方法：复制每个对象并偏移位置
x_offset_increment = 15;  # 新 MZI 的 x 偏移

for (i = 1; i <= length(mzi1_objects); i = i + 1) {
    obj_name = mzi1_objects(i);
    
    # 提取基本名称（去掉 mzi1_ 前缀）
    base_part = replace(obj_name, "mzi1_", "");
    
    # 新对象名称
    new_obj_name = "mzi2_" + base_part;
    
    # 获取原始对象属性
    props = get(obj_name);
    x_pos = get(obj_name, "x");
    
    # 计算新位置
    new_x = x_pos + x_offset_increment;
    
    # 复制对象
    copy(obj_name, new_obj_name, x: new_x);
    
    ?"  复制 " + obj_name + " -> " + new_obj_name + " (x=" + num2str(new_x) + " μm)";
}

# 验证复制结果
?"所有 MZI 对象:";
?"rect";

# 计算结构统计
?"结构统计:";
for (mzi_num = 1; mzi_num <= 2; mzi_num = mzi_num + 1) {
    mzi_prefix = "mzi" + num2str(mzi_num);
    si_volume = 0;
    
    obj_types = ["input", "splitter1", "arm_top", "arm_bottom", "splitter2", "output"];
    for (j = 1; j <= length(obj_types); j = j + 1) {
        obj_type = obj_types(j);
        obj_name = mzi_prefix + "_" + obj_type;
        
        # 尝试获取对象属性
        if (hasexisting(obj_name)) {
            x_span = get(obj_name, "x span");
            y_span = get(obj_name, "y span");
            z_span = get(obj_name, "z span");
            volume = x_span * y_span * z_span;
            si_volume = si_volume + volume;
        }
    }
    
    ?"  " + mzi_prefix + ": 总体积 = " + num2str(si_volume) + " μm³";
}
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

def create_mzi_structure(base_name, x_offset=0):
    """创建马赫-曾德尔干涉仪（MZI）结构"""
    
    # 创建输入波导
    fdtd.addrect(f"{base_name}_input",
                 x=x_offset, y=0, z=0,
                 x_span=2, y_span=0.22, z_span=0.5,
                 material="Si")
    
    # 创建第一个分束器
    fdtd.addrect(f"{base_name}_splitter1",
                 x=x_offset+2, y=0, z=0,
                 x_span=1, y_span=1, z_span=0.5,
                 material="Si")
    
    # 创建上臂波导
    fdtd.addrect(f"{base_name}_arm_top",
                 x=x_offset+2.5, y=0.5, z=0,
                 x_span=0.22, y_span=5, z_span=0.5,
                 material="Si")
    
    # 创建下臂波导
    fdtd.copy(f"{base_name}_arm_top", f"{base_name}_arm_bottom",
              y=-0.5)
    
    # 创建第二个分束器
    fdtd.copy(f"{base_name}_splitter1", f"{base_name}_splitter2",
              x=x_offset+2.5+5)
    
    # 创建输出波导
    fdtd.copy(f"{base_name}_input", f"{base_name}_output",
              x=x_offset+2.5+5+1)
    
    return [f"{base_name}_input", f"{base_name}_splitter1", 
            f"{base_name}_arm_top", f"{base_name}_arm_bottom",
            f"{base_name}_splitter2", f"{base_name}_output"]

# 创建第一个 MZI
print("创建第一个 MZI 结构...")
mzi1_objects = create_mzi_structure("mzi1", x_offset=0)
print(f"创建的对象: {mzi1_objects}")

# 复制整个 MZI 结构
print("\n复制整个 MZI 结构...")

# 方法：复制每个对象并偏移位置
x_offset_increment = 15  # 新 MZI 的 x 偏移

for obj_name in mzi1_objects:
    # 提取基本名称（去掉 mzi1_ 前缀）
    base_part = obj_name.replace("mzi1_", "")
    
    # 新对象名称
    new_obj_name = f"mzi2_{base_part}"
    
    # 获取原始对象属性
    props = fdtd.get(obj_name)
    
    # 计算新位置
    new_x = props.get("x", 0) + x_offset_increment
    
    # 复制对象
    fdtd.copy(obj_name, new_obj_name, x=new_x)
    
    print(f"  复制 {obj_name} -> {new_obj_name} (x={new_x:.1f} μm)")

# 验证复制结果
print("\n所有 MZI 对象:")
fdtd.eval("?rect;")

# 计算结构统计
print("\n结构统计:")
for mzi_prefix in ["mzi1", "mzi2"]:
    si_volume = 0
    for obj_type in ["input", "splitter1", "arm_top", "arm_bottom", "splitter2", "output"]:
        obj_name = f"{mzi_prefix}_{obj_type}"
        try:
            props = fdtd.get(obj_name)
            volume = props.get("x span", 0) * props.get("y span", 0) * props.get("z span", 0)
            si_volume += volume
        except:
            pass
    
    print(f"  {mzi_prefix}: 总体积 = {si_volume:.4f} μm³")
```

### 示例 5：高级复制工具

#### LSF 脚本
```lumerical
# 高级复制工具函数

# 复制并应用几何变换的函数
function copy_with_transform(source, destination, translate, scale) {
    # 复制对象
    copy(source, destination);
    
    # 获取原始属性
    x_pos = get(source, "x");
    y_pos = get(source, "y");
    z_pos = get(source, "z");
    x_span = get(source, "x span");
    y_span = get(source, "y span");
    z_span = get(source, "z span");
    
    # 应用平移
    if (translate(1) != 0 || translate(2) != 0 || translate(3) != 0) {
        new_x = x_pos + translate(1);
        new_y = y_pos + translate(2);
        new_z = z_pos + translate(3);
        set(destination, "x", new_x);
        set(destination, "y", new_y);
        set(destination, "z", new_z);
    }
    
    # 应用缩放
    if (scale(1) != 1 || scale(2) != 1 || scale(3) != 1) {
        new_x_span = x_span * scale(1);
        new_y_span = y_span * scale(2);
        new_z_span = z_span * scale(3);
        set(destination, "x span", new_x_span);
        set(destination, "y span", new_y_span);
        set(destination, "z span", new_z_span);
    }
    
    return destination;
}

# 按模式复制多个对象的函数
function copy_pattern(source, name_pattern, count, spacing) {
    created_objects = {};
    
    for (i = 0; i < count; i = i + 1) {
        # 生成新名称
        new_name = name_pattern + num2str(i);
        
        # 计算位置偏移
        translate = [i * spacing(1), i * spacing(2), i * spacing(3)];
        
        # 复制并变换
        copy_with_transform(source, new_name, translate, [1, 1, 1]);
        created_objects(i+1) = new_name;
    }
    
    return created_objects;
}

# 复制指定类型的所有对象的函数
function copy_all_of_type(object_type, name_prefix) {
    # 获取所有指定类型的对象
    eval("objects = ?" + object_type + ";");
    
    if (!exist("objects")) {
        ?"没有找到 " + object_type + " 类型的对象";
        return {};
    }
    
    created_copies = {};
    
    for (i = 1; i <= length(objects); i = i + 1) {
        obj_name = objects(i);
        
        # 新对象名称
        new_name = name_prefix + "_" + object_type + "_" + num2str(i-1);
        
        # 复制对象
        copy(obj_name, new_name);
        created_copies(i) = new_name;
        
        ?"复制 " + obj_name + " -> " + new_name;
    }
    
    # 清理临时变量
    clear("objects");
    
    return created_copies;
}

# 使用示例
?"示例1: 复制并变换对象";
addfdtd("solver", x span: 20, y span: 20, z span: 2);
addrect("base_object",
        x: 0, y: 0, z: 0,
        x span: 1, y span: 0.5, z span: 0.2,
        material: "Si");

copy_with_transform("base_object", "transformed_copy",
                   translate: [3, 2, 0],
                   scale: [1.5, 0.8, 2.0]);

?"示例2: 按模式复制";
created = copy_pattern("base_object", 
                      "pattern_object_", 
                      count: 4, 
                      spacing: [2, 0, 0]);
?"创建的对象: " + num2str(created);

?"示例3: 复制所有矩形对象";
# 先创建几个不同的矩形
addrect("rect1", x: -5, y: 5, z: 0, x span: 0.5, y span: 0.5, z span: 0.1, material: "SiO2");
addrect("rect2", x: -5, y: 3, z: 0, x span: 0.8, y span: 0.3, z span: 0.1, material: "SiN");

copies = copy_all_of_type("rect", "backup");
?"复制的矩形对象: " + num2str(copies);

?"所有对象列表:";
?"object";
```

#### Python API
```python
import lumapi
import re

class ObjectCopier:
    """高级对象复制工具"""
    
    def __init__(self, session):
        self.session = session
    
    def copy_with_transform(self, source, destination, 
                           translate=(0, 0, 0), 
                           scale=(1, 1, 1),
                           rotate=(0, 0, 0)):
        """复制对象并应用几何变换"""
        
        # 复制对象
        self.session.copy(source, destination)
        
        # 获取原始属性
        props = self.session.get(source)
        
        # 应用平移
        if translate != (0, 0, 0):
            new_x = props.get("x", 0) + translate[0]
            new_y = props.get("y", 0) + translate[1]
            new_z = props.get("z", 0) + translate[2]
            self.session.set(destination, "x", new_x)
            self.session.set(destination, "y", new_y)
            self.session.set(destination, "z", new_z)
        
        # 应用缩放
        if scale != (1, 1, 1):
            new_x_span = props.get("x span", 0) * scale[0]
            new_y_span = props.get("y span", 0) * scale[1]
            new_z_span = props.get("z span", 0) * scale[2]
            self.session.set(destination, "x span", new_x_span)
            self.session.set(destination, "y span", new_y_span)
            self.session.set(destination, "z span", new_z_span)
        
        return destination
    
    def copy_pattern(self, source, name_pattern, count, spacing):
        """按模式复制多个对象"""
        
        created_objects = []
        
        for i in range(count):
            # 生成新名称
            new_name = name_pattern.format(i=i)
            
            # 计算位置偏移
            translate = (i * spacing[0], i * spacing[1], i * spacing[2])
            
            # 复制并变换
            self.copy_with_transform(source, new_name, translate=translate)
            created_objects.append(new_name)
        
        return created_objects
    
    def copy_all_of_type(self, object_type, name_prefix="copy"):
        """复制指定类型的所有对象"""
        
        # 获取所有指定类型的对象
        self.session.eval(f"objects = ?{object_type};")
        objects = self.session.get("objects")
        self.session.clear("objects")
        
        if not objects:
            print(f"没有找到 {object_type} 类型的对象")
            return []
        
        created_copies = []
        
        for i, obj_name in enumerate(objects):
            # 新对象名称
            new_name = f"{name_prefix}_{object_type}_{i}"
            
            # 复制对象
            self.session.copy(obj_name, new_name)
            created_copies.append(new_name)
            
            print(f"复制 {obj_name} -> {new_name}")
        
        return created_copies

# 使用示例
fdtd = lumapi.FDTD()
copier = ObjectCopier(fdtd)

# 设置示例场景
fdtd.addfdtd("solver", x_span=20, y_span=20, z_span=2)

# 创建示例对象
fdtd.addrect("base_object",
             x=0, y=0, z=0,
             x_span=1, y_span=0.5, z_span=0.2,
             material="Si")

print("示例1: 复制并变换对象")
copier.copy_with_transform("base_object", "transformed_copy",
                          translate=(3, 2, 0),
                          scale=(1.5, 0.8, 2.0))

print("\n示例2: 按模式复制")
created = copier.copy_pattern("base_object", 
                             "pattern_object_{i}", 
                             count=4, 
                             spacing=(2, 0, 0))
print(f"创建的对象: {created}")

print("\n示例3: 复制所有矩形对象")
# 先创建几个不同的矩形
fdtd.addrect("rect1", x=-5, y=5, z=0, x_span=0.5, y_span=0.5, z_span=0.1, material="SiO2")
fdtd.addrect("rect2", x=-5, y=3, z=0, x_span=0.8, y_span=0.3, z_span=0.1, material="SiN")

copies = copier.copy_all_of_type("rect", "backup")
print(f"复制的矩形对象: {copies}")

print("\n所有对象列表:")
fdtd.eval("?object;")
```

## 注意事项

1. **名称冲突**：如果目标名称已存在，`copy` 命令可能会覆盖现有对象或产生错误。建议在复制前检查名称是否可用。

2. **对象依赖性**：某些对象可能依赖于其他对象（如监视器依赖于光源）。复制单个对象可能不会复制其依赖关系。

3. **自动命名**：如果不指定目标名称，Lumerical 会自动生成名称（通常是在源名称后添加数字）。自动生成的名称可能不直观，建议显式指定名称。

4. **属性继承**：所有属性都会被复制，包括可见性、颜色、网格设置等。复制后可能需要调整某些属性。

5. **性能考虑**：复制大量复杂对象可能会影响性能。对于需要创建许多相似对象的情况，考虑使用循环和参数化方法。

6. **与 `add` 的区别**：`copy` 复制现有对象，而 `add` 创建新对象。`copy` 通常更快，因为不需要重新指定所有属性。

7. **对象类型**：可以复制大多数对象类型，但某些特殊对象（如脚本对象、优化对象）的复制行为可能有所不同。

8. **撤销操作**：`copy` 操作可以通过 `undo` 命令撤销。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 可以复制所有对象类型 |
| MODE Solutions | ✅ 完全支持 | 可以复制所有对象类型 |
| DEVICE | ✅ 完全支持 | 可以复制所有对象类型 |
| INTERCONNECT | ✅ 完全支持 | 可以复制所有对象类型 |

## 相关命令

- `add` - 添加新对象
- `delete` - 删除对象
- `rename` - 重命名对象
- `move` - 移动对象
- `set` - 设置对象属性
- `get` - 获取对象属性
- `select` - 选择对象
- `undo` - 撤销复制操作

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本语法和示例 |
| 1.1 | 2026-01-31 | 添加 LSF 脚本示例、错误处理章节、版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - copy 命令
2. Lumerical Python API Documentation - session.copy() 方法
3. Lumerical Knowledge Base - 对象复制最佳实践

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*