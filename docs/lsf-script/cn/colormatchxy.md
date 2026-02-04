<!-- Translation completed: 2026-02-04 -->
<!-- Original command: colormatchxy -->

# colormatchxy

    lambda = linspace(300e-9,700e-9,500); # 注意 SI units (meters)  
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
The following figure shows the plot of the test spectrum created by the 示例 code.
  1. <https://en.wikipedia.org/wiki/CIE_1931_color_space>
  2. CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.
  3. CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris.

**语法** | **描述**
---|---
cmxy = colormatchxy(colormatch(spec, lam, "functions")); | 返回 x, y for the spectrum spec evaluated at the 波长 值 in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used.

**示例**

This 示例 shows how to 计算 the x, y 值 for a given spectral 功率 distribution.

This 示例 shows how to 计算 the x, y 值 for a given spectral 功率 distribution.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
