# polarimage

Creates 2D polar image plots. This is typically used to plot far field data.

| **Syntax**              | **Description**                                              |
| ----------------------- | ------------------------------------------------------------ |
| polarimage(ux,uy,data); | Creates a 2D image plot. data must be of dimension N x M and |

- ux is of dimension N x 1, where ux goes from -1 to 1
- uy is of dimension M x 1, where uy goes from -1 to 1

out = polarimage(ux,uy,data, "x label", "y label", "title"); | Creates a 2D image plot
with axis labels Optionally returns the figure number.\
polarimage(ux,uy,data, "x label", "y label", "title", "options"); | Creates a 2D image
plot with axis labels and options, options can be

- logplot

**Example**

This example generates an image of a simple 2D Gaussian function.

```
ux=linspace(-1,1,51);
uy=linspace(-1,1,61);
Ux=meshgridx(ux,uy);
Uy=meshgridy(ux,uy);
data = exp( 1-Ux^2-Uy^2);
# plot data with both the image and polarimage script functions
image(ux,uy,data,"ux","uy","Image plot");   
polarimage(ux,uy,data,"ux","uy","Polar Image plot");
```

The following figure shows the resulting figures.

This example shows how this function might be used with the far field projection
functions.

```
m="monitor1";   # monitor name
ux=farfieldux(m); # position vectors
uy=farfielduy(m);
E2=farfield3d(m); # Far field E2 data
polarimage(ux,uy,E2,"ux","uy","far field |E|^2");  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ plot ](./plot.md) ,
[ polar ](./polar.md) , [ image ](./image.md) , [ closeall ](./closeall.md) ,
[ setplot ](./setplot.md) , [ exportfigure ](./exportfigure.md) ,
[ visualize ](./visualize.md) ,
[ List of commands ](../lsf-script-commands-alphabetical.md)
