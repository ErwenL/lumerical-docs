# farfieldfilter

Sets or gets the filter width for far field filter which is used to remove ripples in
the far field projection due to clipping of the near fields. It should be used when the
near fields at the edge of the monitor are small but not precisely zero.

The bumpy blue line of the figure shows the near field electric field that will be used
for a far field projection. In this case, the field does not go to zero at the edge of
the monitor, which will lead to ripples in the far field projection. The green line
shows the spatial filter that will be applied to the fields, ensuring they go to zero.
The filter parameter defines the width of the filter by the following formula:
α=(a)/(a+b).

| **Syntax**            | **Description**                                                                                                                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = farfieldfilter; | Get the current far field filter setting.                                                                                                                                                                                                          |
| farfieldfilter(α);    | Set the current far field filter setting. α=(a)/(a+b). The far field filter has a single input parameter, which is a number between 0 and 1. By default, it is 0, which turns the filter off. This filter is applied to all far field projections. |

## Note: Periodic structures The far field filter option should not be used for periodic structures. Set it to zero when using the 'assume periodic' option.

**Example**

[ Far field projection - spatial filtering ](https://optics.ansys.com/hc/en-us/articles/360034394314-FFP-Spatial-filtering)

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield2d ](./farfield2d.md) , [ farfield3d ](./farfield3d.md)
