<!--
Translation from English documentation
Original command: fitpearson4pdf
Translation date: 2026-02-04 22:49:49
-->

# fitpearson4pdf

Fits any real-valued 数据, y = f(x), 其中 x 是 一个 real valued 参数, 到 该 Pearson IV probability density 函数 (PDF). The Pearson PDF 是 described 通过:

$$ \frac{1}{f(x)}\frac{df}{dx}=\frac{(x-\lambda)+a_{0}}{b_{0}+b_{1}(x-\lambda)+b_{2}(x-\lambda)^{2}} $$

It 是 categorized as 类型 IV 当 该 discriminant b0  +b1  x+b2  x  2  has no real roots. The Pearson IV PDF 是 typically defined 在 terms 的 该 coefficients a0  ,b0  ,b1  和 b2  该 depend 在 该 variance σ2  , skewness γ1  , 和 kurtosis β2  .

**语法** |  **描述**  
---|---  
p = fitpearson4pdf(x, y) |  Fits 该 数据, y = f(x), 使用 该 Pearson IV probability density 函数 (defined 在 该 equations above) 和 返回 该 值 用于 mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), 和 一个 normalization factor = p(1).  
p = fitpearson4pdf(x, y, normalize) |  Fits 该 数据, y = f(x), 使用 该 Pearson IV probability density 函数 (defined 在 该 equations above) 和 返回 该 值 用于 mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), 和 一个 normalization factor = p(1). **Optional 参数:** normalize = 0 (default) 或 1. If 设置 到 1, 该 fit amplitude 是 relative 到 一个 distribution 使用 一个 unit maximum [p(1) = 1].  
p = fitpearson4pdf(x, y, normalize, fit_threshold) |  Fits 该 数据, y = f(x), 使用 该 Pearson IV probability density 函数 (defined 在 该 equations above) 和 返回 该 值 用于 mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), 和 一个 normalization factor = p(1). **Optional 参数:** normalize = 0 (default) 或 1. If 设置 到 1, 该 fit amplitude 是 relative 到 一个 distribution 使用 一个 unit maximum [p(1) = 1]. fit_threshold = relative tolerance 用于 该 fitting convergence (default = 2e-8). Fitting 将 stop 当 该 relative change 在 该 参数 falls below 此 threshold.  
p = fitpearson4pdf(x, y, normalize, fit_threshold, max_iter) |  Fits 该 数据, y = f(x), 使用 该 Pearson IV probability density 函数 (defined 在 该 equations above) 和 返回 该 值 用于 mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), 和 一个 normalization factor = p(1). **Optional 参数:** normalize = 0 (default) 或 1. If 设置 到 1, 该 fit amplitude 是 relative 到 一个 distribution 使用 一个 unit maximum [p(1) = 1]. fit_threshold = relative tolerance 用于 该 fitting convergence (default = 2e-8). Fitting 将 stop 当 该 relative change 在 该 参数 falls below 此 threshold. max_iter = maximum 数字 的 iteration during 该 fit (default = 400). The fitting 将 stop 当 该 数字 的 iteration reaches 此 值 even 如果 该 fit_threshold 是 not met 用于 all 参数.  
p = fitnormpdf(x, y, normalize, fit_threshold, max_iter, report_fit) |  Fits 该 数据, y = f(x), 使用 该 Pearson IV probability density 函数 (defined 在 该 equations above) 和 返回 该 值 用于 mean = p(2), variance = p(3), skewness = p(4), kurtosis = p(5), 和 一个 normalization factor = p(1). **Optional 参数:** normalize = 0 (default) 或 1. If 设置 到 1, 该 fit amplitude 是 relative 到 一个 distribution 使用 一个 unit maximum (A = 1). fit_threshold = relative tolerance 用于 该 fitting convergence (default = 2e-8). Fitting 将 stop 当 该 relative change 在 该 参数 falls below 此 threshold. max_iter = maximum 数字 的 iteration during 该 fit (default = 400). The fitting 将 stop 当 该 数字 的 iteration reaches 此 值 even 如果 该 fit_threshold 是 not met 用于 all 参数. report_fit = 0 (default) 或 1. If 设置 到 1, 一个 report 在 该 fit quality 将 为 provided 在 该 脚本 prompt.  
  
**示例**

In 该 following example, 一个 experimentally measured 1D doping profile 是 fitted 使用 Pearson IV probability density 函数 使用 该  fitpearson4pdf  脚本 命令. The example 那么 plots 该 measured 数据 和 该 fitted distribution 在 该 same plot.
    
    
    x = [0.00175681 ; 0.0225484 ; 0.0340938 ; 0.0620684 ; 0.0726683 ; 0.0992729 ; 0.125007 ; 0.148238 ; 0.169105 ; 0.200233 ; 0.225537];
    y = [2.58715e+020 ; 3.23242e+020 ; 3.70291e+020 ; 2.81076e+020 ; 1.97757e+020 ; 6.47495e+019 ; 1.09791e+019 ; 2.81586e+018 ; 7.95827e+017 ; 3.40914e+017 ; 1.53187e+017];
    p = fitpearson4pdf(x,y,0,sqrt(1e-18),800,1);
    yfit = p(1) * pearson4pdf( x, p(2), p(3), p(4), p(5) );
    plot(x,yfit,"x (um)", "N (1/cm3)", "pearson4pdf","log10y");
    holdon;
    plot(x,y,"xx","yy","title1","log10y, plot points");
    holdoff;
    legend("fit","measured");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ normpdf ](/hc/en-us/articles/360034406454-normpdf) , [ pearson4pdf ](/hc/en-us/articles/360034926693-person4pdf) , [ fitnormpdf ](/hc/en-us/articles/360034926993-fitnormpdf)
