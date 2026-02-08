# bestoverlap2

This function is similar to [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) but it uses [ expand2 ](/hc/en-us/articles/360034406414-expand2) to get the necessary parameters, which can be useful when an evanescent mode is involved. 

**Syntax** |  **Description**  
---|---  
out = bestoverlap2("test_mode");  |  Calculates the best overlap. 

  * out: a string containing the name of the mode with the best overlap 
  * test_mode: a string containing the name of a D-CARD mode 

  
out = bestoverlap2("test_mode", x,y,z);  |  Calculates the best overlap. 

  * out: a string containing the name of the mode with the best overlap 
  * test_mode: a string containing the name of a D-CARD mode 

Mode alignment can be adjusted before best overlap is calculated. 

  * x offset 
  * y offset 
  * z offset 

The offset is applied to the test_mode.   
  
**Examples**

This example will calculate which of the current modes have the best overlap with the D-CARD named "test_mode". The effective index of the best mode is then returned. 
    
    
    mode_name = bestoverlap2("test_mode");  
    neff = getdata(mode_name,"neff");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ Polarization converter example ](**%20to%20be%20defined%20**) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap)
