# getattribute

Gets an attribute from an existing dataset.

| **Syntax**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ?getattribute(R);                | Returns the names of all the attributes in the dataset R.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Attribute = R.getattribute("a"); | Retrieves the attribute a from the existing dataset R. The result "Attribute" is a matrix in one of the forms below depending on the type of atrribute: vertex_scalar_attribute[npts; npar_1; npar_2; ...1] vertex_vector_attribute[npts; npar_1; npar_2; ...3] cell_scalar_attribute[ncells; 1] cell_vector_attribute[ncells; 3] "npts" is the number of vertices which is equal tothe length of geometric parameters 'x', 'y', 'z' "ncells" is the number of elements equal to number of rows of geometry parameter 'elements' |
| Attribute = getparameter(R,"a"); | Retrieves the attribute a from the existing dataset R. The result "Attribute" is a matrix in one of the forms below depending on the type of atrribute: vertex_scalar_attribute[npts; npar_1; npar_2; ...1] vertex_vector_attribute[npts; npar_1; npar_2; ...3] cell_scalar_attribute[ncells; 1] cell_vector_attribute[ncells; 3] "npts" is the number of vertices which is equal tothe length of geometric parameters 'x', 'y', 'z' "ncells" is the number of elements equal to number of rows of geometry parameter 'elements' |

**Examples**

This example retrieves the dataset results "E" from a profile monitor, and then uses the
[ getparameter ](./getparameter.md) command to get the "f" parameter, and the
getattribute command to get the "Ex" and "E2" attributes from the dataset. Note that f,
Ex and E2 are all scalar matrices, like the results one would get with the
[ getdata ](./getdata.md) command.

```
E = getresult("profile","E");
f = E.getparameter("f");  # the parameter f
Ex = E.getattribute("Ex"); # the x component of the electric field
E2 = E.getattribute("E2"); # the electric field intensity, note that this only works if E is a vector
```

Note that one can also use the [ "." operator ](./dot_cmd.md) to retrieve the parameters
and attributes directly. For example:

```
E = getresult("profile","E");
f = E.f;  # the parameter f
Ex = E.Ex; # the x component of the electric field
E2 = E.E2; # the electric field intensity, note that this only works if E is a vector
```

**See Also**

[ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
, [ matrixdataset ](./matrixdataset.md) ,
[ rectilineardataset ](./rectilineardataset.md) , [ "." operator ](./dot_cmd.md) ,
[ getresult ](./getresult.md) , [ getparameter ](./getparameter.md) ,
[ visualize ](./visualize.md) ,
[ datasets ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
