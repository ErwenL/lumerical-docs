<!--
---
**Translation metadata**
- English title: stackpurcell
- Chinese title: stackpurcell - 多层堆栈珀塞尔因子
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Advanced
- Priority: High
---
-->

# stackpurcell

## 结果

解析计算多层堆栈的珀塞尔因子和远场发射功率密度。有关此方法理论的更多信息，请参见 [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) 示例。此命令的用法与 [stackdipole](./stackdipole.md) 非常相似，但返回的结果是包含以下数据集的结构体。功率密度是从表面法线测量的发射角 \( \theta \) 的函数（见上图）。

| **结果** | **描述** |
|---|---|
| power | 功率 [归一化] _属性：_ purcell_factor。这是在指定位置和发射频率的单色偶极子的总功率除以它在均匀介质中辐射的功率。_参数：_ dipole/z, f/lambda |
| density | 功率密度 [归一化/球面度] _属性：_ upward, downward, upward_into_air, downward_into_air。这是每单位立体角的功率密度，作为远场发射角的函数，也归一化到在均匀介质中辐射的功率。_参数：_ theta, dipole/z, f/lambda |

有关此方法理论的更多信息，请参见 [Stack dipole half-space](./stack_dipole_half_space.md) 示例。关于结果的额外讨论可在 [STACK GUI - OLED Device Introduction.](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction) 找到。

## 用法

| **语法** | **描述** |
|---|---|
| result = stackpurcell(n,d,f,z,orientation,res) | 解析计算多层堆栈的珀塞尔因子和远场发射功率密度 |
| result = stackpurcell(n,d,f,z,options) | |

| **参数** | | **默认值** | **类型** | **描述** |
|---|---|---|---|---|
| n | 必需 | | 向量 | n：每层折射率。大小可以是<br><br>* Nlayers：各向同性和非色散<br>* Nlayers x Nfreq：各向同性和色散<br>* Nlayers x 3：各向异性和非色散<br>* Nlayers x Nfreq x 3：涉及各向异性和色散材料。<br>注意：仅支持 z 方向的双折射（nx=ny≠nz）。除非 nx=ny，否则命令会报错。 |
| d | 必需 | | 向量 | 每层厚度。大小为 N_layers。 |
| f | 必需 | | 向量 | 频率向量。 |
| z | 必需 | | 向量 | 偶极子位置（0 是堆栈底部）。大小为 N_dipoles，偶极子必须位于边界内。 |
| orientation | 可选 | "rand" | 字符串单元格 | 偶极子方向。接受字符串或单元格数组作为 'orientation' 参数，值为：<br><br>* "random" 或 "rand"<br>* "vertical" 或 "vert"<br>* "horizontal" 或 "horz"<br><br>大小为 N_dipoles。 |
| res | 可选 | 1000 | 数值 | 远场发射角度分辨率。 |
| options | 可选 | | 结构体 | *在 2021R1.1 及更高版本中*：此结构体可用于传递可选参数。传递此结构体允许用户指定以下参数："orientation"：定义偶极子方向。"res"/"theta"：明确定义输出角度，而不是简单的分辨率。要指定角度，请将它们作为向量 "theta" 以度为单位传递 [0,90)。"incoherent_propagation"：向量参数定义堆栈的相干和非相干层，0 = 相干传播，1 = 非相干传播。偶极子不能位于非相干层中。如果使用 options，则所有可选参数都必须通过结构体传递。 |

## 示例

探索偶极子位置对远场发射角度分布的影响：

```
### 使用 stackpurcell 探索多层堆栈中偶极子的位置  
# 频率范围  
N_freq = 101;  
lambda = linspace(380e-9,780e-9,N_freq); # 380nm 到 780nm  
f = c/lambda;  
  
# 初始化多层几何结构  
n = matrix(5,N_freq);  
d = matrix(5,1);  
#定义光学和几何层属性  
n(1,1:N_freq) = getfdtdindex("Al (Aluminium) - Palik",f,f(1),f(N_freq)); d(1) = 0; # 底部基板  
# 注意：这从 FDTD 材料数据库读取材料属性。如果您使用其他产品，请显式输入 (n,k)  
n(2,1:N_freq) = 1.85; d(2) = 60e-9;  
n(3,1:N_freq) = 1.9; d(3) = 220e-9;  
n(4,1:N_freq) = 1.8; d(4) = 120e-9;  
n(5,1:N_freq) = 1.53; d(5) = 0; # 顶部基板（玻璃）  
  
# 偶极子位置/方向  
N_dipole= 51; # 偶极子数量  
z = linspace( d(2)+1e-10, d(2)+d(3)+1e-10, N_dipole ); # 仅考虑中间介电层内的位置  
orientation = cell(N_dipole); # 仅考虑随机取向的偶极子  
for(ii = 1:N_dipole){  
orientation{ii} = "rand";}  
  
# angular_res：发射角度（远场角度）分辨率  
res = 198;  
result = stackpurcell(n,d,f,z,orientation,res); # 结果是结构体  
  
# 绘制位于层中间的偶极子的珀塞尔因子  
purcell = pinch(result.power.purcell_factor); # 大小为 Ndipole by Nfreqs  
plot(lambda*1e9, pinch(purcell,1,round(N_dipole/2)),'wavelength (nm)','Purcell factor');  
  
# 在中心频率处绘制远场功率密度  
theta = pinch(result.density.theta);  
density = pinch(result.density.upward_into_air); # 大小为 res by Ndipole by Nfreqs  
image(theta, z*1e+9, pinch(density,3,round(N_freq/2)), "far-field angle (degrees)", "dipole position (nm)", num2str(f(round(N_freq/2))*1e-12)+"THz into Air");  
  
  
  
  
  
# 在 2020R1.2 中  
incoherent_propagation = [0, 0, 1, 0, 0];  
options={ "res": 1000, "orientation": 'rand',"incoherent_propagation":incoherent_propagation};  
stackpurcell(n,d,f,z,options);  
#或  
options={ "theta": linspace(0,45,100) , "orientation": 'vert', "incoherent_propagation":incoherent_propagation};  
stackpurcell(n,d,f,z,options);
```

**另请参见**

[Stack 光学求解器概述](./stack_optical_solver_overview.md) , [ stackrt](./stackrt.md) , [ stackfield](./stackfield.md) , [ stackdipole](./stackdipole.md) , [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) , [OLED slab mode analysis](https://apps.lumerical.com/oleds_slab_mode_analysis_of_a_oled_l.html)
