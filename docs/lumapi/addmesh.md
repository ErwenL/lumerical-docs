# addmesh

## 概述

`addmesh` 命令用于在仿真中添加局部网格覆盖区。网格覆盖区允许在特定区域细化或自定义网格设置，以在关键区域（如波导核心、材料界面、场强区域）获得更准确的仿真结果，同时在其他区域保持较粗的网格以提高计算效率。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
addmesh;
```

### Python API (Lumapi)
```python
session.addmesh()
```

## 参数

`addmesh` 命令没有直接参数，但需要通过后续的 `set` 命令配置网格覆盖区属性。

## 配置属性

添加网格覆盖区后，可以使用 `set` 命令配置以下属性：

### 1. 几何设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "mesh override" | 网格覆盖区名称 |
| `x`, `y`, `z` | float | 0 | 覆盖区中心坐标 (m) |
| `x span`, `y span`, `z span` | float | 1e-6 | 覆盖区各方向跨度 (m) |
| `x min`, `x max` | float | -0.5e-6, 0.5e-6 | 覆盖区 X 方向最小/最大坐标 (m) |
| `y min`, `y max` | float | -0.5e-6, 0.5e-6 | 覆盖区 Y 方向最小/最大坐标 (m) |
| `z min`, `z max` | float | -0.5e-6, 0.5e-6 | 覆盖区 Z 方向最小/最大坐标 (m) |

### 2. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `dx` | float | 自动计算 | X 方向网格步长 (m) |
| `dy` | float | 自动计算 | Y 方向网格步长 (m) |
| `dz` | float | 自动计算 | Z 方向网格步长 (m) |
| `override x mesh` | int | 0 | 是否覆盖 X 方向网格 (0/1) |
| `override y mesh` | int | 0 | 是否覆盖 Y 方向网格 (0/1) |
| `override z mesh` | int | 0 | 是否覆盖 Z 方向网格 (0/1) |
| `mesh cells x` | int | 自动计算 | X 方向网格细胞数 |
| `mesh cells y` | int | 自动计算 | Y 方向网格细胞数 |
| `mesh cells z` | int | 自动计算 | Z 方向网格细胞数 |

### 3. 高级网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh type` | string | "uniform" | 网格类型："uniform", "graded" |
| `grading` | float | 1.0 | 网格渐变因子（>1 表示向外变粗） |
| `symmetric grading` | int | 0 | 是否对称渐变 (0/1) |
| `minimum mesh step` | float | 1e-12 | 最小网格步长 (m) |
| `maximum mesh step` | float | 1e-6 | 最大网格步长 (m) |

### 4. 选择与过滤
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `enabled` | int | 1 | 是否启用覆盖区 (0/1) |
| `based on structure` | int | 0 | 是否基于结构自动调整 (0/1) |
| `structure list` | string | "" | 应用到的结构列表 |
| `material list` | string | "" | 应用到的材料列表 |

### 5. 显示属性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `color` | array[4] | [0.0, 0.5, 1.0, 0.3] | RGBA 颜色值 |
| `alpha` | float | 0.3 | 透明度 (0.0-1.0) |
| `visible` | int | 1 | 是否可见 |

## 返回值

`addmesh` 命令没有返回值。成功执行后，会在仿真中添加一个网格覆盖区对象。

## 示例

### 示例 1: 基本网格覆盖区

#### LSF 脚本
```lumerical
// 添加网格覆盖区
addmesh;

// 设置覆盖区几何
set("name", "waveguide_mesh_refinement");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 10e-6);   // 覆盖波导长度
set("y span", 2e-6);    // 覆盖波导宽度
set("z span", 1e-6);    // 覆盖波导高度

// 设置网格步长
set("dx", 20e-9);       // X 方向 20nm 网格
set("dy", 20e-9);       // Y 方向 20nm 网格
set("dz", 50e-9);       // Z 方向 50nm 网格

// 启用网格覆盖
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);

// 设置显示属性
set("color", [0.0, 1.0, 0.0, 0.3]);  // 绿色半透明
set("alpha", 0.3);
```

#### Python API
```python
import lumapi

# 创建会话
fdtd = lumapi.FDTD()

# 添加网格覆盖区
fdtd.addmesh()

# 设置覆盖区几何
fdtd.set("name", "waveguide_mesh_refinement")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)   # 覆盖波导长度
fdtd.set("y span", 2e-6)    # 覆盖波导宽度
fdtd.set("z span", 1e-6)    # 覆盖波导高度

# 设置网格步长
fdtd.set("dx", 20e-9)       # X 方向 20nm 网格
fdtd.set("dy", 20e-9)       # Y 方向 20nm 网格
fdtd.set("dz", 50e-9)       # Z 方向 50nm 网格

# 启用网格覆盖
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)

# 设置显示属性
fdtd.set("color", [0.0, 1.0, 0.0, 0.3])  # 绿色半透明
fdtd.set("alpha", 0.3)
```

### 示例 2: 渐变网格覆盖区

#### LSF 脚本
```lumerical
addmesh;
set("name", "graded_mesh");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5e-6);
set("y span", 3e-6);
set("z span", 1e-6);

// 使用渐变网格
set("mesh type", "graded");
set("grading", 1.5);        // 向外渐变 1.5 倍
set("symmetric grading", 1); // 对称渐变

// 设置中心区域精细网格
set("dx", 10e-9);           // 中心 X 方向 10nm
set("dy", 10e-9);           // 中心 Y 方向 10nm
set("dz", 20e-9);           // 中心 Z 方向 20nm

// 设置最大网格步长限制
set("minimum mesh step", 5e-9);
set("maximum mesh step", 100e-9);

// 启用覆盖
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmesh()
fdtd.set("name", "graded_mesh")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 5e-6)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 1e-6)

# 使用渐变网格
fdtd.set("mesh type", "graded")
fdtd.set("grading", 1.5)        # 向外渐变 1.5 倍
fdtd.set("symmetric grading", 1) # 对称渐变

# 设置中心区域精细网格
fdtd.set("dx", 10e-9)           # 中心 X 方向 10nm
fdtd.set("dy", 10e-9)           # 中心 Y 方向 10nm
fdtd.set("dz", 20e-9)           # 中心 Z 方向 20nm

# 设置最大网格步长限制
fdtd.set("minimum mesh step", 5e-9)
fdtd.set("maximum mesh step", 100e-9)

# 启用覆盖
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)
```

### 示例 3: 基于结构的网格覆盖

#### LSF 脚本
```lumerical
addmesh;
set("name", "structure_based_mesh");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 8e-6);
set("y span", 4e-6);
set("z span", 2e-6);

// 基于结构自动调整
set("based on structure", 1);

// 指定应用到特定结构
set("structure list", "waveguide1, waveguide2");

// 设置网格步长
set("dx", 15e-9);
set("dy", 15e-9);
set("dz", 30e-9);

// 仅在结构所在区域应用覆盖
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);

// 设置显示属性
set("color", [1.0, 0.5, 0.0, 0.2]);  // 橙色半透明
set("alpha", 0.2);
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmesh()
fdtd.set("name", "structure_based_mesh")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 8e-6)
fdtd.set("y span", 4e-6)
fdtd.set("z span", 2e-6)

# 基于结构自动调整
fdtd.set("based on structure", 1)

# 指定应用到特定结构
fdtd.set("structure list", "waveguide1, waveguide2")

# 设置网格步长
fdtd.set("dx", 15e-9)
fdtd.set("dy", 15e-9)
fdtd.set("dz", 30e-9)

# 仅在结构所在区域应用覆盖
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)

# 设置显示属性
fdtd.set("color", [1.0, 0.5, 0.0, 0.2])  # 橙色半透明
fdtd.set("alpha", 0.2)
```

### 示例 4: 多区域网格覆盖（复杂结构）

#### LSF 脚本
```lumerical
// 第一个覆盖区：波导核心
addmesh;
set("name", "core_mesh");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 10e-6);
set("y span", 500e-9);
set("z span", 220e-9);
set("dx", 10e-9);
set("dy", 10e-9);
set("dz", 20e-9);
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);
set("color", [0.0, 1.0, 0.0, 0.3]);

// 第二个覆盖区：耦合区域
addmesh;
set("name", "coupler_mesh");
set("x", 5e-6);      // 耦合器位置
set("y", 0);
set("z", 0);
set("x span", 2e-6);
set("y span", 3e-6);
set("z span", 500e-9);
set("dx", 5e-9);     // 更精细的网格
set("dy", 5e-9);
set("dz", 10e-9);
set("mesh type", "graded");
set("grading", 1.3);
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);
set("color", [1.0, 0.0, 0.0, 0.2]);

// 第三个覆盖区：弯曲区域
addmesh;
set("name", "bend_mesh");
set("x", -3e-6);     // 弯曲波导位置
set("y", 2e-6);
set("z", 0);
set("x span", 3e-6);
set("y span", 3e-6);
set("z span", 500e-9);
set("dx", 15e-9);
set("dy", 15e-9);
set("dz", 30e-9);
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 0);  // Z 方向不覆盖
set("color", [0.0, 0.0, 1.0, 0.2]);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 第一个覆盖区：波导核心
fdtd.addmesh()
fdtd.set("name", "core_mesh")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 10e-6)
fdtd.set("y span", 500e-9)
fdtd.set("z span", 220e-9)
fdtd.set("dx", 10e-9)
fdtd.set("dy", 10e-9)
fdtd.set("dz", 20e-9)
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)
fdtd.set("color", [0.0, 1.0, 0.0, 0.3])

# 第二个覆盖区：耦合区域
fdtd.addmesh()
fdtd.set("name", "coupler_mesh")
fdtd.set("x", 5e-6)      # 耦合器位置
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 2e-6)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 500e-9)
fdtd.set("dx", 5e-9)     # 更精细的网格
fdtd.set("dy", 5e-9)
fdtd.set("dz", 10e-9)
fdtd.set("mesh type", "graded")
fdtd.set("grading", 1.3)
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)
fdtd.set("color", [1.0, 0.0, 0.0, 0.2])

# 第三个覆盖区：弯曲区域
fdtd.addmesh()
fdtd.set("name", "bend_mesh")
fdtd.set("x", -3e-6)     # 弯曲波导位置
fdtd.set("y", 2e-6)
fdtd.set("z", 0)
fdtd.set("x span", 3e-6)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 500e-9)
fdtd.set("dx", 15e-9)
fdtd.set("dy", 15e-9)
fdtd.set("dz", 30e-9)
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 0)  # Z 方向不覆盖
fdtd.set("color", [0.0, 0.0, 1.0, 0.2])
```

### 示例 5: 使用网格细胞数而非步长

#### LSF 脚本
```lumerical
addmesh;
set("name", "cell_count_mesh");
set("x span", 5e-6);
set("y span", 3e-6);
set("z span", 1e-6);

// 使用网格细胞数定义网格密度
set("mesh cells x", 200);   // X 方向 200 个细胞
set("mesh cells y", 150);   // Y 方向 150 个细胞
set("mesh cells z", 50);    // Z 方向 50 个细胞

// 计算实际网格步长
dx = 5e-6 / 200;  // 25nm
dy = 3e-6 / 150;  // 20nm
dz = 1e-6 / 50;   // 20nm

// 启用覆盖
set("override x mesh", 1);
set("override y mesh", 1);
set("override z mesh", 1);

// 设置显示
set("color", [0.5, 0.0, 0.5, 0.3]);  // 紫色半透明
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addmesh()
fdtd.set("name", "cell_count_mesh")
fdtd.set("x span", 5e-6)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 1e-6)

# 使用网格细胞数定义网格密度
fdtd.set("mesh cells x", 200)   # X 方向 200 个细胞
fdtd.set("mesh cells y", 150)   # Y 方向 150 个细胞
fdtd.set("mesh cells z", 50)    # Z 方向 50 个细胞

# 计算实际网格步长
dx = 5e-6 / 200  # 25nm
dy = 3e-6 / 150  # 20nm
dz = 1e-6 / 50   # 20nm

# 启用覆盖
fdtd.set("override x mesh", 1)
fdtd.set("override y mesh", 1)
fdtd.set("override z mesh", 1)

# 设置显示
fdtd.set("color", [0.5, 0.0, 0.5, 0.3])  # 紫色半透明
```

## 注意事项

### 1. 网格覆盖区优先级
- 多个网格覆盖区可以重叠
- 网格步长取最精细的值
- 可以通过调整覆盖区顺序控制优先级

### 2. 性能与精度平衡
- 精细网格提高精度但增加计算时间和内存
- 粗网格提高速度但可能降低精度
- 应在关键区域使用精细网格，其他区域使用粗网格

### 3. 网格步长选择
- 网格步长应小于最小特征尺寸的 1/10
- 对于高折射率对比度界面，需要更细的网格
- 渐变结构可以使用渐变网格

### 4. 边界效应
- 网格覆盖区边界处可能出现网格不连续
- 使用渐变网格可以减少边界效应
- 确保覆盖区足够大以避免边缘效应

### 5. 验证建议
- 检查网格收敛性：逐步细化网格直到结果稳定
- 验证关键区域的网格质量
- 检查内存使用是否在合理范围内

### 6. 特殊考虑
- **各向异性材料**：可能需要不同方向的网格步长
- **金属结构**：需要非常精细的网格捕捉趋肤效应
- **非线性效应**：需要足够精细的网格捕捉场强变化

## 错误处理

### 常见错误
1. **网格步长太小导致内存不足**
   - 解决方案：增加网格步长或减少覆盖区尺寸

2. **覆盖区冲突**
   - 解决方案：检查重叠覆盖区设置，调整优先级

3. **无效的网格参数**
   - 解决方案：检查网格步长是否在合理范围内

4. **结构不在覆盖区内**
   - 解决方案：调整覆盖区位置和尺寸

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 添加网格覆盖区
    fdtd.addmesh()
    
    # 配置覆盖区属性
    fdtd.set("name", "test_mesh")
    fdtd.set("x span", 5e-6)
    fdtd.set("dx", 10e-9)
    fdtd.set("override x mesh", 1)
    
except lumapi.LumApiError as e:
    print(f"网格覆盖区创建失败: {e}")
    
    # 检查具体错误
    if "memory" in str(e).lower():
        print("错误: 内存不足，请增加网格步长")
    elif "mesh" in str(e).lower() and "invalid" in str(e).lower():
        print("错误: 无效的网格参数")
    elif "overlap" in str(e).lower():
        print("错误: 覆盖区冲突")
    else:
        print(f"未知错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 相关命令

- `mesh`: 网格操作命令
- `grid`: 设置全局网格
- `cleargrid`: 清除网格设置
- `subcell`: 子网格设置（MODE）
- `set`: 设置对象属性
- `get`: 获取网格信息

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: DEVICE（热网格覆盖）
- **不支持**: INTERCONNECT

## 应用场景

### 1. 波导模式分析
```python
# 在波导核心区域细化网格
fdtd.addmesh()
fdtd.set("x span", 10e-6)
fdtd.set("y span", 500e-9)
fdtd.set("z span", 220e-9)
fdtd.set("dx", 10e-9)
fdtd.set("dy", 10e-9)
fdtd.set("dz", 20e-9)
```

### 2. 光子晶体结构
```python
# 在光子晶体孔洞区域细化网格
fdtd.addmesh()
fdtd.set("x span", 5e-6)
fdtd.set("y span", 5e-6)
fdtd.set("mesh type", "graded")
fdtd.set("grading", 1.2)
fdtd.set("dx", 5e-9)  # 非常精细的网格
```

### 3. 金属纳米结构
```python
# 在金属纳米颗粒表面细化网格
fdtd.addmesh()
fdtd.set("x span", 200e-9)
fdtd.set("y span", 200e-9)
fdtd.set("z span", 100e-9)
fdtd.set("dx", 1e-9)  # 1nm 网格捕捉趋肤效应
fdtd.set("dy", 1e-9)
fdtd.set("dz", 2e-9)
```

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增渐变网格支持 |
| Lumerical 2019a | 改进基于结构的网格调整 |
| Lumerical 2018a | 新增多方向独立覆盖支持 |

## 参考

1. Lumerical 网格设置指南
2. Lumerical 最佳实践：网格收敛性分析
3. 有限差分法网格优化文献

---

*最后更新: 2025-01-30*  
*文档版本: 1.0*