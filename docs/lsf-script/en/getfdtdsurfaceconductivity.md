# getfdtdsurfaceconductivity

For materials which use a surface conductivity material model (such as Graphene), this
function returns the surface conductivity of the material in the database as it will be
used in an actual simulation. For a list of materials which use the surface conductivity
model, see
[ Material conductivity models ](https://optics.ansys.com/hc/en-us/articles/360034915113-Material-Conductivity-Models)
.

The conductivity evaluated at the specified frequencies is returned. Note that the fit
result depends on the fit parameters, Max coefficients and Tolerance set for the
material, thus getfdtdsurfaceconductivity result depends on those parameters as well.

| **Syntax**                                                           | **Description**                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getfdtdsurfaceconductivity( "materialname", f, fmin, fmax);    | Returns the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified frequency f. Similar to getsurfaceconductivity, but you also specify fmin and fmax, the span of frequency range of the simulation. All frequency units are in Hz. |
| getfdtdsurfaceconductivity("materialname", f,fmin, fmax, component); | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.                                                                                                                                                                                   |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addmaterial ](./addmaterial.md) , [ setmaterial ](./setmaterial.md) ,
[ getsurfaceconductivity ](./getsurfaceconductivity.md)
