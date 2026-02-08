# imag

Returns the imaginary part of a number or matrix.

| **Syntax**     | **Description**                  |
| -------------- | -------------------------------- |
| out = imag(x); | Returns the imaginary part of x. |

**Example**

Calculate the imaginary part of numbers in an array.

```
?x=linspace(0, 2+1i,2);
result: 
0+0i 
2+1i 
?imag(x);
result: 
0 
1
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ real ](./real.md) ,
[ conj ](./conj.md)
