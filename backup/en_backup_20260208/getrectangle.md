# getrectangle

Gets the width or height of an element rectangle. 

**Syntax** |  **Description**  
---|---  
out=getrectangle ("element",”w”);  |  Returns the width of an element rectangle.   
out=getrectangle ("element",”h”);  |  Returns the height of an element rectangle.   
  
**Example**

To get the x position of a waveguide element named "Straight Waveguide_1" use the following script 
    
    
    ?getrectangle("Straight Waveguide_1","w") ;
    result: 
    1e-006 

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ setrectangle ](/hc/en-us/articles/360034928833-setrectangle) , [ getposition ](/hc/en-us/articles/360034928853-getposition)
