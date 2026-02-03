<!--
Translation from English documentation
Original command: addcircle
Translation date: 2026-02-03
-->

# addcircle

向仿真环境添加[圆形图元](/hc/en-us/articles/360034901513)。圆形图元表示从上方看呈圆形或椭圆形的物理对象。这些对象在2D中是圆形或椭圆形，在3D中是圆形或椭圆柱体。

**Syntax** | **Description**
---|---
addcircle; | 向仿真环境添加圆形图元。此函数不返回任何数据。
addcircle(struct_data); | 添加圆形图元，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将创建一个名为"new_circle"的圆形，半径为5微米，中心位于(x,y,z) = (1, 2, 0)微米。该圆形的厚度（z跨度）为10微米。

    addcircle;
    set("name","new_circle");
    set("x",1e-6);
    set("y",2e-6);
    set("radius",5e-6);
    set("z",0);
    set("z span",10e-6);

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)