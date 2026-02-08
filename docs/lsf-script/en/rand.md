# rand

Generates a uniform random number between 0 and 1. In order to reset the generator seed
use the command randreset.

| **Syntax**                  | **Description**                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| out = rand;                 | Generates a uniform random number between 0 and 1.                                                                                  |
| out = rand(min,max);        | Generates a random number between min and max. By default, min and max are 0 and 1 respectively.                                    |
| out = rand(min,max,option); | option = 1: output is a double precision number between min and max (default) option = 2: output is an integer between min and max. |

**Example**

Simple examples of the output of rand.

```
?rand;
result: 
0.528733 
?rand(0,10,1);
result: 
9.33399  
?rand(0,10,2);
result: 
5 
```

Generate two Gaussian random numbers (Y1 and Y2) using the polar form of the Box Muller
transform.

```
# choose mean and variance
mean_value = 0;
variance_value = 1;
w=1;
for(0;(w>1)|(w==1);0){ # while w>=1
  x1 = 2*rand - 1;
  x2 = 2*rand - 1;
  w = x1^2 + x2^2;
}
w = sqrt( (-2*log( w ) ) / w );
y1 = x1 * w;
y2 = x2 * w;
?Y1 = mean_value + sqrt(variance_value) * y1;
?Y2 = mean_value + sqrt(variance_value) * y2;
result: 
0.198101  
result: 
-2.05023   
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ randreset ](https://optics.ansys.com/hc/en-us/articles/360034406234-randreset) ,
[ randmatrix ](./randmatrix.md) , [ randn ](./randn.md)
