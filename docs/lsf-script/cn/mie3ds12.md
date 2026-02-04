<!--
Translation from English documentation
Original command: mie3ds12
Translation date: 2026-02-04 22:50:13
-->

# mie3ds12

The 函数 mie3ds12 可以 为 used 到 计算 该 scattered far field 的 any (non-magnetic) 材料 embedded 在 any ambient dielectric 材料. The 函数 返回 该 scattering functions S1 和 S2. The scattered far field 可以 为 calculated 通过 

$$\begin{数组}{l}{E_{1}=\frac{e^{i i v}}{-i k r} \cos \varphi \cdot S_{2}(\cos \theta)} \\\ {E_{\perp}=\frac{e^{i k r}}{i k r} \sin \varphi \cdot S_{1}(\cos \theta)}\end{数组} $$ 

Where E  ||  是 该 field 在 该 scattering plane 和 E  ⊥  是 该 field orthogonal 到 该 scattering plane. The scattering plane 是 defined 通过 该 incident 和 scattered directions. The angle θ 是 该 angle within 该 scattering plane (使用 respect 到 该 incident angle) 和 该 angle φ 是 该 angle between 该 incident electric field 和 该 scattering plane. 

###  References: 

[1] Bohren C.F. 和 D.R. Huffman, “Absorption 和 Scattering 的 Light 通过 Small Particles”, John Wiley, New York, NY, 1983. 

[2] Documentation 的 Mätzler C. “MATLAB Functions 用于 Mie Scattering 和 Absorption, Version 2”, IAP Res. Rep. No. 2002-11, August, 2002. 

**语法** |  **描述**  
---|---  
S = mie3ds12(u,m,x);  |  The result Q 是 一个 结构体 该 contains quantities S1, S2 该 has dimensions NxM 其中 N 是 该 长度 的 u 和 M 是 该 长度 的 x.  The 参数 是:  u: 此 是 cos(q)  m: 该 ratio 的 该 refractive index 的 该 sphere 到 该 refractive index 的 该 ambient dielectric medium. This quantity 可能 为 complex-valued because 该 refractive index 的 该 sphere 可能 为 complex. This quantity 应该 either have 一个 singleton 值, 或 为 该 same 长度 的 x 用于 dispersive media.  x: 该 size 参数 该 是 defined as 2*pi*r/lambda0*n1 其中 lambda0 是 该 free space 波长, r 是 该 sphere radius 和 n1 是 该 real-valued refractive index 的 该 ambient medium.   
S = mie3ds12(u,m,x,nmax);  |  nmax : 该 maximum 数字 的 orders 到 计算 用于 该 mie coefficients. The default 值 是 0, 和 在 此 case 该 nmax = ceil(x+4*x^(1/3))+2. There 是 typically no need 到 modify 该 default 值.   
  
**示例**

For example, lets 计算 field 在 XY 和 YZ planes 用于 500nm light 该 是 incident along 该 y axis, polarized along 该 z axis. 
    
    
    # input 参数
    n1 = 1;
    n2 = 1.5;
    lambda0 = 500e-9;
    radius = 500e-9;
    # 计算 m,x 和 call mie3ds12
    m = n2/n1;
    x = 2*pi*radius/lambda0*n1;
    theta = linspace(0,2*pi,1000);
    S = mie3ds12(cos(theta),m,x);
    k = 2*pi/lambda0 * n1;
    R = 1; # radius 的 1m
    # XY plane: phi = 90, Etang = EP, Eperp = Ez = ES
    phi = 90*pi/180;
    Etang = exp(1i*k*R)/(-1i*k*R)*cos(phi)*S.S2;
    Eperp = exp(1i*k*R)/(1i*k*R)*sin(phi)*S.S1;
    polar(theta,abs(Etang),abs(Eperp),"","","XY plane");
    legend("|EP|","|ES|");
    # YZ plane: phi = 0, Etang = EP, Eperp = Ex = ES
    phi = 0;
    Etang = exp(1i*k*R)/(-1i*k*R)*cos(phi)*S.S2;
    Eperp = exp(1i*k*R)/(1i*k*R)*sin(phi)*S.S1;
    polar(theta,abs(Etang),abs(Eperp),"","","YZ plane");
    legend("|EP|","|ES|");

**参见**

[ mie3d ](/hc/en-us/articles/360034406794-mie3d) , [ Mie3D example(FDTD) ](https://apps.lumerical.com/mie-scattering-fdtd.html) , [ Mie3D example(DGTD) ](https://apps.lumerical.com/mie-scattering-dgtd.html)
