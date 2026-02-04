<!--
---
**Translation metadata**
- English title: stackrt
- Chinese title: stackrt - 多层堆栈反射透射计算
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Advanced
- Priority: High
---
-->

# stackrt

使用解析传递矩阵方法计算平面波通过多层堆栈的反射和透射。该函数返回 S 和 P 偏振的透射和反射功率分数（Ts、Tp、Rs、Rp），以及复反射和透射系数（ts、tp、rs、rp）。所有结果作为频率和入射角（可选）的函数在单个数据集中返回。

注意：从 2022 R1.2 开始，stackrt 脚本命令通过指定二阶折射率张量的九个值来支持完全各向异性和色散材料。对于各向异性材料，反射光的偏振可能与入射偏振不同。后缀 **sp** 和 **ps** 表示返回的功率和系数中偏振如何变化。**sp** 表示 **s** 入射和 **p** 反射/透射。

要计算堆栈内的场，请参见 [ stackfield](./stackfield.md)。

| **语法** | **描述** |
|---|---|
| RT = stackrt(n,d,f); | n：每层折射率。大小可以是<br><br>* Nlayers：各向同性和非色散<br>* Nlayers x Nfreq：各向同性和色散<br>* Nlayers x 3：各向异性和非色散<br>* Nlayers x Nfreq x 3：涉及各向异性和色散材料。<br>注意：仅支持 z 方向的双折射（nx=ny≠nz）。除非 nx=ny，否则命令会报错。<br>* Nlayers x Nfreq x 9：涉及各向异性和色散材料。<br>注意：我们将二阶折射率张量展平为数组。第三维度表示张量中的位置。例如，位置索引 "1"、"2"、"3"、"4" 和 "5" 分别对应 n11、n21、n31、n12 和 n22。<br><br>d：每层厚度。大小为 Nlayers。f：长度为 Nfreq 的频率向量。 |
| RT = stackrt(n,d,f,theta); | theta：角度向量，以度为单位。可选。 |

有关复系数的更多信息，请参见 [Stack 光学求解器概述](./stack_optical_solver_overview.md)。

### 示例 1：各向同性材料五层堆栈

计算 5 层堆栈的反射、透射和场分布。

```
f = linspace(c/400e-9, c/1000e-9,100); # 频率向量  
theta = 0:1:45; # 角度向量  
d = [0; 200e-9; 300e-9; 400e-9; 0]; # 空气/SiO2/Si/SiO2/空气  
nf = length(f);  
nd = length(d);  
  
# 每层折射率（非色散）  
n1 = [1; 1.5; 2.5; 1.5; 1];   
  
# 每层折射率（色散）  
n2 = matrix(nd,nf);  
n2(1,1:nf) = 1; # 空气  
n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
n2(5,1:nf) = 1; # 空气  
  
RT1 = stackrt(n1,d,f); # 非色散指数数据，theta=0  
RT2 = stackrt(n2,d,f,theta); # 色散数据指数数据，theta 从 0 到 45 度  
  
visualize(RT1);  
visualize(RT2);  
  
plot(RT1.lambda*1e6,RT1.Rp,RT1.Rs,RT1.Tp,RT1.Ts,"wavelength (um)","Power","non-disperisive, theta=0");  
legend("Rp","Rs","Tp","Ts");  
image(RT2.lambda*1e6,RT2.theta,RT2.Rp,"wavelength (um)","theta (deg)","Rp, dispersive example");
```

### 示例 2：空气中的双折射平板

```
N_layers = 3;  
Nfreqs = 100;  
n = matrix(N_layers, Nfreqs, 3);  
  
n(1, :, :) = 1;   # 空气  
n(2, :, 1) = 2.1; # nx  
n(2, :, 2) = 2.1; # ny  
n(2, :, 3) = 2.5; # nz  
n(3, :, :) = 1;   # 空气  
  
d = [0; 1e-6; 0]; # 空气/双折射平板/空气  
f = linspace(c/1e-6, c/1.5e-6, Nfreqs);  
theta = 0:1:45;  
  
RT = stackrt(n,d,f,theta);  
  
visualize(RT);
```

### 示例 3：空气中完全各向异性和色散平板

下载并运行附带的脚本 stackrt_anisotropic.lsf。

请注意，我们使用脚本文件中第 32-46 行所示的欧拉角定义来旋转对角化的介电常数矩阵，然后导出折射率矩阵。

**另请参见**

[ 命令列表 ](./command_list.md) , [ stackfield ](./stackfield.md) , [ 多层堆栈计算 ](./multilayer_stack_calculations.md) , [ getfdtdindex ](./getfdtdindex.md) , [ visualize ](./visualize.md)
