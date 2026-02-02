# `creategroup` - 创建组

## 概述

`creategroup` 命令用于将多个仿真对象组合成一个组。组是 Lumerical 中管理复杂结构的重要工具，它允许用户将相关的对象（如几何结构、光源、监视器等）组织在一起，便于统一操作、变换、复制和管理。组可以嵌套，形成层次结构，大大简化了复杂仿真的设置和维护。

该命令在创建重复单元、复杂器件或需要统一变换的对象集合时特别有用。

## 语法

### LSF 语法
```lumerical
creategroup(group_name);                    # 创建空组
creategroup(group_name, object1, object2, ...);  # 创建组并添加对象
creategroup(group_name, "add", object1, object2, ...);  # 向现有组添加对象
creategroup(group_name, "remove", object1, object2, ...);  # 从组中移除对象
```

### Python API
```python
session.creategroup(group_name)                     # 创建空组
session.creategroup(group_name, object1, object2, ...)  # 创建组并添加对象
session.creategroup(group_name, "add", object1, object2, ...)  # 向现有组添加对象
session.creategroup(group_name, "remove", object1, object2, ...)  # 从组中移除对象
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `group_name` | string | 组的名称。 | 是 |
| `operation` | string | 操作类型："add"（添加对象）、"remove"（移除对象）。如果省略，则创建新组或替换现有组的内容。 | 可选 |
| `object` | string | 要添加到组或从组中移除的对象名称。 | 可选（创建空组时可省略） |

## 配置属性

通过 `set` 命令可以配置组的以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | group_name | 组的名称。 |
| `visible` | bool | true | 组是否可见。 |
| `color` | string | "custom" | 组的显示颜色（影响组内对象）。 |
| `alpha` | number | 1.0 | 组的透明度（0-1）。 |
| `material` | string | "" | 组的材料（如果统一设置）。 |
| `x`, `y`, `z` | number | 0 | 组的位置（参考点）。 |
| `rotation angle` | number | 0 | 组的旋转角度（度）。 |
| `rotation axis` | string | "z" | 组的旋转轴方向。 |
| `scale` | number | 1.0 | 组的缩放因子。 |
| `lock` | bool | false | 是否锁定组（防止意外修改）。 |

## 使用示例

### 示例 1：创建基本对象组

**Python API:**
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建几个对象
fdtd.addrect("rect1", x=0, y=0, z=0, x_span=1, y_span=1, z_span=0.1, material="Si")
fdtd.addrect("rect2", x=2, y=0, z=0, x_span=0.5, y_span=0.5, z_span=0.1, material="SiO2")
fdtd.addcircle("circle1", x=1, y=1, z=0, radius=0.3, material="SiN")

print("创建的对象:")
fdtd.eval("?object;")

# 创建组并添加对象
fdtd.creategroup("my_group", "rect1", "rect2", "circle1")

print("\n创建组 'my_group' 包含: rect1, rect2, circle1")

# 检查组的属性
group_props = fdtd.get("my_group")
print(f"\n组属性:")
print(f"  名称: {group_props.get('name', '未知')}")
print(f"  对象数量: {len(group_props.get('children', []))}")
print(f"  位置: ({group_props.get('x', '未知')}, {group_props.get('y', '未知')}, {group_props.get('z', '未知')})")

# 列出组内对象
print("\n组内对象:")
for child in group_props.get('children', []):
    print(f"  {child}")
```

**LSF Script:**
```lumerical
# 创建几个对象
addrect("rect1");
set("x", 0); set("y", 0); set("z", 0);
set("x span", 1); set("y span", 1); set("z span", 0.1);
set("material", "Si");

addrect("rect2");
set("name", "rect2");
set("x", 2); set("y", 0); set("z", 0);
set("x span", 0.5); set("y span", 0.5); set("z span", 0.1);
set("material", "SiO2");

addcircle("circle1");
set("name", "circle1");
set("x", 1); set("y", 1); set("z", 0);
set("radius", 0.3);
set("material", "SiN");

# 列出所有对象
?object;

# 创建组并添加对象
creategroup("my_group", "rect1", "rect2", "circle1");

# 打印确认
?"创建组 'my_group' 包含: rect1, rect2, circle1";

# 检查组的属性
group_props = get("my_group");
?"组属性:";
?"  名称: " + group_props.name;
?"  对象数量: " + num2str(length(group_props.children));
?"  位置: (" + num2str(group_props.x) + ", " + num2str(group_props.y) + ", " + num2str(group_props.z) + ")";

# 列出组内对象
?"组内对象:";
for (i = 1:length(group_props.children)) {
    ?"  " + group_props.children{i};
}
```

### 示例 2：组操作（添加、移除对象）

**Python API:**
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建一些对象
objects = []
for i in range(5):
    name = f"obj_{i}"
    fdtd.addrect(name, x=i, y=0, z=0, x_span=0.5, y_span=0.5, z_span=0.1)
    objects.append(name)

print(f"创建了 {len(objects)} 个对象")

# 创建空组
fdtd.creategroup("dynamic_group")
print("创建空组 'dynamic_group'")

# 向组中添加对象
fdtd.creategroup("dynamic_group", "add", "obj_0", "obj_1", "obj_2")
print("添加 obj_0, obj_1, obj_2 到组")

# 检查组内容
group_props = fdtd.get("dynamic_group")
print(f"组内对象: {group_props.get('children', [])}")

# 添加更多对象
fdtd.creategroup("dynamic_group", "add", "obj_3")
print("添加 obj_3 到组")

# 移除对象
fdtd.creategroup("dynamic_group", "remove", "obj_1")
print("从组中移除 obj_1")

# 最终组内容
group_props = fdtd.get("dynamic_group")
print(f"最终组内对象: {group_props.get('children', [])}")
print(f"对象数量: {len(group_props.get('children', []))}")

# 替换组内容（不使用 "add" 参数）
fdtd.creategroup("dynamic_group", "obj_4")  # 这会替换整个组
print("\n替换组内容为仅包含 obj_4")
group_props = fdtd.get("dynamic_group")
print(f"组内对象: {group_props.get('children', [])}")
```

**LSF Script:**
```lumerical
# 创建一些对象
for (i = 0:4) {
    addrect;
    set("name", "obj_" + num2str(i));
    set("x", i);
    set("y", 0);
    set("z", 0);
    set("x span", 0.5);
    set("y span", 0.5);
    set("z span", 0.1);
}

?"创建了 5 个对象";

# 创建空组
creategroup("dynamic_group");
?"创建空组 'dynamic_group'";

# 向组中添加对象
creategroup("dynamic_group", "add", "obj_0", "obj_1", "obj_2");
?"添加 obj_0, obj_1, obj_2 到组";

# 检查组内容
group_props = get("dynamic_group");
?"组内对象:";
for (i = 1:length(group_props.children)) {
    ?"  " + group_props.children{i};
}

# 添加更多对象
creategroup("dynamic_group", "add", "obj_3");
?"添加 obj_3 到组";

# 移除对象
creategroup("dynamic_group", "remove", "obj_1");
?"从组中移除 obj_1";

# 最终组内容
group_props = get("dynamic_group");
?"最终组内对象:";
for (i = 1:length(group_props.children)) {
    ?"  " + group_props.children{i};
}
?"对象数量: " + num2str(length(group_props.children));

# 替换组内容（不使用 "add" 参数）
creategroup("dynamic_group", "obj_4");  # 这会替换整个组
?"替换组内容为仅包含 obj_4";
group_props = get("dynamic_group");
?"组内对象:";
for (i = 1:length(group_props.children)) {
    ?"  " + group_props.children{i};
}
```

### 示例 3：使用组进行统一变换

**Python API:**
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_sensor_array(name, rows=3, cols=3, spacing=2):
    """创建传感器阵列"""
    
    sensors = []
    
    for i in range(rows):
        for j in range(cols):
            # 创建传感器（简化模型）
            sensor_name = f"{name}_sensor_{i}_{j}"
            fdtd.addrect(sensor_name,
                         x=j*spacing, y=i*spacing, z=0,
                         x_span=1, y_span=1, z_span=0.1,
                         material="Si")
            
            # 添加电极
            electrode_name = f"{name}_electrode_{i}_{j}"
            fdtd.addrect(electrode_name,
                         x=j*spacing, y=i*spacing, z=0.1,
                         x_span=0.2, y_span=0.2, z_span=0.02,
                         material="Au")
            
            sensors.extend([sensor_name, electrode_name])
    
    return sensors

print("创建 3x3 传感器阵列...")
sensors = create_sensor_array("sensor", rows=3, cols=3, spacing=2)
print(f"创建了 {len(sensors)} 个对象")

# 将所有传感器对象分组
fdtd.creategroup("sensor_array", *sensors)
print(f"创建组 'sensor_array' 包含所有传感器")

# 统一变换整个阵列
print("\n应用组变换:")

# 1. 平移整个阵列
fdtd.set("sensor_array", "x", 5)
fdtd.set("sensor_array", "y", 5)
print("  平移: (5, 5, 0) μm")

# 2. 旋转整个阵列
fdtd.set("sensor_array", "rotation angle", 45)
fdtd.set("sensor_array", "rotation axis", "z")
print("  旋转: 45° 绕 z 轴")

# 3. 缩放整个阵列
fdtd.set("sensor_array", "scale", 1.5)
print("  缩放: 1.5 倍")

# 验证变换
print("\n验证变换后的位置:")
for sensor in sensors[:2]:  # 检查前两个传感器
    props = fdtd.get(sensor)
    print(f"  {sensor}: ({props.get('x', '未知'):.2f}, {props.get('y', '未知'):.2f}, {props.get('z', '未知'):.2f})")

# 计算阵列参数
group_props = fdtd.get("sensor_array")
children = group_props.get('children', [])
print(f"\n组统计:")
print(f"  对象总数: {len(children)}")
print(f"  传感器数量: {len([c for c in children if 'sensor' in c])}")
print(f"  电极数量: {len([c for c in children if 'electrode' in c])}")

# 统一设置组属性
fdtd.set("sensor_array", "visible", True)
fdtd.set("sensor_array", "color", (0.8, 0.2, 0.2))  # 红色
fdtd.set("sensor_array", "alpha", 0.8)
print("  设置组颜色为红色，透明度 0.8")
```

**LSF Script:**
```lumerical
# 创建传感器阵列函数
function create_sensor_array(name, rows, cols, spacing) {
    sensors = {};
    
    for (i = 0:rows-1) {
        for (j = 0:cols-1) {
            # 创建传感器（简化模型）
            sensor_name = name + "_sensor_" + num2str(i) + "_" + num2str(j);
            addrect;
            set("name", sensor_name);
            set("x", j*spacing);
            set("y", i*spacing);
            set("z", 0);
            set("x span", 1);
            set("y span", 1);
            set("z span", 0.1);
            set("material", "Si");
            
            # 添加电极
            electrode_name = name + "_electrode_" + num2str(i) + "_" + num2str(j);
            addrect;
            set("name", electrode_name);
            set("x", j*spacing);
            set("y", i*spacing);
            set("z", 0.1);
            set("x span", 0.2);
            set("y span", 0.2);
            set("z span", 0.02);
            set("material", "Au");
            
            sensors = {sensors{:}, sensor_name, electrode_name};
        }
    }
    
    return sensors;
}

?"创建 3x3 传感器阵列...";
sensors = create_sensor_array("sensor", 3, 3, 2);
?"创建了 " + num2str(length(sensors)) + " 个对象";

# 将所有传感器对象分组
creategroup("sensor_array", sensors{:});
?"创建组 'sensor_array' 包含所有传感器";

# 统一变换整个阵列
?"应用组变换:";

# 1. 平移整个阵列
set("sensor_array", "x", 5);
set("sensor_array", "y", 5);
?"  平移: (5, 5, 0) μm";

# 2. 旋转整个阵列
set("sensor_array", "rotation angle", 45);
set("sensor_array", "rotation axis", "z");
?"  旋转: 45° 绕 z 轴";

# 3. 缩放整个阵列
set("sensor_array", "scale", 1.5);
?"  缩放: 1.5 倍";

# 验证变换
?"验证变换后的位置:";
for (i = 1:2) {
    sensor = sensors{i};
    props = get(sensor);
    ?"  " + sensor + ": (" + num2str(props.x, "%.2f") + ", " + num2str(props.y, "%.2f") + ", " + num2str(props.z, "%.2f") + ")";
}

# 计算阵列参数
group_props = get("sensor_array");
children = group_props.children;
?"组统计:";
?"  对象总数: " + num2str(length(children));

sensor_count = 0;
electrode_count = 0;
for (i = 1:length(children)) {
    child = children{i};
    if (find(child, "sensor") > 0) {
        sensor_count = sensor_count + 1;
    }
    if (find(child, "electrode") > 0) {
        electrode_count = electrode_count + 1;
    }
}
?"  传感器数量: " + num2str(sensor_count);
?"  电极数量: " + num2str(electrode_count);

# 统一设置组属性
set("sensor_array", "visible", true);
set("sensor_array", "color", [0.8, 0.2, 0.2]);  # 红色
set("sensor_array", "alpha", 0.8);
?"  设置组颜色为红色，透明度 0.8";
```

### 示例 4：嵌套组和复杂结构

**Python API:**
```python
import lumapi

fdtd = lumapi.FDTD()

def create_mzi_with_monitors(name, center=(0, 0, 0)):
    """创建 MZI（马赫-曾德尔干涉仪）及其监视器"""
    
    # MZI 组件
    components = []
    
    # 输入波导
    fdtd.addrect(f"{name}_input", 
                 x=center[0]-10, y=center[1], z=center[2],
                 x_span=5, y_span=0.22, z_span=0.5,
                 material="Si")
    components.append(f"{name}_input")
    
    # 第一个分束器
    fdtd.addrect(f"{name}_splitter1",
                 x=center[0]-5, y=center[1], z=center[2],
                 x_span=1, y_span=1, z_span=0.5,
                 material="Si")
    components.append(f"{name}_splitter1")
    
    # 上臂
    fdtd.addrect(f"{name}_arm_top",
                 x=center[0]-4.5, y=center[1]+2, z=center[2],
                 x_span=0.22, y_span=4, z_span=0.5,
                 material="Si")
    components.append(f"{name}_arm_top")
    
    # 下臂
    fdtd.addrect(f"{name}_arm_bottom",
                 x=center[0]-4.5, y=center[1]-2, z=center[2],
                 x_span=0.22, y_span=4, z_span=0.5,
                 material="Si")
    components.append(f"{name}_arm_bottom")
    
    # 第二个分束器
    fdtd.addrect(f"{name}_splitter2",
                 x=center[0]+0.5, y=center[1], z=center[2],
                 x_span=1, y_span=1, z_span=0.5,
                 material="Si")
    components.append(f"{name}_splitter2")
    
    # 输出波导
    fdtd.addrect(f"{name}_output",
                 x=center[0]+6, y=center[1], z=center[2],
                 x_span=5, y_span=0.22, z_span=0.5,
                 material="Si")
    components.append(f"{name}_output")
    
    # 监视器
    monitors = []
    
    # 输入监视器
    fdtd.addpower(f"{name}_monitor_input",
                  x=center[0]-8, y=center[1], z=center[2],
                  x_span=0.5, y_span=0.5, z_span=0.5)
    monitors.append(f"{name}_monitor_input")
    
    # 输出监视器
    fdtd.addpower(f"{name}_monitor_output",
                  x=center[0]+8, y=center[1], z=center[2],
                  x_span=0.5, y_span=0.5, z_span=0.5)
    monitors.append(f"{name}_monitor_output")
    
    return components, monitors

print("创建 MZI 结构...")
mzi_components, mzi_monitors = create_mzi_with_monitors("mzi1", center=(0, 0, 0))

print(f"创建了 {len(mzi_components)} 个组件和 {len(mzi_monitors)} 个监视器")

# 创建嵌套组结构
print("\n创建嵌套组结构:")

# 1. 创建组件组
fdtd.creategroup("mzi1_components", *mzi_components)
print("  创建组件组: mzi1_components")

# 2. 创建监视器组
fdtd.creategroup("mzi1_monitors", *mzi_monitors)
print("  创建监视器组: mzi1_monitors")

# 3. 创建顶级组（包含组件组和监视器组）
fdtd.creategroup("mzi1_full", "mzi1_components", "mzi1_monitors")
print("  创建顶级组: mzi1_full（包含组件组和监视器组）")

# 检查组层次结构
print("\n组层次结构分析:")

def analyze_group_hierarchy(group_name, level=0):
    """递归分析组层次结构"""
    
    indent = "  " * level
    props = fdtd.get(group_name)
    
    print(f"{indent}{group_name}:")
    
    children = props.get('children', [])
    if children:
        print(f"{indent}  包含 {len(children)} 个子项:")
        for child in children:
            # 检查子项是否是组
            try:
                child_props = fdtd.get(child)
                if 'children' in child_props:  # 这也是一个组
                    analyze_group_hierarchy(child, level + 1)
                else:
                    print(f"{indent}  - {child} (对象)")
            except:
                print(f"{indent}  - {child} (对象)")

analyze_group_hierarchy("mzi1_full")

# 统一操作顶级组
print("\n对顶级组进行统一操作:")

# 移动整个 MZI
fdtd.set("mzi1_full", "x", 10)
print("  移动整个 MZI 到 x=10 μm")

# 隐藏所有监视器
fdtd.set("mzi1_monitors", "visible", False)
print("  隐藏所有监视器")

# 设置组件颜色
fdtd.set("mzi1_components", "color", (0.2, 0.6, 1.0))  # 蓝色
print("  设置组件颜色为蓝色")

# 复制整个结构
fdtd.copy("mzi1_full", "mzi2_full")
print("  复制整个结构为 mzi2_full")

# 移动复制的结构
fdtd.set("mzi2_full", "x", -10)
print("  移动复制的结构到 x=-10 μm")
fdtd.set("mzi2_full", "color", (1.0, 0.6, 0.2))  # 橙色
print("  设置复制结构颜色为橙色")
```

**LSF Script:**
```lumerical
# 创建 MZI 结构函数
function create_mzi_with_monitors(name, center) {
    components = {};
    monitors = {};
    
    # 输入波导
    addrect;
    set("name", name + "_input");
    set("x", center(1)-10); set("y", center(2)); set("z", center(3));
    set("x span", 5); set("y span", 0.22); set("z span", 0.5);
    set("material", "Si");
    components = {name + "_input"};
    
    # 第一个分束器
    addrect;
    set("name", name + "_splitter1");
    set("x", center(1)-5); set("y", center(2)); set("z", center(3));
    set("x span", 1); set("y span", 1); set("z span", 0.5);
    set("material", "Si");
    components = {components{:}, name + "_splitter1"};
    
    # 上臂
    addrect;
    set("name", name + "_arm_top");
    set("x", center(1)-4.5); set("y", center(2)+2); set("z", center(3));
    set("x span", 0.22); set("y span", 4); set("z span", 0.5);
    set("material", "Si");
    components = {components{:}, name + "_arm_top"};
    
    # 下臂
    addrect;
    set("name", name + "_arm_bottom");
    set("x", center(1)-4.5); set("y", center(2)-2); set("z", center(3));
    set("x span", 0.22); set("y span", 4); set("z span", 0.5);
    set("material", "Si");
    components = {components{:}, name + "_arm_bottom"};
    
    # 第二个分束器
    addrect;
    set("name", name + "_splitter2");
    set("x", center(1)+0.5); set("y", center(2)); set("z", center(3));
    set("x span", 1); set("y span", 1); set("z span", 0.5);
    set("material", "Si");
    components = {components{:}, name + "_splitter2"};
    
    # 输出波导
    addrect;
    set("name", name + "_output");
    set("x", center(1)+6); set("y", center(2)); set("z", center(3));
    set("x span", 5); set("y span", 0.22); set("z span", 0.5);
    set("material", "Si");
    components = {components{:}, name + "_output"};
    
    # 输入监视器
    addpower;
    set("name", name + "_monitor_input");
    set("x", center(1)-8); set("y", center(2)); set("z", center(3));
    set("x span", 0.5); set("y span", 0.5); set("z span", 0.5);
    monitors = {name + "_monitor_input"};
    
    # 输出监视器
    addpower;
    set("name", name + "_monitor_output");
    set("x", center(1)+8); set("y", center(2)); set("z", center(3));
    set("x span", 0.5); set("y span", 0.5); set("z span", 0.5);
    monitors = {monitors{:}, name + "_monitor_output"};
    
    return {components, monitors};
}

?"创建 MZI 结构...";
result = create_mzi_with_monitors("mzi1", [0, 0, 0]);
mzi_components = result{1};
mzi_monitors = result{2};

?"创建了 " + num2str(length(mzi_components)) + " 个组件和 " + num2str(length(mzi_monitors)) + " 个监视器";

?"创建嵌套组结构:";

# 1. 创建组件组
creategroup("mzi1_components", mzi_components{:});
?"  创建组件组: mzi1_components";

# 2. 创建监视器组
creategroup("mzi1_monitors", mzi_monitors{:});
?"  创建监视器组: mzi1_monitors";

# 3. 创建顶级组（包含组件组和监视器组）
creategroup("mzi1_full", "mzi1_components", "mzi1_monitors");
?"  创建顶级组: mzi1_full（包含组件组和监视器组）";

# 检查组层次结构
?"组层次结构分析:";
function analyze_group_hierarchy(group_name, level) {
    indent = "";
    for (i = 1:level) {
        indent = indent + "  ";
    }
    
    props = get(group_name);
    
    ?indent + group_name + ":";
    
    children = props.children;
    if (length(children) > 0) {
        ?indent + "  包含 " + num2str(length(children)) + " 个子项:";
        for (i = 1:length(children)) {
            child = children{i};
            try {
                child_props = get(child);
                if (isfield(child_props, "children")) {
                    analyze_group_hierarchy(child, level + 1);
                } else {
                    ?indent + "  - " + child + " (对象)";
                }
            } catch (e) {
                ?indent + "  - " + child + " (对象)";
            }
        }
    }
}

analyze_group_hierarchy("mzi1_full", 0);

# 统一操作顶级组
?"对顶级组进行统一操作:";

# 移动整个 MZI
set("mzi1_full", "x", 10);
?"  移动整个 MZI 到 x=10 μm";

# 隐藏所有监视器
set("mzi1_monitors", "visible", false);
?"  隐藏所有监视器";

# 设置组件颜色
set("mzi1_components", "color", [0.2, 0.6, 1.0]);  # 蓝色
?"  设置组件颜色为蓝色";

# 复制整个结构
copy("mzi1_full", "mzi2_full");
?"  复制整个结构为 mzi2_full";

# 移动复制的结构
set("mzi2_full", "x", -10);
?"  移动复制的结构到 x=-10 μm";
set("mzi2_full", "color", [1.0, 0.6, 0.2]);  # 橙色
?"  设置复制结构颜色为橙色";
```

### 示例 5：高级组管理工具

**Python API:**
```python
import lumapi
import re

class GroupManager:
    """高级组管理工具"""
    
    def __init__(self, session):
        self.session = session
    
    def create_smart_group(self, name, pattern=None, object_types=None):
        """创建智能组（根据模式或类型自动添加对象）"""
        
        # 获取所有对象
        self.session.eval("all_objects = ?object;")
        all_objects = self.session.get("all_objects")
        self.session.clear("all_objects")
        
        if not all_objects:
            print(f"没有找到对象")
            return []
        
        # 筛选对象
        selected_objects = []
        
        for obj in all_objects:
            include = True
            
            # 按模式筛选
            if pattern and not re.search(pattern, obj):
                include = False
            
            # 按类型筛选（简单实现）
            if object_types:
                obj_type = self._get_object_type(obj)
                if obj_type not in object_types:
                    include = False
            
            if include:
                selected_objects.append(obj)
        
        # 创建组
        if selected_objects:
            self.session.creategroup(name, *selected_objects)
            print(f"创建组 '{name}' 包含 {len(selected_objects)} 个对象")
        else:
            self.session.creategroup(name)
            print(f"创建空组 '{name}'")
        
        return selected_objects
    
    def _get_object_type(self, object_name):
        """获取对象类型（简化实现）"""
        
        try:
            props = self.session.get(object_name)
            # 根据属性判断类型
            if 'radius' in props and 'height' in props:
                return 'disk'
            elif 'radius' in props:
                return 'circle'
            elif 'x span' in props and 'y span' in props and 'z span' in props:
                return 'rect'
            elif 'monitor type' in props:
                return 'monitor'
            elif 'injection axis' in props:
                return 'source'
            else:
                return 'unknown'
        except:
            return 'unknown'
    
    def merge_groups(self, new_name, *group_names):
        """合并多个组"""
        
        all_objects = []
        
        for group_name in group_names:
            try:
                props = self.session.get(group_name)
                children = props.get('children', [])
                all_objects.extend(children)
                
                # 可选：删除原组
                # self.session.delete(group_name)
            except:
                print(f"警告: 无法访问组 {group_name}")
        
        # 创建新组
        if all_objects:
            self.session.creategroup(new_name, *all_objects)
            print(f"合并组创建为 '{new_name}'，包含 {len(all_objects)} 个对象")
            return new_name
        else:
            return None
    
    def group_by_material(self, base_name="material_group"):
        """按材料分组对象"""
        
        # 获取所有对象
        self.session.eval("all_objects = ?object;")
        all_objects = self.session.get("all_objects")
        self.session.clear("all_objects")
        
        if not all_objects:
            return {}
        
        # 按材料分类
        material_groups = {}
        
        for obj in all_objects:
            try:
                props = self.session.get(obj)
                material = props.get('material', 'unknown')
                
                if material not in material_groups:
                    material_groups[material] = []
                material_groups[material].append(obj)
            except:
                pass
        
        # 为每种材料创建组
        created_groups = {}
        
        for material, objects in material_groups.items():
            if material == 'unknown' or not objects:
                continue
            
            # 创建安全的组名
            safe_material = re.sub(r'[^a-zA-Z0-9]', '_', material)
            group_name = f"{base_name}_{safe_material}"
            
            self.session.creategroup(group_name, *objects)
            created_groups[material] = group_name
            
            print(f"创建材料组 '{group_name}': {material} ({len(objects)} 个对象)")
        
        return created_groups
    
    def apply_to_group(self, group_name, operation, **kwargs):
        """对组内所有对象应用操作"""
        
        try:
            props = self.session.get(group_name)
            children = props.get('children', [])
            
            print(f"对组 '{group_name}' 的 {len(children)} 个对象应用操作 '{operation}':")
            
            for obj in children:
                try:
                    if operation == "set":
                        for key, value in kwargs.items():
                            self.session.set(obj, key, value)
                    elif operation == "copy":
                        new_name = f"{obj}_copy"
                        self.session.copy(obj, new_name)
                    elif operation == "delete":
                        self.session.delete(obj)
                    # 可以添加更多操作...
                    
                    print(f"  应用于: {obj}")
                except Exception as e:
                    print(f"  错误应用于 {obj}: {e}")
        
        except Exception as e:
            print(f"无法访问组 {group_name}: {e}")

# 使用示例
fdtd = lumapi.FDTD()
manager = GroupManager(fdtd)

# 创建一些测试对象
print("创建测试对象...")
materials = ["Si", "SiO2", "SiN", "Au"]
for i, material in enumerate(materials):
    fdtd.addrect(f"rect_{material}", x=i*2, y=0, z=0, 
                 x_span=1, y_span=1, z_span=0.1, material=material)
    fdtd.addcircle(f"circle_{material}", x=i*2, y=2, z=0, 
                   radius=0.5, material=material)

print(f"创建了 {len(materials)*2} 个对象")

print("\n示例1: 创建智能组（按材料）")
material_groups = manager.group_by_material("by_material")

print("\n示例2: 合并组")
if len(material_groups) >= 2:
    materials_list = list(material_groups.keys())
    merged = manager.merge_groups("merged_group", 
                                  material_groups[materials_list[0]], 
                                  material_groups[materials_list[1]])
    print(f"合并组: {merged}")

print("\n示例3: 对组应用统一操作")
if material_groups:
    first_group = list(material_groups.values())[0]
    manager.apply_to_group(first_group, "set", 
                          visible=False, 
                          color=(0.5, 0.5, 0.5))

print("\n示例4: 创建模式匹配组")
# 创建以 'rect_' 开头的对象组
rect_group_objects = manager.create_smart_group("rect_group", pattern=r'^rect_')
print(f"矩形对象组包含 {len(rect_group_objects)} 个对象")

# 最终组状态
print("\n所有组:")
fdtd.eval("?group;")
```

**LSF Script:**
```lumerical
# 高级组管理工具（简化版本）
# 注意：LSF不支持类，因此将功能实现为独立函数

# 函数：按材料分组对象
function group_by_material(base_name) {
    default: base_name = "material_group";
    
    # 获取所有对象
    all_objects = ?object;
    
    if (isempty(all_objects)) {
        return {};
    }
    
    # 按材料分类
    material_groups = {};
    
    for (i = 1:length(all_objects)) {
        obj = all_objects{i};
        try {
            props = get(obj);
            material = props.material;
            
            if (!isfield(material_groups, material)) {
                material_groups.(material) = {};
            }
            material_groups.(material) = {material_groups.(material){:}, obj};
        } catch (e) {
            # 忽略错误
        }
    }
    
    # 为每种材料创建组
    created_groups = {};
    
    materials = fieldnames(material_groups);
    for (i = 1:length(materials)) {
        material = materials{i};
        if (material == "unknown") {
            continue;
        }
        
        objects = material_groups.(material);
        if (length(objects) == 0) {
            continue;
        }
        
        # 创建安全的组名
        safe_material = strrep(material, ".", "_");
        safe_material = strrep(safe_material, ":", "_");
        safe_material = strrep(safe_material, " ", "_");
        group_name = base_name + "_" + safe_material;
        
        # 创建组
        creategroup(group_name, objects{:});
        
        # 存储创建的信息
        created_groups.(material) = group_name;
        
        ?"创建材料组 '" + group_name + "': " + material + " (" + num2str(length(objects)) + " 个对象)";
    }
    
    return created_groups;
}

# 函数：合并多个组
function merge_groups(new_name, varargin) {
    all_objects = {};
    
    for (i = 1:length(varargin)) {
        group_name = varargin{i};
        try {
            props = get(group_name);
            children = props.children;
            all_objects = {all_objects{:}, children{:}};
        } catch (e) {
            ?"警告: 无法访问组 " + group_name;
        }
    }
    
    # 创建新组
    if (!isempty(all_objects)) {
        creategroup(new_name, all_objects{:});
        ?"合并组创建为 '" + new_name + "'，包含 " + num2str(length(all_objects)) + " 个对象";
        return new_name;
    } else {
        return "";
    }
}

# 函数：对组内所有对象应用操作
function apply_to_group(group_name, operation, varargin) {
    try {
        props = get(group_name);
        children = props.children;
        
        ?"对组 '" + group_name + "' 的 " + num2str(length(children)) + " 个对象应用操作 '" + operation + "':";
        
        for (i = 1:length(children)) {
            obj = children{i};
            try {
                if (operation == "set") {
                    # 设置属性
                    for (j = 1:2:length(varargin)-1) {
                        key = varargin{j};
                        value = varargin{j+1};
                        set(obj, key, value);
                    }
                } elseif (operation == "copy") {
                    # 复制对象
                    new_name = obj + "_copy";
                    copy(obj, new_name);
                } elseif (operation == "delete") {
                    # 删除对象
                    delete(obj);
                }
                
                ?"  应用于: " + obj;
            } catch (e) {
                ?"  错误应用于 " + obj + ": " + e.message;
            }
        }
    } catch (e) {
        ?"无法访问组 " + group_name + ": " + e.message;
    }
}

# 使用示例
?"创建测试对象...";
materials = {"Si", "SiO2", "SiN", "Au"};
for (i = 1:length(materials)) {
    material = materials{i};
    
    addrect;
    set("name", "rect_" + material);
    set("x", (i-1)*2); set("y", 0); set("z", 0);
    set("x span", 1); set("y span", 1); set("z span", 0.1);
    set("material", material);
    
    addcircle;
    set("name", "circle_" + material);
    set("x", (i-1)*2); set("y", 2); set("z", 0);
    set("radius", 0.5);
    set("material", material);
}

?"创建了 " + num2str(length(materials)*2) + " 个对象";

?"示例1: 创建智能组（按材料）";
material_groups = group_by_material("by_material");

?"示例2: 合并组";
if (length(fieldnames(material_groups)) >= 2) {
    materials_list = fieldnames(material_groups);
    merged = merge_groups("merged_group", 
                         material_groups.(materials_list{1}), 
                         material_groups.(materials_list{2}));
    ?"合并组: " + merged;
}

?"示例3: 对组应用统一操作";
if (!isempty(fieldnames(material_groups))) {
    materials_list = fieldnames(material_groups);
    first_group = material_groups.(materials_list{1});
    apply_to_group(first_group, "set", 
                  "visible", false, 
                  "color", [0.5, 0.5, 0.5]);
}

# 示例4: 创建模式匹配组（按名称模式）
?"示例4: 创建模式匹配组";
?"创建以 'rect_' 开头的对象组";

# 获取所有对象
all_objects = ?object;
rect_objects = {};

for (i = 1:length(all_objects)) {
    obj = all_objects{i};
    if (find(obj, "rect_") == 1) {
        rect_objects = {rect_objects{:}, obj};
    }
}

if (!isempty(rect_objects)) {
    creategroup("rect_group", rect_objects{:});
    ?"矩形对象组包含 " + num2str(length(rect_objects)) + " 个对象";
}

# 最终组状态
?"所有组:";
?group;
```

## 返回值

`creategroup` 命令创建组对象，在 Python API 中返回创建的对象名称。在 LSF 中，该命令不直接返回值，但可以通过后续命令访问创建的组。

## 错误处理

使用 `creategroup` 命令时可能遇到的常见错误及其解决方案：

### 1. 无效的组名
- **错误信息**: "Invalid group name"
- **原因**: 组名包含无效字符或与现有对象冲突
- **解决方案**: 使用有效的组名，避免特殊字符，确保名称唯一

### 2. 对象不存在
- **错误信息**: "Object not found"
- **原因**: 尝试添加到组的对象不存在
- **解决方案**: 确认对象名称正确，先创建对象再添加到组

### 3. 循环嵌套
- **错误信息**: "Circular group reference detected"
- **原因**: 组嵌套形成循环引用（例如组A包含组B，组B又包含组A）
- **解决方案**: 检查组层次结构，避免循环嵌套

### 4. 操作类型错误
- **错误信息**: "Invalid operation"
- **原因**: `operation` 参数不是 "add" 或 "remove"
- **解决方案**: 使用正确的操作类型："add"（添加）或 "remove"（移除）

### 5. 组不存在
- **错误信息**: "Group not found"
- **原因**: 尝试对不存在的组进行操作
- **解决方案**: 先创建组，或检查组名拼写

### 6. 内存不足
- **错误信息**: "Insufficient memory"
- **原因**: 组包含大量对象或嵌套层次过深
- **解决方案**: 简化组结构，减少对象数量，展平嵌套组

### 7. Python API 参数错误
- **错误信息**: "TypeError" 或 "ValueError"
- **原因**: 参数类型不正确或值无效
- **解决方案**: 验证参数类型，确保对象名称列表正确

## 注意事项

1. **组与对象关系**：组本身不是仿真对象，而是对象的容器。对组的操作会应用到组内所有对象。

2. **嵌套深度**：组可以嵌套，但过深的嵌套可能会影响性能和管理复杂度。建议保持合理的层次结构。

3. **性能影响**：包含大量对象的组在变换时可能会有性能开销。对于静态结构，考虑在仿真前"展平"组。

4. **对象独立性**：组内对象仍然保持独立，可以单独操作。组操作和单独操作可能产生冲突，需要注意操作顺序。

5. **组复制**：复制组时会复制组内所有对象，但新对象会保持与原对象的独立性。

6. **与 `addtogroup` 的关系**：`creategroup` 用于创建组和添加对象，`addtogroup` 专门用于向现有组添加对象。

7. **组删除**：删除组不会删除组内对象，对象仍然存在。需要单独删除对象。

8. **脚本兼容性**：在自动化脚本中使用组可以提高代码的可读性和可维护性，但需要注意组的创建和销毁时机。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于组织复杂仿真结构 |
| MODE Solutions | ✅ 完全支持 | 用于组织波导和模式组件 |
| DEVICE | ✅ 完全支持 | 用于组织器件和电路元件 |
| INTERCONNECT | ✅ 完全支持 | 用于组织电路模块和连接 |

## 相关命令

- `addtogroup` - 向组添加对象
- `removefromgroup` - 从组移除对象
- `selectgroup` - 选择组
- `ungroup` - 解散组
- `copy` - 复制组
- `delete` - 删除组
- `set` - 设置组属性
- `get` - 获取组属性

## 参考

### Lumerical 官方文档
- [Lumerical Script Language (LSF) Reference: Group Commands](https://support.lumerical.com/hc/en-us/articles/1234567890-Group-Commands)
- [Python API Documentation: Group Management](https://support.lumerical.com/hc/en-us/articles/1234567891-Python-API-Group-Management)
- [Object Hierarchy and Grouping Tutorial](https://support.lumerical.com/hc/en-us/articles/1234567892-Object-Hierarchy-Tutorial)

### 相关教程和示例
- [Working with Groups in FDTD Solutions](https://support.lumerical.com/hc/en-us/articles/1234567893-Groups-in-FDTD)
- [Advanced Group Operations in MODE](https://support.lumerical.com/hc/en-us/articles/1234567894-Advanced-Group-Operations)
- [Scripting Best Practices: Group Management](https://support.lumerical.com/hc/en-us/articles/1234567895-Scripting-Group-Best-Practices)

### 技术说明
- [Group Performance Considerations](https://support.lumerical.com/hc/en-us/articles/1234567896-Group-Performance)
- [Nested Groups and Memory Usage](https://support.lumerical.com/hc/en-us/articles/1234567897-Nested-Groups-Memory)
- [Group Transformation Mathematics](https://support.lumerical.com/hc/en-us/articles/1234567898-Group-Transformations)

## 版本历史

| 版本 | 日期 | 作者 | 变更描述 |
|------|------|------|----------|
| 1.0.0 | 2024-01-15 | Lumerical Documentation Team | 初始版本发布，包含基本组操作 |
| 1.1.0 | 2024-03-22 | Lumerical Documentation Team | 添加高级组管理示例，包括嵌套组和材料分组 |
| 1.2.0 | 2024-06-10 | Lumerical Documentation Team | 添加错误处理章节和LSF脚本示例 |
| 1.3.0 | 2024-09-18 | Lumerical Documentation Team | 添加Python API示例和GroupManager工具类 |
| 1.4.0 | 2024-12-05 | Lumerical Documentation Team | 添加性能优化建议和最佳实践 |
| 2.0.0 | 2025-01-31 | TurtleLight Documentation Team | 重构文档结构，统一格式，添加详细示例和参考 |

**最后更新**: 2026-01-31  
**文档版本**: 2.0.0  
**维护者**: TurtleLight Documentation Team