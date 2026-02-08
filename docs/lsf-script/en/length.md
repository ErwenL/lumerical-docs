# length

Returns the number of elements in a matrix. If the argument is a string, it will return
the length of the string.

| **Syntax**     | **Description**                                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| y = length(x); | y the number of elements in a matrix. For example, if x is an n by m matrix, y = length( x ) = n * m. |

**Example**

Find the length of a matrix and of a string.

```
x=matrix(2,3,3);
?y=length(x);
result: 
18  

?length("hello");
result:
5  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ size ](./size.md)
