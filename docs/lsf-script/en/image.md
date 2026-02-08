# image

Creates 2D image plots.

| **Syntax**                                              | **Description**                                                                                                                                                     |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = image(x,y,z);                                     | Creates a 2D image plot of the data in z. If x is of dimension N x 1 and y is of dimension M x 1, then z must be of dimension N x M. The figure number is returned. |
| image(x,y,z, "x label", "y label", "title");            | Creates a 2D image plot with axis labels and a title. The figure number is returned.                                                                                |
| image(x,y,z, "x label", "y label", "title", "options"); | Creates a 2D image plot with axis labels and options, options can be                                                                                                |

- logplot
- polar
- red2blue
- any comma separated list of the above

**Example**

This example generates a figure of the 2D function pic(x,y)=sin(x)+sin(y).

```
x=linspace(0,10,100);
y=linspace(0,10,100);
x2=sin(x);
y2=sin(y);
pic=meshgridx(x2,y2)+meshgridy(x2,y2);
image(x,y,pic,"","","","logplot");
image(x,y,pic,"","","","logplot,red2blue");
```

The following figures show the output of the example code.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ plot ](./plot.md) ,
[ closeall ](./closeall.md) , [ setplot ](./setplot.md) ,
[ exportfigure ](./exportfigure.md) , [ visualize ](./visualize.md) ,
[ polarimage ](./polarimage.md) , [ vectorplot ](./vectorplot.md)
