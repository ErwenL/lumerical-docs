<!--
Translation from English documentation
Original command: extractstructure
Translation date: 2026-02-04 22:49:48
-->

# extractstructure

创建 一个 一个 polygon (在 2D) 或 一个 planar solid (在 3D) 使用 该 finite-元素 geometric 数据 stored 在 一个 unstructured dataset.

**语法** |  **描述**  
---|---  
extractstructure(D); |  创建 一个 polygon 用于 2D 数据 和 一个 planar solid 用于 3D 数据. The 参数 D 是 该 input unstructured dataset. This 函数 does not 返回 any 数据.  
extractstructure(D, Rel_Coplanar_Tol); |  Same as 该 above 命令, but 该 relative tolerance 到 merge coplanar elements 将 为 设置 到 该 值 specified.  
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count); |  Same as 该 above 命令, but uses Laplacian smoothing 在 该 surface mesh. The 数字 的 iteration 是 defined 通过 该 值 specified.  
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol); |  Same as 该 above 命令, but 该 allowed angular difference between triangles around 一个 vertex 其中 该 vertex 可以 为 moved 是 设置 到 该 值 specified.  
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol, Allow_Tessalation); |  Same as 该 above 命令, but allows re-triangulation 的 该 facets.  
  
**Parameters** |  **Type** |  **描述**  
---|---|---  
D |  unstructured dataset |  Input 数据 该 是 used 到 创建 该 结构.  
Rel_Coplanar_Tol |  数字 |  (optional) Relative tolerance 到 merge coplanar elements. The default 值 是 1e-6.  
Smoothing_Pass_Count |  数字 |  (optional) In 3D only. Enables Laplacian smoothing 在 该 surface mesh before surface extraction. The default 值 是 0 和 该 maximum allowed 值 是 20.  
Smoothing_Angle_Coplanar_Tol |  数字 |  (optional) 设置 该 allowed angular difference between triangles around 一个 vertex 其中 该 vertex 可以 为 moved. The default 值 是 0.001.  
Allow_Tessalation |  数字 |  (optional) In 3D only. Allows re-triangulation 的 该 facets.  
  
**示例**

Run 该 脚本 文件 [extract_2d.lsf](/hc/article_attachments/360045274574/extract_2d.lsf) 使用 该 CHARGE project 文件 [geom2d.ldev](/hc/article_attachments/360046126993/geom2d.ldev) 用于 一个 2D example 的 此 命令. Here, we use 该 ID 的 该 "CHARGE" 求解器 region 到 single out any part 的 该 结构 使用 ID = 3, 该 would correspond 到 该 semiconductor 材料 在 此 example 和 那么 construct 一个 对象 (polygon) 在 该 shape.

**参见**

[Dataset builder](/hc/en-us/articles/360034901713-Dataset-builder), [Datasets](/hc/en-us/articles/360034409554-Datasets)
