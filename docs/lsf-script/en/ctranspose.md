# ctranspose

Transposes a 1D or 2D matrix and takes the complex conjugate of each element. The
resulting matrix is the conjugate transpose or Hermitian transpose.

| **Syntax**         | **Description**                                                                        |
| ------------------ | -------------------------------------------------------------------------------------- |
| y = ctranspose(x); | If x is an N x M matrix, then y will be M x N, where the entries are y(j,i)=x(i,j) * . |

**Example**

Simple example of how to find the conjugate transpose of a 2D complex matrix.

```
?B = [1+3i,2,3+7i;4,5+2i,6];
?BCT = ctranspose(B); # conjugate transpose of A
result:
1+3i  2+0i  3+7i  
4+0i  5+2i  6+0i  
result: 
1-3i  4+-0i  
2+-0i  5-2i  
3-7i  6+-0i  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ transpose ](./transpose.md)
