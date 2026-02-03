<!--
Translation from English documentation
Original command: add2drect
Translation date: 2026-02-03
-->

# add2drect

在仿真空间中添加一个[2D矩形](https://optics.ansys.com/hc/en-us/articles/360034901593)。

**Syntax** | **Description**
---|---
add2drect; | 在仿真空间中添加一个2D矩形。此函数不返回任何数据。
add2rect("property",value); | 添加一个2D矩形并通过指定"property"和值对来设置其属性。
add2drect(struct_data); | 添加一个2D矩形并使用包含"property"和值对的结构体来设置其属性。

**Example**

以下脚本在XY平面上创建一个2D矩形，设置其尺寸，并为其分配材料。

    add2drect;
    set("name","2D_rectangle");
    set("surface normal",3);  # z (normal)
    set("x",1e-6);
    set("x span",2e-6);
    set("y",1e-6);
    set("y span",5e-6);
    set("z",0);
    set("material","Si (Silicon) - Palik");

在添加对象时设置属性：

    add2drect("name","test_obj");  
      
    # using struct  
    struct_data = {"name": "test_obj", "x": 1e-6};  
    add2drect(struct_data);

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [2D rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593-Structures-2D-Rectangle-Optical-)
- [add2dpoly](./add2dpoly.md)
- [2D polygon](https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon)