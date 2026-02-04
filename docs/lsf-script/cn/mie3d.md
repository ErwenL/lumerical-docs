# mie3d

mie3d 函数可用于计算由任何（非磁性）材料制成的嵌入在任何环境电介质材料中的球形颗粒的散射、吸收和消光效率。效率只是归一化到颗粒几何横截面积（πr²）的横截面积。

### 参考文献：

[1] Bohren C.F. 和 D.R. Huffman，"小颗粒的光吸收和散射"，John Wiley，纽约，NY，1983。

[2] Mätzler C. 文档，"Mie 散射和吸收的 MATLAB 函数，版本 2"，IAP Res. Rep. No. 2002-11，2002年8月。

**语法** | **描述**
---|---
Q = mie3d(m,x); | 结果 Q 是一个结构体，包含 Qext、Qabs 和 Qscat（Qext = Qabs+Qscat）。这些将与 x 具有相同长度。参数为：m：球体折射率与环境电介质折射率的比值。该量可以是复数值，因为球体的折射率可能是复数的。对于色散介质，该量应该具有单一值，或与 x 相同长度。x：尺寸参数，定义为 2*pi*r/lambda0*n1，其中 lambda0 是自由空间波长，r 是球体半径，n1 是环境介质的实值折射率。
Q = mie3d(m,x,nmax); | nmax：要计算的 Mie 系数最高阶数。默认值为 0，此时 nmax = ceil(x+4*x^(1/3))+2。通常无需修改默认值。

**示例**

在此示例中，我们将计算并比较可见光谱范围内 n=1.5、色散玻璃和金 1 微米球的消光效率。

```
# 输入参数
n1 = 1;
n2 = 1.5;
lambda0 = linspace(400e-9,700e-9,10000);
radius = 1000e-9;
# 计算 m、x 并调用 mie3d
m = n2/n1;
x = 2*pi*radius/lambda0*n1;
Q1 = mie3d(m,x);
# 用色散玻璃重新计算
n2 = getindex("SiO2 (Glass) - Palik",c/lambda0);
m = n2/n1;
Q2 = mie3d(m,x);
# 用 Al 重新计算
n2 = getindex("Au (Gold) - Palik",c/lambda0);
m = n2/n1;
Q3 = mie3d(m,x);
plot(lambda0*1e9,Q1.Qext,Q2.Qext,Q3.Qext,"wavelength (nm)","Q extinction");
legend("n = 1.5","Glass (Palik)","Gold (Palik)");
```

**另请参阅**

- [mie3ds12](./mie3ds12.md)
- [Mie3D 示例 (FDTD)](https://apps.lumerical.com/mie-scattering-fdtd.html)
- [Mie3D 示例 (DGTD)](https://apps.lumerical.com/mie-scattering-dgtd.html)
