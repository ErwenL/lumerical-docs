# addparameter

Adds a parameter to an existing dataset.

| **Syntax**                                    | **Description**                                                                                                                                                                                             |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R.addparameter("p_name", p);                  | Adds the parameter p to the existing dataset R.                                                                                                                                                             |
| R.addparameter("p1_name", p1, "p2_name", p2); | Adds the interdependent parameter p1_name, p2_name to the R dataset. The most common interdependent parameter is frequency and wavelength. Parameters that are not interdependent must be added separately. |

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

**See Also**

[ rectilineardataset ](./rectilineardataset.md) , [ addattribute ](./addattribute.md) ,
[ addparameter ](./addparameter.md) , [ visualize ](./visualize.md) ,
[ datasets ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets) ,
[ getparameter ](./getparameter.md) , [ getattribute ](./getattribute.md) ,
[ matrixdataset ](./matrixdataset.md)
