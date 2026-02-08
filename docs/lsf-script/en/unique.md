# unique

Returns an array containing all the unique values in a matrix. In other words, this
command returns all the elements in a matrix without repeating them if they appear more
than once in the matrix.

| **Syntax**     | **Description**                                                |
| -------------- | -------------------------------------------------------------- |
| out=unique(a); | Returns an array containing all unique values in the matrix a. |

- This command is intended mainly for integer values.
- It still works for floating-point numbers, but this is within the precision used
  internally by the software so it might fail in cases where the difference between two
  numbers is very small (see example below).

**Example**

Define a matrix and display all the unique elements in the Script Prompt.

```
A = [1,2;2,3];  
?unique(A);  
result:   
1   
2   
3   
  
format long; # set the precision to 16 digits  
A= [2., 2.000000000000001; 3, 4.5];  
?unique(A);  
result:   
2.000000000000000   
2.000000000000001   
3.000000000000000   
4.500000000000000   
  
format short; # set the precision to 8 digits  
B= [2., 2.0000000000000001; 3, 4.5];  
?unique(B);  
result:   
2   
3   
4.5 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ uniquevertices ](./uniquevertices.md)
