# setresource

Sets properties of the available resources in resource manager for the specified solver.

| **Syntax**                                                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setresource("solver", resource_num, "property", "value"); | Sets properties of the available resources in resource manager for the specified solver. The "solver" argument is used to select the solver from which the resource is being selected. The "solver" argument is not supported by INTERCONNECT. resource_num is the number of the desired resource (row number in resource manager). If not specified, the command will return the number of resources currently available for the specified solver. "property" is the desired property of the resource and "value" is the value to be set or the specified property. |

**Note** : The mpi executable cannot be set using this command while in
[safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Example**

This example will set the number of processes for the second resource of the DGTD solver
to 4:

```
setresource("DGTD",2,"processes","4");
```

**See Also**

[addresource](./addresource.md), [deleteresource](./deleteresource.md),
[getresource](./getresource.md)
