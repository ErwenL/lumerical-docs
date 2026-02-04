# polyand

使用布尔"与"运算将两个多边形合并为一个。

多边形顶点包含在一个 Nx2（或 2xN）维的矩阵中，其中 N >= 3 是顶点的数量。维度 2 对应 x、y 位置。例如，边长为 1 的正方形可以描述为 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]。

**语法** | **描述**
---|---
V3 = polyand(V1,V2); | 返回一个新多边形 V3，它是 V1 和 V2 的"与"运算结果。

**示例**

在此示例中，我们创建两个多边形，然后展示如何进行不同的布尔运算。我们设置网格并使用 inpoly 函数，以便可视化多边形并轻松查看结果。

```powershell
# 设置用于可视化多边形的网格（使用 inpoly 命令）
x = linspace(-1,3,200);
y = linspace(-1,3,200);
X = meshgridx(x,y);
Y = meshgridy(x,y);
# 输入两个多边形以及多边形布尔运算
V1 = [ 0,0; 1,0; 1,1; 0,1];
V2 = [ 0,0; 2,2; 0,2];
V3 = polyand(V1,V2);
V4 = polyor(V1,V2);
V5 = polydiff(V1,V2);
V6 = polydiff(V2,V1);
V7 = polyxor(V2,V1);
# 可视化所有多边形
image(x,y,inpoly(V1,X,Y),"x","y","V1");
image(x,y,inpoly(V2,X,Y),"x","y","V2");
image(x,y,inpoly(V3,X,Y),"x","y","V1 and V2");
image(x,y,inpoly(V4,X,Y),"x","y","V1 or V2");
image(x,y,inpoly(V5,X,Y),"x","y","V1 - V2");
image(x,y,inpoly(V6,X,Y),"x","y","V2 - V1");
image(x,y,inpoly(V7,X,Y),"x","y","V1 xor V2");
```

结果如下图所示

|
---|
|
|
|

注意：其他 2D 或 3D 对象 此命令仅适用于 2D 多边形。对于其他 2D 或 3D 对象，用户可以使用「网格顺序」来合并多个重叠对象。

---

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[polyor](./polyor.md)、[polydiff](./polydiff.md)、[polyxor](./polyxor.md)、[polyarea](./polyarea.md)、[centroid](./centroid.md)、[polyintersect](./polyintersect.md)、[inpoly](./inpoly.md)、[polygrow](./polygrow.md)、[网格顺序](https://optics.ansys.com/hc/en-us/articles/360034915233-Mesh-Order)
