# sum

Returns the sum of elements in a matrix.

| **Syntax**      | **Description**                                           |
| --------------- | --------------------------------------------------------- |
| out = sum(x);   | Sum of all the elements in matrix x, over all dimensions. |
| out = sum(x,n); | Sum elements of x over the specified dimension n.         |

**Example**

This example shows how you can sum all the elements of a matrix or just the elements
over a specified dimension.

```
?a = [1,2;3,4]; # define a 2x2 matrix
result: 
1 2 
3 4 
?sum(a); # sum all elements
result: 
10
?sum(a,2); # sum over the second dimension only
result: 
3 
7  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ integrate ](./integrate.md) , [ mean ](./mean.md) , [ prod ](./prod.md)
