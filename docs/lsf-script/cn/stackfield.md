<!--
---
**Translation metadata**
- English title: stackfield
- Chinese title: stackfield - 多层堆栈场分布计算
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Advanced
- Priority: High
---
-->

# stackfield

使用解析传递矩阵方法计算从下方由平面波照射的多层堆栈内的场。该函数返回 E 和 H 场（Es、Ep、Hs、Hp）。所有结果作为频率、入射角和堆栈中位置（z）的函数在单个数据集中返回。

| **语法** | **描述** |
|---|---|
| field = stackfield(n,d,f); | n：每层折射率。大小可以是<br><br>* Nlayers：各向同性和非色散<br>* Nlayers x Nfreq：各向同性和色散<br>* Nlayers x 3：各向异性和非色散<br>* Nlayers x Nfreq x 3：涉及各向异性和色散材料。<br>注意：仅支持 z 方向的双折射（nx=ny≠nz）。除非 nx=ny，否则命令会报错。<br><br>d：每层厚度。大小为 Nlayers。f：长度为 Nfreq 的频率向量。 |
| field = stackfield(n,d,f,theta,res); | theta：角度向量，以度为单位。可选，默认为 0。res：返回的场结果分辨率。可选，默认为 1000。 |
| field = stackfield(n,d,f,theta,res,min,max); | min/max：用户希望计算场的最小/最大位置。0 对应于堆栈底部。可选，默认为多层堆栈的跨度。 |

**示例**

计算 5 层堆栈的场分布。

```
f = linspace(c/400e-9, c/1000e-9,100); # 频率向量  
theta = 0:1:45; # 角度向量  
d = [0; 200e-9; 300e-9; 400e-9; 0]; # 5 层（包括顶部和底部的空气）  
nf = length(f);  
nd = length(d);  
  
# 非色散材料的折射率  
n1 = [1; 1.5; 2.5; 1.5; 1];   
  
# 色散材料的折射率  
n2 = matrix(nd,nf);  
n2(1,1:nf) = 1; # 空气  
n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
n2(5,1:nf) = 1; # 空气  
  
field1 = stackfield(n1,d,f); # 非色散指数数据，theta=0  
field2 = stackfield(n2,d,f,theta); # 色散数据指数数据，theta 从 0 到 45 度  
  
visualize(field1);  
visualize(field2);
```

以下是空气中双折射平板的示例：

```
N_layers = 3;  
Nfreqs = 100;  
res = 1000;  
n = matrix(N_layers, Nfreqs, 3);  
  
n(1, :, :) = 1;   # 空气  
n(2, :, 1) = 2.1; # nx  
n(2, :, 2) = 2.1; # ny  
n(2, :, 3) = 2.5; # nz  
n(3, :, :) = 1;   # 空气  
  
d = [0; 1e-6; 0]; # 空气/双折射平板/空气  
f = linspace(c/1e-6, c/1.5e-6, Nfreqs);  
theta = 0:1:45;  
  
field = stackfield(n,d,f,theta,res);   
  
visualize(field);
```

**另请参见**

[ 命令列表 ](./command_list.md) , [ stackrt](./stackrt.md) , [ getfdtdindex](./getfdtdindex.md) , [ visualize](./visualize.md) , [ stackdipole](./stackdipole.md) , [STACK 产品参考手册](./stack_product_reference_manual.md)
