# checkout

Checks out a licensed feature. 

**Syntax** |  **Description**  
---|---  
checkout(featureID);  |  Checks out and reserve a licensed feature. If the feature cannot be checked out, an error message will be shown in the Script Prompt window. The license will remain be checked out until the application quits.   
  
**Example**
    
    
    checkout("INTERCONNECT_block_mode");
    #If INTERCONNECT_block_mode license does not exist, the following message will be shown
    Error: The license feature 'INTERCONNECT_block_mode' does not exist on ... 

**See Also**

[ run ](/hc/en-us/articles/360034931333-run) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps)
