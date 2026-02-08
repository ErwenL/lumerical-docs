# rectilineardataset

Creates an empty rectilinear dataset that is associate with the x/y/z coordinates (ex. E
and H fields). Like matrix datasets, rectilinear datasets can be parameterized, and can
contain an arbitrary number of attributes (see [addattribute)](./addattribute.md) and
parameters (see [addparameter)](./addparameter.md).

See
[Dataset introduction](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
for more information.

For datasets that are not associated with the x/y/z coordinates (ex. transmission as a
function of frequency), see [ matrixdataset](./matrixdataset.md).

| **Syntax**                                | **Description**                                                                                                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rectilineardataset(x,y,z);                | Creates a empty rectilinear dataset associated with the coordinates x/y/z. Arguments 'x', 'y' and 'z' may be different lengths and the total number of points is the product of their lengths.                      |
| rectilineardataset("dataset_name",x,y,z); | Creates a empty rectilinear dataset named "dataset_name" associated with the coordinates x/y/z. Arguments 'x', 'y' and 'z' may be different lengths and the total number of points is the product of their lengths. |

**Examples**

This example creates a rectilinear dataset (with the name "Absorption") that contains 2
data attributes: the power absorption Pabs, and the refractive index n. Both attributes
are a function of the spatial parameters x/y/z and frequency 'f'. To allow the user to
access the frequency parameter in terms of frequency or wavelength , both frequency (f)
and wavelength (c/f) are added as interdependent parameters.

```
Absorption = rectilineardataset("Absorption",x,y,z);
Absorption.addparameter("lambda",c/f,"f",f);
Absorption.addattribute("Pabs",Pabs);
Absorption.addattribute("refractive index",n);
visualize(Absorption); # visualize this dataset in the Visualizer
```

The following script code shows how to get the raw data from a frequency monitor in FDTD
(using getdata), and how to manually create a dataset from that data. It also shows how
to directly get the electric field dataset from the monitor in a single command (using
getresult).

```
# monitor name
m="monitor";
# get individual data elements with getdata
x=getdata(m,"x");
y=getdata(m,"y");
z=getdata(m,"z");
f=getdata(m,"f");
Ex=getdata(m,"Ex");
Ey=getdata(m,"Ey");
Ez=getdata(m,"Ez");
# create the electric field dataset from the raw data
E_manual = rectilineardataset("E_manual",x,y,z);  # initialize dataset and provide spatial position vectors
E_manual.addparameter("lambda",c/f,"f",f);  # add additional parameter: frequency 
E_manual.addattribute("E",Ex,Ey,Ez);     # add vector electric field attribute
# all of the above commands can be avoided with a single getresult command
E_fromMonitor = getresult(m,"E");
```

The following script code shows how to access the data stored in the 'E_manual' dataset
created in the above example

```
# output contents of dataset to prompt
?E_manual;
# Get parameters
x   = E_manual.x;
y   = E_manual.y;
z   = E_manual.z;
f   = E_manual.f;
lambda = E_manual.lambda;
x_1  = E_manual.x(1); 
# Get attributes. Remember that E is a vector quantity
Ex = E_manual.Ex; # Ex component
Ey = E_manual.Ey; # Ey component
Ez = E_manual.Ez; # Ez component
E2 = E_manual.E2; # |E|^2
E = E_manual.E;  # get all components in a single matrix. An extra dimension of length 3 will be added to the matrix, for each vector component.
```

**See Also**

[rectilineardataset](./rectilineardataset.md), [addattribute](./addattribute.md),
[addparameter](./addparameter.md), [visualize](./visualize.md),
[datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets),
[getparameter](./getparameter.md), [getattribute](./getattribute.md),
[ matrixdataset](./matrixdataset.md), [struct](./struct.md)
