# addtfsf

Adds a Total Field Scattered Field (TFSF) source to the simulation environment.

**Syntax** |  **Description**  
---|---  
addtfsf; |  Add a total field scattered field source to the simulation environment. This function does not return any data.  
addtfsf(struct_data); |  Adds a total field scattered field source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a plane wave source in the FDTD simulation environment that will propagate in the negative z direction. The script will set the dimension (and position) of the source and will define the frequency range.
    
    
    addtfsf;  
    
    set("injection axis","z");  
    set("direction","backward");  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",3e-6);  
    set("z span",6e-6);  
    set("wavelength start",0.3e-6);  
    set("wavelength stop",1.2e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addgaussian ](/hc/en-us/articles/360034404434-addgaussian)
