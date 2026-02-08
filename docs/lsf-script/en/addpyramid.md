# addpyramid

Adds a [pyramid](https://optics.ansys.com/hc/en-us/articles/360034382254) primitive to
the simulation environment.

| **Syntax**               | **Description**                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addpyramid;              | Adds a pyramid primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addpyramid(struct_data); | Adds a pyramid primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add a pyramid object to the simulation environment
and sets its dimension:

```
addpyramid;
set("name","my_pyramid");
set("x span bottom",5e-6);
set("x span top",3e-6);
set("y span bottom",4e-6);
set("y span top",3e-6);
set("z span",1e-6);
set("material","Si (Silicon) - Palik");
```

For a list of the editable properties of the added pyramid object, please see
[Pyramid - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034382254).

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set](./set.md),
[Pyramid - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034382254)
