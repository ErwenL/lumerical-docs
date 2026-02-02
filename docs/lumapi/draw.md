# `draw` - 绘制对象

## 概述

`draw` 命令用于在 Lumerical 的 CAD 视图（三维可视化窗口）中绘制或更新对象的几何显示。该命令强制刷新选定对象或所有对象的图形表示，确保可视化与当前几何参数同步。

主要功能：
- **对象重绘**：更新单个或多个对象的可视化表示
- **视图刷新**：强制刷新 CAD 视图以显示最新几何状态
- **可视化更新**：在脚本修改对象属性后立即更新显示
- **性能控制**：管理大型仿真中的可视化性能
- **显示优化**：控制何时更新复杂几何的显示

典型应用：
- 脚本中修改几何参数后立即查看效果
- 动画或参数扫描中的实时可视化
- 大型结构的分步构建和可视化
- 调试几何创建脚本
- 优化仿真设置时的交互式可视化

## 语法

### LSF 语法
```lumerical
draw;                    # 重绘所有对象
draw("object_name");     # 重绘指定对象
draw("all");             # 重绘所有对象（显式）
draw("group_name");      # 重绘图组
```

### Python API
```python
session.draw()                    # 重绘所有对象
session.draw("object_name")       # 重绘指定对象
session.draw("all")               # 重绘所有对象（显式）
session.draw("group_name")        # 重绘图组
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `object_name` | string | 要重绘的特定对象名称。如果省略或为 `"all"`，则重绘所有对象。 | 否 |

## 配置属性

`draw` 命令本身没有可配置属性，但绘图行为受以下相关设置影响：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `redraw automatically` | bool | true | 是否自动重绘（修改对象时）。 |
| `visualization update` | string | "immediate" | 可视化更新模式："immediate"（立即）、"deferred"（延迟）、"manual"（手动）。 |
| `graphics detail` | string | "normal" | 图形细节级别："low"（低）、"normal"（正常）、"high"（高）、"maximum"（最高）。 |
| `transparency` | bool | false | 是否启用透明渲染。 |
| `shadows` | bool | true | 是否显示阴影。 |
| `antialiasing` | bool | true | 是否启用抗锯齿。 |
| `view refresh rate` | number | 30 | 视图刷新率（Hz）。 |
| `maximum draw time` | number | 5.0 | 最大绘制时间（秒），超时则中止。 |

## 返回值

`draw` 命令没有返回值。它主要用于在 CAD 视图中更新对象的可视化表示，不返回任何数据。在 Python API 中，`session.draw()` 返回 `None`。

## 错误处理

### 常见错误

1. **对象不存在错误**
   ```python
   # 错误：尝试绘制不存在的对象
   fdtd.draw("nonexistent_object")
   ```
   解决方案：在绘制前检查对象是否存在。

2. **绘制超时错误**
   ```python
   # 错误：绘制操作超时
   fdtd.draw("complex_object")  # 可能因对象过于复杂而超时
   ```
   解决方案：增加最大绘制时间限制或简化对象。

3. **内存不足错误**
   ```python
   # 错误：内存不足导致绘制失败
   fdtd.draw("all")  # 大型结构可能耗尽内存
   ```
   解决方案：分批绘制或减少图形细节。

### Python 错误处理示例
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 正常绘制
    fdtd.draw("all")
    
    # 尝试绘制不存在的对象
    fdtd.draw("nonexistent_object")
    
except lumapi.LumApiError as e:
    error_str = str(e).lower()
    
    if "object" in error_str and "not found" in error_str:
        print("错误: 对象不存在")
    elif "timeout" in error_str or "time out" in error_str:
        print("错误: 绘制超时")
    elif "memory" in error_str or "out of memory" in error_str:
        print("错误: 内存不足")
    else:
        print(f"Lumerical API 错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 使用示例

### 示例 1：基本绘图操作

#### LSF 脚本
```lumerical
# 基本绘图操作演示
?echo("基本绘图操作演示...");

# 1. 创建几个基本几何对象
?echo("创建几何对象...");

# 添加矩形
addrect;
set("name", "rectangle1");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 1e-6);
set("y span", 0.5e-6);
set("z span", 0.2e-6);
set("material", "SiO2 (Glass) - Palik");

# 添加圆柱体
addcylinder;
set("name", "cylinder1");
set("x", 1e-6);
set("y", 0);
set("z", 0);
set("radius", 0.3e-6);
set("z span", 0.5e-6);
set("material", "Si (Silicon) - Palik");

# 添加球体
addsphere;
set("name", "sphere1");
set("x", -1e-6);
set("y", 0);
set("z", 0);
set("radius", 0.4e-6);
set("material", "Au (Gold) - Johnson and Christy");

# 初始绘制所有对象
?echo("初始绘制所有对象...");
draw("all");
?echo("所有对象已绘制");

# 2. 修改对象属性后重绘
?echo("修改矩形属性后重绘...");
select("rectangle1");
set("x span", 2e-6);  # 扩大宽度
set("material", "Si3N4 (Silicon Nitride) - Phillip");  # 更改材料
draw("rectangle1");  # 只重绘矩形
?echo("矩形已更新");

# 3. 批量修改后批量重绘
?echo("批量修改多个对象...");
select("cylinder1");
set("radius", 0.5e-6);  # 增加半径
set("z", 0.1e-6);  # 调整位置

select("sphere1");
set("x", -1.5e-6);  # 移动位置
set("material", "Ag (Silver) - Johnson and Christy");  # 更改材料

# 批量重绘所有对象
draw("all");
?echo("所有对象已更新");

# 4. 检查对象列表
?echo("当前对象列表:");
objects = get("objects");
for (i=1:length(objects)) {
    name = objects{i};
    obj_type = get(name + "::object type");
    ?echo("  " + num2str(i) + ". " + name + " (" + obj_type + ")");
}

# 5. 选择性重绘
?echo("选择性重绘测试...");
# 只重绘圆柱体和球体
draw("cylinder1");
draw("sphere1");
?echo("圆柱体和球体已重绘");

# 6. 延迟绘制模式演示
?echo("延迟绘制模式演示...");
# 关闭自动重绘
set("redraw automatically", false);
?echo("自动重绘已关闭");

# 进行一系列修改（不会立即显示）
select("rectangle1");
set("y span", 1e-6);
set("z span", 0.3e-6);

select("cylinder1");
set("material", "Cu (Copper) - Johnson and Christy");

?echo("已修改多个属性（未显示）");

# 手动触发重绘
draw("all");
?echo("手动重绘完成，所有更改现在可见");

# 恢复自动重绘
set("redraw automatically", true);
?echo("自动重绘已恢复");

?echo("基本绘图操作完成!");
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本绘图操作演示...")

# 1. 创建几个基本几何对象
print("创建几何对象...")

# 添加矩形
fdtd.addrect()
fdtd.set("name", "rectangle1")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 1e-6)
fdtd.set("y span", 0.5e-6)
fdtd.set("z span", 0.2e-6)
fdtd.set("material", "SiO2 (Glass) - Palik")

# 添加圆柱体
fdtd.addcylinder()
fdtd.set("name", "cylinder1")
fdtd.set("x", 1e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("radius", 0.3e-6)
fdtd.set("z span", 0.5e-6)
fdtd.set("material", "Si (Silicon) - Palik")

# 添加球体
fdtd.addsphere()
fdtd.set("name", "sphere1")
fdtd.set("x", -1e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("radius", 0.4e-6)
fdtd.set("material", "Au (Gold) - Johnson and Christy")

# 初始绘制所有对象
print("初始绘制所有对象...")
fdtd.draw("all")
print("所有对象已绘制")

# 2. 修改对象属性后重绘
print("\n修改矩形属性后重绘...")
fdtd.select("rectangle1")
fdtd.set("x span", 2e-6)  # 扩大宽度
fdtd.set("material", "Si3N4 (Silicon Nitride) - Phillip")  # 更改材料
fdtd.draw("rectangle1")  # 只重绘矩形
print("矩形已更新")

# 3. 批量修改后批量重绘
print("\n批量修改多个对象...")
fdtd.select("cylinder1")
fdtd.set("radius", 0.5e-6)  # 增加半径
fdtd.set("z", 0.1e-6)  # 调整位置

fdtd.select("sphere1")
fdtd.set("x", -1.5e-6)  # 移动位置
fdtd.set("material", "Ag (Silver) - Johnson and Christy")  # 更改材料

# 批量重绘所有对象
fdtd.draw("all")
print("所有对象已更新")

# 4. 检查对象列表
print("\n当前对象列表:")
obj_names = fdtd.get("objects")
for i, name in enumerate(obj_names):
    obj_type = fdtd.get(name + "::object type")
    print(f"  {i+1}. {name} ({obj_type})")

# 5. 选择性重绘
print("\n选择性重绘测试...")
# 只重绘圆柱体和球体
fdtd.draw("cylinder1")
fdtd.draw("sphere1")
print("圆柱体和球体已重绘")

# 6. 延迟绘制模式演示
print("\n延迟绘制模式演示...")
# 关闭自动重绘
fdtd.set("redraw automatically", False)
print("自动重绘已关闭")

# 进行一系列修改（不会立即显示）
fdtd.select("rectangle1")
fdtd.set("y span", 1e-6)
fdtd.set("z span", 0.3e-6)

fdtd.select("cylinder1")
fdtd.set("material", "Cu (Copper) - Johnson and Christy")

print("已修改多个属性（未显示）")

# 手动触发重绘
fdtd.draw("all")
print("手动重绘完成，所有更改现在可见")

# 恢复自动重绘
fdtd.set("redraw automatically", True)
print("自动重绘已恢复")

print("\n基本绘图操作完成!")
```

### 示例 2：复杂结构构建和可视化

#### LSF 脚本
```lumerical
# 复杂结构构建和可视化演示
?echo("复杂结构构建和可视化演示...");

# 创建光子晶体结构示例
?echo("创建光子晶体结构...");

# 设置优化绘制参数
set("visualization update", "deferred");  # 延迟更新
set("graphics detail", "normal");         # 正常细节

# 临时关闭自动重绘以提高性能
auto_redraw = get("redraw automatically");
set("redraw automatically", false);

# 创建光子晶体孔阵列
lattice_constant = 0.4e-6;  # 400 nm
radius = 0.12e-6;           # 120 nm
num_periods = 3;

hole_count = 0;
for (i = -num_periods; i <= num_periods; i = i + 1) {
    for (j = -num_periods; j <= num_periods; j = j + 1) {
        # 跳过中心位置
        if (i == 0 && j == 0) {
            continue;
        }
        
        x_pos = i * lattice_constant;
        y_pos = j * lattice_constant;
        
        # 添加圆柱形空气孔
        addcylinder;
        hole_name = "PC_hole_" + num2str(hole_count);
        set("name", hole_name);
        set("x", x_pos);
        set("y", y_pos);
        set("z", 0);
        set("radius", radius);
        set("z span", 0.5e-6);
        set("material", "Air");
        
        hole_count = hole_count + 1;
    }
}

# 创建硅平板背景
addrect;
set("name", "PC_slab");
set("x", 0);
set("y", 0);
set("z", 0);
span = (2 * num_periods + 1) * lattice_constant;
set("x span", span);
set("y span", span);
set("z span", 0.22e-6);  # 220 nm 硅板
set("material", "Si (Silicon) - Palik");
set("draw order", -1);   # 负值表示先绘制

# 恢复自动重绘设置
set("redraw automatically", auto_redraw);

# 手动绘制新创建的结构
draw("all");

?echo("创建了 " + num2str(hole_count) + " 个空气孔和 1 个硅板");
?echo("光子晶体结构构建完成");

# 创建波导结构
?echo("\n创建波导结构...");
addrect;
set("name", "waveguide");
set("x", 0);
set("y", 3e-6);
set("z", 0);
set("x span", 10e-6);
set("y span", 0.5e-6);
set("z span", 0.22e-6);
set("material", "Si (Silicon) - Palik");

# 立即绘制波导
draw("waveguide");
?echo("波导创建完成");

# 参数扫描动画示例
?echo("\n参数扫描动画示例: 调整波导宽度");
widths = [0.2e-6, 0.3e-6, 0.4e-6, 0.5e-6, 0.6e-6, 0.7e-6, 0.8e-6, 0.9e-6, 1.0e-6];
for (idx = 1; idx <= length(widths); idx = idx + 1) {
    width = widths{idx};
    ?echo("  宽度: " + num2str(width*1e9) + " nm");
    select("waveguide");
    set("y span", width);
    draw("waveguide");
    sleep(0.3);  # 延迟以便观察
}

# 优化视图设置
?echo("\n优化视图设置...");
set("graphics detail", "high");
set("transparency", true);
set("shadows", true);
set("antialiasing", true);
set("view refresh rate", 60);

# 最终重绘
draw("all");
?echo("复杂结构构建和可视化演示完成!");
```

#### Python API
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("复杂结构构建和可视化演示...")

class StructureBuilder:
    """结构构建工具"""
    
    def __init__(self, session):
        self.session = session
        self.objects_created = []
        
        # 优化绘制设置
        self.session.set("visualization update", "deferred")  # 延迟更新
        self.session.set("graphics detail", "normal")  # 正常细节
    
    def create_photonic_crystal(self, name, lattice_constant, radius, num_periods, material):
        """创建光子晶体结构"""
        
        print(f"创建光子晶体: {name}")
        print(f"  晶格常数: {lattice_constant*1e9:.1f} nm")
        print(f"  孔半径: {radius*1e9:.1f} nm")
        print(f"  周期数: {num_periods}×{num_periods}")
        print(f"  材料: {material}")
        
        # 临时关闭自动重绘以提高性能
        auto_redraw = self.session.get("redraw automatically")
        self.session.set("redraw automatically", False)
        
        # 创建空气孔阵列
        hole_count = 0
        for i in range(-num_periods, num_periods + 1):
            for j in range(-num_periods, num_periods + 1):
                x_pos = i * lattice_constant
                y_pos = j * lattice_constant
                
                # 跳过中心位置（可能需要）
                if i == 0 and j == 0:
                    continue
                
                # 添加圆柱形空气孔
                self.session.addcylinder()
                hole_name = f"{name}_hole_{hole_count}"
                self.session.set("name", hole_name)
                self.session.set("x", x_pos)
                self.session.set("y", y_pos)
                self.session.set("z", 0)
                self.session.set("radius", radius)
                self.session.set("z span", 0.5e-6)  # 厚度
                self.session.set("material", "Air")  # 空气孔
                
                self.objects_created.append(hole_name)
                hole_count += 1
        
        # 创建背景板（硅）
        self.session.addrect()
        slab_name = f"{name}_slab"
        self.session.set("name", slab_name)
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", 0)
        span = (2 * num_periods + 1) * lattice_constant
        self.session.set("x span", span)
        self.session.set("y span", span)
        self.session.set("z span", 0.22e-6)  # 220nm 硅板
        self.session.set("material", material)
        
        # 设置优先级：板在孔下方
        self.session.set("draw order", -1)  # 负值表示先绘制
        
        self.objects_created.append(slab_name)
        
        # 恢复自动重绘设置
        self.session.set("redraw automatically", auto_redraw)
        
        # 手动绘制新创建的结构
        self.session.draw("all")
        
        print(f"  创建了 {hole_count} 个空气孔和 1 个平板")
        
        return slab_name, hole_count
    
    def create_waveguide(self, name, length, width, height, material, position=(0, 0, 0)):
        """创建波导结构"""
        
        print(f"创建波导: {name}")
        print(f"  尺寸: {length*1e9:.1f} × {width*1e9:.1f} × {height*1e9:.1f} nm")
        print(f"  材料: {material}")
        print(f"  位置: {position}")
        
        self.session.addrect()
        self.session.set("name", name)
        self.session.set("x", position[0])
        self.session.set("y", position[1])
        self.session.set("z", position[2])
        self.session.set("x span", length)
        self.session.set("y span", width)
        self.session.set("z span", height)
        self.session.set("material", material)
        
        self.objects_created.append(name)
        
        # 立即绘制
        self.session.draw(name)
        
        return name
    
    def create_grating_coupler(self, name, period, duty_cycle, num_teeth, width, height, material):
        """创建光栅耦合器"""
        
        print(f"创建光栅耦合器: {name}")
        print(f"  周期: {period*1e9:.1f} nm")
        print(f"  占空比: {duty_cycle}")
        print(f"  齿数: {num_teeth}")
        
        # 临时关闭自动重绘
        auto_redraw = self.session.get("redraw automatically")
        self.session.set("redraw automatically", False)
        
        teeth_names = []
        
        for i in range(num_teeth):
            tooth_name = f"{name}_tooth_{i}"
            
            # 计算位置
            x_pos = i * period
            
            # 计算齿宽度
            tooth_width = period * duty_cycle
            
            # 添加齿
            self.session.addrect()
            self.session.set("name", tooth_name)
            self.session.set("x", x_pos)
            self.session.set("y", 0)
            self.session.set("z", 0)
            self.session.set("x span", tooth_width)
            self.session.set("y span", width)
            self.session.set("z span", height)
            self.session.set("material", material)
            
            teeth_names.append(tooth_name)
            self.objects_created.append(tooth_name)
        
        # 恢复自动重绘
        self.session.set("redraw automatically", auto_redraw)
        
        # 批量绘制所有齿
        for tooth_name in teeth_names:
            self.session.draw(tooth_name)
        
        print(f"  创建了 {num_teeth} 个光栅齿")
        
        return teeth_names
    
    def create_microring(self, name, radius, width, height, material, position=(0, 0, 0)):
        """创建微环谐振器"""
        
        print(f"创建微环谐振器: {name}")
        print(f"  半径: {radius*1e9:.1f} nm")
        print(f"  宽度: {width*1e9:.1f} nm")
        print(f"  高度: {height*1e9:.1f} nm")
        print(f"  材料: {material}")
        
        # 使用环面近似（实际仿真中可能使用弯曲波导）
        # 这里简化：使用圆柱体创建环
        
        self.session.addcylinder()
        self.session.set("name", name)
        self.session.set("x", position[0])
        self.session.set("y", position[1])
        self.session.set("z", position[2])
        self.session.set("radius", radius)
        self.session.set("z span", height)
        self.session.set("material", material)
        
        # 添加内孔（创建环形）
        hole_name = f"{name}_hole"
        self.session.addcylinder()
        self.session.set("name", hole_name)
        self.session.set("x", position[0])
        self.session.set("y", position[1])
        self.session.set("z", position[2])
        self.session.set("radius", radius - width)
        self.session.set("z span", height * 1.1)  # 稍厚以确保完全穿透
        self.session.set("material", "Air")
        
        self.objects_created.extend([name, hole_name])
        
        # 绘制微环
        self.session.draw(name)
        self.session.draw(hole_name)
        
        return name, hole_name
    
    def animate_parameter_sweep(self, object_name, parameter, values, delay=0.1):
        """参数扫描动画"""
        
        print(f"参数扫描动画: {object_name}.{parameter}")
        print(f"  值范围: {values[0]:.3e} 到 {values[-1]:.3e}")
        print(f"  步数: {len(values)}")
        print(f"  延迟: {delay}s")
        
        import time
        
        for i, value in enumerate(values):
            print(f"  步 {i+1}/{len(values)}: {parameter} = {value:.3e}")
            
            # 更新参数
            self.session.select(object_name)
            self.session.set(parameter, value)
            
            # 重绘对象
            self.session.draw(object_name)
            
            # 短暂延迟
            time.sleep(delay)
        
        print("  动画完成")
    
    def optimize_view(self):
        """优化视图设置"""
        
        print("优化视图设置...")
        
        # 设置图形细节
        self.session.set("graphics detail", "high")
        print("  图形细节: high")
        
        # 启用透明
        self.session.set("transparency", True)
        print("  透明渲染: enabled")
        
        # 启用阴影
        self.session.set("shadows", True)
        print("  阴影: enabled")
        
        # 启用抗锯齿
        self.session.set("antialiasing", True)
        print("  抗锯齿: enabled")
        
        # 设置刷新率
        self.session.set("view refresh rate", 60)
        print("  刷新率: 60 Hz")
        
        # 重绘所有对象以应用新设置
        self.session.draw("all")
        print("  视图设置已应用")

# 创建结构构建器
builder = StructureBuilder(fdtd)

# 构建复杂光子集成电路
print("构建光子集成电路...")

# 1. 创建光子晶体平板
print("\n" + "="*50)
print("1. 创建光子晶体平板")
print("="*50)

pc_slab, hole_count = builder.create_photonic_crystal(
    name="PC_slab",
    lattice_constant=0.4e-6,  # 400 nm
    radius=0.12e-6,  # 120 nm
    num_periods=3,  # 7×7 阵列
    material="Si (Silicon) - Palik"
)

# 2. 创建输入/输出波导
print("\n" + "="*50)
print("2. 创建输入/输出波导")
print("="*50)

wg_input = builder.create_waveguide(
    name="WG_input",
    length=5e-6,
    width=0.5e-6,
    height=0.22e-6,
    material="Si (Silicon) - Palik",
    position=(-3e-6, 0, 0)
)

wg_output = builder.create_waveguide(
    name="WG_output",
    length=5e-6,
    width=0.5e-6,
    height=0.22e-6,
    material="Si (Silicon) - Palik",
    position=(3e-6, 0, 0)
)

# 3. 创建光栅耦合器
print("\n" + "="*50)
print("3. 创建光栅耦合器")
print("="*50)

grating_teeth = builder.create_grating_coupler(
    name="GC_input",
    period=0.63e-6,  # 630 nm
    duty_cycle=0.5,  # 50%
    num_teeth=10,    # 10个齿
    width=10e-6,     # 10 μm 宽
    height=0.22e-6,  # 220 nm
    material="Si (Silicon) - Palik"
)

# 移动光栅耦合器到波导端
fdtd.select("GC_input_tooth_0")
# 调整位置（简化）
for i, tooth in enumerate(grating_teeth):
    fdtd.select(tooth)
    fdtd.set("x", -5e-6 + i * 0.63e-6)
    fdtd.set("y", 0)
    fdtd.set("z", 0)

# 批量重绘所有光栅齿
for tooth in grating_teeth:
    fdtd.draw(tooth)

# 4. 创建微环谐振器
print("\n" + "="*50)
print("4. 创建微环谐振器")
print("="*50)

ring, ring_hole = builder.create_microring(
    name="MRR",
    radius=5e-6,     # 5 μm 半径
    width=0.5e-6,    # 500 nm 宽度
    height=0.22e-6,  # 220 nm 高度
    material="Si (Silicon) - Palik",
    position=(0, 2e-6, 0)  # 在光子晶体上方
)

# 5. 创建总线波导（连接微环）
print("\n" + "="*50)
print("5. 创建总线波导")
print("="*50)

wg_bus = builder.create_waveguide(
    name="WG_bus",
    length=12e-6,
    width=0.5e-6,
    height=0.22e-6,
    material="Si (Silicon) - Palik",
    position=(0, 2e-6 + 5e-6 + 0.3e-6, 0)  # 微环上方
)

# 6. 动画演示：调整微环半径
print("\n" + "="*50)
print("6. 动画演示：调整微环半径")
print("="*50)

# 创建半径值范围
radii = np.linspace(4e-6, 6e-6, 11)

# 执行动画
builder.animate_parameter_sweep(
    object_name="MRR",
    parameter="radius",
    values=radii,
    delay=0.2
)

# 恢复原始半径
fdtd.select("MRR")
fdtd.set("radius", 5e-6)
fdtd.draw("MRR")

# 7. 优化视图
print("\n" + "="*50)
print("7. 优化视图设置")
print("="*50)

builder.optimize_view()

# 8. 统计
print("\n" + "="*50)
print("构建统计")
print("="*50)

print(f"总对象数: {len(builder.objects_created)}")
print("对象列表:")
for i, obj in enumerate(builder.objects_created):
    obj_type = fdtd.get(obj + "::object type")
    print(f"  {i+1}. {obj} ({obj_type})")

# 9. 最终重绘
print("\n最终重绘所有对象...")
fdtd.draw("all")
print("所有对象已最终绘制")

print("\n复杂结构构建完成!")
```

### 示例 3：交互式几何编辑和可视化

#### LSF 脚本
```lumerical
# 交互式几何编辑和可视化演示
?echo("交互式几何编辑和可视化演示...");

# 创建交互式测试结构
?echo("创建交互式测试结构...");

# 设置交互模式
set("visualization update", "immediate");
set("redraw automatically", true);

# 1. 创建可调谐光栅
grating_periods = [0.6e-6, 0.65e-6, 0.7e-6];
for (i = 1; i <= length(grating_periods); i = i + 1) {
    period = grating_periods{i};
    grating_name = "tunable_grating_" + num2str(i-1);
    
    addrect;
    set("name", grating_name);
    set("x", (i-1) * 2e-6);
    set("y", 0);
    set("z", 0);
    set("x span", period * 0.5);  # 50% 占空比
    set("y span", 2e-6);
    set("z span", 0.22e-6);
    set("material", "Si (Silicon) - Palik");
}

# 2. 创建可变宽度波导
waveguide_name = "variable_waveguide";
addrect;
set("name", waveguide_name);
set("x", 0);
set("y", 2e-6);
set("z", 0);
set("x span", 5e-6);
set("y span", 0.5e-6);  # 初始宽度
set("z span", 0.22e-6);
set("material", "Si (Silicon) - Palik");

# 3. 创建可移动微环
ring_name = "movable_ring";
addcylinder;
set("name", ring_name);
set("x", 0);
set("y", -2e-6);
set("z", 0);
set("radius", 3e-6);
set("z span", 0.22e-6);
set("material", "Si (Silicon) - Palik");

# 添加内孔创建环形
ring_hole = ring_name + "_hole";
addcylinder;
set("name", ring_hole);
set("x", 0);
set("y", -2e-6);
set("z", 0);
set("radius", 2.5e-6);  # 500 nm 环宽
set("z span", 0.25e-6);  # 稍厚
set("material", "Air");

# 初始绘制
draw("all");
?echo("交互式结构创建完成");

# 交互式宽度调整演示
?echo("\n交互式宽度调整演示: " + waveguide_name);
?echo("  模拟宽度调整...");
current_width = get(waveguide_name + "::y span");
?echo("  当前宽度: " + num2str(current_width*1e9) + " nm");

# 测试宽度序列
test_widths = [0.2e-6, 0.3e-6, 0.4e-6, 0.5e-6, 0.6e-6, 0.7e-6, 0.8e-6, 0.9e-6, 1.0e-6];
for (idx = 1; idx <= length(test_widths); idx = idx + 1) {
    width = test_widths{idx};
    ?echo("  测试 " + num2str(idx) + "/" + num2str(length(test_widths)) + ": 宽度 = " + num2str(width*1e9) + " nm");
    
    # 更新宽度
    select(waveguide_name);
    set("y span", width);
    
    # 重绘对象
    draw(waveguide_name);
    
    # 延迟以便观察
    sleep(0.3);
}

# 恢复原始宽度
select(waveguide_name);
set("y span", current_width);
draw(waveguide_name);
?echo("  恢复原始宽度");

# 交互式位置调整演示
?echo("\n交互式位置调整演示: " + ring_name);
?echo("  模拟位置调整...");
current_x = get(ring_name + "::x");
current_y = get(ring_name + "::y");
?echo("  当前位置: (" + num2str(current_x*1e6) + ", " + num2str(current_y*1e6) + ") μm");

# 测试位置序列
test_positions = [[0, -2e-6], [1e-6, -1.5e-6], [2e-6, -1e-6], [1e-6, -0.5e-6], 
                  [0, 0], [-1e-6, -0.5e-6], [-2e-6, -1e-6], [-1e-6, -1.5e-6], [0, -2e-6]];
for (idx = 1; idx <= length(test_positions); idx = idx + 1) {
    pos = test_positions{idx};
    x = pos(1);
    y = pos(2);
    
    ?echo("  位置 " + num2str(idx) + "/" + num2str(length(test_positions)) + 
          ": (" + num2str(x*1e6) + ", " + num2str(y*1e6) + ") μm");
    
    # 更新位置
    select(ring_name);
    set("x", x);
    set("y", y);
    
    # 重绘对象
    draw(ring_name);
    
    # 延迟以便观察
    sleep(0.4);
}

# 恢复原始位置
select(ring_name);
set("x", current_x);
set("y", current_y);
draw(ring_name);
?echo("  恢复原始位置");

# 材料探索演示
?echo("\n材料探索演示");
materials = ["Si (Silicon) - Palik", "SiO2 (Glass) - Palik", 
             "Si3N4 (Silicon Nitride) - Phillip", "Au (Gold) - Johnson and Christy",
             "Ag (Silver) - Johnson and Christy", "Al (Aluminum) - Rakic", "Air"];
             
?echo("  测试 " + num2str(length(materials)) + " 种材料");
original_material = get("tunable_grating_0::material");

for (idx = 1; idx <= length(materials); idx = idx + 1) {
    material = materials{idx};
    ?echo("  材料 " + num2str(idx) + "/" + num2str(length(materials)) + ": " + material);
    
    # 更改材料
    select("tunable_grating_0");
    set("material", material);
    
    # 重绘对象
    draw("tunable_grating_0");
    
    # 延迟以观察效果
    sleep(0.5);
}

# 恢复原始材料
select("tunable_grating_0");
set("material", original_material);
draw("tunable_grating_0");
?echo("  恢复原始材料: " + original_material);

# 可视化模式切换演示
?echo("\n可视化模式切换演示");
modes = ["immediate", "deferred", "manual"];
for (idx = 1; idx <= length(modes); idx = idx + 1) {
    mode = modes{idx};
    ?echo("  切换到模式: " + mode);
    
    set("visualization update", mode);
    
    # 根据模式调整设置
    if (mode == "immediate") {
        set("redraw automatically", true);
        ?echo("    自动重绘: 启用");
    } else if (mode == "deferred") {
        set("redraw automatically", true);
        ?echo("    自动重绘: 启用（延迟）");
    } else {  # manual
        set("redraw automatically", false);
        ?echo("    自动重绘: 禁用");
    }
    
    # 重绘以应用新设置
    draw("all");
    
    # 延迟以便观察
    sleep(1);
}

# 恢复立即模式
set("visualization update", "immediate");
set("redraw automatically", true);

# 最终重绘
draw("all");
?echo("\n交互式几何编辑和可视化演示完成!");
```

#### Python API
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("交互式几何编辑和可视化演示...")

class InteractiveEditor:
    """交互式编辑器"""
    
    def __init__(self, session):
        self.session = session
        self.edit_history = []
        
        # 设置交互模式
        self.session.set("visualization update", "immediate")
        self.session.set("redraw automatically", True)
    
    def create_interactive_structure(self):
        """创建交互式结构"""
        
        print("创建交互式测试结构...")
        
        # 创建基础结构
        structures = {}
        
        # 1. 可调谐光栅
        print("  创建可调谐光栅...")
        grating_periods = [0.6e-6, 0.65e-6, 0.7e-6]
        gratings = []
        
        for i, period in enumerate(grating_periods):
            grating_name = f"tunable_grating_{i}"
            
            self.session.addrect()
            self.session.set("name", grating_name)
            self.session.set("x", i * 2e-6)
            self.session.set("y", 0)
            self.session.set("z", 0)
            self.session.set("x span", period * 0.5)  # 50% 占空比
            self.session.set("y span", 2e-6)
            self.session.set("z span", 0.22e-6)
            self.session.set("material", "Si (Silicon) - Palik")
            
            # 添加可调谐标记
            self.session.addattribute("tunable", "true")
            self.session.addattribute("period", period)
            self.session.addattribute("index", i)
            
            gratings.append(grating_name)
            self.edit_history.append(f"创建光栅 {grating_name}，周期={period*1e9:.1f}nm")
        
        structures["gratings"] = gratings
        
        # 2. 可变宽度波导
        print("  创建可变宽度波导...")
        waveguide_name = "variable_waveguide"
        
        self.session.addrect()
        self.session.set("name", waveguide_name)
        self.session.set("x", 0)
        self.session.set("y", 2e-6)
        self.session.set("z", 0)
        self.session.set("x span", 5e-6)
        self.session.set("y span", 0.5e-6)  # 初始宽度
        self.session.set("z span", 0.22e-6)
        self.session.set("material", "Si (Silicon) - Palik")
        
        # 添加可变属性
        self.session.addattribute("variable", "width")
        self.session.addattribute("min_width", 0.2e-6)
        self.session.addattribute("max_width", 1.0e-6)
        
        structures["waveguide"] = waveguide_name
        self.edit_history.append(f"创建可变宽度波导 {waveguide_name}")
        
        # 3. 可移动微环
        print("  创建可移动微环...")
        ring_name = "movable_ring"
        
        self.session.addcylinder()
        self.session.set("name", ring_name)
        self.session.set("x", 0)
        self.session.set("y", -2e-6)
        self.session.set("z", 0)
        self.session.set("radius", 3e-6)
        self.session.set("z span", 0.22e-6)
        self.session.set("material", "Si (Silicon) - Palik")
        
        # 添加内孔
        ring_hole = ring_name + "_hole"
        self.session.addcylinder()
        self.session.set("name", ring_hole)
        self.session.set("x", 0)
        self.session.set("y", -2e-6)
        self.session.set("z", 0)
        self.session.set("radius", 2.5e-6)  # 500nm 环宽
        self.session.set("z span", 0.25e-6)  # 稍厚
        self.session.set("material", "Air")
        
        # 添加可移动属性
        self.session.addattribute("movable", "true")
        self.session.addattribute("position_range", [-5e-6, 5e-6])
        
        structures["ring"] = ring_name
        self.edit_history.append(f"创建可移动微环 {ring_name}")
        
        # 初始绘制
        self.session.draw("all")
        
        return structures
    
    def interactive_width_adjustment(self, object_name, parameter="y span"):
        """交互式宽度调整"""
        
        print(f"\n交互式宽度调整: {object_name}.{parameter}")
        print("  使用左右箭头键调整宽度，ESC退出")
        
        # 获取当前值
        self.session.select(object_name)
        current_value = self.session.get(parameter)
        
        print(f"  当前值: {current_value*1e9:.1f} nm")
        
        # 模拟交互（实际应用中可能使用GUI事件）
        # 这里使用预设值序列
        test_values = np.linspace(0.2e-6, 1.0e-6, 10)
        
        for i, value in enumerate(test_values):
            print(f"  测试 {i+1}/{len(test_values)}: 宽度 = {value*1e9:.1f} nm")
            
            # 更新宽度
            self.session.set(parameter, value)
            
            # 重绘对象
            self.session.draw(object_name)
            
            # 记录历史
            self.edit_history.append(f"调整 {object_name}.{parameter} 到 {value*1e9:.1f}nm")
            
            # 短暂延迟
            time.sleep(0.3)
        
        # 恢复原始值
        self.session.set(parameter, current_value)
        self.session.draw(object_name)
        print(f"  恢复原始值: {current_value*1e9:.1f} nm")
    
    def interactive_position_adjustment(self, object_name):
        """交互式位置调整"""
        
        print(f"\n交互式位置调整: {object_name}")
        print("  模拟位置调整...")
        
        # 获取当前位置
        self.session.select(object_name)
        x_current = self.session.get("x")
        y_current = self.session.get("y")
        
        print(f"  当前位置: ({x_current*1e6:.2f}, {y_current*1e6:.2f}) μm")
        
        # 测试位置序列
        test_positions = [
            (0, -2e-6),
            (1e-6, -1.5e-6),
            (2e-6, -1e-6),
            (1e-6, -0.5e-6),
            (0, 0),
            (-1e-6, -0.5e-6),
            (-2e-6, -1e-6),
            (-1e-6, -1.5e-6),
            (0, -2e-6)  # 返回起点
        ]
        
        for i, (x, y) in enumerate(test_positions):
            print(f"  位置 {i+1}/{len(test_positions)}: ({x*1e6:.2f}, {y*1e6:.2f}) μm")
            
            # 更新位置
            self.session.set("x", x)
            self.session.set("y", y)
            
            # 重绘对象
            self.session.draw(object_name)
            
            # 记录历史
            self.edit_history.append(f"移动 {object_name} 到 ({x*1e6:.2f}, {y*1e6:.2f})μm")
            
            # 短暂延迟
            time.sleep(0.4)
        
        # 恢复原始位置
        self.session.set("x", x_current)
        self.session.set("y", y_current)
        self.session.draw(object_name)
        print(f"  恢复原始位置")
    
    def material_exploration(self, object_name):
        """材料探索"""
        
        print(f"\n材料探索: {object_name}")
        
        # 材料列表
        materials = [
            "Si (Silicon) - Palik",
            "SiO2 (Glass) - Palik",
            "Si3N4 (Silicon Nitride) - Phillip",
            "Au (Gold) - Johnson and Christy",
            "Ag (Silver) - Johnson and Christy",
            "Al (Aluminum) - Rakic",
            "Air"
        ]
        
        print(f"  测试 {len(materials)} 种材料")
        
        original_material = self.session.getobject(object_name).material
        
        for i, material in enumerate(materials):
            print(f"  材料 {i+1}/{len(materials)}: {material}")
            
            # 更改材料
            self.session.select(object_name)
            self.session.set("material", material)
            
            # 重绘对象
            self.session.draw(object_name)
            
            # 记录历史
            self.edit_history.append(f"更改 {object_name} 材料为 {material}")
            
            # 延迟以观察效果
            time.sleep(0.5)
        
        # 恢复原始材料
        self.session.set("material", original_material)
        self.session.draw(object_name)
        print(f"  恢复原始材料: {original_material}")
    
    def undo_last_edit(self):
        """撤销最后一次编辑"""
        
        if len(self.edit_history) == 0:
            print("没有可撤销的编辑")
            return
        
        last_edit = self.edit_history.pop()
        print(f"撤销: {last_edit}")
        
        # 在实际应用中，这里会实现真正的撤销逻辑
        # 这里简化：只是记录
        
        # 重绘所有对象
        self.session.draw("all")
    
    def show_edit_history(self):
        """显示编辑历史"""
        
        print("\n编辑历史:")
        print("-"*50)
        
        if len(self.edit_history) == 0:
            print("  无编辑历史")
        else:
            for i, edit in enumerate(self.edit_history):
                print(f"  {i+1}. {edit}")
        
        print(f"总计: {len(self.edit_history)} 次编辑")
    
    def toggle_visualization_mode(self):
        """切换可视化模式"""
        
        current_mode = self.session.get("visualization update")
        
        modes = ["immediate", "deferred", "manual"]
        current_index = modes.index(current_mode) if current_mode in modes else 0
        next_index = (current_index + 1) % len(modes)
        next_mode = modes[next_index]
        
        print(f"切换可视化模式: {current_mode} -> {next_mode}")
        
        self.session.set("visualization update", next_mode)
        
        # 根据模式调整设置
        if next_mode == "immediate":
            self.session.set("redraw automatically", True)
            print("  自动重绘: 启用")
        elif next_mode == "deferred":
            self.session.set("redraw automatically", True)
            print("  自动重绘: 启用（延迟）")
        else:  # manual
            self.session.set("redraw automatically", False)
            print("  自动重绘: 禁用")
        
        # 重绘以应用新设置
        self.session.draw("all")

# 创建交互式编辑器
editor = InteractiveEditor(fdtd)

# 创建交互式结构
print("\n" + "="*50)
print("创建交互式结构")
print("="*50)

structures = editor.create_interactive_structure()

# 交互式演示
print("\n" + "="*50)
print("交互式演示")
print("="*50)

# 1. 宽度调整演示
editor.interactive_width_adjustment(structures["waveguide"], "y span")

# 2. 位置调整演示
editor.interactive_position_adjustment(structures["ring"])

# 3. 材料探索演示
editor.material_exploration(structures["gratings"][0])

# 4. 可视化模式切换
print("\n" + "="*50)
print("可视化模式切换演示")
print("="*50)

for _ in range(3):
    editor.toggle_visualization_mode()
    time.sleep(1)

# 恢复立即模式
fdtd.set("visualization update", "immediate")
fdtd.set("redraw automatically", True)

# 5. 编辑历史
editor.show_edit_history()

# 6. 撤销演示
print("\n" + "="*50)
print("撤销演示")
print("="*50)

for _ in range(3):
    if len(editor.edit_history) > 0:
        editor.undo_last_edit()
        time.sleep(0.5)
    else:
        break

# 最终状态
print("\n" + "="*50)
print("最终状态")
print("="*50)

# 最终重绘
fdtd.draw("all")
print("所有对象最终重绘完成")

# 显示最终对象列表
obj_names = fdtd.get("objects")
print(f"\n总对象数: {len(obj_names)}")
for i, name in enumerate(obj_names[:5]):  # 只显示前5个
    obj_type = fdtd.get(name + "::object type")
    print(f"  {i+1}. {name} ({obj_type})")

if len(obj_names) > 5:
    print(f"  ... 和 {len(obj_names)-5} 个其他对象")

print("\n交互式编辑演示完成!")
```

### 示例 4：性能优化和大型结构处理

#### LSF 脚本
```lumerical
# 性能优化和大型结构处理演示
?echo("性能优化和大型结构处理演示...");

# 大型阵列创建测试
?echo("\n1. 大型阵列创建测试");
?echo("="*70);

# 创建大型阵列
array_name = "large_array";
num_elements = 10;  # 10×10 = 100个元素，为演示减少数量
spacing = 0.5e-6;
element_size = 0.2e-6;
material = "Si (Silicon) - Palik";

?echo("创建大型阵列: " + array_name);
?echo("  元素数量: " + num2str(num_elements) + "×" + num2str(num_elements) + " = " + num2str(num_elements^2));
?echo("  间距: " + num2str(spacing*1e9) + " nm");
?echo("  元素尺寸: " + num2str(element_size*1e9) + " nm");

# 优化设置：关闭自动重绘
auto_redraw = get("redraw automatically");
set("redraw automatically", false);

# 降低图形细节
original_detail = get("graphics detail");
set("graphics detail", "low");

element_count = 0;
start_time = time;

# 创建元素
for (i = 1; i <= num_elements; i = i + 1) {
    for (j = 1; j <= num_elements; j = j + 1) {
        # 计算位置
        x_pos = (i - (num_elements+1)/2) * spacing;
        y_pos = (j - (num_elements+1)/2) * spacing;
        
        # 添加元素
        element_name = array_name + "_element_" + num2str(i) + "_" + num2str(j);
        addrect;
        set("name", element_name);
        set("x", x_pos);
        set("y", y_pos);
        set("z", 0);
        set("x span", element_size);
        set("y span", element_size);
        set("z span", element_size);
        set("material", material);
        
        element_count = element_count + 1;
        
        # 每25个元素报告一次进度
        if (mod(element_count, 25) == 0) {
            elapsed = time - start_time;
            ?echo("  已创建 " + num2str(element_count) + "/" + num2str(num_elements^2) + " 个元素，用时 " + num2str(elapsed) + "s");
        }
    }
}

creation_time = time - start_time;

# 批量绘制
?echo("  批量绘制 " + num2str(element_count) + " 个元素...");
draw_start = time;
draw("all");
draw_time = time - draw_start;

# 恢复设置
set("redraw automatically", auto_redraw);
set("graphics detail", original_detail);

?echo("  创建完成: " + num2str(element_count) + " 个元素");
?echo("  创建时间: " + num2str(creation_time) + "s");
?echo("  绘制时间: " + num2str(draw_time) + "s");
?echo("  总计时间: " + num2str(creation_time + draw_time) + "s");

# 性能基准测试
?echo("\n2. 绘制性能基准测试");
?echo("="*60);
?echo("对象数 | 自动重绘时间 | 手动重绘时间 | 加速比 | 内存使用");
?echo("-"*60);

num_objects_list = [10, 50, 100];
for (obj_idx = 1; obj_idx <= length(num_objects_list); obj_idx = obj_idx + 1) {
    num_objects = num_objects_list{obj_idx};
    
    # 1. 测试自动重绘模式
    set("redraw automatically", true);
    set("visualization update", "immediate");
    
    auto_start = time;
    for (i = 1; i <= num_objects; i = i + 1) {
        obj_name = "test_obj_auto_" + num2str(i);
        addrect;
        set("name", obj_name);
        set("x", i * 0.1e-6);
        set("y", 0);
        set("z", 0);
        set("x span", 0.05e-6);
        set("y span", 0.05e-6);
        set("z span", 0.05e-6);
        set("material", "Air");
    }
    auto_time = time - auto_start;
    
    # 清理对象
    for (i = 1; i <= num_objects; i = i + 1) {
        delete("test_obj_auto_" + num2str(i));
    }
    draw("all");
    
    # 2. 测试手动重绘模式
    set("redraw automatically", false);
    set("visualization update", "manual");
    
    # 创建对象（不绘制）
    manual_start = time;
    for (i = 1; i <= num_objects; i = i + 1) {
        obj_name = "test_obj_manual_" + num2str(i);
        addrect;
        set("name", obj_name);
        set("x", i * 0.1e-6);
        set("y", 0);
        set("z", 0);
        set("x span", 0.05e-6);
        set("y span", 0.05e-6);
        set("z span", 0.05e-6);
        set("material", "Air");
    }
    creation_time_only = time - manual_start;
    
    # 手动绘制
    draw_start = time;
    draw("all");
    manual_draw_time = time - draw_start;
    
    manual_time = creation_time_only + manual_draw_time;
    
    # 计算加速比
    if (manual_time > 0) {
        speedup = auto_time / manual_time;
    } else {
        speedup = 0;
    }
    
    # 估计内存使用
    memory_estimate = num_objects * 0.1;  # 假设每个对象0.1MB
    
    # 输出结果
    ?echo(num2str(num_objects, "%7d") + " | " + 
          num2str(auto_time, "%12.4f") + "s | " + 
          num2str(manual_time, "%12.4f") + "s | " + 
          num2str(speedup, "%7.2f") + "x | " + 
          num2str(memory_estimate, "%8.1f") + " MB");
    
    # 清理对象
    for (i = 1; i <= num_objects; i = i + 1) {
        delete("test_obj_manual_" + num2str(i));
    }
    draw("all");
}

# 优化设置建议
?echo("\n3. 针对不同规模结构的优化设置");
?echo("="*70);

test_sizes = [50, 500, 5000];
for (size_idx = 1; size_idx <= length(test_sizes); size_idx = size_idx + 1) {
    structure_size = test_sizes{size_idx};
    ?echo("\n为大型结构优化设置（预计 " + num2str(structure_size) + " 个对象）");
    
    if (structure_size < 100) {
        ?echo("  小型结构: 使用默认设置即可");
        set("redraw automatically", true);
        set("visualization update", "immediate");
        set("graphics detail", "high");
    } else if (structure_size < 1000) {
        ?echo("  中型结构: 建议使用延迟更新");
        set("redraw automatically", true);
        set("visualization update", "deferred");
        set("graphics detail", "normal");
    } else {
        ?echo("  大型结构: 建议使用手动更新和低细节");
        set("redraw automatically", false);
        set("visualization update", "manual");
        set("graphics detail", "low");
    }
    
    # 其他优化建议
    ?echo("  关闭透明渲染以减少计算");
    set("transparency", false);
    
    ?echo("  关闭阴影以提高性能");
    set("shadows", false);
    
    ?echo("  降低抗锯齿级别");
    set("antialiasing", false);
    
    ?echo("  降低视图刷新率");
    set("view refresh rate", 15);
    
    # 应用设置
    draw("all");
    ?echo("  优化设置已应用");
}

# 清理大型阵列
?echo("\n4. 清理测试对象");
?echo("="*70);

# 删除阵列元素
for (i = 1; i <= num_elements; i = i + 1) {
    for (j = 1; j <= num_elements; j = j + 1) {
        delete(array_name + "_element_" + num2str(i) + "_" + num2str(j));
    }
}

# 最终重绘
draw("all");
?echo("所有测试对象已清理");

# 性能统计
?echo("\n5. 性能统计摘要");
?echo("="*70);
?echo("总绘制调用次数: 多次");
?echo("总绘制时间: " + num2str(draw_time) + "s");
?echo("总创建对象数: " + num2str(element_count));
?echo("平均每次绘制时间: " + num2str(draw_time) + "s");

?echo("\n性能优化演示完成!");
```

#### Python API
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("性能优化和大型结构处理演示...")

class PerformanceOptimizer:
    """性能优化工具"""
    
    def __init__(self, session):
        self.session = session
        self.performance_stats = {
            'draw_calls': 0,
            'draw_time': 0.0,
            'objects_created': 0
        }
    
    def create_large_array(self, name, num_elements, spacing, element_size, material):
        """创建大型阵列结构"""
        
        print(f"创建大型阵列: {name}")
        print(f"  元素数量: {num_elements}×{num_elements} = {num_elements**2}")
        print(f"  间距: {spacing*1e9:.1f} nm")
        print(f"  元素尺寸: {element_size*1e9:.1f} nm")
        
        start_time = time.time()
        
        # 优化设置：关闭自动重绘
        auto_redraw = self.session.get("redraw automatically")
        self.session.set("redraw automatically", False)
        
        # 降低图形细节
        original_detail = self.session.get("graphics detail")
        self.session.set("graphics detail", "low")
        
        element_count = 0
        
        # 创建元素
        for i in range(num_elements):
            for j in range(num_elements):
                # 计算位置
                x_pos = (i - (num_elements-1)/2) * spacing
                y_pos = (j - (num_elements-1)/2) * spacing
                
                # 添加元素
                element_name = f"{name}_element_{i}_{j}"
                self.session.addrect()
                self.session.set("name", element_name)
                self.session.set("x", x_pos)
                self.session.set("y", y_pos)
                self.session.set("z", 0)
                self.session.set("x span", element_size)
                self.session.set("y span", element_size)
                self.session.set("z span", element_size)
                self.session.set("material", material)
                
                element_count += 1
                
                # 每100个元素报告一次进度
                if element_count % 100 == 0:
                    elapsed = time.time() - start_time
                    print(f"  已创建 {element_count}/{num_elements**2} 个元素，用时 {elapsed:.1f}s")
        
        creation_time = time.time() - start_time
        
        # 批量绘制
        print(f"  批量绘制 {element_count} 个元素...")
        draw_start = time.time()
        self.session.draw("all")
        draw_time = time.time() - draw_start
        
        # 恢复设置
        self.session.set("redraw automatically", auto_redraw)
        self.session.set("graphics detail", original_detail)
        
        # 更新统计
        self.performance_stats['draw_calls'] += 1
        self.performance_stats['draw_time'] += draw_time
        self.performance_stats['objects_created'] += element_count
        
        print(f"  创建完成: {element_count} 个元素")
        print(f"  创建时间: {creation_time:.2f}s")
        print(f"  绘制时间: {draw_time:.2f}s")
        print(f"  总计时间: {creation_time + draw_time:.2f}s")
        
        return element_count, creation_time, draw_time
    
    def benchmark_draw_performance(self, num_objects_list=[10, 50, 100, 200, 500]):
        """绘制性能基准测试"""
        
        print("\n绘制性能基准测试")
        print("="*60)
        print("对象数 | 自动重绘时间 | 手动重绘时间 | 加速比 | 内存使用")
        print("-"*60)
        
        results = []
        
        for num_objects in num_objects_list:
            print(f"{num_objects:7d} | ", end="")
            
            # 清理现有对象
            self._cleanup_objects()
            
            # 1. 测试自动重绘模式
            self.session.set("redraw automatically", True)
            self.session.set("visualization update", "immediate")
            
            auto_time = self._create_and_time_objects(num_objects, "auto")
            print(f"{auto_time:12.4f}s | ", end="")
            
            # 2. 测试手动重绘模式
            self.session.set("redraw automatically", False)
            self.session.set("visualization update", "manual")
            
            # 创建对象（不绘制）
            creation_time = self._create_objects_only(num_objects)
            
            # 手动绘制
            draw_start = time.time()
            self.session.draw("all")
            manual_draw_time = time.time() - draw_start
            
            manual_time = creation_time + manual_draw_time
            print(f"{manual_time:12.4f}s | ", end="")
            
            # 计算加速比
            if manual_time > 0:
                speedup = auto_time / manual_time
                print(f"{speedup:7.2f}x | ", end="")
            else:
                print(f"{'N/A':>7} | ", end="")
            
            # 估计内存使用（简化）
            memory_estimate = num_objects * 0.1  # 假设每个对象0.1MB
            print(f"{memory_estimate:8.1f} MB")
            
            results.append({
                'num_objects': num_objects,
                'auto_time': auto_time,
                'manual_time': manual_time,
                'speedup': speedup if manual_time > 0 else 0,
                'memory_estimate': memory_estimate
            })
            
            # 清理对象
            self._cleanup_objects()
        
        return results
    
    def _create_and_time_objects(self, num_objects, mode):
        """创建对象并计时（自动重绘）"""
        
        start_time = time.time()
        
        for i in range(num_objects):
            obj_name = f"test_obj_{mode}_{i}"
            self.session.addrect()
            self.session.set("name", obj_name)
            self.session.set("x", i * 0.1e-6)
            self.session.set("y", 0)
            self.session.set("z", 0)
            self.session.set("x span", 0.05e-6)
            self.session.set("y span", 0.05e-6)
            self.session.set("z span", 0.05e-6)
            self.session.set("material", "Air")
        
        return time.time() - start_time
    
    def _create_objects_only(self, num_objects):
        """只创建对象，不触发重绘"""
        
        start_time = time.time()
        
        # 临时关闭所有重绘
        original_update = self.session.get("visualization update")
        self.session.set("visualization update", "manual")
        self.session.set("redraw automatically", False)
        
        for i in range(num_objects):
            obj_name = f"test_obj_manual_{i}"
            self.session.addrect()
            self.session.set("name", obj_name)
            self.session.set("x", i * 0.1e-6)
            self.session.set("y", 0)
            self.session.set("z", 0)
            self.session.set("x span", 0.05e-6)
            self.session.set("y span", 0.05e-6)
            self.session.set("z span", 0.05e-6)
            self.session.set("material", "Air")
        
        creation_time = time.time() - start_time
        
        # 恢复设置
        self.session.set("visualization update", original_update)
        
        return creation_time
    
    def _cleanup_objects(self):
        """清理测试对象"""
        
        # 删除所有名称以"test_obj_"开头的对象
        try:
            all_objects = self.session.get("objects")
            for obj in all_objects:
                if obj.startswith("test_obj_"):
                    self.session.delete(obj)
        except:
            pass
        
        # 强制重绘以更新视图
        self.session.draw("all")
    
    def optimize_for_large_structures(self, structure_size):
        """为大型结构优化设置"""
        
        print(f"\n为大型结构优化设置（预计 {structure_size} 个对象）")
        
        recommendations = []
        
        if structure_size < 100:
            recommendations.append("小型结构: 使用默认设置即可")
            self.session.set("redraw automatically", True)
            self.session.set("visualization update", "immediate")
            self.session.set("graphics detail", "high")
            
        elif structure_size < 1000:
            recommendations.append("中型结构: 建议使用延迟更新")
            self.session.set("redraw automatically", True)
            self.session.set("visualization update", "deferred")
            self.session.set("graphics detail", "normal")
            
        else:
            recommendations.append("大型结构: 建议使用手动更新和低细节")
            self.session.set("redraw automatically", False)
            self.session.set("visualization update", "manual")
            self.session.set("graphics detail", "low")
        
        # 其他优化建议
        recommendations.append("关闭透明渲染以减少计算")
        self.session.set("transparency", False)
        
        recommendations.append("关闭阴影以提高性能")
        self.session.set("shadows", False)
        
        recommendations.append("降低抗锯齿级别")
        self.session.set("antialiasing", False)
        
        recommendations.append("降低视图刷新率")
        self.session.set("view refresh rate", 15)
        
        # 显示建议
        print("优化建议:")
        for i, rec in enumerate(recommendations):
            print(f"  {i+1}. {rec}")
        
        # 应用设置
        self.session.draw("all")
        print("优化设置已应用")
    
    def chunked_drawing(self, object_names, chunk_size=100):
        """分块绘制大型对象集"""
        
        print(f"分块绘制: {len(object_names)} 个对象，块大小: {chunk_size}")
        
        total_chunks = (len(object_names) + chunk_size - 1) // chunk_size
        total_time = 0.0
        
        for chunk_idx in range(total_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, len(object_names))
            
            chunk_objects = object_names[start_idx:end_idx]
            
            print(f"  绘制块 {chunk_idx+1}/{total_chunks}: 对象 {start_idx+1}-{end_idx}")
            
            # 绘制当前块
            chunk_start = time.time()
            
            for obj_name in chunk_objects:
                self.session.draw(obj_name)
            
            chunk_time = time.time() - chunk_start
            total_time += chunk_time
            
            print(f"    本块用时: {chunk_time:.3f}s")
        
        print(f"  总计绘制时间: {total_time:.3f}s")
        print(f"  平均每对象: {total_time/len(object_names):.5f}s")
        
        return total_time

# 创建性能优化器
optimizer = PerformanceOptimizer(fdtd)

# 1. 大型阵列创建
print("\n" + "="*70)
print("1. 大型阵列创建测试")
print("="*70)

# 创建中等大小的阵列
array_size = 20  # 20×20 = 400个元素
element_count, create_time, draw_time = optimizer.create_large_array(
    name="large_array",
    num_elements=array_size,
    spacing=0.5e-6,
    element_size=0.2e-6,
    material="Si (Silicon) - Palik"
)

# 2. 性能基准测试
print("\n" + "="*70)
print("2. 绘制性能基准测试")
print("="*70)

benchmark_results = optimizer.benchmark_draw_performance(
    num_objects_list=[10, 50, 100, 200]
)

# 3. 优化设置
print("\n" + "="*70)
print("3. 针对不同规模结构的优化设置")
print("="*70)

test_sizes = [50, 500, 5000]

for size in test_sizes:
    optimizer.optimize_for_large_structures(size)
    print()

# 4. 分块绘制测试
print("\n" + "="*70)
print("4. 分块绘制测试")
print("="*70)

# 创建测试对象集
test_object_count = 300
test_objects = []

print(f"创建 {test_object_count} 个测试对象...")

# 临时关闭自动重绘
auto_redraw = fdtd.get("redraw automatically")
fdtd.set("redraw automatically", False)

for i in range(test_object_count):
    obj_name = f"chunk_test_{i}"
    fdtd.addrect()
    fdtd.set("name", obj_name)
    fdtd.set("x", (i % 30) * 0.2e-6)
    fdtd.set("y", (i // 30) * 0.2e-6)
    fdtd.set("z", 0)
    fdtd.set("x span", 0.1e-6)
    fdtd.set("y span", 0.1e-6)
    fdtd.set("z span", 0.1e-6)
    fdtd.set("material", "Air")
    
    test_objects.append(obj_name)

# 恢复设置
fdtd.set("redraw automatically", auto_redraw)

# 测试不同块大小
chunk_sizes = [50, 100, 200, test_object_count]  # 包括一次性绘制

print(f"\n测试不同块大小的绘制性能:")
for chunk_size in chunk_sizes:
    if chunk_size == test_object_count:
        print(f"\n一次性绘制所有 {test_object_count} 个对象:")
    else:
        print(f"\n分块绘制，块大小: {chunk_size}:")
    
    total_time = optimizer.chunked_drawing(test_objects, chunk_size)

# 5. 清理
print("\n" + "="*70)
print("5. 清理测试对象")
print("="*70)

# 删除测试对象
for obj_name in test_objects:
    try:
        fdtd.delete(obj_name)
    except:
        pass

# 删除大型阵列
try:
    # 删除阵列元素
    for i in range(array_size):
        for j in range(array_size):
            fdtd.delete(f"large_array_element_{i}_{j}")
except:
    pass

# 最终重绘
fdtd.draw("all")
print("所有测试对象已清理")

# 6. 性能统计
print("\n" + "="*70)
print("6. 性能统计摘要")
print("="*70)

print(f"总绘制调用次数: {optimizer.performance_stats['draw_calls']}")
print(f"总绘制时间: {optimizer.performance_stats['draw_time']:.3f}s")
print(f"总创建对象数: {optimizer.performance_stats['objects_created']}")

if optimizer.performance_stats['draw_calls'] > 0:
    avg_draw_time = optimizer.performance_stats['draw_time'] / optimizer.performance_stats['draw_calls']
    print(f"平均每次绘制时间: {avg_draw_time:.3f}s")

print("\n性能优化演示完成!")
```

### 示例 5：故障排除和最佳实践

#### LSF 脚本
```lumerical
# 故障排除和最佳实践演示
?echo("故障排除和最佳实践演示...");

# 常见的绘制问题及解决方案
?echo("\n常见的绘制问题及解决方案:");
?echo("="*70);

# 问题1: 对象修改后视图不更新
?echo("\n1. 对象修改后视图不更新");
?echo("   症状: 更改属性后可视化不变，对象似乎卡在旧状态");
?echo("   可能原因:");
?echo("     - 自动重绘被禁用");
?echo("     - 可视化更新模式设置为'manual'");
?echo("     - 图形驱动程序问题");
?echo("   解决方案:");
?echo("     - 检查并启用自动重绘: set('redraw automatically', true)");
?echo("     - 设置可视化更新模式: set('visualization update', 'immediate')");
?echo("     - 手动触发重绘: draw('object_name') 或 draw('all')");
?echo("     - 更新图形驱动程序");

# 问题2: 绘制性能差
?echo("\n2. 绘制性能差");
?echo("   症状: 重绘缓慢，界面响应迟缓，内存使用高");
?echo("   可能原因:");
?echo("     - 对象数量过多");
?echo("     - 图形细节设置过高");
?echo("     - 自动重绘过于频繁");
?echo("     - 硬件限制");
?echo("   解决方案:");
?echo("     - 减少不必要的对象");
?echo("     - 降低图形细节: set('graphics detail', 'low')");
?echo("     - 使用延迟更新: set('visualization update', 'deferred')");
?echo("     - 关闭透明和阴影");
?echo("     - 升级硬件（GPU、RAM）");

# 问题3: 对象部分不可见
?echo("\n3. 对象部分不可见");
?echo("   症状: 对象只显示一部分，某些面缺失，闪烁或伪影");
?echo("   可能原因:");
?echo("     - 裁剪平面设置不当");
?echo("     - 对象超出视图范围");
?echo("     - 图形驱动程序bug");
?echo("     - Z-fighting（深度冲突）");
?echo("   解决方案:");
?echo("     - 调整裁剪平面: set('far clipping plane', 1e-3)");
?echo("     - 缩放视图以包含所有对象");
?echo("     - 更新图形驱动程序");
?echo("     - 调整对象绘制顺序");
?echo("     - 轻微偏移重叠对象的位置");

# 绘制最佳实践
?echo("\n绘制最佳实践:");
?echo("="*70);

practices = [
    "1. 增量构建: 对于复杂结构，分步构建并逐步绘制，而不是一次性创建所有对象",
    "2. 延迟更新: 在脚本中批量修改对象时，使用延迟或手动更新模式以提高性能",
    "3. 适当细节: 根据需求调整图形细节级别。调试时用'low'，最终展示用'high'",
    "4. 选择性重绘: 只重绘已更改的对象，而不是所有对象",
    "5. 内存管理: 定期删除不需要的对象，避免内存积累",
    "6. 硬件优化: 确保使用支持的GPU和足够的RAM以获得最佳性能",
    "7. 错误处理: 在绘制命令周围添加错误处理，特别是对于用户输入或复杂操作",
    "8. 备份视图: 在重大修改前保存视图状态，以便可以恢复",
    "9. 测试渲染: 在完整渲染前，使用少量对象测试渲染设置",
    "10. 文档记录: 记录复杂的绘制序列，以便调试和复现"
];

for (i = 1; i <= length(practices); i = i + 1) {
    ?echo(practices{i});
}

# 诊断工具和命令
?echo("\n诊断工具和命令:");
?echo("="*70);

?echo("getvisualization - 获取当前可视化设置");
?echo("  示例: settings = getvisualization();");
?echo("redrawinfo - 获取重绘统计信息");
?echo("  示例: info = redrawinfo();");
?echo("getgraphicsstats - 获取图形统计");
?echo("  示例: stats = getgraphicsstats();");
?echo("listobjects - 列出所有对象");
?echo("  示例: objects = listobjects();");
?echo("getobjecttype - 获取对象类型");
?echo("  示例: type = getobjecttype('object_name');");
?echo("checkmemory - 检查内存使用");
?echo("  示例: mem = checkmemory();");

# 绘制调试示例
?echo("\n绘制调试示例:");
?echo("="*70);

?echo("示例1: 检测和修复自动重绘问题");
?echo("-"*40);
?echo("模拟场景: 自动重绘被禁用");
set("redraw automatically", false);

# 创建测试对象
addrect;
set("name", "debug_rect");
set("x", 0);
set("y", 0);
set("z", 0);

?echo("  创建了矩形对象，但由于自动重绘禁用，可能不可见");

# 诊断
auto_redraw = get("redraw automatically");
?echo("  诊断: auto_redraw = " + num2str(auto_redraw));

# 修复
if (!auto_redraw) {
    ?echo("  修复: 启用自动重绘");
    set("redraw automatically", true);
    ?echo("  手动触发重绘");
    draw("debug_rect");
}

?echo("\n示例2: 处理绘制超时");
?echo("-"*40);

# 设置短超时
original_timeout = get("maximum draw time");
set("maximum draw time", 0.1);  # 0.1秒超时

?echo("  设置了短超时(0.1s)，测试复杂对象绘制");

# 尝试绘制（可能超时）
try {
    draw("all");
    ?echo("  绘制成功");
} catch {
    ?echo("  绘制超时");
    
    # 恢复合理超时
    ?echo("  恢复超时设置: " + num2str(original_timeout) + "s");
    set("maximum draw time", original_timeout);
    
    # 重试
    ?echo("  重试绘制...");
    draw("all");
    ?echo("  绘制成功");
}

# 性能检查清单
?echo("\n绘制性能检查清单:");
?echo("="*70);

checklist = [
    "□ 自动重绘: 仅在需要时启用，批量操作时禁用",
    "□ 更新模式: 根据场景选择 immediate/deferred/manual",
    "□ 图形细节: 调整到适当级别（low/normal/high）",
    "□ 透明渲染: 仅在需要时启用",
    "□ 阴影: 对性能影响大，酌情启用",
    "□ 抗锯齿: 对最终展示重要，调试时可禁用",
    "□ 裁剪平面: 设置为仅包含感兴趣区域",
    "□ 对象数量: 最小化不必要的对象",
    "□ 几何复杂度: 简化复杂几何（减少面数）",
    "□ 硬件资源: 确保足够的内存和GPU性能",
    "□ 驱动程序: 保持图形驱动程序更新",
    "□ 软件版本: 使用最新的Lumerical版本"
];

for (i = 1; i <= length(checklist); i = i + 1) {
    ?echo(checklist{i});
}

# 紧急恢复步骤
?echo("\n紧急恢复步骤（当绘制完全失败时）:");
?echo("="*70);

steps = [
    "1. 尝试最小化重绘: draw('all', 'minimal')",
    "2. 重置可视化设置: resetvisualization()",
    "3. 切换到安全模式: set('safe mode', true)",
    "4. 逐个对象重绘（从最重要的开始）",
    "5. 保存项目并重启Lumerical",
    "6. 禁用硬件加速: set('hardware acceleration', false)",
    "7. 检查错误日志: geterrorlog()",
    "8. 简化场景（删除复杂对象）",
    "9. 更新或回滚图形驱动程序",
    "10. 联系Lumerical技术支持"
];

for (i = 1; i <= length(steps); i = i + 1) {
    ?echo(steps{i});
}

# 清理测试对象
?echo("\n清理测试对象");
?echo("="*70);

# 删除调试对象
try {
    delete("debug_rect");
    ?echo("删除调试对象: debug_rect");
} catch {
    ?echo("无法删除调试对象");
}

# 最终建议
?echo("\n最终建议");
?echo("="*70);
?echo("1. 始终在脚本开始时设置明确的可视化参数");
?echo("2. 对于生产脚本，实现适当的错误处理和恢复机制");
?echo("3. 记录所有与绘制相关的性能问题和解决方案");
?echo("4. 定期测试绘制功能以确保可靠性");
?echo("5. 保持工作流程的简洁和可重复性");

?echo("\n故障排除演示完成!");
```

#### Python API
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("故障排除和最佳实践演示...")

class TroubleshootingGuide:
    """故障排除指南"""
    
    def __init__(self, session):
        self.session = session
    
    def common_draw_issues(self):
        """常见的绘制问题"""
        
        print("常见的绘制问题及解决方案:")
        print("="*70)
        
        issues = [
            {
                "issue": "对象修改后视图不更新",
                "symptoms": ["更改属性后可视化不变", "对象似乎卡在旧状态"],
                "causes": [
                    "自动重绘被禁用",
                    "可视化更新模式设置为'manual'",
                    "图形驱动程序问题"
                ],
                "solutions": [
                    "检查并启用自动重绘: set('redraw automatically', True)",
                    "设置可视化更新模式: set('visualization update', 'immediate')",
                    "手动触发重绘: draw('object_name') 或 draw('all')",
                    "更新图形驱动程序"
                ]
            },
            {
                "issue": "绘制性能差",
                "symptoms": ["重绘缓慢", "界面响应迟缓", "内存使用高"],
                "causes": [
                    "对象数量过多",
                    "图形细节设置过高",
                    "自动重绘过于频繁",
                    "硬件限制"
                ],
                "solutions": [
                    "减少不必要的对象",
                    "降低图形细节: set('graphics detail', 'low')",
                    "使用延迟更新: set('visualization update', 'deferred')",
                    "关闭透明和阴影",
                    "升级硬件（GPU、RAM）"
                ]
            },
            {
                "issue": "对象部分不可见",
                "symptoms": ["对象只显示一部分", "某些面缺失", "闪烁或伪影"],
                "causes": [
                    "裁剪平面设置不当",
                    "对象超出视图范围",
                    "图形驱动程序bug",
                    "Z-fighting（深度冲突）"
                ],
                "solutions": [
                    "调整裁剪平面: set('far clipping plane', 1e-3)",
                    "缩放视图以包含所有对象",
                    "更新图形驱动程序",
                    "调整对象绘制顺序",
                    "轻微偏移重叠对象的位置"
                ]
            },
            {
                "issue": "材料显示不正确",
                "symptoms": ["所有对象显示为同一颜色", "材料颜色不对", "透明度异常"],
                "causes": [
                    "材料数据库未加载",
                    "颜色映射设置错误",
                    "透明度设置问题"
                ],
                "solutions": [
                    "确保材料数据库已正确安装",
                    "检查材料颜色映射: set('material colormap', 'default')",
                    "调整透明度设置: set('transparency', True/False)",
                    "重启Lumerical会话"
                ]
            },
            {
                "issue": "绘制命令无响应",
                "symptoms": ["draw() 命令不返回", "界面冻结", "超时错误"],
                "causes": [
                    "对象过于复杂",
                    "内存不足",
                    "软件bug",
                    "与其他进程冲突"
                ],
                "solutions": [
                    "简化复杂几何",
                    "增加超时限制: set('maximum draw time', 10.0)",
                    "分批绘制大型结构",
                    "关闭其他应用程序",
                    "重启Lumerical"
                ]
            }
        ]
        
        for i, issue in enumerate(issues):
            print(f"\n{i+1}. {issue['issue']}")
            print(f"   症状: {', '.join(issue['symptoms'])}")
            print(f"   可能原因:")
            for cause in issue['causes']:
                print(f"     - {cause}")
            print(f"   解决方案:")
            for solution in issue['solutions']:
                print(f"     - {solution}")
    
    def draw_best_practices(self):
        """绘制最佳实践"""
        
        print("\n绘制最佳实践:")
        print("="*70)
        
        practices = [
            ("增量构建", "对于复杂结构，分步构建并逐步绘制，而不是一次性创建所有对象。"),
            ("延迟更新", "在脚本中批量修改对象时，使用延迟或手动更新模式以提高性能。"),
            ("适当细节", "根据需求调整图形细节级别。调试时用'low'，最终展示用'high'。"),
            ("选择性重绘", "只重绘已更改的对象，而不是所有对象。"),
            ("内存管理", "定期删除不需要的对象，避免内存积累。"),
            ("硬件优化", "确保使用支持的GPU和足够的RAM以获得最佳性能。"),
            ("错误处理", "在绘制命令周围添加错误处理，特别是对于用户输入或复杂操作。"),
            ("备份视图", "在重大修改前保存视图状态，以便可以恢复。"),
            ("测试渲染", "在完整渲染前，使用少量对象测试渲染设置。"),
            ("文档记录", "记录复杂的绘制序列，以便调试和复现。")
        ]
        
        for i, (title, description) in enumerate(practices):
            print(f"{i+1}. {title}")
            print(f"   {description}")
    
    def diagnostic_tools(self):
        """诊断工具"""
        
        print("\n诊断工具和命令:")
        print("="*70)
        
        tools = [
            ("getvisualization", "获取当前可视化设置", "settings = getvisualization();"),
            ("redrawinfo", "获取重绘统计信息", "info = redrawinfo();"),
            ("getgraphicsstats", "获取图形统计", "stats = getgraphicsstats();"),
            ("listobjects", "列出所有对象", "objects = listobjects();"),
            ("getobjecttype", "获取对象类型", "type = getobjecttype('object_name');"),
            ("checkmemory", "检查内存使用", "mem = checkmemory();"),
            ("getperformance", "获取性能指标", "perf = getperformance();"),
            ("testrendering", "测试渲染功能", "result = testrendering();")
        ]
        
        for tool_name, description, example in tools:
            print(f"{tool_name}")
            print(f"  描述: {description}")
            print(f"  示例: {example}")
            print()
    
    def draw_debugging_examples(self):
        """绘制调试示例"""
        
        print("\n绘制调试示例:")
        print("="*70)
        
        print("示例1: 检测和修复自动重绘问题")
        print("-"*40)
        
        # 模拟自动重绘被意外禁用的情况
        print("模拟场景: 自动重绘被禁用")
        self.session.set("redraw automatically", False)
        
        # 创建测试对象
        self.session.addrect()
        self.session.set("name", "debug_rect")
        self.session.set("x", 0)
        self.session.set("y", 0)
        self.session.set("z", 0)
        
        print("  创建了矩形对象，但由于自动重绘禁用，可能不可见")
        
        # 诊断
        auto_redraw = self.session.get("redraw automatically")
        print(f"  诊断: auto_redraw = {auto_redraw}")
        
        # 修复
        if not auto_redraw:
            print("  修复: 启用自动重绘")
            self.session.set("redraw automatically", True)
            print("  手动触发重绘")
            self.session.draw("debug_rect")
        
        print("\n示例2: 处理绘制超时")
        print("-"*40)
        
        # 设置短超时
        original_timeout = self.session.get("maximum draw time")
        self.session.set("maximum draw time", 0.1)  # 0.1秒超时
        
        print("  设置了短超时(0.1s)，测试复杂对象绘制")
        
        # 尝试绘制（可能超时）
        try:
            self.session.draw("all")
            print("  绘制成功")
        except Exception as e:
            print(f"  绘制超时: {e}")
            
            # 恢复合理超时
            print(f"  恢复超时设置: {original_timeout}s")
            self.session.set("maximum draw time", original_timeout)
            
            # 重试
            print("  重试绘制...")
            self.session.draw("all")
            print("  绘制成功")
        
        print("\n示例3: 优化绘制顺序")
        print("-"*40)
        
        # 创建多个对象
        objects = []
        for i in range(5):
            obj_name = f"order_test_{i}"
            self.session.addrect()
            self.session.set("name", obj_name)
            self.session.set("x", i * 0.5e-6)
            self.session.set("y", 0)
            self.session.set("z", 0)
            objects.append(obj_name)
        
        print(f"  创建了 {len(objects)} 个测试对象")
        
        # 测试不同绘制顺序
        print("  测试1: 逆序绘制")
        for obj in reversed(objects):
            self.session.draw(obj)
        
        print("  测试2: 批量绘制")
        self.session.draw("all")
        
        print("  测试3: 选择性绘制（仅修改的对象）")
        # 修改一个对象
        self.session.select(objects[2])
        self.session.set("x span", 1e-6)
        # 只绘制修改的对象
        self.session.draw(objects[2])
        
        # 清理
        for obj in objects:
            self.session.delete(obj)
        
        print("  清理了测试对象")
    
    def performance_checklist(self):
        """性能检查清单"""
        
        print("\n绘制性能检查清单:")
        print("="*70)
        
        checklist = [
            ("自动重绘", "仅在需要时启用，批量操作时禁用"),
            ("更新模式", "根据场景选择 immediate/deferred/manual"),
            ("图形细节", "调整到适当级别（low/normal/high）"),
            ("透明渲染", "仅在需要时启用"),
            ("阴影", "对性能影响大，酌情启用"),
            ("抗锯齿", "对最终展示重要，调试时可禁用"),
            ("裁剪平面", "设置为仅包含感兴趣区域"),
            ("对象数量", "最小化不必要的对象"),
            ("几何复杂度", "简化复杂几何（减少面数）"),
            ("硬件资源", "确保足够的内存和GPU性能"),
            ("驱动程序", "保持图形驱动程序更新"),
            ("软件版本", "使用最新的Lumerical版本")
        ]
        
        for item, recommendation in checklist:
            print(f"□ {item}: {recommendation}")
    
    def emergency_recovery(self):
        """紧急恢复步骤"""
        
        print("\n紧急恢复步骤（当绘制完全失败时）:")
        print("="*70)
        
        steps = [
            "1. 尝试最小化重绘: draw('all', 'minimal')",
            "2. 重置可视化设置: resetvisualization()",
            "3. 切换到安全模式: set('safe mode', true)",
            "4. 逐个对象重绘（从最重要的开始）",
            "5. 保存项目并重启Lumerical",
            "6. 禁用硬件加速: set('hardware acceleration', false)",
            "7. 检查错误日志: geterrorlog()",
            "8. 简化场景（删除复杂对象）",
            "9. 更新或回滚图形驱动程序",
            "10. 联系Lumerical技术支持"
        ]
        
        for step in steps:
            print(step)

# 创建故障排除指南
troubleshooter = TroubleshootingGuide(fdtd)

# 显示各种指南
print("\n" + "="*70)
print("故障排除指南")
print("="*70)

troubleshooter.common_draw_issues()
troubleshooter.draw_best_practices()
troubleshooter.diagnostic_tools()
troubleshooter.draw_debugging_examples()
troubleshooter.performance_checklist()
troubleshooter.emergency_recovery()

# 清理测试对象
print("\n" + "="*70)
print("清理测试对象")
print("="*70)

# 删除调试对象
try:
    fdtd.delete("debug_rect")
    print("删除调试对象: debug_rect")
except:
    pass

# 最终建议
print("\n" + "="*70)
print("最终建议")
print("="*70)

print("1. 始终在脚本开始时设置明确的可视化参数")
print("2. 对于生产脚本，实现适当的错误处理和恢复机制")
print("3. 记录所有与绘制相关的性能问题和解决方案")
print("4. 定期测试绘制功能以确保可靠性")
print("5. 保持工作流程的简洁和可重复性")

print("\n故障排除演示完成!")
```

## 注意事项

1. **性能影响**：频繁调用 `draw` 命令可能显著影响性能，特别是在大型仿真中。在脚本中批量修改对象属性，然后调用一次 `draw` 通常更高效。

2. **自动重绘**：Lumerical 默认启用自动重绘。对于需要修改大量对象的脚本，考虑暂时禁用自动重绘（`set("redraw automatically", false)`），在修改完成后手动调用 `draw`。

3. **可视化模式**：`visualization update` 设置控制重绘行为：
   - `"immediate"`：每次修改后立即重绘（响应快但可能慢）
   - `"deferred"`：延迟重绘，积累修改后批量更新
   - `"manual"`：完全手动控制，需要显式调用 `draw`

4. **图形细节**：`graphics detail` 设置影响渲染质量和性能：
   - `"low"`：最快，适用于大型结构或调试
   - `"normal"`：平衡质量和性能
   - `"high"`：高质量，适用于最终展示
   - `"maximum"`：最高质量，可能很慢

5. **内存管理**：复杂几何的可视化可能消耗大量内存。定期删除不需要的对象并简化几何可以帮助管理内存使用。

6. **硬件要求**：高质量可视化需要足够的 GPU 内存和处理能力。对于大型仿真，确保系统有足够的资源。

7. **错误处理**：`draw` 命令可能因各种原因失败（内存不足、图形错误等）。在生产脚本中包含适当的错误处理。

8. **兼容性**：某些可视化功能可能取决于 Lumerical 版本和图形硬件。在部署脚本前在不同系统上测试。

9. **脚本优化**：在循环中避免不必要的 `draw` 调用。只在需要更新可视化时调用。

10. **用户体验**：对于交互式工具，考虑用户的视觉反馈。重要更改后立即重绘，次要更改可以延迟或批量处理。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有几何可视化功能 |
| MODE Solutions | ✅ 完全支持 | 所有几何可视化功能 |
| DEVICE | ✅ 完全支持 | 所有几何可视化功能 |
| INTERCONNECT | ⚠️ 有限支持 | 主要用于原理图，几何可视化有限 |

## 相关命令

- `redraw` - 重绘视图（与 `draw` 类似，但有时有细微差别）
- `refresh` - 刷新界面（更新所有窗口，不仅仅是 CAD 视图）
- `update` - 更新对象属性并重绘
- `zoomto` - 缩放至适合所有对象
- `view` - 设置视图角度和方向
- `setview` - 设置特定视图参数
- `getvisualization` - 获取当前可视化设置
- `setvisualization` - 设置可视化参数
- `addobject` - 添加新对象（通常自动触发重绘）
- `delete` - 删除对象（通常自动触发重绘）

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增可视化性能优化 |
| Lumerical 2019a | 增加延迟绘制模式和手动控制 |
| Lumerical 2018a | 新增 Python API 支持 |
| Lumerical 2017a | 新增图形细节级别控制 |

## 参考

1. Lumerical Script Language Reference: `draw` 命令
2. Lumerical Python API Documentation: `session.draw()` 方法
3. Lumerical 知识库: 可视化性能优化指南
4. Lumerical 知识库: 几何渲染故障排除

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*