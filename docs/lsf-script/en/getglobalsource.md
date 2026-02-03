# getglobalsource

Sets global monitor properties. This command will return an error in analysis mode. 

**Syntax** |  **Description**  
---|---  
getglobalsource;  |  Returns a list of the global source properties   
getglobalsource("property");  |  Returns the value of the requested property.   
  
**Example**

Set the global start wavelength to 400nm, then confirm value was set properly. 
    
    
    setglobalsource("wavelength start",400e-9);
    ?getglobalsource("wavelength start");
    result: 
    4e-007 

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ getglobalmonitor ](/hc/en-us/articles/360034928933-getglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource)
