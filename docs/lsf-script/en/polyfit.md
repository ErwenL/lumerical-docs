# polyfit

Calculates a polynomial fit based on linear regression. The data can be complex. 

**Syntax** |  **Description**  
---|---  
p = polyfit(x, y, N);  |  Returns the coefficients for a polynomial p(x) of degree N that is the best fit for the data in y.  \\( p(x)=p_1 + p_2x^1+p_3x^2+...+p_Nx^{N-1}+p_{N+1}x^N \\)  The length of the coefficients is N+1.   
  
**Example**

In this example random noise is added to a smooth function. A polynomial fit of the noisy data allows to recover the original function approximately. 
    
    
    clear;
    x = linspace(0,10,100);
    noise_amp = 200;
    y_original = 3.2 + 2i*x + 4.5*x^2 - 0.04*x^3;
    y_noise = y_original + noise_amp*(randmatrix(length(x))-0.5);
    fit = polyfit(x,y_noise,3);
    y_fit = fit(1) + fit(2)*x + fit(3)*x^2 + fit(4)*x^3;
    plot(x,abs(y_original),abs(y_noise),abs(y_fit));
    legend("y_original","y_noise","y_fit");
    ?fit;
    result: 
    -20.3301+1.67422e-013i # fit(1)
    19.7752+2i  # fit(2)
    -0.477739+4.58522e-014i # fit(3) 
    0.304786-4.35069e-015i # fit(4)

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ spline ](/hc/en-us/articles/360034405794-spline)
