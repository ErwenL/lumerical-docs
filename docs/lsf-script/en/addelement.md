# addelement

Adds an element from the INTERCONNECT element library to the simulation environment. 

**Syntax** |  **Description**  
---|---  
addelement("element");  |  Adds an element from the element library.  If no element name is given, this command will add a compound element by default.  This function does not return any data.   
  
**Example**

The following script commands will add a waveguide coupler to the simulation environment and edit its properties. 
    
    
    addelement("Waveguide Coupler");
    eleName = "coupler_1";
    set("name", eleName);
    set("x position", 0); 
    set("y position", 0);
    set("coupling coefficient 1", 0.3);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set)
