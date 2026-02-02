# set

## 概述

`set` 命令是 Lumerical 脚本中最核心和最重要的命令之一，用于设置仿真对象的各种属性。几乎所有仿真对象（几何结构、求解器、监视器、光源等）的配置都需要通过 `set` 命令完成。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
set(property_name, value);
set(property_name, value, object_name);
```

### Python API (Lumapi)
```python
session.set(property_name, value)
session.set(property_name, value, object_name)
```

## 参数

| 参数 | 类型 | 描述 |
|------|------|------|
| `property_name` | string | 要设置的属性名称 |
| `value` | 多种类型 | 属性值，类型取决于属性 |
| `object_name` | string | (可选) 对象名称。如省略，则设置当前选中对象的属性 |

## 返回值

`set` 命令没有返回值。成功执行后，对象的指定属性被更新。

## 属性值类型

`set` 命令支持多种类型的属性值：

### 1. 标量值
```lumerical
set("x", 0);           // 浮点数
set("x span", 2e-6);   // 科学计数法
set("enabled", 1);     // 整数 (0/1 表示布尔值)
```

### 2. 字符串
```lumerical
set("name", "waveguide");            // 简单字符串
set("material", "Si (Silicon)");     // 材料名称
set("x min bc", "PML");              // 边界条件
```

### 3. 数组
```lumerical
set("color", [0.5, 0.5, 0.5, 1.0]);  // RGBA 颜色数组
set("vertices", [0,0,0; 1e-6,0,0; 1e-6,1e-6,0]);  // 多行数组
```

### 4. 矩阵
```lumerical
set("permittivity", [1,0,0; 0,1,0; 0,0,1]);  // 3x3 矩阵
```

### 5. 表达式
```lumerical
set("x", "1.55e-6/2");  // 数学表达式
set("y", "x*2");        // 引用其他属性
```

## 对象选择与上下文

### 1. 隐式对象选择
如果没有指定 `object_name`，`set` 操作当前选中对象：
```lumerical
// 先选择对象
select("FDTD");
// 然后设置属性（不指定对象名称）
set("x span", 2e-6);
```

### 2. 显式对象指定
直接指定对象名称：
```lumerical
set("x span", 2e-6, "FDTD");
```

### 3. Python API 中的对象引用
```python
# 方法1: 使用对象名称
fdtd.set("x span", 2e-6, "FDTD")

# 方法2: 使用对象句柄（如果已知）
```

## 常用属性分类

### 1. 几何属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `x`, `y`, `z` | 所有几何对象 | 中心坐标 (m) | `set("x", 0)` |
| `x span`, `y span`, `z span` | 所有几何对象 | 各方向跨度 (m) | `set("x span", 2e-6)` |
| `x min`, `x max` | 所有几何对象 | 最小/最大坐标 (m) | `set("x min", -1e-6)` |
| `radius` | 球体、圆柱体 | 半径 (m) | `set("radius", 500e-9)` |
| `height` | 圆柱体 | 高度 (m) | `set("height", 1e-6)` |
| `vertices` | 多边形 | 顶点坐标矩阵 | `set("vertices", [0,0,0; 1e-6,0,0])` |

### 2. 材料属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `material` | 所有几何对象 | 材料名称 | `set("material", "Si (Silicon)")` |
| `index` | 几何对象 | 自定义折射率 | `set("index", 3.45)` |
| `index units` | 几何对象 | 折射率单位 | `set("index units", "microns")` |
| `permittivity` | 几何对象 | 自定义介电常数张量 | `set("permittivity", [1,0,0;0,1,0;0,0,1])` |
| `conductivity` | 几何对象 | 电导率 (S/m) | `set("conductivity", 1e7)` |

### 3. 求解器属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `simulation time` | FDTD | 仿真时间 (s) | `set("simulation time", 1000e-15)` |
| `mesh accuracy` | FDTD, FDE, EME | 网格精度 (1-8) | `set("mesh accuracy", 3)` |
| `wavelength` | FDE, EME | 波长 (m) | `set("wavelength", 1.55e-6)` |
| `number of trial modes` | FDE, EME | 模式数量 | `set("number of trial modes", 10)` |
| `background index` | 所有求解器 | 背景折射率 | `set("background index", 1.444)` |

### 4. 边界条件
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `x min bc`, `x max bc` | FDTD, FDE, EME | X方向边界条件 | `set("x min bc", "PML")` |
| `y min bc`, `y max bc` | FDTD, FDE, EME | Y方向边界条件 | `set("y min bc", "PML")` |
| `z min bc`, `z max bc` | FDTD, FDE, EME | Z方向边界条件 | `set("z min bc", "PML")` |
| `pml layers` | FDTD, FDE, EME | PML层数 | `set("pml layers", 10)` |
| `pml type` | FDTD, FDE, EME | PML类型 | `set("pml type", "standard")` |

### 5. 网格属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `mesh cells x` | 所有求解器 | X方向网格细胞数 | `set("mesh cells x", 100)` |
| `mesh cells y` | 所有求解器 | Y方向网格细胞数 | `set("mesh cells y", 100)` |
| `mesh cells z` | 所有求解器 | Z方向网格细胞数 | `set("mesh cells z", 50)` |
| `min mesh step` | 所有求解器 | 最小网格步长 (m) | `set("min mesh step", 1e-9)` |
| `max mesh step` | 所有求解器 | 最大网格步长 (m) | `set("max mesh step", 100e-9)` |
| `dx`, `dy`, `dz` | 所有求解器 | 网格步长 (m) | `set("dx", 10e-9)` |

### 6. 监视器属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `monitor type` | 监视器 | 监视器类型 | `set("monitor type", "time")` |
| `x span`, `y span`, `z span` | 监视器 | 监视区域跨度 | `set("x span", 2e-6)` |
| `frequency points` | 频域监视器 | 频率点数 | `set("frequency points", 100)` |
| `override global monitor settings` | 监视器 | 覆盖全局设置 | `set("override global monitor settings", 1)` |

### 7. 光源属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `injection axis` | 光源 | 注入方向 | `set("injection axis", "x")` |
| `wavelength start` | 光源 | 起始波长 (m) | `set("wavelength start", 1.5e-6)` |
| `wavelength stop` | 光源 | 结束波长 (m) | `set("wavelength stop", 1.6e-6)` |
| `frequency points` | 光源 | 频率点数 | `set("frequency points", 50)` |
| `amplitude` | 光源 | 振幅 | `set("amplitude", 1)` |

### 8. 显示与渲染属性
| 属性 | 适用对象 | 描述 | 示例 |
|------|----------|------|------|
| `color` | 所有对象 | RGBA颜色值 | `set("color", [1,0,0,1])` |
| `alpha` | 所有对象 | 透明度 (0.0-1.0) | `set("alpha", 0.5)` |
| `render type` | 几何对象 | 渲染类型 | `set("render type", "wireframe")` |
| `visible` | 所有对象 | 可见性 | `set("visible", 1)` |

## 示例

### 示例 1: 基本几何对象设置

#### LSF 脚本
```lumerical
// 添加矩形并设置属性
addrect;
set("name", "silicon waveguide");
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 5e-6);
set("y span", 500e-9);
set("z span", 220e-9);
set("material", "Si (Silicon) - Palik");

// 设置颜色和透明度
set("color", [0.8, 0.2, 0.2, 1.0]);
set("alpha", 0.7);

// 设置网格顺序
set("override mesh order from material database", 1);
set("mesh order", 2);
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 添加矩形并设置属性
fdtd.addrect()
fdtd.set("name", "silicon waveguide")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 5e-6)
fdtd.set("y span", 500e-9)
fdtd.set("z span", 220e-9)
fdtd.set("material", "Si (Silicon) - Palik")

# 设置颜色和透明度
fdtd.set("color", [0.8, 0.2, 0.2, 1.0])
fdtd.set("alpha", 0.7)

# 设置网格顺序
fdtd.set("override mesh order from material database", 1)
fdtd.set("mesh order", 2)
```

### 示例 2: 求解器设置

#### LSF 脚本
```lumerical
// 添加 FDTD 求解器
addfdtd;

// 设置几何范围
set("x", 0);
set("y", 0);
set("z", 0);
set("x span", 3e-6);
set("y span", 3e-6);
set("z span", 1e-6);

// 设置边界条件
set("x min bc", "PML");
set("x max bc", "PML");
set("y min bc", "PML");
set("y max bc", "PML");
set("z min bc", "PML");
set("z max bc", "PML");
set("pml layers", 10);
set("pml type", "stretched coordinate");

// 设置网格
set("mesh accuracy", 4);
set("min mesh step", 1e-9);
set("max mesh step", 50e-9);

// 设置仿真参数
set("simulation time", 500e-15);
set("auto shutoff min", 1e-5);
set("background index", 1.444);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 添加 FDTD 求解器
fdtd.addfdtd()

# 设置几何范围
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 3e-6)
fdtd.set("y span", 3e-6)
fdtd.set("z span", 1e-6)

# 设置边界条件
fdtd.set("x min bc", "PML")
fdtd.set("x max bc", "PML")
fdtd.set("y min bc", "PML")
fdtd.set("y max bc", "PML")
fdtd.set("z min bc", "PML")
fdtd.set("z max bc", "PML")
fdtd.set("pml layers", 10)
fdtd.set("pml type", "stretched coordinate")

# 设置网格
fdtd.set("mesh accuracy", 4)
fdtd.set("min mesh step", 1e-9)
fdtd.set("max mesh step", 50e-9)

# 设置仿真参数
fdtd.set("simulation time", 500e-15)
fdtd.set("auto shutoff min", 1e-5)
fdtd.set("background index", 1.444)
```

### 示例 3: 监视器设置

#### LSF 脚本
```lumerical
// 添加时间监视器
addtime;
set("name", "time monitor");
set("monitor type", "2D X-normal");
set("x", 0);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置记录参数
set("override global monitor settings", 1);
set("record E", 1);      // 记录电场
set("record H", 1);      // 记录磁场
set("record P", 1);      // 记录坡印廷矢量
set("frequency points", 100);

// 设置输出文件
set("output Ex", "ex");
set("output Ey", "ey");
set("output Ez", "ez");
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 添加时间监视器
fdtd.addtime()
fdtd.set("name", "time monitor")
fdtd.set("monitor type", "2D X-normal")
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置记录参数
fdtd.set("override global monitor settings", 1)
fdtd.set("record E", 1)      # 记录电场
fdtd.set("record H", 1)      # 记录磁场
fdtd.set("record P", 1)      # 记录坡印廷矢量
fdtd.set("frequency points", 100)

# 设置输出文件
fdtd.set("output Ex", "ex")
fdtd.set("output Ey", "ey")
fdtd.set("output Ez", "ez")
```

### 示例 4: 光源设置

#### LSF 脚本
```lumerical
// 添加模式光源
addmode;
set("name", "mode source");
set("injection axis", "x");
set("x", -1e-6);
set("y", 0);
set("z", 0);
set("y span", 2e-6);
set("z span", 1e-6);

// 设置波长范围
set("wavelength start", 1.5e-6);
set("wavelength stop", 1.6e-6);
set("frequency points", 50);

// 设置模式参数
set("mode selection", "fundamental TE mode");
set("amplitude", 1.0);
set("phase", 0);

// 设置极化
set("polarization angle", 0);
set("polarization ellipse angle", 0);
set("polarization ellipticity", 0);
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 添加模式光源
fdtd.addmode()
fdtd.set("name", "mode source")
fdtd.set("injection axis", "x")
fdtd.set("x", -1e-6)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 1e-6)

# 设置波长范围
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)
fdtd.set("frequency points", 50)

# 设置模式参数
fdtd.set("mode selection", "fundamental TE mode")
fdtd.set("amplitude", 1.0)
fdtd.set("phase", 0)

# 设置极化
fdtd.set("polarization angle", 0)
fdtd.set("polarization ellipse angle", 0)
fdtd.set("polarization ellipticity", 0)
```

### 示例 5: 使用表达式设置属性

#### LSF 脚本
```lumerical
// 使用表达式计算属性值
addrect;

// 使用数学表达式
set("x span", "1.55e-6/2");      // 波长的一半
set("y span", "x span/2");       // x 跨度的一半
set("z", "sin(pi/4)*1e-6");      // 三角函数

// 使用变量
lambda0 = 1.55e-6;
set("x span", lambda0);
set("y span", lambda0/2);

// 条件表达式
set("material", "if(x>0, 'Si', 'SiO2')");
```

#### Python API
```python
fdtd = lumapi.FDTD()
fdtd.addrect()

# 使用表达式计算属性值
lambda0 = 1.55e-6
fdtd.set("x span", lambda0)
fdtd.set("y span", lambda0/2)

# 注意: Python API 中表达式需要作为字符串传递
fdtd.set("z", "sin(pi/4)*1e-6")
```

### 示例 6: 设置多个对象的属性

#### LSF 脚本
```lumerical
// 创建多个对象
addrect;
set("name", "rect1");
set("x", -1e-6);
set("y span", 1e-6);

addrect;
set("name", "rect2");
set("x", 1e-6);
set("y span", 1e-6);

// 批量设置相同属性
set("z", 0, "rect1");
set("z", 0, "rect2");
set("z span", 220e-9, "rect1");
set("z span", 220e-9, "rect2");
set("material", "Si (Silicon)", "rect1");
set("material", "Si (Silicon)", "rect2");

// 使用循环设置多个对象
for(i=1:5) {
    addrect;
    set("name", "rect" + num2str(i));
    set("x", (i-3)*1e-6);
    set("y span", i*200e-9);
}
```

#### Python API
```python
fdtd = lumapi.FDTD()

# 创建多个对象并设置属性
for i in range(1, 6):
    fdtd.addrect()
    name = f"rect{i}"
    fdtd.set("name", name)
    fdtd.set("x", (i-3)*1e-6)
    fdtd.set("y span", i*200e-9)
    fdtd.set("z", 0, name)
    fdtd.set("z span", 220e-9, name)
    fdtd.set("material", "Si (Silicon)", name)
```

## 高级用法

### 1. 使用 `setnamed` 替代 `set`
`setnamed` 命令与 `set` 类似，但总是需要对象名称参数：
```lumerical
// 等效的两种写法
set("x span", 2e-6, "FDTD");
setnamed("FDTD", "x span", 2e-6);
```

### 2. 批量设置属性
```lumerical
// 使用结构体批量设置
properties = struct;
properties.x = 0;
properties.y = 0;
properties.z = 0;
properties.x_span = 2e-6;
set("FDTD", properties);
```

### 3. 获取当前值后修改
```lumerical
// 获取当前值，修改后设置
current_span = get("x span");
new_span = current_span * 1.1;
set("x span", new_span);
```

### 4. 条件设置
```lumerical
// 根据条件设置不同值
if(get("material") == "Si") {
    set("color", [0.8, 0.2, 0.2, 1.0]);
} else {
    set("color", [0.2, 0.2, 0.8, 1.0]);
}
```

## 注意事项

### 1. 属性名称大小写
- 大多数属性名称不区分大小写，但建议使用小写
- 材料名称区分大小写
- 对象名称区分大小写

### 2. 单位系统
- 所有长度单位都是米 (m)
- 时间单位是秒 (s)
- 角度单位是度
- 可以使用工程单位：`1e-6` 表示 1 微米

### 3. 属性依赖性
某些属性设置依赖于其他属性：
```lumerical
// 必须先启用覆盖才能设置网格顺序
set("override mesh order from material database", 1);
set("mesh order", 2);  // 现在可以设置
```

### 4. 只读属性
某些属性是只读的，不能通过 `set` 修改：
- `type`: 对象类型
- `uid`: 对象唯一标识符
- `creation date`: 创建日期

### 5. 对象存在性验证
设置属性前应确保对象存在：
```lumerical
if(hasexisting("FDTD")) {
    set("x span", 2e-6, "FDTD");
} else {
    addfdtd;
    set("x span", 2e-6);
}
```

## 错误处理

### 常见错误
1. **对象不存在**
   ```lumerical
   // 错误: 对象 "nonexistent" 不存在
   set("x", 0, "nonexistent");
   ```
   解决方案：先创建对象或检查对象名称

2. **属性不存在**
   ```lumerical
   // 错误: 属性 "invalid_property" 不存在
   set("invalid_property", 1);
   ```
   解决方案：检查属性名称拼写

3. **无效的属性值**
   ```lumerical
   // 错误: 负的跨度值无效
   set("x span", -1e-6);
   ```
   解决方案：提供有效的属性值

4. **类型不匹配**
   ```lumerical
   // 错误: 期望数值但提供了字符串
   set("x span", "text");
   ```
   解决方案：提供正确类型的值

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    fdtd.addfdtd()
    
    # 尝试设置属性
    fdtd.set("x span", 2e-6)
    
    # 尝试设置无效属性
    fdtd.set("invalid_property", 1)
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
except Exception as e:
    print(f"一般错误: {e}")
    
    # 检查错误类型
    if "object" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 对象不存在")
    elif "property" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 属性不存在")
    elif "invalid" in str(e).lower() and "value" in str(e).lower():
        print("错误: 无效的属性值")
```

## 性能优化

### 1. 批量设置减少 API 调用
```python
# 不好: 多次 API 调用
fdtd.set("x", 0)
fdtd.set("y", 0)
fdtd.set("z", 0)
fdtd.set("x span", 2e-6)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)

# 好: 使用字典批量设置（如果支持）
properties = {
    "x": 0,
    "y": 0,
    "z": 0,
    "x span": 2e-6,
    "y span": 2e-6,
    "z span": 2e-6
}
# 注: 实际可能需要循环设置，但减少 Python-Lumerical 切换
```

### 2. 避免不必要的设置
```python
# 只设置需要修改的属性，而不是所有属性
if needs_update:
    fdtd.set("x span", new_value)
```

### 3. 使用本地变量
```python
# 减少属性名字符串重复
prop_name = "x span"
fdtd.set(prop_name, value1)
fdtd.set(prop_name, value2)  # 复用字符串
```

## 相关命令

- `get`: 获取对象属性值
- `getdata`: 获取仿真数据
- `setnamed`: 按名称设置对象属性
- `setglobalmonitor`: 设置全局监视器属性
- `setglobalsource`: 设置全局光源属性
- `select`: 选择对象
- `addproperty`: 添加自定义属性

## 产品支持

- **完全支持**: 所有 Lumerical 产品
- **核心命令**: 在所有产品中功能一致
- **属性差异**: 不同产品的对象有不同属性集

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增表达式引擎改进 |
| Lumerical 2019a | 增加批量设置性能优化 |
| Lumerical 2018a | 新增 Python API 支持 |

## 参考

1. Lumerical 脚本命令参考手册
2. Lumerical 对象属性参考
3. Lumerical 知识库: `set` 命令最佳实践

---

*最后更新: 2025-01-30*  
*文档版本: 1.0*