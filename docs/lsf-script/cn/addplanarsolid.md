<!--
Translation from English documentation
Original command: addplanarsolid
Translation date: 2026-02-04 09:10:18
-->

# addplanarsolid

添加具有指定顶点的平面实体图元。平面实体为创建自定义复杂3D几何体提供了非常便捷的选项。您可以在此页面找到有关平面实体的更多信息：[结构 - 平面实体](/hc/en-us/articles/360034901573-Structures-Planar-solid)。

**语法** |  **描述**  
---|---  
addplanarsolid; |  添加空平面实体对象。  
addplanarsolid(vtx, fct); |  添加平面实体对象，其顶点由'vtx'定义，其面由'fct'定义  
addplanarsolid(struct_data);  |  添加空平面实体对象，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

下面的示例使用两种方法添加平面实体切割面盒子。第一种方法将面表用作单元格数组，第二种方法将面表用作矩阵。
    
    
    method_type = 1;  # choose 1 or 2 to switch between methods
    vtx = [0,0,0;
         1,0,0;
         1,1,0;
         0,1,0;
         0,0,2;
         1,0,2;
         1,1,2;
         0,1,2]*1e-6;
    # Method 1: facet table as cell array
    a = cell(7);
    for (i = 1:7) {
     a{i} = cell(1);
    }
    a{1}{1} = [1,4,3,2];
    a{2}{1} = [1,5,8,4];
    a{3}{1} = [1,2,6,5];
    a{4}{1} = [2,3,6];
    a{5}{1} = [3,8,6];
    a{6}{1} = [3,4,8];
    a{7}{1} = [5,6,8];
    if (method_type == 1) {
     addplanarsolid(vtx,a);
    }
    # Method 2: facet table as matrix
    b = matrix(4,1,7); # max four points per polygon, max 1 polygon per facet
    for (i = 1:7) { 
      fpoly = a{i}{1}; 
      for (j = 1:length(fpoly)) { 
        b(j,1,i) = fpoly(j); 
        }
      }
    if (method_type == 2) { 
      addplanarsolid; 
      set('vertices',vtx); # must be done first 
      set('facets',b);
      }

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
