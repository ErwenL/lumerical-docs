# findmodes

Calculates the modes supported by the structure using the current calculation settings. This function is the script equivalent to the "Calculate Modes" button. Each mode will be saved as a D-CARD named "modeX", where X is the xth mode found. The D-CARD saves data such as effective index and mode profile. 

**Syntax** |  **Description**  
---|---  
n=findmodes;  |  n will be equal to the number of modes found.   
  
**Example**

To perform a frequency sweep on the first mode and plot the dispersion: 
    
    
    switchtolayout;  
    
    findmodes;  
    selectmode(1);  
    setanalysis("track selected mode",1);  
    setanalysis("detailed dispersion calculation",1);  
    
    frequencysweep;  
    D=getdata("frequencysweep","D");  
    f=getdata("frequencysweep","f_D");  
    
    plot(c/f*1e6,D*1e6,"Wavelength (um)", "Dispersion (ps/nm/km)");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ selectmode ](/hc/en-us/articles/360034405234-selectmode) , [ frequencysweep ](/hc/en-us/articles/360034925153-frequencysweep) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate)
