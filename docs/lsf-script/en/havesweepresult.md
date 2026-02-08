# havesweepresult

Checks whether a parameter parameter sweep/optimization/Monte Carlo/S-parameter sweep
has results. Similar to haveresult .

| **Syntax**                       | **Description**                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| ?havesweepresult;                | Returns 1 if any sweeps or optimizations, Monte Carlo analysis, or S-parameter sweeps have results. Returns 0 if data is not available. |
| ?havesweepresult("name");        | Returns 1 if the specified sweep, optimization, Monte Carlo, or S-parameter sweep has results.                                          |
| ?havesweepresult("name","data"); | Returns 1 if the sweep, optimization, Monte Carlo, or S-parameter sweep named "name" has the specified result "data".                   |

**Examples**

The following example shows the output of getsweepresult and havesweepdata . Please
download the example file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
?getsweepresult;
?havesweepresult("thickness_optimization","fom trend");
> thickness_sweep
> thickness_optimization
> result: 
1   
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ runsweep ](./runsweep.md) , [ getsweepresult ](./getsweepresult.md) ,
[ getresult ](./getresult.md) , [ haveresult ](./haveresult.md)
