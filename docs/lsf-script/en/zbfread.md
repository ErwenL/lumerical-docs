# zbfread

zbfread reads a Zemax zbf file and adds the data into structure array that will be
available in the script workspace for further processing. The structure array will
contain the following data:

• Ex, Ey, Ez, x, y, z

• frequency, wavelength, index

Note that ONLY the transverse E field components can be obtained from the zbf file. The
longitudinal component is not supported by the zbf format and it is populated with zero
values during the read operation.

| **Syntax**                           | **Description**                                                                                                                                                             |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A = zbfread("filename.zbf");         | Reads zbf file into structure array A where: A.index is the refractive index stored in the zbf file A.beam is the dataset that contains the E field vs frequency/wavelength |
| A = zbfread("filename.zbf", axis=3); | Axis = 1,2,3 is an optional parameter to specify if the beam should be rotated to propagate along x or y axis instead of the default z axis                                 |

### Example

The following code example shows how to read zbf file data into a structure array with
and without rotation of the default propagation direction.

```
# Create spatial distribution of E field data with Gaussian distribution
x = linspace(-5e-6,5e-6,100);
y = linspace(-6e-6,6e-6,101);
X = meshgridx(x,y);
Y = meshgridy(x,y);
Ex = exp(- (X^2+Y^2)/(2e-6)^2);
Ey = 2i*Ex;
Ez = 0*Ey;
# Create dataset and add E field and wavelength data
M = rectilineardataset("E",x,y,0);
M.addparameter("lambda",500e-9);
M.addattribute("E",Ex,Ey,Ez);
M.addattribute("scalar",3*Ex);
# Write dataset M into zbf file in with and without the optional parameters
zbfwrite("testfile.zbf",M);
# Read the structured data from zbf file without rotation(default z direction)
B = zbfread("testfile.zbf");
visualize(B.beam);
# Read the structured data from zbf file and rotate the propagation direction to y
B = zbfread("testfile.zbf",axis=2);
visualize(B.beam);
```

**See Also**

[zbfexport](./zbfread.md), [zbfload](./zbfload.md), [zbfwrite](./zbfwrite.md),
[struct](./struct.md)
