# add2dpoly

Adds a [2D polygon](https://optics.ansys.com/hc/en-us/articles/360034901613) in the simulation space.

**Syntax** |  **Description**  
---|---  
add2dpoly; |  Adds a 2D polygon in simulation space. This function does not return any data.  
add2dpoly("property",value); |  Adds a 2D polygon and set its the property by specifying the "property" and value pair.  
add2dpoly(struct_data); |  Adds a 2D polygon and set its the property using a struct containing "property" and value pairs.  
  
**Example**

The following script creates a 2D matrix to store the vertices of a polygon and uses it to create a 2D polygon primitive on the XY plane.
    
    
    vtx = [1,0;2,2;4,2;4,1;3,1]*1e-6;  # microns
    add2dpoly;
    set("name","2D_polygon");
    set("surface normal",3); #  1 = x (normal), 2 = y (normal), 3 = z (normal)
    set("vertices",vtx);
    set("z",2e-6);

Setting the properties while adding the object:
    
    
    add2dpoly("name","test_obj");
    
    # using struct  
    struct_data = {"name": "test_obj", "x":  1e-6};
    add2dpoly(struct_data);

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [add2drect](./add2drect.md)
- [2D polygon](https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon)
- [2D rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593-Structures-2D-Rectangle-Optical-)
