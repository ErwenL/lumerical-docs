# adddgtdsolver

Adds a [DGTD solver region](https://optics.ansys.com/hc/en-us/articles/360034397874) to
the simulation environment.

| **Syntax**                  | **Description**                                                                                                                                                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adddgtdsolver;              | Adds a DGTD solver region to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| adddgtdsolver(struct_data); | Adds a DGTD solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example 1**

The following script commands will add a DGTD solver to the objects tree and print the
name of all of its properties.

```
adddgtdsolver;
?set;
```

**Example 2**

The following script command will add a DGTD solver region, assign it to a simulation
region, and set the simulation time.

```
adddgtdsolver;
set("solver geometry","simulation region 1"); 
set("simulation time",100e-15);  # 100 fs
```

**See Also**

[ adddgtdmesh ](./adddgtdmesh.md)
