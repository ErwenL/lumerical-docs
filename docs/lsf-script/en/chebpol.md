# chebpol

Generates the Chebyshev polynomials of the first kind. This command can be used in combination with dcht to calculate the Chebyshev interpolation. Compared to the chebin command, using chebpol for the interpolation offers additional control over the interpolation process as it allows the user to specify the polynomial order. 

**Syntax** |  **Description**  
---|---  
chebpol(N,xi,xmin,xmax)  |  This command generates a matrix containing the Chebyshev polynomials of the first kind of orders zero to N-1 evaluated at the xi points.   
  
**Example**

This example uses chebpol to interpolate function f and compares the results to the original points. 
    
    
    clear;
    closeall;
    # Sample function on Chebyshev grid 
    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); 
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    # Chebyshev interpolation done by hand
    dchtf = dcht(f);
    Tx = chebpol(length(f),xi,xmin,xmax);
    fi = mult(Tx,dchtf);
    plot(xi,fi,"x","f(x)","Function Interpolated by Hand");
    holdon;
    plot(x,f,"x","f(x)","Function Interpolated by Hand","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",1.05);
    setplot("y1 min",-1.05);
    setplot("y2 max",1.05);
    setplot("y2 min",-1.05);

**See Also**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926833-chebpol) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol1 ](/hc/en-us/articles/360034926853-chebpol1)
