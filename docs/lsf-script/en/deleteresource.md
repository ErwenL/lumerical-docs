# deleteresource

Removes the selected resource from the list of available resources in resource manager.

| **Syntax**                             | **Description**                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deleteresource("solver",resource_num); | Removes the selected resource from the list of available resources in resource manager. The "solver" argument is used to select the solver to delete the resource from. The "solver" argument is not supported by INTERCONNECT. resource_num is the number (row number in resource manager list) for the resource to be deleted. |

**Example**

The following line will delete the second resource from the DGTD solver in DEVICE.

```
deleteresource("DGTD","2");  
```

**See Also**

[addresource](./addresource.md), [setresource](./setresource.md),
[getresource](./getresource.md)
