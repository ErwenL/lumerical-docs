# addport (INTERCONNECT)

Adds a port to a compound/script element (Note that this command does not apply for primitive elements). This topic addresses the  addport  command in INTERCONNECT - for information about the FDTD command, see [ addport (FDTD) ](/hc/en-us/articles/360034924793-addport) . 

**Syntax** |  **Description**  
---|---  
addport("element", "port", "type", "data", "position", "location");  |  Adds a new port to the element with the specified properties.  Returns the name of the port that is created.   
**Property** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
element  |  required  |  |  string  |  Name of the element to add a port to.   
port  |  required  |  |  string  |  Name of the port to add. The named will be modified if there is already a port of the same name.   
type  |  required  |  |  string  |  The type of port to add. The options are: Bidirectional, Input, Output, Analyzer Input   
data  |  required  |  |  string  |  The type of data for the port. The options are: Variant, Optical Signal, Electrical Signal, Digital Signal   
position  |  optional  |  |  string  |  Position of the port. The options are: Top, Bottom, Left, Right   
location  |  optional  |  |  number  |  location of the port, within the range [0, 1].   
  
**Example**

Open this example file  compound_element.icp  from [ Compound Elements ](**%20to%20be%20defined%20**) and input the following script 
    
    
    disconnect("Optical Network Analyzer","input 1","Compound Element","port 2");
    disconnect("Optical Network Analyzer","output","Compound Element","port 1");
    removeport("Compound Element","port 1"); #delete the port
    addport("Compound Element","port 1","input","optical Signal"); #add port

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ removeport ](/hc/en-us/articles/360034929293-removeport)
