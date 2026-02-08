# transpose

Transposes a 1D or 2D matrix.

| **Syntax**        | **Description**                                                                     |
| ----------------- | ----------------------------------------------------------------------------------- |
| y = transpose(x); | If x is an N x M matrix, then y will be M x N, where the entries are y(j,i)=x(i,j). |

**Example**

Simple example of how to transpose a 2D matrix.

```
?A = [1,2,3;4,5,6];
?AT = transpose(A); # transpose of A
result:
1  2  3  
4  5  6  
result: 
1  4  
2  5  
3  6  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ ctranspose ](./ctranspose.md) , [ reshape ](./reshape.md) , [ flip ](./flip.md) ,
[ permute ](./permute.md) , [ size ](./size.md)
