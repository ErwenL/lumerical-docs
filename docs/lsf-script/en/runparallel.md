# runparallel

Launch the simulation in parallel mode. Equivalent to run and run(3). When the
simulation finishes, all simulation data will be saved to the current file. This command
has been deprecated. Use run.

| **Syntax**   | **Description**                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| runparallel; | Launch the simulation in parallel mode as defined in the resource manager. This function does not return any data. |

**Example**

```
newproject;
addfdtd;    
adddipole;  
runparallel;      
```

**See Also**

[ run ](./run.md) , [ runanalysis ](./runanalysis.md)
