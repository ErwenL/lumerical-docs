# getresult

Get results from simulation objects. Results will be returned as datasets.

| **Syntax**                         | **Description**                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| ?getresult("monitor_name");        | Returns the names of all the results for the monitor. All the dataset and scalar matrix results will be returned in this case. |
| R = getresult("monitor_name","T"); | Returns the result T from the monitor. T is a dataset.                                                                         |

**Examples**

This example shows how to get the electric field dataset from a monitor. We then apply a
number of operations to the dataset, such as finding the maximum |E|^2 value, viewing
the dataset with the visualizer, and creating a plot of Ex at the first frequency point.

Note that E is a dataset, rather than a simple matrix based variable. Data within the
dataset can be accessed with the '.' operator, as shown below.

```
# get Electric field dataset
E=getresult("monitor","E");
# output dataset value to prompt
?E;
# check size of position vectors and data matrices
?size(E.f);
?size(E.Ex);
# find maximum |E|^2 value 
?max(E.E2);
# view dataset with visualizer
visualize(E);
# select first frequency point of Ex data, then create plot
Ex = pinch(E.Ex,4,1); 
image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex");
 E vs x, y, z, lambda/f
 result: 
 5 1 
 result: 
 343 255 1 5 
 result: 
 3.223651 
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md),
[ haveresult](./haveresult.md),
[ Dataset introduction](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets),
[ "." operator](./dot_cmd.md), [ visualize](./visualize.md), [ getdata](./getdata.md),
[ rectilineardataset](./rectilineardataset.md), [ matrixdataset](./matrixdataset.md),
[ getattribute](./getattribute.md), [ addattribute](./addparameter.md),
[ splitstring ](./splitstring.md)
