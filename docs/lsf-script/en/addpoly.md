# addpoly

Adds a polygon primitive to the simulation environment. The polygon object defines a
polygon in the XY plane using a set of x, y coordinates (vertices) and then extrudes it
in the Z direction to create a 3D geometry.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addpoly;              | Adds a polygon primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addpoly(struct_data); | Adds a polygon primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script creates a 2D matrix to store the vertices of a polygon and uses it
to create a polygon primitive.

```
vtx = [1,0;2,2;4,2;4,1;3,1]*1e-6;  # microns
addpoly;
set("name","random_polygon");
set("vertices",vtx);
set("z span",2e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
