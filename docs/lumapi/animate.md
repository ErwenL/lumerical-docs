# animate

## 概述

`animate` 命令用于创建仿真结果的动画。动画可以可视化场分布、温度变化、模式演化等动态过程，帮助理解物理现象的时空演变。该命令支持多种动画类型，包括时间动画、参数扫描动画、模式动画等。

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
animate;
```

### Python API (Lumapi)
```python
session.animate()
```

## 参数

`animate` 命令没有直接参数，但需要通过后续的 `set` 命令配置动画类型、数据源和输出设置。

## 配置属性

创建动画后，可以使用 `set` 命令配置以下属性：

### 1. 基本动画设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `name` | string | "animation" | 动画名称 |
| `animation type` | string | "time" | 动画类型："time", "parameter", "frequency", "mode", "custom" |
| `data source` | string | "" | 数据源名称（监视器或结果对象） |
| `enabled` | bool | true | 是否启用动画 |
| `auto play` | bool | true | 是否自动播放 |

### 2. 时间动画设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `time range` | vector | [0, 1e-12] | 时间范围 [start, end] (s) |
| `time steps` | int | 100 | 时间步数 |
| `frame rate` | float | 30 | 帧率 (fps) |
| `time scaling` | string | "linear" | 时间缩放："linear", "log", "custom" |
| `loop mode` | string | "forward" | 循环模式："forward", "reverse", "pingpong", "none" |

### 3. 参数动画设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `parameter name` | string | "" | 参数名称 |
| `parameter range` | vector | [0, 1] | 参数范围 [min, max] |
| `parameter steps` | int | 50 | 参数步数 |
| `parameter values` | array | [] | 参数值数组（自定义序列） |
| `sweep type` | string | "linear" | 扫描类型："linear", "log", "random", "custom" |

### 4. 频率动画设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `frequency range` | vector | [100e12, 200e12] | 频率范围 [min, max] (Hz) |
| `frequency points` | int | 101 | 频率点数 |
| `frequency scaling` | string | "linear" | 频率缩放："linear", "log" |
| `wavelength range` | vector | 自动计算 | 波长范围 [min, max] (m) |

### 5. 模式动画设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `mode index` | int | 1 | 模式索引 |
| `mode range` | vector | [1, 10] | 模式范围 [start, end] |
| `phase sweep` | bool | false | 是否进行相位扫描 |
| `phase range` | vector | [0, 2*pi] | 相位范围 [start, end] (rad) |
| `mode animation` | string | "amplitude" | 模式动画："amplitude", "phase", "both" |

### 6. 可视化设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `field component` | string | "E" | 场分量："E", "H", "P", "T", "custom" |
| `component axis` | string | "magnitude" | 分量轴："x", "y", "z", "magnitude", "all" |
| `color map` | string | "hot" | 颜色映射："hot", "jet", "rainbow", "grayscale", "custom" |
| `color range` | vector | [0, 1] | 颜色范围 [min, max] |
| `opacity` | float | 1.0 | 不透明度 (0-1) |
| `contour lines` | bool | false | 是否显示等高线 |
| `vector arrows` | bool | false | 是否显示矢量箭头 |
| `lighting` | bool | true | 是否启用光照 |

### 7. 相机与视角
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `camera position` | vector | [0, 0, 10e-6] | 相机位置 (x, y, z) |
| `camera target` | vector | [0, 0, 0] | 相机目标点 |
| `camera up` | vector | [0, 1, 0] | 相机向上向量 |
| `field of view` | float | 30 | 视野角度 (度) |
| `zoom factor` | float | 1.0 | 缩放因子 |
| `rotation enabled` | bool | false | 是否启用旋转 |
| `rotation speed` | float | 1.0 | 旋转速度 (度/秒) |

### 8. 输出设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `output format` | string | "avi" | 输出格式："avi", "mp4", "gif", "png sequence", "mat" |
| `output file` | string | "animation.avi" | 输出文件路径 |
| `resolution` | vector | [640, 480] | 分辨率 [width, height] (像素) |
| `quality` | int | 90 | 输出质量 (0-100) |
| `compression` | string | "mpeg4" | 压缩格式 |
| `bitrate` | int | 2000 | 比特率 (kbps) |
| `include timestamp` | bool | true | 是否包含时间戳 |
| `include colorbar` | bool | true | 是否包含颜色条 |
| `include legend` | bool | true | 是否包含图例 |

### 9. 高级设置
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `interpolation` | string | "linear" | 插值方法："linear", "cubic", "nearest" |
| `smoothing` | bool | true | 是否启用平滑 |
| `smoothing factor` | float | 0.5 | 平滑因子 |
| `normalization` | string | "frame" | 归一化："frame", "global", "none" |
| `background subtraction` | bool | false | 是否进行背景减除 |
| `contrast enhancement` | bool | false | 是否增强对比度 |
| `frame blending` | bool | false | 是否启用帧混合 |

### 10. 播放控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `playback speed` | float | 1.0 | 播放速度 (倍速) |
| `start delay` | float | 0 | 开始延迟 (秒) |
| `end delay` | float | 0 | 结束延迟 (秒) |
| `repeat count` | int | 1 | 重复次数 (0 表示无限) |
| `reverse playback` | bool | false | 是否反向播放 |
| `pause at end` | bool | false | 是否在结束时暂停 |

### 11. 脚本控制
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `pre frame script` | string | "" | 每帧前执行的脚本 |
| `post frame script` | string | "" | 每帧后执行的脚本 |
| `animation script` | string | "" | 自定义动画脚本 |
| `event callbacks` | dict | {} | 事件回调函数字典 |
## 返回值

`animate` 命令没有返回值。成功执行后，会创建一个动画对象，可以通过后续的 `set` 命令进行配置。

## 使用示例

### 示例 1：创建时间演化动画（电场）
```python
import lumapi

session = lumapi.FDTD()

# 运行 FDTD 仿真获取时域数据
session.addfdtd()
session.set("simulation time", 100e-15)

# 添加场监视器
session.addprofile()
session.set("name", "field_monitor")
session.set("monitor type", "time")

# 运行仿真
session.run()

# 创建时间动画
session.animate()
session.set("name", "electric_field_animation")
session.set("animation type", "time")
session.set("data source", "field_monitor")

# 配置时间范围
session.set("time range", [0, 100e-15])  # 0 到 100 fs
session.set("time steps", 200)
session.set("frame rate", 30)

# 配置场可视化
session.set("field component", "E")
session.set("component axis", "magnitude")  # 显示电场幅度
session.set("color map", "hot")
session.set("color range", [0, 1e6])  # 0 到 1 MV/m

# 配置相机视角
session.set("camera position", [0, 0, 5e-6])
session.set("camera target", [0, 0, 0])
session.set("zoom factor", 1.5)

# 配置输出
session.set("output format", "mp4")
session.set("output file", "electric_field_time_evolution.mp4")
session.set("resolution", [1920, 1080])  # 1080p
session.set("quality", 95)
session.set("compression", "h264")
session.set("bitrate", 5000)  # 5 Mbps

# 包含辅助信息
session.set("include timestamp", True)
session.set("include colorbar", True)
session.set("include legend", True)

# 生成动画
print("Creating electric field time animation...")
session.runanimation()
```

### 示例 2：参数扫描动画（波长变化）
```python
import lumapi
import numpy as np

session = lumapi.MODE()

# 创建波导结构
session.addrect()
session.set("name", "waveguide")
session.set("x span", 0.5e-6)
session.set("y span", 0.22e-6)
session.set("z span", 10e-6)

# 添加模式源和监视器
session.addmode()
session.set("name", "mode_source")
session.set("wavelength", 1.55e-6)

session.addpower()
session.set("name", "power_monitor")

# 参数扫描：波长从 1.3 到 1.6 μm
wavelengths = np.linspace(1.3e-6, 1.6e-6, 31)

# 创建参数动画
session.animate()
session.set("name", "wavelength_sweep_animation")
session.set("animation type", "parameter")
session.set("parameter name", "wavelength")
session.set("parameter values", wavelengths.tolist())  # 自定义参数序列

# 配置每帧操作
pre_frame_script = """
# 每帧前更新波长
wavelength = getdata("animation", "current_parameter_value")
setnamed("mode_source", "wavelength", wavelength)

# 运行模式求解
runmode()

# 获取传输功率
T = transmission("power_monitor")
setdata("animation", "current_transmission", T)
"""

session.set("pre frame script", pre_frame_script)

# 配置可视化
session.set("field component", "E")
session.set("component axis", "y")  # 显示 Ey 分量
session.set("color map", "rainbow")
session.set("color range", [-1e6, 1e6])  # ±1 MV/m

# 添加文本覆盖（显示当前波长和传输）
post_frame_script = """
# 添加文本标注
wavelength = getdata("animation", "current_parameter_value")
T = getdata("animation", "current_transmission")

text = sprintf("λ = %.1f nm\\nT = %.3f", 
               wavelength*1e9, T)
addtext(text, [1e-6, 1e-6, 0], "fontsize", 12, "color", "white")
"""

session.set("post frame script", post_frame_script)

# 配置输出
session.set("output format", "gif")  # GIF 适合参数扫描动画
session.set("output file", "wavelength_sweep.gif")
session.set("frame rate", 10)  # 较慢的帧率以便观察
session.set("loop mode", "pingpong")  # 来回播放

# 配置高级设置
session.set("interpolation", "cubic")
session.set("smoothing", True)
session.set("smoothing factor", 0.7)
session.set("normalization", "global")  # 全局归一化

# 生成动画
print("Creating wavelength sweep animation...")
session.runanimation()
```

### 示例 3：模式动画（相位演化）
```python
import lumapi

session = lumapi.FDTD()

# 创建环形谐振器
session.addring()
session.set("name", "ring_resonator")
session.set("inner radius", 4e-6)
session.set("outer radius", 5e-6)
session.set("z span", 0.22e-6)

# 添加波导耦合
session.addrect()
session.set("name", "waveguide")
session.set("x span", 0.5e-6)
session.set("y span", 0.22e-6)
session.set("y", -6e-6)

# 运行模式分析获取模式场
session.addmode()
session.set("name", "mode_analysis")
session.set("wavelength", 1.55e-6)

# 创建模式动画
session.animate()
session.set("name", "mode_phase_animation")
session.set("animation type", "mode")
session.set("mode index", 1)  # 基模
session.set("mode animation", "phase")  # 相位演化

# 配置相位扫描
session.set("phase sweep", True)
session.set("phase range", [0, 2*np.pi])  # 完整相位周期
session.set("time steps", 60)  # 60 帧（每帧 6 度）

# 配置模式场可视化
session.set("field component", "E")
session.set("component axis", "real")  # 显示实部
session.set("color map", "jet")
session.set("color range", [-2e6, 2e6])  # 对称范围

# 配置矢量箭头显示场方向
session.set("vector arrows", True)
session.set("arrow density", 0.2)

# 配置等相位线
session.set("contour lines", True)

# 配置相机旋转（环绕观察）
session.set("rotation enabled", True)
session.set("rotation speed", 15)  # 15 度/秒

# 配置输出
session.set("output format", "avi")
session.set("output file", "mode_phase_evolution.avi")
session.set("resolution", [1280, 720])  # 720p
session.set("quality", 90)

# 配置播放控制
session.set("playback speed", 0.5)  # 半速播放
session.set("loop mode", "forward")  # 向前循环
session.set("repeat count", 3)  # 播放 3 次

# 生成动画
print("Creating mode phase evolution animation...")
session.runanimation()
```

### 示例 4：自定义复合动画
```python
import lumapi
import numpy as np

session = lumapi.DEVICE()

# 创建热仿真结构
session.addrect()
session.set("name", "heater")
session.set("x span", 10e-6)
session.set("y span", 2e-6)
session.set("heat power", 0.5)  # 0.5 W

session.addrect()
session.set("name", "substrate")
session.set("x span", 50e-6)
session.set("y span", 10e-6)
session.set("y", -6e-6)
session.set("material", "Si")

# 运行瞬态热分析
session.addthermal()
session.set("name", "thermal_analysis")
session.set("analysis type", "transient")
session.set("transient duration", 1e-3)  # 1 ms
session.set("time steps", 100)

# 创建自定义复合动画
session.animate()
session.set("name", "thermal_transient_composite")
session.set("animation type", "custom")

# 自定义动画脚本
animation_script = """
# 复合动画：同时显示温度分布和温度曲线

# 获取时间数据
times = getdata("thermal_analysis", "time")
num_frames = length(times)

for frame_idx = 1:num_frames
    # 获取当前时间点的温度分布
    T_dist = getdata("thermal_analysis", "temperature", frame_idx)
    
    # 创建子图1：温度分布
    subplot(2,1,1)
    imagesc(T_dist)
    colorbar
    title(sprintf("Temperature distribution at t = %.3f ms", 
                  times(frame_idx)*1e3))
    xlabel("x (μm)")
    ylabel("y (μm)")
    
    # 创建子图2：温度随时间变化曲线
    subplot(2,1,2)
    
    # 获取到当前时间为止的温度历史
    T_history = getdata("thermal_analysis", "temperature_history", 
                        "max_frames", frame_idx)
    
    # 计算最高温度
    T_max = max(T_history(:))
    T_avg = mean(T_history(:))
    
    # 绘制温度曲线
    plot(times(1:frame_idx)*1e3, T_max(1:frame_idx), 'r-', 'LineWidth', 2)
    hold on
    plot(times(1:frame_idx)*1e3, T_avg(1:frame_idx), 'b-', 'LineWidth', 2)
    hold off
    
    xlabel("Time (ms)")
    ylabel("Temperature (K)")
    title("Temperature evolution")
    legend("Maximum temperature", "Average temperature")
    grid on
    
    # 设置坐标轴范围
    xlim([0, max(times)*1e3])
    ylim([300, 500])
    
    # 捕获当前帧
    frame = getframe(gcf);
    animation_frames{frame_idx} = frame;
    
    # 进度报告
    if mod(frame_idx, 10) == 0
        fprintf("Processed %d/%d frames\\n", frame_idx, num_frames)
    end
end

# 组合所有帧创建动画
animation = cat(4, animation_frames{:});
"""

session.set("animation script", animation_script)

# 配置输出设置
session.set("output format", "mp4")
session.set("output file", "thermal_transient_composite.mp4")
session.set("resolution", [1600, 1200])  # 高分辨率用于子图
session.set("frame rate", 20)

# 配置高级渲染
session.set("quality", 100)
session.set("compression", "h265")  # 高效视频编码
session.set("bitrate", 10000)  # 10 Mbps

# 配置事件回调
callbacks = {
    "on_start": "print('Starting thermal animation generation...')",
    "on_progress": """
        function(progress) {
            print(sprintf('Progress: %.1f%%', progress*100))
        }
    """,
    "on_complete": "print('Thermal animation completed successfully!')"
}

session.set("event callbacks", callbacks)

# 生成动画
print("Creating composite thermal animation...")
session.runanimation()
```

## 注意事项

1. **数据量**：动画生成可能产生大量数据，确保有足够的磁盘空间
2. **计算时间**：复杂动画可能需要较长的渲染时间
3. **内存使用**：高分辨率动画可能消耗大量内存
4. **文件格式**：选择适当的输出格式平衡质量和文件大小
5. **时间同步**：确保动画帧率与物理时间尺度匹配
6. **颜色映射**：选择适当的颜色映射以清晰展示数据特征
7. **视角选择**：合适的相机视角对展示三维结构很重要
8. **脚本性能**：自定义脚本应优化以避免性能瓶颈
## 错误处理

### 常见错误
1. **数据源不存在**: `data source` 属性指定的监视器或结果对象不存在
   - 解决方案：检查数据源名称是否正确，确保在创建动画前已添加相应的监视器

2. **输出路径无效**: `output file` 路径不可写或格式不支持
   - 解决方案：检查文件路径权限，确保输出目录存在，使用支持的格式（avi, mp4, gif等）

3. **内存不足**: 高分辨率或长时间动画可能超出可用内存
   - 解决方案：降低分辨率、减少帧数或使用压缩格式

4. **时间范围无效**: `time range` 超出仿真数据范围
   - 解决方案：确保时间范围在监视器数据的时间区间内

5. **参数值无效**: 动画参数超出合理范围（如负的帧率）
   - 解决方案：验证所有参数值在有效范围内

### Python 错误处理
```python
import lumapi

try:
    session = lumapi.FDTD()
    
    # 添加监视器
    session.addprofile()
    session.set("name", "field_monitor")
    session.set("monitor type", "time")
    
    # 创建动画
    session.animate()
    session.set("name", "test_animation")
    session.set("data source", "field_monitor")
    session.set("output file", "animation.mp4")
    
    # 检查数据源是否存在
    if not session.get("field_monitor"):
        raise ValueError("数据源 'field_monitor' 不存在")
    
    # 验证输出路径
    import os
    output_path = session.get("output file")
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 验证时间范围
    time_range = session.get("time range")
    if time_range[0] < 0 or time_range[1] <= time_range[0]:
        raise ValueError("时间范围无效")
    
    # 生成动画
    session.runanimation()
    
except ValueError as e:
    print(f"参数错误: {e}")
    # 恢复默认值或提示用户
    
except RuntimeError as e:
    print(f"运行时错误: {e}")
    if "memory" in str(e).lower():
        print("内存不足，尝试降低分辨率或减少帧数")
    elif "file" in str(e).lower():
        print("文件操作错误，检查输出路径和权限")
    elif "data" in str(e).lower():
        print("数据源错误，检查监视器设置")
    else:
        print(f"未知运行时错误: {e}")
        
except Exception as e:
    print(f"动画创建失败: {e}")
```

## 产品支持

- **FDTD Solutions**: 支持电场、磁场、功率流等动画
- **MODE Solutions**: 支持模式场、传播常数等动画
- **DEVICE**: 支持温度分布、热流等动画
- **INTERCONNECT**: 支持信号波形、眼图等动画

## 相关命令

- `addmovie` - 添加电影对象
- `saveanimation` - 保存动画到文件
- `playanimation` - 播放动画
- `exportanimation` - 导出动画
- `getanimation` - 获取动画数据
- `setanimation` - 设置动画属性

## 版本历史

| 版本 | 修改 |
|------|------|
| Lumerical 2020a | 新增 `animation type` 属性支持更多动画类型 |
| Lumerical 2019a | 改进动画渲染引擎，支持更高分辨率输出 |
| Lumerical 2018a | 新增 `event callbacks` 属性支持脚本控制 |
| 1.1 | 更新日期，完善文档格式，添加错误处理章节 |

## 参考

1. Lumerical 动画生成指南
2. Lumerical 脚本命令参考手册
3. Lumerical Python API 文档

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*