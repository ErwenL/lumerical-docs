# addwaveguide

## 概述

`addwaveguide` 命令用于在仿真中添加一个波导结构。波导是光子集成电路（PIC）中的核心元件，用于引导和传输光信号。该命令专为 MODE Solutions 设计，支持创建各种类型的波导，包括条形波导、脊形波导、槽波导等，可定义复杂的横截面形状和沿传播方向的锥度变化。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addwaveguide;
```

### Python API (Lumapi)
```python
session.addwaveguide()
```

## 参数

`addwaveguide` 命令没有直接参数，但需要通过后续的 `set` 命令配置波导属性。

## 配置属性

添加波导后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "waveguide" | 波导名称 |
| `x`, `y`, `z` | float | 0 | 波导起始点坐标 (m) |
| `length` | float | 10e-6 | 波导长度 (m) |
| `width` | float | 500e-9 | 波导宽度 (m) |
| `height` | float | 220e-9 | 波导高度 (m) |
| `slab height` | float | 0 | 平板高度（用于脊形波导）(m) |
| `sidewall angle` | float | 90 | 侧壁角度 (度)，90 表示垂直侧壁 |
| `taper width 1` | float | 500e-9 | 起始端宽度 (m)，用于锥形波导 |
| `taper width 2` | float | 500e-9 | 终止端宽度 (m)，用于锥形波导 |
| `taper length` | float | 0 | 锥形区长度 (m)，0 表示无锥度 |

### 2. 材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material` | string | "<Object defined dielectric>" | 波导芯层材料名称 |
| `slab material` | string | "<Object defined dielectric>" | 平板层材料名称（用于脊形波导） |
| `cladding material` | string | "SiO2 (Glass) - Palik" | 包层材料名称 |
| `index` | float | 1.0 | 折射率（当 material 为 "<Object defined dielectric>" 时使用） |
| `index units` | string | "microns" | 折射率单位："m", "microns", "nm" |

### 3. 波导类型与模式属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `waveguide type` | string | "strip" | 波导类型："strip", "ridge", "slot", "rib" |
| `bent waveguide` | int | 0 | 是否弯曲波导：0=直波导，1=弯曲波导 |
| `bend radius` | float | 10e-6 | 弯曲半径 (m)，当 bent waveguide=1 时使用 |
| `bend angle` | float | 90 | 弯曲角度 (度) |
| `polarization` | string | "TE" | 偏振模式："TE", "TM", "both" |
| `mode` | int | 1 | 模式阶数 |

### 4. 网格与渲染属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `override mesh order from material database` | int | 0 | 是否覆盖材料数据库中的网格顺序 |
| `mesh order` | int | 2 | 网格顺序（需先启用覆盖） |
| `render type` | string | "detailed" | 渲染类型："detailed", "wireframe" |
| `alpha` | float | 1.0 | 透明度 (0.0-1.0) |
| `color` | array[4] | [0.5, 0.5, 0.5, 1.0] | RGBA 颜色值 |

### 5. 旋转属性（可选）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `first axis` | string | "none" | 第一旋转轴："none", "x", "y", "z" |
| `rotation 1` | float | 0 | 第一旋转角度 (度) |
| `second axis` | string | "none" | 第二旋转轴 |
| `rotation 2` | float | 0 | 第二旋转角度 (度) |
| `third axis` | string | "none" | 第三旋转轴 |
| `rotation 3` | float | 0 | 第三旋转角度 (度) |

## 返回值

`addwaveguide` 命令没有返回值。成功执行后，会在仿真中添加一个波导对象。

## 示例

### 示例 1: 基本条形波导创建

#### LSF 脚本
```lumerical
// 添加条形波导
addwaveguide;

// 设置几何尺寸
set("name", "Si strip waveguide");
set("x", 0);
set("y", 0);
set("z", 0);
set("length", 50e-6);      // 长度 50μm
set("width", 500e-9);      // 宽度 500nm
set("height", 220e-9);     // 高度 220nm

// 设置材料
set("material", "Si (Silicon) - Palik");
set("cladding material", "SiO2 (Glass) - Palik");

// 设置波导类型
set("waveguide type", "strip");
set("polarization", "TE");

// 设置网格顺序
set("override mesh order from material database", 1);
set("mesh order", 2);
```

#### Python API
```python
import lumapi

# 创建会话（MODE Solutions）
mode = lumapi.MODE()

# 添加波导
mode.addwaveguide()

# 设置几何尺寸
mode.set("name", "Si strip waveguide")
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("length", 50e-6)      # 长度 50μm
mode.set("width", 500e-9)      # 宽度 500nm
mode.set("height", 220e-9)     # 高度 220nm

# 设置材料
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")

# 设置波导类型
mode.set("waveguide type", "strip")
mode.set("polarization", "TE")

# 设置网格顺序
mode.set("override mesh order from material database", 1)
mode.set("mesh order", 2)
```

### 示例 2: 脊形波导创建

#### LSF 脚本
```lumerical
// 添加脊形波导
addwaveguide;
set("name", "Si rib waveguide");
set("length", 100e-6);         // 长度 100μm
set("width", 500e-9);          // 脊宽度 500nm
set("height", 220e-9);         // 脊高度 220nm
set("slab height", 100e-9);    // 平板高度 100nm

// 设置材料
set("material", "Si (Silicon) - Palik");
set("slab material", "Si (Silicon) - Palik");
set("cladding material", "SiO2 (Glass) - Palik");

// 设置波导类型
set("waveguide type", "ridge");
set("polarization", "TE");

// 设置侧壁角度（略倾斜）
set("sidewall angle", 85);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addwaveguide()
mode.set("name", "Si rib waveguide")
mode.set("length", 100e-6)         # 长度 100μm
mode.set("width", 500e-9)          # 脊宽度 500nm
mode.set("height", 220e-9)         # 脊高度 220nm
mode.set("slab height", 100e-9)    # 平板高度 100nm

# 设置材料
mode.set("material", "Si (Silicon) - Palik")
mode.set("slab material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")

# 设置波导类型
mode.set("waveguide type", "ridge")
mode.set("polarization", "TE")

# 设置侧壁角度（略倾斜）
mode.set("sidewall angle", 85)
```

### 示例 3: 弯曲波导

#### LSF 脚本
```lumerical
// 添加弯曲波导
addwaveguide;
set("name", "bent waveguide");
set("length", 30e-6);         // 直波导段长度
set("width", 500e-9);         // 宽度 500nm
set("height", 220e-9);        // 高度 220nm

// 设置弯曲参数
set("bent waveguide", 1);     // 启用弯曲
set("bend radius", 20e-6);    // 弯曲半径 20μm
set("bend angle", 90);        // 弯曲角度 90度

// 设置材料
set("material", "Si (Silicon) - Palik");
set("cladding material", "SiO2 (Glass) - Palik");

// 设置波导类型
set("waveguide type", "strip");
set("polarization", "TE");
```

#### Python API
```python
mode = lumapi.MODE()
mode.addwaveguide()
mode.set("name", "bent waveguide")
mode.set("length", 30e-6)         # 直波导段长度
mode.set("width", 500e-9)         # 宽度 500nm
mode.set("height", 220e-9)        # 高度 220nm

# 设置弯曲参数
mode.set("bent waveguide", 1)     # 启用弯曲
mode.set("bend radius", 20e-6)    # 弯曲半径 20μm
mode.set("bend angle", 90)        # 弯曲角度 90度

# 设置材料
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")

# 设置波导类型
mode.set("waveguide type", "strip")
mode.set("polarization", "TE")
```

### 示例 4: 锥形波导（模斑转换器）

#### LSF 脚本
```lumerical
// 添加锥形波导（模斑转换器）
addwaveguide;
set("name", "taper waveguide");
set("length", 20e-6);          // 总长度 20μm
set("height", 220e-9);         // 高度 220nm

// 设置锥形参数
set("taper width 1", 200e-9);  // 起始宽度 200nm
set("taper width 2", 500e-9);  // 终止宽度 500nm
set("taper length", 15e-6);    // 锥形区长度 15μm

// 设置材料
set("material", "Si (Silicon) - Palik");
set("cladding material", "SiO2 (Glass) - Palik");

// 设置波导类型
set("waveguide type", "strip");
set("polarization", "TE");

// 设置线框渲染以查看锥形
set("render type", "wireframe");
set("alpha", 0.7);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addwaveguide()
mode.set("name", "taper waveguide")
mode.set("length", 20e-6)          # 总长度 20μm
mode.set("height", 220e-9)         # 高度 220nm

# 设置锥形参数
mode.set("taper width 1", 200e-9)  # 起始宽度 200nm
mode.set("taper width 2", 500e-9)  # 终止宽度 500nm
mode.set("taper length", 15e-6)    # 锥形区长度 15μm

# 设置材料
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")

# 设置波导类型
mode.set("waveguide type", "strip")
mode.set("polarization", "TE")

# 设置线框渲染以查看锥形
mode.set("render type", "wireframe")
mode.set("alpha", 0.7)
```

### 示例 5: 波导阵列（波分复用器）

#### LSF 脚本
```lumerical
// 创建波导阵列（用于波分复用器）
for(i = 0; i < 8; i++) {
    addwaveguide;
    set("name", "waveguide_array_" + num2str(i));
    set("x", 0);
    set("y", i * 5e-6);        // Y方向偏移 5μm
    set("z", 0);
    set("length", 100e-6);     // 长度 100μm
    set("width", 500e-9);      // 宽度 500nm
    set("height", 220e-9);     // 高度 220nm
    
    // 设置材料
    set("material", "Si (Silicon) - Palik");
    set("cladding material", "SiO2 (Glass) - Palik");
    
    // 设置波导类型
    set("waveguide type", "strip");
    set("polarization", "TE");
    
    // 设置颜色区分
    color_value = (i+1)/8;
    set("color", [color_value, 0.2, 0.8-color_value, 0.8]);
}
```

#### Python API
```python
mode = lumapi.MODE()

# 创建波导阵列（用于波分复用器）
for i in range(8):
    mode.addwaveguide()
    mode.set("name", f"waveguide_array_{i}")
    mode.set("x", 0)
    mode.set("y", i * 5e-6)        # Y方向偏移 5μm
    mode.set("z", 0)
    mode.set("length", 100e-6)     # 长度 100μm
    mode.set("width", 500e-9)      # 宽度 500nm
    mode.set("height", 220e-9)     # 高度 220nm
    
    # 设置材料
    mode.set("material", "Si (Silicon) - Palik")
    mode.set("cladding material", "SiO2 (Glass) - Palik")
    
    # 设置波导类型
    mode.set("waveguide type", "strip")
    mode.set("polarization", "TE")
    
    # 设置颜色区分
    color_value = (i+1)/8
    mode.set("color", [color_value, 0.2, 0.8-color_value, 0.8])
```

## 注意事项

### 1. 波导类型选择
- **条形波导 (strip)**: 完全限制结构，适用于高折射率对比度系统
- **脊形波导 (ridge)**: 部分限制结构，具有平板层，适用于低损耗传输
- **槽波导 (slot)**: 在低折射率槽中增强电场，适用于传感应用
- **肋形波导 (rib)**: 类似脊形波导，但平板层较薄

### 2. 几何参数
- 波导宽度和高度决定模式限制和有效折射率
- 侧壁角度影响散射损耗和制造容差
- 锥形波导用于模斑转换和低损耗耦合
- 弯曲波导的弯曲半径影响弯曲损耗

### 3. 材料设置
- 波导芯层材料通常为高折射率材料（如硅、氮化硅）
- 包层材料通常为低折射率材料（如二氧化硅、空气）
- 脊形波导需要设置芯层材料和平板层材料
- 自定义折射率材料需设置 `material` 为 "<Object defined dielectric>" 并指定 `index`

### 4. 模式分析
- MODE Solutions 专为波导模式分析设计
- 使用 `polarization` 属性指定偏振模式（TE/TM）
- `mode` 属性指定模式阶数（1=基模）
- 弯曲波导需要考虑弯曲引起的模式畸变

### 5. 性能优化
- 波导尺寸越小，模式限制越强，但制造难度增加
- 锥形波导可以改善模式匹配，降低耦合损耗
- 弯曲波导的弯曲半径应足够大以避免显著损耗
- 考虑使用 `addmesh` 命令在波导区域添加网格覆盖区提高分辨率

## 错误处理

### 常见错误
1. **尺寸无效**: `width` ≤ 0 或 `height` ≤ 0 或 `length` ≤ 0
   - 解决方案：确保所有尺寸 > 0

2. **弯曲半径过小**: `bend radius` 太小导致模式泄漏
   - 解决方案：增加弯曲半径，一般建议 > 5μm

3. **材料不存在**: 指定的材料名称不在数据库中
   - 解决方案：检查材料名称拼写，或使用自定义折射率

4. **波导类型无效**: `waveguide type` 不是有效类型
   - 解决方案：检查波导类型值

5. **锥形参数冲突**: `taper length` > `length`
   - 解决方案：确保 `taper length` ≤ `length`

6. **网格生成失败**: 波导尺寸过小或形状过于复杂导致网格问题
   - 解决方案：调整波导尺寸，确保足够的网格分辨率

### Python 错误处理
```python
import lumapi

try:
    mode = lumapi.MODE()
    
    # 添加波导
    mode.addwaveguide()
    
    # 配置波导属性
    mode.set("name", "test waveguide")
    mode.set("length", 50e-6)
    mode.set("width", 500e-9)
    mode.set("height", 220e-9)
    
    # 检查参数有效性
    length = mode.get("length")
    width = mode.get("width")
    height = mode.get("height")
    
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("波导尺寸必须 > 0")
    
    # 检查弯曲半径（如果启用弯曲）
    if mode.get("bent waveguide") == 1:
        bend_radius = mode.get("bend radius")
        if bend_radius < 5e-6:
            print("警告: 弯曲半径较小，可能增加弯曲损耗")
    
    # 设置材料
    mode.set("material", "Si (Silicon) - Palik")
    mode.set("cladding material", "SiO2 (Glass) - Palik")
    
except ValueError as e:
    print(f"几何参数错误: {e}")
    # 恢复默认值
    mode.set("length", 10e-6)
    mode.set("width", 500e-9)
    mode.set("height", 220e-9)
    
except Exception as e:
    print(f"波导创建失败: {e}")
    
    # 检查具体错误
    if "material" in str(e).lower():
        print("错误: 材料不存在，请检查材料名称")
    elif "width" in str(e).lower() or "height" in str(e).lower() or "length" in str(e).lower():
        print("错误: 尺寸无效，请检查宽度/高度/长度值")
    elif "bend" in str(e).lower():
        print("错误: 弯曲参数无效，请检查弯曲半径和角度")
    elif "waveguide type" in str(e).lower():
        print("错误: 波导类型无效，必须是 'strip', 'ridge', 'slot', 'rib' 之一")
    elif "taper" in str(e).lower():
        print("错误: 锥形参数无效，请检查锥形宽度和长度")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `addrect`: 添加矩形（可用于创建简单波导）
- `addplanarsolid`: 添加平面实体（可用于创建平板波导）
- `addcylinder`: 添加圆柱体（可用于创建光纤）
- `bentwaveguide`: 设置弯曲波导参数
- `addmesh`: 添加网格覆盖区（用于波导区域细化）
- `select`: 选择对象进行进一步操作
- `setnamed`: 按名称设置对象属性

## 产品支持

- **主要支持**: MODE Solutions
- **有限支持**: FDTD Solutions（部分功能）
- **不支持**: DEVICE, INTERCONNECT

## 应用场景

### 1. 光子集成电路设计
```python
# 创建硅光子波导用于数据传输
mode.addwaveguide()
mode.set("name", "Si photonic waveguide")
mode.set("length", 1000e-6)    # 长度 1mm
mode.set("width", 500e-9)      # 宽度 500nm
mode.set("height", 220e-9)     # 厚度 220nm
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")
mode.set("waveguide type", "strip")
mode.set("polarization", "TE")
```

### 2. 模斑转换器设计
```python
# 创建锥形波导用于光纤-芯片耦合
mode.addwaveguide()
mode.set("name", "spot size converter")
mode.set("length", 100e-6)         # 长度 100μm
mode.set("height", 220e-9)         # 高度 220nm
mode.set("taper width 1", 200e-9)  # 起始宽度 200nm（匹配纳米波导）
mode.set("taper width 2", 3000e-9) # 终止宽度 3μm（匹配光纤模式）
mode.set("taper length", 80e-6)    # 锥形长度 80μm
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")
```

### 3. 波导弯曲设计
```python
# 创建紧凑型弯曲波导
mode.addwaveguide()
mode.set("name", "compact bend")
mode.set("length", 10e-6)          # 直波导段长度
mode.set("width", 500e-9)          # 宽度 500nm
mode.set("height", 220e-9)         # 高度 220nm
mode.set("bent waveguide", 1)      # 启用弯曲
mode.set("bend radius", 5e-6)      # 小弯曲半径 5μm
mode.set("bend angle", 90)         # 90度弯曲
mode.set("material", "Si (Silicon) - Palik")
mode.set("cladding material", "SiO2 (Glass) - Palik")
```

### 4. 波导阵列（AWG）
```python
# 创建阵列波导光栅（AWG）的波导阵列
n_waveguides = 50
for i in range(n_waveguides):
    mode.addwaveguide()
    mode.set("name", f"awg_waveguide_{i}")
    mode.set("x", 0)
    mode.set("y", i * 2e-6)        # 阵列间距 2μm
    mode.set("length", 500e-6)     # 长度 500μm
    mode.set("width", 500e-9)      # 宽度 500nm
    mode.set("height", 220e-9)     # 高度 220nm
    mode.set("material", "Si (Silicon) - Palik")
    mode.set("cladding material", "SiO2 (Glass) - Palik")
    
    # 设置长度渐变（用于 AWG）
    extra_length = i * 10e-6
    mode.set("length", 500e-6 + extra_length)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `taper width 1/2` 和 `taper length` 属性 |
| Lumerical 2019a | 新增 `bent waveguide` 和 `bend radius/angle` 属性 |
| Lumerical 2018a | 新增 `waveguide type` 属性支持多种波导类型 |
| Lumerical 2017a | 首次引入 `addwaveguide` 命令 |
| 1.1 | 更新日期，完善文档格式，补充应用场景 |

## 参考

1. Lumerical MODE Solutions 用户指南
2. Lumerical 波导设计手册
3. 光子集成电路设计原理
4. Lumerical 脚本命令参考手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*