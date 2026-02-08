# addresource

Adds a resource to the list of available resources in resource manager.

| **Syntax**             | **Description**                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addresource("solver"); | Adds a resource to the list of available resources in resource manager. The "solver" argument is used to select the solver to add the resource to. The "solver" argument is not supported by INTERCONNECT. It also returns the resource number as an integer. |

**Example**

The following line will add a resource to the DGTD solver in Finite Element IDE.

```
addresource("DGTD");  
```

**See Also**

[deleteresource](./deleteresource.md), [setresource](./setresource.md),
[getresource](./getresource.md)
