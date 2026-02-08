# addimporttemperature

Adds an import temperature source to the CHARGE solver (only applicable to
non-isothermal transport). The import temperature object can be used to import a
temperature map for non-isothermal simulation. A CHARGE solver region must be present in
the objects tree for this command to work.

| **Syntax**                         | **Description**                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addimporttemperature;              | Adds an import temperature source to the CHARGE solver. The source only gets applied if the "temperature dependence" is set to "non-isothermal." This function does not return any data.                                                                                                 |
| addimporttemperature(struct_data); | Adds an import temperature source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

Once the import temperature source is created, the data can be imported from a matlab
(.mat) file using the GUI or by assigning a dataset to the object using the
[ importdataset ](./importdataset.md) script command. The dataset can either be in
rectilinear or unstructured (finite-element) format.

**Example**

The following script command will add an import temperature source and will load an
analytic 3D temperature data into it.

```
addimporttemperature;
set("name","Tmap");
# create coordinate vectors and 3D matrix for temperature map
x = linspace(0,1e-6,11);
y = linspace(-1e-6,1e-6,2);
z = linspace(0,2e-6,101);
T = matrix(11,2,101) + 400;  # assume the temperature is 400 K everywhere
# create dataset
temperature = rectilineardataset("temp",x,y,z);
temperature.addparameter("a",1);  # add a dummy parameter
temperature.addattribute("T",T);
# load data into source
select("CHARGE::Tmap"); 
importdataset(temperature);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ linspace ](./linspace.md) , [ rectilineardataset ](./rectilineardataset.md) ,
[ select ](./select.md) , [ importdataset ](./importdataset.md) ,
[ addimportheat ](./addimportheat.md)
