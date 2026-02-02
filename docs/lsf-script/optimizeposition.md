# optimizeposition

The optimizeposition command calculates the x shift, y shift, and z shift resulting in maximum overlap between the specified mode and d-card when using the FDE solver. 

The x shift, y shift, and z shift correspond to the offset in the d-card profile in x, y, and z. 

This function also populates the overlap and power coupling as well as the x shift, y shift, and z shift positions in the Overlap analysis tab of the Eigensolver Analysis window, similarly to when you click on the "Optimize position" button in the GUI. 

See the [ overlap ](/hc/en-us/articles/360034405254-overlap) function for more details about overlap and coupling calculations. 

**Syntax** |  **Description**  
---|---  
out = optimizeposition(mode number, d-card number);  | 

  * mode number: the mode number in the mode list 
  * d-card number: the number of the d-card in the deck 

Note that the "shift d-card center" option must be selected in order to use this function.   
  
**Examples**

This example shows how to use the optimizeposition command to calculate the x shift, y shift, and z shift between a specified mode and d-card resulting in maximum overlap, print out the shift values and the optimal overlap and power coupling with the applied shift. 
    
    
    setanalysis("shift d-card center",1);  
    shift = optimizeposition(4,1); # find x, y, z shift resulting in optimal overlap between  
                                   # the 4th mode in the mode list and the 1st mode in the deck  
    
    ?"x shift:"+num2str(shift(1));  
    ?"y shift:"+num2str(shift(2));  
    ?"z shift:"+num2str(shift(3));  
    
    out = overlap("mode4","global_mode1",shift(1),shift(2),shift(3));  
    ?"maximum overlap:"+num2str(out(1));  
    ?"maximum power coupling:"+num2str(out(2));

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis)
