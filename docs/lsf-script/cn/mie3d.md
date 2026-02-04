<!--
Translation from English documentation
Original command: mie3d
Translation date: 2026-02-04 22:50:13
-->

# mie3d

The 函数 mie3d 可以 为 used 到 计算 该 scattering, absorption, 和 extinction efficiencies 的 一个 spherical particle made 的 any (non-magnetic) 材料 embedded 在 any ambient dielectric 材料. The efficiencies 是 simply 该 cross sections normalized 到 该 geometric cross section 的 该 particle (\\(\pi r^2\\)). 

###  References: 

[1] Bohren C.F. 和 D.R. Huffman, “Absorption 和 Scattering 的 Light 通过 Small Particles”, John Wiley, New York, NY, 1983. 

[2] Documentation 的 Mätzler C. “MATLAB Functions 用于 Mie Scattering 和 Absorption, Version 2”, IAP Res. Rep. No. 2002-11, August, 2002. 

**语法** |  **描述**  
---|---  
Q = mie3d(m,x);  |  The result Q 是 一个 结构体 该 contains quantities Qext, Qabs 和 Qscat (Qext = Qabs+Qscat). These 将 have 该 same 长度 as x.  The 参数 是:  m: 该 ratio 的 该 refractive index 的 该 sphere 到 该 refractive index 的 该 ambient dielectric medium. This quantity 可能 为 complex-valued because 该 refractive index 的 该 sphere 可能 为 complex. This quantity 应该 either have 一个 singleton 值, 或 为 该 same 长度 的 x 用于 dispersive media.  x: 该 size 参数 该 是 defined as 2*pi*r/lambda0*n1 其中 lambda0 是 该 free space 波长, r 是 该 sphere radius, 和 n1 是 该 real-valued refractive index 的 该 ambient medium.   
Q = mie3d(m,x,nmax);  |  nmax : 该 maximum 数字 的 orders 到 计算 用于 该 mie coefficients. The default 值 是 0, 和 在 此 case 该 nmax = ceil(x+4*x^(1/3))+2. There 是 typically no need 到 modify 该 default 值.   
  
**示例**

In 此 example we 将 计算 和 compare 该 extinction efficiencies 用于 1 micron spheres 的 n=1.5, dispersive glass 和 gold over 该 visible spectrum. 
    
    
    # input 参数
    n1 = 1;
    n2 = 1.5;
    lambda0 = linspace(400e-9,700e-9,10000);
    radius = 1000e-9;
    # 计算 m,x 和 call mie3d
    m = n2/n1;
    x = 2*pi*radius/lambda0*n1;
    Q1 = mie3d(m,x);
    # recalculate 使用 dispersive glass
    n2 = getindex("SiO2 (Glass) - Palik",c/lambda0);
    m = n2/n1;
    Q2 = mie3d(m,x);
    # recalculate 使用 Al
    n2 = getindex("Au (Gold) - Palik",c/lambda0);
    m = n2/n1;
    Q3 = mie3d(m,x);
    plot(lambda0*1e9,Q1.Qext,Q2.Qext,Q3.Qext,"波长 (nm)","Q extinction");
    legend("n = 1.5","Glass (Palik)","Gold (Palik)");

**参见**

[ mie3ds12 ](/hc/en-us/articles/360034406814-mie3ds12) , [ Mie3D example (FDTD) ](https://apps.lumerical.com/mie-scattering-fdtd.html) , [ Mie3D example (DGTD) ](https://apps.lumerical.com/mie-scattering-dgtd.html)
