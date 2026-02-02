# addfdeprofile

## 概述

`addfdeprofile` 命令用于在 FDE（频域求解器）仿真中添加场监视器。FDE 场监视器记录 FDE 求解器计算得到的本征模式场分布，可以获取模式电场、磁场、坡印廷矢量等场量，用于分析模式特性、场分布、能量局域化等。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addfdeprofile;
```

### Python API (Lumapi)
```python
session.addfdeprofile()
```

## 参数

`addfdeprofile` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加 FDE 场监视器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "fdeprofile" | FDE 场监视器名称 |
| `x`, `y`, `z` | float | 0 | 监视器中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 监视器各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 监视器 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 监视器 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 监视器 Z 方向最小/最大坐标 (m) |

### 2. 监视器类型与方向
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `monitor type` | string | "2D X-normal" | 监视器类型 |
| `normal direction` | string | "x" | 法线方向："x", "y", "z" |
| `dimension` | string | "2D" | 维度："2D", "1D" |
| `plane position` | float | 0 | 平面位置（沿法线方向） |

### 监视器类型选项：
- **横截面**: `"2D X-normal"`, `"2D Y-normal"`, `"2D Z-normal"`
- **线扫描**: `"1D X-line"`, `"1D Y-line"`, `"1D Z-line"`

### 3. FDE 模式设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mode number` | int | 1 | 模式编号（从 1 开始） |
| `polarization` | string | "TE" | 偏振类型："TE", "TM", "hybrid" |
| `effective index` | float | 自动计算 | 有效折射率（只读） |
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `frequency` | float | 自动计算 | 频率 (Hz) |
| `propagation direction` | string | "+z" | 传播方向："+z", "-z" |

### 4. 场分量设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record Ex` | bool | true | 是否记录 Ex 分量 |
| `record Ey` | bool | true | 是否记录 Ey 分量 |
| `record Ez` | bool | true | 是否记录 Ez 分量 |
| `record Hx` | bool | false | 是否记录 Hx 分量 |
| `record Hy` | bool | false | 是否记录 Hy 分量 |
| `record Hz` | bool | false | 是否记录 Hz 分量 |
| `record n` | bool | false | 是否记录折射率分布 |
| `record epsilon` | bool | false | 是否记录介电常数分布 |
| `record Poynting` | bool | false | 是否记录坡印廷矢量 |

### 5. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record data` | bool | true | 是否记录数据 |
| `data format` | string | "complex" | 数据格式："complex", "amplitude", "phase" |
| `normalization` | string | "power" | 归一化方式："power", "peak", "none" |
| `power normalization` | float | 1 | 功率归一化值 (W) |
| `spatial interpolation` | string | "linear" | 空间插值方法 |
| `sampling` | string | "uniform" | 采样方式："uniform", "non-uniform" |

### 6. 可视化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `enabled` | bool | true | 是否启用监视器 |
| `color` | string | "custom" | 颜色设置 |
| `opacity` | float | 0.5 | 透明度 (0-1) |
| `visualization` | string | "field" | 可视化类型："field", "contour", "vector" |
| `field component` | string | "Ex" | 显示的场分量 |
| `scale` | string | "linear" | 缩放方式："linear", "log" |
| `colormap` | string | "hot" | 颜色映射 |

### 7. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
 | `override mesh` | bool | false | 是否覆盖网格设置 |
| `mesh cells x` | int | 自动计算 | X 方向网格细胞数 |
| `mesh cells y` | int | 自动计算 | Y 方向网格细胞数 |
| `mesh cells z` | int | 自动计算 | Z 方向网格细胞数 |
| `subpixel smoothing` | bool | true | 是否启用亚像素平滑 |
| `material averaging` | string | "default" | 材料平均方法 |

## 返回值

`addfdeprofile` 命令没有返回值。成功执行后，会在仿真中添加一个 FDE 场监视器对象。

## 示例

### 示例 1：添加基本 FDE 场监视器
```python
import lumapi

# 创建 MODE 会话
session = lumapi.MODE()

# 添加 FDE 场监视器
session.addfdeprofile()

# 配置监视器属性
session.set("name", "fundamental_mode")
session.set("monitor type", "2D X-normal")
session.set("x span", 2e-6)
session.set("y span", 1e-6)
session.set("mode number", 1)  # 基模
session.set("polarization", "TE")

# 配置场分量记录
session.set("record Ex", True)
session.set("record Ey", True)
session.set("record Ez", False)
session.set("record Poynting", True)  # 记录功率流
```

### 示例 2：多模式场比较
```python
import lumapi

session = lumapi.MODE()

# 添加多个 FDE 场监视器记录不同模式
for mode_idx in range(1, 6):  # 前 5 个模式
    session.addfdeprofile()
    session.set("name", f"mode_{mode_idx}")
    session.set("monitor type", "2D Y-normal")
    session.set("x span", 3e-6)
    session.set("z span", 2e-6)
    session.set("mode number", mode_idx)
    
    # 配置不同偏振
    if mode_idx % 2 == 0:
        session.set("polarization", "TE")
    else:
        session.set("polarization", "TM")
    
    # 记录完整场信息
    session.set("record Ex", True)
    session.set("record Ey", True)
    session.set("record Ez", True)
    session.set("record Hx", True)
    session.set("record Hy", True)
    session.set("record Hz", True)
    
    # 设置归一化
    session.set("normalization", "power")
    session.set("power normalization", 1e-3)  # 1 mW
```

### 示例 3：波长扫描场监视器
```python
import lumapi

session = lumapi.MODE()

# 添加 FDE 场监视器
session.addfdeprofile()
session.set("name", "wavelength_sweep")
session.set("monitor type", "2D Z-normal")
session.set("x span", 2.5e-6)
session.set("y span", 1.5e-6)

# 配置波长扫描
wavelengths = [1.3e-6, 1.4e-6, 1.5e-6, 1.6e-6]  # 不同波长
for i, wl in enumerate(wavelengths):
    # 可以在此处更新波长并重新计算
    session.set("wavelength", wl)
    session.set("mode number", 1)  # 基模
    
    # 记录特定波长的场分布
    session.set("record data", True)
    session.set("data format", "complex")
```

## 错误处理

### 常见错误
1. **未找到 FDE 求解器**：未添加 FDE 求解器时使用 `addfdeprofile`
   - 解决方案：先使用 `addfde` 命令添加 FDE 求解器

2. **模式编号无效**：`mode number` 超出已计算模式范围
   - 解决方案：确保模式编号在有效范围内，增加 FDE 求解器的模式数量

3. **波长超出范围**：设置的波长不在材料色散范围内
   - 解决方案：检查材料在目标波长的光学属性，调整波长值

4. **网格分辨率不足**：场分布细节受网格限制
   - 解决方案：细化网格，特别是高折射率对比区域

5. **内存不足**：记录过多场分量或模式导致内存不足
   - 解决方案：减少记录的分量、使用数据压缩、增加虚拟内存

### Python 错误处理
```python
import lumapi

try:
    mode = lumapi.MODE()
    
    # 添加 FDE 场监视器
    mode.addfdeprofile()
    
    # 配置监视器属性
    mode.set("name", "fde_profile_test")
    mode.set("monitor type", "2D X-normal")
    mode.set("mode number", 1)
    mode.set("wavelength", 1.55e-6)
    
    # 检查模式编号有效性
    mode_num = mode.get("mode number")
    if mode_num <= 0:
        raise ValueError("模式编号必须为正整数")
    
    # 检查波长有效性
    wavelength = mode.get("wavelength")
    if wavelength <= 0:
        raise ValueError("波长必须为正数")
    
    # 检查 FDE 求解器是否存在
    # 注意：实际应用中需要检查 FDE 求解器是否已添加
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值
    mode.set("mode number", 1)
    mode.set("wavelength", 1.55e-6)
    
except lumapi.LumApiError as e:
    print(f"FDE 场监视器创建失败: {e}")
    
    # 检查具体错误类型
    if "FDE" in str(e).upper():
        print("错误: FDE 求解器未找到或配置错误")
    elif "mode" in str(e).lower():
        print("错误: 模式编号无效或超出范围")
    elif "wavelength" in str(e).lower():
        print("错误: 波长设置无效")
    elif "memory" in str(e).lower():
        print("错误: 内存不足，请减少场分量或使用数据压缩")
    elif "mesh" in str(e).lower():
        print("错误: 网格分辨率不足，请细化网格")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **FDE 求解器要求**：使用 `addfdeprofile` 前需要先添加 FDE 求解器（`addfde`）
2. **模式收敛**：确保 FDE 求解器计算了足够多的模式
3. **网格分辨率**：场分布精度受网格分辨率影响，需要合理设置
4. **内存使用**：记录多个场分量和模式会增加内存使用
5. **归一化**：功率归一化确保不同模式间可比性

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 不支持

## 相关命令

- `addfde` - 添加 FDE 求解器
- `addprofile` - 添加标准场监视器
- `addemeprofile` - 添加 EME 场监视器
- `set` - 设置对象属性
- `getdata` - 获取监视器数据
- `findmodes` - 查找模式

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增坡印廷矢量记录支持 |
| Lumerical 2019a | 改进模式选择算法 |
| Lumerical 2018a | 首次引入 `addfdeprofile` 命令 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical MODE Solutions FDE 求解器指南
2. 波导模式理论与分析方法
3. 本征模式场分布计算

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*