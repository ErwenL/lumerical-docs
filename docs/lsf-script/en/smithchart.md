# smithchart

Plots impedance values in a Smith chart. The default impedance used for normalization is
50 Ohms; this can be modified in the plot settings once the plot has been created.

| **Syntax**                                            | **Description**                                                                                                                                                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = smithchart(Z);                                  | Creates a curve in a Smith chart with the impedance values in the array Z. The array Z must be of the form NX1 or 1XN.                                                                    |
| out = smithchart(Z1,Z2,Z3);                           | Creates three curves in a Smith chart with the impedance values in the arrays Z1, Z2 and Z3. Each array must be of the form NX1 or 1XN, but they do not have to be of the same dimension. |
| out = smithchart(Z, "title", "aspect ratio", norm_Z); | Creates a Smith chart with a title, a given aspect ratio and a normalized impedance norm_Z. The aspect ratio must be string that is either "1:1" or "fill scene".                         |

**Example**

Create a simple Smith chart

```
Z1 = 50*(3+1i*linspace(-50,50,101)); # re(Z) = 3 circle
Z2 = 50*(linspace(0,50,101)+0.75i); # im(Z) = 0.75 line
smithchart(Z1,Z2,"Example of Smith chart", "1:1", 50); # Normalized impedance 50 Ohms
#The plot properties can also be set using setplot:
smithchart(Z1,Z2);
setplot("title", "Example of Smith chart");
setplot("aspect ratio", "1:1");
setplot("normalized impedance", 50);
```

The following figure shows the output of the example code.

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md), [polar](./polar.md),
[ setplot ](./setplot.md)
