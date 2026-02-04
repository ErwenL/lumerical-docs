<!--
Translation from English documentation
Original command: icht
Translation date: 2026-02-03
-->

# icht

获取 Chebyshev 插值系数并返回相应的函数样本。

**语法** |  **描述**
---|---
out=icht(coeff,option);  |  从 Chebyshev 插值系数 coeff 返回函数样本。选项：如果选择 option=1，则向量 x 不包括端点；如果选择 option=2，则向量 x 包括端点。

**示例**

此示例展示如何从采样的函数获取插值系数，然后从系数计算回函数样本。

    Nc = 15;           # Number of sample points
    xmin = 0;
    xmax = 1;
    x = chpts(xmin,xmax,Nc,1); # Returns Chebyshev roots grid on interval between xmin and xmax
    f = exp(1i*2*pi*x);     # Function sampling using Chebyshev grid
    coeff = dcht(f,1);     # Get interpolation coefficients
    # Calculate the function samples from the coefficients and compare them to the original function samples
    ?icht(coeff,1);
    ?f;

**相关命令**

- [dcht](./dcht.md)
- [chpts](./chpts.md)
- [chebin](./chebin.md)
