# loadelement

Loads an element from a file created using the [ saveelement ](/hc/en-us/articles/360034927493-saveelement) command in the current working directory. The element will be placed in the current schematic editor window. 

**Syntax** |  **Description**  
---|---  
loadelement ("name");  |  Loads an element from the file in the current working directory with extension ICE.   
  
Example 
    
    
    #adds an element star coupler and saves it to an .ice file in the current working directory
    addelement("Star Coupler");
    saveelement("STAR_1");
    #loads the star coupler element "STAR_1.ice" to the schematic editor
    loadelement("STAR_1.ice");
    #change element position in the schematic editor
    set("x position", -200)

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ library ](/hc/en-us/articles/360034927473-library) , [ addtolibrary ](/hc/en-us/articles/360034407234-addtolibrary) , [ probe ](/hc/en-us/articles/360034407294-probe) , [ saveelement ](/hc/en-us/articles/360034927493-saveelement)
