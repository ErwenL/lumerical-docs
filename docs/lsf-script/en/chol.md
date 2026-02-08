# chol

Calculates the Cholesky lower triangular factorization or decomposition. For a given
matrix A, chol returns a lower triangular matrix L such that A is the matrix product of
L and its conjugate transpose. The matrix A can be real or complex but it must be
Hermitian and positive-definite.

| **Syntax**   | **Description**                                                                           |
| ------------ | ----------------------------------------------------------------------------------------- |
| L = chol(A); | Returns a lower triangular matrix L that satisfies the equation A = mult(L,ctranspose(L)) |

**Example**

Find the Cholesky decomposition of a 3x3 matrix.

```
?A = [4, 12, -16; 12, 37, -43; -16,-43,98];
?L = chol(A);
?mult(L,ctranspose(L)); #This should be the same as A
result: 
4  12  -16  
12  37  -43  
-16  -43  98  
result: 
2+0i  0+0i  0+0i  
6+0i  1+0i  0+0i  
-8+0i  5+0i  3+0i  
result: 
4+0i  12+0i  -16+0i  
12+0i  37+0i  -43+0i  
-16+0i  -43+0i  98+0i  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ mult ](./mult.md) ,
[ ctranspose ](./ctranspose.md)
