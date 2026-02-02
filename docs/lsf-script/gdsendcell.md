# gdsendcell

This function finishes a cell in a GDSII file. This function ends the current cell in the GDSII file stream. The command gdsbegincell has to be called before closing a cell.

**Syntax** |  **Description**  
---|---  
gdsendcell(f) |  Finishes the previously created cell in a GDSII file.  
**Parameter** |  **Type** |  **Description**  
---|---|---  
f |  string |  a file handle that was previously opened with gdsopen.  
  
## Example

An example of script code is available on the [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

**See Also**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddref](/hc/en-us/articles/360034406934-gdsaddrect), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext, ](/hc/en-us/articles/360034927193-gdsaddtext)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
