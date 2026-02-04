<!-- Translation completed: 2026-02-04 -->
<!-- Original command: amin -->

# amin

返回矩阵指定维度中的最小值。对于复数，仅考虑实部。

**语法** | **描述**
---|---
out = amin(x,n); | 矩阵x的指定维度n中的最小值。

**示例**

查找矩阵第一维度的最小值：

```lsf
A = randmatrix(5,4);
B = amin(A,1); # 向量长度4，B[i] = min(A(1:5,i))
```

**另请参阅**

[命令列表](List_of_commands.md)、[min](min.md)、[max](max.md)、[abs](abs.md)、[mean](mean.md)、[amax](amax.md)
