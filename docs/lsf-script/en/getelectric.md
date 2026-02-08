# getelectric

Returns the sum of the amplitude squares for all electric field components, i.e. it
returns |Ex| 2 +|Ey| 2 +|Ez| 2 .

| **Syntax**                           | **Description**                                                                                                                                                                                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getelectric( "monitorname");   | Returns                                                                                                                                                                                                                                                                                 |
| getelectric( "monitorname", option); | The optional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. |

**Examples**

This example creates an image plot of |E|^2 for a z-normal frequency monitor in the x-y
plane.

```
E2=getelectric("output");
x=getdata("output","x");
y=getdata("output","y");
image(x,y,E2);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ getdata ](./getdata.md)
, [ getmagnetic ](./getmagnetic.md) , [ cwnorm ](./cwnorm.md) , [ nonorm ](./nonorm.md)
