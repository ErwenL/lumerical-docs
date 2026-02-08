# getperiodicity

Returns the periodicity vector(s) associated with the active periodic boundary conditions in the specified solver. 

**Syntax** |  **Description**  
---|---  
out = getperiodicity("solvername");  |  Returns the periodicity vector(s) of the system based on the active periodic boundary conditions in the named solver. The output is a [3XN] matrix where N is the number of dimensions that have active periodic boundary conditions (typically one or two).   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
solvername  |  required  |  |  string  |  Name of the solver from which to extract the periodicity vector(s).   
  
**Example**

This example retrieves the periodicity vectors from a DGTD simulation with periodic boundary conditions. 
    
    
    period = getperiodicity("DGTD"); 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
