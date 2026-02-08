# erfinv

Calculates the inverse error function as defined by the following equation:

$$ \\operatorname{erfinv}(z)=\\sum\_{k=0}^{\\infty} \\frac{c\_{k}}{2
k+1}\\left(\\frac{\\sqrt{\\pi}}{2} z\\right)^{2 k+1} $$

| **Syntax**     | **Description**                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| out=erfinv(z); | Returns the inverse error function of z where z is a scalar number or matrix of scalar numbers. For inputs outside the interval (-1, 1), erfinv returns NaN. |

**Example**

Plot the inverse error function for -1

```
z=[-0.99:0.01:0.99];
erfinv_z = erfinv(z);
plot(z,erfinv_z,"z","erfinv");
```

The following figure shows the plot created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ erf ](./erf.md) ,
[ erfc ](./erfc.md) , [ erfcinv ](./erfcinv.md)
