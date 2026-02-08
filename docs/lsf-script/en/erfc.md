# erfc

Calculates the complementary error function as defined by the following equation:

$$ \\operatorname{erfc}(z)=1-\\frac{2}{\\sqrt{\\pi}} \\int\_{0}^{z} \\exp
\\left(-t^{2}\\right) d t $$

| **Syntax**   | **Description**                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| out=erfc(z); | Returns the complementary error function of z where z is a scalar number or matrix of scalar numbers. |

**Example**

Plot the complementary error function from z=-5 to 5.

```
z=linspace(-5,5,50); # generate vector of numbers from -5 to 5 with 50 points
erfc_z = erfc(z);
plot(z,erfc_z,"z","erfc");
```

The following figure shows the plot created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ erf ](./erf.md) ,
[ erfinv ](./erfinv.md) , [ erfcinv ](./erfcinv.md)
