# gdsaddtext

This function adds a text notation to a gds file at a specified position. This is usually just done on a notes layer for annotations. It supports text at a vertex position.

**Syntax** |  **Description**  
---|---  
gdsaddtext(fileHandle, layer, x, y, text); |  Adds a text notation to a gds file at a specified position.  
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
fileHandle |  string |  a file handle that was previously opened with gdsopen  
layer |  integer |  layer must be an integer  
x,y |  number |  x, y are floating point coordinates where text is placed (lower left corner of text box)  
text |  string |  text is an ascii string that forms the note body  
  
## Example

An example of script code is available on the [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath) page.

**See Also**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath, ](/hc/en-us/articles/360034406954-gdsaddpath)[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
