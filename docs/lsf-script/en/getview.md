# getview

This command allows the viewing properties of the Layout Editor to be retrieved.

| **Syntax**           | **Description**                                                    |
| -------------------- | ------------------------------------------------------------------ |
| outstring = getview; | Returns a list of the view properties that can be set. The command |

```
?getview;
```

will return

```
extent, zoom, theta, phi  
```

out = getview("property"); | Returns the current value of any of the view properties.
For example,

```
zoom_level = getview("zoom");
```

will return the current zoom setting of the perspective view relative to the default
level.

## Note: The "extent" and "zoom" options for this command are not available in Finite Element IDE.

**Example**

The properties that can be obtained with getview are described in
[ setview ](./setview.md) .

```
?getview;
extent, zoom, theta, phi
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ setview ](./setview.md) , [ orbit ](./orbit.md) , [ redraw ](./redraw.md)
