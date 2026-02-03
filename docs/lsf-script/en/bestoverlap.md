# bestoverlap

Finds the mode with highest (best) overlap between the specified D-CARD and the currently calculated modes in the mode list. Returns the name of the mode with the best overlap. This function is used for tracking the desired mode during parameter sweeps using the FDE solver. 

See the [ overlap ](/hc/en-us/articles/360034405254-overlap) function for more details about overlap and coupling calculations. 

**Syntax** |  **Description**  
---|---  
out = bestoverlap("test_mode");  |  Calculates the best overlap. 

  * out: a string containing the name of the mode with the best overlap 
  * test_mode: a string containing the name of a D-CARD mode 

  
  
**Examples**

This example will calculate which of the current modes have the best overlap with the D-CARD named "test_mode". The effective index of the best mode is then returned. 
    
    
    mode_name = bestoverlap("test_mode");  
    neff = getdata(mode_name,"neff");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ bestoverlap2 ](/hc/en-us/articles/360034925193-bestoverlap2) , [ Polarization converter example ](**%20to%20be%20defined%20**)
