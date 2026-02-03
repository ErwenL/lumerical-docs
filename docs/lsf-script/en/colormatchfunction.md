# colormatchfunction

Returns the set of color matching functions \\( \overline{x} \\), \\( \overline{y} \\) ,\\( \overline{z} \\) selected by the user. These functions are dimensionless. The available sets are the CIE 1931 and CIE 1964. 

References: 

CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press. 

CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris. 

**Syntax** |  **Description**  
---|---  
?colormatchfunction;  |  Show the list of available color matching functions.   
M = colormatchfunction("functions");  |  Get the desired set of color matching functions from the list of available ones.   
  
**Example**

This example shows how to get the list of available color matching functions and plot them. 
    
    
    ?colormatchfunction; #Show the list of color matching functions
    result:
    CIE 1931
    CIE 1964
    M1 = colormatchfunction("CIE 1931");
    M2 = colormatchfunction("CIE 1964");
    lambda1 = pinch(M1,2,1)*1e9; #Get the wavelength values where the function M1 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar1 = pinch(M1,2,2);
    ybar1 = pinch(M1,2,3);
    zbar1 = pinch(M1,2,4);
    lambda2 = pinch(M2,2,1)*1e9; #Get the wavelength values where the function M2 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar2 = pinch(M2,2,2);
    ybar2 = pinch(M2,2,3);
    zbar2 = pinch(M2,2,4);
    plotxy(lambda1,xbar1,lambda1,ybar1,lambda1,zbar1,lambda2,xbar2,lambda2,ybar2,lambda2,zbar2,"wavelength (nm)","Color matching functions");
    legend("xbar (CIE 1931)","ybar (CIE 1931)","zbar (CIE 1931)","xbar (CIE 1964)","ybar (CIE 1964)","zbar (CIE 1964)");

The following figure shows the output of the example code. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
