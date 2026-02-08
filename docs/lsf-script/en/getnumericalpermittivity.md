# getnumericalpermittivity

This advanced function returns the permittivity of a material in the database as it will
be used in an actual FDTD simulation, including the effects of a finite time step, dt.
In FDTD, the relationship between the displacement field, D, and the electric field, E,
is given by

$$ \\vec{D}(\\omega)=\\varepsilon\_{0} \\varepsilon\_{\\gamma}(\\omega, d t)
\\vec{E}(\\omega) $$

In the limit where dt tends to zero, we have

$$ \\lim _{d t \\rightarrow 0} \\varepsilon_{r}(\\omega, d t)=n^{2}(\\omega) $$

where n( ω ) is the refractive index returned by the script function getfdtdindex, or
shown in the Materials Explorer. If you set dt to zero when calling this function, it
will return exactly the same result as the square of getfdtdindex.

The name of the function is a reminder that it returns the numerical permittivity, i.e.,
the ratio of D and E, which is different from the refractive index, i.e. the ratio of
the speed of light in a vacuum to the phase velocity of light in the medium. To
understand the relationship between them, we must consider the full, numerical
dispersion relation between ω and k, which is given by

$$ \\varepsilon\_{r}(\\omega, d t)\\left\[\\frac{1}{c d t} \\sin \\left(\\frac{\\omega d
t}{2}\\right)\\right\]^{2}=\\left\[\\frac{1}{d x} \\sin \\left(\\frac{k\_{x} d
x}{2}\\right)\\right\]^{2}+\\left\[\\frac{1}{d y} \\sin \\left(\\frac{k\_{y} d
y}{2}\\right)\\right\]^{2}+\\left\[\\frac{1}{d z} \\sin \\left(\\frac{k\_{z} d
z}{2}\\right)\\right\]^{2} $$

In the limit where dt, dx, dy and dz tend to zero, it is easy to show that we have the
expected result

$$ \\omega=\\frac{c k}{\\sqrt{\\varepsilon\_{r}(\\omega, d t=0)}}=\\frac{c
k}{n(\\omega)} $$

The spatial FDTD mesh and time step are generally chosen to obtain a desired level of
simulation accuracy, essentially by ensuring that the arguments of the sine functions
are sufficiently small that sin(x)~x and that the simulation is stable. For some
materials, it may be desired to further reduce the value of the time step, dt, without
modifying the spatial FDTD mesh, in order to obtain a higher level of accuracy for ε r (
ω ,dt). This script function makes it possible to calculate, in advance, the value of dt
required to obtain the desired accuracy for the permittivity.

The results from getnumericalpermittivity will be different if the Broadband Fixed Angle
Source Technique (BFAST) is used. Since the script function does not require a
calculation being performed beforehand, the user needs to specify if the computation
uses BFAST or not. See the
[ BFAST page ](https://optics.ansys.com/hc/en-us/articles/360034902273-Source-BFAST) for
more details about this technique.

| **Syntax**                                                                        | **Description**                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getnumericalpermittivity ( "materialname", f, fmin, fmax, dt);              | Returns the complex permittivity of the material with the given name. The permittivity is returned for the specified frequency f. This is similar to getfdtdindex except for the additional parameter dt. All frequency units are in Hz. |
| getnumericalpermittivity("materialname", f,fmin, fmax, dt, component);            | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.                                                                                                             |
| getnumericalpermittivity("materialname", f,fmin, fmax, dt, component, use_bfast); | Optional argument use_bfast can be 0 or 1. It indicates whether the simulation is performed using the Broadband Fixed Angle Source Technique (BFAST) or not. The default is 0.                                                           |

**Examples**

This example shows how to get the material permittivity with the getindex, getfdtdindex
and getnumerical permittivity functions. In this case, we compare the experimental
permittivity data to the theoretical FDTD fit of the that data as well as to the
numerical permittivity that will result using a finite value of dt.

```
material="Si (Silicon) - Palik";   # material 
source_min_f=c/800e-9;      # source min frequency
source_max_f=c/200e-9;      # source max frequency
f_vector=linspace(source_max_f,source_min_f,100);
component = 1; # desired permittivity component x (1), y (2) or z (3). Relevant for anisotropic materials, default 1
use_bfast = 0; # Change to 1 if using BFAST, default 0 
# get experimental data
eps_exp=(getindex(material,f_vector))^2;
# get FDTD fit of experimental data
eps_fit=(getfdtdindex(material,f_vector,source_min_f,source_max_f))^2;
# get the numerical FDTD result for 3 different values of dt
Tmin = 1/max(f_vector);
dt = Tmin * [ 0.1; 0.05; 0.01 ];
# alternate way to get dt values: 100%, 10%, 1% of current dt value
# dt = getnamed("FDTD","dt");
# dt = [dt; dt*0.1; dt*0.01];
 
eps_numerical1=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(1),component,use_bfast);
eps_numerical2=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(2),component,use_bfast);
eps_numerical3=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(3),component,use_bfast);
# plot results
if (use_bfast==1){fdtd_method = "FDTD - BFAST";}
else{fdtd_method = "FDTD";}
plot(c/f_vector*1e9,real(eps_exp),real(eps_fit),
          real(eps_numerical1),
          real(eps_numerical2),
          real(eps_numerical3),
          "wavelenth (nm)","Re(eps)",material);
legend("experimental data","FDTD fit",
    fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
    fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
    fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");
plot(c/f_vector*1e9,imag(eps_exp),imag(eps_fit),
          imag(eps_numerical1),
          imag(eps_numerical2),
          imag(eps_numerical3),"wavelenth (nm)","Im(eps)",material);
legend("experimental data","FDTD fit",
    fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
    fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
    fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getindex ](./getindex.md) , [ addmaterial ](./addmaterial.md) ,
[ setmaterial ](./setmaterial.md) , [ getfdtdindex ](./getfdtdindex.md)
