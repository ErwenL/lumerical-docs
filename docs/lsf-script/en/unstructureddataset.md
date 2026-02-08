# unstructureddataset

Creates an empty dataset that is associated with arbitrary x/y/z coordinate in space,
and with additional matrix, a connectivity matrix to connect them. The connectivity
matrix comes after x, y, and z. Like rectilinear datasets, unstructured datasets can be
parameterized, and can contain an arbitrary number of attributes (see
[ addattribute) ](./addattribute.md) and parameters (see
[ addparameter) ](./addparameter.md) .

See
[ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
for more information. For datasets that are not associated with the x/y/z coordinates
(ex. transmission as a function of frequency), see [ matrixdataset ](./matrixdataset.md)
.

| **Syntax**                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unstructureddataset(x,y,z,C); | Creates an empty unstructured dataset associated with the coordinates x/y/z and a connectivity matrix to connect them. Arguments 'x', 'y' and 'z' must be the same length; equivalent to the total number of points. The argument 'C' should be a matrix of integers where the number of rows equal to number of shapes in the mesh, the number of columns should be 2 (line segments), 3 (triangles) or 4 (tetrahedra), and values should be integers. |

**Examples**

Below is a simple example of the usage of unstructured dataset. x, y and z vectors
represent arbitrary points in space and C represent the connectivity matrix that
connects them. The values for the vectors can be loaded from the
[ unstructured_charge_example.mat ](/hc/article_attachments/360046127873/unstructured_charge_example.mat)
file. It is possible to further script this process and import the data to an object,
eg, np density grid attribute, see the [ importdataset ](./importdataset.md) command.

```
# constructing an unstructured dataset
matlabload("unstructured_charge_example.mat"); # taking the data from a CHARGE simulation. The data can be from a different source
x = charge.x;
y = charge.y;
z = charge.z;
C = charge.elements;
data = unstructureddataset("test",x,y,z,C);
V_cathode = charge.V_cathode;
V_anode = charge.V_anode;
n = pinch(charge.n);
p = pinch(charge.p);
data.addparameter("V_cathode",V_cathode);
data.addparameter("V_anode",V_anode);
data.addattribute("n",n);
data.addattribute("p",p);
visualize(data);
```

This next example creates an unstructured dataset (with the name "Absorption") that
contains 2 data attributes: the power absorption Pabs, and the refractive index n. Both
attributes are a function of the spatial parameters x/y/z and frequency f. Connectivity
matrix cm has also been specified. To allow the user to access the frequency parameter
in terms of frequency or wavelength , both frequency (f) and wavelength (c/f) are added
as interdependent parameters.

```
Absorption = unstructureddataset("Absorption",x,y,z,cm);
Absorption.addparameter("lambda",c/f,"f",f);
Absorption.addattribute("Pabs",Pabs);
Absorption.addattribute("refractive index",n);
visualize(Absorption); # visualize this dataset in the Visualizer
```

This example shows how to define an equilaterial triangle in the plane z=0

```
x = [0;1;2];
y = [0;sqrt(3);0];
z = [0;0;0];
C = [1,3,2];
ds = unstructureddataset(x,y,z,C);
```

**See Also**

[ rectilineardataset ](./rectilineardataset.md) , [ addattribute ](./addattribute.md) ,
[ addparameter ](./addparameter.md) , [ visualize ](./visualize.md) ,
[ datasets ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) ,
[ getparameter ](./getparameter.md) , [ getattribute ](./getattribute.md) ,
[ matrixdataset ](./matrixdataset.md) , [ struct ](./struct.md)
