# mult

Performs matrix multiplication of two or more matrices. The dimensions of the matrices
have to match.

| **Syntax**          | **Description**                                                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = mult(A,B,...) | Returns the matrix multiplication of matrices A, B, C ... Dimension of matrices must match; for example, if A is an MxN matrix and B is a NXP matrix, mult(A,B) has dimensions MxP. |

**Example**

Find the matrix product of two matrices.

```
A = [ 1, 2; 2, 4];
B = [ 2, 5; -1, 3];
?mult(A,B);
result: 
0 11 
0 22 
?mult(A,B,[1;2]);
result: 
22 
44
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ = ](./minus.md) ,
[ == ](./minus.md) , [ != ](./minus.md) , [ \<= ](./minus.md) , [ >= ](./minus.md) ,
[ < ](./minus.md) , [ > ](./minus.md) , [ & ](./minus.md) , [ and ](./and.md) ,
[ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md) ,
[ eig ](./eig.md) , [ permute ](./permute.md) , [ reshape ](./reshape.md) ,
[ inv ](./inv.md)
