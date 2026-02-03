# removesweepresult

Removes a result from a sweep/optimization/Monte Carlo item.

**Syntax** |  **Description**  
---|---  
removesweepresult("name", "result_name"); |  Removes a result from a sweep/optimization/Monte Carlo item. "name" is the absolute name of an analysis item.  
  
**Example**

This example shows how to remove a result from a sweep. Please download the example file from the [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files.
    
    
    removesweepresult("thickness_sweep", "T");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034404254-addsphere) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
