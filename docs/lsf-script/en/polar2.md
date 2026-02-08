# polar2

Creates polar plots. In particular, this function is used when the data sets are sampled
on different arrays of angle values.

| **Syntax**                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = polar2(theta,rho)                                     | Creates a polar coordinate plot of the angle theta versus the radius rho. theta is the angle from the x-axis to the radius vector specified in radians; rho is the length of the radius vector. Theta and rho can be vectors of the same length, or if the length of theta is n, then rho can be a nxm matrix, which corresponds to m sets of rho values. The figure number is returned. |
| polar2(theta1,rho1,theta2,rho2)                             | Creates a plot with two curves. The two data sets can be sampled on different theta vectors.                                                                                                                                                                                                                                                                                             |
| polar2(theta,rho,"x label", "y label", "title")             | Creates a plot of y vs x with axis labels and a title, returns the figure number.                                                                                                                                                                                                                                                                                                        |
| polar2(theta,rho,"x label", "y label", "title", "options"); | Creates a plot with desired options. Options can be be                                                                                                                                                                                                                                                                                                                                   |

- greyscale
- polar (same as the polar script command)
- any comma separated list of the above

Returns the figure number.

**Example**

Plot in polar coordinates two different data sets.

```
theta1 = linspace(0,2*pi,100);
r1 = cos(theta1);
theta2 = linspace(0,pi,50);
r2 = sin(theta2);
polar2(theta1,r1,theta2,r2);
```

The following figure shows the output of the the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ polar ](./polar.md) ,
[ legend ](./legend.md) , [ image ](./image.md) , [ closeall ](./closeall.md) ,
[ setplot ](./setplot.md) , [ exportfigure ](./exportfigure.md) ,
[ polarimage ](./polarimage.md) , [ plot ](./plot.md)
