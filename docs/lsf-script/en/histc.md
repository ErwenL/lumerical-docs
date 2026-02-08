# histc

Creates a histogram plot.

| **Syntax**                                  | **Description**                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| out = histc(y);                             | Creates a histogram plot of y. Returns the figure number.                                             |
| histc(y,n);                                 | Creates a histogram plot of y, using n bins. Returns the figure number.                               |
| histc (y,n, "x label", "y label", "title"); | Creates a histogram plot of y, using n bins, with axis labels and a title. Returns the figure number. |

**Example**

These are scripts for creating simple histograms.

```
#Creates a histogram plot of y.
y = randmatrix(1,10);
y = y*10;
out = histc(y);
#Creates a histogram plot of y, using n bins.
#Returns the figure number.
y = randmatrix(1,10);
y = y*10;
n = 5;
out = histc(y,n);
#Creates a histogram plot of y, using n bins, with axis labels and a title.
histc (y,n, "x label", "y label", "title");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ histogram ](./histogram.md) , [ legend ](./legend.md) , [ plot ](./plot.md) ,
[ closeall ](./closeall.md) , [ visualize ](./visualize.md)
