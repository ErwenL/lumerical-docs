# randn

Generates a normally distributed random number. In order to reset the generator seed use
the command randreset.

| **Syntax**                | **Description**                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| out = randn;              | Generates a normally distributed random number with mean 0 and standard deviation 1.                |
| out = randn(mean,stddev); | Generates a normally distributed random number with user defined mean value and standard deviation. |

**Example**

This example shows how to create an histogram of a normal distribution.

```
n = 1000;
y = matrix(n);
mean_val = 1;
std_dev = 0.25;
for (i=1:n){
    y(i) = randn(mean_val, std_dev);
}
histc(y);
```

The histogram will look similar to the following one.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ randreset ](https://optics.ansys.com/hc/en-us/articles/360034406234-randreset) ,
[ lognrnd ](./lognrnd.md) , [ randnmatrix ](./randnmatrix.md)
