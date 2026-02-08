# setview

This command allows the viewing properties of the Layout Editor to be modified.

| **Syntax**           | **Description**                                                    |
| -------------------- | ------------------------------------------------------------------ |
| outstring = setview; | Returns a list of the view properties that can be set. The command |

```
?setview;
```

will return

```
extent, zoom, theta, phi  
```

setview("property"); | Sets the default value for any of the view properties. For
example,

```
setview("extent");
```

is the same as pressing the graphical extent button.\
setview("property",value); | Sets the values to of any property for viewing.

The following table describes the properties that can be set

| **Property**                                       | **Description**                                                                                                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| extent (not available in CHARGE, HEAT, FEEM, DGTD) | Control the view extent. In this case, value should be a 2x1, 4x1 or 6x1 matrix representing the view range min x, max x, min y, max y, min z and max z respectively. |
| zoom                                               | Controls the relative zoom of the perspective view compared to the default level. To zoom in by a factor of 2 in the perspective view, use                            |

```
setview("zoom",2);  
```

theta | Controls the polar angle of the perspective view, in degrees.\
phi | Controls the azimuthal angle of the perspective view, in degrees.

**Example**

This example uses the setview command to spin the "perspective view" by 360 degrees.

```
setview("extent");
setview("zoom",4);
setview("theta", 30);
for (i=0:10:360) {
  setview("phi",i);
} 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ getview ](./getview.md) , [ orbit ](./orbit.md) , [ redraw ](./redraw.md)
