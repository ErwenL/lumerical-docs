# addgroup

Adds a container group to the simulation environment. Container groups can be used to
put multiple structures, monitors, and/or sources together in a single group in the
objects tree. In Ansys Lumerical Multiphysics™, container groups are always children of
the solver regions and cannot contain any structure. If multiple solver regions are
present in the Ansys Lumerical Multiphysics objects tree, this command will add a
container group to the solver region that is currently selected.

| **Syntax**               | **Description**                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addgroup;                | Adds a container group to the simulation environment. In Ansys Lumerical Multiphysics, the added container group is placed under the currently selected solver region. This function does not return any data.                                                                                                                                                                                 |
| addgroup(struct_data);   | Adds a container group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. In Ansys Lumerical Multiphysics, the added container group is placed under the currently selected solver region. This function does not return any data. |
| addgroup(“solver_name”); | Only for Ansys Lumerical Multiphysics. Adds a container group to the solver region specified by solver_name. This function does not return any data.                                                                                                                                                                                                                                           |

**Example**

Add a container group to the HEAT solver region (in Ansys Lumerical Multiphysics) and
put a uniform heat source in it.

```
select("HEAT");
addgroup;
set("name","test_group");
adduniformheat;
addtogroup("test_group");
```

NOTE: In this example script, since the uniform heat source is also a child of the HEAT
solver, we do not need to specify the full path for the container group name (e.g.
HEAT::test_group).

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addtogroup ](./addtogroup.md) , [ addstructuregroup ](./addstructuregroup.md) ,
[ addanalysisgroup ](./addanalysisgroup.md)
