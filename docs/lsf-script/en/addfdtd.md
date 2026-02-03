# addfdtd

Adds an [FDTD solver region](/hc/en-us/articles/360034382534) to the simulation environment. The extent of the solver region determines the simulated volume/area in FDTD.

**Syntax** |  **Description**  
---|---  
addfdtd; |  Adds an FDTD solver region to the simulation environment. This function does not return any data.  
addfdtd(struct_data); |  Adds an FDTD solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a 3D FDTD solver region, set its dimension, and run the simulation. The script assumes that the simulation environment already has the geometry and sources/monitors set up.
    
    
    addfdtd;
    set("dimension",2);  #  1 = 2D, 2 = 3D
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    run;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ run ](/hc/en-us/articles/360034931333-run)
