<!--
Translation from English documentation
Original command: colormatch
Translation date: 2026-02-04 22:49:48
-->

# colormatch

返回 该 X, Y 和 Z tristimulus 值 calculated 用于 一个 given spectral power distribution (power per unit area per unit 波长) 和 一个 选中的 设置 的 color matching functions. The colormatch 函数 assumes 该 该 units 的 波长 用于 该 spectral power distribution 是 纳米, 用于 example, W/(m  2  nm). The available color functions 是 该 CIE 1931 和 CIE 1964.

The X, Y, Z 值 have dimensions 的 power per unit area, 在 该 units used 用于 该 spectral power distribution. The expressions 用于 calculating 该 X, Y 和 Z 值 是:

$$ \begin{aligned} X &=\int I(\lambda) \overline{x}(\lambda) d \lambda \\\ Y &=\int I(\lambda) \overline{y}(\lambda) d \lambda \\\ Z &=\int I(\lambda) \overline{z}(\lambda) d \lambda \end{aligned} $$

其中 I(͛λ) 是 该 spectral power distribution 和 \\( \overline{x} \\), \\( \overline{y} \\) ,\\( \overline{z} \\) 是 该 color matching functions.

References:

[ https://en.wikipedia.org/wiki/CIE_1931_color_space ](https://en.wikipedia.org/wiki/CIE_1931_color_space)

CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.

CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris.

**语法** |  **描述**  
---|---  
cm = colormatch(spec, lam, "functions"); |  返回 X, Y, Z 用于 该 spectrum spec evaluated at 该 波长 值 在 lam (units 的 米), 使用 该 选中的 color functions. If no functions 是 specified, 该 "CIE 1931" 设置 是 used.  
  
**示例**

This example shows 如何 到 计算 该 X, Y, Z 值 用于 一个 given spectral power distribution.
    
    
    # 创建 一个 dummy spectrum
    lambda = linspace(300e-9,700e-9,500); # note SI units (米)
    spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2); 
    plot(lambda*1e9,spectrum,"波长(nm)","test spectrum");
     
    ?cm64 = colormatch(spectrum,lambda,"CIE 1964");
    result:
    14.3731 
    6.07161 
    79.5907
    ?cm36 = colormatch(spectrum,lambda); # "CIE 1931" 是 assumed 如果 no color matching functions 是 specified
    result:
    13.1613 
    2.99189 
    72.2623

The following figure shows 该 plot 的 该 test spectrum created 通过 该 example code.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
