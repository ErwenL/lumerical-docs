# addmodesource

## 概述

`addmodesource` 命令用于在 varFDTD（变分 FDTD）仿真中添加模式光源。varFDTD 模式光源专为变分 FDTD 求解器设计，支持高效的模式激励和参数扫描，适用于参数化设计和优化仿真。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addmodesource;
```

### Python API (Lumapi)
```python
session.addmodesource()
```

## 参数

`addmodesource` 命令没有直接参数，但需要通过后续的 `set` 命令配置光源属性。

## 配置属性

添加 varFDTD 模式光源后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "mode source" | 光源名称 |
| `enabled` | bool | true | 是否启用光源 |
| `type` | string | "varfdtd" | 光源类型（固定为 varfdtd） |
| `x`, `y`, `z` | float | 0 | 光源中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 光源各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 光源 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 光源 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 光源 Z 方向最小/最大坐标 (m) |

### 2. 光源方向与模式
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `injection axis` | string | "x" | 注入方向："x", "y", "z" |
| `direction` | string | "forward" | 传播方向："forward", "backward" |
| `mode selection` | string | "fundamental" | 模式选择 |
| `mode number` | int | 1 | 模式编号 |
| `polarization` | string | "TE" | 偏振："TE", "TM", "custom" |
| `mode calculation` | string | "auto" | 模式计算方式："auto", "manual" |

### 3. varFDTD 特定设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parameter sweep` | bool | false | 是否启用参数扫描 |
| `sweep type` | string | "linear" | 扫描类型："linear", "log", "list" |
| `parameter` | string | "wavelength" | 扫描参数："wavelength", "width", "height" |
| `start value` | float | 1.5e-6 | 起始值 |
| `stop value` | float | 1.6e-6 | 结束值 |
| `number of points` | int | 10 | 扫描点数 |
| `optimization enabled` | bool | false | 是否启用优化 |
| `sensitivity analysis` | bool | false | 是否进行灵敏度分析 |

### 4. 波长与频谱设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `wavelength span` | float | 0.1e-6 | 波长范围 (m) |
| `frequency` | float | 自动计算 | 频率 (Hz) |
| `frequency span` | float | 自动计算 | 频率范围 (Hz) |
| `spectrum type` | string | "gaussian" | 频谱类型："gaussian", "flat", "custom" |
| `bandwidth` | float | 10e12 | 带宽 (Hz) |
| `center wavelength` | float | 1.55e-6 | 中心波长 (m) |

### 5. 场分布设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `field profile` | string | "auto" | 场分布："auto", "user defined" |
| `Ex amplitude` | float | 1 | Ex 分量幅度 |
| `Ey amplitude` | float | 0 | Ey 分量幅度 |
| `Ez amplitude` | float | 0 | Ez 分量幅度 |
| `phase x` | float | 0 | X 相位 (弧度) |
| `phase y` | float | 0 | Y 相位 (弧度) |
| `phase z` | float | 0 | Z 相位 (弧度) |
| `normalization` | string | "power" | 归一化："power", "amplitude", "none" |
| `power` | float | 1e-3 | 功率 (W) |

### 6. 优化与灵敏度设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `objective function` | string | "transmission" | 目标函数："transmission", "reflection", "custom" |
| `target value` | float | 1 | 目标值 |
| `tolerance` | float | 1e-3 | 容差 |
| `design parameters` | matrix | [] | 设计参数列表 |
| `sensitivity parameters` | matrix | [] | 灵敏度参数列表 |
| `adjoint enabled` | bool | false | 是否启用伴随求解 |

### 7. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh override` | bool | false | 是否覆盖网格设置 |
| `mesh cells x` | int | 自动计算 | X 方向网格数 |
| `mesh cells y` | int | 自动计算 | Y 方向网格数 |
| `mesh cells z` | int | 自动计算 | Z 方向网格数 |
| `subpixel smoothing` | bool | true | 亚像素平滑 |
| `conformal meshing` | bool | true | 共形网格 |
| `advanced mode solver` | bool | false | 高级模式求解器 |

## 返回值

`addmodesource` 命令没有返回值。成功执行后，会在仿真中添加一个 varFDTD 模式光源对象。

## 示例

### 示例 1：添加基本 varFDTD 模式光源

#### LSF 脚本
```lumerical
// 添加 varFDTD 模式光源
addmodesource;

// 配置光源属性
set("name", "varfdtd_source");
set("injection axis", "x");
set("direction", "forward");
set("wavelength", 1.55e-6);
set("mode number", 1);  // 基模
set("polarization", "TE");

// 设置几何尺寸
set("x span", 2e-6);
set("y span", 1e-6);
set("z span", 0.5e-6);

// 配置功率
set("normalization", "power");
set("power", 1e-3);  // 1 mW
```

#### Python API
```python
import lumapi

# 创建 varFDTD 会话
session = lumapi.varFDTD()

# 添加 varFDTD 模式光源
session.addmodesource()

# 配置光源属性
session.set("name", "varfdtd_source")
session.set("injection axis", "x")
session.set("direction", "forward")
session.set("wavelength", 1.55e-6)
session.set("mode number", 1)  # 基模
session.set("polarization", "TE")

# 设置几何尺寸
session.set("x span", 2e-6)
session.set("y span", 1e-6)
session.set("z span", 0.5e-6)

# 配置功率
session.set("normalization", "power")
session.set("power", 1e-3)  # 1 mW
```

### 示例 2：参数扫描模式光源
```python
import lumapi

session = lumapi.varFDTD()

# 添加 varFDTD 模式光源
session.addmodesource()
session.set("name", "sweep_source")
session.set("injection axis", "y")

# 启用参数扫描
session.set("parameter sweep", True)
session.set("sweep type", "linear")
session.set("parameter", "wavelength")
session.set("start value", 1.5e-6)  # 1500 nm
session.set("stop value", 1.6e-6)   # 1600 nm
session.set("number of points", 21)  # 21个波长点

# 配置模式设置
session.set("mode selection", "fundamental")
session.set("polarization", "TM")
session.set("mode calculation", "auto")

# 配置高级选项
session.set("optimization enabled", False)
session.set("sensitivity analysis", True)
```

### 示例 3：优化设计中的模式光源
```python
import lumapi

session = lumapi.varFDTD()

# 添加 varFDTD 模式光源
session.addmodesource()
session.set("name", "optimization_source")
session.set("injection axis", "z")

# 配置优化设置
session.set("optimization enabled", True)
session.set("objective function", "transmission")
session.set("target value", 0.9)  # 目标透射率 90%
session.set("tolerance", 1e-4)

# 设置设计参数
session.set("design parameters", [
    ["waveguide_width", 0.5e-6, 0.3e-6, 0.7e-6],  # 名称, 初始值, 最小值, 最大值
    ["waveguide_height", 0.22e-6, 0.2e-6, 0.25e-6],
    ["gap", 0.1e-6, 0.05e-6, 0.2e-6]
])

# 配置灵敏度分析
session.set("sensitivity analysis", True)
session.set("sensitivity parameters", ["waveguide_width", "waveguide_height"])

# 配置伴随求解
session.set("adjoint enabled", True)
```

## 注意事项

1. **varFDTD 求解器**：`addmodesource` 仅适用于 varFDTD 求解器环境
2. **参数扫描**：参数扫描会显著增加仿真时间但提供更全面的分析
3. **优化收敛**：优化问题可能收敛到局部最优，需要合理设置初始值和边界
4. **计算资源**：伴随求解和灵敏度分析需要额外计算资源
5. **模式准确性**：确保模式求解器设置正确以获得准确模式分布

## 错误处理

### 常见错误
1. **求解器不匹配**: 在非 varFDTD 求解器中使用 `addmodesource`
   - 解决方案：确保在 varFDTD 求解器环境中使用该命令

2. **参数无效**: 扫描参数或优化参数设置无效
   - 解决方案：检查参数范围、类型和边界条件

3. **模式计算失败**: 无法计算指定模式
   - 解决方案：检查波导结构、材料和波长设置

4. **内存不足**: 参数扫描或优化问题过大
   - 解决方案：减少扫描点数或简化优化问题

### Python 错误处理
```python
import lumapi

try:
    # 创建 varFDTD 会话
    session = lumapi.varFDTD()
    
    # 添加 varFDTD 模式光源
    session.addmodesource()
    
    # 配置光源属性
    session.set("name", "test_source")
    session.set("injection axis", "x")
    session.set("wavelength", 1.55e-6)
    
    # 检查参数有效性
    if session.get("wavelength") <= 0:
        raise ValueError("波长必须 > 0")
    
    # 验证求解器类型
    solver_type = session.get("type")
    if solver_type != "varfdtd":
        raise ValueError("必须在 varFDTD 求解器中使用 addmodesource")
        
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认设置
    session.set("wavelength", 1.55e-6)
    
except lumapi.LumApiError as e:
    print(f"模式光源创建失败: {e}")
    
    # 检查具体错误
    if "solver" in str(e).lower() and "mismatch" in str(e).lower():
        print("错误: 求解器不匹配，请使用 varFDTD 求解器")
    elif "parameter" in str(e).lower() and "invalid" in str(e).lower():
        print("错误: 参数无效，请检查参数设置")
    elif "mode" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 模式未找到，请检查结构设置")
    elif "memory" in str(e).lower():
        print("错误: 内存不足，请减少扫描点数或简化问题")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 产品支持

- **FDTD Solutions**: 不支持
- **MODE Solutions**: 不支持
- **DEVICE**: 不支持
- **INTERCONNECT**: 不支持
- **varFDTD**: 支持

## 相关命令

- `addvarfdtd` - 添加 varFDTD 求解器
- `addmode` - 添加标准模式光源
- `addfdtd` - 添加 FDTD 求解器
- `set` - 设置对象属性
- `optimize` - 执行优化
- `getsensitivity` - 获取灵敏度数据

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2022a | 首次引入 varFDTD 模式光源 |
| 1.1 | 更新日期，完善文档格式，补充示例和错误处理 |

## 参考

1. Lumerical varFDTD 用户指南 - 光源章节
2. Lumerical 参数扫描与优化教程
3. 变分法在光子器件设计中的应用

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*