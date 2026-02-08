# getparameter

Gets a parameter from an existing dataset.

| **Syntax**                       | **Description**                                                                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ?getparameter(R);                | Returns the names of all the parameters in the dataset R.                                                                                                                                                                                        |
| Parameter = R.getparameter("p"); | Retrieves the parameter p from the existing dataset R. The result "Parameter" is a scalar matrix. See [ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) for details about dimensions of attribute data. |
| Parameter = getparameter(R,"p"); | Retrieves the parameter p from the existing dataset R. The result "Parameter" is a scalar matrix. See [ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) for details about dimensions of attribute data. |

**Examples**

This example retrieves the dataset results "E" from a profile monitor, and then uses the
getparameter command to get the "f" parameter, and the
[ getattribute ](./getattribute.md) command to get the "Ex" and "E2" attributes from the
dataset. Note that f, Ex and E2 are all scalar matrices, like the results one would get
with the [ getdata ](./getdata.md) command.

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

[ matrixdataset ](./matrixdataset.md) , [ rectilineardataset ](./rectilineardataset.md)
, [ "." operator ](./dot_cmd.md) , [ getresult ](./getresult.md) ,
[ getattribute ](./getattribute.md) , [ visualize ](./visualize.md) ,
[ datasets ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
