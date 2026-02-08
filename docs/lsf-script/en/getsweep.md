# getsweep

Gets a property from a parameter sweep/optimization/Monte Carlo/S-parameter sweep item.

| **Syntax**                         | **Description**                                                                                                                                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getsweep("name", "property_name"); | Gets a property from a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "property_name" is the property showed in the edit window. Returns the value of the property. |
| ?getsweep("name");                 | Lists the properties that are available from the analysis item.                                                                                                                                                                        |

**Example**

This example shows how to get a property from a parameter sweep. Please download the
example file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
?getsweep("thickness_sweep", "thickness");
> Struct with fields:
> name
> parameter
> start
> stop
> type
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ deletesweep ](./deletesweep.md) , [ copysweep ](./copysweep.md) ,
[ pastesweep ](./pastesweep.md) , [ addsweep ](./addsweep.md) ,
[ insertsweep ](./insertsweep.md) ,
[setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](./setsetting.md),
[ addsweepparameter ](./addsweepparameter.md) , [ addsweepresult ](./addsweepresult.md)
, [ removesweepparameter ](./removesweepparameter.md) ,
[ removesweepresult ](./removesweepresult.md)
