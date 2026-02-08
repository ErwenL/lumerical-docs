# addchargesolver

Adds an
[electrical (CHARGE) solver region](https://optics.ansys.com/hc/en-us/articles/360034924473)
to the simulation environment.

| **Syntax**                    | **Description**                                                                                                                                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addchargesolver;              | Adds an electrical (CHARGE) solver region to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addchargesolver(struct_data); | Adds an electrical (CHARGE) solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a 2D y-normal CHARGE solver region, set its
dimension, and run the simulation. The script assumes that the simulation environment
already has the geometry and boundary conditions set up.

```
addchargesolver;
set("solver geometry",1);  # 2D y-normal
set("x",0);
set("x span",2e-6);
set("y",0);
set("z",0);
set("z span",10e-6);
run;
```

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [run](./run.md)
