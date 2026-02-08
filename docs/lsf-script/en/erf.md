# erf

Calculates the error function as defined by the following equation:

$$ \\operatorname{erf}(z)=\\frac{2}{\\sqrt{\\pi}} \\int\_{0}^{z} \\exp
\\left(-t^{2}\\right) d t $$

| **Syntax**  | **Description**                                                                     |
| ----------- | ----------------------------------------------------------------------------------- |
| out=erf(z); | Returns error function of z where z is a scalar number or matrix of scalar numbers. |

**Example**

Plot the error function from z=-5 to 5.

```
z=linspace(-5,5,50); # generate vector of numbers from -5 to 5 with 50 points
erf_z = erf(z);
plot(z,erf_z,"z","erf");
```

The following figure shows the plot created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ erfc ](./erfc.md) ,
[ erfinv ](./erfinv.md) , [ erfcinv ](./erfcinv.md)
