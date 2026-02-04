<!-- Translated: 2026-02-03 -->
<!-- Original: transpose -->

# transpose

转置一维或二维矩阵。

**语法** | **描述**
---| ---
y = transpose(x); | 如果 x 是 N x M 矩阵，则 y 将是 M x N，其中条目为 y(j,i)=x(i,j)。

**示例**

二维矩阵转置的简单示例。

```lsf
?A = [1,2,3;4,5,6];
?AT = transpose(A); # transpose of A
result:
1  2  3
4  5  6
result:
1  4
2  5
3  6
```

**另见**

[命令列表](./list-of-commands.md)、[ctranspose](./ctranspose.md)、[reshape](./reshape.md)、[flip](./flip.md)、[permute](./permute.md)、[size](./size.md)
