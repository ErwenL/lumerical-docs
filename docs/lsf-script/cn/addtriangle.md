<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addtriangle -->

# addtriangle

**语法** | **描述**
---|---
addtriangle; | Adds a triangle primitive to the 仿真 environment. This 函数 does not 返回 any data.
addtriangle(struct_data); | Adds a triangle primitive and set its property using a struct containing "property" and 值 pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-脚本-命令) 脚本 命令 page for an 示例. This 函数 does not 返回 any data.

**示例**

The following 脚本 creates a triangle primitive and sets the coordinates of its three corners using a 2D 矩阵.
    vtx = [1,0;2,2;4,0]*1e-6;  # microns  
    addtriangle;  
    set("name","new_triangle");  
    set("vertices",vtx);  
    set("z span",2e-6);

The following 脚本 creates a triangle primitive and sets the coordinates of its three corners using a 2D 矩阵.
    vtx = [1,0;2,2;4,0]*1e-6;  # microns  
    addtriangle;  
    set("name","new_triangle");  
    set("vertices",vtx);  
    set("z span",2e-6);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addpoly ](/hc/en-us/articles/360034404174-addpoly) , [ set ](/hc/en-us/articles/360034928773-set)
