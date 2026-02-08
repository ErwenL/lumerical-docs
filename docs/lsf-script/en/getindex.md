# getindex

Returns the complex refractive index of a material in the material database. The
refractive index at the specified frequency is linearly interpolated from the
neighboring frequencies where the data is available.

| **Syntax**                              | **Description**                                                                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| out = getindex("materialname", f);      | Returns the complex index of the material with the given name. The index is returned for the specified frequency f. Frequency f is in Hz. |
| getindex("materialname", f, component); | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.              |

**Example**

This example shows how to get material (n,k) data with the getindex and getfdtdindex
functions. In this case, we compare the experimental data to the fit of the that data
that will be used in the simulation.

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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ getfdtdindex ](./getfdtdindex.md) , [ getmodeindex ](**%20to%20be%20defined%20**) ,
[ addmaterial ](./addmaterial.md) , [ setmaterial ](./setmaterial.md) ,
[ getsurfaceconductivity ](./getsurfaceconductivity.md)
