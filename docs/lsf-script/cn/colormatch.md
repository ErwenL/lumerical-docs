<!-- Translation completed: 2026-02-04 -->
<!-- Original command: colormatch -->

# colormatch

    lambda = linspace(300e-9,700e-9,500); # 注意 SI units (meters)
    spectrum = exp(-(lambda-450e-9)^2/(30e-9)^2); 
    plot(lambda*1e9,spectrum,"波长(nm)","test spectrum");
    ?cm64 = colormatch(spectrum,lambda,"CIE 1964");
    result:
    14.3731 
    6.07161 
    79.5907
    ?cm36 = colormatch(spectrum,lambda); # "CIE 1931" is assumed if no color matching functions are specified
    result:
    13.1613 
    2.99189 
    72.2623
The following figure shows the plot of the test spectrum created by the 示例 code.

**语法** | **描述**
---|---
cm = colormatch(spec, lam, "functions"); | 返回 X, Y, Z for the spectrum spec evaluated at the 波长 值 in lam (units of meters), using the selected color functions. If no functions are specified, the "CIE 1931" set is used.

**示例**

This 示例 shows how to 计算 the X, Y, Z 值 for a given spectral 功率 distribution.

This 示例 shows how to 计算 the X, Y, Z 值 for a given spectral 功率 distribution.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ colormatchfunction ](/hc/en-us/articles/360034926733-colormatchfunction) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
