# finite

如果值是有限的则返回 1（真）。NaN 或 #1.INF 等数字返回 0（假）。

**语法** | **描述**
---|---
out = finite(x); | 返回与 x 大小相同的矩阵。对于 x 中有限的值，值为 1；对于 NaN 值，值为 0。

**示例**

此示例显示有限函数的不同输出。

```powershell
?finite([1/0, 2, -3.4]);
result:
0 1 1
```

**另请参阅**

[命令列表](../命令列表.md)、[lineintersect](./lineintersect.md)、[linecross](./linecross.md)