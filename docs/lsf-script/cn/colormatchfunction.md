<!-- Translation completed: 2026-02-04 -->
<!-- Original command: colormatchfunction -->

# colormatchfunction

**语法** | **描述**
---|---
?colormatchfunction; | Show the list of available color matching functions.
M = colormatchfunction("functions"); | Get the desired set of color matching functions from the list of available 全1矩阵.

**示例**

This 示例 shows how to get the list of available color matching functions and plot them. 
    ?colormatchfunction; #Show the list of color matching functions
    result:
    CIE 1931
    CIE 1964
    M1 = colormatchfunction("CIE 1931");
    M2 = colormatchfunction("CIE 1964");
    lambda1 = 压缩(M1,2,1)*1e9; #Get the 波长 值 where the 函数 M1 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar1 = 压缩(M1,2,2);
    ybar1 = 压缩(M1,2,3);
    zbar1 = 压缩(M1,2,4);
    lambda2 = 压缩(M2,2,1)*1e9; #Get the 波长 值 where the 函数 M2 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar2 = 压缩(M2,2,2);
    ybar2 = 压缩(M2,2,3);
    zbar2 = 压缩(M2,2,4);
    plotxy(lambda1,xbar1,lambda1,ybar1,lambda1,zbar1,lambda2,xbar2,lambda2,ybar2,lambda2,zbar2,"波长 (nm)","Color matching functions");
    legend("xbar (CIE 1931)","ybar (CIE 1931)","zbar (CIE 1931)","xbar (CIE 1964)","ybar (CIE 1964)","zbar (CIE 1964)");
The following figure shows the 输出 of the 示例 code. 

This 示例 shows how to get the list of available color matching functions and plot them. 
    ?colormatchfunction; #Show the list of color matching functions
    result:
    CIE 1931
    CIE 1964
    M1 = colormatchfunction("CIE 1931");
    M2 = colormatchfunction("CIE 1964");
    lambda1 = 压缩(M1,2,1)*1e9; #Get the 波长 值 where the 函数 M1 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar1 = 压缩(M1,2,2);
    ybar1 = 压缩(M1,2,3);
    zbar1 = 压缩(M1,2,4);
    lambda2 = 压缩(M2,2,1)*1e9; #Get the 波长 值 where the 函数 M2 is evaluated (in SI units, i.e. meters) and convert to nanometers.
    xbar2 = 压缩(M2,2,2);
    ybar2 = 压缩(M2,2,3);
    zbar2 = 压缩(M2,2,4);
    plotxy(lambda1,xbar1,lambda1,ybar1,lambda1,zbar1,lambda2,xbar2,lambda2,ybar2,lambda2,zbar2,"波长 (nm)","Color matching functions");
    legend("xbar (CIE 1931)","ybar (CIE 1931)","zbar (CIE 1931)","xbar (CIE 1964)","ybar (CIE 1964)","zbar (CIE 1964)");
The following figure shows the 输出 of the 示例 code. 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ colormatch ](/hc/en-us/articles/360034926753-colormatch) , [ colormatchxy ](/hc/en-us/articles/360034926773-colormatchxy) , [ colormatchuv ](/hc/en-us/articles/360034406514-colormatchuv)
