# farfield2d

Projects a given power or field profile monitor or a rectilinear dataset to the far
field to a 1 meter radius semi-circle. The electric field intensity |E| 2 is returned.
Farfield2d does not use a set of linearly spaced angles for the projection, use
[farfieldangle - Script command](https://optics.ansys.com/hc/en-us/articles/360034930653)
to get the appropriate angle vector.

| **Syntax**                                                                | **Description**                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| out = farfield2d("mname", f, n, illumination, periods, index, direction); | Projects a given power or field profile monitor to the far field at the specified frequency points. The result is an NxM matrix where the first dimension is the resolution of the far field projection, and the second dimension is the number of frequency points projected. |
| out = farfield2d(dataset, f, n, illumination, periods, index, direction); | Projects a given rectilinear dataset to the far field at the specified frequency points. The result is an NxM matrix where the first dimension is the resolution of the far field projection, and the second dimension is the number of frequency points projected.            |

| **Parameter** |          | **Default value**           | **Type** | **Description**                                                                                                                                       |
| ------------- | -------- | --------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| mname         | required |                             | string   | Name of the monitor                                                                                                                                   |
| dataset       | required |                             | dataset  | Rectilinear dataset containing both E and H                                                                                                           |
| f             | optional | 1                           | vector   | Index of the desired frequency point. f can be a single value, or a vector of frequency points. Multithreaded projection was introduced since R2016b. |
| n             | optional | 2000                        | number   | The number of points in the far field.                                                                                                                |
| illumination  | optional | 1                           | number   | For periodic structures Gaussian illumination: 1 Plane wave illumination: 2                                                                           |
| periods       | optional | 1                           | number   | number of periods to be used                                                                                                                          |
| index         | optional | value at monitor center     | number   | The index of the material to use for the projection.                                                                                                  |
| direction     | optional | direction of max power flow | number   | Direction: this can be +1 or -1.                                                                                                                      |

**Example**

This example plots the far field projection of a 1D monitor called monitor. In this
example the second frequency point is projected. If the monitor only contains data at
one frequency, the second argument is not required.

```
E2=farfield2d("monitor",2,501);
theta=farfieldangle("monitor",2,501);
plot(theta,E2,"angle (deg)","|E|^2 far field"); 
```

The following example plots the far field projection of a rectilinear dataset. Here, the
dataset is from a 1D monitor.

```
dataset=getresult("monitor", "E");  
dataset.addattribute("H",getattribute(getresult("monitor","H"),"H"));  
  
E2=farfield2d(dataset,2,501);  
theta=farfieldangle(dataset,2,501);  
plot(theta,E2,"angle (deg)","|E|^2 far field"); 
```

For additional examples see
[ Far field projection ](https://optics.ansys.com/hc/en-us/articles/360034914713) .

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield3d ](./farfield3d.md) , [ farfieldangle ](./farfieldangle.md) ,
[ farfieldvector2d ](./farfieldvector2d.md) , [ farfieldpolar2d ](./farfieldpolar2d.md)
, [ farfieldexact2d ](./farfieldexact2d.md) , [ farfieldfilter ](./farfieldfilter.md) ,
[ farfieldexact ](./farfieldexact.md) ,
[ farfield2dintegrate ](./farfield2dintegrate.md)
