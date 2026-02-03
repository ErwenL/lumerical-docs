# chebpol1

Returns the first derivative of the Chebyshev polynomials of the first kind. 

**Syntax** |  **Description**  
---|---  
chebpol1(N,xi,xmin,xmax)  |  This command generates a matrix containing the Chebyshev polynomials of the first kind of orders zero to N-1 evaluated at the xi points.   
  
**Example**

This example uses chebpol1 to calculate the first derivative of a function f sampled on a Chebishev grid. 
    
    
    clear;
    closeall;
    # Sample function on Chebyshev grid 
    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); # function and
    fp = -2.0*pi*sin(2*pi*x)+1i*2.0*pi*cos(2.0*pi*x); # its derivative
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    # Function derivative from Chebyshev transform
    dchtf = dcht(f);
    Txp = chebpol1(length(f),xi,xmin,xmax);
    fip = mult(Txp,dchtf);
    plot(xi,fip,"x","f'(x)","Function Derivative");
    holdon;
    plot(x,fp,"x","f'(x)","Function Derivative","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",8);
    setplot("y1 min",-8);
    setplot("y2 max",8);
    setplot("y2 min",-8);

**See Also**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926853-chebpol1) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol ](/hc/en-us/articles/360034926833-chebpol)
