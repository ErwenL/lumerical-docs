# erfcinv

Calculates the inverse complementary error function as defined by the following equation
in relationship to the inverse error function erfinv :

$$ erfcinv(1-z)=erfinv(z) $$

| **Syntax**      | **Description**                                                                                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out=erfcinv(z); | Returns the inverse complementary error function of z where z is a scalar number or matrix of scalar numbers. For inputs outside the interval (0, 2), erfcinv returns NaN. |

**Example**

Plot the inverse complementary error function for 0

```
z=0.01:0.05:1.99; 
erfcinv_z = erfcinv(z);
plot(z,erfcinv_z,"z","erf");
```

The following figure shows the plot created by the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ erf ](./erf.md) ,
[ erfc ](./erfc.md) , [ erfinv ](./erfinv.md)
