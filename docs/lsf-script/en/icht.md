# icht

Takes the Chebyshev interpolation coefficients and returns the corresponding function samples. 

**Syntax** |  **Description**  
---|---  
out=icht(coeff,option);  |  Returns function samples from Chebyshev interpolation coefficients coeff.  Option:  If option=1 is selected, the vector x will not include the endpoints  If option=2 is selected, the vector x will include the endpoints   
  
**Example**

This example shows how to obtain interpolation coefficients from a sampled function and then calculate back the function samples from the coefficients. 
    
    
    Nc = 15;         # Number of sample points
    xmin = 0;
    xmax = 1;
    x = chpts(xmin,xmax,Nc,1); # Returns Chebyshev roots grid on interval between xmin and xmax
    f = exp(1i*2*pi*x);    # Function sampling using Chebyshev grid
    coeff = dcht(f,1);     # Get interpolation coefficients
    # Calculate the function samples from the coefficients and compare them to the original function samples
    ?icht(coeff,1);
    ?f;     

**See Also**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin)
