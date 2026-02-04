# polyxor

使用布尔"异或"运算将两个多边形合并为一个。

多边形顶点包含在一个 Nx2（或 2xN）维的矩阵中，其中 N >= 3 是顶点的数量。维度 2 对应 x、y 位置。例如，边长为 1 的正方形可以描述为 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]。

**语法** | **描述**
---|---
V3 = polyxor(V1,V2); | 返回一个新多边形 V3，它是 V1 和 V2 的"异或"运算结果。

**示例**

请参阅 polyand 函数描述中的示例。

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[polyand](./polyand.md)、[polyor](./polyor.md)、[polydiff](./polydiff.md)、[polyarea](./polyarea.md)、[centroid](./centroid.md)、[polyintersect](./polyintersect.md)、[inpoly](./inpoly.md)、[polygrow](./polygrow.md)
