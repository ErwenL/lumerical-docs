# partitionvolume

Enters into the partition volume mode.

**Syntax** |  **Description**  
---|---  
partitionvolume; |  Enters into the partition volume mode  
  
**Example**

Create a new simulation in CHARGE, HEAT, FEEM, or DGTD and switch to partition mode.
    
    
    newproject;  # create a new simulation file
    adddgtdsolver;    # add the DGTD solver
    partitionvolume;      # go to the partition volume mode

**See Also**

[ run ](/hc/en-us/articles/360034931333-run) , [ runanalysis](/hc/en-us/articles/360034409874-runanalysis), [mesh](/hc/en-us/articles/360034410654),
