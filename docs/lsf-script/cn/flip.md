# flip

沿给定维度翻转（反转顺序）矩阵。

**语法** | **描述**
---|---
C = flip(A, dim); | 沿维度 dim 翻转矩阵 A。

**示例**

反转 2x3 矩阵的行和列的顺序。

```powershell
?A=[1,2,3;4,5,6];
?B=flip(A,1); # 翻转（反转）行的顺序
?B=flip(A,2); # 翻转（反转）列的顺序
result:
1 2 3
4 5 6
result:
4 5 6
1 2 3
result:
3 2 1
6 5 4
```

**另请参阅**

[命令列表](../命令列表.md)、[size](./size.md)、[length](./length.md)、[pinch](./pinch.md)、[transpose](./transpose.md)、[reshape](./reshape.md)、[permute](./permute.md)