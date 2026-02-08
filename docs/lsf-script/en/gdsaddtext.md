# gdsaddtext

This function adds a text notation to a gds file at a specified position. This is
usually just done on a notes layer for annotations. It supports text at a vertex
position.

| **Syntax**                                 | **Description**                                             |
| ------------------------------------------ | ----------------------------------------------------------- |
| gdsaddtext(fileHandle, layer, x, y, text); | Adds a text notation to a gds file at a specified position. |

| **Parameter** | **Type** | **Description**                                                                          |
| ------------- | -------- | ---------------------------------------------------------------------------------------- |
| fileHandle    | string   | a file handle that was previously opened with gdsopen                                    |
| layer         | integer  | layer must be an integer                                                                 |
| x,y           | number   | x, y are floating point coordinates where text is placed (lower left corner of text box) |
| text          | string   | text is an ascii string that forms the note body                                         |

## Example

An example of script code is available on the [gdsaddpath](./gdsaddpath.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsbegincell](./gdsbegincell.md),
[gdsendcell](./gdsendcell.md), [gdsaddpoly](./gdsaddpoly.md),
[gdsaddcircle](./gdsaddcircle.md), [gdsaddrect](./gdsaddrect.md),
[gdsimport](./gdsimport.md),
[gdsaddpath, ](./gdsaddpath.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
