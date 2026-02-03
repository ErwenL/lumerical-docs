# scorrcoef

Generates a spatial correlation matrix. 

**Syntax** |  **Description**  
---|---  
scorrcoef(x_pos, y_pos, x_corr, y_corr);  |  Generates a spatial correlation matrix. x_pos and y_pos are vectors containing the x and y layout coordinate respectively, and x_corr and y_corr are the correlation values for the x and y coordinates respectively.  Correlation is defined as a Gaussian function:  $$ \begin{array}{l}{c\left[(x, y)_{i},(x, y)_{j}\right]=\exp \left(-\frac{1}{2}\left(\frac{\left(x_{j}-x_{i}\right)^{2}}{\sigma_{x}^{2}}+\frac{\left(y_{j}-y_{i}\right)^{2}}{\sigma_{y}^{2}}\right)\right)} \\\ {x=\left[-\frac{x_{\text { span }}}{2},+\frac{x_{\text { span }}}{2}\right]} \\\ {y=\left[-\frac{y_{\text { span }}}{2},+\frac{y_{\text { span }}}{2}\right]}\end{array} $$   
  
**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
