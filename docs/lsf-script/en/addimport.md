# addimport

Adds an import primitive to the simulation environment. The import primitive can be used
to create a 3D geometry by importing a surface, an image, or binary data. It can also be
used to create an n,k material.

| **Syntax**              | **Description**                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addimport;              | Adds an import primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addimport(struct_data); | Adds an import primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will generate a surface data and then use the data to
create a layer of glass whose top surface is defined by the generated data.

```
# generate a surface
nx = 50;
ny = 40;
x = linspace(-6,6,nx);
y = linspace(-5,5,ny);
X = meshgridx(x,y);
Y = meshgridy(x,y);
Z = exp(-(X^2+Y^2)/4^2) * sin(pi*Y/2);
# Remember that all units are SI. We defined the surface in microns
# so all lengths must be multiplied by 1e-6
x = x*1e-6; # switch to SI units
y = y*1e-6; # switch to SI units
Z = Z*1e-6; # switch to SI units
# create substrate layer with an import object
addimport;
set("material","SiO2 (Glass) - Palik");
# upper surface and reference height
importsurface2(Z,x,y,1);
set("upper ref height",0e-6); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ importsurface ](./importsurface.md) , [ importsurface2 ](./importsurface2.md)
