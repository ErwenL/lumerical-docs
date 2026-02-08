# setactivesolver

Sets the specified solver as the active solver. For example, this can be used to toggle between the FDE, varFDTD, and EME simulations in MODE. 

**Syntax** |  **Description**  
---|---  
?setactivesolver;  |  Lists all the possible solver choices   
setactivesolver('solver_name');  |  Set the solver with the specified name as the active solver.   
  
**Example**

If the solver is not set, this command will add it. 
    
    
    setactivesolver("EME");
    ?getactivesolver;
    EME

When "EME" solver is already added, this command will set it as active; if it is not added yet, this command will add this solver and set it as active. 

**See Also**

[ getactivesolver ](/hc/en-us/articles/360034929333-getactivesolver)
