<!-- Translation completed: 2026-02-04 -->
<!-- Original command: amax -->

# amax

返回矩阵指定维度中的最大值。对于复数，仅考虑实部。

**语法** | **描述**
---|---
out = amax(x,n); | 矩阵x的指定维度n中的最大值。

**示例**

查找矩阵第一维度的最大值：

```lsf
A = randmatrix(5,4);
B = amax(A,1); # 向量长度4，B[i] = max(A(1:5,i))
```

**另请参阅**

[命令列表](List_of_commands.md)、[min](min.md)、[max](max.md)、[abs](abs.md)、[mean](mean.md)、[amin](amin.md)
