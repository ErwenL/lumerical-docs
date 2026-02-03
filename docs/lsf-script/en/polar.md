# polar

Creates polar plots. All data sets must be sampled on the same array of angle values. 

See polar2 for data sets that are sampled on different arrays of theta values. 

**Syntax** |  **Description**  
---|---  
out = polar(theta,rho)  |  Creates a polar coordinate plot of the angle theta versus the radius rho. theta is the angle from the x-axis to the radius vector specified in radians; rho is the length of the radius vector.  Theta and rho can be vectors of the same length, or if the length of theta is n, then rho can be a nxm matrix, which corresponds to m sets of rho values.  The figure number is returned.   
polar(theta,rho1,rho2,rho3)  |  Creates a polar plot with three curves. theta, rho1, rho2, rho3 must be of the same length. The figure number is returned.   
polar(theta,rho,"x label", "y label", "title")  |  Creates a polar plot with axis labels and a title. The figure number is returned.   
polar(theta,rho,"x label", "y label", "title", "options");  |  Creates a polar plot with desired options. Options can be be 

  * greyscale 
  * polar (use with plot command to generate the same plot as the polar script command) 
  * any comma separated list of the above 

Returns the figure number.   
  
**Example**

Create a simple polar plot. 
    
    
    theta = linspace(0,2*pi,100);
    r = cos(theta);
    polar(theta,r);

The following figure shows the output of the the example code. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ polar2 ](/hc/en-us/articles/360034931173-polar2) , [ legend ](/hc/en-us/articles/360034931233-legend) , [ image ](/hc/en-us/articles/360034931253-image) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ setplot ](/hc/en-us/articles/360034931293-setplot) , [ exportfigure ](/hc/en-us/articles/360034410574-exportfigure) , [ polarimage ](/hc/en-us/articles/360034931193-polarimage) , [ plot ](/hc/en-us/articles/360034410474-plot)
