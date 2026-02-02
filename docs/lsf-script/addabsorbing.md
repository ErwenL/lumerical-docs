# addabsorbing

Adds an absorbing boundary condition to the 'DGTD' solver. A DGTD solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addabsorbing; |  Adds a PML boundary condition to the 'DGTD' solver. This function does not return any data.  
  
**Example 1**

The following script commands will add an absorbing boundary condition to the 'DGTD' solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addabsorbing;
    ?set;

**Example 2**

The following script commands will add an absorbing boundary condition to the 'DGTD' solver, name it, and assign it to the -z and +z boundaries of the simulation region.
    
    
    addabsorbing; 
    set("name","absorbing_z");
    set("surface type","simulation region");
    set("z min",1);
    set("z max",1);

**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addpml ](/hc/en-us/articles/360034924873-addabsorbing) , [ addpmc ](/hc/en-us/articles/360034924913-addpmc) , [ addpec ](/hc/en-us/articles/360034924893-addpec) , [ addperiodic ](/hc/en-us/articles/360034404934-addperiodic)
