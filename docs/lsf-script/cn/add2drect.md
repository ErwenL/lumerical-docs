<!--
Translation from English documentation
Original command: add2drect
Translation date: 2026-02-04
-->

# add2drect

在仿真空间中添加一个[2D矩形](https://optics.ansys.com/hc/en-us/articles/360034901593)。

**语法** |  **描述**  
---|---  
add2drect; |  在仿真空间中添加一个2D矩形。此函数不返回任何数据。  
add2drect("property",value); |  添加一个2D矩形并通过指定"property"和value对来设置其属性。  
add2drect(struct_data); |  添加一个2D矩形并使用包含"property"和value对的结构体来设置其属性。  
   
**示例**

以下脚本在XY平面上创建一个2D矩形，设置其尺寸，并为其分配材料。
    
    
    add2drect;
    set("name","2D_rectangle");
    set("surface normal",3);  # z (法向)
    set("x",1e-6);
    set("x span",2e-6);
    set("y",1e-6);
    set("y span",5e-6);
    set("z",0);
    set("material","Si (Silicon) - Palik");

在添加对象时设置属性：
    
    
    add2drect("name","test_obj");  
      
    # 使用结构体  
    struct_data = {"name": "test_obj", "x": 1e-6};  
    add2drect(struct_data);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [2D矩形](https://optics.ansys.com/hc/en-us/articles/360034901593-Structures-2D-Rectangle-Optical-)
- [add2dpoly](./add2dpoly.md)
- [2D多边形](https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon)
