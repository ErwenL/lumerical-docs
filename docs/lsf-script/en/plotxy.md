# plotxy

Creates line plots. In particular, this function is used when the data sets are sampled
on different position vectors.

| **Syntax**                                          | **Description**                                                                                                                                                                        |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = plotxy(x,y);                                  | Creates a plot of y vs x, y and x are both 1D vectors with the same length. The figure number is returned.                                                                             |
| plotxy(x1,y1,x2,y2,xn,yn);                          | Creates a plot with multiple curves. The xn-yn pairs must have the same length, but x1, x2, and xn can have different start-end values and resolutions. The figure number is returned. |
| plotxy(x1,y1,x2,y2, "x label", "y label", "title"); | Creates line plots with axis labels and a title, returns the figure number.                                                                                                            |

**Example**

This example will generate a figure with two functions with different resolutions:

```
x1=linspace(0,2*pi,15);
y1=sin(x1);
x2=linspace(1,pi,3);
y2=x2/2;
plotxy(x1,y1,x2,y2,"x","y","title");
legend("y1=sin(x1) - 15 pts","y2=x2/2 - 3 pts");
```

The following figure shows the output of the the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ plot ](./plot.md) ,
[ legend ](./legend.md) , [ image ](./image.md) , [ closeall ](./closeall.md) ,
[ setplot ](./setplot.md) , [ exportfigure ](./exportfigure.md) ,
[ visualize ](./visualize.md) , [ vectorplot ](./vectorplot.md) ,
[ holdon ](./holdon.md)
