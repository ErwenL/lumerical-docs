# adddipole

Adds a [dipole source](/hc/en-us/articles/360034382794) to the simulation environment. In MODE the command requires an active varFDTD solver region in the objects tree.

**Syntax** |  **Description**  
---|---  
adddipole; |  Adds a dipole source to the simulation environment. This function does not return any data.  
adddipole(struct_data); |  Adds a dipole source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a dipole source to the FDTD simulation environment and set its position.
    
    
    adddipole;
    set("x",0);
    set("y",-1e-6);
    set("z",5e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addgaussian ](/hc/en-us/articles/360034404434-addgaussian) , [ addtfsf ](/hc/en-us/articles/360034404454-addtfsf)
