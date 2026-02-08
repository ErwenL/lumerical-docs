# getmaterial

Returns properties of a material in the material database.

| **Syntax**                                          | **Description**                                                                                                                                                                                                                                       |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ?getmaterial( "materialname");                      | Displays the property names of the specified material that can be modified.                                                                                                                                                                           |
| out = getmaterial( "materialname", "propertyname"); | Returns the property named "propertyname" of the material with the name "materialname". The returned variable is either a matrix or a string, depending on the property in the query.                                                                 |
| out = getmaterial( "materialname", _**cell**_);     | Return multiple properties, by passing a [cell](https://support.lumerical.com/hc/en-us/articles/360034929913-cell) with entries equal to "propertyname". In this case out will be a struct with keys equal to the "propertyname" entries in the cell. |

**Examples**

These commands add a new Conductive material, set the name to "aluminum", anisotropy to
"Diagonal", and set the permittivity as well as conductivity properties for the
material. The command getmaterial() is then used to find the permittivity of the
material.

```
A=[4;5;6];
B=[1;2;3];
mymaterial = addmaterial("Conductive");
setmaterial(mymaterial,"name","Aluminium");
setmaterial("Aluminum", "Anisotropy", 1); # enable diagonal anisotropy
setmaterial("Aluminum","Permittivity", A);
setmaterial("Aluminum","Conductivity", B);
?getmaterial("Aluminum","Permittivity");
result: 
4 5 6   
  
#Using cell array  
props = cell(2);  
props{1} = "Permittivity"; props{2} = "Conductivity";  
Al_vals = getmaterial("Aluminum",props);  
?Al_vals.Conductivity;  
result:   
1 2 3 
```

This example shows how to access raw data from a Sampled data material.

## Note: Sampled data matrix format The sampled data matrix has 2 or 4 columns, for isotropic or anisotropic materials - The first column is the frequency vector, in Hz. - The next column(s) are the complex valued permittivity. If you want refractive index data (rather than permittivity), remember that permittivity is simply the square of the refractive index.

```
matName = "Ag (Silver) - CRC";
?getmaterial(matName);
maxCoeff = getmaterial(matName,"max coefficient");
sampledData = getmaterial(matName,"sampled data");
# convert sampledData matrix to refractive index
f1  = pinch(sampledData,2,1); # first column
eps = pinch(sampledData,2,2);  # second column
nk1 = sqrt(eps);
# use getindex command for comparison
f2 = linspace(100e12,1000e12,100);
nk2 = getindex(matName,f2);
plotxy(c/f1*1e6,real(nk1),
    c/f1*1e6,imag(nk1),
    c/f2*1e6,real(nk2),
    c/f2*1e6,imag(nk2),
    "wavelength (um)","refractive index");
legend("n - getmaterial",
    "k - getmaterial",
    "n - getindex",
    "k - getindex"); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addmaterial ](./addmaterial.md) , [ setmaterial ](./setmaterial.md) ,
[ getindex ](./getindex.md) , [ getfdtdindex ](./getfdtdindex.md)
