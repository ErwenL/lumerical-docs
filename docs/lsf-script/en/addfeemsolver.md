# addfeemsolver

Adds a [FEEM solver region](/hc/en-us/articles/360034918393) to the simulation environment.

**Syntax** |  **Description**  
---|---  
addfeemsolver; |  Adds a FEEM solver region to the simulation environment. This function does not return any data.  
addfeemsolver(struct_data);  |  Adds a FEEM solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example 1**

The following script commands will add a FEEM solver to the objects tree and print the name of all of its properties.
    
    
    addfeemsolver;
    ?set;

**Example 2**

The following script command will add a FEEM solver region and assign it to a simulation region.
    
    
    addfeemsolver;
    set("solver geometry","simulation region 1");

**See Also**

[ addfeemmesh ](/hc/en-us/articles/360034405014-addfeemmesh)
