# addsphere

Adds a sphere primitive to the simulation environment.

| **Syntax**              | **Description**                                                                                                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addsphere;              | Adds a sphere primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addsphere(struct_data); | Adds a sphere primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a sphere with a radius of 5 um centered at
(x,y,z) = (1, 2, 0) microns.

```
addsphere;
set("name","new_sphere");
set("x",1e-6);
set("y",2e-6);
set("z",0);
set("radius",5e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
