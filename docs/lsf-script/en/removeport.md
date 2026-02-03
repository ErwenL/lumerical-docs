# removeport

Removes a port from a compound/script element (Note that this command does not apply for primitive elements). 

**Syntax** |  **Description**  
---|---  
removeport("element", "port");  |  Removes "port" from "element".  Returns 1 if the port is successfully removed, 0 otherwise.   
  
**Example**

Open this example file  compound_element.icp  from [ Compound Elements ](**%20to%20be%20defined%20**) and input the following script 
    
    
    disconnect("Optical Network Analyzer","input 1","Compound Element","port 2");
    disconnect("Optical Network Analyzer","output","Compound Element","port 1");
    removeport("Compound Element","port 1"); #delete the port
    addport("Compound Element","port 1","input","optical Signal"); #add port

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addport ](/hc/en-us/articles/360034408934-addport)
