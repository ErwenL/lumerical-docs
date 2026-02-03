# addpmc

Adds a PMC (perfect electrical conductor) boundary condition to the DGTD or FEEM solver in Finite Element IDE. A DGTD or FEEM solver region must be present in the objects tree for this command to work. If both solvers are present then the intended solver's name must be provided as an argument to the script command.

**Syntax** |  **Description**  
---|---  
addpmc; |  Adds a PMC boundary condition to the DGTD or FEEM solver (whichever is present in the objects tree). This function does not return any data.  
addpmc("solver_name"); |  Adds a PMC boundary condition to the desired solver defined by the argument "solver_name". The options are "DGTD" and "FEEM". This function does not return any data.  
  
**Example 1**

The following script commands will add a PMC boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addpmc;
    ?set;

**Example 2**

The following script commands will add a PMC boundary condition to the DGTD solver, name it, and assign it to the -y and +y boundaries of the simulation region.
    
    
    addpmc("DGTD"); 
    set("name","PMC_y");
    set("surface type","simulation region");
    set("y min",1);
    set("y max",1);

**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addpml ](/hc/en-us/articles/360034924913-addpmc) , [ addpec ](/hc/en-us/articles/360034924893-addpec) , [ addperiodic ](/hc/en-us/articles/360034404934-addperiodic) , [ addabsorbing ](/hc/en-us/articles/360034924873-addabsorbing)
