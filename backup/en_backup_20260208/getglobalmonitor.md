# getglobalmonitor

Sets global monitor properties. This command will return an error in analysis mode. 

**Syntax** |  **Description**  
---|---  
?getglobalmonitor;  |  Returns a list of the global monitor properties   
?getglobalmonitor("property");  |  Returns the value of the requested property.   
  
**Example**

Set the global number of monitored frequency points to 11, then confirm value was set properly. 
    
    
    setglobalmonitor("frequency points",11);
    ?getglobalmonitor("frequency points");
    result: 
    11  

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource) , [ getglobalsource ](/hc/en-us/articles/360034928953-getglobalsource)
