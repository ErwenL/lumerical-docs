<!-- Translation completed: 2026-02-04 -->
<!-- Original command: colormatchuv -->

# colormatchuv

    lambda = linspace(300e-9,700e-9,500); # 注意 SI units (meters)
    spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2); 
    plot(lambda*1e9,spectrum,"波长(nm)","test spectrum");
    ?cmuv64 = colormatchuv( colormatch(spectrum,lambda,"CIE 1964") );
    result:
    0.167023 
    0.158749 
    ?cmuv36 = colormatchuv( colormatch(spectrum,lambda) );
    result:
    0.191558 
    0.0979782
The following figure shows the plot of the test spectrum created by the 示例 code. 

**语法** | **描述**
---|---
cmuv = colormatchuv(colormatch(spec, lam, "functions")); | 返回 u', v' for the spectrum spec evaluated at the 波长 值 in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used.

**示例**

This 示例 shows how to 计算 the u', v' 值 for a given spectral 功率 distribution. 

This 示例 shows how to 计算 the u', v' 值 for a given spectral 功率 distribution. 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy)
