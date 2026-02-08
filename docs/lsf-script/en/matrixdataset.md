# matrixdataset

Creates an empty matrix dataset. Matrix datasets are used for data (attributes and
parameters) that don't have any spatial dependence (i.e. Reflection vs frequency). For
datasets that do have x/y/z spatial coordinates (i.e. electric fields), use
[rectilineardataset](./rectilineardataset.md) or
[unstructureddataset](./unstructureddataset.md).

Matrix datasets can be parameterized, and can contain an arbitrary number of attributes
(see [addattribute)](./addattribute.md) and parameters (see
[addparameter)](./addparameter.md).

See
[Dataset introduction](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
for more information.

| **Syntax**             | **Description**                                |
| ---------------------- | ---------------------------------------------- |
| matrixdataset;         | Creates an empty dataset.                      |
| matrixdataset("name"); | Creates an empty dataset with the name "name". |

**Examples**

This example uses a matrix dataset to store cross section (sigma) data as a function of
frequency. In this case, the cross section data sigma is the attribute, and frequency is
the parameter. To allow the user to access the frequency parameter in terms of frequency
or wavelength , both frequency (f) and wavelength (c/f) are added as interdependent
parameters.

```
sigma = matrixdataset("cross_section");
sigma.addparameter("lambda",c/f,"f",f); # add parameter f and lambda
sigma.addattribute("sigma",CS); # add attribute CS
visualize(sigma); # visualize this dataset in the Visualizer
```

The following script code generates some example data, then creates a R(radius,height)
dataset.

```
# create example results
radius = 0:10; 
height = 1:0.1:3;
reflection = randmatrix(length(radius),length(height)); 
# create Reflection dataset
R = matrixdataset("R"); # initialize dataset
R.addparameter("radius",radius); # add radius parameter
R.addparameter("height",height); # add height parameter
R.addattribute("R",reflection); # add reflection attribute
# plot data
image(radius,height,reflection); # use original matrices
image(R.radius,R.height,R.R);  # use dataset
# send dataset to visualizer
visualize(R); 
```

**See Also**

[rectilineardataset](./rectilineardataset.md), [addattribute](./addattribute.md),
[addparameter](./addparameter.md), [visualize](./visualize.md),
[datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets),
[getparameter](./getparameter.md), [getattribute](./getattribute.md),
[matrixdataset](./matrixdataset.md), [struct](./struct.md)
