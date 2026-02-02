# addvarfdtd

Adds a 2.5D varFDTD solver region to the MODE simulation environment.

**Syntax** |  **Description**  
---|---  
addvarfdtd; |  Adds a 2.5D varFDTD simulation region. This function does not return any data.  
addvarfdtd(struct_data); |  Adds a 2.5D varFDTD simulation region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a 2.5D varFDTD solver region to the MODE simulation environment, set its dimension and simulation time, and run the simulation.
    
    
    addvarfdtd;  
    
    set("x",0);  
    set("x span",10e-6);  
    set("y",0);  
    set("y span",10e-6);  
    set("z",0);  
    set("z span",1e-6);  
    set("simulation time",5000e-15);  # 5000 fs  
    
    run;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ run ](/hc/en-us/articles/360034931333-run) , [ addeme ](/hc/en-us/articles/360034404314-addeme) , [ addfde ](/hc/en-us/articles/360034404294-addfde)
