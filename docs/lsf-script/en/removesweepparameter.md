# removesweepparameter

Removes a parameter from a parameter sweep/optimization/Monte Carlo/S-parameter sweep item.

**Syntax** |  **Description**  
---|---  
removesweepparameter("name", "parameter_name"); |  Removes a parameter from a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "parameter_name" is the parameter name.  
  
**Examples**

This example shows how to remove a parameter from a sweep. Please download the example file from the [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files.
    
    
    removesweepparameter("thickness_sweep", "thickness");

This example shows how to remove the second row from the s-matrix mapping table in an S-parameter matrix sweep.
    
    
    removesweepparameter("s-parameter sweep",2);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034404254-addsphere) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
