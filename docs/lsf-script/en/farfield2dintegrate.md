# farfield2dintegrate

Calculates the integral of the far field projection over some range of theta in 2D
simulation. Angles are specified in degrees, but the integral is done in radians.

$$ \\int\_{\\theta} E^{2}(\\theta) d \\theta $$

| **Syntax**                                               | **Description**                         |
| -------------------------------------------------------- | --------------------------------------- |
| out = farfield2dintegrate(E2, theta, halfangle, theta0); | Integrate 2D far field projection data. |

| **Parameter** |          | **Default value** | **Type** | **Description**                                                                                                                                        |
| ------------- | -------- | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| E2            | required |                   | matrix   | E field data from farfield2d                                                                                                                           |
| theta         | required |                   | matrix   | Theta from farfieldangle                                                                                                                               |
| halfangle     | optional | 90                | vector   | Half angle (in degrees) of the integration region. Must have same length as theta0 or length 1. Half angle should be between 0 to 90 degrees.          |
| theta0        | optional | 0                 | vector   | Center angle (in degrees) theta of the integration region. Must have same length as halfangle or length 1. Theta0 should be between -90 to 90 degrees. |

**Example**

Calculate the fraction of power in the far field from 20 to 70 degrees.

```
m="monitor1";
E2=farfield2d(m);
theta=farfieldangle(m);
?farfield2dintegrate(E2,theta,25,45) / farfield2dintegrate(E2,theta);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield2d ](./farfield2d.md) , [ farfieldangle ](./farfieldangle.md)
