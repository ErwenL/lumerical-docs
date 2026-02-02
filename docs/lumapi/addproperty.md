# addproperty

## 概述

`addproperty` 命令用于向材料、对象或仿真添加自定义属性。这些属性可以是材料的光学、电学、热学或机械特性，也可以是对象的几何参数或仿真设置。该命令允许用户扩展 Lumerical 的内置属性集，支持高级仿真需求。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addproperty;
```

### Python API (Lumapi)
```python
session.addproperty()
```

## 参数

`addproperty` 命令没有直接参数，但需要通过后续的 `set` 命令配置属性类型和值。属性的具体配置取决于目标对象类型。

## 配置属性

添加属性后，可以使用 `set` 命令配置以下属性：

### 1. 基本属性设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "property" | 属性名称 |
| `target` | string | "material" | 目标对象类型："material", "object", "simulation", "global" |
| `target name` | string | "" | 目标对象名称（如果为空，应用于所有匹配对象） |
| `property type` | string | "scalar" | 属性类型："scalar", "vector", "matrix", "tensor", "function" |
| `data type` | string | "float" | 数据类型："float", "int", "bool", "string", "complex" |
| `unit` | string | "unitless" | 单位（如 "m", "Hz", "W/m·K" 等） |
| `description` | string | "" | 属性描述 |

### 2. 数值属性配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `value` | 取决于类型 | 0 | 属性值（标量、向量或矩阵） |
| `default value` | 取决于类型 | 0 | 默认值 |
| `min value` | float | -inf | 最小值（仅标量） |
| `max value` | float | inf | 最大值（仅标量） |
| `allowed values` | array | [] | 允许的值列表（离散选项） |
| `is required` | bool | false | 是否为必需属性 |

### 3. 函数属性配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `function expression` | string | "" | 函数表达式（如 "sin(2*pi*f*t)"） |
| `independent variables` | array | ["x"] | 独立变量列表 |
| `dependent variable` | string | "y" | 因变量名称 |
| `parameter names` | array | [] | 参数名称列表 |
| `parameter values` | array | [] | 参数值列表 |
| `function type` | string | "analytical" | 函数类型："analytical", "tabular", "interpolated" |

### 4. 材料属性配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `material property type` | string | "optical" | 材料属性类型："optical", "electrical", "thermal", "mechanical" |
| `wavelength dependent` | bool | false | 是否与波长相关 |
| `temperature dependent` | bool | false | 是否与温度相关 |
| `frequency range` | vector | [0, inf] | 频率范围 [min, max] (Hz) |
| `temperature range` | vector | [0, 1000] | 温度范围 [min, max] (K) |
| `anisotropic` | bool | false | 是否为各向异性属性 |

### 5. 光学材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `nonlinear coefficient` | float | 0 | 非线性系数 (m²/W) |
| `two photon absorption` | float | 0 | 双光子吸收系数 (m/W) |
| `raman coefficient` | float | 0 | 拉曼系数 |
| `kerr coefficient` | float | 0 | 克尔系数 |
| `electro-optic coefficient` | float | 0 | 电光系数 (m/V) |
| `thermo-optic coefficient` | float | 0 | 热光系数 (1/K) |
| `birefringence` | float | 0 | 双折射率 |
| `dispersion slope` | float | 0 | 色散斜率 |

### 6. 电学材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `conductivity` | float | 0 | 电导率 (S/m) |
| `resistivity` | float | inf | 电阻率 (Ω·m) |
| `mobility` | float | 0 | 载流子迁移率 (m²/V·s) |
| `carrier concentration` | float | 0 | 载流子浓度 (1/m³) |
| `bandgap` | float | 0 | 带隙 (eV) |
| `dielectric breakdown` | float | inf | 介电击穿场强 (V/m) |
| `work function` | float | 0 | 功函数 (eV) |

### 7. 热学材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal conductivity` | float | 0 | 热导率 (W/m·K) |
| `specific heat` | float | 0 | 比热容 (J/kg·K) |
| `density` | float | 0 | 密度 (kg/m³) |
| `thermal expansion` | float | 0 | 热膨胀系数 (1/K) |
| `emissivity` | float | 0 | 发射率 |
| `absorptivity` | float | 0 | 吸收率 |

### 8. 高级配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `validation script` | string | "" | 验证脚本（检查属性值有效性） |
| `update script` | string | "" | 更新脚本（属性变化时执行） |
| `dependency` | array | [] | 依赖的其他属性列表 |
| `visibility` | string | "normal" | 可见性："normal", "advanced", "hidden" |
 | `group` | string | "default" | 属性分组 |
| `category` | string | "general" | 类别 |

## 返回值

`addproperty` 命令没有直接的返回值。成功执行后，会在目标对象上创建一个新的自定义属性，该属性可以通过 `set` 和 `get` 命令进行配置和访问。

## 示例

### 示例 1：添加非线性光学属性
```python
import lumapi

session = lumapi.FDTD()

# 首先添加材料
session.addmaterial()
session.set("name", "silicon_nl")

# 添加非线性属性
session.addproperty()
session.set("name", "nonlinear_coefficient")
session.set("target", "material")
session.set("target name", "silicon_nl")
session.set("material property type", "optical")

# 配置非线性参数
session.set("nonlinear coefficient", 2.4e-18)  # 硅的非线性系数 (m²/W)
session.set("two photon absorption", 8e-11)    # 双光子吸收系数 (m/W)
session.set("kerr coefficient", 3e-16)         # 克尔系数

# 配置波长相关性
session.set("wavelength dependent", True)
session.set("frequency range", [150e12, 500e12])  # 150-500 THz

# 配置单位
session.set("unit", "m²/W")
session.set("description", "Silicon nonlinear optical coefficients for FDTD simulation")
```

### 示例 2：添加温度相关热导率
```python
import lumapi

session = lumapi.DEVICE()

# 添加材料热属性
session.addproperty()
session.set("name", "thermal_conductivity_vs_temperature")
session.set("target", "material")
session.set("material property type", "thermal")

# 配置为温度相关函数
session.set("property type", "function")
session.set("function type", "tabular")
session.set("independent variables", ["temperature"])
session.set("dependent variable", "thermal_conductivity")

# 定义温度-热导率数据点
temperatures = [200, 250, 300, 350, 400, 450, 500]  # K
conductivities = [120, 115, 110, 105, 100, 95, 90]  # W/m·K

# 创建表格数据
import numpy as np
data = np.column_stack((temperatures, conductivities))
session.set("value", data.tolist())

# 配置单位
session.set("unit", "W/m·K")
session.set("temperature dependent", True)
session.set("temperature range", [200, 500])
```

### 示例 3：添加自定义几何参数
```python
import lumapi

session = lumapi.MODE()

# 添加波导对象
session.addrect()
session.set("name", "waveguide")

# 添加自定义几何参数
session.addproperty()
session.set("name", "taper_length")
session.set("target", "object")
session.set("target name", "waveguide")
session.set("property type", "scalar")
session.set("data type", "float")
session.set("value", 10e-6)  # 10 μm 锥形长度
session.set("unit", "m")
session.set("min value", 1e-6)  # 最小 1 μm
session.set("max value", 100e-6) # 最大 100 μm
session.set("description", "Taper length for adiabatic mode conversion")

# 添加另一个参数
session.addproperty()
session.set("name", "sidewall_angle")
session.set("target", "object")
session.set("target name", "waveguide")
session.set("property type", "scalar")
session.set("data type", "float")
session.set("value", 85)  # 85 度侧壁角
session.set("unit", "degrees")
session.set("allowed values", [80, 85, 90])  # 只允许这三个值
```

### 示例 4：添加仿真全局参数
```python
import lumapi

session = lumapi.INTERCONNECT()

# 添加全局仿真参数
session.addproperty()
session.set("name", "simulation_temperature")
session.set("target", "simulation")
session.set("property type", "scalar")
session.set("data type", "float")
session.set("value", 300)  # 300 K
session.set("unit", "K")
session.set("description", "Global simulation temperature for all components")

# 添加蒙特卡洛参数
session.addproperty()
session.set("name", "monte_carlo_iterations")
session.set("target", "simulation")
session.set("property type", "scalar")
session.set("data type", "int")
session.set("value", 1000)  # 1000 次迭代
session.set("min value", 10)
session.set("max value", 10000)

# 添加容差参数
session.addproperty()
session.set("name", "convergence_tolerance")
session.set("target", "simulation")
session.set("property type", "scalar")
session.set("data type", "float")
session.set("value", 1e-6)
session.set("unit", "relative")

# 添加验证脚本
validation_script = """
def validate_temperature(value):
    if value < 0:
        return "Temperature must be positive"
    if value > 1000:
        return "Temperature too high for reliable simulation"
    return ""
"""
session.set("validation script", validation_script)
```

## 注意事项

1. **目标对象存在性**：确保目标对象（材料、几何体等）在添加属性之前已存在
2. **属性命名唯一性**：属性名称在目标对象范围内应唯一
3. **数据类型匹配**：确保属性值与声明的数据类型匹配
4. **单位一致性**：使用正确的单位，注意单位换算
5. **性能影响**：过多自定义属性可能影响仿真性能
6. **依赖管理**：正确处理属性之间的依赖关系
7. **验证脚本**：使用验证脚本确保属性值在合理范围内
 8. **向后兼容性**：自定义属性可能不被所有 Lumerical 版本支持

## 错误处理

### 常见错误
1. **目标对象不存在**
   - 错误信息：`Target object not found`
   - 解决方案：确保目标对象（材料、几何体等）已创建

2. **属性名称冲突**
   - 错误信息：`Property name already exists`
   - 解决方案：使用唯一的属性名称

3. **无效的数据类型**
   - 错误信息：`Invalid data type for property`
   - 解决方案：检查属性类型与值的匹配

4. **超出范围的值**
   - 错误信息：`Value out of range`
   - 解决方案：确保值在 `min value` 和 `max value` 范围内

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加属性
    fdtd.addproperty()
    fdtd.set("name", "custom_property")
    fdtd.set("target", "material")
    fdtd.set("target name", "non_existent_material")  # 可能引发错误
    
    fdtd.set("value", 1.5)
    
except lumapi.LumApiError as e:
    print(f"添加属性失败: {e}")
    
    # 检查具体错误类型
    if "not found" in str(e).lower():
        print("错误: 目标对象不存在")
    elif "already exists" in str(e).lower():
        print("错误: 属性名称已存在")
    elif "invalid" in str(e).lower():
        print("错误: 无效的参数")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持材料属性、仿真参数
- **MODE Solutions**: 支持材料属性、几何参数
- **DEVICE**: 支持热学、电学材料属性
- **INTERCONNECT**: 支持全局仿真参数、组件参数

## 相关命令

- `addmaterial` - 添加材料
- `set` - 设置对象属性
- `get` - 获取属性值
- `addscript` - 添加脚本对象
- `addcustom` - 添加自定义监视器
- `addimport` - 导入外部数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增函数类型属性支持 |
| Lumerical 2019a | 扩展材料属性类型 |
| Lumerical 2018a | 初始版本 |

## 参考

1. Lumerical 自定义属性指南
2. Lumerical 脚本语言参考手册
3. Lumerical Python API 文档

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*