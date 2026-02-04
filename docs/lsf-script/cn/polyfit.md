# polyfit

基于线性回归计算多项式拟合。数据可以是复数。

**语法** | **描述**
---|---
p = polyfit(x, y, N); | 返回次数为 N 的多项式 p(x) 的系数，该多项式是对 y 中数据的最佳拟合。\\( p(x)=p_1 + p_2x^1+p_3x^2+...+p_Nx^{N-1}+p_{N+1}x^N \\) 系数的长度为 N+1。

**示例**

在此示例中，噪声被添加到平滑函数中。对噪声数据进行多项式拟合可以大致恢复原始函数。

```powershell
clear;
x = linspace(0,10,100);
noise_amp = 200;
y_original = 3.2 + 2i*x + 4.5*x^2 - 0.04*x^3;
y_noise = y_original + noise_amp*(randmatrix(length(x))-0.5);
fit = polyfit(x,y_noise,3);
y_fit = fit(1) + fit(2)*x + fit(3)*x^2 + fit(4)*x^3;
plot(x,abs(y_original),abs(y_noise),abs(y_fit));
legend("y_original","y_noise","y_fit");
?fit;
结果：
-20.3301+1.67422e-013i # fit(1)
19.7752+2i  # fit(2)
-0.477739+4.58522e-014i # fit(3)
0.304786-4.35069e-015i # fit(4)
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[interp](./interp.md)、[spline](./spline.md)
