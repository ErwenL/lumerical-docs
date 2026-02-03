# gdsaddpoly

This function adds a polygon element to a GDSII file stream. Polygons are also known as boundary elements in GDS terminology. This command can be called only if a cell has been created.The maximum number of vertices that can be added in a single polygon is 8190 due to [limitations](https://www.artwork.com/gdsii/max_vertex.htm) in the maximum number of vertices in a gdsii boundary. You can only use this command if a gds cell has already been created, for example, using [gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell-Script-command).

For complex geometries requiring more vertices, use [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command).

**Syntax** |  **Description**  
---|---  
gdsaddpoly(f, layer, [vertices]) |  Adds a polygon element on a layer with vertices.  
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
f |  string |  A file handle that was previously opened with [gdsopen](https://optics.ansys.com/hc/en-us/articles/360034927093-gdsopen-Script-command).  
layer |  string or number |  String: a string of the form "layer:datatype" (for example "6:2") can be used to define the layer number and datatype for this structure from the GDSII file to import. Layer and datatype are integers. Number: defines the layer number and sets the datatype to be zero.  
vertices |  matrix |  Vertices of the polygon, in a Nx2 matrix where the first column represents x and the second column represents y, e.g., [x1,y1; x2,y2;...xn,yn]. The values are in meters. The first and last values should not be the same, the polygon will be automatically closed.  
  
## Example

An example of script code is available on the [gdsopen](/hc/en-us/articles/360034927093-gdsopen) page.

**See Also**

[gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsclose](/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](/hc/en-us/articles/360034406894-gdsendcell), [gdsaddcircle](/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddref](/hc/en-us/articles/360034927173-gdsaddref), [gdsimport](/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath](/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext,](/hc/en-us/articles/360034927193-gdsaddtext) [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
