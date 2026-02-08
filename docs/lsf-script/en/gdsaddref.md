# gdsaddref

This function adds a reference to another cell to the current cell in the GDSII file
stream. This function replicates the referenced cell (has to be previously opened and
finished) to the current cell and creates a nested hierarchy. The layer numbers of the
replicated structures follow the referenced cell. References can only be added in a
GDSII cell, so this command can be called only if a current cell has been created, for
example, using
[gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell-Script-command).
In addition, the cell to be replicated has to exist before it is referenced.

| **Syntax**                                     | **Description**                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| gdsaddref(f, "cellname", dx, dy, angle_in_deg) | Adds a reference to another cell ("cellname") to the current cell, with a specified move of dx and dy. |

| **Parameter** | **Type** | **Description**                                                                                                                                                                                                                             |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f             | string   | A file handle that was previously opened with gdsopen.                                                                                                                                                                                      |
| cellname      | string   | Name of the referenced cell.                                                                                                                                                                                                                |
| dx            | number   | X-movement of the replicated cell in the current cell.                                                                                                                                                                                      |
| dy            | number   | Y-movement of the replicated cell in the current cell.                                                                                                                                                                                      |
| angle_in_deg  | number   | Optional, angle of rotation in degrees of the replicated cell. For this operation, the **replicated** cell is rotated with respect to **its** **own** origin, and that cell is placed at the coordinates specified by parameters dx and dy. |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsbegincell](./gdsbegincell.md),
[gdsendcell](./gdsendcell.md), [gdsaddpoly](./gdsaddpoly.md),
[gdsaddcircle](./gdsaddcircle.md), [gdsaddrect](./gdsaddrect.md),
[gdsimport](./gdsimport.md), [gdsaddpath](./gdsaddpath.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
