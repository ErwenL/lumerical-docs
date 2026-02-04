<!--
Translation from English documentation
Original command: inpoly
Translation date: 2026-02-03
-->

# inpoly

确定一个点是在多边形内部还是外部。该函数是向量化的，因此可用于创建多边形的网格。

多边形顶点包含在维度为 Nx2（或 2xN）的单个矩阵中，其中 N >= 3 是顶点的数量。维度 2 对应 x、y 位置。例如，边长为 1 的正方形可以描述为 V = [0,0; 1,0; 1,1; 0,1] 或 V = [0,1,1,0;0,0,1,1]。

**语法** |  **描述**
---|---
out = inpoly(V,x,y);  |  返回与 x 维度相同的矩阵，如果对应的点在多边形内部则为 1，否则为 0。矩阵 x 和 y 必须具有相同的长度，或者其中一个可以是单例。

**示例**

以下示例显示如何识别网格中位于多边形内部的点。

    V = [ 0,0; 1,0; 1,1; 0,1];
    x = linspace(-4,4,100);
    y = linspace(-4,4,100);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    image(x,y,inpoly(V,X,Y),"x","y");

生成的图像是：

**相关命令**

- [List of commands](./List-of-commands.md)
- [polyarea](./polyarea.md)
- [centroid](./centroid.md)
- [polyintersect](./polyintersect.md)
- [polygrow](./polygrow.md)
- [polyand](./polyand.md)
- [polyor](./polyor.md)
- [polydiff](./polydiff.md)
- [polyxor](./polyxor.md)
- [meshgridx](./meshgridx.md)
- [meshgridy](./meshgridy.md)
