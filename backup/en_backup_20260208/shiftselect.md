# shiftselect

Same as select, but does not unselect other currently selected objects. Note that only objects from the same "group" can be selected simultaneously. 

**Syntax** |  **Description**  
---|---  
shiftselect("name");  |  The same as select("name"), but does not unselect currently selected objects. Can be used to select multiple objects.  This function does not return any data.   
shiftselect("group name::name");  |  The same as select("groupname::name"), but does not unselect currently selected objects.   
  
**Example**

Add two objects and then select both and shift them the same amount. 
    
    
    addrect;
    set("name","substrate");
    addring;# ring is selected automatically
    shiftselect("substrate");# select both objects
    move(0, 1e-6,0); # both will shift 1e-6 in y;

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ groupscope ](/hc/en-us/articles/360034928553-groupscope)
