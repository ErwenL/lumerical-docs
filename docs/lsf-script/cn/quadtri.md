<!--
Translation from English documentation
Original command: quadtri
Translation date: 2026-02-03 10:55:27
-->

# quadtri

使用一阶梯形求积法计算二维三角形网格上收集的数据的数值积分。 

**Syntax** |  **Description**  
---|---  
out = quadtri(tri,vtx,u,n);  |  计算三角形网格上收集的数据的积分。如果输入数据为标量，则返回标量；如果输入数据为矢量，则返回具有三个分量的矢量。   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
tri  |  required  |  |  matrix  |  [Mx3] 网格上 M 个三角形单元的连接矩阵。   
vtx  |  required  |  |  matrix  |  [Nx2] 或 [Nx3] 矩阵，包含网格 N 个顶点的 (x,y,z) 坐标。如果矩阵只有两列，则假定 z 坐标为零。   
u  |  required  |  |  matrix  |  [Nx1] 或 [Nx3] 矩阵，包含每个顶点位置待积分的数据。如果矩阵大小为 [Nx1]，则数据为标量；如果矩阵大小为 [Nx3]，则数据为矢量。   
n  |  optional  |  empty  |  matrix  |  [Mx3] 矩阵，包含网格上每个 M 三角形的表面法向量。列对应每个向量的 (x,y,z) 分量。仅当待积分数据为矢量时需要此输入。   
  
**Example**

以下示例计算 u 在有限元网格上的近似积分。 
    
    
    # define 4 vertices in the shape of a rectangle, 
    #point[#1;#2;#3;#4]
    vtx = [0,0; 4,0; 4,3; 0,3];
    # make two triangles (#1,#2,#4) and (#2,#3,#4) with area = 6
    tri = [1,2,4; 2,3,4];
    # Define result values at each vertex point, 
    #point #1, #2, #3, #4
    u=[4,3,2,0];
    # the result of this integral should be 
    # ((4+3+0)/3 + (3+2+0)/3)*6 = 24
    ?I = quadtri(tri,vtx,u);
    result: 
    24 

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [interptri](../en/interptri.md)
- [quadtet](../en/quadtet.md)
- [interptet](../en/interptet.md)
