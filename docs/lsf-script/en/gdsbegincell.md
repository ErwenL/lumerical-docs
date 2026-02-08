# gdsbegincell

This function creates a cell in a GDSII file. All GDS elements (polygons, boxes,
references, array references, etc) must be placed inside a cell, so this function must
be called before adding any elements. When finished adding elements, gdsendcell can be
called to finish the cell. Cells cannot be nested, so after calling gdsbegincell, a new
cell cannot be called again until the first called cell has been closed. Although the
GDSII file is a flat list of cells, cells can reference other cells, thus creating a
nested hierarchy. See [gdsaddref](./gdsaddref.md) for more details. A GDS "cell" exists
as a "structure group" when imported to FDTD, see [gdsimport](./gdsimport.md) for more
details.

| **Syntax**                  | **Description**                     |
| --------------------------- | ----------------------------------- |
| gdsbegincell(f, "cellname") | Creates a new cell in a GDSII file. |
| **Parameter**               | **Type**                            |
| ---                         | ---                                 |
| f                           | string                              |
| cellname                    | string                              |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

Note: Just to clarify, a GDS cell is different from a [Cell Array](./cell.md) in FDTD.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsendcell](./gdsendcell.md),
[gdsaddpoly](./gdsaddpoly.md), [gdsaddcircle](./gdsaddcircle.md),
[gdsaddrect](./gdsaddrect.md), [gdsimport](./gdsimport.md), [gdsaddref](./gdsaddref.md),
[gdsaddpath](./gdsaddpath.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
