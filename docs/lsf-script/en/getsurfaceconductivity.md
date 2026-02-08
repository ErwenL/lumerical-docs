# getsurfaceconductivity

For materials which use a surface conductivity material model (such as Graphene), this
function returns the complex index of any material that is in the material database. The
surface conductivity at the specified frequency is interpolated from the neighboring
frequencies where the conductivity data is available. For a list of materials which use
the surface conductivity model, see
[ Material conductivity models ](https://optics.ansys.com/hc/en-us/articles/360034915113-Material-Conductivity-Models)
.

| **Syntax**                                             | **Description**                                                                                                                                                                     |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getsurfaceconductivity( "materialname", f);      | Returns the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified frequency f where f is in units of Hz. |
| getsurfaceconductivity( "materialname", f, component); | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.                                                        |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addmaterial ](./addmaterial.md) , [ setmaterial ](./setmaterial.md) ,
[ getfdtdsurfaceconductivity ](./getfdtdsurfaceconductivity.md)
