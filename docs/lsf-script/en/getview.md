# getview

This command allows the viewing properties of the Layout Editor to be retrieved. 

**Syntax** |  **Description**  
---|---  
outstring = getview;  |  Returns a list of the view properties that can be set. The command 
    
    
    ?getview;

will return 
    
    
    extent, zoom, theta, phi  
  
out = getview("property");  |  Returns the current value of any of the view properties. For example, 
    
    
    zoom_level = getview("zoom");

will return the current zoom setting of the perspective view relative to the default level.   
  
Note:  The "extent" and "zoom" options for this command are not available in Finite Element IDE.   
---  
  
**Example**

The properties that can be obtained with getview are described in [ setview ](/hc/en-us/articles/360034929173-setview) . 
    
    
    ?getview;
    extent, zoom, theta, phi

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ setview ](/hc/en-us/articles/360034929173-setview) , [ orbit ](/hc/en-us/articles/360034929193-orbit) , [ redraw ](/hc/en-us/articles/360034929133-redraw)
