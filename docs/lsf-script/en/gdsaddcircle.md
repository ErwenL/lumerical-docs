# gdsaddcircle

This function adds an approximation of a circle to a GDSII file stream. GDSII files do
not support circles, so this is just a convenient function to create a polygon
representation of a circle. Polygons can only be added in a GDSII cell, so this command
can be called only if a cell has been created.

| **Syntax**                         | **Description**                                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------- |
| gdsaddcircle(f, layer, x, y, r, n) | Adds an approximation of a circle on a layer with x-, y-coordinates, radius and number of polygon sides. |

| **Parameter** | **Type**         | **Description**                                                                                                                                                                                                                                                             |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f             | string           | a file handle that was previously opened with gdsopen.                                                                                                                                                                                                                      |
| layer         | string or number | string: a string of the form "layer:datatype" (for example "6:2") can be used to define the layer number and datatype for this structure from the GDSII file to import. Layer and datatype are integers. number: defines the layer number and sets the datatype to be zero. |
| x             | number           | x-coordinate of the center position in meters.                                                                                                                                                                                                                              |
| y             | number           | y-coordinate of the center position in meters.                                                                                                                                                                                                                              |
| r             | number           | radius of the circle in meters.                                                                                                                                                                                                                                             |
| n             | number           | number of sides to use in the polygon approximation. It is 64 by default.                                                                                                                                                                                                   |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsbegincell](./gdsbegincell.md),
[gdsendcell](./gdsendcell.md), [gdsaddpoly](./gdsaddpoly.md),
[gdsaddref](./gdsaddref.md), [gdsimport](./gdsimport.md), [gdsaddpath](./gdsaddpath.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
