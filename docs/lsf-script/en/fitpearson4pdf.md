# fitpearson4pdf

Fits any real-valued data, y = f(x), where x is a real valued argument, to the Pearson
IV probability density function (PDF). The Pearson PDF is described by:

$$
\\frac{1}{f(x)}\\frac{df}{dx}=\\frac{(x-\\lambda)+a\_{0}}{b\_{0}+b\_{1}(x-\\lambda)+b\_{2}(x-\\lambda)^{2}}
$$

It is categorized as type IV when the discriminant b0 +b1 x+b2 x 2 has no real roots.
The Pearson IV PDF is typically defined in terms of the coefficients a0 ,b0 ,b1 and b2
that depend on the variance σ2 , skewness γ1 , and kurtosis β2 .

| **Syntax**                                                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| p = fitpearson4pdf(x, y)                                             | Fits the data, y = f(x), with the Pearson IV probability density function (defined in the equations above) and returns the values for mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), and a normalization factor = p(1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| p = fitpearson4pdf(x, y, normalize)                                  | Fits the data, y = f(x), with the Pearson IV probability density function (defined in the equations above) and returns the values for mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), and a normalization factor = p(1). **Optional argument:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum [p(1) = 1].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| p = fitpearson4pdf(x, y, normalize, fit_threshold)                   | Fits the data, y = f(x), with the Pearson IV probability density function (defined in the equations above) and returns the values for mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), and a normalization factor = p(1). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum [p(1) = 1]. fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold.                                                                                                                                                                                                                                                                                                                   |
| p = fitpearson4pdf(x, y, normalize, fit_threshold, max_iter)         | Fits the data, y = f(x), with the Pearson IV probability density function (defined in the equations above) and returns the values for mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), and a normalization factor = p(1). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum [p(1) = 1]. fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold. max_iter = maximum number of iteration during the fit (default = 400). The fitting will stop when the number of iteration reaches this value even if the fit_threshold is not met for all parameters.                                                                                                             |
| p = fitnormpdf(x, y, normalize, fit_threshold, max_iter, report_fit) | Fits the data, y = f(x), with the Pearson IV probability density function (defined in the equations above) and returns the values for mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), and a normalization factor = p(1). **Optional arguments:** normalize = 0 (default) or 1. If set to 1, the fit amplitude is relative to a distribution with a unit maximum (A = 1). fit_threshold = relative tolerance for the fitting convergence (default = 2e-8). Fitting will stop when the relative change in the parameters falls below this threshold. max_iter = maximum number of iteration during the fit (default = 400). The fitting will stop when the number of iteration reaches this value even if the fit_threshold is not met for all parameters. report_fit = 0 (default) or 1. If set to 1, a report on the fit quality will be provided in the script prompt. |

**Example**

In the following example, an experimentally measured 1D doping profile is fitted with
Pearson IV probability density function using the fitpearson4pdf script command. The
example then plots the measured data and the fitted distribution on the same plot.

```
x = [0.00175681 ; 0.0225484 ; 0.0340938 ; 0.0620684 ; 0.0726683 ; 0.0992729 ; 0.125007 ; 0.148238 ; 0.169105 ; 0.200233 ; 0.225537];
y = [2.58715e+020 ; 3.23242e+020 ; 3.70291e+020 ; 2.81076e+020 ; 1.97757e+020 ; 6.47495e+019 ; 1.09791e+019 ; 2.81586e+018 ; 7.95827e+017 ; 3.40914e+017 ; 1.53187e+017];
p = fitpearson4pdf(x,y,0,sqrt(1e-18),800,1);
yfit = p(1) * pearson4pdf( x, p(2), p(3), p(4), p(5) );
plot(x,yfit,"x (um)", "N (1/cm3)", "pearson4pdf","log10y");
holdon;
plot(x,y,"xx","yy","title1","log10y, plot points");
holdoff;
legend("fit","measured");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ normpdf ](./normpdf.md)
, [ pearson4pdf ](https://optics.ansys.com/hc/en-us/articles/360034926693-person4pdf) ,
[ fitnormpdf ](./fitnormpdf.md)
