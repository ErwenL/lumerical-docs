# polyintersect

判断两个多边形是否相交。

多边形顶点包含在一个 Nx2（或 2xN）维的矩阵中，其中 N >= 3 是顶点的数量。维度 2 对应 x、y 位置。例如，边长为 1 的正方形可以描述为 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]。

**语法** | **描述**
---|---
out = polyintersect(V1,V2); | 返回

- 0 如果多边形不相交
- 0.5 如果多边形相切
- 1 如果它们相交
- 2 如果一个多边形完全包含另一个

**示例**

以下示例说明两个多边形的不同可能的相交情况：

```powershell
V1 = [ 0,0; 1,0; 1,1; 0,1];
V2 = [ 0,0; 2,0; 2,2; 0,1];
?polyintersect(V1,V2);
结果：
2
?polyintersect(V1,V2+0.5); #将 V2 向右移动 0.5
结果：
1
?polyintersect(V1,V2+1); #将 V2 向右移动 1
结果：
0.5
?polyintersect(V1,V2+2); #将 V2 向右移动 2
结果：
0
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[polyarea](./polyarea.md)、[centroid](./centroid.md)、[inpoly](./inpoly.md)、[polygrow](./polygrow.md)、[polyand](./polyand.md)、[polyor](./polyor.md)、[polydiff](./polydiff.md)、[polyxor](./polyxor.md)
