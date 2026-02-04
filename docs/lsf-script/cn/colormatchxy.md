<!--
Translation from English documentation
Original command: colormatchxy
Translation date: 2026-02-04 22:49:48
-->

# colormatchxy

返回 该 x 和 y chromaticity 值 calculated 用于 一个 given spectral power distribution (power per unit area per unit 波长) 和 一个 选中的 设置 的 color matching functions. The colormatchxy 函数 assumes 该 该 units 的 波长 用于 该 spectral power distribution 是 纳米, 用于 example, W/(m  2  nm). The available color functions 是 该 CIE 1931 和 CIE 1964.

The x 和 y 值 是 dimensionless 和 they 是 related 到 该 X, Y, 和 Z 值 通过:

$$ x=\frac{X}{X+Y+Z}, y=\frac{Y}{X+Y+Z} $$

**语法** |  **描述**  
---|---  
cmxy = colormatchxy(colormatch(spec, lam, "functions")); |  返回 x, y 用于 该 spectrum spec evaluated at 该 波长 值 在 lam (units 的 米), 使用 该 选中的 color functions. If no functions 是 specified, 该 "CIE 1931" 设置 是 used.  
  
**示例**

This example shows 如何 到 计算 该 x, y 值 用于 一个 given spectral power distribution.
    
    
    # 创建 一个 dummy spectrum  
    lambda = linspace(300e-9,700e-9,500); # note SI units (米)  
    spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2);   
    plot(lambda*1e9,spectrum,"波长(nm)","test spectrum");  
      
    ?cmxy64 = colormatchxy( colormatch(spectrum,lambda,"CIE 1964") );  
    result:  
    0.14368   
    0.0606946   
    ?cmxy36 = colormatchxy( colormatch(spectrum,lambda) );  
    result:  
    0.148857   
    0.033839

The following figure shows 该 plot 的 该 test spectrum created 通过 该 example code.

### Related Publications

  1. <https://en.wikipedia.org/wiki/CIE_1931_color_space>
  2. CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.
  3. CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris.



### 参见

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
