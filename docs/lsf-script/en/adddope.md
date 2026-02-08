# adddope

Adds a [constant doping object](https://optics.ansys.com/hc/en-us/articles/360034918653)
to the simulation environment. This command requires a CHARGE solver region to be
present in the objects tree.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| adddope;              | Add a constant doping region. This function does not return any data.                                                                                                                                                                                                                |
| adddope(struct_data); | Adds a constant doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a p-type constant doping object and set its
dimension and concentration.

```
adddope;
set("name","pwell");
set("dopant type","p");
set("concentration",1e25);  # SI unit (/m3)
set("x",0);
set("x span",2e-6);
set("y",0);
set("y span",1e-6);
set("z",5e-6);
set("z span",1e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ adddiffusion ](./adddiffusion.md)
