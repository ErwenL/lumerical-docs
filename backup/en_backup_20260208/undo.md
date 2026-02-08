# undo

Undos the last command that modified any objects, you can undo the last 5 commands. 

**Syntax** |  **Description**  
---|---  
undo;  |  Undo last modify object command.  This function does not return any data.   
  
**Example**

If you add some objects manually or type in commands in the prompt like this line by line 
    
    
    addplane;
    addrect;
    addring;
    addcircle;
    addpower;
    addfdtd;

then type  undo  5 times or more, it will only delete the last 5 objects.The first added plane wave source is kept. 

If type  redo  5 times or more, it will only recover the last 5 objects. 

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ redo ](/hc/en-us/articles/360034929253-redo) , [ historyon ](/hc/en-us/articles/360034929273-historyon) , [ historyoff ](/hc/en-us/articles/360034408914-historyoff)
