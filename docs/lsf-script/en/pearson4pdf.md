# pearson4pdf

Evaluate the Pearson IV probability density function (PDF) for real-valued argument x

$$
\\frac{1}{f(x)}\\frac{df}{dx}=\\frac{(x-\\lambda)+a\_{0}}{b\_{0}+b\_{1}(x-\\lambda)+b\_{2}(x-\\lambda)^{2}}
$$

The Pearson PDF is categorized as type IV when the discriminant b0 +b1 x+b2 x2 has no
real roots. The Pearson IV PDF is typically defined in terms of the coefficients a0 ,b0
,b1 and b2 that depend on the variance σ2 , skewness γ1 , and kurtosis β2 . For a given
set of data, users can use
[fitpearson4pdf](https://optics.ansys.com/hc/en-us/articles/360034926693) to get the
necessary parameters such as σ2 , γ1 , and β2 .

| **Syntax**                               | **Description**                                                                                                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f = pearson4pdf(x)                       | Returns the Pearson IV probability density function (PDF) for real-valued argument x, equivalent to normal distribution N(0,1).                           |
| f = pearson4pdf(x,mu,sigma,gamma1,beta2) | Returns the Pearson IV probability density function (PDF) for real-valued argument x. Please see above for the definition of µ, σ, γ1 , and β2 (β2 =3+δ). |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[fitpearson4pdf](https://optics.ansys.com/hc/en-us/articles/360034926693),
[ normpdf ](./normpdf.md)
