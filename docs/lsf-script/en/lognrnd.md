# lognrnd

Generates a log-normal distributed random number. In order to reset the generator seed
use the command randreset.

| **Syntax**                   | **Description**                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| out = lognrnd (mean,stddev); | Generates a lognormal distributed random number with user defined mean value and standard deviation. |

**Example**

This example shows how to create an histogram of a log-normal distribution.

```
n = 1000;
y = matrix(n);
mean_val = 1;
std_dev = 0.25;
for (i=1:n){
    y(i) = lognrnd(mean_val, std_dev);
}
histc(y);
```

The histogram will look similar to the following one.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ randreset ](https://optics.ansys.com/hc/en-us/articles/360034406234-randreset) ,
[ randn ](./randn.md) , [ histc ](./histc.md)
