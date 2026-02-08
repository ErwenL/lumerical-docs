# getfdtdindex

Returns the complex refractive index of a material in the database with material fit
that will be used in a simulation in FDTD.

Many materials (such as Sampled materials) have properties that depend on frequency.
Using getfdtdindex, you can specify frequency range, and the fitting routine will find a
best fit of the material data over that range. The refractive index evaluated at the
specified frequencies is then returned.

Note that the fit result depends on the fit parameters, Max coefficients and Tolerance
set for the material, thus getfdtdindex result depends on those parameters as well. Tips
for setting these parameters can be found at
[ Modifying the material fits ](https://optics.ansys.com/hc/en-us/articles/360034915053-Modifying-the-Material-Fits)
.

| **Syntax**                                             | **Description**                                                                                                                                                                                                                                           |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getfdtdindex( "materialname", f, fmin, fmax);    | Returns the complex index of the material with the given name. The index is returned for the specified frequency f. Similar to getindex, but you also specify fmin and fmax, the span of frequency of the FDTD simulation. All frequency units are in Hz. |
| getfdtdindex("materialname", f,fmin, fmax, component); | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.                                                                                                                              |

**Examples**

This example shows how to get material (n,k) data with the getindex and getfdtdindex
functions. In this case, we compare the experimental data to the FDTD fit of the that
data that will be used in the simulation.

```
material="Au (Gold) - CRC";   # material 
source_min_f=c/700e-9;      # source min frequency
source_max_f=c/400e-9;      # source max frequency
f_vector=linspace(source_max_f,source_min_f,100);
# get experimental data
n_exp=getindex(material,f_vector);
# get FDTD fit of experimental data
n_fdtd=getfdtdindex(material,f_vector,source_min_f,source_max_f);
# plot results
plot(c/f_vector*1e9,real(n_exp),real(n_fdtd),"wavelenth (nm)","n",material);
legend("experimental data","FDTD fit");
plot(c/f_vector*1e9,imag(n_exp),imag(n_fdtd),"wavelenth (nm)","k",material);
legend("experimental data","FDTD fit");
# output index data to text file
data=matrix(100,5);
data(1:100,1)=c/f_vector*1e9;
data(1:100,2)=real(n_exp);
data(1:100,3)=imag(n_exp);
data(1:100,4)=real(n_fdtd);
data(1:100,5)=imag(n_fdtd);
write(material+".txt","wavelength_nm exp_n exp_k fdtd_n fdtd_k");
write(material+".txt",num2str(data));
```

This example shows how to get the permittivity of a material. The getfdtdindex and
getindex functions always return the material index, so we must apply eps = n^2 to get
the permittivity.

```
material="Au (Gold) - CRC";   # material 
source_min_f=c/700e-9;      # source min frequency
source_max_f=c/400e-9;      # source max frequency
f_vector=linspace(source_max_f,source_min_f,100);
# get (n,k) data
n_fdtd=getfdtdindex(material,f_vector,source_min_f,source_max_f);
# get permittivity data
eps_fdtd=n_fdtd^2;    
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getindex ](./getindex.md) ,
[ getmodeindex ](https://optics.ansys.com/hc/en-us/articles/360034930073) ,
[ addmaterial ](./addmaterial.md) , [ setmaterial ](./setmaterial.md) ,
[ getnumericalpermittivity ](./getnumericalpermittivity.md)
