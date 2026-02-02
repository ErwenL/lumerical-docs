# addemeprofile

## 概述

`addemeprofile` 命令用于在 EME（本征模式扩展）仿真中添加场监视器。EME 场监视器记录 EME 求解器计算得到的场分布，可以获取传播方向上的场剖面，用于分析模式耦合、场分布演化、传输特性等。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addemeprofile;
```

### Python API (Lumapi)
```python
session.addemeprofile()
```

## 参数

`addemeprofile` 命令没有直接参数，但需要通过后续的 `set` 命令配置监视器属性。

## 配置属性

添加 EME 场监视器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "emeprofile" | EME 场监视器名称 |
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
| `propagation axis` | string | "x" | 传播方向（与 EME 求解器一致） |

### 监视器类型选项：
- **传播剖面**: `"2D X-normal"`, `"2D Y-normal"`, `"2D Z-normal"`
- **横向剖面**: `"1D X-line"`, `"1D Y-line"`, `"1D Z-line"`

### 3. EME 特定设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `EME span` | float | 1e-6 | EME 传播方向跨度 (m) |
| `EME position` | float | 0 | 沿传播方向的位置 (m) |
| `number of modes` | int | 10 | 记录的模式数量 |
| `mode selection` | string | "all" | 模式选择："all", "guided", "radiation" |
| `include backward modes` | bool | false | 是否包含反向传播模式 |
| `field type` | string | "E" | 场类型："E"（电场）, "H"（磁场） |

### 4. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record data` | bool | true | 是否记录数据 |
| `frequency points` | int | 1 | 频率点数 |
| `frequency center` | float | 193.1e12 | 中心频率 (Hz) |
| `frequency span` | float | 100e12 | 频率范围 (Hz) |
| `override global monitor settings` | bool | false | 是否覆盖全局监视器设置 |
| `spatial interpolation` | string | "linear" | 空间插值方法 |
| `record phase` | bool | true | 是否记录相位信息 |

### 5. 场分量设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record Ex` | bool | true | 是否记录 Ex 分量 |
| `record Ey` | bool | true | 是否记录 Ey 分量 |
| `record Ez` | bool | true | 是否记录 Ez 分量 |
| `record Hx` | bool | false | 是否记录 Hx 分量 |
| `record Hy` | bool | false | 是否记录 Hy 分量 |
| `record Hz` | bool | false | 是否记录 Hz 分量 |
| `record Px` | bool | false | 是否记录 Px 分量（坡印廷矢量） |
| `record Py` | bool | false | 是否记录 Py 分量 |
| `record Pz` | bool | false | 是否记录 Pz 分量 |

### 6. 可视化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
 | `enabled` | bool | true | 是否启用监视器 |
| `color` | string | "custom" | 颜色设置 |
| `opacity` | float | 0.5 | 透明度 (0-1) |
| `visualization` | string | "field" | 可视化类型："field", "contour", "arrow" |
| `field component` | string | "Ex" | 显示的场分量 |

## 返回值

`addemeprofile` 命令没有返回值。成功执行后，会在仿真中添加一个 EME 场监视器对象。

## 示例

### 示例 1：添加基本 EME 场监视器
```python
import lumapi

# 创建会话
session = lumapi.MODE()

# 添加 EME 场监视器
session.addemeprofile()

# 配置监视器属性
session.set("name", "eme_field_profile")
session.set("monitor type", "2D X-normal")
session.set("x span", 2e-6)
session.set("y span", 1e-6)
session.set("propagation axis", "x")

# 设置 EME 特定参数
session.set("EME span", 5e-6)
session.set("EME position", 2.5e-6)  # 在传播方向中间位置
session.set("number of modes", 20)
session.set("field type", "E")
```

### 示例 2：配置多模式场记录
```python
import lumapi

session = lumapi.MODE()

# 添加 EME 场监视器
session.addemeprofile()
session.set("name", "multi_mode_profile")
session.set("x span", 3e-6)
session.set("y span", 2e-6)
session.set("monitor type", "2D Y-normal")

# 配置模式选择
session.set("number of modes", 15)
session.set("mode selection", "guided")  # 只记录导模
session.set("include backward modes", True)

# 配置场分量记录
session.set("record Ex", True)
session.set("record Ey", True)
session.set("record Ez", True)
session.set("record Hx", True)  # 同时记录磁场
session.set("record Hy", True)
session.set("record Hz", True)

# 设置频率扫描
session.set("frequency points", 50)
session.set("frequency center", 1550e12)  # 1550 nm
session.set("frequency span", 50e12)
```

### 示例 3：传播方向多个剖面
```python
import lumapi

session = lumapi.MODE()

# 在传播方向的不同位置添加多个 EME 场监视器
positions = [0, 1e-6, 2e-6, 3e-6, 4e-6]
for i, pos in enumerate(positions):
    session.addemeprofile()
    session.set("name", f"eme_profile_{i+1}")
    session.set("monitor type", "2D Z-normal")
    session.set("x span", 2e-6)
    session.set("y span", 1e-6)
    session.set("EME position", pos)  # 设置不同位置
    session.set("EME span", 5e-6)  # 总传播长度
    
    # 只记录前几个模式
    session.set("number of modes", 5)
    session.set("field type", "E")
    session.set("record Pz", True)  # 记录传播方向的功率流
```

## 错误处理

### 常见错误
1. **未找到 EME 求解器**：未添加 EME 求解器时使用 `addemeprofile`
   - 解决方案：先使用 `addeme` 命令添加 EME 求解器

2. **传播方向不匹配**：监视器传播方向与 EME 求解器设置不一致
   - 解决方案：检查并确保 `propagation axis` 与 EME 求解器设置一致

3. **位置超出范围**：`EME position` 超出 `EME span` 范围
   - 解决方案：确保监视器位置在 EME 传播长度范围内

4. **模式数量不足**：记录的模式数量少于实际需要的模式数
   - 解决方案：增加 `number of modes` 参数值

5. **内存不足**：记录过多场分量或模式导致内存不足
   - 解决方案：减少记录的分量、模式数或频率点数

### Python 错误处理
```python
import lumapi

try:
    mode = lumapi.MODE()
    
    # 添加 EME 场监视器
    mode.addemeprofile()
    
    # 配置监视器属性
    mode.set("name", "eme_profile_test")
    mode.set("monitor type", "2D X-normal")
    mode.set("propagation axis", "x")
    mode.set("EME span", 10e-6)
    mode.set("EME position", 5e-6)
    
    # 检查位置是否在范围内
    eme_span = mode.get("EME span")
    eme_position = mode.get("EME position")
    
    if eme_position < 0 or eme_position > eme_span:
        raise ValueError(f"EME position ({eme_position}m) 必须在 0 到 {eme_span}m 范围内")
    
    # 检查模式数量
    num_modes = mode.get("number of modes")
    if num_modes <= 0:
        raise ValueError("模式数量必须为正数")
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值
    mode.set("EME position", eme_span/2 if 'eme_span' in locals() else 5e-6)
    mode.set("number of modes", 10)
    
except lumapi.LumApiError as e:
    print(f"EME 场监视器创建失败: {e}")
    
    # 检查具体错误类型
    if "EME" in str(e).upper():
        print("错误: EME 求解器未找到或配置错误")
    elif "propagation" in str(e).lower():
        print("错误: 传播方向设置错误")
    elif "position" in str(e).lower():
        print("错误: 位置参数无效")
    elif "memory" in str(e).lower():
        print("错误: 内存不足，请减少模式数量或场分量")
    elif "mode" in str(e).lower():
        print("错误: 模式数量设置错误")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 注意事项

1. **EME 求解器要求**：使用 `addemeprofile` 前需要先添加 EME 求解器（`addeme`）
2. **模式收敛**：确保记录的模式数量足够覆盖感兴趣的场分布
3. **计算资源**：记录多个场分量和模式会增加内存使用和计算时间
4. **传播方向**：监视器的传播方向必须与 EME 求解器设置一致
5. **位置精度**：EME position 应在 EME span 范围内，否则无法获取有效数据

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 不支持

## 相关命令

- `addeme` - 添加 EME 求解器
- `addprofile` - 添加标准场监视器
- `addfdeprofile` - 添加 FDE 场监视器
- `set` - 设置对象属性
- `getdata` - 获取监视器数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增反向模式记录支持 |
| Lumerical 2019a | 改进场分量选择逻辑 |
| Lumerical 2018a | 首次引入 `addemeprofile` 命令 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical EME 求解器用户指南
2. 本征模式扩展方法理论
3. 波导模式耦合与传输分析

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*