# unselectall

Unselects all objects and groups. This is the counter operation of [ selectall ](/hc/en-us/articles/360034408354-selectall) . 

**Syntax** |  **Description**  
---|---  
unselectall;  |  Unselects all objects and groups.  This function does not return any data.   
  
**Example**

The following script add two objects, select them and assign their x position. Unselect them for other modifications . 
    
    
    addrect;
    set("name","A1");
    addring;
    set("name","ring");
    selectall;
    set("x",-1e-6);
    unselectall;

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ selectall ](/hc/en-us/articles/360034408354-selectall)
