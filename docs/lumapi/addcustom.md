# addcustom

## 概述

`addcustom` 命令用于在仿真中添加自定义监视器。自定义监视器允许用户定义特定的场量计算或数据处理，扩展了标准监视器的功能，适用于需要特殊后处理或自定义物理量监测的应用场景。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addcustom;
```

### Python API (Lumapi)
```python
session.addcustom()
```

## 参数

`addcustom` 命令没有直接参数，但需要通过后续的 `set` 命令配置自定义监视器属性。

## 配置属性

添加自定义监视器后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "custom" | 自定义监视器名称 |
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
| `dimension` | string | "3D" | 维度："3D", "2D", "1D", "0D" |

### 监视器类型选项：
- **体积监视器**: `"3D"`, `"volume"`
- **平面监视器**: `"2D X-normal"`, `"2D Y-normal"`, `"2D Z-normal"`
- **线监视器**: `"1D X-line"`, `"1D Y-line"`, `"1D Z-line"`
- **点监视器**: `"0D"`, `"point"`

### 3. 自定义脚本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `script` | string | "" | 自定义脚本代码 |
| `script language` | string | "Lumerical" | 脚本语言："Lumerical", "MATLAB" |
| `input variables` | string | "" | 输入变量定义 |
| `output variables` | string | "" | 输出变量定义 |

### 4. 记录设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `record data` | bool | true | 是否记录数据 |
| `frequency points` | int | 1 | 频率点数 |
| `frequency center` | float | 193.1e12 | 中心频率 (Hz) |
| `frequency span` | float | 100e12 | 频率范围 (Hz) |
| `override global monitor settings` | bool | false | 是否覆盖全局监视器设置 |
| `spatial interpolation` | string | "none" | 空间插值方法 |

### 5. 可视化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `enabled` | bool | true | 是否启用监视器 |
| `color` | string | "custom" | 颜色设置 |
| `opacity` | float | 0.5 | 透明度 (0-1) |
| `visualization` | string | "none" | 可视化类型 |

## 返回值

`addcustom` 命令没有返回值。成功执行后，会在仿真中添加一个自定义监视器对象。

## 示例

### 示例 1：添加基本自定义监视器
```python
import lumapi

# 创建会话
session = lumapi.FDTD()

# 添加自定义监视器
session.addcustom()

# 配置监视器属性
session.set("name", "custom_monitor_1")
session.set("monitor type", "2D X-normal")
session.set("x", 0)
session.set("y span", 2e-6)
session.set("z span", 1e-6)

# 设置自定义脚本
session.set("script", "E = getdata(\"E\");\nP = abs(E)^2;")
session.set("output variables", "P")
```

### 示例 2：自定义场量计算
```python
import lumapi

session = lumapi.FDTD()

# 添加自定义监视器用于计算能量密度
session.addcustom()
session.set("name", "energy_density")
session.set("monitor type", "3D")
session.set("x span", 3e-6)
session.set("y span", 2e-6)
session.set("z span", 1e-6)

# 自定义脚本计算电磁能量密度
custom_script = """
# 获取电场和磁场
E = getdata("E");
H = getdata("H");

# 计算能量密度
epsilon0 = 8.854e-12;
mu0 = 4*pi*1e-7;

# 电能密度
U_e = 0.5 * epsilon0 * sum(abs(E)^2, 4);

# 磁能密度  
U_h = 0.5 * mu0 * sum(abs(H)^2, 4);

# 总能量密度
U_total = U_e + U_h;
"""

session.set("script", custom_script)
session.set("output variables", "U_total;U_e;U_h")
```

## 注意事项

1. **性能影响**：自定义监视器可能增加仿真时间，特别是复杂的脚本计算
2. **内存使用**：自定义监视器记录的数据会增加内存使用
3. **脚本调试**：自定义脚本应在简单测试案例中验证后再用于复杂仿真
4. **兼容性**：确保自定义脚本语法与当前 Lumerical 版本兼容
5. **数据格式**：注意输入输出变量的数据维度匹配

## 错误处理

### 常见错误
1. **脚本语法错误**: 自定义脚本包含语法错误
   - 解决方案：在 Lumerical 脚本编辑器中验证脚本语法

2. **变量未定义**: 脚本中引用了未定义的变量
   - 解决方案：确保所有变量在脚本中正确定义或通过输入变量传递

3. **内存不足**: 自定义监视器记录数据过多
   - 解决方案：减少记录的数据量或增加内存分配

4. **监视器位置无效**: 监视器位置超出仿真区域
   - 解决方案：确保监视器坐标在仿真边界内

### Python 错误处理
```python
import lumapi

try:
    # 创建会话
    session = lumapi.FDTD()
    
    # 添加自定义监视器
    session.addcustom()
    
    # 配置监视器属性
    session.set("name", "test_custom")
    session.set("monitor type", "2D X-normal")
    session.set("script", "E = getdata(\"E\");")
    
    # 验证脚本语法
    script = session.get("script")
    if not script or len(script.strip()) == 0:
        raise ValueError("自定义脚本不能为空")
        
    # 检查监视器位置
    x_span = session.get("x span")
    if x_span <= 0:
        raise ValueError("监视器跨度必须 > 0")
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认设置
    session.set("x span", 1e-6)
    session.set("script", "# 默认空脚本")
    
except lumapi.LumApiError as e:
    print(f"自定义监视器创建失败: {e}")
    
    # 检查具体错误
    if "script" in str(e).lower() and "syntax" in str(e).lower():
        print("错误: 脚本语法错误，请检查脚本语法")
    elif "variable" in str(e).lower() and "undefined" in str(e).lower():
        print("错误: 变量未定义，请检查脚本变量")
    elif "memory" in str(e).lower():
        print("错误: 内存不足，请减少记录数据或增加内存")
    elif "position" in str(e).lower() or "boundary" in str(e).lower():
        print("错误: 监视器位置无效，请检查坐标设置")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持
- **MODE Solutions**: 支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 不支持

## 相关命令

- `addpower` - 添加功率监视器
- `addindex` - 添加折射率监视器  
- `addprofile` - 添加场监视器
- `set` - 设置对象属性
 - `getdata` - 获取监视器数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增自定义脚本支持 |
| Lumerical 2019a | 改进自定义监视器性能 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical 自定义监视器用户指南
2. Lumerical 脚本语言参考手册
3. 自定义场量计算在光子仿真中的应用

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*