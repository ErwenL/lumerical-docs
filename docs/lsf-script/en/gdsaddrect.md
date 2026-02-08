# gdsaddrect

This function adds a rectangle element to a GDSII file stream. This is just a convenient
function to create a polygon for the case of a rectangle. Other element type for
rectangle (such as, box) is not supported at this moment. Polygons can only be added in
a GDSII cell, so this command can be called only if a cell has been created.

| **Syntax**                                | **Description**                                                               |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| gdsaddrect(f, layer, x, y, width, height) | Adds a rectangle element on a layer with x-, y-coordinates, width and height. |

| **Parameter** | **Type**         | **Description**                                                                                                                                                                                                                                                             |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f             | string           | a file handle that was previously opened with gdsopen.                                                                                                                                                                                                                      |
| layer         | string or number | string: a string of the form "layer:datatype" (for example "6:2") can be used to define the layer number and datatype for this structure from the GDSII file to import. Layer and datatype are integers. number: defines the layer number and sets the datatype to be zero. |
| x             | number           | x-coordinate of the center position in meters.                                                                                                                                                                                                                              |
| y             | number           | y-coordinate of the center position in meters.                                                                                                                                                                                                                              |
| width         | number           | width of the rectangle in meters.                                                                                                                                                                                                                                           |
| height        | number           | height of the rectangle in meters.                                                                                                                                                                                                                                          |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsbegincell](./gdsbegincell.md),
[gdsendcell](./gdsendcell.md), [gdsaddpoly](./gdsaddpoly.md),
[gdsaddref](./gdsaddref.md), [gdsimport](./gdsimport.md), [gdsaddpath](./gdsaddpath.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
