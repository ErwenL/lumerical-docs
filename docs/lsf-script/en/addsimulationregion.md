# addsimulationregion

Adds a simulation region to the Finite Element IDE design environment. Once created the
simulation region can be linked to any existing solver.

| **Syntax**                        | **Description**                                                                                                                                                                                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addsimulationregion;              | Adds a simulation region to the Finite Element IDE design environment. This function does not return any data.                                                                                                                                                                  |
| addsimulationregion(struct_data); | Adds a simulation region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a 2D y-normal simulation region, rename it, set
its dimension, and assign it to the CHARGE solver (assuming that it already exists in
the objects tree).

```
addsimulationregion;
set("name","CHARGE simulation region");
set("dimension",2);  # 2D y-normal
set("x",0);
set("x span",2e-6);
set("y",0);
set("z",0);
set("z span",10e-6);
setnamed("CHARGE","simulation region","CHARGE simulation region");
```

**See Also**

[ adddgtdsolver ](./adddgtdsolver.md)
