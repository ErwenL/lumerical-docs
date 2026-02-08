# pastesweep

Pastes a sweep/optimization/Monte Carlo analysis item from clipboard to the
"Optimizations and Sweeps" tab.

| **Syntax**          | **Description**                                                                                                                                                                                                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pastesweep("name"); | Pastes a sweep/optimization/Monte Carlo analysis item from clipboard. "name" is the absolute name of the parent item where the new analysis item will be pasted as a child. If the name is empty, paste the new analysis item as a top-most item. Returns the absolute name of the new item. Returns empty string if paste got failed. |

**Example**

Please refer to the [ copysweep ](./copysweep.md) script page for implementation
example.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addsweep ](./addsweep.md) , [ deletesweep ](./deletesweep.md) ,
[ copysweep ](./copysweep.md) , [ insertsweep ](./insertsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md)
