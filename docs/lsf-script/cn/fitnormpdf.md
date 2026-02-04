# fitnormpdf

拟合任意实值数据 y = f(x)，其中 x 是实值参数，使用正态（高斯）概率密度函数 (PDF) 定义为：

$$ f(x)=\frac{A}{\sqrt{2\pi \sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}} $$

其中 µ 是正态分布的均值，σ 是标准差，A 是归一化因子。

**语法** | **描述**
---|---
p = fitnormpdf(x, y) | 使用正态（高斯）概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回 A = p(1)、µ = p(2) 和 σ = p(3) 的值。
p = fitnormpdf(x, y, normalize) | 使用正态（高斯）概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回 A = p(1)、µ = p(2) 和 σ = p(3) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布（A = 1）。
p = fitnormpdf(x, y, normalize, fit_threshold) | 使用正态（高斯）概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回 A = p(1)、µ = p(2) 和 σ = p(3) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布（A = 1）。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter) | 使用正态（高斯）概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回 A = p(1)、µ = p(2) 和 σ = p(3) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布（A = 1）。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。max_iter = 拟合期间的最大迭代次数（默认 = 400）。当迭代次数达到此值时，即使未满足所有参数的 fit_threshold，拟合也将停止。
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter, report_fit) | 使用正态（高斯）概率密度函数（定义在上方方程中）拟合数据 y = f(x)，并返回 A = p(1)、µ = p(2) 和 σ = p(3) 的值。**可选参数：** normalize = 0（默认）或 1。如果设置为 1，则拟合振幅相对于最大值为 1 的分布（A = 1）。fit_threshold = 拟合收敛的相对容差（默认 = 2e-8）。当参数的相对变化低于此阈值时，拟合将停止。max_iter = 拟合期间的最大迭代次数（默认 = 400）。当迭代次数达到此值时，即使未满足所有参数的 fit_threshold，拟合也将停止。report_fit = 0（默认）或 1。如果设置为 1，将在脚本提示中提供拟合质量报告。

**示例**

在以下示例中，使用 fitnormpdf 脚本命令将实验测量的 1D 掺杂分布拟合为正态（高斯）概率密度函数。然后该示例在同一图上绘制测量数据和拟合分布。

```powershell
x = [0.00175681 ; 0.0225484 ; 0.0340938 ; 0.0620684 ; 0.0726683 ; 0.0992729 ; 0.125007 ; 0.148238 ; 0.169105 ; 0.200233 ; 0.225537];
y = [2.58715e+020 ; 3.23242e+020 ; 3.70291e+020 ; 2.81076e+020 ; 1.97757e+020 ; 6.47495e+019 ; 1.09791e+019 ; 2.81586e+018 ; 7.95827e+017 ; 3.40914e+017 ; 1.53187e+017];
p = fitnormpdf(x,y,0,sqrt(2e-16),400,1);
yfit = p(1)*normpdf(x, p(2), p(3));
plot(x,yfit,"x (um)", "N (1/cm3)", "normpdf","log10y");
holdon;
plot(x,y,"xx","yy","title1","log10y, plot points");
holdoff;
legend("fit","measured");
```

**另请参阅**

[命令列表](../命令列表.md)、[normpdf](./normpdf.md)、[pearson4pdf](./pearson4pdf.md)、[fitpearson4pdf](./fitpearson4pdf.md)