# gdsbegincell

This function creates a cell in a GDSII file. All GDS elements (polygons, boxes, references, array references, etc) must be placed inside a cell, so this function must be called before adding any elements. When finished adding elements, gdsendcell can be called to finish the cell. Cells cannot be nested, so after calling gdsbegincell, a new cell cannot be called again until the first called cell has been closed. Although the GDSII file is a flat list of cells, cells can reference other cells, thus creating a nested hierarchy. See [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref) for more details. A GDS "cell" exists as a "structure group" when imported to FDTD, see [gdsimport](/hc/en-us/articles/360034406974-gdsimport) for more details.

**Syntax** |  **Description**  
---|---  
gdsbegincell(f, "cellname") |  Creates a new cell in a GDSII file.  
**Parameter** |  **Type** |  **Description**  
---|---|---  
f |  string |  a file handle that was previously opened with gdsopen.  
cellname |  string |  name of the cell.  
  
## Example

An example of script code is available on the [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

Note: Just to clarify, a GDS cell is different from a [Cell Array](/hc/en-us/articles/360034929913-cell) in FDTD.

**See Also**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext, ](/hc/en-us/articles/360034927193-gdsaddtext)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
