# addheatmesh

Adds a [mesh constraint (override region)](/hc/en-us/articles/360034397994) to a 'HEAT' simulation. A HEAT solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addheatmesh; |  Adds a mesh constraint to the 'HEAT' simulation environment. This function does not return any data.  
addheatmesh(struct_data); |  Adds a mesh constraint to the 'HEAT' simulation environment and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a mesh constraint to the HEAT solver region in Finite Element IDE, name it, set its dimension, and set the maximum edge length for any element within the volume.
    
    
    addheatsolver;
    addheatmesh;
    set("name","mesh_SCR");
    # set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    # restrict maximum edge length for elements
    set("max edge length",5e-9);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addheatsolver ](/hc/en-us/articles/360034924493-addheatsolver) , [ set ](/hc/en-us/articles/360034928773-set)
