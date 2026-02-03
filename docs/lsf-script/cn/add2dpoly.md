<!--
Translation from English documentation
Original command: add2dpoly
Translation date: 2026-02-03
-->

# add2dpoly

在仿真空间中添加一个[2D多边形](https://optics.ansys.com/hc/en-us/articles/360034901613)。

**Syntax** | **Description**
---|---
add2dpoly; | 在仿真空间中添加一个2D多边形。此函数不返回任何数据。
add2dpoly("property",value); | 添加一个2D多边形并通过指定"property"和值对来设置其属性。
add2dpoly(struct_data); | 添加一个2D多边形并使用包含"property"和值对的结构体来设置其属性。

**Example**

以下脚本创建一个2D矩阵来存储多边形的顶点，并使用它在XY平面上创建一个2D多边形图元。

    vtx = [1,0;2,2;4,2;4,1;3,1]*1e-6;  # microns
    add2dpoly;
    set("name","2D_polygon");
    set("surface normal",3); #  1 = x (normal), 2 = y (normal), 3 = z (normal)
    set("vertices",vtx);
    set("z",2e-6);

在添加对象时设置属性：

    add2dpoly("name","test_obj");
    
    # using struct  
    struct_data = {"name": "test_obj", "x":  1e-6};
    add2dpoly(struct_data);

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [add2drect](./add2drect.md)
- [2D polygon](https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon)
- [2D rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593-Structures-2D-Rectangle-Optical-)