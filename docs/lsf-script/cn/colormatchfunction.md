<!--
Translation from English documentation
Original command: colormatchfunction
Translation date: 2026-02-04 22:49:48
-->

# colormatchfunction

返回 该 设置 的 color matching functions \\( \overline{x} \\), \\( \overline{y} \\) ,\\( \overline{z} \\) 选中的 通过 该 用户. These functions 是 dimensionless. The available 设置 是 该 CIE 1931 和 CIE 1964. 

References: 

CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press. 

CIE Proceedings (1964) Vienna Session, 1963, Vol. B, pp. 209-220 (Committee Report E-1.4.1), Bureau Central de la CIE, Paris. 

**语法** |  **描述**  
---|---  
?colormatchfunction;  |  Show 该 list 的 available color matching functions.   
M = colormatchfunction("functions");  |  获取 该 desired 设置 的 color matching functions 从 该 list 的 available ones.   
  
**示例**

This example shows 如何 到 获取 该 list 的 available color matching functions 和 plot them. 
    
    
    ?colormatchfunction; #Show 该 list 的 color matching functions
    result:
    CIE 1931
    CIE 1964
    M1 = colormatchfunction("CIE 1931");
    M2 = colormatchfunction("CIE 1964");
    lambda1 = pinch(M1,2,1)*1e9; #获取 该 波长 值 其中 该 函数 M1 是 evaluated (在 SI units, i.e. 米) 和 转换 到 纳米.
    xbar1 = pinch(M1,2,2);
    ybar1 = pinch(M1,2,3);
    zbar1 = pinch(M1,2,4);
    lambda2 = pinch(M2,2,1)*1e9; #获取 该 波长 值 其中 该 函数 M2 是 evaluated (在 SI units, i.e. 米) 和 转换 到 纳米.
    xbar2 = pinch(M2,2,2);
    ybar2 = pinch(M2,2,3);
    zbar2 = pinch(M2,2,4);
    plotxy(lambda1,xbar1,lambda1,ybar1,lambda1,zbar1,lambda2,xbar2,lambda2,ybar2,lambda2,zbar2,"波长 (nm)","Color matching functions");
    legend("xbar (CIE 1931)","ybar (CIE 1931)","zbar (CIE 1931)","xbar (CIE 1964)","ybar (CIE 1964)","zbar (CIE 1964)");

The following figure shows 该 output 的 该 example code. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
