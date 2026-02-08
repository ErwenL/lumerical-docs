# addimportnk

Adds a nk import object to the FEEM simulation environment where the profile of the
material with a spatially varying index can be imported from an external Matlab file.

| **Syntax**                | **Description**                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addimportnk;              | Adds an import primitive to define material with a spatially varying index profile in the FEEM solver. This function does not return any data.                                                                                                                                                                                                               |
| addimportnk(struct_data); | Adds an import primitive to define material with a spatially varying index profile in the FEEM solver and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

Once the nk import object is created, the data can be imported from a matlab (.mat) file
using the GUI or by assigning a dataset to the object using the
[ importdataset ](./importdataset.md) script command. The dataset can be in rectilinear
or unstructured (finite-element) format.

**Example**

The following script command will add an import (n,k) object to the FEEM solver region
and will load an analytic 3D heat data into it.

```
addfeemsolver;
addimportnk;
# create coordinate vectors and 3D matrix for nk input
x = linspace(0,1e-6,11);
y = linspace(-1e-6,1e-6,2);
z = linspace(0,2e-6,101);
nk = matrix(11,2,101)+3.45; # assume the index input is 3.45 everywhere
for (i=1:length(x)){  
# assume that index varies along x-axis 
nk(i,:,:)=x(i)*1e5;}
# add waveguide
addrect;
setname('WG');
set('x min',-1e-6); 
set('x max',1e-6);
set('y span',2e-6); 
set('y',0);
set('z span',2e-6); 
set('z',1e-6);
# create dataset
nkmaterial = rectilineardataset("nk import",x,y,z);
nkmaterial.addparameter("lambda",1.55e-6); # (Required) add any parameter
nkmaterial.addattribute("nk",nk);
# load data into nk import
select("FEEM::nk import");
importdataset(nkmaterial);
set("volume type","solid");
set("volume solid","WG");
set("selected attribute","nk");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addfeemsolver ](./addfeemsolver.md) , [ rectilineardataset ](./rectilineardataset.md)
, [ select ](./select.md) , [ importdataset ](./importdataset.md)
