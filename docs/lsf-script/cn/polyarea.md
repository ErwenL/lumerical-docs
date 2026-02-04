# polyarea

返回多边形的面积。如果顶点按逆时针方向定义，则面积为正；如果顶点按顺时针方向定义，则面积为负。

多边形顶点包含在一个 Nx2（或 2xN）维的矩阵中，其中 N >= 3 是顶点的数量。维度 2 对应 x、y 位置。例如，边长为 1 的正方形可以描述为 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]。

**语法** | **描述**
---|---
out = polyarea(V); | 返回 V 的面积。面积的符号表示 V 是按逆时针（正）还是顺时针（负）方向定义的。

**示例**

计算边长为 1 的正方形的面积：

```powershell
V = [ 0,0; 1,0; 1,1; 0,1];
?polyarea(V);
结果：
1
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[centroid](./centroid.md)、[polyintersect](./polyintersect.md)、[inpoly](./inpoly.md)、[polygrow](./polygrow.md)、[polyand](./polyand.md)、[polyor](./polyor.md)、[polydiff](./polydiff.md)、[polyxor](./polyxor.md)
