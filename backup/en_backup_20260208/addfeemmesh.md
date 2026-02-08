# addfeemmesh

Adds a [mesh constraint (override region)](/hc/en-us/articles/360034397994) to a 'FEEM' simulation.. A FEEM solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addfeemmesh; |  Adds a mesh constraint to the 'FEEM' simulation environment. This function does not return any data.  
addfeemmesh(struct_data); |  Adds a FEEM mesh constraint and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example 1**

The following script commands will add a mesh constraint to the FEEM solver already present in the objects tree and print the name of all of its properties.
    
    
    addfeemmesh;
    ?set;

**Example 2**

The following script commands will add a mesh constraint to the FEEM solver region in Finite Element IDE, name it, assign it to a specific surface between two domains, and set the maximum edge length for any element on the surface.
    
    
    addfeemsolver;
    addfeemmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**See Also**

[ addfeemsolver ](/hc/en-us/articles/360034405014-addfeemmesh)
