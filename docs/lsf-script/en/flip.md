# flip

Flips (reverses the order of) a matrix along a given dimension.

| **Syntax**        | **Description**                             |
| ----------------- | ------------------------------------------- |
| C = flip(A, dim); | Flips the matrix A along the dimension dim. |

**Example**

Reverse the order of rows and columns of a 2x3 matrix.

```
?A=[1,2,3;4,5,6];
?B=flip(A,1); # flip (reverse) order of rows
?B=flip(A,2); # flip (reverse) order of columns 
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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ size ](./size.md) ,
[ length ](./length.md) , [ pinch ](./pinch.md) , [ transpose ](./transpose.md) ,
[ reshape ](./reshape.md) , [ permute ](./permute.md)
