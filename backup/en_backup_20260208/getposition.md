# getposition

Gets the current horizontal or vertical position of an element. 

**Syntax** |  **Description**  
---|---  
out=getposition("element",”x”);  |  Returns the current horizontal position of an element.   
out=getposition("element",”y”);  |  Returns the current vertical position of an element.   
  
**Example**

This example is to get the x position of an element named "Waveguide Coupler_1" 
    
    
    ?getposition("Waveguide Coupler_1","x");
    result: 
    1e-006  

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ setposition ](/hc/en-us/articles/360034408534-setposition) , [ getrectangle ](/hc/en-us/articles/360034408554-getrectangle)
