# emepropagate

Propagates fields for EME profile monitor and calculates s-matrix and user s-matrix
results, as well as any error diagnostic results when in Analysis mode using EME solver.
This is equivalent to clicking the "eme propagate" button.

| **Syntax**    | **Description**                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| emepropagate; | Propagate fields and s-matrix results. This is equivalent to the "eme propagate" button in the graphical user interface. |

**Examples**

This code will set up the group spans column in the EME analysis window then propagate
using the EME solver.

```
# set group spans to 1 micron  
setemeanalysis("group spans",[1e-6;1e-6;1e-6]);  

# propagate eme  
emepropagate;
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ Spot size converter ](**%20to%20be%20defined%20**) , [ emesweep ](./emesweep.md) ,
[ getemesweep ](./getemesweep.md)
