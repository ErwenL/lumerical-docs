# `edit` - 编辑对象

## 概述

`edit` 命令用于打开 Lumerical 的对象编辑器对话框，允许用户以图形界面方式查看和修改对象属性。该命令为脚本提供了与 Lumerical GUI 交互的能力，特别适用于需要用户交互或可视化编辑的场景。

主要功能：
- **打开编辑器**：为指定对象打开属性编辑器对话框
- **交互式编辑**：允许用户在 GUI 中修改对象属性
- **属性查看**：以结构化方式查看对象的所有属性
- **批量编辑**：支持同时编辑多个对象
- **实时预览**：某些编辑器提供实时预览功能
- **验证输入**：通过对话框进行输入验证

典型应用：
- 交互式脚本中的用户参数输入
- 复杂对象的可视化配置
- 调试时查看对象详细属性
- 教学和演示中的交互示例
- 需要用户确认的参数设置
- 复杂结构的分步构建

## 语法

### LSF 语法
```lumerical
edit;                     # 打开选中对象的编辑器
edit("object_name");      # 打开指定对象的编辑器
edit("object_name", "property");  # 打开对象的特定属性编辑器
edit("all");              # 打开所有对象的编辑器（如果支持）
```

### Python API
```python
session.edit()                     # 打开选中对象的编辑器
session.edit("object_name")        # 打开指定对象的编辑器
session.edit("object_name", "property")  # 打开对象的特定属性编辑器
session.edit("all")                # 打开所有对象的编辑器（如果支持）
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `object_name` | string | 要编辑的对象名称。如果省略，则编辑当前选中对象。 | 否 |
| `property` | string | 要编辑的特定属性名称。如果指定，直接打开该属性的编辑器。 | 否 |

## 配置属性

`edit` 命令本身没有可配置属性，但编辑器行为受以下相关设置影响：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `editor mode` | string | "advanced" | 编辑器模式："simple"（简单）、"advanced"（高级）、"expert"（专家）。 |
| `auto apply` | bool | true | 是否自动应用更改（某些编辑器）。 |
| `live preview` | bool | true | 是否启用实时预览（如果支持）。 |
| `editor timeout` | number | 0 | 编辑器超时时间（秒），0表示无超时。 |
| `modal editing` | bool | true | 是否使用模态对话框（阻止其他操作）。 |
| `remember size` | bool | true | 是否记住编辑器窗口大小。 |
| `remember position` | bool | true | 是否记住编辑器窗口位置。 |
| `show advanced` | bool | false | 是否显示高级属性。 |
| `show read only` | bool | false | 是否显示只读属性。 |

## 返回值

`edit` 命令没有返回值。该命令打开 Lumerical 的对象编辑器对话框，允许用户以图形界面方式查看和修改对象属性。命令的成功与否通常通过能否打开编辑器来判断，而不是通过返回值。

在 Python API 中，`session.edit()` 通常返回 `None`。如果命令失败（例如对象不存在或编辑器不可用），Lumerical 会抛出异常。

## 错误处理

### 常见错误

1. **对象不存在错误**
   ```python
   # 错误：对象 "nonexistent" 不存在
   fdtd.edit("nonexistent")
   ```
   解决方案：使用 `add` 命令先创建对象，或使用 `hasexisting` 检查对象是否存在。

2. **编辑器不可用错误**
   ```python
   # 错误：在无头模式中编辑器不可用
   fdtd.edit("existing_object")
   ```
   解决方案：检查运行环境是否支持图形界面，或在无头模式中使用 `set` 命令替代。

3. **属性不存在错误**
   ```python
   # 错误：属性 "invalid_property" 不存在
   fdtd.edit("existing_object", "invalid_property")
   ```
   解决方案：检查属性名称拼写，参考对象的可用属性列表。

4. **权限不足错误**
   ```python
   # 错误：对象被锁定或只读
   fdtd.edit("locked_object")
   ```
   解决方案：检查对象状态，确保有修改权限。

### Python 错误处理示例

```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addrect("test_rect", x=0, y=0, z=0, x_span=1e-6, y_span=0.5e-6, material="Si")
    
    # 尝试打开编辑器
    fdtd.edit("test_rect")
    
    # 尝试编辑不存在的对象
    fdtd.edit("nonexistent")
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
    # 检查错误类型
    error_str = str(e).lower()
    if "object" in error_str and "not found" in error_str:
        print("错误: 对象不存在")
    elif "editor" in error_str and "not available" in error_str:
        print("错误: 编辑器不可用")
    elif "property" in error_str and "not found" in error_str:
        print("错误: 属性不存在")
    elif "permission" in error_str or "locked" in error_str:
        print("错误: 权限不足")
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

### 示例 1：基本对象编辑

#### LSF 脚本
```lumerical
// 创建矩形对象
addrect;
set("name", "test_rectangle");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 1e-6);
set("y span", 0.5e-6);
set("z span", 0.2e-6);
set("material", "SiO2 (Glass) - Palik");

// 1. 编辑当前选中对象
select("test_rectangle");
edit;  // 打开当前选中对象的编辑器

// 2. 编辑指定对象
edit("test_rectangle");

// 3. 编辑特定属性
edit("test_rectangle", "material");

// 4. 编辑所有对象（如果支持）
// edit("all");

// 5. 模拟交互编辑后验证
? "编辑完成后验证对象属性...";
x_span = get("test_rectangle::x span");
material = get("test_rectangle::material");
?format "编辑后属性 - x span: %.3e m, 材料: %s", x_span, material;

// 清理
delete("test_rectangle");
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本对象编辑演示...")

# 1. 创建测试对象
print("创建测试对象...")

# 创建矩形
fdtd.addrect()
fdtd.set("name", "test_rectangle")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 1e-6)
fdtd.set("y span", 0.5e-6)
fdtd.set("z span", 0.2e-6)
fdtd.set("material", "SiO2 (Glass) - Palik")

print("矩形对象已创建")

# 2. 打开对象编辑器
print("\n打开矩形对象编辑器...")
print("注意：这将打开 Lumerical GUI 编辑器对话框")
print("在非交互式环境中，此命令可能有限制")

# 在可能的情况下打开编辑器
try:
    # 打开编辑器
    fdtd.edit("test_rectangle")
    print("编辑器已打开（如果支持）")
    
    # 模拟用户编辑后的操作
    print("假设用户在编辑器中进行了修改...")
    
    # 获取编辑后的属性
    new_x_span = fdtd.get("test_rectangle::x span")
    new_material = fdtd.get("test_rectangle::material")
    
    print(f"编辑后属性:")
    print(f"  x span: {new_x_span} m")
    print(f"  材料: {new_material}")
    
except Exception as e:
    print(f"编辑器命令受限: {e}")
    print("在无头模式或某些环境中，edit命令可能不可用")

# 3. 编辑特定属性
print("\n尝试编辑特定属性...")
try:
    # 打开特定属性编辑器
    fdtd.edit("test_rectangle", "material")
    print("材料编辑器已打开（如果支持）")
    
    # 模拟材料选择
    print("假设用户选择了新材料...")
    fdtd.set("test_rectangle::material", "Si (Silicon) - Palik")
    
except Exception as e:
    print(f"特定属性编辑受限: {e}")

# 4. 编辑当前选中对象
print("\n编辑当前选中对象...")
try:
    # 选中对象
    fdtd.select("test_rectangle")
    print("对象已选中")
    
    # 打开编辑器（不指定对象名，使用当前选中）
    fdtd.edit()
    print("当前选中对象的编辑器已打开（如果支持）")
    
except Exception as e:
    print(f"编辑选中对象受限: {e}")

# 5. 创建多个对象并编辑
print("\n创建多个对象并尝试编辑...")

# 创建第二个对象
fdtd.addcylinder()
fdtd.set("name", "test_cylinder")
fdtd.set("x", 1e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("radius", 0.3e-6)
fdtd.set("z span", 0.5e-6)
fdtd.set("material", "Au (Gold) - Johnson and Christy")

print("圆柱对象已创建")

try:
    # 尝试编辑多个对象（可能不支持）
    fdtd.edit("all")
    print("所有对象编辑器已打开（如果支持）")
except Exception as e:
    print(f"编辑所有对象受限: {e}")
    print("Lumerical 通常不支持同时编辑多个不同对象")

# 6. 编辑器交互模拟
print("\n模拟编辑器交互工作流...")

class InteractiveEditorWorkflow:
    """交互式编辑器工作流模拟"""
    
    def __init__(self, session):
        self.session = session
        self.editor_state = {}
    
    def simulate_edit_rectangle(self, rect_name):
        """模拟矩形编辑过程"""
        
        print(f"模拟编辑矩形: {rect_name}")
        
        # 获取当前属性
        properties = self._get_object_properties(rect_name)
        print("当前属性:")
        for prop, value in properties.items():
            print(f"  {prop}: {value}")
        
        # 模拟用户修改
        print("\n模拟用户修改:")
        
        # 修改尺寸
        new_x_span = properties.get("x span", 1e-6) * 1.5
        print(f"  将 x span 从 {properties.get('x span')} 修改为 {new_x_span}")
        self.session.set(f"{rect_name}::x span", new_x_span)
        
        # 修改材料
        new_material = "Si3N4 (Silicon Nitride) - Phillip"
        print(f"  将材料从 {properties.get('material')} 修改为 {new_material}")
        self.session.set(f"{rect_name}::material", new_material)
        
        # 修改颜色（如果支持）
        try:
            self.session.set(f"{rect_name}::color", [0, 0, 1])  # 蓝色
            print("  将颜色修改为蓝色")
        except:
            pass
        
        # 记录编辑器状态
        self.editor_state[rect_name] = {
            'edited': True,
            'changes': {
                'x span': new_x_span,
                'material': new_material
            }
        }
        
        return new_x_span, new_material
    
    def simulate_edit_cylinder(self, cyl_name):
        """模拟圆柱编辑过程"""
        
        print(f"模拟编辑圆柱: {cyl_name}")
        
        # 获取当前属性
        properties = self._get_object_properties(cyl_name)
        print("当前属性:")
        for prop, value in properties.items():
            print(f"  {prop}: {value}")
        
        # 模拟用户修改
        print("\n模拟用户修改:")
        
        # 修改半径
        new_radius = properties.get("radius", 0.3e-6) * 0.8
        print(f"  将半径从 {properties.get('radius')} 修改为 {new_radius}")
        self.session.set(f"{cyl_name}::radius", new_radius)
        
        # 修改高度
        new_z_span = properties.get("z span", 0.5e-6) * 1.2
        print(f"  将 z span 从 {properties.get('z span')} 修改为 {new_z_span}")
        self.session.set(f"{cyl_name}::z span", new_z_span)
        
        # 记录编辑器状态
        self.editor_state[cyl_name] = {
            'edited': True,
            'changes': {
                'radius': new_radius,
                'z span': new_z_span
            }
        }
        
        return new_radius, new_z_span
    
    def _get_object_properties(self, obj_name):
        """获取对象属性（简化版）"""
        
        # 获取常见属性
        properties = {}
        
        try:
            properties["name"] = obj_name
            properties["x"] = self.session.get(f"{obj_name}::x")
            properties["y"] = self.session.get(f"{obj_name}::y")
            properties["z"] = self.session.get(f"{obj_name}::z")
            
            # 尝试获取其他属性
            for prop in ["x span", "y span", "z span", "radius", "material", "color"]:
                try:
                    properties[prop] = self.session.get(f"{obj_name}::{prop}")
                except:
                    pass
                    
        except Exception as e:
            print(f"获取属性失败: {e}")
        
        return properties
    
    def show_edit_summary(self):
        """显示编辑摘要"""
        
        print("\n编辑摘要:")
        print("=" * 50)
        
        for obj_name, state in self.editor_state.items():
            if state.get('edited'):
                print(f"对象: {obj_name}")
                print(f"  修改的属性:")
                for prop, value in state['changes'].items():
                    print(f"    {prop}: {value}")
                print()

# 创建交互式工作流
workflow = InteractiveEditorWorkflow(fdtd)

# 模拟编辑过程
print("\n开始模拟编辑工作流...")

# 模拟编辑矩形
workflow.simulate_edit_rectangle("test_rectangle")

# 模拟编辑圆柱
workflow.simulate_edit_cylinder("test_cylinder")

# 显示摘要
workflow.show_edit_summary()

# 7. 验证编辑结果
print("\n验证编辑结果...")

def verify_edits(session):
    """验证编辑结果"""
    
    print("验证矩形编辑:")
    rect_x_span = session.get("test_rectangle::x span")
    rect_material = session.get("test_rectangle::material")
    
    print(f"  x span: {rect_x_span} m (应为 {1e-6 * 1.5} m)")
    print(f"  材料: {rect_material} (应为 Si3N4)")
    
    print("\n验证圆柱编辑:")
    cyl_radius = session.get("test_cylinder::radius")
    cyl_z_span = session.get("test_cylinder::z span")
    
    print(f"  半径: {cyl_radius} m (应为 {0.3e-6 * 0.8} m)")
    print(f"  z span: {cyl_z_span} m (应为 {0.5e-6 * 1.2} m)")
    
    # 计算误差
    expected_rect_x_span = 1e-6 * 1.5
    expected_cyl_radius = 0.3e-6 * 0.8
    expected_cyl_z_span = 0.5e-6 * 1.2
    
    errors = []
    
    if abs(rect_x_span - expected_rect_x_span) > 1e-12:
        errors.append(f"矩形 x span 不匹配: {rect_x_span} vs {expected_rect_x_span}")
    
    if rect_material != "Si3N4 (Silicon Nitride) - Phillip":
        errors.append(f"矩形材料不匹配: {rect_material}")
    
    if abs(cyl_radius - expected_cyl_radius) > 1e-12:
        errors.append(f"圆柱半径不匹配: {cyl_radius} vs {expected_cyl_radius}")
    
    if abs(cyl_z_span - expected_cyl_z_span) > 1e-12:
        errors.append(f"圆柱 z span 不匹配: {cyl_z_span} vs {expected_cyl_z_span}")
    
    if errors:
        print("\n验证失败:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("\n验证通过: 所有编辑已正确应用")
        return True

# 执行验证
verify_edits(fdtd)

# 8. 清理
print("\n清理测试对象...")
try:
    fdtd.delete("test_rectangle")
    fdtd.delete("test_cylinder")
    print("测试对象已删除")
except:
    print("删除对象失败")

print("\n基本对象编辑演示完成!")
```

### 示例 2：复杂结构交互式设计
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("复杂结构交互式设计演示...")

class InteractiveDesignStudio:
    """交互式设计工作室"""
    
    def __init__(self, session):
        self.session = session
        self.design_history = []
        self.current_design = None
        
        # 创建基础结构
        self._setup_base_structure()
    
    def _setup_base_structure(self):
        """设置基础结构"""
        
        print("设置基础结构...")
        
        # 创建基板
        self.session.addrect()
        self.session.set("name", "substrate")
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", -0.5e-6)
        self.session.set("x span", 10e-6)
        self.session.set("y span", 10e-6)
        self.session.set("z span", 1e-6)
        self.session.set("material", "SiO2 (Glass) - Palik")
        
        # 创建硅层
        self.session.addrect()
        self.session.set("name", "si_layer")
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", 0.11e-6)  # 220nm硅层的一半高度
        self.session.set("x span", 8e-6)
        self.session.set("y span", 8e-6)
        self.session.set("z span", 0.22e-6)
        self.session.set("material", "Si (Silicon) - Palik")
        
        print("基础结构创建完成")
    
    def design_waveguide_interactive(self):
        """交互式设计波导"""
        
        print("\n交互式波导设计")
        print("=" * 50)
        
        # 创建波导
        wg_name = "designed_waveguide"
        self.session.addrect()
        self.session.set("name", wg_name)
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", 0.11e-6)
        
        # 初始参数
        initial_params = {
            "x span": 5e-6,
            "y span": 0.5e-6,
            "z span": 0.22e-6,
            "material": "Si (Silicon) - Palik"
        }
        
        # 设置初始参数
        for param, value in initial_params.items():
            self.session.set(f"{wg_name}::{param}", value)
        
        print("初始波导已创建")
        print("参数:")
        for param, value in initial_params.items():
            print(f"  {param}: {value}")
        
        # 模拟交互式编辑
        print("\n模拟交互式编辑过程...")
        
        # 第一步：编辑尺寸
        print("1. 编辑波导尺寸")
        self._simulate_editor_open(wg_name, "尺寸参数")
        
        # 用户修改尺寸
        new_params = {
            "x span": 6e-6,    # 加长
            "y span": 0.45e-6, # 变窄
            "z span": 0.25e-6  # 加厚
        }
        
        for param, value in new_params.items():
            self.session.set(f"{wg_name}::{param}", value)
            print(f"  修改 {param}: {initial_params[param]} -> {value}")
        
        # 第二步：编辑材料
        print("\n2. 编辑波导材料")
        self._simulate_editor_open(wg_name, "material")
        
        # 用户选择材料
        new_material = "Si3N4 (Silicon Nitride) - Phillip"
        self.session.set(f"{wg_name}::material", new_material)
        print(f"  修改材料: {initial_params['material']} -> {new_material}")
        
        # 第三步：编辑位置
        print("\n3. 编辑波导位置")
        self._simulate_editor_open(wg_name, "位置")
        
        # 用户移动位置
        new_position = {"x": 1e-6, "y": 0.5e-6}
        self.session.set(f"{wg_name}::x", new_position["x"])
        self.session.set(f"{wg_name}::y", new_position["y"])
        print(f"  移动位置: x=0->{new_position['x']}, y=0->{new_position['y']}")
        
        # 记录设计历史
        design_step = {
            "object": wg_name,
            "type": "waveguide",
            "initial": initial_params,
            "final": {
                **new_params,
                "material": new_material,
                "position": new_position
            },
            "timestamp": "模拟交互编辑"
        }
        
        self.design_history.append(design_step)
        self.current_design = wg_name
        
        print("\n波导设计完成")
        self._show_design_summary(design_step)
        
        return wg_name
    
    def design_grating_coupler_interactive(self):
        """交互式设计光栅耦合器"""
        
        print("\n交互式光栅耦合器设计")
        print("=" * 50)
        
        # 创建光栅耦合器组
        gc_name = "designed_grating"
        
        # 初始参数
        initial_params = {
            "period": 0.63e-6,
            "duty_cycle": 0.5,
            "num_teeth": 20,
            "width": 12e-6,
            "height": 0.22e-6,
            "material": "Si (Silicon) - Palik"
        }
        
        print("创建光栅耦合器...")
        print("初始参数:")
        for param, value in initial_params.items():
            print(f"  {param}: {value}")
        
        # 创建光栅齿
        teeth = []
        for i in range(initial_params["num_teeth"]):
            tooth_name = f"{gc_name}_tooth_{i}"
            
            # 计算位置和尺寸
            x_pos = i * initial_params["period"]
            tooth_width = initial_params["period"] * initial_params["duty_cycle"]
            
            # 创建齿
            self.session.addrect()
            self.session.set("name", tooth_name)
            self.session.set("x", x_pos)
            self.session.set("y", 0)
            self.session.set("z", 0.11e-6)
            self.session.set("x span", tooth_width)
            self.session.set("y span", initial_params["width"])
            self.session.set("z span", initial_params["height"])
            self.session.set("material", initial_params["material"])
            
            teeth.append(tooth_name)
        
        print(f"创建了 {len(teeth)} 个光栅齿")
        
        # 模拟交互式编辑
        print("\n模拟交互式编辑过程...")
        
        # 第一步：编辑光栅参数
        print("1. 编辑光栅参数")
        self._simulate_editor_open(gc_name + "_tooth_0", "光栅参数")
        
        # 用户修改参数
        new_params = {
            "period": 0.65e-6,      # 增加周期
            "duty_cycle": 0.55,     # 增加占空比
            "num_teeth": 15,        # 减少齿数
            "width": 15e-6          # 增加宽度
        }
        
        print("用户修改:")
        for param, new_value in new_params.items():
            old_value = initial_params[param]
            print(f"  {param}: {old_value} -> {new_value}")
        
        # 重新创建光栅（简化：删除旧齿，创建新齿）
        print("\n重新创建光栅...")
        
        # 删除旧齿
        for tooth in teeth:
            try:
                self.session.delete(tooth)
            except:
                pass
        
        # 创建新齿
        new_teeth = []
        for i in range(new_params["num_teeth"]):
            tooth_name = f"{gc_name}_tooth_{i}"
            
            # 计算新位置和尺寸
            x_pos = i * new_params["period"]
            tooth_width = new_params["period"] * new_params["duty_cycle"]
            
            # 创建新齿
            self.session.addrect()
            self.session.set("name", tooth_name)
            self.session.set("x", x_pos)
            self.session.set("y", 0)
            self.session.set("z", 0.11e-6)
            self.session.set("x span", tooth_width)
            self.session.set("y span", new_params["width"])
            self.session.set("z span", initial_params["height"])
            self.session.set("material", initial_params["material"])
            
            new_teeth.append(tooth_name)
        
        print(f"重新创建了 {len(new_teeth)} 个光栅齿")
        
        # 第二步：编辑材料
        print("\n2. 编辑材料")
        self._simulate_editor_open(gc_name + "_tooth_0", "material")
        
        new_material = "Si3N4 (Silicon Nitride) - Phillip"
        for tooth in new_teeth:
            self.session.set(f"{tooth}::material", new_material)
        
        print(f"  修改材料: {initial_params['material']} -> {new_material}")
        
        # 第三步：编辑位置
        print("\n3. 编辑位置")
        self._simulate_editor_open(gc_name + "_tooth_0", "位置")
        
        # 移动整个光栅
        new_x = -5e-6
        new_y = 3e-6
        
        for i, tooth in enumerate(new_teeth):
            tooth_x = i * new_params["period"] + new_x
            self.session.set(f"{tooth}::x", tooth_x)
            self.session.set(f"{tooth}::y", new_y)
        
        print(f"  移动光栅: x=0->{new_x}, y=0->{new_y}")
        
        # 记录设计历史
        design_step = {
            "object": gc_name,
            "type": "grating_coupler",
            "initial": initial_params,
            "final": {
                **new_params,
                "material": new_material,
                "position": {"x": new_x, "y": new_y},
                "num_teeth_actual": len(new_teeth)
            },
            "teeth": new_teeth,
            "timestamp": "模拟交互编辑"
        }
        
        self.design_history.append(design_step)
        
        print("\n光栅耦合器设计完成")
        self._show_design_summary(design_step)
        
        return gc_name, new_teeth
    
    def _simulate_editor_open(self, object_name, editor_type):
        """模拟编辑器打开"""
        
        print(f"  打开 {object_name} 的 {editor_type} 编辑器...")
        
        # 在实际交互式环境中，这里会调用 fdtd.edit(object_name)
        # 但为了演示，我们只是模拟
        print(f"  [模拟] 编辑器窗口已打开")
        print(f"  [模拟] 用户正在查看和修改属性...")
    
    def _show_design_summary(self, design_step):
        """显示设计摘要"""
        
        print("\n设计摘要:")
        print("-" * 40)
        print(f"对象: {design_step['object']}")
        print(f"类型: {design_step['type']}")
        
        if design_step['type'] == 'waveguide':
            print("\n最终参数:")
            for param, value in design_step['final'].items():
                if param != 'position':
                    print(f"  {param}: {value}")
            
            pos = design_step['final'].get('position', {})
            print(f"  位置: x={pos.get('x', 0)}, y={pos.get('y', 0)}")
        
        elif design_step['type'] == 'grating_coupler':
            print("\n最终参数:")
            for param, value in design_step['final'].items():
                if param not in ['position', 'num_teeth_actual', 'teeth']:
                    print(f"  {param}: {value}")
            
            pos = design_step['final'].get('position', {})
            print(f"  位置: x={pos.get('x', 0)}, y={pos.get('y', 0)}")
            print(f"  齿数: {design_step['final'].get('num_teeth_actual', 0)}")
    
    def design_photonic_crystal_interactive(self):
        """交互式设计光子晶体"""
        
        print("\n交互式光子晶体设计")
        print("=" * 50)
        
        pc_name = "designed_photonic_crystal"
        
        # 初始参数
        initial_params = {
            "lattice_constant": 0.4e-6,
            "hole_radius": 0.12e-6,
            "num_periods_x": 5,
            "num_periods_y": 5,
            "slab_thickness": 0.22e-6,
            "material": "Si (Silicon) - Palik"
        }
        
        print("创建光子晶体...")
        print("初始参数:")
        for param, value in initial_params.items():
            print(f"  {param}: {value}")
        
        # 创建光子晶体平板
        slab_name = f"{pc_name}_slab"
        self.session.addrect()
        self.session.set("name", slab_name)
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", 0.11e-6)
        
        slab_span_x = (2 * initial_params["num_periods_x"] + 1) * initial_params["lattice_constant"]
        slab_span_y = (2 * initial_params["num_periods_y"] + 1) * initial_params["lattice_constant"]
        
        self.session.set("x span", slab_span_x)
        self.session.set("y span", slab_span_y)
        self.session.set("z span", initial_params["slab_thickness"])
        self.session.set("material", initial_params["material"])
        
        # 创建空气孔阵列
        holes = []
        hole_count = 0
        
        for i in range(-initial_params["num_periods_x"], initial_params["num_periods_x"] + 1):
            for j in range(-initial_params["num_periods_y"], initial_params["num_periods_y"] + 1):
                # 跳过中心位置
                if i == 0 and j == 0:
                    continue
                
                hole_name = f"{pc_name}_hole_{hole_count}"
                x_pos = i * initial_params["lattice_constant"]
                y_pos = j * initial_params["lattice_constant"]
                
                self.session.addcylinder()
                self.session.set("name", hole_name)
                self.session.set("x", x_pos)
                self.session.set("y", y_pos)
                self.session.set("z", 0.11e-6)
                self.session.set("radius", initial_params["hole_radius"])
                self.session.set("z span", initial_params["slab_thickness"] * 1.1)  # 稍厚以确保穿透
                self.session.set("material", "Air")
                
                holes.append(hole_name)
                hole_count += 1
        
        print(f"创建了光子晶体平板和 {hole_count} 个空气孔")
        
        # 模拟交互式编辑
        print("\n模拟交互式编辑过程...")
        
        # 第一步：编辑晶格参数
        print("1. 编辑晶格参数")
        self._simulate_editor_open(slab_name, "晶格参数")
        
        # 用户修改参数
        new_params = {
            "lattice_constant": 0.42e-6,  # 增加晶格常数
            "hole_radius": 0.15e-6,       # 增加孔半径
            "num_periods_x": 4,           # 减少周期数
            "num_periods_y": 4
        }
        
        print("用户修改:")
        for param, new_value in new_params.items():
            old_value = initial_params[param]
            print(f"  {param}: {old_value} -> {new_value}")
        
        # 重新计算平板尺寸
        new_slab_span_x = (2 * new_params["num_periods_x"] + 1) * new_params["lattice_constant"]
        new_slab_span_y = (2 * new_params["num_periods_y"] + 1) * new_params["lattice_constant"]
        
        # 更新平板
        self.session.set(f"{slab_name}::x span", new_slab_span_x)
        self.session.set(f"{slab_name}::y span", new_slab_span_y)
        
        # 删除旧孔
        for hole in holes:
            try:
                self.session.delete(hole)
            except:
                pass
        
        # 创建新孔
        new_holes = []
        new_hole_count = 0
        
        for i in range(-new_params["num_periods_x"], new_params["num_periods_x"] + 1):
            for j in range(-new_params["num_periods_y"], new_params["num_periods_y"] + 1):
                if i == 0 and j == 0:
                    continue
                
                hole_name = f"{pc_name}_hole_{new_hole_count}"
                x_pos = i * new_params["lattice_constant"]
                y_pos = j * new_params["lattice_constant"]
                
                self.session.addcylinder()
                self.session.set("name", hole_name)
                self.session.set("x", x_pos)
                self.session.set("y", y_pos)
                self.session.set("z", 0.11e-6)
                self.session.set("radius", new_params["hole_radius"])
                self.session.set("z span", initial_params["slab_thickness"] * 1.1)
                self.session.set("material", "Air")
                
                new_holes.append(hole_name)
                new_hole_count += 1
        
        print(f"重新创建了 {new_hole_count} 个空气孔")
        
        # 第二步：编辑材料
        print("\n2. 编辑材料")
        self._simulate_editor_open(slab_name, "material")
        
        new_material = "GaAs (Gallium Arsenide) - Palik"
        self.session.set(f"{slab_name}::material", new_material)
        print(f"  修改材料: {initial_params['material']} -> {new_material}")
        
        # 第三步：编辑缺陷
        print("\n3. 编辑缺陷（引入线缺陷）")
        self._simulate_editor_open(slab_name, "缺陷设计")
        
        # 移除一行孔以创建波导
        print("  移除中心一行孔以创建线缺陷波导...")
        
        # 找到并移除 y=0 的一行孔（除了中心）
        holes_to_remove = []
        for hole in new_holes:
            try:
                y_pos = self.session.get(f"{hole}::y")
                if abs(y_pos) < 1e-9:  # y ≈ 0
                    holes_to_remove.append(hole)
            except:
                pass
        
        for hole in holes_to_remove:
            try:
                self.session.delete(hole)
                new_holes.remove(hole)
            except:
                pass
        
        print(f"  移除了 {len(holes_to_remove)} 个孔以创建线缺陷")
        
        # 记录设计历史
        design_step = {
            "object": pc_name,
            "type": "photonic_crystal",
            "initial": initial_params,
            "final": {
                **new_params,
                "material": new_material,
                "slab_thickness": initial_params["slab_thickness"],
                "hole_count": new_hole_count - len(holes_to_remove),
                "has_defect": True,
                "defect_type": "line_defect"
            },
            "holes": new_holes,
            "slab": slab_name,
            "timestamp": "模拟交互编辑"
        }
        
        self.design_history.append(design_step)
        
        print("\n光子晶体设计完成")
        self._show_design_summary(design_step)
        
        return pc_name, slab_name, new_holes
    
    def show_complete_design(self):
        """显示完整设计"""
        
        print("\n" + "=" * 60)
        print("完整交互式设计摘要")
        print("=" * 60)
        
        print(f"设计步骤数: {len(self.design_history)}")
        print(f"总对象数: {self._count_total_objects()}")
        
        print("\n设计历史:")
        for i, step in enumerate(self.design_history):
            print(f"\n步骤 {i+1}: {step['type']} - {step['object']}")
            print(f"  时间: {step['timestamp']}")
            
            if step['type'] == 'waveguide':
                print(f"  最终长度: {step['final'].get('x span', 'N/A')}")
                print(f"  最终材料: {step['final'].get('material', 'N/A')}")
            
            elif step['type'] == 'grating_coupler':
                print(f"  齿数: {step['final'].get('num_teeth_actual', 'N/A')}")
                print(f"  周期: {step['final'].get('period', 'N/A')}")
            
            elif step['type'] == 'photonic_crystal':
                print(f"  孔数: {step['final'].get('hole_count', 'N/A')}")
                print(f"  缺陷: {step['final'].get('defect_type', '无')}")
        
        print("\n设计完成!")
    
    def _count_total_objects(self):
        """计算总对象数"""
        
        try:
            all_objects = self.session.get("objects")
            return len(all_objects)
        except:
            return 0

# 创建交互式设计工作室
design_studio = InteractiveDesignStudio(fdtd)

# 执行交互式设计流程
print("开始交互式设计流程...")

# 1. 设计波导
waveguide = design_studio.design_waveguide_interactive()

# 2. 设计光栅耦合器
grating, grating_teeth = design_studio.design_grating_coupler_interactive()

# 3. 设计光子晶体
photonic_crystal, pc_slab, pc_holes = design_studio.design_photonic_crystal_interactive()

# 显示完整设计
design_studio.show_complete_design()

# 最终验证
print("\n最终验证...")
print("检查所有设计对象是否存在...")

all_objects = fdtd.get("objects")
print(f"总对象数: {len(all_objects)}")

# 按类型分组
object_types = {}
for obj in all_objects:
    try:
        obj_type = fdtd.get(f"{obj}::object type")
        object_types[obj_type] = object_types.get(obj_type, 0) + 1
    except:
        object_types["unknown"] = object_types.get("unknown", 0) + 1

print("对象类型分布:")
for obj_type, count in object_types.items():
    print(f"  {obj_type}: {count}")

print("\n交互式设计演示完成!")
```

### 示例 3：编辑器集成和自动化
```python
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("编辑器集成和自动化演示...")

class EditorAutomation:
    """编辑器自动化工具"""
    
    def __init__(self, session):
        self.session = session
        self.editor_states = {}
        self.automation_log = []
        
        # 编辑器配置
        self.editor_config = {
            'auto_apply': True,
            'live_preview': True,
            'modal_dialogs': False,
            'timeout': 30  # 秒
        }
    
    def log_automation(self, action, details):
        """记录自动化操作"""
        
        log_entry = {
            'timestamp': time.time(),
            'action': action,
            'details': details
        }
        
        self.automation_log.append(log_entry)
        print(f"[自动化] {action}: {details}")
    
    def configure_editors(self, config=None):
        """配置编辑器设置"""
        
        if config:
            self.editor_config.update(config)
        
        self.log_automation("配置编辑器", self.editor_config)
        
        # 在实际应用中，这里会设置编辑器参数
        # 例如：set('editor mode', 'advanced') 等
        
        return self.editor_config
    
    def batch_edit_objects(self, object_names, property_changes):
        """批量编辑对象"""
        
        self.log_automation("开始批量编辑", {
            'objects': object_names,
            'changes': property_changes
        })
        
        results = {}
        
        for obj_name in object_names:
            try:
                # 检查对象是否存在
                obj_type = self.session.get(f"{obj_name}::object type")
                
                self.log_automation("编辑对象", {
                    'object': obj_name,
                    'type': obj_type
                })
                
                # 应用属性更改
                obj_results = {}
                for prop, value in property_changes.items():
                    try:
                        # 保存原始值
                        original_value = self.session.get(f"{obj_name}::{prop}")
                        
                        # 应用新值
                        self.session.set(f"{obj_name}::{prop}", value)
                        
                        # 验证更改
                        new_value = self.session.get(f"{obj_name}::{prop}")
                        
                        obj_results[prop] = {
                            'original': original_value,
                            'new': new_value,
                            'success': True
                        }
                        
                        self.log_automation("属性更改", {
                            'object': obj_name,
                            'property': prop,
                            'from': original_value,
                            'to': new_value
                        })
                        
                    except Exception as e:
                        obj_results[prop] = {
                            'success': False,
                            'error': str(e)
                        }
                        
                        self.log_automation("属性更改失败", {
                            'object': obj_name,
                            'property': prop,
                            'error': str(e)
                        })
                
                results[obj_name] = {
                    'type': obj_type,
                    'changes': obj_results,
                    'success': all(r['success'] for r in obj_results.values())
                }
                
                # 打开编辑器查看结果（模拟）
                self._simulate_editor_open(obj_name)
                
            except Exception as e:
                results[obj_name] = {
                    'success': False,
                    'error': str(e)
                }
                
                self.log_automation("对象编辑失败", {
                    'object': obj_name,
                    'error': str(e)
                })
        
        self.log_automation("批量编辑完成", {
            'total': len(object_names),
            'successful': sum(1 for r in results.values() if r.get('success', False))
        })
        
        return results
    
    def _simulate_editor_open(self, object_name):
        """模拟编辑器打开（用于验证）"""
        
        # 在实际应用中，这里会调用 self.session.edit(object_name)
        # 但为了演示，我们只是记录
        
        self.log_automation("模拟编辑器打开", {'object': object_name})
        
        # 模拟短暂延迟
        time.sleep(0.1)
    
    def edit_with_validation(self, object_name, property_changes, validation_rules=None):
        """带验证的编辑"""
        
        self.log_automation("开始带验证的编辑", {
            'object': object_name,
            'changes': property_changes,
            'rules': validation_rules
        })
        
        # 检查对象
        try:
            obj_type = self.session.get(f"{obj_name}::object type")
        except Exception as e:
            self.log_automation("对象不存在", {'error': str(e)})
            return {'success': False, 'error': f"对象不存在: {e}"}
        
        # 验证规则
        if validation_rules is None:
            validation_rules = {}
        
        # 应用更改
        results = {}
        validation_errors = []
        
        for prop, new_value in property_changes.items():
            try:
                # 获取原始值
                original_value = self.session.get(f"{obj_name}::{prop}")
                
                # 验证规则
                if prop in validation_rules:
                    rule = validation_rules[prop]
                    
                    # 类型验证
                    if 'type' in rule:
                        expected_type = rule['type']
                        if expected_type == 'number' and not isinstance(new_value, (int, float)):
                            raise ValueError(f"属性 {prop} 需要数值类型")
                        elif expected_type == 'string' and not isinstance(new_value, str):
                            raise ValueError(f"属性 {prop} 需要字符串类型")
                    
                    # 范围验证
                    if 'min' in rule and new_value < rule['min']:
                        raise ValueError(f"属性 {prop} 不能小于 {rule['min']}")
                    if 'max' in rule and new_value > rule['max']:
                        raise ValueError(f"属性 {prop} 不能大于 {rule['max']}")
                    
                    # 选项验证
                    if 'options' in rule and new_value not in rule['options']:
                        raise ValueError(f"属性 {prop} 必须是 {rule['options']} 之一")
                
                # 应用更改
                self.session.set(f"{obj_name}::{prop}", new_value)
                
                # 验证更改
                actual_value = self.session.get(f"{obj_name}::{prop}")
                
                results[prop] = {
                    'original': original_value,
                    'requested': new_value,
                    'actual': actual_value,
                    'success': True
                }
                
                self.log_automation("属性更改成功", {
                    'property': prop,
                    'from': original_value,
                    'to': actual_value
                })
                
            except Exception as e:
                results[prop] = {
                    'success': False,
                    'error': str(e)
                }
                
                validation_errors.append(f"{prop}: {e}")
                
                self.log_automation("属性更改失败", {
                    'property': prop,
                    'error': str(e)
                })
        
        # 打开编辑器查看结果（如果有成功更改）
        if any(r['success'] for r in results.values()):
            self._simulate_editor_open(object_name)
        
        # 返回结果
        final_result = {
            'object': object_name,
            'type': obj_type,
            'changes': results,
            'success': all(r['success'] for r in results.values()),
            'validation_errors': validation_errors
        }
        
        self.log_automation("带验证的编辑完成", final_result)
        
        return final_result
    
    def interactive_parameter_sweep(self, object_name, parameter, values, delay=0.5):
        """交互式参数扫描"""
        
        self.log_automation("开始交互式参数扫描", {
            'object': object_name,
            'parameter': parameter,
            'values': values,
            'delay': delay
        })
        
        # 获取原始值
        try:
            original_value = self.session.get(f"{object_name}::{parameter}")
        except Exception as e:
            self.log_automation("无法获取原始值", {'error': str(e)})
            return {'success': False, 'error': str(e)}
        
        results = []
        
        for i, value in enumerate(values):
            self.log_automation("参数扫描步骤", {
                'step': i + 1,
                'total': len(values),
                'value': value
            })
            
            try:
                # 设置新值
                self.session.set(f"{object_name}::{parameter}", value)
                
                # 获取实际值
                actual_value = self.session.get(f"{object_name}::{parameter}")
                
                # 打开编辑器查看当前状态
                self._simulate_editor_open(object_name)
                
                # 记录结果
                result = {
                    'requested': value,
                    'actual': actual_value,
                    'success': True
                }
                
                results.append(result)
                
                self.log_automation("步骤完成", result)
                
                # 延迟
                time.sleep(delay)
                
            except Exception as e:
                result = {
                    'requested': value,
                    'success': False,
                    'error': str(e)
                }
                
                results.append(result)
                
                self.log_automation("步骤失败", result)
        
        # 恢复原始值
        try:
            self.session.set(f"{object_name}::{parameter}", original_value)
            self.log_automation("恢复原始值", {'value': original_value})
        except:
            pass
        
        # 最终结果
        final_result = {
            'object': object_name,
            'parameter': parameter,
            'original_value': original_value,
            'results': results,
            'success': any(r['success'] for r in results)
        }
        
        self.log_automation("参数扫描完成", final_result)
        
        return final_result
    
    def show_automation_log(self, limit=20):
        """显示自动化日志"""
        
        print("\n自动化操作日志:")
        print("=" * 60)
        
        log_entries = self.automation_log[-limit:] if limit else self.automation_log
        
        for entry in log_entries:
            timestamp = time.strftime("%H:%M:%S", time.localtime(entry['timestamp']))
            print(f"[{timestamp}] {entry['action']}")
            if isinstance(entry['details'], dict):
                for key, value in entry['details'].items():
                    print(f"    {key}: {value}")
            else:
                print(f"    {entry['details']}")
            print()
        
        print(f"总日志条目: {len(self.automation_log)}")
    
    def export_editor_states(self):
        """导出编辑器状态"""
        
        self.log_automation("导出编辑器状态", {})
        
        # 获取所有对象
        try:
            all_objects = self.session.get("objects")
        except:
            all_objects = []
        
        states = {}
        
        for obj_name in all_objects:
            try:
                obj_type = self.session.get(f"{obj_name}::object type")
                
                # 获取常见属性
                properties = {}
                for prop in ['x', 'y', 'z', 'x span', 'y span', 'z span', 'radius', 'material']:
                    try:
                        properties[prop] = self.session.get(f"{obj_name}::{prop}")
                    except:
                        pass
                
                states[obj_name] = {
                    'type': obj_type,
                    'properties': properties
                }
                
            except:
                pass
        
        self.editor_states = states
        
        self.log_automation("编辑器状态导出完成", {
            'objects_exported': len(states)
        })
        
        return states

# 创建编辑器自动化工具
editor_auto = EditorAutomation(fdtd)

# 配置编辑器
print("配置编辑器设置...")
editor_config = editor_auto.configure_editors({
    'auto_apply': True,
    'live_preview': False,
    'timeout': 60
})

# 创建测试对象
print("\n创建测试对象...")

test_objects = []

# 创建多个矩形
for i in range(3):
    rect_name = f"auto_rect_{i}"
    fdtd.addrect()
    fdtd.set("name", rect_name)
    fdtd.set("x", i * 2e-6)
    fdtd.set("y", 0)
    fdtd.set("z", 0)
    fdtd.set("x span", 1e-6)
    fdtd.set("y span", 0.5e-6)
    fdtd.set("z span", 0.2e-6)
    fdtd.set("material", "SiO2 (Glass) - Palik")
    
    test_objects.append(rect_name)

print(f"创建了 {len(test_objects)} 个测试对象")

# 1. 批量编辑演示
print("\n1. 批量编辑演示")
print("-" * 40)

batch_changes = {
    "y span": 0.3e-6,      # 变窄
    "material": "Si (Silicon) - Palik",  # 更改材料
    "color": [1, 0, 0]     # 红色（如果支持）
}

batch_results = editor_auto.batch_edit_objects(test_objects[:2], batch_changes)

print("\n批量编辑结果:")
for obj_name, result in batch_results.items():
    if result.get('success'):
        print(f"  {obj_name}: 成功")
        for prop, change in result.get('changes', {}).items():
            if change.get('success'):
                print(f"    {prop}: {change.get('original')} -> {change.get('new')}")
    else:
        print(f"  {obj_name}: 失败 - {result.get('error', '未知错误')}")

# 2. 带验证的编辑演示
print("\n2. 带验证的编辑演示")
print("-" * 40)

validation_rules = {
    "x span": {
        "type": "number",
        "min": 0.1e-6,
        "max": 10e-6
    },
    "material": {
        "type": "string",
        "options": ["Si (Silicon) - Palik", "SiO2 (Glass) - Palik", "Air"]
    }
}

validated_edit = editor_auto.edit_with_validation(
    test_objects[0],
    {
        "x span": 2e-6,
        "material": "Si (Silicon) - Palik",
        "invalid_prop": "不应该存在的属性"  # 这应该会失败
    },
    validation_rules
)

print("\n带验证的编辑结果:")
print(f"  对象: {validated_edit.get('object')}")
print(f"  成功: {validated_edit.get('success')}")
print(f"  错误: {validated_edit.get('validation_errors', [])}")

# 3. 交互式参数扫描演示
print("\n3. 交互式参数扫描演示")
print("-" * 40)

# 创建扫描对象
scan_obj = "scan_test_object"
fdtd.addrect()
fdtd.set("name", scan_obj)
fdtd.set("x", 0)
fdtd.set("y", 2e-6)
fdtd.set("z", 0)
fdtd.set("x span", 1e-6)
fdtd.set("y span", 0.5e-6)
fdtd.set("material", "Si (Silicon) - Palik")

test_objects.append(scan_obj)

# 扫描参数
scan_values = np.linspace(0.5e-6, 2.0e-6, 5)

scan_results = editor_auto.interactive_parameter_sweep(
    scan_obj,
    "x span",
    scan_values,
    delay=0.3
)

print("\n参数扫描结果:")
print(f"  参数: {scan_results.get('parameter')}")
print(f"  原始值: {scan_results.get('original_value')}")
print(f"  扫描值数: {len(scan_results.get('results', []))}")

successful_scans = sum(1 for r in scan_results.get('results', []) if r.get('success', False))
print(f"  成功扫描: {successful_scans}")

# 4. 导出编辑器状态
print("\n4. 导出编辑器状态")
print("-" * 40)

editor_states = editor_auto.export_editor_states()

print(f"导出了 {len(editor_states)} 个对象的状态")
print("\n对象状态示例:")
for i, (obj_name, state) in enumerate(list(editor_states.items())[:3]):
    print(f"  {i+1}. {obj_name} ({state.get('type')})")
    for prop, value in state.get('properties', {}).items():
        if isinstance(value, (int, float)):
            print(f"     {prop}: {value:.3e}")
        else:
            print(f"     {prop}: {value}")

# 5. 显示自动化日志
print("\n5. 自动化操作日志")
print("-" * 40)

editor_auto.show_automation_log(limit=10)

# 清理测试对象
print("\n清理测试对象...")
for obj in test_objects:
    try:
        fdtd.delete(obj)
    except:
        pass

print(f"清理了 {len(test_objects)} 个测试对象")

# 最终状态
print("\n最终状态检查...")
try:
    remaining_objects = fdtd.get("objects")
    print(f"剩余对象数: {len(remaining_objects)}")
except:
    print("无法获取剩余对象列表")

print("\n编辑器集成和自动化演示完成!")
```

### 示例 4：编辑器调试和故障排除
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("编辑器调试和故障排除演示...")

class EditorDebugger:
    """编辑器调试工具"""
    
    def __init__(self, session):
        self.session = session
        self.debug_log = []
        self.error_count = 0
        
    def debug_edit_command(self, object_name, expected_type=None):
        """调试edit命令"""
        
        print(f"\n调试edit命令: {object_name}")
        print("-" * 40)
        
        debug_info = {
            'object': object_name,
            'timestamp': np.datetime64('now'),
            'steps': []
        }
        
        # 步骤1: 检查对象是否存在
        step1 = {'action': '检查对象存在性'}
        try:
            obj_type = self.session.get(f"{object_name}::object type")
            step1['result'] = f"存在，类型: {obj_type}"
            step1['success'] = True
            
            # 验证类型（如果指定）
            if expected_type and obj_type != expected_type:
                step1['warning'] = f"类型不匹配: 预期 {expected_type}，实际 {obj_type}"
                
        except Exception as e:
            step1['result'] = f"不存在或错误: {e}"
            step1['success'] = False
            step1['error'] = str(e)
        
        debug_info['steps'].append(step1)
        self._log_step(step1)
        
        # 如果对象不存在，停止调试
        if not step1['success']:
            debug_info['overall_success'] = False
            self.debug_log.append(debug_info)
            return debug_info
        
        # 步骤2: 检查对象属性
        step2 = {'action': '检查对象属性'}
        try:
            # 获取常见属性
            properties = {}
            common_props = ['x', 'y', 'z', 'x span', 'y span', 'z span', 'radius', 'material']
            
            for prop in common_props:
                try:
                    value = self.session.get(f"{object_name}::{prop}")
                    properties[prop] = value
                except:
                    pass
            
            step2['result'] = f"找到 {len(properties)} 个属性"
            step2['properties'] = properties
            step2['success'] = True
            
        except Exception as e:
            step2['result'] = f"获取属性失败: {e}"
            step2['success'] = False
            step2['error'] = str(e)
        
        debug_info['steps'].append(step2)
        self._log_step(step2)
        
        # 步骤3: 尝试打开编辑器
        step3 = {'action': '尝试打开编辑器'}
        try:
            # 在实际环境中，这里会调用 self.session.edit(object_name)
            # 但为了调试，我们模拟
            
            # 检查编辑器的可用性
            step3['result'] = "编辑器命令可用"
            
            # 模拟编辑器打开
            print(f"  模拟: 打开 {object_name} 的编辑器")
            
            # 检查编辑器设置
            try:
                # 获取可能的编辑器设置
                editor_settings = {}
                # 这里可以添加获取编辑器设置的代码
                
                step3['editor_settings'] = editor_settings
            except:
                pass
            
            step3['success'] = True
            
        except Exception as e:
            step3['result'] = f"编辑器命令失败: {e}"
            step3['success'] = False
            step3['error'] = str(e)
            self.error_count += 1
        
        debug_info['steps'].append(step3)
        self._log_step(step3)
        
        # 步骤4: 验证编辑能力
        step4 = {'action': '验证编辑能力'}
        if step3['success']:
            try:
                # 测试是否可以修改属性
                test_prop = "material"
                original_value = self.session.get(f"{object_name}::{test_prop}")
                
                # 尝试修改（然后恢复）
                test_value = "Air" if original_value != "Air" else "SiO2 (Glass) - Palik"
                self.session.set(f"{object_name}::{test_prop}", test_value)
                
                # 验证修改
                new_value = self.session.get(f"{object_name}::{test_prop}")
                
                # 恢复原值
                self.session.set(f"{object_name}::{test_prop}", original_value)
                
                step4['result'] = f"编辑测试通过: {test_prop} 可从 {original_value} 修改为 {test_value}"
                step4['success'] = True
                step4['test'] = {
                    'property': test_prop,
                    'original': original_value,
                    'test_value': test_value,
                    'new_value': new_value,
                    'restored': True
                }
                
            except Exception as e:
                step4['result'] = f"编辑测试失败: {e}"
                step4['success'] = False
                step4['error'] = str(e)
                self.error_count += 1
        else:
            step4['result'] = "跳过（编辑器不可用）"
            step4['success'] = False
            step4['skipped'] = True
        
        debug_info['steps'].append(step4)
        self._log_step(step4)
        
        # 总体评估
        successful_steps = sum(1 for step in debug_info['steps'] if step.get('success', False))
        total_steps = len(debug_info['steps'])
        
        debug_info['overall_success'] = successful_steps == total_steps
        debug_info['success_rate'] = successful_steps / total_steps if total_steps > 0 else 0
        
        print(f"调试完成: {successful_steps}/{total_steps} 个步骤成功")
        
        self.debug_log.append(debug_info)
        return debug_info
    
    def _log_step(self, step):
        """记录调试步骤"""
        
        status = "✓" if step.get('success', False) else "✗"
        print(f"  {status} {step['action']}: {step.get('result', '')}")
        
        if 'warning' in step:
            print(f"    警告: {step['warning']}")
        if 'error' in step:
            print(f"    错误: {step['error']}")
    
    def debug_multiple_objects(self, object_names):
        """调试多个对象"""
        
        print(f"\n调试多个对象 ({len(object_names)} 个)")
        print("=" * 60)
        
        results = {}
        
        for obj_name in object_names:
            result = self.debug_edit_command(obj_name)
            results[obj_name] = result
            
            print()  # 空行分隔
        
        # 汇总统计
        total_objects = len(results)
        successful_objects = sum(1 for r in results.values() if r.get('overall_success', False))
        
        print(f"\n调试汇总:")
        print(f"  总对象数: {total_objects}")
        print(f"  完全成功: {successful_objects}")
        print(f"  部分成功: {total_objects - successful_objects}")
        print(f"  总错误数: {self.error_count}")
        
        return results
    
    def analyze_editor_issues(self):
        """分析编辑器问题"""
        
        print("\n编辑器问题分析")
        print("=" * 60)
        
        if not self.debug_log:
            print("无调试数据")
            return
        
        # 收集常见问题
        issues = {
            'object_not_found': 0,
            'property_access_error': 0,
            'editor_command_failed': 0,
            'edit_test_failed': 0
        }
        
        for debug_info in self.debug_log:
            for step in debug_info.get('steps', []):
                if not step.get('success', False):
                    action = step.get('action', '')
                    
                    if '检查对象存在性' in action:
                        issues['object_not_found'] += 1
                    elif '检查对象属性' in action:
                        issues['property_access_error'] += 1
                    elif '尝试打开编辑器' in action:
                        issues['editor_command_failed'] += 1
                    elif '验证编辑能力' in action:
                        issues['edit_test_failed'] += 1
        
        print("问题统计:")
        for issue_type, count in issues.items():
            if count > 0:
                print(f"  {issue_type}: {count}")
        
        # 提供解决方案
        print("\n常见问题解决方案:")
        
        if issues['object_not_found'] > 0:
            print("  1. 对象不存在:")
            print("     - 检查对象名称拼写")
            print("     - 确保对象已被创建")
            print("     - 使用 listobjects() 查看所有对象")
        
        if issues['property_access_error'] > 0:
            print("  2. 属性访问错误:")
            print("     - 检查属性名称是否正确")
            print("     - 某些属性可能对该对象类型无效")
            print("     - 使用 get(object_name + '::*') 查看所有属性")
        
        if issues['editor_command_failed'] > 0:
            print("  3. 编辑器命令失败:")
            print("     - 检查 Lumerical 版本是否支持 edit 命令")
            print("     - 在无头模式中，edit 命令可能不可用")
            print("     - 确保有图形界面支持")
        
        if issues['edit_test_failed'] > 0:
            print("  4. 编辑测试失败:")
            print("     - 检查对象是否被锁定或只读")
            print("     - 验证用户权限")
            print("     - 检查材料数据库是否可用")
    
    def generate_debug_report(self, filename="editor_debug_report.txt"):
        """生成调试报告"""
        
        print(f"\n生成调试报告: {filename}")
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Lumerical 编辑器调试报告\n")
                f.write("=" * 60 + "\n")
                f.write(f"生成时间: {np.datetime64('now')}\n")
                f.write(f"总调试会话: {len(self.debug_log)}\n")
                f.write(f"总错误数: {self.error_count}\n\n")
                
                for i, debug_info in enumerate(self.debug_log):
                    f.write(f"调试会话 {i+1}\n")
                    f.write("-" * 40 + "\n")
                    
                    f.write(f"对象: {debug_info.get('object', '未知')}\n")
                    f.write(f"时间: {debug_info.get('timestamp', '未知')}\n")
                    f.write(f"总体成功: {debug_info.get('overall_success', False)}\n")
                    f.write(f"成功率: {debug_info.get('success_rate', 0)*100:.1f}%\n\n")
                    
                    for j, step in enumerate(debug_info.get('steps', [])):
                        f.write(f"步骤 {j+1}: {step.get('action', '未知')}\n")
                        f.write(f"  结果: {step.get('result', '无')}\n")
                        f.write(f"  成功: {step.get('success', False)}\n")
                        
                        if 'error' in step:
                            f.write(f"  错误: {step.get('error')}\n")
                        if 'warning' in step:
                            f.write(f"  警告: {step.get('warning')}\n")
                        
                        f.write("\n")
                    
                    f.write("\n")
                
                f.write("报告结束\n")
            
            print(f"报告已保存到 {filename}")
            return True
            
        except Exception as e:
            print(f"生成报告失败: {e}")
            return False

# 创建编辑器调试器
debugger = EditorDebugger(fdtd)

# 创建测试对象
print("创建测试对象...")

test_objects = []

# 正常对象
fdtd.addrect()
fdtd.set("name", "normal_rect")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("x span", 1e-6)
fdtd.set("material", "SiO2 (Glass) - Palik")
test_objects.append("normal_rect")

# 另一个正常对象
fdtd.addcylinder()
fdtd.set("name", "normal_cylinder")
fdtd.set("x", 2e-6)
fdtd.set("radius", 0.3e-6)
fdtd.set("material", "Si (Silicon) - Palik")
test_objects.append("normal_cylinder")

# 不存在的对象（用于测试错误）
test_objects.append("non_existent_object")

print(f"准备调试 {len(test_objects)} 个对象")

# 1. 调试单个对象
print("\n1. 调试单个正常对象")
debug_result1 = debugger.debug_edit_command("normal_rect", expected_type="rectangle")

# 2. 调试多个对象
print("\n2. 调试多个对象")
debug_results = debugger.debug_multiple_objects(test_objects)

# 3. 分析问题
print("\n3. 分析编辑器问题")
debugger.analyze_editor_issues()

# 4. 生成调试报告
print("\n4. 生成调试报告")
debugger.generate_debug_report()

# 5. 特殊情况测试
print("\n5. 特殊情况测试")

# 测试空名称
print("\n测试空对象名称...")
try:
    fdtd.edit("")
    print("  空名称测试: 可能失败或选择当前对象")
except Exception as e:
    print(f"  空名称测试失败: {e}")

# 测试特殊字符
print("\n测试特殊字符对象名称...")
special_name = "test@object#123"
try:
    fdtd.addrect()
    fdtd.set("name", special_name)
    print(f"  创建特殊名称对象: {special_name}")
    
    # 尝试编辑
    fdtd.edit(special_name)
    print(f"  编辑特殊名称对象: 可能成功")
    
    # 清理
    fdtd.delete(special_name)
except Exception as e:
    print(f"  特殊名称测试失败: {e}")

# 清理正常对象
print("\n清理测试对象...")
for obj in ["normal_rect", "normal_cylinder"]:
    try:
        fdtd.delete(obj)
        print(f"  删除对象: {obj}")
    except:
        print(f"  无法删除对象: {obj}")

print("\n编辑器调试和故障排除演示完成!")
```

### 示例 5：编辑命令最佳实践和高级技巧
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("编辑命令最佳实践和高级技巧演示...")

class EditBestPractices:
    """编辑命令最佳实践"""
    
    def __init__(self, session):
        self.session = session
        self.practice_examples = []
    
    def demonstrate_best_practices(self):
        """演示最佳实践"""
        
        print("Lumerical edit 命令最佳实践")
        print("=" * 70)
        
        practices = [
            self.practice1_select_before_edit,
            self.practice2_use_specific_properties,
            self.practice3_error_handling,
            self.practice4_batch_operations,
            self.practice5_user_feedback,
            self.practice6_performance_considerations,
            self.practice7_compatibility,
            self.practice8_alternative_approaches
        ]
        
        for i, practice_func in enumerate(practices):
            print(f"\n{i+1}. ", end="")
            practice_func()
    
    def practice1_select_before_edit(self):
        """实践1: 编辑前先选中对象"""
        
        print("编辑前先选中对象")
        print("-" * 40)
        
        # 创建测试对象
        obj_name = "practice1_object"
        self.session.addrect()
        self.session.set("name", obj_name)
        
        print("正确做法:")
        print("  1. 先选中对象")
        self.session.select(obj_name)
        print("  2. 再调用edit()（无参数）")
        
        try:
            self.session.edit()
            print("  结果: 编辑当前选中对象")
        except:
            print("  结果: edit() 可能不可用")
        
        print("\n错误做法:")
        print("  直接调用 edit('object_name') 而不先选中")
        print("  虽然可能工作，但先选中更符合工作流程")
        
        # 清理
        self.session.delete(obj_name)
        
        self.practice_examples.append("先选中后编辑")
    
    def practice2_use_specific_properties(self):
        """实践2: 使用特定属性编辑"""
        
        print("使用特定属性编辑而非通用编辑")
        print("-" * 40)
        
        # 创建测试对象
        obj_name = "practice2_object"
        self.session.addrect()
        self.session.set("name", obj_name)
        self.session.set("material", "SiO2 (Glass) - Palik")
        
        print("场景: 只需要修改材料")
        print("\n方法1: 打开完整编辑器")
        print("  edit('practice2_object')")
        print("  问题: 打开所有属性，用户可能困惑")
        
        print("\n方法2: 直接设置属性")
        print("  set('practice2_object::material', 'Si (Silicon) - Palik')")
        print("  优点: 快速，无需用户交互")
        
        print("\n方法3: 打开特定属性编辑器")
        print("  edit('practice2_object', 'material')")
        print("  优点: 只显示相关属性，用户体验更好")
        
        print("\n建议: 根据场景选择:")
        print("  - 需要用户选择: 使用方法3")
        print("  - 程序化设置: 使用方法2")
        print("  - 需要全面编辑: 使用方法1")
        
        # 清理
        self.session.delete(obj_name)
        
        self.practice_examples.append("特定属性编辑")
    
    def practice3_error_handling(self):
        """实践3: 错误处理"""
        
        print("健壮的错误处理")
        print("-" * 40)
        
        print("编辑操作可能失败的场景:")
        print("  1. 对象不存在")
        print("  2. 属性不存在")
        print("  3. 权限不足")
        print("  4. 编辑器不可用")
        
        print("\n错误处理示例:")
        
        def safe_edit(object_name, property_name=None):
            """安全的编辑函数"""
            
            try:
                # 检查对象是否存在
                try:
                    obj_type = self.session.get(f"{object_name}::object type")
                    print(f"  对象存在: {object_name} ({obj_type})")
                except:
                    print(f"  错误: 对象 {object_name} 不存在")
                    return False
                
                # 尝试编辑
                if property_name:
                    print(f"  尝试编辑属性: {property_name}")
                    # 在实际应用中: self.session.edit(object_name, property_name)
                else:
                    print(f"  尝试编辑对象")
                    # 在实际应用中: self.session.edit(object_name)
                
                # 模拟成功
                print("  编辑操作成功")
                return True
                
            except Exception as e:
                print(f"  编辑失败: {e}")
                return False
        
        # 测试
        print("\n测试1: 编辑存在的对象")
        safe_edit("non_existent", "material")
        
        print("\n测试2: 编辑不存在的属性")
        # 创建测试对象
        obj_name = "practice3_object"
        self.session.addrect()
        self.session.set("name", obj_name)
        
        safe_edit(obj_name, "non_existent_property")
        
        # 清理
        self.session.delete(obj_name)
        
        print("\n建议: 总是包装edit调用在try-except中")
        
        self.practice_examples.append("错误处理")
    
    def practice4_batch_operations(self):
        """实践4: 批量操作"""
        
        print("批量编辑操作优化")
        print("-" * 40)
        
        print("场景: 需要编辑多个对象的相同属性")
        
        # 创建多个对象
        object_names = []
        for i in range(3):
            obj_name = f"batch_obj_{i}"
            self.session.addrect()
            self.session.set("name", obj_name)
            self.session.set("x", i * 2e-6)
            self.session.set("material", "SiO2 (Glass) - Palik")
            object_names.append(obj_name)
        
        print(f"创建了 {len(object_names)} 个测试对象")
        
        print("\n方法1: 逐个编辑（低效）")
        print("  for obj in objects:")
        print("    edit(obj)")
        print("    # 用户需要为每个对象操作")
        print("  问题: 用户体验差，效率低")
        
        print("\n方法2: 批量设置属性（高效）")
        print("  for obj in objects:")
        print("    set(obj + '::material', '新材料')")
        print("  然后让用户整体查看:")
        print("  edit(objects[0])  # 查看示例")
        print("  优点: 快速，减少用户交互")
        
        print("\n方法3: 创建对象组")
        print("  将相关对象分组，编辑组属性")
        print("  适用于关联对象")
        
        # 演示批量设置
        print("\n演示批量设置:")
        new_material = "Si (Silicon) - Palik"
        for obj in object_names:
            self.session.set(f"{obj}::material", new_material)
            print(f"  设置 {obj} 材料为 {new_material}")
        
        # 清理
        for obj in object_names:
            self.session.delete(obj)
        
        self.practice_examples.append("批量操作")
    
    def practice5_user_feedback(self):
        """实践5: 用户反馈"""
        
        print("提供用户反馈")
        print("-" * 40)
        
        print("编辑操作应提供清晰的反馈:")
        
        print("\n1. 编辑前提示")
        print("  echo('即将编辑对象: ' + object_name)")
        print("  echo('当前属性: ' + str(current_value))")
        
        print("\n2. 编辑后确认")
        print("  echo('编辑完成')")
        print("  echo('新属性: ' + str(new_value))")
        
        print("\n3. 进度指示")
        print("  对于批量编辑，显示进度")
        
        print("\n4. 错误信息")
        print("  友好的错误提示，而非技术异常")
        
        # 示例
        print("\n示例实现:")
        
        def user_friendly_edit(session, object_name, property_name=None):
            """用户友好的编辑函数"""
            
            print(f"\n[编辑开始]")
            
            # 检查对象
            try:
                obj_type = session.get(f"{object_name}::object type")
                print(f"  对象: {object_name} ({obj_type})")
            except:
                print(f"  错误: 对象 {object_name} 不存在")
                return False
            
            # 获取当前值（如果指定属性）
            if property_name:
                try:
                    current_value = session.get(f"{object_name}::{property_name}")
                    print(f"  当前 {property_name}: {current_value}")
                except:
                    print(f"  警告: 无法获取 {property_name} 的当前值")
            
            # 模拟编辑
            print(f"  打开编辑器...")
            # session.edit(object_name, property_name)
            
            # 模拟用户操作
            print(f"  等待用户操作...")
            
            # 获取新值
            if property_name:
                try:
                    new_value = session.get(f"{object_name}::{property_name}")
                    print(f"  新 {property_name}: {new_value}")
                except:
                    print(f"  无法获取新值")
            
            print(f"[编辑完成]")
            return True
        
        # 创建测试对象
        obj_name = "feedback_object"
        self.session.addrect()
        self.session.set("name", obj_name)
        
        # 演示
        user_friendly_edit(self.session, obj_name, "material")
        
        # 清理
        self.session.delete(obj_name)
        
        self.practice_examples.append("用户反馈")
    
    def practice6_performance_considerations(self):
        """实践6: 性能考虑"""
        
        print("编辑命令的性能影响")
        print("-" * 40)
        
        print("性能考虑:")
        print("  1. 编辑器打开需要GUI交互，可能阻塞脚本")
        print("  2. 频繁打开编辑器影响用户体验")
        print("  3. 复杂对象编辑器可能响应慢")
        
        print("\n优化建议:")
        print("  1. 避免在循环中调用edit()")
        print("  2. 对于批量操作，先收集所有更改，最后统一编辑")
        print("  3. 考虑使用非模态编辑器（如果支持）")
        print("  4. 对于复杂对象，允许用户跳过详细编辑")
        
        print("\n示例: 优化编辑流程")
        
        # 创建复杂对象
        complex_obj = "complex_structure"
        self.session.addrect()
        self.session.set("name", complex_obj)
        
        # 添加多个属性
        properties_to_set = {
            "x span": 5e-6,
            "y span": 0.5e-6,
            "z span": 0.22e-6,
            "material": "Si (Silicon) - Palik",
            "x": 0,
            "y": 0,
            "z": 0
        }
        
        print("\n优化前（多次编辑）:")
        print("  for prop, value in properties:")
        print("    set(object + '::' + prop, value)")
        print("    edit(object, prop)  # 每次编辑都打开编辑器")
        print("  问题: 编辑器频繁打开，用户体验差")
        
        print("\n优化后（批量设置，单次编辑）:")
        print("  # 批量设置所有属性")
        print("  for prop, value in properties:")
        print("    set(object + '::' + prop, value)")
        print("  # 最后打开一次编辑器供用户确认")
        print("  edit(object)")
        print("  优点: 快速，用户体验好")
        
        # 演示批量设置
        print("\n演示批量设置:")
        for prop, value in properties_to_set.items():
            self.session.set(f"{complex_obj}::{prop}", value)
            print(f"  设置 {prop} = {value}")
        
        print("  最后打开编辑器供用户确认...")
        
        # 清理
        self.session.delete(complex_obj)
        
        self.practice_examples.append("性能优化")
    
    def practice7_compatibility(self):
        """实践7: 兼容性考虑"""
        
        print("编辑命令的兼容性")
        print("-" * 40)
        
        print("兼容性问题:")
        print("  1. Lumerical 版本差异")
        print("  2. 操作系统差异")
        print("  3. 图形界面可用性")
        print("  4. 脚本与GUI模式")
        
        print("\n检测兼容性示例:")
        
        def check_edit_compatibility(session):
            """检查edit命令兼容性"""
            
            compatibility_info = {
                'edit_available': False,
                'gui_mode': False,
                'version': '未知',
                'recommendation': ''
            }
            
            print("兼容性检查:")
            
            # 检查是否在GUI模式（简化检查）
            try:
                # 尝试获取界面相关属性
                gui_related = session.get("?")  # 简化表示
                compatibility_info['gui_mode'] = True
                print("  GUI模式: 是")
            except:
                compatibility_info['gui_mode'] = False
                print("  GUI模式: 否（可能是无头模式）")
            
            # 测试edit命令
            try:
                # 创建测试对象
                test_obj = "compat_test"
                session.addrect()
                session.set("name", test_obj)
                
                # 尝试edit（可能会失败但不抛出异常，取决于环境）
                # 这里简化测试
                edit_works = True  # 假设工作
                
                if edit_works:
                    compatibility_info['edit_available'] = True
                    print("  edit命令: 可用")
                else:
                    compatibility_info['edit_available'] = False
                    print("  edit命令: 不可用")
                
                # 清理
                session.delete(test_obj)
                
            except Exception as e:
                compatibility_info['edit_available'] = False
                print(f"  edit命令测试失败: {e}")
            
            # 提供建议
            if not compatibility_info['gui_mode']:
                compatibility_info['recommendation'] = "无头模式下edit命令可能受限，考虑使用set命令直接设置属性"
            elif not compatibility_info['edit_available']:
                compatibility_info['recommendation'] = "edit命令不可用，检查Lumerical版本和权限"
            else:
                compatibility_info['recommendation'] = "edit命令可用，可以正常使用"
            
            print(f"  建议: {compatibility_info['recommendation']}")
            
            return compatibility_info
        
        # 执行兼容性检查
        compatibility = check_edit_compatibility(self.session)
        
        print("\n兼容性策略:")
        print("  1. 检测环境，动态选择方法")
        print("  2. 提供回退方案（如使用set命令）")
        print("  3. 记录兼容性信息供调试")
        
        self.practice_examples.append("兼容性处理")
    
    def practice8_alternative_approaches(self):
        """实践8: 替代方法"""
        
        print("edit命令的替代方法")
        print("-" * 40)
        
        print("当edit命令不可用或不合适时:")
        
        print("\n替代方法1: 直接设置属性")
        print("  使用set()命令:")
        print("    set('object::property', value)")
        print("  优点: 快速，可脚本化")
        print("  缺点: 无用户交互")
        
        print("\n替代方法2: 使用GUI命令组合")
        print("  组合使用:")
        print("    select('object')  # 选中对象")
        print("    # 其他GUI命令...")
        print("  优点: 更灵活")
        print("  缺点: 复杂")
        
        print("\n替代方法3: 创建自定义编辑器")
        print("  使用脚本创建简单的属性编辑器:")
        print("    - 显示当前值")
        print("    - 提供输入框")
        print("    - 验证输入")
        print("    - 应用更改")
        print("  优点: 完全控制")
        print("  缺点: 开发工作量大")
        
        print("\n替代方法4: 使用Lumerical的GUI自动化")
        print("  通过自动化工具控制GUI:")
        print("    - 模拟点击")
        print("    - 填写表单")
        print("    - 读取值")
        print("  优点: 利用现有GUI")
        print("  缺点: 脆弱，依赖GUI布局")
        
        # 示例: 简单的自定义编辑器
        print("\n简单自定义编辑器示例:")
        
        def simple_material_editor(session, object_name):
            """简单的材料编辑器"""
            
            print(f"\n自定义材料编辑器 - 对象: {object_name}")
            print("-" * 40)
            
            # 获取当前材料
            try:
                current_material = session.get(f"{object_name}::material")
                print(f"当前材料: {current_material}")
            except:
                print("无法获取当前材料")
                return
            
            # 可用材料列表
            available_materials = [
                "Si (Silicon) - Palik",
                "SiO2 (Glass) - Palik",
                "Si3N4 (Silicon Nitride) - Phillip",
                "Air"
            ]
            
            print("\n可用材料:")
            for i, material in enumerate(available_materials):
                print(f"  {i+1}. {material}")
            
            # 模拟用户选择（实际中可能通过GUI）
            selected_index = 1  # 假设选择第一个
            new_material = available_materials[selected_index]
            
            print(f"\n选择: {selected_index+1} ({new_material})")
            
            # 应用更改
            try:
                session.set(f"{object_name}::material", new_material)
                print(f"材料已更改为: {new_material}")
            except Exception as e:
                print(f"更改失败: {e}")
        
        # 创建测试对象
        obj_name = "alternative_object"
        self.session.addrect()
        self.session.set("name", obj_name)
        
        # 演示自定义编辑器
        simple_material_editor(self.session, obj_name)
        
        # 清理
        self.session.delete(obj_name)
        
        print("\n总结: 根据需求选择合适的方法")
        
        self.practice_examples.append("替代方法")
    
    def summary(self):
        """总结"""
        
        print("\n" + "=" * 70)
        print("编辑命令最佳实践总结")
        print("=" * 70)
        
        print(f"演示了 {len(self.practice_examples)} 个最佳实践:")
        for i, practice in enumerate(self.practice_examples):
            print(f"  {i+1}. {practice}")
        
        print("\n关键要点:")
        print("  1. edit命令适合需要用户交互的场景")
        print("  2. 对于自动化脚本，优先使用set命令")
        print("  3. 始终考虑错误处理和兼容性")
        print("  4. 提供良好的用户反馈")
        print("  5. 根据环境选择合适的方法")
        
        print("\n记住: 没有一种方法适用于所有场景")
        print("根据具体需求和环境选择最佳方法")

# 创建最佳实践演示
best_practices = EditBestPractices(fdtd)

# 演示所有最佳实践
best_practices.demonstrate_best_practices()

# 总结
best_practices.summary()

print("\n编辑命令最佳实践和高级技巧演示完成!")
```

## 注意事项

1. **环境依赖性**：`edit` 命令高度依赖图形用户界面（GUI）。在无头模式（headless mode）或远程服务器上可能不可用或行为不同。

2. **模态对话框**：默认情况下，`edit` 命令打开模态对话框，会阻塞脚本执行直到用户关闭对话框。这可能是期望的行为，也可能不是，取决于应用场景。

3. **用户交互**：`edit` 命令需要用户交互。在完全自动化的脚本中，考虑使用 `set` 命令直接设置属性。

4. **性能影响**：频繁打开编辑器可能影响性能，特别是对于复杂对象。在循环中避免调用 `edit`。

5. **兼容性**：不同 Lumerical 版本的 `edit` 命令可能有细微差别。测试脚本在目标版本上的行为。

6. **错误处理**：`edit` 命令可能因各种原因失败（对象不存在、权限问题等）。实现适当的错误处理。

7. **替代方案**：对于不需要用户交互的场景，考虑使用 `set`、`setnamed` 或其他属性设置命令。

8. **批量编辑**：Lumerical 通常不支持同时编辑多个不同对象。对于批量操作，考虑脚本化解决方案。

9. **属性验证**：编辑器通常提供属性验证。如果使用脚本设置属性，确保实现自己的验证逻辑。

10. **用户体验**：对于交互式工具，`edit` 命令可以提供良好的用户体验。对于高级用户，考虑提供直接属性设置的选项。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有对象编辑器 |
| MODE Solutions | ✅ 完全支持 | 所有对象编辑器 |
| DEVICE | ✅ 完全支持 | 所有对象编辑器 |
| INTERCONNECT | ⚠️ 有限支持 | 主要用于原理图元件编辑 |

## 相关命令

- `set` - 设置对象属性（无GUI）
- `get` - 获取对象属性
- `select` - 选择对象（通常与 `edit` 配合使用）
- `addobject` - 添加新对象
- `delete` - 删除对象
- `copy` - 复制对象
- `move` - 移动对象
- `rotate` - 旋转对象
- `scale` - 缩放对象
- `group` - 对象编组（可编辑组）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2024-01-01 | 初始版本，包含基本语法和示例 |
| 1.1 | 2025-12-01 | 添加详细配置属性表格和Python API示例 |
| 1.2 | 2026-01-31 | 完善错误处理章节，补充LSF脚本示例，添加版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - Edit Command
2. Lumerical Python API Documentation - session.edit() Method
3. Lumerical Knowledge Base: "Interactive Object Editing in Scripts"
4. Lumerical User Guide: "Using the Object Editor"

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*