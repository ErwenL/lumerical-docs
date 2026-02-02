# getresult

## 概述

`getresult` 命令用于从仿真对象（特别是监视器）中获取计算结果数据。这是后处理和分析仿真结果的核心命令，可以获取电场、磁场、功率、模式系数等多种数据类型。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
data = getresult(object_name, data_name);
[data1, data2, ...] = getresult(object_name, data_name1, data_name2, ...);
```

### Python API (Lumapi)
```python
data = session.getresult(object_name, data_name)
data1, data2, ... = session.getresult(object_name, data_name1, data_name2, ...)
```

## 参数

| 参数 | 类型 | 描述 |
|------|------|------|
| `object_name` | string | 对象名称（通常是监视器名称） |
| `data_name` | string | 要获取的数据名称 |

## 返回值

返回请求的数据，类型取决于数据名称。可以返回：
- 标量值
- 向量（一维数组）
- 矩阵（二维数组）
- 结构体（包含多个字段）
- 多个输出（当请求多个数据名称时）

## 数据名称分类

### 1. 基本监视器数据
| 数据名称 | 监视器类型 | 描述 | 返回类型 |
|----------|------------|------|----------|
| `E` | 所有电场监视器 | 电场分量 | 结构体 |
| `Ex`, `Ey`, `Ez` | 所有电场监视器 | 各方向电场 | 矩阵 |
| `H` | 所有磁场监视器 | 磁场分量 | 结构体 |
| `Hx`, `Hy`, `Hz` | 所有磁场监视器 | 各方向磁场 | 矩阵 |
| `power` | 功率监视器 | 功率 | 矩阵 |
| `f` | 频域监视器 | 频率向量 | 向量 |
| `lambda` | 频域监视器 | 波长向量 | 向量 |
| `t` | 时域监视器 | 时间向量 | 向量 |

### 2. 模式监视器数据
| 数据名称 | 监视器类型 | 描述 | 返回类型 |
|----------|------------|------|----------|
| `a` | 模式展开监视器 | 前向模式系数 | 矩阵 |
| `b` | 模式展开监视器 | 后向模式系数 | 矩阵 |
| `Nf` | 模式展开监视器 | 前向模式数 | 标量 |
| `Nb` | 模式展开监视器 | 后向模式数 | 标量 |
| `mode` | 模式监视器 | 模式场数据 | 结构体 |
| `n_eff` | 模式监视器 | 有效折射率 | 向量 |
| `loss` | 模式监视器 | 模式损耗 | 向量 |

### 3. 高级数据
| 数据名称 | 监视器类型 | 描述 | 返回类型 |
|----------|------------|------|----------|
| `Poynting` | 功率监视器 | 坡印廷矢量 | 结构体 |
| `Sx`, `Sy`, `Sz` | 功率监视器 | 各方向坡印廷分量 | 矩阵 |
| `absorption` | 功率监视器 | 吸收功率 | 矩阵 |
| `transmission` | 功率监视器 | 透射功率 | 矩阵 |
| `reflection` | 功率监视器 | 反射功率 | 矩阵 |
| `E2` | 电场监视器 | 电场强度平方 | 矩阵 |
| `H2` | 磁场监视器 | 磁场强度平方 | 矩阵 |

### 4. 元数据
| 数据名称 | 监视器类型 | 描述 | 返回类型 |
|----------|------------|------|----------|
| `x` | 空间监视器 | X 坐标向量 | 向量 |
| `y` | 空间监视器 | Y 坐标向量 | 向量 |
| `z` | 空间监视器 | Z 坐标向量 | 向量 |
| `x0` | 点监视器 | X 坐标 | 标量 |
| `y0` | 点监视器 | Y 坐标 | 标量 |
| `z0` | 点监视器 | Z 坐标 | 标量 |

## 示例

### 示例 1: 获取电场数据

#### LSF 脚本
```lumerical
// 假设有名为 "monitor1" 的电场监视器
E_data = getresult("monitor1", "E");

// 访问结构体字段
Ex = E_data.Ex;      // Ex 分量
Ey = E_data.Ey;      // Ey 分量
Ez = E_data.Ez;      // Ez 分量
f = E_data.f;        // 频率向量
x = E_data.x;        // X 坐标向量
y = E_data.y;        // Y 坐标向量
z = E_data.z;        // Z 坐标向量

// 直接获取特定分量
Ex_only = getresult("monitor1", "Ex");
freq = getresult("monitor1", "f");

// 获取多个数据
[Ex, Ey, f] = getresult("monitor1", "Ex", "Ey", "f");
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 获取电场数据
E_data = fdtd.getresult("monitor1", "E")

# 访问数据
Ex = E_data["Ex"]      # Ex 分量
Ey = E_data["Ey"]      # Ey 分量
Ez = E_data["Ez"]      # Ez 分量
f = E_data["f"]        # 频率向量
x = E_data["x"]        # X 坐标向量
y = E_data["y"]        # Y 坐标向量
z = E_data["z"]        # Z 坐标向量

# 直接获取特定分量
Ex_only = fdtd.getresult("monitor1", "Ex")
freq = fdtd.getresult("monitor1", "f")

# 获取多个数据
Ex, Ey, f = fdtd.getresult("monitor1", "Ex", "Ey", "f")
```

### 示例 2: 获取模式系数

#### LSF 脚本
```lumerical
// 假设有名为 "mode_expansion" 的模式展开监视器
[a, b, Nf, Nb] = getresult("mode_expansion", "a", "b", "Nf", "Nb");

// a 和 b 是矩阵: 行=模式数, 列=频率点数
num_modes = Nf;  // 前向模式数
num_freq = size(a, 2);  // 频率点数

// 获取特定模式的系数
mode1_forward = a(1, :);  // 第一个模式的前向系数（所有频率）
mode1_backward = b(1, :); // 第一个模式的后向系数

// 获取特定频率的模式系数
freq_idx = 10;
coeff_at_freq = a(:, freq_idx);  // 所有模式在特定频率的系数
```

#### Python API
```python
# 获取模式系数
a, b, Nf, Nb = fdtd.getresult("mode_expansion", "a", "b", "Nf", "Nb")

# a 和 b 是矩阵: 行=模式数, 列=频率点数
num_modes = Nf  # 前向模式数
num_freq = a.shape[1]  # 频率点数

# 获取特定模式的系数
mode1_forward = a[0, :]  # 第一个模式的前向系数（所有频率）
mode1_backward = b[0, :]  # 第一个模式的后向系数

# 获取特定频率的模式系数
freq_idx = 9  # Python 索引从0开始
coeff_at_freq = a[:, freq_idx]  # 所有模式在特定频率的系数
```

### 示例 3: 获取功率数据

#### LSF 脚本
```lumerical
// 获取功率监视器数据
power_data = getresult("power_monitor", "power");
f = getresult("power_monitor", "f");

// 计算透射率（如果有参考功率）
T = power_data / reference_power;

// 获取坡印廷矢量
Poynting = getresult("power_monitor", "Poynting");
Sx = Poynting.Sx;
Sy = Poynting.Sy;
Sz = Poynting.Sz;

// 直接获取各分量
[Sx, Sy, Sz] = getresult("power_monitor", "Sx", "Sy", "Sz");
```

#### Python API
```python
# 获取功率监视器数据
power_data = fdtd.getresult("power_monitor", "power")
f = fdtd.getresult("power_monitor", "f")

# 计算透射率（如果有参考功率）
T = power_data / reference_power

# 获取坡印廷矢量
Poynting = fdtd.getresult("power_monitor", "Poynting")
Sx = Poynting["Sx"]
Sy = Poynting["Sy"]
Sz = Poynting["Sz"]

# 直接获取各分量
Sx, Sy, Sz = fdtd.getresult("power_monitor", "Sx", "Sy", "Sz")
```

### 示例 4: 获取模式场数据

#### LSF 脚本
```lumerical
// 获取模式监视器数据
mode_data = getresult("mode_monitor", "mode");

// 访问模式场
Ex = mode_data.Ex;  // 电场 X 分量
Ey = mode_data.Ey;  // 电场 Y 分量
Ez = mode_data.Ez;  // 电场 Z 分量
Hx = mode_data.Hx;  // 磁场 X 分量
Hy = mode_data.Hy;  // 磁场 Y 分量
Hz = mode_data.Hz;  // 磁场 Z 分量

// 获取模式参数
n_eff = getresult("mode_monitor", "n_eff");
loss = getresult("mode_monitor", "loss");

// 获取坐标
x = mode_data.x;
y = mode_data.y;
z = mode_data.z;
```

#### Python API
```python
# 获取模式监视器数据
mode_data = fdtd.getresult("mode_monitor", "mode")

# 访问模式场
Ex = mode_data["Ex"]  # 电场 X 分量
Ey = mode_data["Ey"]  # 电场 Y 分量
Ez = mode_data["Ez"]  # 电场 Z 分量
Hx = mode_data["Hx"]  # 磁场 X 分量
Hy = mode_data["Hy"]  # 磁场 Y 分量
Hz = mode_data["Hz"]  # 磁场 Z 分量

# 获取模式参数
n_eff = fdtd.getresult("mode_monitor", "n_eff")
loss = fdtd.getresult("mode_monitor", "loss")

# 获取坐标
x = mode_data["x"]
y = mode_data["y"]
z = mode_data["z"]
```

### 示例 5: 高级数据处理

#### LSF 脚本
```lumerical
// 计算电场强度
E_data = getresult("field_monitor", "E");
E2 = abs(E_data.Ex)^2 + abs(E_data.Ey)^2 + abs(E_data.Ez)^2;

// 计算时间平均坡印廷矢量
Poynting = getresult("power_monitor", "Poynting");
S_avg = 0.5 * real(Poynting.Sx + Poynting.Sy + Poynting.Sz);

// 计算模式重叠积分（需要两个模式监视器）
mode1 = getresult("mode1", "mode");
mode2 = getresult("mode2", "mode");

// 计算重叠积分
overlap = sum(sum(sum(conj(mode1.Ex) .* mode2.Ex + ...
                     conj(mode1.Ey) .* mode2.Ey + ...
                     conj(mode1.Ez) .* mode2.Ez))) * ...
          (mode1.x(2)-mode1.x(1)) * (mode1.y(2)-mode1.y(1)) * (mode1.z(2)-mode1.z(1));
```

#### Python API
```python
import numpy as np

# 计算电场强度
E_data = fdtd.getresult("field_monitor", "E")
E2 = np.abs(E_data["Ex"])**2 + np.abs(E_data["Ey"])**2 + np.abs(E_data["Ez"])**2

# 计算时间平均坡印廷矢量
Poynting = fdtd.getresult("power_monitor", "Poynting")
S_avg = 0.5 * np.real(Poynting["Sx"] + Poynting["Sy"] + Poynting["Sz"])

# 计算模式重叠积分（需要两个模式监视器）
mode1 = fdtd.getresult("mode1", "mode")
mode2 = fdtd.getresult("mode2", "mode")

# 计算重叠积分
dx = mode1["x"][1] - mode1["x"][0]
dy = mode1["y"][1] - mode1["y"][0]
dz = mode1["z"][1] - mode1["z"][0]

overlap = np.sum(np.conj(mode1["Ex"]) * mode2["Ex"] + 
                 np.conj(mode1["Ey"]) * mode2["Ey"] + 
                 np.conj(mode1["Ez"]) * mode2["Ez"]) * dx * dy * dz
```

## 数据结构和维度

### 1. 电场/磁场数据结构
```matlab
// E_data 结构体示例
E_data = 
    Ex: [100x50x20 double]  % 三维数组: x×y×z
    Ey: [100x50x20 double]
    Ez: [100x50x20 double]
    f:  [1x30 double]       % 频率向量
    x:  [100x1 double]      % X 坐标向量
    y:  [50x1 double]       % Y 坐标向量
    z:  [20x1 double]       % Z 坐标向量
```

### 2. 模式系数维度
```matlab
// 模式系数矩阵
a = [Nmodes × Nfreq]  % 模式数 × 频率点数
b = [Nmodes × Nfreq]  % 模式数 × 频率点数
```

### 3. 功率数据维度
```matlab
// 功率数据
power = [1 × Nfreq]   % 标量功率 vs 频率
// 或
power = [Nx × Ny × Nz × Nfreq]  % 空间分布功率
```

## 注意事项

### 1. 数据可用性
- 数据必须在仿真运行后可用
- 监视器必须已记录请求的数据类型
- 使用 `getdata` 命令检查数据是否存在

### 2. 内存管理
- 大型数据集可能占用大量内存
- 考虑只获取需要的数据子集
- 使用 `getdata` 获取数据大小信息

### 3. 数据类型
- 电场/磁场数据通常是复数（频域）
- 功率数据通常是实数
- 模式系数是复数

### 4. 坐标系统
- 坐标向量是单调递增的
- 网格点位置在坐标向量中定义
- 使用 `meshgrid` 创建坐标矩阵用于绘图

### 5. 单位
- 电场: V/m
- 磁场: A/m
- 功率: W
- 频率: Hz
- 波长: m

## 错误处理

### 常见错误
1. **对象不存在**
   ```lumerical
   // 错误: 对象 "nonexistent" 不存在
   data = getresult("nonexistent", "E");
   ```
   解决方案：检查对象名称

2. **数据不存在**
   ```lumerical
   // 错误: 数据 "nonexistent_data" 不存在
   data = getresult("monitor1", "nonexistent_data");
   ```
   解决方案：检查数据名称，确保监视器记录了该数据

3. **数据维度不匹配**
   ```lumerical
   // 错误: 尝试访问不存在的维度
   value = E_data.Ex(200, 100, 50);  // 但维度是 [100,50,20]
   ```
   解决方案：检查数据维度

### Python 错误处理
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 尝试获取数据
    data = fdtd.getresult("monitor1", "E")
    
except lumapi.LumApiError as e:
    print(f"Lumerical API 错误: {e}")
    
    if "object" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 对象不存在")
    elif "data" in str(e).lower() and "not found" in str(e).lower():
        print("错误: 数据不存在")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 性能优化

### 1. 只获取需要的数据
```python
# 不好: 获取所有数据然后提取需要的部分
all_data = fdtd.getresult("monitor1", "E")
Ex = all_data["Ex"]

# 好: 只获取需要的数据
Ex = fdtd.getresult("monitor1", "Ex")
```

### 2. 批量获取相关数据
```python
# 减少 API 调用次数
Ex, Ey, f = fdtd.getresult("monitor1", "Ex", "Ey", "f")
```

### 3. 使用数据子集
```python
# 如果只需要特定频率的数据
all_data = fdtd.getresult("monitor1", "E")
Ex_all = all_data["Ex"]
Ex_subset = Ex_all[:, :, :, freq_indices]  # 只取特定频率
```

## 相关命令

- `getdata`: 获取仿真数据（更通用的命令）
- `get`: 获取对象属性值
- `getnamed`: 按名称获取对象属性
- `pininfo`: 获取端口信息
- `transmission`: 计算透射率
- `reflection`: 计算反射率
- `overlap`: 计算模式重叠积分

## 产品支持

- **完全支持**: FDTD Solutions, MODE Solutions
- **部分支持**: DEVICE, INTERCONNECT（不同数据类型）
- **核心命令**: 在所有产品中可用，但数据名称可能不同

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增多输出支持 |
| Lumerical 2019a | 改进大数据集处理性能 |
| Lumerical 2018a | 新增 Python API 支持 |

## 参考

1. Lumerical 监视器数据参考手册
2. Lumerical 后处理和分析指南
3. Lumerical 知识库: 数据提取最佳实践

---

*最后更新: 2025-01-30*  
*文档版本: 1.0*