## 概述

`bentwaveguide` 命令用于设置弯曲波导的参数。弯曲波导是集成光子学中的基本组件，用于实现光路转向、环形谐振器、马赫-曾德尔干涉仪等结构。该命令支持多种弯曲类型（圆弧、S形、欧拉弯曲等），可以精确控制弯曲半径、过渡长度、损耗等参数。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
bentwaveguide;
```

### Python API (Lumapi)
```python
session.bentwaveguide()
```

## 参数

`bentwaveguide` 命令没有直接参数，但需要通过后续的 `set` 命令配置弯曲类型、几何参数和物理属性。

## 配置属性

设置弯曲波导后，可以使用 `set` 命令配置以下属性：

### 1. 基本几何参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "bent_waveguide" | 弯曲波导名称 |
| `bend type` | string | "circular" | 弯曲类型："circular", "s_bend", "euler", "bezier", "custom" |
| `radius` | float | 5e-6 | 弯曲半径 (m) |
| `bend angle` | float | 90 | 弯曲角度 (度) |
| `start point` | vector | [0, 0, 0] | 起始点坐标 (x, y, z) (m) |
| `end point` | vector | [5e-6, 5e-6, 0] | 终止点坐标 (m) |
| `center point` | vector | [0, 5e-6, 0] | 圆心坐标（圆弧弯曲） (m) |

### 2. 波导横截面
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `width` | float | 0.5e-6 | 波导宽度 (m) |
| `height` | float | 0.22e-6 | 波导高度 (m) |
| `core material` | string | "Si" | 纤芯材料 |
| `cladding material` | string | "SiO2" | 包层材料 |
| `sidewall angle` | float | 90 | 侧壁角度 (度) |
| `etch depth` | float | 0.22e-6 | 刻蚀深度 (m) |

### 3. S形弯曲参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `s_bend_length` | float | 10e-6 | S形弯曲总长度 (m) |
| `s_bend_offset` | float | 2e-6 | S形弯曲横向偏移 (m) |
| `transition_length` | float | 5e-6 | 过渡区长度 (m) |
| `smoothness` | float | 0.5 | 平滑度参数 (0-1) |
| `symmetric` | bool | true | 是否对称S形弯曲 |

### 4. 欧拉弯曲参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `euler_order` | int | 3 | 欧拉弯曲阶数 |
| `curvature_limit` | float | 1e6 | 曲率极限 (1/m) |
| `curvature_rate` | float | 1e12 | 曲率变化率 (1/m²) |
| `min_radius` | float | 2e-6 | 最小曲率半径 (m) |
| `max_radius` | float | 20e-6 | 最大曲率半径 (m) |

### 5. 贝塞尔曲线参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `control_points` | array | [] | 控制点坐标数组 |
| `bezier_order` | int | 3 | 贝塞尔曲线阶数 |
| `tension` | float | 0.5 | 张力参数 (0-1) |
| `continuity` | string | "C2" | 连续性要求："C0", "C1", "C2" |

### 6. 损耗参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `bend_loss` | float | 0 | 弯曲损耗 (dB/90°) |
| `radiation_loss` | float | 自动计算 | 辐射损耗 (dB/m) |
| `mode_mismatch_loss` | float | 自动计算 | 模式失配损耗 (dB) |
| `transition_loss` | float | 自动计算 | 过渡区损耗 (dB) |
| `total_loss` | float | 自动计算 | 总损耗 (dB) |

### 7. 模式特性
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `effective_index` | float | 自动计算 | 有效折射率 |
| `group_index` | float | 自动计算 | 群折射率 |
| `confinement_factor` | float | 自动计算 | 限制因子 |
| `mode_profile` | string | "fundamental" | 模式剖面类型 |
| `polarization` | string | "TE" | 偏振模式："TE", "TM", "both" |

### 8. 网格设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mesh_accuracy` | int | 2 | 网格精度 (1-5) |
| `mesh_refinement` | int | 3 | 网格细化次数 |
| `bend_mesh_density` | float | 2.0 | 弯曲区网格密度因子 |
| `conformal_mesh` | bool | true | 是否使用共形网格 |
| `subpixel_smoothing` | bool | true | 是否使用子像素平滑 |

### 9. 仿真设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `wavelength` | float | 1.55e-6 | 仿真波长 (m) |
| `wavelength_range` | vector | [1.5e-6, 1.6e-6] | 波长范围 (m) |
| `frequency_points` | int | 101 | 频率点数 |
| `solver_type` | string | "FDE" | 求解器类型："FDE", "varFDTD", "EME" |
| `boundary_conditions` | string | "PML" | 边界条件 |

### 10. 优化参数
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `optimization_enabled` | bool | false | 是否启用优化 |
| `objective_function` | string | "minimize_loss" | 目标函数 |
| `optimization_variables` | array | ["radius", "width"] | 优化变量列表 |
| `constraints` | dict | {} | 优化约束 |
| `tolerance` | float | 1e-6 | 优化容差 |

### 11. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `taper_enabled` | bool | false | 是否启用锥形过渡 |
| `taper_length` | float | 0 | 锥形长度 (m) |
| `taper_type` | string | "linear" | 锥形类型 |
| `curvature_compensation` | bool | false | 是否启用曲率补偿 |
| `dispersion_compensation` | bool | false | 是否启用色散补偿 |

### 12. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `save_results` | bool | true | 是否保存结果 |
| `result_format` | string | "mat" | 结果格式 |
| `visualization` | bool | true | 是否可视化 |
| `animation` | bool | false | 是否生成动画 |

## 使用示例

### 示例 1：基本圆弧弯曲波导
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 创建圆弧弯曲波导
session.bentwaveguide()
session.set("name", "circular_bend_90deg")
session.set("bend type", "circular")

# 配置几何参数
session.set("radius", 10e-6)      # 10 μm 半径
session.set("bend angle", 90)     # 90度弯曲
session.set("start point", [0, 0, 0])
session.set("center point", [0, 10e-6, 0])  # 圆心在 (0, 10μm)

# 配置波导横截面
session.set("width", 0.5e-6)      # 500 nm 宽度
session.set("height", 0.22e-6)    # 220 nm 高度
session.set("core material", "Si (Silicon) - Palik")
session.set("cladding material", "SiO2 (Glass) - Palik")

# 配置仿真设置
session.set("wavelength", 1.55e-6)  # 1550 nm
session.set("wavelength_range", [1.5e-6, 1.6e-6])  # C波段
session.set("polarization", "TE")

# 运行模式分析
session.runmode()

# 获取结果
neff = session.getdata("circular_bend_90deg", "neff")
loss = session.getdata("circular_bend_90deg", "loss")
print(f"Effective index: {neff:.4f}")
print(f"Bend loss: {loss:.4f} dB/90°")

# 可视化
session.select("circular_bend_90deg")
session.set("visualization", True)
session.set("opacity", 0.8)
```

### 示例 2：低损耗S形弯曲波导
```python
import lumapi

session = lumapi.MODE()

# 创建低损耗S形弯曲波导
session.bentwaveguide()
session.set("name", "low_loss_s_bend")
session.set("bend type", "s_bend")

# 配置S形弯曲参数
session.set("s_bend_length", 20e-6)      # 20 μm 总长度
session.set("s_bend_offset", 5e-6)       # 5 μm 横向偏移
session.set("transition_length", 8e-6)   # 8 μm 过渡长度
session.set("smoothness", 0.7)           # 高平滑度
session.set("symmetric", True)           # 对称S形

# 配置波导尺寸（优化用于低损耗）
session.set("width", 0.45e-6)      # 450 nm 宽度（稍窄以减少辐射）
session.set("height", 0.25e-6)     # 250 nm 高度（稍高以增强限制）

# 配置高级模式设置
session.set("mode_profile", "fundamental")
session.set("polarization", "TE")

# 配置网格设置（精细网格以准确计算损耗）
session.set("mesh_accuracy", 3)
session.set("mesh_refinement", 4)
session.set("bend_mesh_density", 3.0)  # 弯曲区3倍网格密度

# 配置仿真波长扫描
wavelengths = [1.31e-6, 1.55e-6, 1.65e-6]  # 多个通信波长
loss_results = []

for i, wavelength in enumerate(wavelengths):
    session.set("wavelength", wavelength)
    session.runmode()
    
    # 获取损耗
    total_loss = session.getdata("low_loss_s_bend", "total_loss")
    bend_loss = session.getdata("low_loss_s_bend", "bend_loss")
    radiation_loss = session.getdata("low_loss_s_bend", "radiation_loss")
    
    loss_results.append({
        "wavelength_nm": wavelength * 1e9,
        "total_loss_db": total_loss,
        "bend_loss_db": bend_loss,
        "radiation_loss_db": radiation_loss
    })
    
    print(f"λ = {wavelength*1e9:.0f} nm: "
          f"Total loss = {total_loss:.4f} dB, "
          f"Bend loss = {bend_loss:.4f} dB, "
          f"Radiation loss = {radiation_loss:.4f} dB")

# 分析最佳波长
best_result = min(loss_results, key=lambda x: x["total_loss_db"])
print(f"\nBest performance at {best_result['wavelength_nm']} nm: "
      f"{best_result['total_loss_db']:.4f} dB total loss")
```

### 示例 3：欧拉弯曲用于紧凑型转弯
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 创建欧拉弯曲波导（用于紧凑低损耗转弯）
session.bentwaveguide()
session.set("name", "euler_bend_compact")
session.set("bend type", "euler")

# 配置欧拉弯曲参数
session.set("euler_order", 3)           # 3阶欧拉弯曲
session.set("radius", 3e-6)             # 3 μm 设计半径
session.set("bend angle", 90)           # 90度转弯
session.set("curvature_limit", 2e6)     # 最大曲率 2×10⁶ 1/m
session.set("curvature_rate", 5e11)     # 曲率变化率

# 配置紧凑型波导
session.set("width", 0.4e-6)            # 400 nm 宽度（紧凑设计）
session.set("height", 0.18e-6)          # 180 nm 高度

# 配置锥形过渡（减少模式失配）
session.set("taper_enabled", True)
session.set("taper_length", 2e-6)       # 2 μm 锥形长度
session.set("taper_type", "parabolic")  # 抛物线锥形

# 配置曲率补偿（优化弯曲轮廓）
session.set("curvature_compensation", True)

# 配置优化设置
session.set("optimization_enabled", True)
session.set("objective_function", "minimize_loss")
session.set("optimization_variables", ["radius", "taper_length", "euler_order"])
session.set("constraints", {
    "radius >= 2e-6": True,
    "taper_length <= 5e-6": True,
    "total_length <= 15e-6": True
})
session.set("tolerance", 1e-5)

# 运行优化
print("Starting Euler bend optimization...")
session.runoptimization()

# 获取优化结果
opt_radius = session.getdata("euler_bend_compact", "optimized_radius")
opt_taper_length = session.getdata("euler_bend_compact", "optimized_taper_length")
opt_loss = session.getdata("euler_bend_compact", "optimized_loss")

print(f"Optimized radius: {opt_radius*1e6:.2f} μm")
print(f"Optimized taper length: {opt_taper_length*1e6:.2f} μm")
print(f"Optimized loss: {opt_loss:.4f} dB")

# 与圆弧弯曲比较
session.bentwaveguide()
session.set("name", "circular_bend_comparison")
session.set("bend type", "circular")
session.set("radius", opt_radius)
session.set("bend angle", 90)
session.set("width", 0.4e-6)
session.set("height", 0.18e-6)
session.runmode()

circular_loss = session.getdata("circular_bend_comparison", "loss")
improvement = (circular_loss - opt_loss) / circular_loss * 100

print(f"\nComparison with circular bend:")
print(f"  Circular bend loss: {circular_loss:.4f} dB")
print(f"  Euler bend loss: {opt_loss:.4f} dB")
print(f"  Improvement: {improvement:.1f}%")
```

### 示例 4：复杂贝塞尔弯曲波导阵列
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 定义复杂弯曲路径的控制点
control_points = [
    [0, 0, 0],          # 起点
    [5e-6, 2e-6, 0],    # 控制点1
    [10e-6, -3e-6, 0],  # 控制点2
    [15e-6, 5e-6, 0],   # 控制点3
    [20e-6, 0, 0]       # 终点
]

# 创建贝塞尔弯曲波导
session.bentwaveguide()
session.set("name", "bezier_bend_complex")
session.set("bend type", "bezier")
session.set("control_points", control_points)
session.set("bezier_order", 4)  # 4阶贝塞尔曲线

# 配置波导参数
session.set("width", 0.5e-6)
session.set("height", 0.22e-6)
session.set("tension", 0.6)      # 中等张力
session.set("continuity", "C2")  # 二阶连续

# 创建弯曲波导阵列（参数扫描）
radii = [3e-6, 5e-6, 8e-6, 12e-6]
widths = [0.4e-6, 0.5e-6, 0.6e-6]
results = []

for i, radius in enumerate(radii):
    for j, width in enumerate(widths):
        # 复制并修改参数
        bend_name = f"bend_array_r{int(radius*1e6)}_w{int(width*1e9)}"
        session.copy()
        session.set("target", "bezier_bend_complex")
        session.set("new name", bend_name)
        
        # 更新参数
        session.setnamed(bend_name, "radius", radius)
        session.setnamed(bend_name, "width", width)
        
        # 运行分析
        session.runmode()
        
        # 收集结果
        loss = session.getdata(bend_name, "total_loss")
        neff = session.getdata(bend_name, "effective_index")
        length = session.getdata(bend_name, "total_length")
        
        results.append({
            "name": bend_name,
            "radius_um": radius * 1e6,
            "width_nm": width * 1e9,
            "loss_db": loss,
            "neff": neff,
            "length_um": length * 1e6
        })
        
        print(f"{bend_name}: "
              f"R={radius*1e6:.0f}μm, "
              f"W={width*1e9:.0f}nm, "
              f"Loss={loss:.4f}dB, "
              f"Length={length*1e6:.1f}μm")

# 找到最佳设计（最低损耗）
best_design = min(results, key=lambda x: x["loss_db"])
print(f"\nBest design: {best_design['name']}")
print(f"  Radius: {best_design['radius_um']:.0f} μm")
print(f"  Width: {best_design['width_nm']:.0f} nm")
print(f"  Loss: {best_design['loss_db']:.4f} dB")
print(f"  Length: {best_design['length_um']:.1f} μm")

# 创建损耗与半径/宽度的等高线图
import matplotlib.pyplot as plt

# 提取数据用于绘图
radius_vals = sorted(set(r["radius_um"] for r in results))
width_vals = sorted(set(r["width_nm"] for r in results))
loss_matrix = np.zeros((len(radius_vals), len(width_vals)))

for r in results:
    i = radius_vals.index(r["radius_um"])
    j = width_vals.index(r["width_nm"])
    loss_matrix[i, j] = r["loss_db"]

# 创建等高线图
plt.figure(figsize=(10, 8))
X, Y = np.meshgrid(width_vals, radius_vals)
contour = plt.contourf(X, Y, loss_matrix, 20, cmap='viridis')
plt.colorbar(contour, label='Loss (dB)')
plt.contour(X, Y, loss_matrix, 10, colors='black', linewidths=0.5, alpha=0.5)

# 标记最佳设计
plt.scatter(best_design["width_nm"], best_design["radius_um"], 
            color='red', s=100, marker='*', label='Best Design')

plt.xlabel('Waveguide Width (nm)')
plt.ylabel('Bend Radius (μm)')
plt.title('Bend Loss vs. Width and Radius')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('bend_optimization_contour.png', dpi=150)
plt.close()

print("Contour plot saved as 'bend_optimization_contour.png'")
```

## 注意事项

1. **弯曲半径限制**：过小的弯曲半径会导致高辐射损耗，通常需要半径 > 3×波导宽度
2. **模式匹配**：弯曲波导与直波导连接处需要注意模式匹配以减少插入损耗
3. **网格收敛**：弯曲区域需要更精细的网格以确保计算精度
4. **偏振依赖性**：弯曲损耗通常与偏振有关，需要分别评估TE和TM模式
5. **制造公差**：实际制造中的尺寸偏差会影响弯曲性能，需要容差分析
6. **热效应**：高功率应用中，弯曲波导可能产生不均匀的热分布
7. **非线性效应**：弯曲可能增强非线性效应，需要特别关注
8. **串扰**：密集弯曲波导阵列中需要注意相邻波导间的串扰

## 产品支持

- **FDTD Solutions**: 支持弯曲波导的时域分析
- **MODE Solutions**: 支持弯曲波导的模式分析和优化（主要应用）
- **DEVICE**: 支持弯曲波导的热学、电学分析
- **INTERCONNECT**: 支持弯曲波导的电路模型

## 相关命令

- `addwaveguide` - 添加直波导
- `addbend` - 添加弯曲结构
- `addspline` - 添加样条曲线
- `set` - 设置弯曲参数
- `getbend` - 获取弯曲结果
- `optimizebend` - 优化弯曲设计
- `plotbend` - 绘制弯曲特性