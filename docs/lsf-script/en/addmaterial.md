# addmaterial

Adds a new material to the material database given the material model or type and
returns the name of the new material. For details on available material models see:
[ Material permittivity models ](https://optics.ansys.com/hc/en-us/articles/360034394634-Material-Permittivity-Models)
and
[ Material conductivity models ](https://optics.ansys.com/hc/en-us/articles/360034915113-Material-Conductivity-Models)
.

| **Syntax**                         | **Description**                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| ?addmaterial;                      | Lists all available material models that can be added into the material database.                                              |
| out = addmaterial("materialtype"); | Adds a new material and returns the name of the new material. The argument "materialtype" has to match correct string exactly. |

**Example**

These commands add a new Conductive material, set the name to "aluminum", anisotropy to
"Diagonal", and set the permittivity as well as conductivity properties for the
material.

```
A=[4;5;6];
B=[1;2;3];
mymaterial = addmaterial("Conductive");
setmaterial(mymaterial,"name","Aluminum");
setmaterial("Aluminum", "Anisotropy", 1); # enable diagonal anisotropy
setmaterial("Aluminum","Permittivity", A);
setmaterial("Aluminum","Conductivity", B);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ deletematerial ](./deletematerial.md) , [ copymaterial ](./copymaterial.md) ,
[ setmaterial ](./setmaterial.md) , [ getmaterial ](./getmaterial.md)
