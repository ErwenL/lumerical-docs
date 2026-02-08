# addimportedsource

Adds an imported source to the simulation environment.

| **Syntax**                      | **Description**                                                                                                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addimportedsource;              | Adds an imported source to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addimportedsource(struct_data); | Adds an imported source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add an imported source to the simulation environment,
assign a name to it and load an E field profile from a \*.mat file.

```
addimportedsource;
set("name","source2");
# Load a field profile saved in Matlab file named myfile.mat
select("source2");
importdataset("myfile.mat");
```

To see an example of how script commands can be used to create an imported source using
monitor data go to this KB page:
[ Custom source profile from monitor data ](https://optics.ansys.com/hc/en-us/articles/360034383034-Custom-source-profile-from-monitor-data)
.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ asapimport ](./asapimport.md) , [ asapload ](./asapload.md) ,
[ asapexport ](./asapexport.md) , [ importdataset ](./importdataset.md)
