# adddgtdmesh

Adds a [mesh constraint (override region)](https://optics.ansys.com/hc/en-us/articles/360034397994) to a 'DGTD' simulation. A DGTD solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
adddgtdmesh; |  Adds a mesh constraint to the 'DGTD' simulation environment. This function does not return any data.  
  
**Example 1**

The following script commands will add a mesh constraint to the DGTD solver already present in the objects tree and print the name of all of its properties.
    
    
    adddgtdmesh;
    ?set;

**Example 2**

The following script commands will add a mesh constraint to the DGTD solver region in Finite Element IDE, name it, assign it to a specific surface between two domains, and set the maximum edge length for any element on the surface.
    
    
    adddgtdsolver;
    adddgtdmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**See Also**

[ adddgtdsolver ](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
