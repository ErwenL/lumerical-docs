# addrect

Adds a rectangle primitive to the simulation environment.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addrect;              | Adds a rectangle primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addrect(struct_data); | Adds a rectangle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script creates a rectangle primitive, sets its dimension, and assigns a
material to it.

```
addrect;
set("name","new_rectangle");
set("x",1e-6);
set("x span",2e-6);
set("y",1e-6);
set("y span",5e-6);
set("z",0);
set("z span",10e-6);
set("material","Si (Silicon) - Palik");
```

**See Also**

[List of commands ](../lsf-script-commands-alphabetical.md), [set](./set.md)
