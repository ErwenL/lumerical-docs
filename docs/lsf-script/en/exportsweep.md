# exportsweep

Exports S-parameter results from an S-parameter sweep task to a .dat file which can be
loaded by the [Optical N-Port S-parameter](**%20to%20be%20defined%20**) element in
INTERCONNECT.

| **Syntax**                                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exportsweep("sweep_name","filename","format"); | Exports S-parameter results from the specified S-parameter sweep task to a .dat file with specified file name in the current working directory. The "format" can be either "lumerical" or "touchstone" formats, and if not specified the "lumerical" format will be used. The "touchstone" format will be format v1.1. If the maximum passivity over the frequency range is larger than 1.03 or the maximum reciprocity error over the frequency range exceeds 0.03, a warning message will appear in the script prompt when you export the data. If a file of the same name already exists, the existing file will be overwritten. This function does not return any data. |

Note that Touchstone format v1.1 doesn't handle different modes, so the number of
"ports" is really the number of effective ports (port/mode combinations).

**Example**

The following code can be used to export S-parameter data to a Touchstone file called
s_params.s4p.

```
exportsweep("s-parameter sweep","s_params.s4p", "touchstone"); 
```

**See Also**

[addsweep](./addsweep.md), [runsweep](./runsweep.md),
[getsweepresult](./getsweepresult.md),
[S-parameter matrix sweep](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep)
