# polydft

Returns the chirped z-transform of a set of data. The polydft function is very similar
to a two-dimensional czt function with the difference being that the E function does not
need to be finely sampled and only providing the vertices of a polygon as input range of
the function would be enough to perform the transform. The only limit however is that E
is considered constant within the limits of the polygon. The polygon mesh can be created
using the inpoly function.

| **Syntax**              | **Description**                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| out = polydft(E,kx,ky); | Returns the two dimensional chirped z-transform of E. kx and ky must be linearly spaced sets of wavenumbers but can cover any range. |

**Example**

This example demonstrates two different approaches for calculating the discrete Fourier
transform (DFT) of a piecewise constant 2D function on the xy-plane. The function is
defined as having the value of one inside the polygonal area specified by the vertices
poly_vert. One approach uses the polydft command directly on the polygon vertices, the
other approach uses a finely staircased representation of the function and the czt
command.

```
# -------
# Inputs:
# -------
# xy-plane region
x_span = y_span = 5.0;
# area inside the above region where function is nonzero
poly_vert = [0.25*x_span,0.35*y_span;
             0.50*x_span,0.15*y_span;
             0.75*x_span,0.35*y_span;
             0.75*x_span,0.65*y_span;
             0.50*x_span,0.85*y_span;
             0.25*x_span,0.65*y_span];
# grid for staircasing the above polygon
Nx = Ny = 2^8;
# ---------
# Function:
# ---------
delta_x = x_span/Nx;
delta_y = y_span/Ny;
x = delta_x*linspace(0.0,Nx-1,Nx);
y = delta_y*linspace(0.0,Ny-1,Ny);
X = meshgridx(x,y);
Y = meshgridy(x,y);
poly_fun = inpoly(poly_vert,X,Y);
image(x,y,poly_fun,"x","y","staircased function");
# ----
# DFT:
# ----
# using the czt command
delta_fx = 1.0/(Nx*delta_x);
delta_fy = 1.0/(Ny*delta_y);
fx = delta_fx*linspace(-0.5*(Nx-1),0.5*(Nx-1),Nx);
kx = 2.0*pi*fx;
fy = delta_fy*linspace(-0.5*(Ny-1),0.5*(Ny-1),Ny);
ky = 2.0*pi*fy;
poly_fun_czt = czt(poly_fun,x,y,kx,ky)/(Nx*Ny);
image(kx,ky,abs(poly_fun_czt),"kx","ky","czt");
# using the polydft command
Kx = meshgridx(kx,ky);
Ky = meshgridy(kx,ky);
poly_fun_polydft = polydft(poly_vert,Kx,Ky)/(x_span*y_span);
image(x,y,abs(poly_fun_polydft),"kx","ky","polydft");
# ------------------------
# Function Reconstruction:
# ------------------------
# from czt
poly_fun_from_czt = czt(poly_fun_czt,-kx,-ky,x,y);
image(x,y,real(poly_fun_from_czt),"x","y","reconstruction from czt");
# from polydft
poly_fun_from_polydft = czt(poly_fun_polydft,-kx,-ky,x,y);
image(x,y,real(poly_fun_from_polydft),"x","y","reconstruction from polydft"); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ czt ](./czt.md) ,
[ inpoly ](./inpoly.md) , [ fft ](./fft.md) , [ fftw ](./fftw.md)
