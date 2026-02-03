# gdsaddstencil

Adds one or more polygon elements to the current gds cell based on a slice formed by the intersection of a given z-plane and structures with a specific material and a partial name. Multiple polygons are created when there are more than 8190 vertices. You can only use this command if a gds cell has already been created, for example, using [gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell-Script-command).

If the material is “<Object defined dielectric>", the index value must be provided.

This command will always ignore disabled geometry.

**Syntax** |  **Description**  
---|---  
gdsaddstencil(f, layer, {"material": mat_name,  
"partialname": partial_name, "z": z, "curve_chord_tol": tol, "dx": dx, "dy": dy  
}); |  Adds one or more polygon elements based on the intersection of a z-plane and structures. The parameters are explained below.  
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
f |  string |  A file handle that was previously opened with [gdsopen](https://optics.ansys.com/hc/en-us/articles/360034927093-gdsopen-Script-command).  
layer |  string or number |  String: a string of the form "layer:datatype" (for example "6:2") can be used to define the layer number and datatype for this structure from the GDSII file to import. Layer and datatype are integers. Number: defines the layer number and sets the datatype to be zero.  
mat_name |  string |  Material name for intersection. The command creates polygon(s) only for materials with this name.  
partialname  |  string |  Partial name of object for intersection. The command creates polygon(s) only for objects in the object tree that has this string as a part of its name.  
z |  number |  The z-plane to create the intersection on. Only a scalar value is accepted.  
curve_chord_tol |  number |  Optional with a default of 0. The maximum chordal distance between a facet edge and its original edge entity.  
dx |  number |  Optional with a default of 0. Position within the slice to be used as the origin of the gds coordinates.  
dy |  number |  Optional with a default of 0. Position within the slice to be used as the origin of the gds coordinates.  
  
**See Also**

[gdsopen](https://optics.ansys.com/hc/en-us/articles/360034927093-gdsopen), [gdsclose](https://optics.ansys.com/hc/en-us/articles/360034927113-gdsclose), [gdsbegincell](https://optics.ansys.com/hc/en-us/articles/360034927133-gdsbegincell), [gdsendcell](https://optics.ansys.com/hc/en-us/articles/360034406894-gdsendcell), [gdsaddpoly](https://optics.ansys.com/hc/en-us/articles/360034927153-gdsaddpoly), [gdsaddcircle](https://optics.ansys.com/hc/en-us/articles/360034406914-gdsaddcircle), [gdsaddrect](https://optics.ansys.com/hc/en-us/articles/360034406934-gdsaddrect), [gdsimport](https://optics.ansys.com/hc/en-us/articles/360034406974-gdsimport), [gdsaddpath](https://optics.ansys.com/hc/en-us/articles/360034406954-gdsaddpath), [gdsaddtext](https://optics.ansys.com/hc/en-us/articles/360034927193-gdsaddtext), [gdsaddref](https://optics.ansys.com/hc/en-us/articles/360034927173-gdsaddref-Script-command), [polystencil ](https://optics.ansys.com/hc/en-us/articles/4401965734291-polystencil-Script-command)
