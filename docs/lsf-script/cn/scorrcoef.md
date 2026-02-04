<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: scorrcoef -->

# scorrcoef

生成空间相关矩阵。

**语法** |  **描述**  
---|---  
scorrcoef(x_pos, y_pos, x_corr, y_corr);  |  生成空间相关矩阵。x_pos 和 y_pos 分别是包含 x 和 y 布局坐标的向量，x_corr 和 y_corr 分别是 x 和 y 坐标的相关值。相关性定义为高斯函数： $$ \begin{array}{l}{c\left[(x, y)_{i},(x, y)_{j}\right]=\exp \left(-\frac{1}{2}\left(\frac{\left(x_{j}-x_{i}\right)^{2}}{\sigma_{x}^{2}}+\frac{\left(y_{j}-y_{i}\right)^{2}}{\sigma_{y}^{2}}\right)\right)} \\ {x=\left[-\frac{x_{\text { span }}}{2},+\frac{x_{\text { span }}}{2}\right]} \\ {y=\left[-\frac{y_{\text { span }}}{2},+\frac{y_{\text { span }}}{2}\right]}\end{array} $$  
  
**另请参阅**

- [命令列表](./index.md)
- [cov](./cov.md)
- [corrtransf](./corrtransf.md)
