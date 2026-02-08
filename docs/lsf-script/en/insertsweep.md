# insertsweep

Inserts a sweep/optimization/Monte Carlo item as a parent to an existing analysis item.
The existing item becomes a child of the newly inserted sweep.

| **Syntax**           | **Description**                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| insertsweep("name"); | Inserts a sweep/optimization/Monte Carlo item as a child to a parent analysis item. "name" is the absolute name of the existing analysis item. |

**Example**

```
addsweep(0);
insertsweep("sweep");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ deletesweep ](./deletesweep.md) , [ copysweep ](./copysweep.md) ,
[ pastesweep ](./pastesweep.md) , [ addsweep ](./addsweep.md) ,
[ getsweep ](./getsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md)
