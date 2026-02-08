# addcustom

Adds a [custom](https://optics.ansys.com/hc/en-us/articles/360036620233) primitive to
the simulation environment. Custom primitives are objects that are defined by equations
describing the boundaries of the physical object.

| **Syntax**              | **Description**                                                                                                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addcustom;              | Adds a custom primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addcustom(struct_data); | Adds a custom primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a half circle with a radius of 0.5 micron in
the XY plane and extrude it along the Z axis.

```
addcustom;
set("create 3D object by","extrusion");#  y = sqrt(0.5^2-(x-0.5)^2)
set("equation 1","sqrt("+num2str(0.5)+"^2-(x-"+num2str(0.5)+")^2)");   
set("x span",1e-6);
set("y span",1e-6);
set("z span",2e-6);
```

The same equation can be used to create half a sphere by rotating the half circle rather
than extruding it.

```
addcustom;
set("create 3D object by","revolution");#  y = sqrt(0.5^2-(x-0.5)^2)
set("equation 1","sqrt("+num2str(0.5)+"^2-(x-"+num2str(0.5)+")^2)");   
set("x span",1e-6);
set("y span",1e-6);
set("z span",2e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
