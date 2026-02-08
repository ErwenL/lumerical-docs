# addtriangle

Adds a 3 vertex, triangle shaped polygon primitive to the simulation environment.

**Syntax** |  **Description**  
---|---  
addtriangle; |  Adds a triangle primitive to the simulation environment. This function does not return any data.  
addtriangle(struct_data); |  Adds a triangle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script creates a triangle primitive and sets the coordinates of its three corners using a 2D matrix.
    
    
    vtx = [1,0;2,2;4,0]*1e-6;  # microns  
    
    addtriangle;  
    set("name","new_triangle");  
    set("vertices",vtx);  
    set("z span",2e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addpoly ](/hc/en-us/articles/360034404174-addpoly) , [ set ](/hc/en-us/articles/360034928773-set)
