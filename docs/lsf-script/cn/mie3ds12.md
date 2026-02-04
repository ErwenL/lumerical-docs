# mie3ds12

mie3ds12 函数可用于计算嵌入在任何环境电介质材料中的任何（非磁性）材料的散射远场。函数返回散射函数 S1 和 S2。散射远场可以通过以下公式计算：

$$ \begin{array}{l}{E_{||}=\frac{e^{i k r}}{-i k r} \cos \varphi \cdot S_{2}(\cos \theta)} \\ {E_{\perp}=\frac{e^{i k r}}{i k r} \sin \varphi \cdot S_{1}(\cos \theta)}\end{array} $$

其中 E|| 是散射平面内的场，E⊥ 是垂直于散射平面的场。散射平面由入射和散射方向定义。θ 是散射平面内的角度（相对于入射角），φ 是入射电场与散射平面之间的角度。

### 参考文献：

[1] Bohren C.F. 和 D.R. Huffman，"小颗粒的光吸收和散射"，John Wiley，纽约，NY，1983。

[2] Mätzler C. 文档，"Mie 散射和吸收的 MATLAB 函数，版本 2"，IAP Res. Rep. No. 2002-11，2002年8月。

**语法** | **描述**
---|---
S = mie3ds12(u,m,x); | 结果 Q 是一个结构体，包含 S1、S2，其维度为 NxM，其中 N 是 u 的长度，M 是 x 的长度。参数为：u：这是 cos(θ) m：球体折射率与环境电介质折射率的比值。该量可以是复数值，因为球体的折射率可能是复数的。对于色散介质，该量应该具有单一值，或与 x 相同长度。x：尺寸参数，定义为 2*pi*r/lambda0*n1，其中 lambda0 是自由空间波长，r 是球体半径，n1 是环境介质的实值折射率。
S = mie3ds12(u,m,x,nmax); | nmax：要计算的 Mie 系数最高阶数。默认值为 0，此时 nmax = ceil(x+4*x^(1/3))+2。通常无需修改默认值。

**示例**

例如，让我们计算沿 y 轴入射、偏振沿 z 轴的 500nm 光在 XY 和 YZ 平面中的场。

```
# 输入参数
n1 = 1;
n2 = 1.5;
lambda0 = 500e-9;
radius = 500e-9;
# 计算 m、x 并调用 mie3ds12
m = n2/n1;
x = 2*pi*radius/lambda0*n1;
theta = linspace(0,2*pi,1000);
S = mie3ds12(cos(theta),m,x);
k = 2*pi/lambda0 * n1;
R = 1; # 半径为 1m
# XY 平面：phi = 90，Etang = EP，Eperp = Ez = ES
phi = 90*pi/180;
Etang = exp(1i*k*R)/(-1i*k*R)*cos(phi)*S.S2;
Eperp = exp(1i*k*R)/(1i*k*R)*sin(phi)*S.S1;
polar(theta,abs(Etang),abs(Eperp),"","","XY plane");
legend("|EP|","|ES|");
# YZ 平面：phi = 0，Etang = EP，Eperp = Ex = ES
phi = 0;
Etang = exp(1i*k*R)/(-1i*k*R)*cos(phi)*S.S2;
Eperp = exp(1i*k*R)/(1i*k*R)*sin(phi)*S.S1;
polar(theta,abs(Etang),abs(Eperp),"","","YZ plane");
legend("|EP|","|ES|");
```

**另请参阅**

- [mie3d](./mie3d.md)
- [Mie3D 示例 (FDTD)](https://apps.lumerical.com/mie-scattering-fdtd.html)
- [Mie3D 示例 (DGTD)](https://apps.lumerical.com/mie-scattering-dgtd.html)
