# addpml

Adds a PML (perfectly matched layer) boundary condition object to the DGTD or FEEM solver in Finite Element IDE. At least, one of these solvers should be present in the Objects Tree for this command to work.

**Syntax** |  **Description**  
---|---  
addpml; |  Adds a PML boundary condition to the DGTD or FEEM solver. Use only when there is a single solver in the Object Tree. This function does not return any data.  
addpml("DGTD"); addpml("FEEM"); |  When there are both DGTD and FEEM in the Object Tree, you need to specify the solver.  
  
**Example 1:**

The following script commands will add a PML boundary condition to the 'DGTD' solver already present in the object tree and print all available properties of the boundary condition.
    
    
    addpml;
    ?set;

NOTE: When there are both DGTD and FEEM solvers in the Object Tree, running the script without any "solver" argument will produce the following error:  
---  
  
**Example 2**

The following script commands will add a PML boundary condition to the 'DGTD' solver, name it, and set the values for sigma and alpha.
    
    
    adddgtdsolver;
    addpml({"name":"simple_pml", "sigma":5});

NOTE:  The PML boundary condition automatically gets applied to the shell regions in the corresponding simulation region.  
---  
  
**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addpmc ](/hc/en-us/articles/360034924913-addpmc) , [ addpec ](/hc/en-us/articles/360034924893-addpec) , [ addperiodic ](/hc/en-us/articles/360034404934-addperiodic) , [ addabsorbing ](/hc/en-us/articles/360034924873-addabsorbing)
