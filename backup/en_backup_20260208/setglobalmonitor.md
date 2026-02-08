# setglobalmonitor

Sets global monitor properties. This command will return an error in analysis mode. 

**Syntax** |  **Description**  
---|---  
?setglobalmonitor;  |  Returns a list of the global monitor properties   
setglobalmonitor("property",value);  |  Set the global monitor property named "property" to a value.  This function does not return any data.   
  
**Example**

Set the global number of monitored frequency points to 11, then confirm value was set properly. 
    
    
    setglobalmonitor("frequency points",11);
    ?getglobalmonitor("frequency points");
    result: 
    11  

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ getglobalmonitor ](/hc/en-us/articles/360034928933-getglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource) , [ getglobalsource ](/hc/en-us/articles/360034928953-getglobalsource)
