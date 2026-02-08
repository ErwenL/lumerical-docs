# almostequal

Performs an almost-equal comparison. When using floating point numbers (rather than
integers), two values that are meant to be equal may not be exactly equal due to
rounding errors that are always present in floating point calculations. In such cases,
the almostequal function can be useful. For complex numbers, A and B, almostequal
function returns true only when both the real and imaginary parts, evaluated separately,
are true.

| **Syntax**                                             | **Description** |
| ------------------------------------------------------ | --------------- |
| out = almostequal(A, B);                               | Returns 1 if    |
| out = almostequal(A, B, relative diff);                | Returns 1 if    |
| out = almostequal(A, B, relative diff, absolute diff); | Returns 1 if    |

**Examples**

This example shows the usage of the almostequal function.

```
A=[1,2];
B=[1,1];
?almostequal(A,B);
result: 
1 0 
?almostequal(A,B,0.01,2);
result: 
1 1 
 
?almostequal(1,2,1);
result: 
1   
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ = ](./minus.md) ,
[ == ](./minus.md) , [ != ](./minus.md) , [ \<= ](./minus.md) , [ >= ](./minus.md) ,
[ < ](./minus.md) , [ > ](./minus.md) , [ & ](./minus.md) , [ and ](./and.md) ,
[ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md)
