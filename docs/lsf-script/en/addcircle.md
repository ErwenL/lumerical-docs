# addcircle

Adds a [circle primitive](https://optics.ansys.com/hc/en-us/articles/360034901513) to
the simulation environment. Circles denote physical objects which appear circular or
ellipsoid from above. These objects are circles or ellipses in 2D, and circular or
ellipsoid cylinders in 3D.

| **Syntax**              | **Description**                                                                                                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addcircle;              | Adds a circle primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addcircle(struct_data); | Adds a circle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a circle named "new_circle" with a radius of 5
um centered at (x,y,z) = (1, 2, 0) microns. The circle will have a thickness (z span) of
10 microns.

```
addcircle;
set("name","new_circle");
set("x",1e-6);
set("y",2e-6);
set("radius",5e-6);
set("z",0);
set("z span",10e-6);
```

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
