<!-- Translation completed: 2026-02-03 -->
<!-- Original command: svd -->

# svd

返回包含矩阵A奇异值分解的3元胞数组。该命令支持实数和复数矩阵A。

**语法** | **描述**
---|---
`[U,S,V*] = svd(A);` | 返回包含矩阵A奇异值分解的3元胞数组。S是与A同维度的对角矩阵，对角线元素为非负数且按降序排列。U和V*是酉矩阵(V*是V的共轭转置)。如果M = svd(A)，则A = mult( M{1}, M{2}, M{3} )。

**示例**

求方阵A和矩形矩阵B的奇异值分解。

```
A = [ 1.5, 2,0; -2, 1.5,0; 0,0,1.2];
M=svd(A);
?U = M{1};
?S = M{2};
?V_ctranspose = M{3};
?max(abs( mult(U,S,V_ctranspose)-A)); # this should be zero
result:
-0.6 0.8 0 
0.8 0.6 0 
-0 -0 1 
result: 
2.5 0 0 
0 2.5 0 
0 0 1.2 
result: 
-1 -0 -0 
0 1 -0 
0 0 1 
result: 
2.22045e-016 
B = [ 1.5, 2,0; -2, 1.5,0];
M=svd(B);
?U = M{1};
?S = M{2};
?V_ctranspose = M{3};
?max(abs( mult(U,S,V_ctranspose)-B)); # this should be zero
result: 
-1  4.44089e-017  
4.44089e-017  1  
result: 
2.5  0  0  
0  2.5  0  
result: 
-0.6  -0.8  0  
-0.8  0.6  0  
0  0  1  
result: 
2.22045e-016
```

**参见**

[命令列表](List_of_commands.md), [eig](eig.md), [ctranspose](ctranspose.md), [mult](mult.md)
