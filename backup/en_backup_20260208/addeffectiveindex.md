# addeffectiveindex

Adds an [effective index monitor](/hc/en-us/articles/360034396454) to the simulation environment. This command requires the presence of an active varFDTD solver region.

**Syntax** |  **Description**  
---|---  
addeffectiveindex; |  Adds an effective index monitor to the varFDTD solver region. This function does not return any data.  
addeffectiveindex(struct_data); |  Adds an effective index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add an effective index monitor to the simulation region and set its dimension.
    
    
    addeffectiveindex;
    set("name","neff");
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set)
