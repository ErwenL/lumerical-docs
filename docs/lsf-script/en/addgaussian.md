# addgaussian

Adds a [Gaussian source](/hc/en-us/articles/360034382854) to the simulation environment.

**Syntax** |  **Description**  
---|---  
addgaussian; |  Adds a Gaussian source to the simulation environment. This function does not return any data.  
addgaussian(struct_data); |  Adds a Gaussian source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a Gaussian source in the simulation environment that will propagate in the negative z direction. The script will set the dimension (and position) of the source and will define the beam waist radius using scalar approximation.
    
    
    addgaussian;
    set("injection axis","z");
    set("direction","backward");
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",10e-6);
    set("use scalar approximation",1);
    set("waist radius w0",0.5e-6);
    set("distance from waist",-5e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addtfsf ](/hc/en-us/articles/360034404454-addtfsf)
