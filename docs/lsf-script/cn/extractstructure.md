# extractstructure

使用存储在非结构化数据集中的有限元几何数据创建多边形（2D 情况下）或平面实体（3D 情况下）。

**语法** | **描述**
---|---
extractstructure(D); | 为 2D 数据创建多边形，为 3D 数据创建平面实体。参数 D 是输入的非结构化数据集。此函数不返回任何数据。
extractstructure(D, Rel_Coplanar_Tol); | 与上述命令相同，但设置合并共面元素的相对容差为指定值。
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count); | 与上述命令相同，但对表面网格使用拉普拉斯平滑。迭代次数由指定值定义。
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol); | 与上述命令相同，但设置顶点周围三角形之间允许的角度差，使得顶点可以在该范围内移动。
extractstructure(D, Rel_Coplanar_Tol, Smoothing_Pass_Count, Smoothing_Angle_Coplanar_Tol, Allow_Tessalation); | 与上述命令相同，但允许对 facets 进行重新三角剖分。

**参数** | **类型** | **描述**
---|---|---
D | 非结构化数据集 | 用于创建结构的输入数据。
Rel_Coplanar_Tol | 数字 |（可选）合并共面元素的相对容差。默认值为 1e-6。
Smoothing_Pass_Count | 数字 |（可选）仅适用于 3D。启用表面网格的拉普拉斯平滑后再进行表面提取。默认值为 0，最大允许值为 20。
Smoothing_Angle_Coplanar_Tol | 数字 |（可选）设置顶点周围三角形之间允许的角度差，使得顶点可以在该范围内移动。默认值为 0.001。
Allow_Tessalation | 数字 |（可选）仅适用于 3D。允许对 facets 进行重新三角剖分。

**示例**

运行脚本文件 [extract_2d.lsf](/hc/article_attachments/360045274574/extract_2d.lsf) 和 CHARGE 项目文件 [geom2d.ldev](/hc/article_attachments/360046126993/geom2d.ldev) 来获取此命令的 2D 示例。在这里，我们使用 "CHARGE" 求解器区域的 ID 来单独提取 ID = 3 的结构部分，这在此示例中对应半导体材料，然后创建一个该形状的对象（多边形）。

**另请参阅**

[数据集构建器](**%20to%20be%20defined\**)、[数据集](**%20to%20be%20defined\**)