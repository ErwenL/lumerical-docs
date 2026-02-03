# getactivesolver

Gets the active solver. This could be the FDE, varFDTD, or EME solvers in MODE. 

**Syntax** |  **Description**  
---|---  
?getactivesolver;  |  List the active solver.   
  
**Example**

When "EME" solver is already added, the following script will give the result: 
    
    
    setactivesolver("EME");
    ?getactivesolver;
    EME

**See Also**

[ setactivesolver ](/hc/en-us/articles/360034409014-setactivesolver)
