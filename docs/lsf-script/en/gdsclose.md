# gdsclose

This function closes a GDSII file for writing. Before calling this command, a .gds file
has to be previously opened, see [gdsopen](./gdsopen.md).

| **Syntax**           | **Description**                                      |
| -------------------- | ---------------------------------------------------- |
| gdsclose("filename") | closes a .gds file in the current working directory. |
| **Parameter**        | **Type**                                             |
| ---                  | ---                                                  |
| filename             | string                                               |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsbegincell](./gdsbegincell.md),
[gdsendcell](./gdsendcell.md), [gdsaddpoly](./gdsaddpoly.md),
[gdsaddcircle](./gdsaddcircle.md), [gdsaddrect](./gdsaddrect.md),
[gdsaddref](./gdsaddref.md), [gdsimport](./gdsimport.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
