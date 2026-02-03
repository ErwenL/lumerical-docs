<!--
Translation from English documentation
Original command: quadtet
Translation date: 2026-02-03 10:52:50
-->

# quadtet

计算三维有限元网格上数据的数值积分。 

**Syntax** |  **Description**  
---|---  
out = quadtet(tet,vtx,u);  |  输出一个标量，即 u 在有限元网格上的积分，其中 

  * tet：连接数组，Mx4，包含索引 M 个四面体四个顶点的行条目 
  * vtx：顶点数组，Nx3，包含定位 N 个顶点点的 (x,y,z) 对行条目 
  * u：有限元网格上的数据 (Nx1) 

  
  
**Example**

以下是一个简单示例，展示如何计算 u 在有限元网格上的近似积分。 
    
    
    # define 8 vertex points in the shape of a cube
    # point[#1;#2;#3;#4;#5;#6;#7;#8]
    vtx = [1,0,0; 0,0,0; 0,1,0; 1,1,0; 1,0,1; 0,0,1; 0,1,1; 1,1,1];
    # make six tetrahedrals from the 8 vertex points, volume=1/6
    tet = [1,2,4,8; 1,2,5,8; 2,5,6,8; 2,3,7,8; 2,6,7,8; 2,3,4,8];
    # Define result values at each vertex point
    # point #1,#2,#3,#4,#5,#6,#7,#8
    u=[4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5];
    # the result of this integral should be 2.16667
    ?I = quadtet(tet,vtx,u);
    result: 
    2.16667 

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [interptri](../en/interptri.md)
- [quadtri](../en/quadtri.md)
