<!--
Translation from English documentation
Original command: scorrcoef
Translation date: 2026-02-04 22:50:14
-->

# scorrcoef

Generates 一个 spatial correlation 矩阵. 

**语法** |  **描述**  
---|---  
scorrcoef(x_pos, y_pos, x_corr, y_corr);  |  Generates 一个 spatial correlation 矩阵. x_pos 和 y_pos 是 vectors containing 该 x 和 y layout coordinate respectively, 和 x_corr 和 y_corr 是 该 correlation 值 用于 该 x 和 y coordinates respectively.  Correlation 是 defined as 一个 Gaussian 函数:  $$ \begin{数组}{l}{c\left[(x, y)_{i},(x, y)_{j}\right]=\exp \left(-\frac{1}{2}\left(\frac{\left(x_{j}-x_{i}\right)^{2}}{\sigma_{x}^{2}}+\frac{\left(y_{j}-y_{i}\right)^{2}}{\sigma_{y}^{2}}\right)\right)} \\\ {x=\left[-\frac{x_{\text { span }}}{2},+\frac{x_{\text { span }}}{2}\right]} \\\ {y=\left[-\frac{y_{\text { span }}}{2},+\frac{y_{\text { span }}}{2}\right]}\end{数组} $$   
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
