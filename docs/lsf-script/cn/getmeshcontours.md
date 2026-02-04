<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getmeshcontours -->

# getmeshcontours

    ID_1 = contours{1}.ID;
    domains_1 = contours{1}.adjacent;
    vertices_1 = contours{1}.元素;

**语法** | **描述**
---|---
A = getmeshcontours(dataset); | 返回 information about the contours between different domains of the unstructured 数据集 named "数据集". The 输出 is provided as a cell 数组. Each entry is a struct with three fields:  **ID:** An 整数 ID that is unique for that contour.  **adjacent:** Two integers representing the IDs of the adjacent domains.  **元素:** For 2D, Nx2 数组 and for 3D, Nx3 数组 of integers that are the indexes to the vertices for each face on the 边界.

**示例**

The 脚本 commands below will get the contour information for the "grid" 数据集 (available after calculating the finite-元素 网格). 
    网格("CHARGE");  # 计算 the 网格 in Finite 元素 IDE using the CHARGE 求解器
    grid = getresult("CHARGE","grid");  # get the 网格 information ("grid" 数据集)
    contours = getmeshcontours(grid);

The 脚本 commands below will get the contour information for the "grid" 数据集 (available after calculating the finite-元素 网格). 
    网格("CHARGE");  # 计算 the 网格 in Finite 元素 IDE using the CHARGE 求解器
    grid = getresult("CHARGE","grid");  # get the 网格 information ("grid" 数据集)
    contours = getmeshcontours(grid);

**另请参阅**

[ Datasets ](/hc/en-us/articles/360034409554-Datasets) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ getresult ](/hc/en-us/articles/360034409854-getresult)
