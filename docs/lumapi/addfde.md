# addfde

## 概述

`addfde` 命令用于在 MODE Solutions 仿真中添加一个 FDE（频域求解器）区域。FDE 求解器用于计算波导中的本征模式，包括模式场分布、有效折射率、损耗等特性。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addfde;
```

### Python API (Lumapi)
```python
session.addfde()
```

## 参数

`addfde` 命令没有直接参数，但需要通过后续的 `set` 命令配置求解器属性。

## 配置属性

添加 FDE 求解器后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x`, `y`, `z` | float | 0 | 仿真区域中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 仿真区域跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 仿真区域最小/最大坐标 (m) |
| `dimension` | string | "3D" | 仿真维度："3D" 或 "2D" |

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
| `dx`, `dy`, `dz` | float | 自动计算 | 网格步长 (m) |

### 4. 求解器设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `solver type` | string | "2D Z normal" | 求解器类型 |
| `number of trial modes` | int | 4 | 计算的模式数量 |
| `search` | string | "max index" | 模式搜索方法 |
| `wavelength` | float | 1.55e-6 | 波长 (m) |
| `background index` | float | 1.0 | 背景折射率 |
| `group index calculation` | int | 0 | 是否计算群折射率 |

### 5. 模式选择
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `selected mode numbers` | string | "1" | 选择的模式编号 |
| `polarization` | string | "TE" | 偏振态："TE", "TM", "undefined" |

## 返回值

`addfde` 命令没有返回值。成功执行后，会在仿真中添加一个 FDE 求解器对象。

## 示例

### 示例 1: 基本 FDE 求解器设置

#### LSF 脚本
```lumerical
// 添加 FDE 求解器
addfde;

// 设置几何参数
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 2e-6);
set("y span", 2e-6);
set("z span", 2e-6);

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");
set("z min bc", "PML");
set("z max bc", "PML");
set("pml layers", 10);

// 设置求解器参数
set("wavelength", 1.55e-6);
set("number of trial modes", 6);
set("solver type", "3D");
set("background index", 1.444);  // 二氧化硅背景

// 设置网格
set("mesh accuracy", 3);
```

#### Python API
```python
import lumapi

# 创建 MODE 会话
mode = lumapi.MODE()

# 添加 FDE 求解器
mode.addfde()

# 设置几何参数
mode.set("x", 0)
mode.set("y", 0)
mode.set("z", 0)
mode.set("x span", 2e-6)
mode.set("y span", 2e-6)
mode.set("z span", 2e-6)

# 设置边界条件
mode.set("x min bc", "PML")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")
mode.set("z min bc", "PML")
mode.set("z max bc", "PML")
mode.set("pml layers", 10)

# 设置求解器参数
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 6)
mode.set("solver type", "3D")
mode.set("background index", 1.444)  # 二氧化硅背景

# 设置网格
mode.set("mesh accuracy", 3)
```

### 示例 2: 2D 波导模式分析

#### LSF 脚本
```lumerical
addfde;
set("solver type", "2D Z normal");
set("x span", 1.5e-6);
set("y span", 1.5e-6);
set("z span", 0);  // 2D 仿真 Z 方向跨度为 0

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");

// 设置波长和模式数
set("wavelength", 1.55e-6);
set("number of trial modes", 10);

// 设置偏振
set("polarization", "TE");

// 设置网格
set("mesh accuracy", 4);
set("mesh cells x", 150);
set("mesh cells y", 150);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addfde()
mode.set("solver type", "2D Z normal")
mode.set("x span", 1.5e-6)
mode.set("y span", 1.5e-6)
mode.set("z span", 0)  # 2D 仿真 Z 方向跨度为 0

# 设置边界条件
mode.set("x min bc", "PML")
mode.set("x max bc", "PML")
mode.set("y min bc", "PML")
mode.set("y max bc", "PML")

# 设置波长和模式数
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 10)

# 设置偏振
mode.set("polarization", "TE")

# 设置网格
mode.set("mesh accuracy", 4)
mode.set("mesh cells x", 150)
mode.set("mesh cells y", 150)
```

### 示例 3: 对称边界条件优化计算

#### LSF 脚本
```lumerical
addfde;
set("x span", 2e-6);
set("y span", 2e-6);
set("z span", 2e-6);

// 使用对称边界条件减少计算量
set("x min bc", "Symmetric");
set("x max bc", "PML");
set("y min bc", "Symmetric");
set("y max bc", "PML");

// 设置求解器参数
set("wavelength", 1.31e-6);
set("number of trial modes", 4);
set("search", "near n");

// 设置背景折射率为硅
set("background index", 3.45);

// 设置群折射率计算
set("group index calculation", 1);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addfde()
mode.set("x span", 2e-6)
mode.set("y span", 2e-6)
mode.set("z span", 2e-6)

# 使用对称边界条件减少计算量
mode.set("x min bc", "Symmetric")
mode.set("x max bc", "PML")
mode.set("y min bc", "Symmetric")
mode.set("y max bc", "PML")

# 设置求解器参数
mode.set("wavelength", 1.31e-6)
mode.set("number of trial modes", 4)
mode.set("search", "near n")

# 设置背景折射率为硅
mode.set("background index", 3.45)

# 设置群折射率计算
mode.set("group index calculation", 1)
```

### 示例 4: 高级网格设置和模式选择

#### LSF 脚本
```lumerical
addfde;
set("x span", 3e-6);
set("y span", 3e-6);
set("z span", 1e-6);

// 自定义网格设置
set("define x mesh by", "maximum mesh step");
set("define y mesh by", "maximum mesh step");
set("define z mesh by", "maximum mesh step");
set("dx", 20e-9);  // X 方向最大网格步长 20nm
set("dy", 20e-9);  // Y 方向最大网格步长 20nm
set("dz", 50e-9);  // Z 方向最大网格步长 50nm

// 设置求解器
set("wavelength", 1.55e-6);
set("number of trial modes", 12);

// 选择特定模式进行分析
set("selected mode numbers", "1,3,5");

// 设置高级搜索参数
set("search", "max index");
set("target effective index", 2.5);
```

#### Python API
```python
mode = lumapi.MODE()
mode.addfde()
mode.set("x span", 3e-6)
mode.set("y span", 3e-6)
mode.set("z span", 1e-6)

# 自定义网格设置
mode.set("define x mesh by", "maximum mesh step")
mode.set("define y mesh by", "maximum mesh step")
mode.set("define z mesh by", "maximum mesh step")
mode.set("dx", 20e-9)  # X 方向最大网格步长 20nm
mode.set("dy", 20e-9)  # Y 方向最大网格步长 20nm
mode.set("dz", 50e-9)  # Z 方向最大网格步长 50nm

# 设置求解器
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 12)

# 选择特定模式进行分析
mode.set("selected mode numbers", "1,3,5")

# 设置高级搜索参数
mode.set("search", "max index")
mode.set("target effective index", 2.5)
```

## 注意事项

### 1. 仿真区域大小
- FDE 仿真区域应足够大以包含整个波导结构和模式场
- 通常需要在波导周围留出足够空间以避免边界反射
- 对于泄露模式，需要更大的仿真区域

### 2. 网格设置
- 网格精度直接影响模式计算的准确性
- 对于高折射率对比度结构，需要更细的网格
- 可以使用非均匀网格在波导核心区域细化

### 3. 边界条件选择
- **PML**: 吸收边界条件，适合大多数情况
- **Metal**: 完美电导体边界
- **Periodic**: 周期性边界条件，用于光子晶体
- **Symmetric/Anti-symmetric**: 对称边界条件，可减少计算量

### 4. 波长设置
- 波长影响模式的有效折射率
- 对于宽带分析，需要扫描多个波长点
- 波长单位是米 (m)

### 5. 模式搜索
- `search` 参数控制模式搜索方法：
  - `max index`: 搜索最高有效折射率模式
  - `near n`: 搜索接近指定折射率的模式
  - `min loss`: 搜索最低损耗模式

### 6. 内存要求
FDE 求解器内存使用与网格细胞数成正比，但通常比 FDTD 少。

## 错误处理

### 常见错误
1. **内存不足**: 网格太密或仿真区域太大
   - 解决方案：减小网格密度或仿真区域

2. **模式收敛失败**: 无法找到收敛的模式
   - 解决方案：调整搜索参数，增加 `number of trial modes`

3. **边界反射影响**: PML 设置不当
   - 解决方案：增加 PML 层数或调整 PML 参数

4. **无效的求解器类型**: 不支持的 `solver type`
   - 解决方案：检查 `solver type` 是否为有效值

### Python 错误处理
```python
import lumapi

try:
    mode = lumapi.MODE()
    mode.addfde()
    
    # 配置求解器
    mode.set("x span", 2e-6)
    mode.set("wavelength", 1.55e-6)
    mode.set("number of trial modes", 6)
    
    # 运行模式求解
    mode.findmodes()
    
except Exception as e:
    print(f"FDE 求解器设置失败: {e}")
    
    # 检查具体错误
    if "memory" in str(e).lower():
        print("错误: 内存不足，请减小网格或仿真区域")
    elif "converge" in str(e).lower():
        print("错误: 模式未收敛，请调整搜索参数")
    elif "solver type" in str(e).lower():
        print("错误: 无效的求解器类型")
    else:
        print(f"未知错误: {e}")
```

## 相关命令

- `findmodes`: 运行模式求解
- `modedata`: 获取模式数据
- `modeoverlap`: 计算模式重叠积分
- `selectmode`: 选择特定模式
- `addfdevar`: 添加变分 FDE 求解器
- `setglobalmonitor`: 设置全局监视器

## 产品支持

- **主要支持**: MODE Solutions
- **可选支持**: FDTD Solutions (部分功能)
- **不支持**: DEVICE, INTERCONNECT

## 应用场景

### 1. 波导模式分析
```python
# 分析硅波导模式
mode.addfde()
mode.set("solver type", "2D Z normal")
mode.set("x span", 2e-6)
mode.set("y span", 2e-6)
mode.set("wavelength", 1.55e-6)
mode.set("number of trial modes", 10)
mode.findmodes()
```

### 2. 耦合器设计
```python
# 分析定向耦合器模式
mode.addfde()
mode.set("solver type", "3D")
mode.set("x span", 4e-6)
mode.set("y span", 2e-6)
mode.set("z span", 0.5e-6)
mode.set("number of trial modes", 8)
mode.set("polarization", "TE")
```

### 3. 光子晶体分析
```python
# 分析光子晶体平板模式
mode.addfde()
mode.set("solver type", "3D")
mode.set("x span", 5e-6)
mode.set("y span", 5e-6)
mode.set("z span", 0.3e-6)
mode.set("x min bc", "Periodic")
mode.set("x max bc", "Periodic")
mode.set("y min bc", "Periodic")
mode.set("y max bc", "Periodic")
```

## 版本历史

| 版本 | 修改 |
|------|------|
| MODE 2020a | 新增 `group index calculation` 参数 |
| MODE 2019a | 改进模式搜索算法 |
| MODE 2018a | 新增对称边界条件支持 |

## 参考

1. Lumerical MODE Solutions 用户手册
2. Lumerical 知识库: FDE 求解器最佳实践
3. Lumerical 论坛: 模式分析技巧

---

*最后更新: 2026-01-31*  
*文档版本: 1.0*