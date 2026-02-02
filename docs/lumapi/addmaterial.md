# addmaterial

## 概述

`addmaterial` 命令用于在仿真中添加或定义新材料。材料是 Lumerical 仿真的基础，定义了光学和电学特性，包括折射率、吸收、色散等属性。该命令支持从材料数据库选择预定义材料，或创建自定义材料模型。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addmaterial;
```

### Python API (Lumapi)
```python
session.addmaterial()
```

## 参数

`addmaterial` 命令没有直接参数，但需要通过后续的 `set` 命令配置材料属性。

## 配置属性

添加材料后，可以使用 `set` 命令配置以下属性：

### 1. 基本材料属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "material" | 材料名称 |
| `type` | string | "dielectric" | 材料类型："dielectric", "metal", "conductive", "anisotropic" |
| `model` | string | "constant n" | 材料模型："constant n", "sellmeier", "drude-lorentz", "sampled data" |

### 2. 光学属性（介电材料）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `refractive index` | float | 1.0 | 折射率（常数模型） |
| `extinction coefficient` | float | 0 | 消光系数 |
| `permittivity` | float | 1.0 | 介电常数 |
| `permeability` | float | 1.0 | 磁导率 |

### 3. 材料模型参数
#### Sellmeier 模型
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `sellmeier type` | string | "standard" | Sellmeier 类型："standard", "modified" |
| `sellmeier coefficients` | array | [0,0,0,0,0,0] | Sellmeier 系数 [B1, C1, B2, C2, B3, C3] |

#### Drude-Lorentz 模型
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `plasma frequency` | float | 1e15 | 等离子体频率 (Hz) |
| `collision frequency` | float | 1e13 | 碰撞频率 (Hz) |
| `lorentz oscillators` | int | 0 | Lorentz 振子数量 |

### 4. 电学属性（导电材料）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `conductivity` | float | 0 | 电导率 (S/m) |
| `resistivity` | float | 0 | 电阻率 (Ω·m) |
| `mobility` | float | 0 | 载流子迁移率 (m²/V·s) |
| `carrier concentration` | float | 0 | 载流子浓度 (1/m³) |

### 5. 热学属性（可选）
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `thermal conductivity` | float | 0 | 热导率 (W/m·K) |
| `specific heat` | float | 0 | 比热容 (J/kg·K) |
| `density` | float | 0 | 密度 (kg/m³) |

### 6. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.5, 0.5, 0.5, 1.0] | RGBA 颜色值 |
| `alpha` | float | 1.0 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addmaterial` 命令没有返回值。成功执行后，会在材料数据库中添加一个新材料对象。

## 示例

### 示例 1: 添加常数折射率材料

#### LSF 脚本
```lumerical
// 添加新材料
addmaterial;
set("name", "custom_silicon");
set("type", "dielectric");
set("model", "constant n");
set("refractive index", 3.45);          // 硅在1550nm的折射率
set("extinction coefficient", 0.001);   // 轻微吸收
set("color", [0.8, 0.2, 0.2, 1.0]);     // 红色
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加新材料
fdtd.addmaterial()
fdtd.set("name", "custom_silicon")
fdtd.set("type", "dielectric")
fdtd.set("model", "constant n")
fdtd.set("refractive index", 3.45)          # 硅在1550nm的折射率
fdtd.set("extinction coefficient", 0.001)   # 轻微吸收
fdtd.set("color", [0.8, 0.2, 0.2, 1.0])     # 红色
```

### 示例 2: 使用 Sellmeier 模型创建色散材料

#### LSF 脚本
```lumerical
addmaterial;
set("name", "SiO2_sellmeier");
set("type", "dielectric");
set("model", "sellmeier");

// 设置 Sellmeier 系数 (SiO2 的典型值)
// n² = 1 + B1·λ²/(λ² - C1) + B2·λ²/(λ² - C2) + B3·λ²/(λ² - C3)
set("sellmeier type", "standard");
set("sellmeier coefficients", [
    0.6961663,    // B1
    0.0684043,    // C1 (μm²)
    0.4079426,    // B2
    0.1162414,    // C2 (μm²)
    0.8974794,    // B3
    9.896161      // C3 (μm²)
]);

// 设置材料颜色为蓝色半透明
set("color", [0.2, 0.2, 0.8, 0.7]);
set("alpha", 0.7);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmaterial()
fdtd.set("name", "SiO2_sellmeier")
fdtd.set("type", "dielectric")
fdtd.set("model", "sellmeier")

# 设置 Sellmeier 系数 (SiO2 的典型值)
# n² = 1 + B1·λ²/(λ² - C1) + B2·λ²/(λ² - C2) + B3·λ²/(λ² - C3)
fdtd.set("sellmeier type", "standard")
fdtd.set("sellmeier coefficients", [
    0.6961663,    # B1
    0.0684043,    # C1 (μm²)
    0.4079426,    # B2
    0.1162414,    # C2 (μm²)
    0.8974794,    # B3
    9.896161      # C3 (μm²)
])

# 设置材料颜色为蓝色半透明
fdtd.set("color", [0.2, 0.2, 0.8, 0.7])
fdtd.set("alpha", 0.7)
```

### 示例 3: 创建金属材料（Drude 模型）

#### LSF 脚本
```lumerical
addmaterial;
set("name", "gold_drude");
set("type", "metal");
set("model", "drude-lorentz");

// 设置 Drude 参数（金的典型值）
set("plasma frequency", 2.183e15);      // 等离子体频率 (Hz)
set("collision frequency", 6.46e12);    // 碰撞频率 (Hz)

// 设置电导率（可选）
set("conductivity", 4.1e7);             // 电导率 (S/m)

// 设置颜色为金色
set("color", [1.0, 0.84, 0.0, 1.0]);    // 金色

// 设置渲染属性
set("render type", "metal");
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmaterial()
fdtd.set("name", "gold_drude")
fdtd.set("type", "metal")
fdtd.set("model", "drude-lorentz")

# 设置 Drude 参数（金的典型值）
fdtd.set("plasma frequency", 2.183e15)      # 等离子体频率 (Hz)
fdtd.set("collision frequency", 6.46e12)    # 碰撞频率 (Hz)

# 设置电导率（可选）
fdtd.set("conductivity", 4.1e7)             # 电导率 (S/m)

# 设置颜色为金色
fdtd.set("color", [1.0, 0.84, 0.0, 1.0])    # 金色

# 设置渲染属性
fdtd.set("render type", "metal")
```

### 示例 4: 使用采样数据创建自定义材料

#### LSF 脚本
```lumerical
addmaterial;
set("name", "sampled_material");
set("type", "dielectric");
set("model", "sampled data");

// 定义波长范围和折射率数据
wavelengths = linspace(1.0e-6, 2.0e-6, 100);  // 1-2 μm，100个点
n_data = 1.5 + 0.1 * sin(2*pi*(wavelengths-1e-6)/1e-6);  // 示例数据
k_data = 0.01 * ones(100);                     // 恒定消光系数

// 设置采样数据
set("wavelength data", wavelengths);
set("refractive index data", n_data);
set("extinction coefficient data", k_data);

// 设置插值方法
set("interpolation method", "cubic");

// 设置材料描述
set("description", "Custom material with sinusoidal refractive index");
```

#### Python API
```python
import numpy as np

fdtd = lumapi.FDTD()
fdtd.addmaterial()
fdtd.set("name", "sampled_material")
fdtd.set("type", "dielectric")
fdtd.set("model", "sampled data")

# 定义波长范围和折射率数据
wavelengths = np.linspace(1.0e-6, 2.0e-6, 100)  # 1-2 μm，100个点
n_data = 1.5 + 0.1 * np.sin(2*np.pi*(wavelengths-1e-6)/1e-6)  # 示例数据
k_data = 0.01 * np.ones(100)                     # 恒定消光系数

# 设置采样数据
fdtd.set("wavelength data", wavelengths)
fdtd.set("refractive index data", n_data)
fdtd.set("extinction coefficient data", k_data)

# 设置插值方法
fdtd.set("interpolation method", "cubic")

# 设置材料描述
fdtd.set("description", "Custom material with sinusoidal refractive index")
```

### 示例 5: 创建各向异性材料

#### LSF 脚本
```lumerical
addmaterial;
set("name", "anisotropic_crystal");
set("type", "anisotropic");
set("model", "constant n");

// 设置主轴折射率（单轴晶体）
set("ordinary refractive index", 1.55);   // 寻常光折射率
set("extraordinary refractive index", 1.65);  // 非寻常光折射率

// 设置晶体取向（欧拉角，单位：度）
set("rotation 1", 30);    // 绕 Z 轴旋转
set("rotation 2", 45);    // 绕 X 轴旋转
set("rotation 3", 0);     // 绕 Z 轴旋转

// 设置介电张量（可选，替代折射率）
// eps = [εxx, εxy, εxz; εyx, εyy, εyz; εzx, εzy, εzz]
set("permittivity tensor", [
    2.4025, 0, 0,
    0, 2.4025, 0,
    0, 0, 2.7225
]);

// 设置材料颜色
set("color", [0.5, 0.8, 0.3, 0.8]);
set("alpha", 0.8);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmaterial()
fdtd.set("name", "anisotropic_crystal")
fdtd.set("type", "anisotropic")
fdtd.set("model", "constant n")

# 设置主轴折射率（单轴晶体）
fdtd.set("ordinary refractive index", 1.55)   # 寻常光折射率
fdtd.set("extraordinary refractive index", 1.65)  # 非寻常光折射率

# 设置晶体取向（欧拉角，单位：度）
fdtd.set("rotation 1", 30)    # 绕 Z 轴旋转
fdtd.set("rotation 2", 45)    # 绕 X 轴旋转
fdtd.set("rotation 3", 0)     # 绕 Z 轴旋转

# 设置介电张量（可选，替代折射率）
# eps = [εxx, εxy, εxz; εyx, εyy, εyz; εzx, εzy, εzz]
fdtd.set("permittivity tensor", [
    2.4025, 0, 0,
    0, 2.4025, 0,
    0, 0, 2.7225
])

# 设置材料颜色
fdtd.set("color", [0.5, 0.8, 0.3, 0.8])
fdtd.set("alpha", 0.8)
```

## 注意事项

### 1. 材料类型选择
- **介电材料** (`dielectric`): 绝缘体，如 SiO₂, Si₃N₄
- **金属材料** (`metal`): 导体，如 Au, Ag, Al
- **导电材料** (`conductive`): 半导体，如 doped Si
- **各向异性材料** (`anisotropic`): 晶体，如 LiNbO₃, quartz

### 2. 材料模型选择
- **常数折射率** (`constant n`): 简单，无波长依赖性
- **Sellmeier 模型**: 准确描述透明材料的色散
- **Drude-Lorentz 模型**: 描述金属和等离子体材料
- **采样数据** (`sampled data`): 实验测量数据

### 3. 单位系统
- 波长: 米 (m)
- 频率: 赫兹 (Hz)
- 折射率: 无量纲
- 电导率: 西门子/米 (S/m)
- 介电常数: 无量纲（相对介电常数）

### 4. 材料数据库
- Lumerical 内置材料数据库包含常用材料
- 自定义材料可以保存到用户数据库
- 材料可以导入/导出为 `.mat` 文件

### 5. 性能考虑
- 复杂材料模型增加计算时间
- 色散材料需要更多内存
- 各向异性材料增加仿真复杂度

### 6. 验证建议
- 检查材料参数在仿真波长范围内的合理性
- 验证色散模型收敛性
- 测试材料界面处的数值稳定性

## 错误处理

### 常见错误
1. **无效的材料参数**
   - 解决方案：检查参数范围和单位

2. **模型不收敛**
   - 解决方案：简化材料模型或调整参数

3. **内存不足**
   - 解决方案：减少采样点数量或使用简单模型

4. **文件格式错误**（导入采样数据时）
   - 解决方案：检查数据格式和单位

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加材料
    fdtd.addmaterial()
    
    # 配置材料属性
    fdtd.set("name", "test_material")
    fdtd.set("type", "dielectric")
    fdtd.set("refractive index", 3.45)
    
except lumapi.LumApiError as e:
    print(f"材料创建失败: {e}")
    
    # 检查具体错误
    if "refractive index" in str(e).lower():
        print("错误: 无效的折射率值")
    elif "memory" in str(e).lower():
        print("错误: 内存不足")
    elif "model" in str(e).lower():
        print("错误: 材料模型不支持")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `setmaterial`: 设置对象的材料属性
- `getmaterial`: 获取材料数据
- `material`: 材料数据库操作
- `addproperty`: 添加自定义材料属性
- `import`: 导入材料数据
- `export`: 导出材料数据

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: DEVICE（电学和热学属性）
- **有限支持**: INTERCONNECT（仅基本材料属性）

## 应用场景

### 1. 光子集成电路材料
```python
# 创建硅光子材料
fdtd.addmaterial()
fdtd.set("name", "Si_photonic")
fdtd.set("type", "dielectric")
fdtd.set("model", "sellmeier")
fdtd.set("sellmeier coefficients", [10.668, 0.301, 0.003, 1.134, 1.541, 1104])
```

### 2. 金属纳米结构
```python
# 创建银纳米粒子材料
fdtd.addmaterial()
fdtd.set("name", "Ag_nanoparticle")
fdtd.set("type", "metal")
fdtd.set("model", "drude-lorentz")
fdtd.set("plasma frequency", 9.01e15)
fdtd.set("collision frequency", 3.14e13)
```

### 3. 非线性光学材料
```python
# 创建非线性晶体材料
fdtd.addmaterial()
fdtd.set("name", "LiNbO3_nonlinear")
fdtd.set("type", "anisotropic")
fdtd.set("ordinary refractive index", 2.286)
fdtd.set("extraordinary refractive index", 2.200)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增采样数据模型支持 |
| Lumerical 2019a | 改进各向异性材料性能 |
| Lumerical 2018a | 新增热学属性支持 |

## 参考

1. Lumerical 材料数据库参考手册
2. Lumerical 材料建模指南
3. Palik 光学常数手册

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*