<!-- Translation completed: 2026-02-03 -->
<!-- Original command: sum -->

# sum

返回矩阵元素的和。

**语法** | **描述**
---|---
`out = sum(x);` | 矩阵x中所有元素在所有维度上的总和。
`out = sum(x,n);` | 矩阵x在指定维度n上的元素和。

**示例**

此示例展示如何对矩阵的所有元素求和，或仅对指定维度的元素求和。

```
?a = [1,2;3,4]; # define a 2x2 matrix
result: 
1 2 
3 4 
?sum(a); # sum all elements
result: 
10
?sum(a,2); # sum over the second dimension only
result: 
3 
7
```

**参见**

[命令列表](List_of_commands.md), [integrate](integrate.md), [mean](mean.md), [prod](prod.md)
