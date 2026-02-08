# inv

Calculates the inverse of a matrix. The matrix has to be invertible.

| **Syntax**         | **Description**                                                                 |
| ------------------ | ------------------------------------------------------------------------------- |
| out = inv(A)       | Returns the inverse of matrix A.                                                |
| out = inv(A, tol); | Returns the Moore-Penrose pseudoinverse of matrix A, with a tolerance of "tol". |

**Examples**

Invert a matrix and multiply by original matrix to get the identity.

```
A= [ 1, 2; 3, 4];
B= inv(A);
?mult(B,A);  # This should return the identity matrix
result: 
1 0 
0 1  
```

Derive the Moore-Penrose pseudoinverse of the same matrix, with a tolerance of 0.1.

```
?C = inv(A, 0.1);  
result:   
0.0426428 0.0963963   
0.0605104 0.136787 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ = ](./minus.md) ,
[ == ](./minus.md) , [ != ](./minus.md) , [ \<= ](./minus.md) , [ >= ](./minus.md) ,
[ < ](./minus.md) , [ > ](./minus.md) , [ & ](./minus.md) , [ and ](./and.md) ,
[ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md) ,
[ eig ](./eig.md) , [ mult](./mult.md),
[solve](https://optics.ansys.com/hc/en-us/articles/360041139833)
