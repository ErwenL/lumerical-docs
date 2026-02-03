# spline

Does a cubic spline interpolation of a data set.

**Syntax** |  **Description**  
---|---  
out = spline(Ex,xold,xnew); |  "not-a-knot" cubic spline interpolation of a 1D function.

  * Ex is an existing data set
  * xold specifies the points where Ex is sampled
  * xnew specifies new points to interpolate the data.

The points in xnew do not have to be within the bounds of xold.  
spline(Ex,xold,xnew,[derivMin; derivMax]); |  "clamped cubic spline" interpolation of a 1D function.

  * Ex is an existing data set
  * xold specifies the points where Ex is sampled
  * xnew specifies new points to interpolate the data.
  * derivMin specifies the 1st-order derivatives at the starting point
  * derivMax specifies the 1st-order derivatives at the ending point

  
[[NOTE:]] The [[spline]] script has been modified in version 2020R2 or later. To recover the result from previous versions, use the "clamped cubic spline" option and define the "derivMin" and "deriveMax" as follows:
    
    
    derivMin = (Ex(2)-Ex(1))/(xold(2)-xold(1));  
    derivMax = (Ex(end)-Ex(end-1))/(xold(end)-xold(end-1));  
  
---  
  
**Example**

Resample Ex at xnew using cubic spline and linear interpolation methods. Note that xnew is outside the bounds of xold.
    
    
    xold=linspace(0,10,7);
    Ex=sin(xold);
    xnew=linspace(-1,9,25); # defining a new x vector
    Exnew=interp(Ex,xold,xnew); # interpolating the new data set
    Exnew2=spline(Ex,xold,xnew); # smoothing
    plotxy(xold,Ex,xnew,Exnew,xnew,Exnew2,"x","y","");
    legend("old data", "interp", "Spline");

The example code will generate the following plots, displaying the difference between the linear and cubic spline interpolation techniques.

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy)
