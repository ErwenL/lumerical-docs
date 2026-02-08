# svd

Returns a 3-cell array with the singular value decomposition of a matrix A. The command
supports real and complex A.

| **Syntax**          | **Description**                                                                                                                                                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [U,S,V\*] = svd(A); | Returns a 3-cell array with the singular value decomposition of matrix A. S is a diagonal matrix of the same dimension as A, with non-negative diagonal elements in decreasing order. U and V\* are unitary matrices (V\* is the conjugate transpose of V). If M = svd(A), then A = mult( M{1}, M{2}, M{3} ). |

**Example**

Find the single value decomposition of a square matrix A and of a rectangular matrix B.

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
-1  4.44089e-017  
4.44089e-017  1  
result: 
2.5  0  0  
0  2.5  0  
result: 
-0.6  -0.8  0  
-0.8  0.6  0  
0  0  1  
result: 
2.22045e-016  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ eig ](./eig.md) ,
[ ctranspose ](./ctranspose.md) , [ mult ](./mult.md)
