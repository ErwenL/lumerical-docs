# cascadedsmatrix

## 概述

`cascadedsmatrix` 命令用于计算级联 S 参数矩阵。在光子集成电路和射频电路分析中，复杂系统通常由多个组件级联而成，每个组件有其自身的 S 参数矩阵。该命令能够将多个 S 矩阵按照指定连接方式级联，得到整个系统的等效 S 矩阵，是系统级仿真和网络分析的关键工具。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
cascadedsmatrix;
```

### Python API (Lumapi)
```python
session.cascadedsmatrix()
```

## 参数

`cascadedsmatrix` 命令没有直接参数，但需要通过后续的 `set` 命令配置级联配置、输入矩阵和计算选项。

## 配置属性

计算级联 S 矩阵后，可以使用 `set` 命令配置以下属性：

### 1. 基本设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "cascaded_smatrix" | 级联矩阵名称 |
| `operation` | string | "cascade" | 操作类型："cascade", "deembed", "parallel", "series", "hybrid" |
| `num matrices` | int | 2 | S 矩阵数量 |
| `port mapping` | matrix | [] | 端口映射矩阵 |
| `reference planes` | array | [] | 参考平面位置 |

### 2. S 矩阵输入配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `s matrices` | array | [] | S 矩阵数组 |
| `matrix names` | array | [] | 矩阵名称数组 |
| `matrix files` | array | [] | 矩阵文件路径数组 |
| `data format` | string | "complex" | 数据格式："complex", "magnitude_phase", "db_phase", "real_imag" |
| `frequency points` | int | 0 | 频率点数（0 表示自动检测） |

### 3. 级联配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `cascade order` | array | [] | 级联顺序数组 |
| `connection matrix` | matrix | [] | 连接矩阵 |
| `port connections` | dict | {} | 端口连接字典 |
| `impedance matching` | bool | true | 是否阻抗匹配 |
| `port renormalization` | bool | false | 是否端口重归一化 |

### 4. 级联算法设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `algorithm` | string | "tmatrix" | 级联算法："tmatrix", "abcd", "scattering", "wave" |
| `method` | string | "direct" | 计算方法："direct", "iterative", "recursive" |
| `precision` | int | 16 | 计算精度（有效数字） |
| `tolerance` | float | 1e-12 | 计算容差 |
| `stabilization` | bool | true | 是否启用数值稳定化 |

### 5. T 矩阵方法
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `t matrix conversion` | string | "standard" | T 矩阵转换方法 |
| `t matrix order` | string | "forward" | T 矩阵顺序："forward", "reverse" |
| `normalize t matrix` | bool | true | 是否归一化 T 矩阵 |

### 6. ABCD 矩阵方法
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `abcd matrix conversion` | string | "standard" | ABCD 矩阵转换方法 |
| `chain parameter` | bool | false | 是否使用链式参数 |
| `normalize abcd` | bool | true | 是否归一化 ABCD 矩阵 |

### 7. 去嵌配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `deembedding ports` | array | [] | 去嵌端口列表 |
| `deembedding method` | string | "thru" | 去嵌方法："thru", "line", "reflect", "load" |
| `calibration standards` | dict | {} | 校准标准字典 |
| `error terms` | array | [] | 误差项数组 |

### 8. 并行连接配置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parallel ports` | array | [] | 并行连接端口列表 |
| `parallel type` | string | "shunt" | 并行类型："shunt", "series", "mixed" |
| `admittance matrix` | matrix | [] | 导纳矩阵 |
| `impedance matrix` | matrix | [] | 阻抗矩阵 |

### 9. 频率处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency vector` | array | [] | 频率向量 (Hz) |
| `frequency interpolation` | string | "linear" | 频率插值："linear", "spline", "log" |
| `frequency alignment` | bool | true | 是否频率对齐 |
| `common frequency` | array | [] | 公共频率向量 |

### 10. 端口处理
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `port numbering` | string | "sequential" | 端口编号方式 |
| `port reordering` | array | [] | 端口重排序数组 |
| `port reduction` | bool | false | 是否端口约简 |
| `internal ports` | array | [] | 内部端口列表 |

### 11. 结果输出
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `output format` | string | "complex" | 输出格式 |
| `save result` | bool | true | 是否保存结果 |
| `result file` | string | "" | 结果文件路径 |
| `visualization` | bool | false | 是否可视化 |
| `export format` | string | "mat" | 导出格式 |

### 12. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `causality enforcement` | bool | false | 是否强制因果性 |
| `passivity enforcement` | bool | false | 是否强制无源性 |
| `reciprocity enforcement` | bool | false | 是否强制互易性 |
| `noise correlation` | bool | false | 是否计算噪声相关矩阵 |
| `thermal noise` | bool | false | 是否考虑热噪声 |

## 返回值

`cascadedsmatrix` 命令计算并返回级联后的 S 参数矩阵。在 Python API 中，`session.cascadedsmatrix()` 创建一个级联计算对象，计算完成后可以通过 `getdata` 方法获取结果 S 矩阵。返回的 S 矩阵是一个复数数组，维度为 [频率点数 × 外部端口数 × 外部端口数]。

## 示例

### 示例 1：基本两级组件级联
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 定义两个组件的 S 矩阵（2×2，单频率点）
# 组件1：3dB 耦合器
s1 = np.array([[[0.0, 0.707],   # S11, S12
                [0.707, 0.0]]])  # S21, S22

# 组件2：波导（相位延迟）
phase_shift = np.exp(1j*np.pi/4)  # 45度相移
s2 = np.array([[[0.0, phase_shift],
                [phase_shift, 0.0]]])

# 计算级联 S 矩阵
session.cascadedsmatrix()
session.set("name", "cascade_2stage")
session.set("s matrices", [s1.tolist(), s2.tolist()])
session.set("cascade order", [0, 1])  # 先组件1，后组件2
session.set("port connections", {0: {"out1": 1, "in2": 0}})  # 组件1输出1连接到组件2输入0
session.set("algorithm", "tmatrix")
session.set("operation", "cascade")

# 计算
session.runcascade()

# 获取结果
result = session.getdata("cascade_2stage", "s_matrix")
print(f"Cascaded S matrix shape: {np.array(result).shape}")
print(f"S11: {result[0][0][0]:.4f}")
print(f"S12: {result[0][0][1]:.4f}")
print(f"S21: {result[0][1][0]:.4f}")
print(f"S22: {result[0][1][1]:.4f}")

# 验证：级联后应为 3dB 耦合器 + 45度相移
expected_s21 = 0.707 * phase_shift
print(f"Expected S21: {expected_s21:.4f}")
print(f"Actual S21: {result[0][1][0]:.4f}")
print(f"Error: {abs(result[0][1][0] - expected_s21):.6f}")
```

### 示例 2：多频率点级联（滤波器链）
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 创建多频率点 S 矩阵数据
num_freq = 101
frequencies = np.linspace(150e12, 200e12, num_freq)  # 150-200 THz

# 组件1：环形谐振器（频率选择性）
def ring_resonator_smatrix(freq, f0=175e12, bandwidth=5e12):
    """环形谐振器 S 矩阵（简化模型）"""
    s = np.zeros((2, 2), dtype=complex)
    detuning = (freq - f0) / (bandwidth/2)
    transmission = 1 - 0.8 / (1 + detuning**2)  # 洛伦兹型响应
    reflection = np.sqrt(1 - abs(transmission)**2)
    
    s[0, 0] = reflection  # S11
    s[0, 1] = transmission  # S12
    s[1, 0] = transmission  # S21
    s[1, 1] = reflection  # S22
    
    return s

# 组件2：波导（频率相关相移）
def waveguide_smatrix(freq, length=100e-6, neff=2.4):
    """波导 S 矩阵（纯相移）"""
    s = np.zeros((2, 2), dtype=complex)
    phase = 2*np.pi * neff * length * freq / 3e8
    s[0, 1] = np.exp(1j*phase)  # S12
    s[1, 0] = np.exp(1j*phase)  # S21
    return s

# 组件3：MMI 耦合器（宽带）
def mmi_smatrix(freq, coupling=0.5):
    """MMI 耦合器 S 矩阵（宽带近似）"""
    s = np.zeros((2, 2), dtype=complex)
    s[0, 1] = np.sqrt(coupling)  # S12
    s[1, 0] = np.sqrt(coupling)  # S21
    s[0, 0] = np.sqrt(1-coupling)  # S11
    s[1, 1] = np.sqrt(1-coupling)  # S22
    return s

# 生成频率相关的 S 矩阵
s_matrices = []
for i, f in enumerate(frequencies):
    # 三个组件的 S 矩阵
    s_ring = ring_resonator_smatrix(f, f0=175e12, bandwidth=8e12)
    s_wg = waveguide_smatrix(f, length=50e-6, neff=2.4)
    s_mmi = mmi_smatrix(f, coupling=0.5)
    
    # 组合成 3×3×2×2 矩阵（频率×组件×端口×端口）
    s_matrices.append([s_ring.tolist(), s_wg.tolist(), s_mmi.tolist()])

# 计算级联
session.cascadedsmatrix()
session.set("name", "filter_chain_cascade")
session.set("s matrices", s_matrices)
session.set("frequency vector", frequencies.tolist())
session.set("cascade order", [0, 1, 2])  # 环形→波导→MMI
session.set("port connections", {
    0: {"out1": 1, "in2": 0},  # 环形输出到波导输入
    1: {"out1": 2, "in2": 0}   # 波导输出到MMI输入
})
session.set("algorithm", "tmatrix")
session.set("frequency interpolation", "spline")
session.set("frequency alignment", True)

# 运行级联计算
print("Computing cascaded S matrix for filter chain...")
session.runcascade()

# 获取结果并分析
result = session.getdata("filter_chain_cascade", "s_matrix")
result_freq = session.getdata("filter_chain_cascade", "frequencies")

# 提取传输响应
transmission = np.abs(result[:, 1, 0])  # S21 幅度
phase = np.angle(result[:, 1, 0])      # S21 相位

# 找到谐振频率（最小传输）
min_idx = np.argmin(transmission)
resonant_freq = result_freq[min_idx]
min_transmission = transmission[min_idx]

print(f"Filter chain analysis:")
print(f"  Resonant frequency: {resonant_freq/1e12:.2f} THz")
print(f"  Minimum transmission: {20*np.log10(min_transmission):.2f} dB")
print(f"  3dB bandwidth: {np.sum(transmission < 0.707)* (frequencies[1]-frequencies[0])/1e9:.2f} GHz")

# 绘制响应
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(result_freq/1e12, 20*np.log10(transmission))
plt.axvline(resonant_freq/1e12, color='r', linestyle='--', alpha=0.5)
plt.xlabel('Frequency (THz)')
plt.ylabel('Transmission (dB)')
plt.title('Filter Chain Transmission')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(result_freq/1e12, np.unwrap(phase))
plt.xlabel('Frequency (THz)')
plt.ylabel('Phase (rad)')
plt.title('Filter Chain Phase Response')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('filter_chain_response.png', dpi=150)
plt.close()

print("Response plot saved as 'filter_chain_response.png'")
```

### 示例 3：复杂网络去嵌和并行连接
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 创建测试夹具和待测器件（DUT）的 S 矩阵
num_freq = 51
freq = np.linspace(140e12, 160e12, num_freq)

# 夹具1（输入侧）：传输线模型
def fixture1_smatrix(f):
    l = 10e-6  # 长度
    neff = 2.4
    atten = 0.2  # dB/mm
    phase = 2*np.pi * neff * l * f / 3e8
    loss = 10**(-atten*l*1e3/20)  # 转换为线性
    
    s = np.array([[0.0, loss*np.exp(1j*phase)],
                  [loss*np.exp(1j*phase), 0.0]])
    return s

# 夹具2（输出侧）：类似但不同参数
def fixture2_smatrix(f):
    l = 15e-6
    neff = 2.4
    atten = 0.15
    phase = 2*np.pi * neff * l * f / 3e8
    loss = 10**(-atten*l*1e3/20)
    
    s = np.array([[0.0, loss*np.exp(1j*phase)],
                  [loss*np.exp(1j*phase), 0.0]])
    return s

# DUT：马赫-曾德尔干涉仪（MZI）
def dut_smatrix(f):
    # MZI 的简化模型：两个耦合器 + 相位差
    delta_L = 20e-6  # 路径差
    neff = 2.4
    delta_phi = 2*np.pi * neff * delta_L * f / 3e8
    
    # 3dB 耦合器矩阵
    k = 1/np.sqrt(2)
    s_coupler = np.array([[0.0, k, k, 0.0],
                          [k, 0.0, 0.0, k],
                          [k, 0.0, 0.0, k],
                          [0.0, k, k, 0.0]])
    
    # 相位差矩阵
    p = np.exp(1j*delta_phi/2)
    phase_mat = np.diag([1.0, p, 1.0, 1.0/p])
    
    # 整体 MZI S 矩阵（4端口）
    s_mzi = s_coupler @ phase_mat @ s_coupler
    return s_mzi

# 生成完整的夹具+DUT+夹具 S 矩阵
s_full = []
s_fixture1 = []
s_fixture2 = []
s_dut = []

for f in freq:
    s_full.append([
        fixture1_smatrix(f).tolist(),
        dut_smatrix(f).tolist(),
        fixture2_smatrix(f).tolist()
    ])
    s_fixture1.append(fixture1_smatrix(f).tolist())
    s_fixture2.append(fixture2_smatrix(f).tolist())
    s_dut.append(dut_smatrix(f).tolist())

# 1. 去嵌：从完整测量中去除夹具影响
session.cascadedsmatrix()
session.set("name", "deembedded_dut")
session.set("s matrices", s_full)
session.set("frequency vector", freq.tolist())
session.set("operation", "deembed")
session.set("deembedding ports", [0, 3])  # 去嵌端口 0 和 3
session.set("deembedding method", "thru")
session.set("calibration standards", {
    "thru": s_fixture1 + s_fixture2,  # 直通标准
    "reflect": [np.array([[0.1, 0], [0, 0.1]]).tolist()]*num_freq  # 反射标准
})
session.set("algorithm", "abcd")

print("Deembedding DUT from fixture measurements...")
session.runcascade()

# 2. 并行连接：两个相同的 MZI 并行
session.cascadedsmatrix()
session.set("name", "parallel_mzi")
session.set("s matrices", s_dut * 2)  # 两个相同的 DUT
session.set("frequency vector", freq.tolist())
session.set("operation", "parallel")
session.set("parallel ports", [[0, 2], [1, 3]])  # 输入端口并行，输出端口并行
session.set("parallel type", "shunt")
session.set("impedance matching", True)

print("Computing parallel connection of two MZIs...")
session.runcascade()

# 3. 混合连接：串联+并行
session.cascadedsmatrix()
session.set("name", "hybrid_network")
# 创建三个不同的组件
s_components = [
    s_dut,  # MZI
    s_fixture1,  # 传输线
    s_dut  # 另一个 MZI
]
session.set("s matrices", s_components)
session.set("frequency vector", freq.tolist())
session.set("operation", "hybrid")
session.set("connection matrix", [
    [0, 1, 0, 0],  # 组件0输出1连接到组件1输入0
    [1, 0, 2, 0],  # 组件1输出0连接到组件2输入0
    [0, 0, 1, 0]   # 组件2输出1是最终输出
])
session.set("port reordering", [0, 3])  # 保留端口0和3作为外部端口

print("Computing hybrid series-parallel network...")
session.runcascade()

# 获取所有结果
deembedded = session.getdata("deembedded_dut", "s_matrix")
parallel = session.getdata("parallel_mzi", "s_matrix")
hybrid = session.getdata("hybrid_network", "s_matrix")

print(f"\nNetwork analysis results:")
print(f"  Deembedded DUT shape: {np.array(deembedded).shape}")
print(f"  Parallel MZI shape: {np.array(parallel).shape}")
print(f"  Hybrid network shape: {np.array(hybrid).shape}")

# 分析传输特性
f0_idx = num_freq // 2  # 中心频率
deembedded_trans = np.abs(deembedded[f0_idx][1][0])
parallel_trans = np.abs(parallel[f0_idx][1][0])
hybrid_trans = np.abs(hybrid[f0_idx][1][0])

print(f"\nTransmission at {freq[f0_idx]/1e12:.1f} THz:")
print(f"  Deembedded DUT: {20*np.log10(deembedded_trans):.2f} dB")
print(f"  Parallel MZIs: {20*np.log10(parallel_trans):.2f} dB")
print(f"  Hybrid network: {20*np.log10(hybrid_trans):.2f} dB")
```

### 示例 4：大型光子集成电路级联
```python
import lumapi
import numpy as np

session = lumapi.INTERCONNECT()

# 模拟大型 PIC 的组件库
component_types = {
    "waveguide": {
        "func": lambda f, l: np.array([[0.0, np.exp(1j*2*np.pi*2.4*l*f/3e8)],
                                      [np.exp(1j*2*np.pi*2.4*l*f/3e8), 0.0]]),
        "params": {"l": [10e-6, 50e-6, 100e-6]}
    },
    "coupler": {
        "func": lambda f, k: np.array([[np.sqrt(1-k), np.sqrt(k)],
                                      [np.sqrt(k), np.sqrt(1-k)]]),
        "params": {"k": [0.5, 0.3, 0.7]}  # 耦合系数
    },
    "filter": {
        "func": lambda f, f0, bw: np.array([[0.0, 1-0.8/(1+((f-f0)/(bw/2))**2)],
                                           [1-0.8/(1+((f-f0)/(bw/2))**2), 0.0]]),
        "params": {"f0": [1550e12, 1570e12], "bw": [10e12, 20e12]}
    },
    "phase_shifter": {
        "func": lambda f, phi: np.array([[0.0, np.exp(1j*phi)],
                                        [np.exp(1j*phi), 0.0]]),
        "params": {"phi": [0, np.pi/2, np.pi]}
    }
}

# 生成随机 PIC 拓扑
num_components = 20
num_freq = 31
freq = np.linspace(150e12, 160e12, num_freq)

# 创建组件实例
components = []
for i in range(num_components):
    comp_type = np.random.choice(list(component_types.keys()))
    params = component_types[comp_type]["params"]
    
    # 随机选择参数
    selected_params = {}
    for key, values in params.items():
        selected_params[key] = np.random.choice(values)
    
    # 生成频率相关的 S 矩阵
    s_matrix = []
    for f in freq:
        s = component_types[comp_type]["func"](f, **selected_params)
        s_matrix.append(s.tolist())
    
    components.append({
        "type": comp_type,
        "params": selected_params,
        "s_matrix": s_matrix,
        "num_ports": 2  # 简化为2端口
    })

# 创建随机连接拓扑
connections = []
for i in range(num_components - 1):
    # 随机连接组件
    if np.random.random() > 0.3:  # 70% 概率连接
        connections.append({
            "from": i,
            "from_port": 1,  # 输出端口
            "to": i + 1,
            "to_port": 0     # 输入端口
        })

# 添加一些反馈或分支连接
if num_components > 5:
    # 添加一个反馈环
    connections.append({"from": num_components-1, "from_port": 1, 
                       "to": 2, "to_port": 0})
    # 添加一个分支
    connections.append({"from": 3, "from_port": 1, 
                       "to": 6, "to_port": 0})

# 准备级联计算
s_matrices = [comp["s_matrix"] for comp in components]

session.cascadedsmatrix()
session.set("name", "large_pic_cascade")
session.set("s matrices", s_matrices)
session.set("frequency vector", freq.tolist())
session.set("operation", "cascade")

# 构建连接矩阵
port_connections = {}
for conn in connections:
    key = conn["from"]
    if key not in port_connections:
        port_connections[key] = {}
    port_connections[key][f"out{conn['from_port']}"] = conn["to"]

session.set("port connections", port_connections)

# 配置高级选项
session.set("algorithm", "tmatrix")
session.set("method", "recursive")  # 递归方法适合大型网络
session.set("precision", 12)
session.set("stabilization", True)
session.set("port reduction", True)
session.set("internal ports", list(range(1, num_components-1)))

# 运行级联计算
print(f"Computing cascaded S matrix for {num_components}-component PIC...")
print(f"  Frequency points: {num_freq}")
print(f"  Connections: {len(connections)}")
print(f"  Using recursive T-matrix method...")

import time
start_time = time.time()
session.runcascade()
end_time = time.time()

# 获取结果
result = session.getdata("large_pic_cascade", "s_matrix")
result_freq = session.getdata("large_pic_cascade", "frequencies")

computation_time = end_time - start_time
print(f"\nComputation completed in {computation_time:.2f} seconds")
print(f"Result S matrix shape: {np.array(result).shape}")

# 分析系统性能
transmission = np.abs(result[:, 1, 0])  # S21
reflection = np.abs(result[:, 0, 0])    # S11

print(f"\nSystem performance:")
print(f"  Average transmission: {20*np.log10(np.mean(transmission)):.2f} dB")
print(f"  Minimum transmission: {20*np.log10(np.min(transmission)):.2f} dB")
print(f"  Maximum reflection: {20*np.log10(np.max(reflection)):.2f} dB")

# 识别谐振频率
peaks, _ = find_peaks(-transmission, height=0.5)
if len(peaks) > 0:
    print(f"  Found {len(peaks)} resonance(s):")
    for i, peak in enumerate(peaks[:3]):  # 显示前3个谐振
        print(f"    Resonance {i+1}: {result_freq[peak]/1e12:.2f} THz, "
              f"Depth: {20*np.log10(transmission[peak]):.2f} dB")

# 保存结果供后续分析
session.eval(f"""
cascade_result = struct;
cascade_result.s_matrix = {result.tolist()};
cascade_result.frequencies = {result_freq.tolist()};
cascade_result.components = {components};
cascade_result.connections = {connections};
cascade_result.computation_time = {computation_time};
save('large_pic_cascade_result.mat', 'cascade_result');
""")

print(f"\nResults saved to 'large_pic_cascade_result.mat'")
```

## 注意事项

1. **数值稳定性**：大型网络或高频下的级联计算可能数值不稳定，需要启用稳定化选项
2. **端口匹配**：确保级联组件的端口阻抗匹配，否则需要重归一化
3. **频率对齐**：不同组件的频率点可能不同，需要适当的插值和对齐
4. **因果性和无源性**：级联后的 S 矩阵应保持因果性和无源性，可能需要后处理强制满足
5. **计算复杂度**：大型网络的级联计算可能耗时，考虑使用递归或分块方法
6. **内存使用**：多频率点、多端口的 S 矩阵可能消耗大量内存
7. **连接验证**：检查端口连接的正确性，避免无效连接或端口冲突
8. **参考平面**：注意组件的参考平面位置，必要时进行去嵌或平移

## 错误处理

使用 `cascadedsmatrix` 命令时可能遇到的常见错误及其解决方案：

### 1. 矩阵维度不匹配
- **错误信息**: "Matrix dimension mismatch"
- **原因**: 输入的 S 矩阵维度与端口数量不一致
- **解决方案**: 检查每个 S 矩阵是否为 N×N 复数矩阵，确保所有矩阵在相同频率点具有相同维度

### 2. 频率向量不匹配
- **错误信息**: "Frequency vector mismatch"
- **原因**: 不同组件的频率点不一致且未启用频率对齐
- **解决方案**: 启用 `frequency alignment` 属性，或提供统一的 `common frequency` 向量

### 3. 连接配置无效
- **错误信息**: "Invalid connection configuration"
- **原因**: 端口连接指定了不存在的端口或组件
- **解决方案**: 检查 `port connections` 字典，确保所有引用的组件索引和端口号有效

### 4. 数值不稳定
- **错误信息**: "Numerical instability detected"
- **原因**: 级联计算中出现奇异矩阵或病态条件
- **解决方案**: 启用 `stabilization` 属性，增加 `precision`，或使用不同的 `algorithm`

### 5. 内存不足
- **错误信息**: "Insufficient memory"
- **原因**: 大型网络或多频率点计算超出可用内存
- **解决方案**: 使用 `port reduction` 减少内部端口，分块计算，或减少频率点数

### 6. 算法不收敛
- **错误信息**: "Algorithm did not converge"
- **原因**: 迭代算法未在最大迭代次数内收敛
- **解决方案**: 增加 `tolerance`，使用 `direct` 方法替代 `iterative`，或检查输入数据的合理性

### 7. Python API 超时
- **错误信息**: "Operation timed out"
- **原因**: 大型网络计算时间过长
- **解决方案**: 设置超时限制，使用进度监控，或优化网络拓扑
  ```python
  import signal
  def timeout_handler(signum, frame):
      raise TimeoutError("Cascade computation timed out")
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(300)  # 5分钟超时
  try:
      session.runcascade()
  except TimeoutError:
      print("Computation timed out, consider simplifying the network")
  finally:
      signal.alarm(0)
  ```

## 产品支持

- **FDTD Solutions**: 不支持（S 参数级联在 INTERCONNECT 中进行）
- **MODE Solutions**: 不支持（组件分析在 MODE 中，级联在 INTERCONNECT）
- **DEVICE**: 不支持
- **INTERCONNECT**: 支持（主要应用）

## 相关命令

- `callsplitter` - 调用分路器模型
- `getsmatrix` - 获取 S 参数矩阵
- `setsmatrix` - 设置 S 参数矩阵
- `importsmatrix` - 导入 S 参数文件
- `exportsmatrix` - 导出 S 参数
- `analyzenetwork` - 分析网络性能
- `optimizenetwork` - 优化网络参数

## 参考

1. Lumerical INTERCONNECT User Guide - S-parameter Cascading
2. Microwave Network Analysis and S-parameter Theory
3. Lumerical Python API Documentation - Network Analysis Module

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含级联算法和配置属性 |
| 1.1 | 2026-01-31 | 添加返回值说明和错误处理章节 |

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*