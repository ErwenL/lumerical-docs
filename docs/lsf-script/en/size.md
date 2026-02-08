# size

Returns the size of a matrix.

| **Syntax**     | **Description**                                                                  |
| -------------- | -------------------------------------------------------------------------------- |
| y = size(x);   | y is a matrix which shows the dimensions of x.                                   |
| y = size(x,n); | n is an optional parameter to get the size of the matrix in a specific dimension |

**Example**

Check the dimensions of a matrix.

```
x=matrix(2,3,3);
?y=size(x);
result: 
2 3 3 
?size(x,2);
result: 
3  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ flip ](./flip.md) , [ transpose ](./transpose.md)
