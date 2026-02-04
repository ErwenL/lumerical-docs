# fitpearson4pdf

拟合任意实值数据 y = f(x)，其中 x 是实值参数，到 Pearson IV 概率密度函数 (PDF)。Pearson PDF 描述为：

$$ \frac{1}{f(x)}\frac{df}{dx}=\frac{(x-\lambda)+a_{0}}{b_{0}+b_{1}(x-\lambda)+b_{2}(x-\lambda)^{2}} $$

当判别式 b0 +b1 x+b2 x^2 没有实根时，它被分类为 IV 型。Pearson IV PDF 通常根据依赖于方差 σ2、偏度 γ1 和峰度 β2 的系数 a0、b0、b1 和 b2 来定义。

**语法** | **描述**
---|---
p = fitpearson4pdf(x, y) | 使用 Pearson IV 概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回均值 = p(2)、方差 = p(3)、偏度 = p(4)、峰度 = p(5) 和归一化因子 = p(1) 的值。
p = fitpearson4pdf(x, y, normalize) | 使用 Pearson IV 概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回均值 = p(2)、方差 = p(3)、偏度 = p(4)、峰度 = p(5) 和归一化因子 = p(1) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布 [p(1) = 1]。
p = fitpearson4pdf(x, y, normalize, fit_threshold) | 使用 Pearson IV 概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回均值 = p(2)、方差 = p(3)、偏度 = p(4)、峰度 = p(5) 和归一化因子 = p(1) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布 [p(1) = 1]。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。
p = fitpearson4pdf(x, y, normalize, fit_threshold, max_iter) | 使用 Pearson IV 概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回均值 = p(2)、方差 = p(3)、偏度 = p(4)、峰度 = p(5) 和归一化因子 = p(1) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布 [p(1) = 1]。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。max_iter = 拟合期间的最大迭代次数（默认 = 400）。当迭代次数达到此值时，即使未满足所有参数的 fit_threshold，拟合也将停止。
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter, report_fit) | 使用 Pearson IV 概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回均值 = p(2)、方差 = p(3)、偏度 = p(4)、峰度 = p(5) 和归一化因子 = p(1) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布（A = 1）。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。max_iter = 拟合期间的最大迭代次数（默认 = 400）。当迭代次数达到此值时，即使未满足所有参数的 fit_threshold，拟合也将停止。report_fit = 0（默认）或 1。如果设置为 1，将在脚本提示中提供拟合质量报告。

**示例**

在以下示例中，使用 fitpearson4pdf 脚本命令将实验测量的 1D 掺杂分布拟合为 Pearson IV 概率密度函数。然后该示例在同一图上绘制测量数据和拟合分布。

```powershell
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

**另请参阅**

[命令列表](../命令列表.md)、[normpdf](./normpdf.md)、[pearson4pdf](./pearson4pdf.md)、[fitnormpdf](./fitnormpdf.md)