# interp

Calculates the linear interpolation of a given data set. The data can be complex. 

**Syntax** |  **Description**  
---|---  
out = interp(Ex, xold, xnew);  |  Does a linear interpolation of a 1D data set. 

  * Ex is existing data 
  * xold specifies the points where Ex is sampled 
  * xnew specifies new point to interpolate the data. 

The xnew does not have to be within the bounds of xold.   
interp(Ex, xold, yold, xnew, ynew);  |  The 2D version of interp.   
interp(Ex, xold, yold, zold, xnew, ynew, znew);  |  The 3D version of interp.   
interp(Ex, xold, yold, zold, told, xnew, ynew, znew, tnew);  |  The 4D version of interp.   
  
**Example**

Resample Ex at xnew using linear interpolation. Note that xnew can be outside the bounds of xold. 
    
    
    xold=linspace(0,10,100);
    Ex=sin(xold);
    xnew=linspace(-1,9,10); # defining a new x vector
    Exnew=interp(Ex,xold,xnew); # interpolating the new data set
    plotxy(xold,Ex,xnew,Exnew,"x","y","");
    legend("old data", "interp");

The example code will generate a plot for two vectors that were sampled at different positions. It shows the data sampled at the old and new positions. Note that the 'interp' data only looks 'bad' because 'xnew' has only 10 points compared to 100 in the original data. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ spline ](/hc/en-us/articles/360034405794-spline) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy)
