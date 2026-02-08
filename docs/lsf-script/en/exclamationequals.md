# !=

Performs a logical not-equal-to comparison. Returns 1 if values are not equal. Returns 0
if values are equal. This operator can be used in matrix operations. This operators can
be used with complex numbers.

| **Syntax**  | **Description**                                                    |
| ----------- | ------------------------------------------------------------------ |
| out = a!=b; | If a is not equal to b, then out equals 1. Otherwise out equals 0. |

**Examples**

This example shows the usage of the "!=" comprison.

```
a=1:5;
b=1:5;
b(4)=5;
?out = a!=b;
result: 
0 
0 
0 
1 
0 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ == ](./minus.md) ,
[ almostequal ](./almostequal.md) , , [ = ](./minus.md) , , , [ & ](./minus.md) ,
[ and ](./and.md) , [ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) ,
[ ~ ](./minus.md)
