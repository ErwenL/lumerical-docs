<!-- Translation completed: 2026-02-04 -->
<!-- Original command: pinch -->

# pinch

从矩阵中移除单例维度。

**语法** | **描述**
---|---
out = pinch(x); | 移除所有单例维度。例如，如果x是1x1x1xM维的矩阵，那么y=pinch(x)将返回Mx1矩阵，其中y(i) = x(1,1,1,i)。
pinch(x,i); | 移除指定维度。如果x是NxMxKxP矩阵，那么y=pinch(x,2)将返回NxKxP矩阵，其中y(i,j,k) = x(i,1,j,k)。
pinch(x,i,j); | 移除指定维度，但保留被移除维度的特定索引。如果x是NxMxKxP矩阵，那么y=pinch(x,2,4)将返回NxKxP矩阵，其中y(i,j,k) = x(i,4,j,k)。

**示例**

此示例展示了如何使用pinch从矩阵中移除单例维度。使用matrix命令创建6x1x4x1矩阵。对此矩阵应用pinch函数将移除两个单例维度，得到6x4矩阵。

```lsf
x=matrix(6,1,4,1);
?size(x);
result: 
6 1 4 1 
?size(pinch(x));
result: 
6 4 
```

**另请参阅**

[命令列表](List_of_commands.md)、[find](find.md)、[size](size.md)、[flip](flip.md)
