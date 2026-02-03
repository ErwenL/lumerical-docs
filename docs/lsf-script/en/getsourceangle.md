# getsourceangle

Returns the source angle theta as a function of frequency. Broadband sources inject fields that have a constant in-plane wavevector at all frequencies. This implies injection angle must change as a function of frequency. The in-plane wavevector is chosen such that the incidence angle at the center frequency of the simulation (\\(f_{sim}\\)) will match the source angle theta (\\(\theta_{sim}\\)) specified in the source properties. Higher frequencies will be injected at smaller angles, while lower frequencies will be injected at larger angles. This 'theta vs wavelength' plot in the beam source edit window shows the same function.

$$ \theta(f) = \arcsin\bigg[\frac{sin(\theta_{sim})f_{sim}}{f}\bigg]$$

**Syntax** |  **Description**  
---|---  
theta = getsourceangle( "sourcename", f); |  Returns the source angle theta (degrees) as a function of frequency. f is a vector of frequencies (Hz).  
  
**Example**

This example shows how to get the source injection angle as a function of frequency. The source frequency range is 300-600THz, and the nominal source angle theta is 10 degrees.
    
    
    f_max=600e12;  
    f_min=300e12;  
    f=linspace(f_min,f_max,5);  
    
    ?theta_f=getsourceangle("source1",f);  
    result:   
    15.0981   
    12.0273   
    10   
    8.55978   
    7.48324  

**See Also**

[sourcepower](/hc/en-us/articles/360034925313-sourcepower), [Broadband injection angles](/hc/en-us/articles/360034382894-Plane-waves-Angled-injection), [BFAST](/hc/en-us/articles/360034902273-Source-BFAST)
