# polygrow

扩展或收缩多边形。生成的多边形将具有与多边形 V 相同的顶点数和顺序。请考虑在 使用 polygrow 之前使用 polyclean。

多边形顶点包含在一个 Nx2（或 2xN）维的矩阵中，其中 N \\(\\ge\\) 3 是顶点的数量。维度 2 对应 x 和 y 位置。例如，边长为 1 的正方形可以描述为 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]。

**语法** | **描述**
---|---
polygrow(V, delta, {"tolerance": tol_value, "legacy": true/false}) | 返回按 delta 扩展后的新多边形的顶点。要收缩多边形，请使用 delta < 0。

- 对于逆时针顺序的顶点且 delta > 0，边向右移动 delta（正数扩展，负数收缩）
- 容差用于识别接缝（不扩展）和蝴蝶结顶点（固定不动）。将 legacy 选项设置为 "true" 以跳过此检查。
- 会尝试防止尖锐角处的自相交。
- delta 值可以是标量或矩阵（结果将为多边形或多边形单元数组）

**示例**

以下示例显示边长为 1 的正方形的顶点在所有边上扩展 0.1 容差为 1e-15 的情况。将 "legacy" 值设置为 "false" 可以识别接缝和蝴蝶结顶点。

```powershell
V = [ 0,0; 1,0; 1,1; 0,1];
?polygrow(V, 0.1, {"tolerance": 1e-15, "legacy": false});

结果：
-0.1 -0.1
 1.1 -0.1
 1.1  1.1
-0.1  1.1
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[polyclean](./polyclean.md)、[polyarea](./polyarea.md)、[centroid](./centroid.md)、[polyintersect](./polyintersect.md)、[inpoly](./inpoly.md)、[polyand](./polyand.md)、[polyor](./polyor.md)、[polydiff](./polydiff.md)、[polyxor](./polyxor.md)
