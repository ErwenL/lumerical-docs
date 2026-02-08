# shiftselectpartial

Same as selectpartial, but does not unselect other currently selected objects. 

**Syntax** |  **Description**  
---|---  
shiftselectpartial("partialname");  |  The same as selectpartial("partialname"), but does not unselect currently selected objects. Can be used to select multiple objects.  This function does not return any data.   
shiftselectpartial("partialgroupname::partialname");  |  The same as selectpartial("partialgroupname::partialname"), but does not unselect currently selected objects. Can be used to select multiple objects.   
  
**Example**

Select 2 objects with different partial names. 
    
    
    addrect; 
    set("name","substrate_1");
    addrect; 
    set("name","pattern_1");
    unselectall;
    shiftselectpartial("substrate");
    shiftselectpartial("pattern");

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ groupscope ](/hc/en-us/articles/360034928553-groupscope)
