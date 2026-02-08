# farfieldpolar2d

Projects a given power or field profile monitor or a rectilinear dataset to the far
field to a 1 meter radius semi-circle. This is similar to the farfield2d script command
except the complex electric fields are returned, rather than field intensity. The data
is returned as matrix of NxP if one frequency point is projected, or NxPx3 when multiple
frequency points are projected where N is the resolution of the far field projection, P
is the number frequency points projected, and the last index refers to E r , E θ and E z
, in cylindrical coordinates. For TM simulations, this function gives precisely the
result of farfieldvector2d because the only non-zero field component is Ez.

| **Syntax**                           | **Description**                                                          |
| ------------------------------------ | ------------------------------------------------------------------------ |
| out = farfieldpolar2d( "mname",...); | Returns the polar complex electric fields. Same arguments as farfield2d. |
| out = farfieldpolar2d( dataset,...); | Returns the polar complex electric fields. Same arguments as farfield2d. |

**Example**

This example plots the amplitude of the Er component of the far field projection of a 1D
monitor called "monitor". In this example the second frequency point is projected. If
the monitor only contains data at one frequency, the second argument is not required.
For the example of far field projection of a rectilinear dataset see
[farfield2d](./farfield2d.md).

```
E=farfieldpolar2d("monitor",2,501);
Er = abs(pinch(E,2,1)); # amplitude of Er
theta=farfieldangle("monitor",2,501);
plot(theta,Er,"angle (deg)","Er far field"); 
```

For additional examples see
[ Far field projection](https://optics.ansys.com/hc/en-us/articles/360034914713).

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield2d ](./farfield2d.md) , [ farfieldvector2d ](./farfieldvector2d.md) ,
[ farfieldangle ](./farfieldangle.md)
