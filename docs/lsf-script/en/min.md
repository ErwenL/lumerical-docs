# min

Returns the minimum value in a matrix. For complex numbers, only the real part is
considered.

| **Syntax**    | **Description**                |
| ------------- | ------------------------------ |
| out = min(x); | The minimum value in matrix x. |

**Example**

A simple example showing how you can find the minimum of a real array.

```
?x=linspace(0,3,4);
result: 
0 
1 
2 
3 
?min(x);
result: 
0 
```

If the array has complex numbers only the real part is considered, as shown below.

```
?x = 3 + 4i;
?min(x);
?min(abs(x));
result: 
3+4i 
result: 
3 
result: 
5 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ max ](./max.md) ,
[ abs ](./abs.md) , [ mean ](./mean.md) , [ amax ](./amax.md) , [ amin ](./amin.md)
