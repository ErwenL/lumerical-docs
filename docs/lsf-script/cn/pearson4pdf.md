# pearson4pdf

计算实数值参数 x 的 Pearson IV 概率密度函数（PDF）

$$ \frac{1}{f(x)}\frac{df}{dx}=\frac{(x-\lambda)+a_{0}}{b_{0}+b_{1}(x-\lambda)+b_{2}(x-\lambda)^{2}} $$

当判别式 b0 +b1 x+b2 x2 没有实根时，Pearson PDF 被分类为 IV 型。Pearson IV PDF 通常用系数 a0、b0、b1 和 b2 定义，这些系数取决于方差 σ2、偏度 γ1 和峰度 β2。对于给定的数据集，用户可以使用 fitpearson4pdf 获取必要的参数，如 σ2、γ1 和 β2。

**语法** | **描述**
---|---
f = pearson4pdf(x) | 返回实数值参数 x 的 Pearson IV 概率密度函数（PDF），等同于正态分布 N(0,1)。
f = pearson4pdf(x,mu,sigma,gamma1,beta2) | 返回实数值参数 x 的 Pearson IV 概率密度函数（PDF）。请参阅上文了解 µ、σ、γ1 和 β2（β2 =3+δ）的定义。

**另请参阅**

- [命令列表](./命令列表.md)
- [fitpearson4pdf](./fitpearson4pdf.md)
- [normpdf](./normpdf.md)
