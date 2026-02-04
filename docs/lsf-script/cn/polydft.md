# polydft

返回一组数据的啁啾 z 变换。polydft 函数与二维 czt 函数非常相似，区别在于 E 函数不需要精细采样，只需提供多边形的顶点作为函数的输入范围即可执行变换。然而唯一的限制是 E 在多边形范围内被视为常数。可以使用 inpoly 函数创建多边形网格。

**语法** | **描述**
---|---
out = polydft(E,kx,ky); | 返回 E 的二维啁啾 z 变换。kx 和 ky 必须是线性间隔的波数集合，但可以覆盖任意范围。

**示例**

本示例演示了两种不同的方法来计算 xy 平面上分段常数二维函数的离散傅里叶变换（DFT）。该函数定义为在由顶点 poly_vert 指定的多边形区域内取值为 1。一种方法直接在多边形顶点上使用 polydft 命令，另一种方法使用函数的精细阶梯表示和 czt 命令。

```powershell
# -------
# 输入：
# -------
# xy 平面区域
x_span = y_span = 5.0;
# 上述区域内函数非零的区域
poly_vert = [0.25*x_span,0.35*y_span;
             0.50*x_span,0.15*y_span;
             0.75*x_span,0.35*y_span;
             0.75*x_span,0.65*y_span;
             0.50*x_span,0.85*y_span;
             0.25*x_span,0.65*y_span];
# 用于将上述多边形阶梯化的网格
Nx = Ny = 2^8;
# ---------
# 函数：
# ---------
delta_x = x_span/Nx;
delta_y = y_span/Ny;
x = delta_x*linspace(0.0,Nx-1,Nx);
y = delta_y*linspace(0.0,Ny-1,Ny);
X = meshgridx(x,y);
Y = meshgridy(x,y);
poly_fun = inpoly(poly_vert,X,Y);
image(x,y,poly_fun,"x","y","阶梯化函数");
# ----
# DFT：
# ----
# 使用 czt 命令
delta_fx = 1.0/(Nx*delta_x);
delta_fy = 1.0/(Ny*delta_y);
fx = delta_fx*linspace(-0.5*(Nx-1),0.5*(Nx-1),Nx);
kx = 2.0*pi*fx;
fy = delta_fy*linspace(-0.5*(Ny-1),0.5*(Ny-1),Ny);
ky = 2.0*pi*fy;
poly_fun_czt = czt(poly_fun,x,y,kx,ky)/(Nx*Ny);
image(kx,ky,abs(poly_fun_czt),"kx","ky","czt");
# 使用 polydft 命令
Kx = meshgridx(kx,ky);
Ky = meshgridy(kx,ky);
poly_fun_polydft = polydft(poly_vert,Kx,Ky)/(x_span*y_span);
image(x,y,abs(poly_fun_polydft),"kx","ky","polydft");
# ------------------------
# 函数重构：
# ------------------------
# 来自 czt
poly_fun_from_czt = czt(poly_fun_czt,-kx,-ky,x,y);
image(x,y,real(poly_fun_from_czt),"x","y","来自 czt 的重构");
# 来自 polydft
poly_fun_from_polydft = czt(poly_fun_polydft,-kx,-ky,x,y);
image(x,y,real(poly_fun_from_polydft),"x","y","来自 polydft 的重构");
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[czt](./czt.md)、[inpoly](./inpoly.md)、[fft](./fft.md)、[fftw](./fftw.md)
