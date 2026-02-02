# export - 导出数据

## 概述

`export` 命令用于将 Lumerical 仿真数据导出为各种文件格式，以便在其他软件中进行分析、可视化或进一步处理。这是数据后处理和结果共享的关键命令。

### 主要功能
- 将场数据、监视器结果、材料数据等导出为常见格式
- 支持多种文件格式（CSV、TXT、MAT、HDF5、图像格式等）
- 控制导出数据的精度、格式和范围
- 批量导出多个数据集

### 导出数据类型
1. **场数据** - 电场、磁场、功率密度等空间分布
2. **监视器数据** - 功率、模式、频谱等仿真结果
3. **材料数据** - 折射率、介电常数等材料特性
4. **几何数据** - 结构布局、网格信息
5. **脚本数据** - 仿真设置和参数

### 典型应用场景
1. **数据后处理** - 导出到 MATLAB、Python 或 Origin 进行进一步分析
2. **结果可视化** - 导出图像用于报告和论文
3. **数据交换** - 与其他仿真软件共享数据
4. **自动化流程** - 集成到自动化数据处理流程中
5. **长期存储** - 将关键结果存档为标准化格式

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
export(filename, format, data_source, options);

# 导出监视器数据
export("power_data.csv", "CSV", "power_monitor");

# 导出场数据为图像
export("field_image.png", "PNG", "field_monitor", "field component", "Ey");

# 导出多个数据
export("results.mat", "MAT", {"power", "field", "spectrum"});

# 带选项的导出
export("data.txt", "TXT", "monitor", 
       "precision", 6, 
       "append", false, 
       "overwrite", true);
```

### Python API (Lumapi)
```python
# 基本调用
session.export("filename", "format", "data_source")

# 导出监视器数据
session.export("power_data.csv", "CSV", "power_monitor")

# 导出场数据为图像
session.export("field_image.png", "PNG", "field_monitor", "field component", "Ey")

# 使用字典传递选项
options = {
    "precision": 6,
    "append": False,
    "overwrite": True
}
session.export("data.txt", "TXT", "monitor", **options)

# 导出多个数据源
data_sources = ["power_monitor", "field_monitor", "spectrum_monitor"]
for source in data_sources:
    session.export(f"{source}.csv", "CSV", source)
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `filename` | 字符串 | 是 | 无 | 输出文件名（可包含路径） |
| `format` | 字符串 | 是 | 无 | 导出格式：`"CSV"`, `"TXT"`, `"MAT"`, `"HDF5"`, `"PNG"`, `"JPG"`, `"BMP"`, `"TIFF"` |
| `data_source` | 字符串/数组 | 是 | 无 | 数据源：监视器名称、场组件、变量名等 |
| `options` | 键值对 | 否 | 无 | 导出选项（见下表） |

## 导出选项

不同格式支持不同的选项：

| 选项 | 类型 | 默认值 | 适用格式 | 描述 |
|------|------|--------|----------|------|
| `"precision"` | 整数 | 6 | CSV, TXT, MAT | 数值精度（小数位数） |
| `"append"` | 布尔 | `false` | CSV, TXT | 是否追加到现有文件 |
| `"overwrite"` | 布尔 | `true` | 所有格式 | 是否覆盖现有文件 |
| `"field component"` | 字符串 | 无 | PNG, JPG 等 | 场分量：`"Ex"`, `"Ey"`, `"Ez"`, `"Hx"`, `"Hy"`, `"Hz"` |
| `"frequency"` | 数值 | 无 | 图像格式 | 导出特定频率的场 |
| `"wavelength"` | 数值 | 无 | 图像格式 | 导出特定波长的场 |
| `"x min"`, `"x max"` | 数值 | 自动 | 所有格式 | X 范围限制 |
| `"y min"`, `"y max"` | 数值 | 自动 | 所有格式 | Y 范围限制 |
| `"z min"`, `"z max"` | 数值 | 自动 | 所有格式 | Z 范围限制 |
| `"colormap"` | 字符串 | `"jet"` | 图像格式 | 色彩映射：`"jet"`, `"hot"`, `"gray"`, `"hsv"` 等 |
| `"colorbar"` | 布尔 | `true` | 图像格式 | 是否显示颜色条 |
| `"scale"` | 字符串 | `"linear"` | 图像格式 | 比例尺：`"linear"`, `"log"` |
| `"dB range"` | 数值 | 40 | 图像格式 | dB 范围（对数尺度时） |
| `"units"` | 字符串 | `"SI"` | CSV, TXT | 单位系统：`"SI"`, `"micron"`, `"nm"`, `"THz"` 等 |

## 返回值

`export` 命令在 Lumerical 脚本语言（LSF）中通常不返回显式值，主要用于执行导出操作。命令执行成功时无返回值，执行失败时会抛出错误。

在 Python API 中，`session.export()` 方法的返回值取决于执行结果：

| 调用方式 | 返回值 | 说明 |
|----------|--------|------|
| **成功执行** | `None` | 导出操作成功完成，无返回值 |
| **执行失败** | 抛出异常 | 抛出 `RuntimeError` 或相关异常，包含错误信息 |

### 返回值使用示例

```python
import lumapi

fdtd = lumapi.FDTD()

# 检查导出是否成功的函数
def check_export_success(filename):
    """验证导出操作是否成功"""
    import os
    
    try:
        # 执行导出
        fdtd.export(filename, "CSV", "power_monitor")
        
        # 检查文件是否创建
        if os.path.exists(filename):
            print(f"导出成功：文件 '{filename}' 已创建")
            return True
        else:
            print(f"导出失败：文件 '{filename}' 未创建")
            return False
            
    except Exception as e:
        print(f"导出错误：{type(e).__name__} - {e}")
        return False

# 使用示例
success = check_export_success("test_export.csv")
if success:
    print("可进行后续数据处理")
else:
    print("需要检查仿真设置和数据源")

# 另一种方式：使用 try-except 捕获返回值
try:
    fdtd.export("data.csv", "CSV", "power_monitor")
    print("导出命令执行成功（无返回值）")
except RuntimeError as e:
    print(f"导出失败：{e}")
except Exception as e:
    print(f"其他错误：{e}")
```

### LSF 脚本中的返回值处理

```lumerical
// LSF 中 export 命令不返回显式值
// 可以通过检查文件存在性来判断是否成功

export("results.csv", "CSV", "monitor");

// 检查导出是否成功
if (fileexists("results.csv")) {
    ?"导出成功：文件已创建";
    // 可进行后续处理
} else {
    ?"导出失败：文件未创建";
    ?"请检查数据源和文件路径";
}

// 或者使用 try-catch 捕获错误
try {
    export("data.txt", "TXT", "monitor");
    ?"导出成功";
} catch (e) {
    ?"导出失败：" + e;
}
```

## 使用示例

### 示例 1：基本数据导出
```python
import lumapi

fdtd = lumapi.FDTD()

# 运行简单仿真
fdtd.eval("""
    addfdtd;
    set("dimension", "2D");
    set("x span", 3e-6);
    set("y span", 2e-6);
    
    addrect;
    set("material", "Si (Silicon) - Palik");
    set("x span", 500e-9);
    set("y span", 220e-9);
    
    addmode;
    set("injection axis", "x");
    
    addpower;
    set("monitor type", "linear x");
    set("x", 1e-6);
    
    run;
""")

# 导出功率监视器数据
print("导出功率监视器数据...")
fdtd.export("power_data.csv", "CSV", "power")
fdtd.export("power_data.txt", "TXT", "power", "precision", 8)

# 导出场数据
print("导出电场数据...")
fdtd.export("Ex_field.png", "PNG", "field", "field component", "Ex")
fdtd.export("Ey_field.png", "PNG", "field", "field component", "Ey")

# 导出为MATLAB格式
print("导出为MATLAB格式...")
fdtd.export("simulation_results.mat", "MAT", {"power", "field"})

print("导出完成！")
print("生成的文件:")
print("  - power_data.csv: CSV格式功率数据")
print("  - power_data.txt: 文本格式功率数据")
print("  - Ex_field.png: Ex分量场分布图")
print("  - Ey_field.png: Ey分量场分布图")
print("  - simulation_results.mat: MATLAB格式完整结果")
```

### 示例 2：高级场数据导出
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 运行 3D 仿真
fdtd.eval("""
    # 3D FDTD 仿真
    addfdtd;
    set("dimension", "3D");
    set("x span", 2e-6);
    set("y span", 2e-6);
    set("z span", 1e-6);
    
    # 创建波导结构
    addrect;
    set("name", "waveguide");
    set("material", "Si (Silicon) - Palik");
    set("x span", 500e-9);
    set("y span", 220e-9);
    set("z span", 10e-6);
    
    # 模式源
    addmode;
    set("name", "source");
    set("injection axis", "z");
    set("mode selection", "fundamental TE mode");
    
    # 场监视器
    addprofile;
    set("name", "field_monitor");
    set("monitor type", "3D");
    set("x span", 1.5e-6);
    set("y span", 1.5e-6);
    set("z", 5e-6);
    
    run;
""")

# 导出不同格式的场数据
print("导出 3D 场数据...")

# 1. 导出为 HDF5 格式（适合大型数据集）
fdtd.export("field_data.h5", "HDF5", "field_monitor")
print("  HDF5 格式导出完成: field_data.h5")

# 2. 导出特定平面的截面
fdtd.export("field_xy.png", "PNG", "field_monitor", 
            "field component", "E", 
            "z", 5e-6,
            "colormap", "hot",
            "colorbar", True,
            "scale", "log",
            "dB range", 50)
print("  XY 平面场分布图: field_xy.png")

# 3. 导出多个频率点的场
frequencies = fdtd.eval('getdata("field_monitor", "f");')
if frequencies is not None:
    num_freq = min(3, len(frequencies))  # 导出前3个频率点
    
    for i in range(num_freq):
        freq = frequencies[i]
        wavelength = 3e8 / freq
        
        fdtd.export(f"field_freq_{i+1}.png", "PNG", "field_monitor",
                    "field component", "E",
                    "frequency", freq,
                    "colormap", "jet",
                    "title", f"Field at {wavelength*1e9:.1f}nm ({freq/1e12:.1f}THz)")
        print(f"  频率点 {i+1}: {freq/1e12:.1f} THz -> field_freq_{i+1}.png")

# 4. 导出原始数值数据（用于自定义处理）
fdtd.export("field_raw.csv", "CSV", "field_monitor", 
            "field component", "E",
            "x min", -0.5e-6, "x max", 0.5e-6,
            "y min", -0.5e-6, "y max", 0.5e-6,
            "z", 5e-6,
            "precision", 10)
print("  原始数值数据: field_raw.csv")

# 5. 导出为 MATLAB 格式，包含所有场分量
fdtd.eval("""
    export("field_all.mat", "MAT", "field_monitor", 
           "field components", {"Ex", "Ey", "Ez", "Hx", "Hy", "Hz"});
""")
print("  所有场分量MAT文件: field_all.mat")
```

### 示例 3：批量导出和数据处理
```python
import lumapi
import os
import numpy as np

mode = lumapi.MODE()

# 批量分析不同宽度的波导
widths = [400e-9, 450e-9, 500e-9, 550e-9, 600e-9]
wavelength = 1.55e-6

# 创建输出目录
output_dir = "waveguide_analysis"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

results_summary = []

for i, width in enumerate(widths):
    print(f"分析波导宽度: {width*1e9:.0f} nm")
    
    # 创建和求解波导
    script = f"""
    # 清理之前的对象
    deleteall;
    
    # 创建波导
    addrect;
    set("name", "waveguide");
    set("material", "Si (Silicon) - Palik");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("x span", {width});
    set("y span", 220e-9);
    
    # 创建 FDE 求解器
    addfde;
    set("name", "fde_solver");
    set("x", 0);
    set("y", 0);
    set("z", 0);
    set("z span", 2e-6);
    set("wavelength", {wavelength});
    set("number of trial modes", 5);
    
    # 运行求解
    findmodes;
    """
    
    mode.eval(script)
    
    # 获取结果
    neff_result = mode.getresult("fde_solver", "neff")
    if neff_result is not None and len(neff_result) > 0:
        neff = neff_result[0]
        
        # 导出模式场分布
        field_filename = os.path.join(output_dir, f"mode_field_width_{width*1e9:.0f}nm.png")
        mode.export(field_filename, "PNG", "fde_solver",
                    "field component", "E",
                    "mode index", 1,
                    "colormap", "jet",
                    "title", f"Mode field (width={width*1e9:.0f}nm, n_eff={neff:.4f})")
        
        # 导出模式数据
        data_filename = os.path.join(output_dir, f"mode_data_width_{width*1e9:.0f}nm.csv")
        mode.eval(f"""
            export("{data_filename}", "CSV", "fde_solver",
                   "data", "mode fields",
                   "mode index", 1,
                   "precision", 8);
        """)
        
        # 记录结果
        results_summary.append({
            "width_nm": width * 1e9,
            "width_m": width,
            "neff": neff,
            "field_image": field_filename,
            "data_file": data_filename
        })
        
        print(f"  完成: n_eff = {neff:.6f}")
    else:
        print(f"  失败: 未找到模式")
    
    # 清理
    mode.eval("deleteall;")

# 导出汇总结果
summary_filename = os.path.join(output_dir, "waveguide_analysis_summary.csv")
with open(summary_filename, 'w') as f:
    f.write("width_nm,width_m,neff,field_image,data_file\n")
    for result in results_summary:
        f.write(f"{result['width_nm']:.1f},{result['width_m']:.10e},{result['neff']:.6f},"
                f"{result['field_image']},{result['data_file']}\n")

print(f"\n批量分析完成！")
print(f"结果保存在目录: {output_dir}")
print(f"汇总文件: {summary_filename}")

# 创建结果报告
report_script = f"""
# 创建分析报告
figure;
hold on;

# 绘制有效折射率 vs 宽度
widths = {[r['width_m'] for r in results_summary]};
neffs = {[r['neff'] for r in results_summary]};

plot(widths*1e9, neffs, 'bo-', 'LineWidth', 2, 'MarkerSize', 8);
xlabel('波导宽度 (nm)');
ylabel('有效折射率 n_e_f_f');
title('SOI波导有效折射率 vs 宽度 (厚度=220nm, λ=1550nm)');
grid on;

# 添加数据标签
for i = 1:length(widths)
    text(widths(i)*1e9 + 5, neffs(i), sprintf('%.4f', neffs(i)), 
         'VerticalAlignment', 'bottom', 'FontSize', 9);
end

# 保存图表
savefig('{os.path.join(output_dir, "neff_vs_width.png")}');
hold off;

?"分析报告生成完成";
?"有效折射率范围: " + num2str(min(neffs)) + " - " + num2str(max(neffs));
"""
mode.eval(report_script)

print(f"分析报告图: {os.path.join(output_dir, 'neff_vs_width.png')}")
```

### 示例 4：材料数据导出
```python
import lumapi

mode = lumapi.MODE()

# 导出材料光学特性
print("导出材料数据...")

# 定义材料列表和波长范围
materials = ["Si (Silicon) - Palik", "SiO2 (Glass) - Palik", "Si3N4", "Au (Gold) - Palik"]
wavelengths_nm = np.linspace(400, 1700, 131)  # 400-1700nm, 10nm间隔
wavelengths = wavelengths_nm * 1e-9

# 为每种材料创建数据文件
for material in materials:
    print(f"  处理材料: {material}")
    
    # 收集数据
    n_values = []
    k_values = []
    
    for wl in wavelengths:
        freq = 3e8 / wl
        try:
            # 获取复介电常数
            epsilon = mode.epsilon(material, freq, True)
            epsilon_real = np.real(epsilon)
            epsilon_imag = np.imag(epsilon)
            
            # 计算折射率和消光系数
            n = np.sqrt((epsilon_real + np.sqrt(epsilon_real**2 + epsilon_imag**2)) / 2)
            k = np.sqrt((-epsilon_real + np.sqrt(epsilon_real**2 + epsilon_imag**2)) / 2)
            
            n_values.append(n)
            k_values.append(k)
        except:
            n_values.append(np.nan)
            k_values.append(np.nan)
    
    # 导出为CSV
    filename = f"{material.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')}.csv"
    
    with open(filename, 'w') as f:
        f.write(f"# Material: {material}\n")
        f.write("# Wavelength (nm), Refractive index (n), Extinction coefficient (k)\n")
        
        for wl_nm, n, k in zip(wavelengths_nm, n_values, k_values):
            if not np.isnan(n) and not np.isnan(k):
                f.write(f"{wl_nm:.1f},{n:.6f},{k:.6f}\n")
    
    print(f"    数据导出到: {filename}")
    
    # 同时导出为MATLAB格式
    mat_filename = filename.replace('.csv', '.mat')
    mode.eval(f"""
        # 在 Lumerical 中创建数据并导出
        wavelengths = {list(wavelengths)};
        n_data = {list(n_values)};
        k_data = {list(k_values)};
        
        # 导出为MAT文件
        export("{mat_filename}", "MAT", {{"wavelengths", "n_data", "k_data"}});
    """)

print("\n所有材料数据导出完成！")

# 创建材料比较图
comparison_script = """
# 创建材料比较图
figure;

# 子图1：折射率比较
subplot(2,1,1);
hold on;

colors = {'b-', 'r-', 'g-', 'm-'};
for i = 1:length(materials)
    # 这里应该加载之前导出的数据
    # 简化：直接使用之前计算的数据
end

xlabel('波长 (nm)');
ylabel('折射率 n');
title('材料折射率比较');
legend(materials, 'Location', 'best');
grid on;
hold off;

# 子图2：消光系数比较
subplot(2,1,2);
hold on;
for i = 1:length(materials)
    # 绘制消光系数
end
xlabel('波长 (nm)');
ylabel('消光系数 k');
title('材料消光系数比较');
set(gca, 'YScale', 'log');
grid on;
hold off;

# 保存图表
savefig('material_comparison.png');
?"材料比较图已保存为 material_comparison.png";
"""
mode.eval(comparison_script)
```

### 示例 5：自动化报告生成
```python
import lumapi
import datetime

fdtd = lumapi.FDTD()

# 运行仿真
fdtd.eval("""
    # 标准仿真
    addfdtd;
    set("dimension", "3D");
    set("x span", 3e-6);
    set("y span", 3e-6);
    set("z span", 1e-6);
    
    addrect;
    set("name", "device");
    set("material", "Si (Silicon) - Palik");
    set("x span", 1e-6);
    set("y span", 500e-9);
    set("z span", 220e-9);
    
    addmode;
    set("name", "source");
    
    addpower;
    set("name", "monitor1");
    set("monitor type", "2D X-normal");
    set("x", 1e-6);
    
    addpower;
    set("name", "monitor2");
    set("monitor type", "2D Y-normal");
    set("y", 1e-6);
    
    run;
""")

# 生成自动化报告
report_dir = f"simulation_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
os.makedirs(report_dir, exist_ok=True)

print(f"生成仿真报告到目录: {report_dir}")

# 1. 导出关键结果图像
image_files = []

# 场分布图
fdtd.export(os.path.join(report_dir, "field_3d.png"), "PNG", "field", 
            "field component", "E",
            "colormap", "jet",
            "colorbar", True,
            "title", "3D Electric Field Distribution")
image_files.append("field_3d.png")

# 功率监视器数据
fdtd.export(os.path.join(report_dir, "power_monitor1.png"), "PNG", "monitor1",
            "colormap", "hot",
            "scale", "log")
image_files.append("power_monitor1.png")

fdtd.export(os.path.join(report_dir, "power_monitor2.png"), "PNG", "monitor2",
            "colormap", "hot",
            "scale", "log")
image_files.append("power_monitor2.png")

# 2. 导出数值数据
data_files = []

# 传输光谱
fdtd.export(os.path.join(report_dir, "transmission.csv"), "CSV", "monitor1",
            "data", "T",
            "precision", 8)
data_files.append("transmission.csv")

# 场数据切片
fdtd.export(os.path.join(report_dir, "field_slice.csv"), "CSV", "field",
            "field component", "E",
            "x", 0,
            "precision", 6)
data_files.append("field_slice.csv")

# 3. 导出仿真设置
fdtd.eval(f"""
    # 导出对象属性
    objects = get("objecttype");
    export("{os.path.join(report_dir, "simulation_objects.csv")}", "CSV", "objects");
    
    # 导出网格信息
    mesh_info = meshinfo("FDTD");
    export("{os.path.join(report_dir, "mesh_info.txt")}", "TXT", "mesh_info");
""")
data_files.extend(["simulation_objects.csv", "mesh_info.txt"])

# 4. 生成报告摘要
report_summary = f"""仿真报告摘要
生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
仿真类型: 3D FDTD
仿真区域: 3×3×1 μm³
结构: 硅波导 (1×0.5×0.22 μm³)

导出文件:
图像文件:
{chr(10).join(['  - ' + f for f in image_files])}

数据文件:
{chr(10).join(['  - ' + f for f in data_files])}

仿真结果:
传输效率: {fdtd.eval('transmission("monitor1");'):.4f}
最大场强: {fdtd.eval('max(abs(getdata("field", "E")));'):.4e} V/m
仿真时间: {fdtd.eval('getnamed("FDTD", "total time");'):.2f} s
"""

with open(os.path.join(report_dir, "report_summary.txt"), 'w') as f:
    f.write(report_summary)

print("报告生成完成！")
print(f"报告目录: {report_dir}")
print(f"摘要文件: {os.path.join(report_dir, 'report_summary.txt')}")
```

## 注意事项

### 1. 文件路径
- 使用绝对路径或相对于工作目录的路径
- 确保目标目录有写入权限
- Windows 路径使用双反斜杠或原始字符串

### 2. 数据格式选择
- **CSV/TXT**: 适合小到中型数据集，人类可读
- **MAT**: 适合 MATLAB 用户，保留数据类型
- **HDF5**: 适合大型数据集，支持压缩
- **图像格式**: 适合可视化，有损压缩

### 3. 内存管理
- 大型数据集导出可能消耗大量内存
- 考虑分块导出或选择子区域
- 及时清理不再需要的数据

### 4. 性能优化
- 批量导出时合并相似操作
- 对于重复导出，考虑缓存数据
- 选择适当的精度（过高精度增加文件大小）

### 5. 兼容性
- 确保目标软件支持导出格式
- 注意数值精度和单位转换
- 验证导出数据的完整性

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 场数据、监视器数据导出 |
| **MODE Solutions** | 完全支持 | 模式数据、材料数据导出 |
| **DEVICE** | 支持 | 电学特性数据导出 |
| **INTERCONNECT** | 支持 | 电路参数、S参数导出 |

## 相关命令

- [`save`](./save.md) - 保存项目文件
- [`load`](./load.md) - 加载项目文件
- [`getdata`](./getdata.md) - 获取数据（可用于自定义导出）
- [`write`](./write.md) - 写入数据文件（更底层的操作）

## 最佳实践

### 1. 标准化导出命名
```python
def generate_export_filename(base_name, data_type, format, timestamp=None):
    """生成标准化的导出文件名"""
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    
    format_ext = {
        'CSV': '.csv',
        'TXT': '.txt',
        'MAT': '.mat',
        'HDF5': '.h5',
        'PNG': '.png',
        'JPG': '.jpg'
    }
    
    ext = format_ext.get(format.upper(), '.dat')
    return f"{base_name}_{data_type}_{timestamp}{ext}"

# 使用标准化命名
filename = generate_export_filename("simulation", "field_data", "CSV")
session.export(filename, "CSV", "field_monitor")
```

### 2. 导出验证
```python
def verify_export(filename, min_size_kb=1):
    """验证导出文件是否成功创建且非空"""
    if not os.path.exists(filename):
        print(f"错误: 文件未创建 - {filename}")
        return False
    
    file_size = os.path.getsize(filename) / 1024  # KB
    if file_size < min_size_kb:
        print(f"警告: 文件过小 ({file_size:.2f} KB < {min_size_kb} KB) - {filename}")
        return False
    
    print(f"验证通过: {filename} ({file_size:.2f} KB)")
    return True

# 导出后验证
session.export("data.csv", "CSV", "monitor")
verify_export("data.csv", min_size_kb=0.1)
```

### 3. 批量导出管理
```python
class ExportManager:
    """导出管理器"""
    
    def __init__(self, session, output_dir="exports"):
        self.session = session
        self.output_dir = output_dir
        self.export_log = []
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def export_data(self, data_source, format="CSV", **options):
        """导出数据并记录"""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(self.output_dir, f"{data_source}_{timestamp}.{format.lower()}")
        
        try:
            # 执行导出
            if options:
                self.session.export(filename, format, data_source, **options)
            else:
                self.session.export(filename, format, data_source)
            
            # 记录日志
            log_entry = {
                "timestamp": timestamp,
                "data_source": data_source,
                "format": format,
                "filename": filename,
                "status": "success"
            }
            self.export_log.append(log_entry)
            
            print(f"导出成功: {filename}")
            return filename
            
        except Exception as e:
            print(f"导出失败: {data_source} - {e}")
            return None
    
    def save_log(self):
        """保存导出日志"""
        log_file = os.path.join(self.output_dir, "export_log.csv")
        with open(log_file, 'w') as f:
            f.write("timestamp,data_source,format,filename,status\n")
            for entry in self.export_log:
                f.write(f"{entry['timestamp']},{entry['data_source']},{entry['format']},"
                       f"{entry['filename']},{entry['status']}\n")
        return log_file

# 使用导出管理器
manager = ExportManager(fdtd, "simulation_exports")
manager.export_data("power_monitor", "CSV", precision=8)
manager.export_data("field_monitor", "PNG", field_component="E", colormap="jet")
log_file = manager.save_log()
print(f"导出日志: {log_file}")
```

## 错误处理

### 常见错误类型

| 错误类型 | 原因 | 解决方案 |
|----------|------|----------|
| **文件权限错误** | 目标目录无写入权限 | 检查目录权限，使用 `os.access()` 验证 |
| **内存不足错误** | 导出数据量过大 | 减少导出范围，分块导出，使用 HDF5 格式 |
| **格式不支持错误** | 格式名称错误或版本不支持 | 检查格式拼写，使用 `"CSV"`, `"TXT"`, `"MAT"`, `"PNG"` 等标准格式 |
| **数据源不存在错误** | 监视器或变量名称错误 | 使用 `getdata()` 验证数据源存在性 |
| **路径无效错误** | 文件路径包含非法字符 | 使用 `os.path.isabs()` 和 `os.path.exists()` 验证路径 |
| **数据类型不匹配错误** | 数据格式与导出格式不兼容 | 检查数据类型，使用合适的导出选项 |

### Python 错误处理示例

```python
import lumapi
import os

fdtd = lumapi.FDTD()

def safe_export(filename, format, data_source, **options):
    """安全的导出函数，包含错误处理"""
    try:
        # 验证文件路径
        if not filename or not isinstance(filename, str):
            raise ValueError("文件名必须是有效的字符串")
        
        # 验证数据源
        if not data_source or not isinstance(data_source, str):
            raise ValueError("数据源必须是有效的字符串")
        
        # 执行导出
        result = fdtd.export(filename, format, data_source, **options)
        
        # 验证导出结果
        if not os.path.exists(filename):
            raise RuntimeError(f"导出失败：文件未创建 - {filename}")
        
        file_size = os.path.getsize(filename)
        if file_size == 0:
            print(f"警告：导出文件为空 - {filename}")
        
        print(f"导出成功：{filename} ({file_size} 字节)")
        return True
        
    except PermissionError as e:
        print(f"权限错误：无法写入文件 - {filename}")
        print(f"错误详情：{e}")
        return False
        
    except MemoryError as e:
        print(f"内存不足：数据量过大")
        print("建议：减少导出范围或使用分块导出")
        return False
        
    except ValueError as e:
        print(f"参数错误：{e}")
        return False
        
    except Exception as e:
        print(f"未知错误：{type(e).__name__} - {e}")
        return False

# 使用错误处理的导出
success = safe_export("data.csv", "CSV", "power_monitor", precision=8)
if success:
    print("导出完成，可进行后续处理")
else:
    print("导出失败，请检查错误信息")
```

### LSF 脚本错误处理

```lumerical
# LSF 脚本中的错误处理
# 使用 try-catch 块处理导出错误

try {
    # 尝试导出
    export("data.csv", "CSV", "power_monitor");
    
    # 验证导出是否成功
    if (!fileexists("data.csv")) {
        throw("导出失败：文件未创建");
    }
    
    ?"导出成功！";
    
} catch (e) {
    # 错误处理
    ?"导出错误：" + e;
    ?"建议：检查数据源和文件路径";
    
    # 尝试替代方案
    try {
        export("data.txt", "TXT", "power_monitor");
        ?"已使用 TXT 格式重新导出";
    } catch (e2) {
        ?"再次失败：" + e2;
    }
}
```

## 故障排除

### 常见问题
1. **权限错误**: 确保有目标目录的写入权限
2. **内存不足**: 减少导出数据量或选择子区域
3. **格式不支持**: 检查格式名称拼写和大小写
4. **数据源不存在**: 验证监视器或变量名称

### 调试建议
- 先尝试导出小数据集测试配置
- 检查文件路径和名称有效性
- 验证数据源是否包含有效数据
- 查看 Lumerical 消息窗口的错误信息

## 版本历史

| 版本 | 日期 | 修改内容 | 修改人 |
|------|------|----------|--------|
| 1.0 | 2025-01-31 | 初始版本，包含基本语法、参数说明和示例 | 文档整理团队 |
| 1.1 | 2026-01-31 | 添加错误处理章节，完善故障排除内容，添加版本历史 | AI Agent C |

---

*文档版本：1.0 | 最后更新：2025-01-31*