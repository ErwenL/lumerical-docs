# redrawmode

This command can be used to determine the current status of automatic redrawing. It can also be used to set the current status of automatic redrawing. The graphics will be redrawn after any script command that may change the properties of a graphical object. 

**Syntax** |  **Description**  
---|---  
out = redrawmode;  |  The value of out indicates if automatic redrawing is off or on 

  * out=1: automatic redrawing is on 
  * out=0: automatic redrawing is off 

  
out = redrawmode(in);  |  Set the automatic redrawing off or on. To turn it on, use in=1. To turn it off, use in=0. The value of out is set after executing the command so that out=in once this command has been executed.   
  
**Example**

This example uses redrawmode to turn automatic redrawing off, then restore automatic redrawing to the state it had before executing this script. 
    
    
    redraw_state = redrawmode;
    redrawoff;
    for(i=1:60) {
      addcircle;
      set("x",i*1e-6);
    }
    redrawmode(redraw_state);

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ redraw ](/hc/en-us/articles/360034929133-redraw) , [ redrawoff ](/hc/en-us/articles/360034408814-redrawoff)
