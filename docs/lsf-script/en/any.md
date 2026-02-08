# any

Returns 1 if any of the specified matrix entries are nonzero and returns 0 otherwise.

| **Syntax**      | **Description**                                                                       |
| --------------- | ------------------------------------------------------------------------------------- |
| out = any(A);   | Will return 1 if any of the A matrix entries are nonzero and will return 0 otherwise. |
| out = any(A,n); | n is an optional parameter to analyze entries in a specific dimension                 |

**Example #1**

The following is a simple example showing how to use this command.

```
a = [0,0,3,0];
b = [1,3;6,0.1];
d = [0;0;0;0];
?any(a);
?any(b);
?any(d);
result:
1
result:
1  
result: 
0  
?any(a,1);
result: 
0  
0  
1  
0 
```

**See Also**

[ all ](./all.md) , [ almostequal ](./almostequal.md)
