# mie3ds12

The function mie3ds12 can be used to calculate the scattered far field of any
(non-magnetic) material embedded in any ambient dielectric material. The function
returns the scattering functions S1 and S2. The scattered far field can be calculated by

$$\\begin{array}{l}{E\_{1}=\\frac{e^{i i v}}{-i k r} \\cos \\varphi \\cdot S\_{2}(\\cos
\\theta)} \\\\ {E\_{\\perp}=\\frac{e^{i k r}}{i k r} \\sin \\varphi \\cdot S\_{1}(\\cos
\\theta)}\\end{array} $$

Where E || is the field in the scattering plane and E ⊥ is the field orthogonal to the
scattering plane. The scattering plane is defined by the incident and scattered
directions. The angle θ is the angle within the scattering plane (with respect to the
incident angle) and the angle φ is the angle between the incident electric field and the
scattering plane.

### References:

[1] Bohren C.F. and D.R. Huffman, “Absorption and Scattering of Light by Small
Particles”, John Wiley, New York, NY, 1983.

[2] Documentation of Mätzler C. “MATLAB Functions for Mie Scattering and Absorption,
Version 2”, IAP Res. Rep. No. 2002-11, August, 2002.

| **Syntax**                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S = mie3ds12(u,m,x);      | The result Q is a struct which contains quantities S1, S2 which has dimensions NxM where N is the length of u and M is the length of x. The arguments are: u: this is cos(q) m: the ratio of the refractive index of the sphere to the refractive index of the ambient dielectric medium. This quantity may be complex-valued because the refractive index of the sphere may be complex. This quantity should either have a singleton value, or be the same length of x for dispersive media. x: the size parameter which is defined as 2*pi*r/lambda0\*n1 where lambda0 is the free space wavelength, r is the sphere radius and n1 is the real-valued refractive index of the ambient medium. |
| S = mie3ds12(u,m,x,nmax); | nmax : the maximum number of orders to calculate for the mie coefficients. The default value is 0, and in this case the nmax = ceil(x+4\*x^(1/3))+2. There is typically no need to modify the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Example**

For example, lets calculate field in XY and YZ planes for 500nm light that is incident
along the y axis, polarized along the z axis.

```
# input parameters
n1 = 1;
n2 = 1.5;
lambda0 = 500e-9;
radius = 500e-9;
# calculate m,x and call mie3ds12
m = n2/n1;
x = 2*pi*radius/lambda0*n1;
theta = linspace(0,2*pi,1000);
S = mie3ds12(cos(theta),m,x);
k = 2*pi/lambda0 * n1;
R = 1; # radius of 1m
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
```

**See Also**

[ mie3d ](./mie3d.md) ,
[ Mie3D example(FDTD) ](https://apps.lumerical.com/mie-scattering-fdtd.html) ,
[ Mie3D example(DGTD) ](https://apps.lumerical.com/mie-scattering-dgtd.html)
