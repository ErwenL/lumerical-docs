# deletesweep

Deletes a specified parameter sweep, optimization, or Monte Carlo analysis task.

| **Syntax**           | **Description**                                                                        |
| -------------------- | -------------------------------------------------------------------------------------- |
| deletesweep("name"); | Deletes the sweep, optimization, or Monte Carlo analysis task with the specified name. |

**Examples**

This example shows how to delete a task named "thickness_sweep". Please download the
example file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
deletesweep("thickness_sweep");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addsweep ](./addsweep.md) , [ copysweep ](./copysweep.md) ,
[ pastesweep ](./pastesweep.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)
