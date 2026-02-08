# bestoverlap

Finds the mode with highest (best) overlap between the specified D-CARD and the
currently calculated modes in the mode list. Returns the name of the mode with the best
overlap. This function is used for tracking the desired mode during parameter sweeps
using the FDE solver.

See the [ overlap ](./overlap.md) function for more details about overlap and coupling
calculations.

| **Syntax**                      | **Description**              |
| ------------------------------- | ---------------------------- |
| out = bestoverlap("test_mode"); | Calculates the best overlap. |

- out: a string containing the name of the mode with the best overlap
- test_mode: a string containing the name of a D-CARD mode

**Examples**

This example will calculate which of the current modes have the best overlap with the
D-CARD named "test_mode". The effective index of the best mode is then returned.

```
mode_name = bestoverlap("test_mode");  
neff = getdata(mode_name,"neff");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ findmodes ](./findmodes.md) , [ coupling ](./coupling.md) , [ overlap ](./overlap.md)
, [ propagate ](./propagate.md) , [ expand ](./expand.md) , [ expand2 ](./expand2.md) ,
[ bestoverlap2 ](./bestoverlap2.md) ,
[ Polarization converter example ](**%20to%20be%20defined%20**)
