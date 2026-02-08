# removesweepresult

Removes a result from a sweep/optimization/Monte Carlo item.

| **Syntax**                                | **Description**                                                                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| removesweepresult("name", "result_name"); | Removes a result from a sweep/optimization/Monte Carlo item. "name" is the absolute name of an analysis item. |

**Example**

This example shows how to remove a result from a sweep. Please download the example file
from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
removesweepresult("thickness_sweep", "T");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copysweep ](./copysweep.md) , [ pastesweep ](./pastesweep.md) ,
[ addsweep ](./addsphere.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ Sweep scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands)
,
[ Optimization scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
,
[ Monte Carlo scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
