# addmode

Adds a mode source to the simulation environment for FDTD. For MODE, adds an eigenmode (FDE) solver region to the simulation environment.

Note:  The 'addmode' command is deprecated in MODE and will be removed in future releases. Please refer to [ addfde ](/hc/en-us/articles/360034404294-addfde) as a replacement.  
---  
**Syntax** |  **Description**  
---|---  
addmode; |  For FDTD: Add a mode source to the simulation environment. This function does not return any data.  
addmode; |  For MODE: Add an eigenmode solver to the simulation environment.  
addmode(struct_data); |  Adds a mode source (when used in FDTD) or an eigenmode solver (when used in MODE) and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a mode source in FDTD and set its dimension and injection axis.
    
    
    addmode;
    set("injection axis","x");
    set("x",0);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);

The following script commands will add an eigenmode (FDE) solver region in MODE on the XY plane and calculate the eigen modes.
    
    
    addmode;
    set("solver type",3);
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    findmodes;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes)
