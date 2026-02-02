# addeme

## 概述

`addeme` 命令用于在 MODE Solutions 仿真中添加一个 EME（本征模式扩展）求解器区域。EME 求解器通过将波导分解为多个截面并计算每个截面的模式，然后通过模式匹配计算整个结构的传输特性。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addeme;
```

### Python API (Lumapi)
```python
session.addeme()
```

## 参数

`addeme` 命令没有直接参数，但需要通过后续的 `set` 命令配置求解器属性。

## 配置属性

添加 EME 求解器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 仿真区域中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 仿真区域跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `propagation axis` | string | "x" | 传播方向："x", "y", "z" |

### 2. 边界条件
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x min bc`, `x max bc` | string | "PML" | X 方向边界条件 |
| `y min bc`, `y max bc` | string | "PML" | Y 方向边界条件 |
| `z min bc`, `z max bc` | string | "PML" | Z 方向边界条件 |
| `pml layers` | int | 8 | PML 层数 |
| `pml type` | string | "standard" | PML 类型 |

### 3. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh accuracy` | int | 2 | 网格精度 (1-8) |
| `mesh cells x`, `mesh cells y`, `mesh cells z` | int | 自动计算 | 各方向网格细胞数 |
| `min mesh step` | float | 1e-12 | 最小网格步长 (m) |
| `max mesh step` | float | 1e-6 | 最大网格步长 (m) |

### 4. EME 求解器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `number of trial modes` | int | 4 | 每个截面的模式数量 |
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `background index` | float | 1.0 | 背景折射率 |
| `group index calculation` | int | 0 | 是否计算群折射率 |
| `eme type` | string | "3D" | EME 类型："3D" 或 "2D" |

### 5. 截面设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `number of sections` | int | 1 | 截面数量 |
| `section spans` | string | "" | 各截面跨度 (m) |
| `section positions` | string | "" | 各截面位置 (m) |

### 6. 模式选择
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `selected mode numbers` | string | "1" | 选择的模式编号 |
| `polarization` | string | "TE" | 偏振态："TE", "TM", "undefined" |

## 返回值

`addeme` 命令没有返回值。成功执行后，会在仿真中添加一个 EME 求解器对象。

## 示例

### 示例 1: 基本 EME 求解器设置

#### LSF 脚本
```lumerical
// 添加 EME 求解器
addeme;

// 设置几何参数
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5e-6);  // 传播方向长度
set("y span", 2e-6);
set("z span", 2e-6);
set("propagation axis", "x");

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");
set("z min bc", "PML");
set("z max bc", "PML");

// 设置求解器参数
set("wavelength", 1.55e-6);
set("number of trial modes", 8);
set("eme type", "3D");
set("background index", 1.444);

// 设置网格
set("mesh accuracy", 3);
```

#### Python API
```python
import lumapi

# 创建 MODE 会话
mode = lumapi.MODE()

# 添加 EME 求解器
mode.addeme()

# 设置几何参数
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("x span", 5e-6)  # 传播方向长度
mode.set("y span", 2e-6)
mode.set("z span", 2e-6)
mode.set("propagation axis", "x")

# 设置边界条件
mode.set("x min bc", "PML")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")
mode.set("z min bc", "PML")
mode.set("z max bc", "PML")

# 设置求解器参数
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 8)
mode.set("eme type", "3D")
mode.set("background index", 1.444)

# 设置网格
mode.set("mesh accuracy", 3)
```

### 示例 2: 多截面波导分析

#### LSF 脚本
```lumerical
addeme;
set("propagation axis", "x");
set("x span", 10e-6);  // 总长度 10μm
set("y span", 2e-6);
set("z span", 1e-6);

// 设置 3 个截面
set("number of sections", 3);
set("section positions", "-5e-6, 0, 5e-6");
set("section spans", "2e-6, 3e-6, 2e-6");

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");

// 设置求解器参数
set("wavelength", 1.31e-6);
set("number of trial modes", 12);
set("eme type", "3D");

// 设置网格
set("mesh accuracy", 4);
set("mesh cells y", 100);
set("mesh cells z", 50);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addeme()
mode.set("propagation axis", "x")
mode.set("x span", 10e-6)  # 总长度 10μm
mode.set("y span", 2e-6)
mode.set("z span", 1e-6)

# 设置 3 个截面
mode.set("number of sections", 3)
mode.set("section positions", "-5e-6, 0, 5e-6")
mode.set("section spans", "2e-6, 3e-6, 2e-6")

# 设置边界条件
mode.set("x min bc", "PML")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")

# 设置求解器参数
mode.set("wavelength", 1.31e-6)
mode.set("number of trial modes", 12)
mode.set("eme type", "3D")

# 设置网格
mode.set("mesh accuracy", 4)
mode.set("mesh cells y", 100)
mode.set("mesh cells z", 50)
```

### 示例 3: 2D EME 分析

#### LSF 脚本
```lumerical
addeme;
set("eme type", "2D");
set("propagation axis", "x");
set("x span", 8e-6);
set("y span", 2e-6);
set("z span", 0);  // 2D 仿真 Z 方向跨度为 0

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");

// 设置求解器参数
set("wavelength", 1.55e-6);
set("number of trial modes", 20);
set("polarization", "TE");

// 设置 5 个截面
set("number of sections", 5);
set("section positions", "-4e-6, -2e-6, 0, 2e-6, 4e-6");
set("section spans", "1e-6, 1.5e-6, 2e-6, 1.5e-6, 1e-6");
```

#### Python API
```python
mode = lumapi.MODE()
mode.addeme()
mode.set("eme type", "2D")
mode.set("propagation axis", "x")
mode.set("x span", 8e-6)
mode.set("y span", 2e-6)
mode.set("z span", 0)  # 2D 仿真 Z 方向跨度为 0

# 设置边界条件
mode.set("x min bc", "PML")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")

# 设置求解器参数
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 20)
mode.set("polarization", "TE")

# 设置 5 个截面
mode.set("number of sections", 5)
mode.set("section positions", "-4e-6, -2e-6, 0, 2e-6, 4e-6")
mode.set("section spans", "1e-6, 1.5e-6, 2e-6, 1.5e-6, 1e-6")
```

### 示例 4: 高级 EME 设置

#### LSF 脚本
```lumerical
addeme;
set("propagation axis", "y");
set("x span", 3e-6);
set("y span", 6e-6);  // 传播方向
set("z span", 1.5e-6);

// 设置边界条件
set("x min bc", "Symmetric");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");
set("z min bc", "Symmetric");
set("z max bc", "PML");

// 设置求解器参数
set("wavelength", 1.55e-6);
set("number of trial modes", 15);
set("background index", 3.45);  // 硅背景

// 设置群折射率计算
set("group index calculation", 1);

// 设置自定义截面
set("number of sections", 4);
set("section positions", "-3e-6, -1e-6, 1e-6, 3e-6");
set("section spans", "1e-6, 2e-6, 2e-6, 1e-6");

// 设置高级网格
set("mesh accuracy", 5);
set("min mesh step", 5e-9);
set("max mesh step", 100e-9);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addeme()
mode.set("propagation axis", "y")
mode.set("x span", 3e-6)
mode.set("y span", 6e-6)  # 传播方向
mode.set("z span", 1.5e-6)

# 设置边界条件
mode.set("x min bc", "Symmetric")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")
mode.set("z min bc", "Symmetric")
mode.set("z max bc", "PML")

# 设置求解器参数
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 15)
mode.set("background index", 3.45)  # 硅背景

# 设置群折射率计算
mode.set("group index calculation", 1)

# 设置自定义截面
mode.set("number of sections", 4)
mode.set("section positions", "-3e-6, -1e-6, 1e-6, 3e-6")
mode.set("section spans", "1e-6, 2e-6, 2e-6, 1e-6")

# 设置高级网格
mode.set("mesh accuracy", 5)
mode.set("min mesh step", 5e-9)
mode.set("max mesh step", 100e-9)
```

## 注意事项

### 1. 传播方向
- `propagation axis` 定义模式传播的方向
- 截面沿传播方向排列
- 传播方向的边界条件通常设置为 PML

### 2. 截面设置
- 截面数量影响计算精度和速度
- 截面应足够多以准确描述结构变化
- 截面位置和跨度应根据实际结构设置

### 3. 模式数量
- `number of trial modes` 应足够多以包含所有重要模式
- 过多的模式会增加计算时间
- 通常 10-20 个模式对于大多数应用足够

### 4. 边界条件
- 横向边界条件影响模式计算
- 对称边界条件可减少计算量
- PML 边界条件适合大多数情况

### 5. 网格设置
- 网格精度影响模式计算的准确性
- 对于高折射率对比度结构，需要更细的网格
- 可以使用非均匀网格在关键区域细化

### 6. EME 与 FDE 比较
- **EME**: 适合长距离传播、渐变结构、多截面分析
- **FDE**: 适合单个截面模式分析、本征值问题
- **选择依据**: 根据问题类型选择合适求解器

## 错误处理

### 常见错误
1. **内存不足**: 模式数量太多或网格太密
   - 解决方案：减少模式数量或降低网格精度

2. **截面设置错误**: 截面位置或跨度无效
   - 解决方案：检查截面位置是否在仿真区域内

3. **模式收敛失败**: 无法找到收敛的模式
   - 解决方案：增加模式数量或调整搜索参数

4. **传播方向错误**: `propagation axis` 设置不当
   - 解决方案：检查传播方向是否与截面设置一致

### Python 错误处理
```python
import lumapi

try:
    mode = lumapi.MODE()
    mode.addeme()
    
    # 配置求解器
    mode.set("propagation axis", "x")
    mode.set("x span", 5e-6)
    mode.set("number of sections", 3)
    
    # 运行 EME 求解
    mode.findmodes()
    
except Exception as e:
    print(f"EME 求解器设置失败: {e}")
    
    # 检查具体错误
    if "section" in str(e).lower():
        print("错误: 截面设置无效，请检查位置和跨度")
    elif "propagation" in str(e).lower():
        print("错误: 传播方向设置错误")
    elif "memory" in str(e).lower():
        print("错误: 内存不足，请减少模式或截面数量")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `findmodes`: 运行模式求解
- `modedata`: 获取模式数据
- `modeoverlap`: 计算模式重叠积分
- `emepropagate`: 运行 EME 传播计算
- `addfde`: 添加 FDE 求解器
- `setglobalmonitor`: 设置全局监视器

## 产品支持

- **主要支持**: MODE Solutions
- **可选支持**: FDTD Solutions (部分功能)
- **不支持**: DEVICE, INTERCONNECT

## 应用场景

### 1. 锥形波导分析
```python
# 分析锥形波导传输
mode.addeme()
mode.set("propagation axis", "x")
mode.set("x span", 20e-6)
mode.set("number of sections", 10)
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 15)
```

### 2. 多模干涉耦合器
```python
# 分析 MMI 耦合器
mode.addeme()
mode.set("propagation axis", "x")
mode.set("x span", 50e-6)
mode.set("y span", 10e-6)
mode.set("number of sections", 20)
mode.set("number of trial modes", 25)
```

### 3. 光子晶体波导
```python
# 分析光子晶体波导传输
mode.addeme()
mode.set("propagation axis", "x")
mode.set("x span", 30e-6)
mode.set("number of sections", 15)
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 30)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| MODE 2020a | 新增 `group index calculation` 参数 |
| MODE 2019a | 改进多截面处理性能 |
| MODE 2018a | 新增 2D EME 支持 |

## 参考

1. Lumerical MODE Solutions 用户手册
2. Lumerical 知识库: EME 求解器最佳实践
3. Lumerical 论坛: EME 传播分析技巧

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*