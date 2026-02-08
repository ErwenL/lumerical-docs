# havesweepdata

Checks whether a parameter sweep/optimization/Monte Carlo analysis has data. Similar to
the script command havedata .

| **Syntax**                     | **Description**                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| ?havesweepdata;                | Returns 1 if any sweeps, optimizations or Monte Carlo analysis have data. Returns 0 if data is not available.      |
| ?havesweepdata("name");        | Returns 1 if the specified sweep, optimization or Monte Carlo analysis has data.                                   |
| ?havesweepdata("name","data"); | Returns 1 if the specified sweep, optimization or Monte Carlo analysis named "name" has the specified data "data". |

**Examples**

The following example shows the output of getsweepresult and havesweepdata . Please
download the example file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
?getsweepresult;
?havesweepdata("thickness_optimization","fom trend");
> thickness_sweep
> thickness_optimization
> result: 
0    
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ runsweep ](./runsweep.md) , [ getsweepdata ](./getsweepdata.md) ,
[ getdata ](./getdata.md) , [ havedata ](./havedata.md)
