<!--
Translator: Claude
Translation Date: 2026-02-03
Status: Completed
-->
# sort

对矩阵进行升序或降序排序。复数值按幅值然后按角度排序。对于更复杂的排序方法，请参阅sortmap函数。

此函数在2018a R6版本中引入。

**语法** | **描述**
---|---
out = sort(A); | 返回A的排序矩阵，按升序排列。复数值按幅值然后按角度排序。A被视为用于排序的线性数组，但out保留A的形状。通常该命令用于Nx1或1xN矩阵。
out = sort(A, ascending); | 可选的布尔参数默认设置为true。当为false时，排序按降序进行。

**示例**

此示例展示了简单的排序。对于更复杂的用法，请参阅sortmap。

```
A = [3, 4, 1, 7, 10, -1];
?B = sort(A);
?D = sort(A, false);
```

**另请参阅**

[ sortmap ](sortmap.html)
