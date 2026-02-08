# addattribute

Adds an attribute to an existing dataset.

| **Syntax**                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R.addattribute("a_name", a);               | Adds the scalar attribute a to the dataset R. See [ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) for details about the required dimensions of attribute data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R.addattribute("a_vector", a_1, a_2, a_3); | Adds the vector attribute a_vector to the existing dataset R. The components of the vector are a_1, a_2 and a_3. See [ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) for details about the required dimensions of attribute data.                                                                                                                                                                                                                                                                                                                                                                                                  |
| R.addattribute("a_name", [data], "type");  | Adds the attribute "a_name" to the unstructured dataset R. [data] can be in one of the forms below: vertex_scalar_attribute[npts; npar_1; npar_2; ...1] vertex_vector_attribute[npts; npar_1; npar_2; ...3] cell_scalar_attribute[ncells; 1] cell_vector_attribute[ncells; 3] (npts is the number of vertices, the length of geometric parameters 'x', 'y', 'z' cells is the number of elements, equal to number of rows of geometry parameter 'elements' ) The "type" argument is an optional string to specify attribute type and can take values of "vertex" or "cell". If not provided, the function will guess the attribute type based on the shape of [data] argument. |

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

Alternatively, one can also create a vector rectilinear dataset (with the name E).

```
E = rectilineardataset("E",x,y,z);
E.addparameter("f",f);
E.addattribute("E",Ex,Ey,Ez); # add a vector E with the components Ex, Ey and Ez
visualize(E); # visualize this dataset in the Visualizer
```

**See Also**

- [rectilineardataset](./rectilineardataset.md)
- [addattribute](./addattribute.md)
- [addparameter](./addparameter.md)
- [visualize](./visualize.md)
- [datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [matrixdataset](./matrixdataset.md)
