# removesweepparameter

Removes a parameter from a parameter sweep/optimization/Monte Carlo/S-parameter sweep
item.

| **Syntax**                                      | **Description**                                                                                                                                                                      |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| removesweepparameter("name", "parameter_name"); | Removes a parameter from a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "parameter_name" is the parameter name. |

**Examples**

This example shows how to remove a parameter from a sweep. Please download the example
file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
removesweepparameter("thickness_sweep", "thickness");
```

This example shows how to remove the second row from the s-matrix mapping table in an
S-parameter matrix sweep.

```
removesweepparameter("s-parameter sweep",2);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copysweep ](./copysweep.md) , [ pastesweep ](./pastesweep.md) ,
[ addsweep ](./addsphere.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepresult ](./removesweepresult.md) ,
[ Sweep scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands)
,
[ Optimization scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
,
[ Monte Carlo scripting commands ](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
