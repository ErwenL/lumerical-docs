# conj

Returns the complex conjugate of a number or matrix.

| **Syntax**     | **Description**                     |
| -------------- | ----------------------------------- |
| out = conj(x); | Returns the complex conjugate of x. |

**Example**

Calculate the complex conjugate of numbers in an array.

```
?x=linspace(0, 2+1i,2);
result: 
0+0i 
2+1i 
?conj(x);
result: 
0+0i 
2-1i 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ real ](./real.md) ,
[ imag ](./imag.md)
