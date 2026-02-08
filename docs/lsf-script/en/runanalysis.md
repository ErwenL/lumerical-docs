# runanalysis

Runs the analysis script in analysis objects.

Note: Scripts that already have data are not re-run; to re-run a script, first clear
data using clearanalysis.

| **Syntax**                 | **Description**                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| runanalysis;               | Runs the analysis scripts in all analysis objects in the simulation file. This function does not return any data. |
| runanalysis("group name"); | Runs the analysis script in the analysis object named "group name". This function does not return any data.       |

**See Also**

[run](./run.md), [getdata](./getdata.md), [getresult](./getresult.md),
[havedata](./havedata.md), [clearanalysis](./clearanalysis.md),
[runsetup](./runsetup.md)
