# checkout

Checks out a licensed feature.

| **Syntax**           | **Description**                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| checkout(featureID); | Checks out and reserve a licensed feature. If the feature cannot be checked out, an error message will be shown in the Script Prompt window. The license will remain be checked out until the application quits. |

**Example**

```
checkout("INTERCONNECT_block_mode");
#If INTERCONNECT_block_mode license does not exist, the following message will be shown
Error: The license feature 'INTERCONNECT_block_mode' does not exist on ... 
```

**See Also**

[ run ](./run.md) , [ getsweepdata ](./getsweepdata.md) , [ addjob ](./addjob.md) ,
[ runjobs ](./runjobs.md) ,
[ parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
