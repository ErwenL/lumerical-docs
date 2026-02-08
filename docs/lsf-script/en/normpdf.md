# normpdf

Evaluates the normal (Gaussian) probability density function (PDF) for real-valued
argument x

$$ f(x)=\\frac{1}{\\sqrt{2\\pi \\sigma^{2}}}e^{-\\frac{(x-\\mu)^{2}}{2\\sigma^{2}}} $$

where µ is the mean and σ is the standard deviation. By default, μ=0 and σ=1.

| **Syntax**              | **Description**                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| f = normpdf(x)          | Returns the normal (Gaussian) probability density function (PDF) for real-valued argument x. By default, μ=0 and σ=1                        |
| f = normpdf(x,mu,sigma) | Returns the normal (Gaussian) probability density function (PDF) for real-valued argument x. µ is the mean and σ is the standard deviation. |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ pearson4pdf ](https://optics.ansys.com/hc/en-us/articles/360034926693-person4pdf)
