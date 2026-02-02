# append

## 概述

`append` 命令用于将数据追加到数组、矩阵或数据结构中。该命令支持多种数据类型和维度，可以用于动态构建数据集、合并仿真结果、创建时间序列等。`append` 是数据处理和结果整理中的基本操作。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
append;
```

### Python API (Lumapi)
```python
session.append()
```

## 参数

`append` 命令没有直接参数，但需要通过后续的 `set` 命令配置目标数组、源数据和追加方式。

## 配置属性

使用 `append` 后，可以通过 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `target` | string | "" | 目标数组名称 |
| `source` | 任意 | [] | 源数据（数组、矩阵或标量） |
| `operation` | string | "append" | 操作类型："append", "prepend", "insert", "replace" |
| `dimension` | int | 0 | 追加维度 (0=自动, 1=行, 2=列, 3=深度) |
| `create if missing` | bool | true | 如果目标不存在则创建 |

### 2. 数组类型设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `data type` | string | "auto" | 数据类型："auto", "double", "complex", "int", "bool", "string" |
| `array type` | string | "numeric" | 数组类型："numeric", "cell", "struct", "table" |
| `shape` | vector | [] | 数组形状（行数, 列数, ...） |
| `fill value` | 任意 | 0 | 填充值（用于预分配） |

### 3. 追加位置控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `position` | int | -1 | 插入位置 (-1=末尾, 0=开头, n=第n个位置) |
| `index` | vector | [] | 多维索引位置 |
| `condition` | string | "" | 追加条件（表达式） |
| `filter` | dict | {} | 数据过滤器 |

### 4. 数据转换设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `type conversion` | string | "auto" | 类型转换："auto", "strict", "loose", "custom" |
| `scaling factor` | float | 1.0 | 缩放因子 |
| `offset` | float | 0.0 | 偏移量 |
| `normalization` | string | "none" | 归一化："none", "minmax", "zscore", "unit" |
| `rounding` | string | "none" | 舍入："none", "round", "floor", "ceil", "fix" |
| `precision` | int | 16 | 数值精度（有效数字） |

### 5. 结构体追加设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `field name` | string | "" | 字段名称（用于结构体） |
| `field type` | string | "auto" | 字段类型 |
| `merge fields` | bool | true | 是否合并字段（结构体数组） |
| `unique fields` | bool | false | 是否要求字段唯一 |

### 6. 表格追加设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `column names` | array | [] | 列名数组 |
| `row names` | array | [] | 行名数组 |
| `table variable` | string | "" | 表格变量名称 |
| `append rows` | bool | true | 是否追加行（true）或列（false） |
| `match columns` | bool | true | 是否匹配列名 |

### 7. 性能优化
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `preallocation` | bool | false | 是否预分配内存 |
| `chunk size` | int | 1000 | 分块大小 |
| `buffer size` | int | 10000 | 缓冲区大小 |
| `compression` | bool | false | 是否压缩数据 |
| `parallel processing` | bool | false | 是否并行处理 |

### 8. 错误处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `error handling` | string | "warn" | 错误处理："stop", "warn", "ignore", "log" |
| `size mismatch` | string | "resize" | 尺寸不匹配处理："resize", "pad", "crop", "error" |
| `type mismatch` | string | "convert" | 类型不匹配处理："convert", "cast", "error" |
| `duplicate handling` | string | "allow" | 重复处理："allow", "unique", "replace", "error" |

### 9. 元数据
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `metadata` | dict | {} | 数组元数据 |
| `units` | string | "" | 数据单位 |
| `description` | string | "" | 数据描述 |
| `tags` | array | [] | 数据标签 |

### 10. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `custom function` | string | "" | 自定义处理函数 |
| `validation rules` | array | [] | 数据验证规则 |
| `transformation` | string | "" | 数据变换表达式 |
| `callback` | string | "" | 回调函数 |

## 返回值

`append` 命令不直接返回值，而是修改目标数组。操作结果通过目标数组的变化体现：

- **成功追加**：目标数组包含追加后的数据，可以通过 `getdata` 命令获取
- **错误情况**：如果追加失败，目标数组保持不变，错误信息可通过错误处理配置获取
- **状态信息**：可以通过 `getv("append", "last_operation")` 获取最后一次追加操作的状态信息

追加操作的影响：
1. **数组大小变化**：目标数组的大小会根据追加的数据量增加
2. **数据类型可能变化**：如果启用类型转换，数组数据类型可能改变
3. **内存占用变化**：数组占用内存相应增加
4. **性能统计**：可以通过性能监控属性获取追加操作的性能数据

## 使用示例

### 示例 1：基本数组追加
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

# 创建空数组
session.eval("data = [];")

# 追加标量值
session.append()
session.set("target", "data")
session.set("source", 1.0)
# 结果: data = [1.0]

# 追加向量
session.append()
session.set("target", "data")
session.set("source", [2.0, 3.0, 4.0])
# 结果: data = [1.0, 2.0, 3.0, 4.0]

# 追加矩阵
session.append()
session.set("target", "data")
session.set("source", [[5.0, 6.0], [7.0, 8.0]])
# 结果: data = [1.0, 2.0, 3.0, 4.0, [5.0, 6.0], [7.0, 8.0]]

# 追加复杂数据
complex_data = [1+2j, 3+4j, 5+6j]
session.append()
session.set("target", "data")
session.set("source", complex_data)
session.set("data type", "complex")
# 结果: data 包含复数元素

# 检查结果
result = session.getdata("data")
print(f"Data shape: {result.shape}")
print(f"Data type: {result.dtype}")
```

### 示例 2：时间序列数据收集
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

# 初始化时间序列数组
session.eval("""
time_series = struct;
time_series.time = [];
time_series.E_field = [];
time_series.H_field = [];
time_series.power = [];
""")

# 仿真循环
num_iterations = 100
time_step = 1e-15

for i in range(num_iterations):
    # 运行一个时间步
    session.run(1)  # 运行1个时间步
    
    # 获取当前场数据
    E = session.getelectric("field_monitor")
    H = session.getmagnetic("field_monitor")
    P = session.getpower("power_monitor")
    
    current_time = i * time_step
    
    # 追加时间点
    session.append()
    session.set("target", "time_series.time")
    session.set("source", current_time)
    session.set("units", "s")
    
    # 追加电场数据（作为结构体字段）
    session.append()
    session.set("target", "time_series.E_field")
    session.set("source", E)
    session.set("field name", f"iteration_{i}")
    session.set("units", "V/m")
    
    # 追加磁场数据
    session.append()
    session.set("target", "time_series.H_field")
    session.set("source", H)
    session.set("field name", f"iteration_{i}")
    session.set("units", "A/m")
    
    # 追加功率数据
    session.append()
    session.set("target", "time_series.power")
    session.set("source", P)
    session.set("field name", f"iteration_{i}")
    session.set("units", "W")
    
    # 进度报告
    if (i+1) % 10 == 0:
        print(f"Completed {i+1}/{num_iterations} iterations")

# 最终数据整理
session.eval("""
% 转换为更高效的数据结构
time_series.time = time_series.time(:);  % 列向量
time_series.E_field = cat(3, time_series.E_field{:});  % 3D数组
time_series.H_field = cat(3, time_series.H_field{:});  % 3D数组
time_series.power = [time_series.power{:}];  % 矩阵
""")

# 保存时间序列数据
session.eval('save("time_series_data.mat", "time_series");')
```

### 示例 3：参数扫描结果收集
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 定义参数扫描范围
widths = np.linspace(0.4e-6, 0.8e-6, 9)  # 400-800 nm, 9个点
heights = np.linspace(0.2e-6, 0.3e-6, 6)  # 200-300 nm, 6个点

# 初始化结果结构
session.eval("""
results = struct;
results.parameters = struct;
results.parameters.width = [];
results.parameters.height = [];
results.data = struct;
results.data.effective_index = [];
results.data.loss = [];
results.data.mode_profile = {};
""")

# 参数扫描循环
result_idx = 0
for i, width in enumerate(widths):
    for j, height in enumerate(heights):
        # 更新波导尺寸
        session.setnamed("waveguide", "x span", width)
        session.setnamed("waveguide", "y span", height)
        
        # 运行模式分析
        session.runmode()
        
        # 获取结果
        neff = session.getdata("mode", "neff")
        loss = session.getdata("mode", "loss")
        profile = session.getelectric("mode_profile")
        
        # 追加参数
        session.append()
        session.set("target", "results.parameters.width")
        session.set("source", width)
        session.set("units", "m")
        
        session.append()
        session.set("target", "results.parameters.height")
        session.set("source", height)
        session.set("units", "m")
        
        # 追加有效折射率
        session.append()
        session.set("target", "results.data.effective_index")
        session.set("source", neff)
        
        # 追加损耗
        session.append()
        session.set("target", "results.data.loss")
        session.set("source", loss)
        session.set("units", "dB/cm")
        
        # 追加模式剖面（作为细胞数组）
        session.append()
        session.set("target", "results.data.mode_profile")
        session.set("source", profile)
        session.set("array type", "cell")
        
        result_idx += 1
        print(f"Completed {result_idx}/{len(widths)*len(heights)}: "
              f"width={width*1e9:.0f}nm, height={height*1e9:.0f}nm")

# 重新组织数据为网格格式
session.eval("""
% 将线性数组重塑为网格
results.parameters.width_grid = reshape(results.parameters.width, 
                                        [length(widths), length(heights)]);
results.parameters.height_grid = reshape(results.parameters.height, 
                                         [length(widths), length(heights)]);
results.data.effective_index_grid = reshape(results.data.effective_index, 
                                            [length(widths), length(heights)]);
results.data.loss_grid = reshape(results.data.loss, 
                                 [length(widths), length(heights)]);
results.data.mode_profile_grid = reshape(results.data.mode_profile, 
                                         [length(widths), length(heights)]);
""")

# 保存参数扫描结果
session.eval('save("parameter_sweep_results.mat", "results");')
```

### 示例 4：高级表格数据追加
```python
import lumapi
import numpy as np
from datetime import datetime

session = lumapi.INTERCONNECT()

# 创建实验结果表格
session.eval("""
experiment_results = table();
experiment_results.Properties.Description = 'Optical component characterization results';
experiment_results.Properties.VariableDescriptions = {
    'Timestamp', '实验时间戳';
    'Component', '测试组件名称';
    'Wavelength', '测试波长 (nm)';
    'InsertionLoss', '插入损耗 (dB)';
    'ReturnLoss', '回波损耗 (dB)';
    'Bandwidth3dB', '3dB带宽 (GHz)';
    'Temperature', '测试温度 (°C)';
    'Notes', '实验备注'
};
experiment_results.Properties.VariableUnits = {
    '', '', 'nm', 'dB', 'dB', 'GHz', '°C', ''
};
""")

# 模拟多次测量
measurements = [
    {
        'component': 'MZI_1550',
        'wavelength': 1550.0,
        'insertion_loss': 0.5,
        'return_loss': 40.2,
        'bandwidth': 35.6,
        'temperature': 25.0,
        'notes': 'Baseline measurement'
    },
    {
        'component': 'MZI_1550',
        'wavelength': 1550.0,
        'insertion_loss': 0.52,
        'return_loss': 39.8,
        'bandwidth': 35.1,
        'temperature': 25.2,
        'notes': 'Repeat measurement'
    },
    {
        'component': 'Ring_Resonator',
        'wavelength': 1550.0,
        'insertion_loss': 1.2,
        'return_loss': 35.6,
        'bandwidth': 2.5,
        'temperature': 25.0,
        'notes': 'High-Q resonator'
    },
    {
        'component': 'Directional_Coupler',
        'wavelength': 1310.0,
        'insertion_loss': 0.3,
        'return_loss': 45.1,
        'bandwidth': 50.2,
        'temperature': 24.8,
        'notes': 'Wideband coupler'
    }
]

# 追加测量数据到表格
for i, meas in enumerate(measurements):
    # 创建新行数据
    new_row = {
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Component': meas['component'],
        'Wavelength': meas['wavelength'],
        'InsertionLoss': meas['insertion_loss'],
        'ReturnLoss': meas['return_loss'],
        'Bandwidth3dB': meas['bandwidth'],
        'Temperature': meas['temperature'],
        'Notes': meas['notes']
    }
    
    # 追加行到表格
    session.append()
    session.set("target", "experiment_results")
    session.set("source", new_row)
    session.set("array type", "table")
    session.set("append rows", True)
    session.set("match columns", True)
    
    # 添加元数据
    metadata = {
        'measurement_id': i+1,
        'operator': 'AutoLab_v1.0',
        'instrument': 'Optical_VNA_Agilent',
        'calibration_date': '2024-01-15'
    }
    
    session.set("metadata", metadata)
    print(f"Added measurement {i+1}: {meas['component']}")

# 表格后处理
session.eval("""
% 计算统计信息
stats = struct;
stats.components = unique(experiment_results.Component);
stats.num_measurements = height(experiment_results);

for i = 1:length(stats.components)
    component = stats.components{i};
    idx = strcmp(experiment_results.Component, component);
    
    stats.(component).mean_IL = mean(experiment_results.InsertionLoss(idx));
    stats.(component).std_IL = std(experiment_results.InsertionLoss(idx));
    stats.(component).mean_RL = mean(experiment_results.ReturnLoss(idx));
    stats.(component).std_RL = std(experiment_results.ReturnLoss(idx));
    stats.(component).num_measurements = sum(idx);
end

% 添加统计信息到表格属性
experiment_results.Properties.UserData.Stats = stats;
experiment_results.Properties.UserData.ProcessingDate = datestr(now);
""")

# 导出表格数据
session.eval('''
% 保存为多种格式
writetable(experiment_results, 'experiment_results.csv');
save('experiment_results.mat', 'experiment_results', 'stats');
''')

print(f"Experiment table created with {len(measurements)} measurements")
print(f"Components tested: {set(m['component'] for m in measurements)}")
```

## 注意事项

1. **数据类型一致性**：追加操作应保持数据类型一致性，避免意外类型转换
2. **内存管理**：大量数据追加时注意内存使用，考虑分块处理
3. **性能优化**：预分配数组可以显著提高追加性能
4. **维度匹配**：确保源数据和目标数组在追加维度上匹配
5. **索引有效性**：插入位置应在有效范围内
6. **数据完整性**：验证追加后的数据完整性和一致性
7. **错误处理**：配置适当的错误处理策略
8. **数据备份**：重要数据在操作前应备份

## 错误处理

`append` 命令提供全面的错误处理机制，可通过配置属性控制：

### 错误处理策略
1. **停止模式** (`error handling: "stop"`)：遇到错误立即停止，保留原始数据
2. **警告模式** (`error handling: "warn"`)：发出警告，跳过错误数据继续执行
3. **忽略模式** (`error handling: "ignore"`)：忽略错误，尝试继续执行
4. **日志模式** (`error handling: "log"`)：记录错误到日志文件

### 常见错误及处理
1. **尺寸不匹配错误**：源数据与目标数组维度不兼容
2. **类型转换错误**：数据类型无法安全转换
3. **内存不足错误**：追加操作超出可用内存
4. **索引越界错误**：插入位置超出数组范围
5. **重复数据错误**：启用唯一性检查时发现重复数据

### Python 错误处理示例
```python
import lumapi

session = lumapi.FDTD()

# 配置错误处理
session.append()
session.set("error handling", "warn")
session.set("size mismatch", "resize")
session.set("type mismatch", "convert")

try:
    # 尝试追加不匹配的数据
    session.eval("target_array = [1, 2, 3];")
    session.append()
    session.set("target", "target_array")
    session.set("source", [[4, 5], [6, 7]])  # 维度不匹配
    result = session.getdata("target_array")
    print(f"Append result: {result}")
except Exception as e:
    print(f"Append error: {e}")
    # 检查警告信息
    warnings = session.getv("append", "warnings")
    if warnings:
        print(f"Warnings: {warnings}")
```

### LSF 错误处理示例
```lumerical
# 配置错误处理
append;
set("error handling", "warn");
set("size mismatch", "resize");

# 尝试追加不匹配的数据
target_array = [1, 2, 3];
append;
set("target", "target_array");
set("source", {4, 5, 6, 7});  # 可以追加

# 检查操作状态
status = getv("append", "last_operation");
if (status.success) {
    ? "Append successful. New array: " + num2str(target_array);
} else {
    ? "Append failed: " + status.error_message;
}
```

### 调试建议
1. 启用详细日志：`set("verbose", true)`
2. 检查操作状态：使用 `getv("append", "last_operation")`
3. 验证数据格式：追加前检查源数据和目标数组格式
4. 逐步执行：复杂操作分解为多个简单追加

## 产品支持

- **FDTD Solutions**: 支持仿真结果数据追加
- **MODE Solutions**: 支持模式数据追加
- **DEVICE**: 支持热学、电学数据追加
- **INTERCONNECT**: 支持电路参数、测量数据追加

## 相关命令

- `cat` - 连接数组
- `horzcat` - 水平连接
- `vertcat` - 垂直连接
- `reshape` - 重塑数组形状
- `size` - 获取数组尺寸
- `length` - 获取数组长度
- `isempty` - 检查数组是否为空
- `clear` - 清除数组

## 版本历史

| 版本 | 修改 |
|------|------|
| 1.0 | 初始版本，包含基本数组追加功能 |
| 1.1 | 添加结构体和表格追加支持 |
| 1.2 | 扩展错误处理和性能优化选项 |
| 2.0 | 添加元数据支持和高级数据转换功能 |

## 参考

1. Lumerical Script Language Reference - Append Command
2. Lumerical Python API Documentation - append() Method
3. MATLAB Array Manipulation Documentation
4. Numerical Data Processing Techniques

---

*最后更新: 2026-01-31*  
*文档版本: 2.0*