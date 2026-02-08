# add2drect

Adds a [2D rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593) in the
simulation space.

| **Syntax**                  | **Description**                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------- |
| add2drect;                  | Adds a 2D rectangle in simulation space. This function does not return any data.                   |
| add2rect("property",value); | Adds a 2D rectangle and set its the property by specifying the "property" and value pair.          |
| add2drect(struct_data);     | Adds a 2D rectangle and set its the property using a struct containing "property" and value pairs. |

**Example**

The following script creates a 2D rectangle on the XY plane, sets its dimension, and
assigns a material to it.

```
add2drect;
set("name","2D_rectangle");
set("surface normal",3);  # z (normal)
set("x",1e-6);
set("x span",2e-6);
set("y",1e-6);
set("y span",5e-6);
set("z",0);
set("material","Si (Silicon) - Palik");
```

Setting the properties while adding the object:

```
add2drect("name","test_obj");  
  
# using struct  
struct_data = {"name": "test_obj", "x": 1e-6};  
add2drect(struct_data);
```

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [2D rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593-Structures-2D-Rectangle-Optical-)
- [add2dpoly](./add2dpoly.md)
- [2D polygon](https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon)
