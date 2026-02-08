# addefieldmonitor

Adds an
[electric field monitor](https://optics.ansys.com/hc/en-us/articles/360034918793) to the
simulation environment. This command requires the presence of a CHARGE solver region in
the objects tree.

| **Syntax**                     | **Description**                                                                                                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addefieldmonitor;              | Adds an electric field monitor to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addefieldmonitor(struct_data); | Adds an electric field monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add a 2D y-normal electric field monitor to the
simulation environment, set its dimension, enable saving the electrostatic potential,
and save the data in a .mat file.

```
addefieldmonitor;
set("name","E_field");
set("monitor type",6);  # 2D y-normal
set("x",0);
set("x span",5e-6);
set("y",0);
set("z",0);
set("y span",5e-6);
set("record electrostatic potential",1);
set("save data",1);
filename = "electric_field.mat";
set("filename",filename);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ addbandstructuremonitor ](./addbandstructuremonitor.md) ,
[ addchargemonitor ](./addchargemonitor.md) , [ addjfluxmonitor ](./addjfluxmonitor.md)
