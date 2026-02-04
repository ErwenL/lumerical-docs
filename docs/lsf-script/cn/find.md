<!-- Translation completed: 2026-02-04 -->
<!-- Original command: find -->

# find

在矩阵中搜索满足某些条件的项。返回这些值的索引。对于多维矩阵，find函数仍将返回单个索引。当在循环中使用find的输出时，这非常有用。

**语法** | **描述**
---|---
out = find(x,n); | 返回x中与值'n'最接近的第一个元素的索引。
out = find(x==n); | 返回x中值恰好等于'n'的所有元素的索引。如果返回0，表示没有找到值为'n'的元素。
out = find(x); | 返回x中所有非零元素的索引。如果返回0，表示没有找到非零值的元素。
out = find(x>n); | 返回x中所有大于'n'的值的索引。
out = find((x>=n) & (x<m)) | 返回x中所有大于或等于'n'且小于'm'的值的索引。

**示例**

以下两个示例展示了find函数的基本输出。

```lsf
x = -2:7;
?find(x>5);
result: 
9 
10
x = linspace(0,10e-6,100);
?x( find(x,5e-6) );
result: 
5.05051e-006 
```

**另请参阅**

[命令列表](List_of_commands.md)、[pinch](pinch.md)、[findpeaks](findpeaks.md)、[integrate](integrate.md)、[length](length.md)、[size](size.md)
