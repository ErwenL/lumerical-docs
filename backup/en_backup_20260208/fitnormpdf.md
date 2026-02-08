# fitnormpdf

Fits any real-valued data, y = f(x), where x is a real valued argument, with the normal (Gaussian) probability density function (PDF) defined as:

$$ f(x)=\frac{A}{\sqrt{2\pi \sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}} $$

where µ is the mean and σ is the standard deviation of the normal distribution and A is a normalization factor.

**Syntax** |  **Description**  
---|---  
p = fitnormpdf(x, y) |  Fits the data, y = f(x), with the normal (Gaussian) probability density function (defined in the equation above) and returns the values for A = p(1), µ = p(2), and σ = p(3).  
p = fitnormpdf(x, y, normalize) |  Fits the data, y = f(x), with the normal (Gaussian) probability density function (defined in the equation above) and returns the values for A = p(1), µ = p(2), and σ = p(3). **Optional argument:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum (A = 1).  
p = fitnormpdf(x, y, normalize, fit_threshold) |  Fits the data, y = f(x), with the normal (Gaussian) probability density function (defined in the equation above) and returns the values for A = p(1), µ = p(2), and σ = p(3). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum (A = 1). fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold.  
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter) |  Fits the data, y = f(x), with the normal (Gaussian) probability density function (defined in the equation above) and returns the values for A = p(1), µ = p(2), and σ = p(3). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum (A = 1). fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold. max_iter = maximum number of iteration during the fit (default = 400). The fitting will stop when the number of iteration reaches this value even if the fit_threshold is not met for all parameters.  
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter, report_fit) |  Fits the data, y = f(x), with the normal (Gaussian) probability density function (defined in the equation above) and returns the values for A = p(1), µ = p(2), and σ = p(3). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum (A = 1). fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold. max_iter = maximum number of iteration during the fit (default = 400). The fitting will stop when the number of iteration reaches this value even if the fit_threshold is not met for all parameters. report_fit = 0 (default) or 1. If set to 1, a report on the fit quality will be provided in the script prompt.  
  
**Example**

In the following example, an experimentally measured 1D doping profile is fitted with normal (Gaussian) probability density function using the  fitnormpdf  script command. The example then plots the measured data and the fitted distribution on the same plot.
    
    
    x = [0.00175681 ; 0.0225484 ; 0.0340938 ; 0.0620684 ; 0.0726683 ; 0.0992729 ; 0.125007 ; 0.148238 ; 0.169105 ; 0.200233 ; 0.225537];
    y = [2.58715e+020 ; 3.23242e+020 ; 3.70291e+020 ; 2.81076e+020 ; 1.97757e+020 ; 6.47495e+019 ; 1.09791e+019 ; 2.81586e+018 ; 7.95827e+017 ; 3.40914e+017 ; 1.53187e+017];
    p = fitnormpdf(x,y,0,sqrt(2e-16),400,1);
    yfit = p(1)*normpdf(x, p(2), p(3));
    plot(x,yfit,"x (um)", "N (1/cm3)", "normpdf","log10y");
    holdon;
    plot(x,y,"xx","yy","title1","log10y, plot points");
    holdoff;
    legend("fit","measured");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ normpdf ](/hc/en-us/articles/360034406454-normpdf) , [ pearson4pdf ](/hc/en-us/articles/360034926693-person4pdf) , [ fitpearson4pdf ](/hc/en-us/articles/360034927013-fitpearson4pdf)
