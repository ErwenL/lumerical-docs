<!--
Translation from English documentation
Original command: addpoly
Translation date: 2026-02-04 09:12:27
-->

# addpoly

向仿真环境中添加多边形图元。多边形对象使用一组x、y坐标（顶点）在XY平面中定义多边形，然后沿Z方向将其挤出以创建3D几何体。

**语法** |  **描述**  
---|---  
addpoly; |  向仿真环境中添加多边形图元。此函数不返回任何数据。  
addpoly(struct_data);  |  添加多边形图元，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本创建一个2D矩阵来存储多边形的顶点，并使用它创建多边形图元。
    
    
    vtx = [1,0;2,2;4,2;4,1;3,1]*1e-6;  # microns
    addpoly;
    set("name","random_polygon");
    set("vertices",vtx);
    set("z span",2e-6);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
