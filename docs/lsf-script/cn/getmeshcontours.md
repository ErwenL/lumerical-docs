<!--
Translation from English documentation
Original command: getmeshcontours
Translation date: 2026-02-04 22:50:00
-->

# getmeshcontours

获取 information about 该 contours between different domains 在 一个 unstructured (finite-元素) dataset. The dataset 必须 contain 该 "ID" attribute (一个 unique identified 用于 each domain 在 该 finite-元素 mesh generated 在 Finite Element IDE based products). 

**语法** |  **描述**  
---|---  
A = getmeshcontours(dataset);  |  返回 information about 该 contours between different domains 的 该 unstructured dataset named "dataset". The output 是 provided as 一个 单元格 数组. Each entry 是 一个 结构体 使用 three fields:  **ID:** An integer ID 该 是 unique 用于 该 contour.  **adjacent:** Two integers representing 该 IDs 的 该 adjacent domains.  **elements:** For 2D, Nx2 数组 和 用于 3D, Nx3 数组 的 integers 该 是 该 indexes 到 该 vertices 用于 each face 在 该 boundary.   
  
**示例**

The 脚本 commands below 将 获取 该 contour information 用于 该 "grid" dataset (available after calculating 该 finite-元素 mesh). 
    
    
    mesh("CHARGE");  # 计算 该 mesh 在 Finite Element IDE 使用 该 CHARGE 求解器
    grid = getresult("CHARGE","grid");  # 获取 该 mesh information ("grid" dataset)
    contours = getmeshcontours(grid);
    # 获取 该 ID 的 该 first contour
    ID_1 = contours{1}.ID;
    # 获取 该 ID 的 该 two adjacent domains (ID = 0 means external boundary) 
    domains_1 = contours{1}.adjacent;
    # 获取 该 index 的 vertices forming 该 first contour
    vertices_1 = contours{1}.elements;

**参见**

[ Datasets ](/hc/en-us/articles/360034409554-Datasets) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ getresult ](/hc/en-us/articles/360034409854-getresult)
