<!--
---
**Translation metadata**
- English title: stackdipole
- Chinese title: stackdipole - 多层堆栈偶极子发射
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Advanced
- Priority: High
---
-->

# stackdipole

### 

### 结果

该函数解析计算无图案多层堆栈的偶极子发射特性。对于可以简化为 1D 的结构，这种技术比使用 FDTD 运行完全矢量模拟高效得多。

结果通过以下方程计算。所有返回的结果都是发射角 \( \theta \) 的函数，该角度从表面法线测量（见上图）。此外，计算假设电流密度为 1 \( A/m^2\)。积分限由输入偶极子光谱确定。

$$  
\text {stackdipole}(\theta)=\int_{\lambda}(j \times e f \times st) \left(\frac{r d \times F_{r a d}(\theta, \lambda)}{r d \times F(\lambda)+(1-r d)}\right) \left(\text {photon probability}(\lambda) \times E_{p h}(\lambda)\right) d \lambda  
$$

| **结果** | **描述** |
|---|---|
| radiance | \( \frac{W}{\text{steradian }m^2 }\) 辐射亮度是光学功率在 SI 单位下的度量，作为 \( \theta \) 的函数 |
| luminance | \( \text{candela }/ m^2 \) 亮度是人眼感知亮度的度量。 |
| X, Y, and Z | 三刺激值是 CIE 1931 色彩空间的基向量[1]，定量描述感知颜色，数学定义见 [colormatch](./colormatch.md) 页面。 |

有关此方法理论的更多信息，请参见 [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) 示例。关于结果的额外讨论可在 [STACK GUI - OLED Device Introduction](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction) 和 [OLED Methodology](./oled_methodology.md) 色度部分找到。

注意：在 2021R1.1 中，stack dipole 结果的长度可能已改变。以前，单例维度在输出前被缩减。如果您已更新并遇到问题，您可能需要自己对结果使用 [pinch](./pinch.md)。

---

### 用法

| **语法** | **描述** |
|---|---|
| dipole_emission = stackdipole(n,d,f,z,dipole_spec, orientation,res,direction, ef,st,rd); | 解析计算多层堆栈的偶极子发射特性 |
| dipole_emission = stackdipole(n,d,f,z,dipole_spec, options); | |

| **参数** | | **默认值** | **类型** | **描述** |
|---|---|---|---|---|
| n | 必需 | | 向量 | n：每层折射率。大小可以是<br><br>* Nlayers：各向同性和非色散<br>* Nlayers x Nfreq：各向同性和色散<br>* Nlayers x 3：各向异性和非色散<br>* Nlayers x Nfreq x 3：涉及各向异性和色散材料。<br>注意：仅支持 z 方向的双折射（nx=ny≠nz）。除非 nx=ny，否则命令会报错。 |
| d | 必需 | | 向量 | 每层厚度。大小为 N_layers。 |
| f | 必需 | | 向量 | 长度为 Nfreq 的频率向量。 |
| z | 必需 | | 向量 | 偶极子位置（0 是堆栈底部）。大小为 N_dipoles，偶极子必须位于边界内。 |
| dipole_spec | 必需 | | 向量 | 偶极子光谱。这被视为功率强度分布，通过中点规则在波长上积分。光子概率分布通过归一化 dipole_spec/f 计算。大小为 N_dipoles x length(f)。 |
| orientation | 可选 | "rand" | 字符串单元格 | 偶极子方向。接受字符串或单元格数组作为 'orientation' 参数，值为：<br><br>* "random" 或 "rand"<br>* "vertical" 或 "vert"<br>* "horizontal" 或 "horz"<br><br>大小为 N_dipoles。 |
| res | 可选 | 1000 | 数值 | 远场发射角度分辨率。 |
| direction | 可选 | 1 | 数值 | 远场半球选择，可以是 +1（顶部）或 -1（底部）。 |
| ef | 可选 | 1 | 向量 | 激子分数。默认值为 1，表示每个载流子都产生一个激子。大小为 N_dipoles。 |
| st | 可选 | 0.25 | 向量 | 单重态激子分数。默认值为 0.25，表示每个自旋单重态有 3 个自旋三重态。大小为 N_dipoles。 |
| rd | 可选 | 1 | 向量 | 相对衰减速率。默认值为 1，表示每个单重态激子都产生一个光子，并且没有非辐射衰变过程的贡献。大小为 N_dipoles。 |
| options | 可选 | | 结构体 | *在 2021R1.1 及更高版本中*：此结构体可用于传递可选参数。传递此结构体允许用户指定以下参数："orientation"：定义偶极子方向。"res"/"theta"：明确定义输出角度，而不是简单的分辨率。要指定角度，请将它们作为向量 "theta" 以度为单位传递 [0,90)。"incoherent_propagation"：向量参数定义堆栈的相干和非相干层，0 = 相干传播，1 = 非相干传播。偶极子不能位于非相干层中。如果使用 options，则所有可选参数都必须通过结构体传递。 |

#### **示例**

计算电介质半空间中偶极子源的辐射功率。

```
# 几何结构：材料 n1 和 n2 的半空间
n1 = 1.5; # 下半空间
n2 = 1.0; # 上半空间  
  
# 源：单色 500nm 偶极子
wavelength = 500e-9;
delta = 80e-9; # 位置：在材料 n2 中距界面 delta nm 处  
  
angular_res = 173; # 发射角度（远场角度）分辨率  
  
# STACK 命令的设置
n = [n1; n2]; #STACK 光学属性
d = [0, 2*delta]; #STACK 几何属性
f = [c/wavelength]; #STACK 频率点
z = [delta]; #STACK 偶极子位置
spectrum = [1.0]; #STACK 偶极子光谱  
  
result_unpol = stackdipole(n,d,f,z,spectrum,"rand",angular_res);
result_Vert = stackdipole(n,d,f,z,spectrum,"vert",angular_res);
result_Horz = stackdipole(n,d,f,z,spectrum,"horz",angular_res);
  
plot(result_unpol.theta,result_unpol.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","unpolarized");
plot(result_Vert.theta,result_Vert.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","vertical P orientation");
plot(result_Horz.theta,result_Horz.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","horizontal P orientation");  
  
# 计算功率
sin_theta = sin(pi/180*pinch(result_unpol.theta));
#从 theta 0-pi/2 和 phi 0-2pi 积分功率
?total_power_pVert_upward = (0.5*pi)*(2*pi)*integrate(sin_theta*result_Vert.radiance,1,linspace(0,1,angular_res));
  
  
# 在 2020R1.3 中  
options={ "res": 173, "orientation": 'rand', "incoherent_propagation": incoherent_propagation};  
result = stackdipole(n,d,f,z,spectrum,options);  
  
options={ "theta": linspace(0,30,100), "orientation": 'rand', "incoherent_propagation": incoherent_propagation};  
result = stackdipole(n,d,f,z,spectrum,options);
```

### 相关出版物

1. CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.

### 另请参见

[Stack 光学求解器概述](./stack_optical_solver_overview.md) , [ stackrt](./stackrt.md) , [ stackfield](./stackfield.md) , [ stackpurcell](./stackpurcell.md) , [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) , [OLED slab mode analysis ](https://apps.lumerical.com/oleds_slab_mode_analysis_of_a_oled_l.html)
