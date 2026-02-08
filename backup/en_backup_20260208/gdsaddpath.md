# gdsaddpath

This function adds adds a segmented line path with a fixed width. It supports the options with the square corner style.

**Syntax** |  **Description**  
---|---  
gdsaddpath(fileHandle, layer_datatype, width, vertices); |  Adds a segmented line path with a fixed width.  
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
fileHandle |  string |  a file handle that was previously opened with gdsopen.  
layer_datatype |  integer |  layer_datatype is the same as other gdsadd commands, either an integer layer, or an integer layer colon integer data type encoded as string 'x:y'.  
width |  number |  width is a floating number.  
vertices |  matrix |  2 column matrix of floating point coordinates.  
  
## Example

This shows an example to export a path and text to GDSII format via script code
    
    
    f=gdsopen("path_text.gds", 1e-3, 1e-9);
    gdsbegincell(f, 'example');
    gdsaddpath(f, 1, 0.5e-6, [-1, 0; 1, 0]*1e-6);
    gdsaddpath(f, '1:10', 0.5e-6, [-0.9, 0; -1.1, 0]*1e-6);
    gdsaddpath(f, '1:10', 0.5e-6, [0.9, 0; 1.1, 0]*1e-6);
    gdsaddtext(f, 10, -1e-6, 0, 'this is a pin');
    gdsendcell(f);
    gdsclose(f);

**See Also**

[ gdsopen ](/hc/en-us/articles/360034927093-gdsopen) , [ gdsclose ](/hc/en-us/articles/360034927113-gdsclose) , [ gdsbegincell ](/hc/en-us/articles/360034927133-gdsbegincell) , [ gdsendcell ](/hc/en-us/articles/360034406894-gdsendcell) , [ gdsaddpoly ](/hc/en-us/articles/360034927153-gdsaddpoly) , [ gdsaddcircle ](/hc/en-us/articles/360034406914-gdsaddcircle) , [ gdsaddrect ](/hc/en-us/articles/360034406934-gdsaddrect) , [ gdsimport ](/hc/en-us/articles/360034406974-gdsimport) , [ gdsaddtext](/hc/en-us/articles/360034927193-gdsaddtext), [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
