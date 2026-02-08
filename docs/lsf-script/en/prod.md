# prod

Returns the product of elements in a matrix.

| **Syntax**       | **Description**                                               |
| ---------------- | ------------------------------------------------------------- |
| out = prod(x);   | Product of all the elements in matrix x, over all dimensions. |
| out = prod(x,n); | Product elements of x over the specified dimension n.         |

**Example**

This example shows how you can multiply all the elements of a matrix or just the
elements over a specified dimension.

```
?a = [1,2;3,4]; # define a 2x2 matrix
result: 
1 2 
3 4 
?prod(a); # multiply all elements
result: 
24
?prod(a,2); # muliply over the second dimension only
result: 
2
12
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ integrate ](./integrate.md) , [ mean ](./mean.md) , [ sum ](./sum.md)
