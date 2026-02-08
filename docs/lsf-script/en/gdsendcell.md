# gdsendcell

This function finishes a cell in a GDSII file. This function ends the current cell in
the GDSII file stream. The command gdsbegincell has to be called before closing a cell.

| **Syntax**    | **Description**                                       |
| ------------- | ----------------------------------------------------- |
| gdsendcell(f) | Finishes the previously created cell in a GDSII file. |
| **Parameter** | **Type**                                              |
| ---           | ---                                                   |
| f             | string                                                |

## Example

An example of script code is available on the [gdsopen](./gdsopen.md) page.

**See Also**

[gdsopen](./gdsopen.md), [gdsclose](./gdsclose.md), [gdsbegincell](./gdsbegincell.md),
[gdsaddpoly](./gdsaddpoly.md), [gdsaddcircle](./gdsaddcircle.md),
[gdsaddrect](./gdsaddrect.md), [gdsimport](./gdsimport.md),
[gdsaddref](./gdsaddrect.md), [gdsaddpath](./gdsaddpath.md),
[gdsaddtext, ](./gdsaddtext.md)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
