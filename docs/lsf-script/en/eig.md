# eig

Finds the eigenvalue and/or eigenvector of a matrix. The matrix has to be square.

| **Syntax**                     | **Description**                                            |
| ------------------------------ | ---------------------------------------------------------- |
| out = eig(A); out = eig(A, 1); | Returns the eigenvalues of matrix A.                       |
| out = eig(A, 2);               | Returns the eigenvectors of matrix A.                      |
| out = eig(A, 3);               | Returns both the eigenvalues and eigenvectors of matrix A. |

**Example**

A simple example showing the different options for the results from the eigenvalue
calculation.

```
A = [ 1, 2; 2, 4];
?eig(A);
result: 
0 
5 
?eig(A,1);
result: 
0 
5 
?eig(A,2);
result: 
-0.894427 -0.447214 
0.447214 -0.894427 
?eig(A,3);
result(i,j,1):
0 0 
0 5 
result(i,j,2):
-0.894427 -0.447214 
0.447214 -0.894427 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ = ](./minus.md) ,
[ == ](./minus.md) , [ != ](./minus.md) , [ \<= ](./minus.md) , [ >= ](./minus.md) ,
[ < ](./minus.md) , [ > ](./minus.md) , [ & ](./minus.md) , [ and ](./and.md) ,
[ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md) ,
[ mult ](./mult.md) , [ permute ](./permute.md) , [ reshape ](./reshape.md) ,
[ inv ](./inv.md)
