# addfde

Adds a [Finite Difference Eigenmode (FDE) solver region object](/hc/en-us/articles/360034916973) to the MODE simulation environment.

**Syntax** |  **Description**  
---|---  
addfde; |  Adds an FDE solver region to the simulation environment. This function does not return any data.  
addfde(struct_data); |  Adds an FDE solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add an FDE solver region on the XY plane and calculate the eigen modes.
    
    
    addfde;
    set("solver type",3);  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);
    findmodes;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ addvarfdtd ](/hc/en-us/articles/360034924193-addvarfdtd) , [ addeme ](/hc/en-us/articles/360034404314-addeme)
