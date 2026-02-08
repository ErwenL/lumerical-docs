# scorrcoef

Generates a spatial correlation matrix.

| **Syntax**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| scorrcoef(x_pos, y_pos, x_corr, y_corr); | Generates a spatial correlation matrix. x_pos and y_pos are vectors containing the x and y layout coordinate respectively, and x_corr and y_corr are the correlation values for the x and y coordinates respectively. Correlation is defined as a Gaussian function: $$ \\begin{array}{l}{c\\left\[(x, y)_{i},(x, y)_{j}\\right\]=\\exp \\left(-\\frac{1}{2}\\left(\\frac{\\left(x\_{j}-x\_{i}\\right)^{2}}{\\sigma\_{x}^{2}}+\\frac{\\left(y\_{j}-y\_{i}\\right)^{2}}{\\sigma\_{y}^{2}}\\right)\\right)} \\\\ {x=\\left[-\\frac{x\_{\\text { span }}}{2},+\\frac{x\_{\\text { span }}}{2}\\right]} \\\\ {y=\\left[-\\frac{y\_{\\text { span }}}{2},+\\frac{y\_{\\text { span }}}{2}\\right]}\\end{array} $$ |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ cov ](./cov.md) ,
[ corrtransf ](./corrtransf.md)
