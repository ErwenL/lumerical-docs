# copysweep

Copies a sweep/optimization/Monte Carlo analysis item to clipboard.

| **Syntax**         | **Description**                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| copysweep("name"); | Copies a sweep/optimization/Monte Carlo analysis item to clipboard. "name" is the absolute name of a sweep/optimization/Monte Carlo analysis (eg. ::optimization::sweep1) |

**Example**

This example copies the sweep "thickness_sweep" to the clipboard and pastes it back to
the "Optimizations and Sweeps" tab again. Please download the example file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
copysweep("thickness_sweep");
pastesweep("");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addsweep ](./addsweep.md) , [ deletesweep ](./deletesweep.md) ,
[ pastesweep ](./pastesweep.md) , [ addsweep ](./addsphere.md) ,
[ insertsweep ](./insertsweep.md) , [ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md)
