# addgridattribute

Adds a grid attribute object to the simulation environment. Grid attribute objects
include:

- [Liquid Crystal Rotation](https://optics.ansys.com/hc/en-us/articles/360034915153)
- [Permittivity Rotation](https://optics.ansys.com/hc/en-us/articles/360034394714)
- [Matrix Transformation](https://optics.ansys.com/hc/en-us/articles/360034915173)
- [np Density and Temperature Index Perturbation](https://optics.ansys.com/hc/en-us/articles/360034901753)

| **Syntax**                | **Description**                                 |
| ------------------------- | ----------------------------------------------- |
| addgridattribute("type"); | Adds a grid attribute object to the simulation. |

- type: Type of attribute to add. Options are "lc orientation", "permittivity rotation",
  "matrix transform", "np density", or "temperature".

This function does not return any data.\
addgridattribute("type",dataset); | Adds a grid attribute with spatially varying data.

- type: Type of attribute to add. Options are "lc orientation", "permittivity rotation",
  "matrix transform", "np density", or "temperature".
- dataset: A dataset containing the grid attribute data - see the below table for
  details.

| Data                                               | Simulation object                      | Dataset type | Name for variables defining coordinate data                                                                                               | Name for variables defining actual data |
| -------------------------------------------------- | -------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Liquid crystal orientation (3 element unit vector) | 'lc orientation' grid attribute        | Rectilinear  | x, y, z                                                                                                                                   | u                                       |
| Rotation angles in radians                         | 'permittivity rotation' grid attribute | Rectilinear  | x, y, z                                                                                                                                   | theta, phi, psi                         |
| Unitary transform matrix (3x3 tensor)              | 'matrix transform' grid attribute      | Rectilinear  | x, y, z                                                                                                                                   | U                                       |
| Charge density                                     | 'np density' grid attribute            | Unstructured | x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) | n, p                                    |
| Temperature in Kelvin                              | 'temperature' grid attribute           | Unstructured | x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) | N                                       |

### Example

The following script is an excerpt from LCD_twist.lsf in the
[ Twisted Nematic LCD](**%20to%20be%20defined%20**) application example which defines a
spatially varying liquid crystal.

```
# define x/y/z
x = 0;
y = 0;
z = linspace(0e-6,5e-6,100);
X = meshgrid3dx(x,y,z);
Y = meshgrid3dy(x,y,z);
Z = meshgrid3dz(x,y,z);
n = matrix(length(x),length(y),length(z),3);
# define the orientation function
n(1:length(x),1:length(y),1:length(z),1) = cos(Z*pi*1e5);
n(1:length(x),1:length(y),1:length(z),2) = sin(Z*pi*1e5);
n(1:length(x),1:length(y),1:length(z),3) = Z;
# create dataset containing orientation vectors and position parameters
LC=rectilineardataset("LC",x,y,z);
LC.addattribute("u",n);
# add LC import grid attribute
addgridattribute("lc orientation",LC);
setnamed("LC attribute","nz",50); # set resolution
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md),
[ Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets),
[ importdataset](./importdataset.md), [ cleardataset](./cleardataset.md),
[ unstructureddataset](./unstructureddataset.md),
[ Dataset builder](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder),
[LC Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915153),
[Permittivity Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034394714),
[Matrix Transformation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915173)
