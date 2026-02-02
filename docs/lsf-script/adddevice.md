# adddevice

Adds a CHARGE solver region to the simulation environment. 

Note:  The 'adddevice' command is deprecated and will be removed in future releases. Please refer to [ addchargesolver ](/hc/en-us/articles/360034924473-addchargesolver) as a replacement.   
---  
**Syntax** |  **Description**  
---|---  
adddevice;  |  Add a CHARGE solver region to the simulation environment.  This function does not return any data.   
  
**Example**

The following script command will add a 2D y-normal CHARGE solver region, set its dimension, and run the simulation. The script assumes that the simulation environment already has the geometry and boundary conditions set up. 
    
    
    adddevice;
    set("solver geometry",1);  #  2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ run ](/hc/en-us/articles/360034931333-run)
