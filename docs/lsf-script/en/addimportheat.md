# addimportheat

Adds a heat source to the Finite Element IDE simulation environment where the profile of
the heat source can be imported from an external source. For the CHARGE solver, the
import heat source only gets applied if the "temperature dependence" is set to
"coupled."

| **Syntax**                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addimportheat;                             | Adds an import primitive to define a heat source. This format of the command is only application when only one solver is present/active in the model tree. This function does not return any data. If multiple solvers are present then use the second or fourth format.                                                                                                                                                                                      |
| addimportheat("solver_name");              | This format of the command will add an import heat source to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.”                                                                                                                                                                                                                                                                                                         |
| addimportheat(struct_data);                | Adds an import primitive to define a heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.                                                                                                                                                       |
| addimportheat("solver_name", struct_data); | This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” Adds an import primitive to define a heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

Once the import heat source is created, the data can be imported from a matlab (.mat)
file using the GUI or by assigning a dataset to the object using the
[ importdataset ](./importdataset.md) script command. The dataset can be in rectilinear
or unstructured (finite-element) format.

**Example**

The following script command will add an import heat source to the HEAT solver region
and will load an analytic 3D heat data into it.

```
addimportheat("HEAT");
set("name","Pin"); 
# create coordinate vectors and 3D matrix for heat input
x = linspace(0,1e-6,11);
y = linspace(-1e-6,1e-6,2);
z = linspace(0,2e-6,101);
Q = matrix(11,2,101) + 1e15;  # assume the heat input is 1e15 W/m^3 everywhere 
# create dataset
heat = rectilineardataset("Pin",x,y,z);
heat.addparameter("a",1);  # add a dummy parameter
heat.addattribute("Q",Q); 
# load data into source
select("HEAT::Pin"); 
importdataset(heat);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addemasolver ](./linspace.md) , [ rectilineardataset ](./rectilineardataset.md) ,
[ select ](./select.md) , [ importdataset ](./importdataset.md) ,
[ adduniformheat ](./adduniformheat.md) ,
[ addimporttemperature ](./addimporttemperature.md)
