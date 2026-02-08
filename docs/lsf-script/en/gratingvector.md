# gratingvector

Returns the relative strength of all physical grating orders where vector field
information is returned in Cartesian coordinates. This is useful when studying the
polarization effects. The data is normalized such that the sum of |Ex|^2+|Ey|^2+ |Ez|^2
over all grating orders equals 1. See the
[grating](https://optics.ansys.com/hc/en-us/articles/360034927213) function
documentation for information on interpreting N, M, ux, uy for various monitor
orientations.

3D simulations: Data is returned in a NxMxPx3 matrix where N,M are the number of grating
orders. P is the number of frequency points. The third dimension is Ex, Ey, Ez.

2D simulations: Data is returned in a NxPx3 matrix where N is the number of grating
orders. P is the number of frequency points. The second dimension is Ex, Ey, Ez.

The results are returned on hemisphere 1m away. For more information on the basis used
please refer to
[Understanding field polarization in far field projections](https://optics.ansys.com/hc/en-us/articles/360034914753)

| **Syntax**                                          | **Description**                                                                                           |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| out = gratingvector( "mname", f, index, direction); | Returns the strength of all physical grating orders from monitorname. Output is in Cartesian coordinates. |

| **Parameter** |          | **Default value**           | **Type** | **Description**                                                                |
| ------------- | -------- | --------------------------- | -------- | ------------------------------------------------------------------------------ |
| mname         | required |                             | string   | name of the monitor from which far field is calculated                         |
| f             | optional | 1                           | vector   | Index of the desired frequency point. This can be a single number or a vector. |
| index         | optional | value at monitor center     | number   | The index of the material to use for the projection.                           |
| direction     | optional | direction of max power flow | number   | Direction: this can be +1 or -1.                                               |

**Examples**

This 2D result shows that gratingvector gives the same result as the grating function
when we calculate |Ex|^2+|Ey|^2+ |Ez|^2.

```
?Gv=gratingvector("monitor1");
result: 
0.0476203+0.219991i 0.0509014+0.235148i 0+0i 
0.0794422+0.373053i 0.0173684+0.0815601i 0+0i 
0.638599+0.42186i -0.203101-0.134169i 0+0i 
0.0335526+0.172349i -0.0480246-0.246687i 0+0i 
?sum(abs(Gv)^2,2);
result: 
0.108549 
0.152433 
0.645027 
0.093991 
?G=grating("monitor1");
result: 
0.108549 
0.152433 
0.645027 
0.093991 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ grating ](./grating.md)
, [ gratingn ](./gratingn.md) , [ gratingperiod1 ](./gratingperiod1.md) ,
[ gratingbloch1 ](./gratingbloch1.md) , [ gratingu1 ](./gratingu1.md) ,
[ gratingangle ](./gratingangle.md) , [ gratingpolar ](./gratingpolar.md) ,
[ Far field projections - Field polarization ](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)
