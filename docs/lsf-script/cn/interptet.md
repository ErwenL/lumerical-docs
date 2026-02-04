<!--
Translation from English documentation
Original command: interptet
Translation date: 2026-02-03
-->

# interptet

将数据集从四面体网格插值到另一个四面体或规则网格。数据可以是复数。

此函数通常用于对最初在有限元网格中评估的数据（例如来自 CHARGE 的监视器数据）重新采样到新的规则网格。

**注意：** 自 2020a R7 起，interptet 可以将数据集从四面体插值到矩形网格或点列表。数据可以是矢量的。

**语法** |  **描述**
---|---
out = interptet(tet, vtx, u, xi, yi, zi, extrap_val); out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "rectilinear");  |  对函数进行四面体到规则插值，并输出 PxQxRxS 数组的插值 f(xi,yi,zi,p)。

  * u 是有限元网格的现有数据 (NxS)
  * xi、yi 和 zi 分别是长度 P、Q 和 R 的数组。它们指定在规则网格上在 x 方向、y 方向和 z 方向上对 u 进行采样的点
  * tet 是连通数组 Mx4，包含索引 4 个四面体顶点的行条目。取自模拟区域
  * vtx 是具有四面体网格顶点的矩阵 Nx3，包含 (x,y,z) 对的行条目。取自模拟区域
  * extrap_val（可选）：如果插值点在有限元网格之外，该点将被分配此值（默认为 Inf）

out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "unstructured");  |  对函数进行四面体到点云插值，并输出 PxS 数组的插值。

  * u 是有限元网格的现有数据 (NxS)
  * xi、yi 和 zi 是长度为 P 的数组。它们指定要对其采样的 P 个点
  * tet 是连通数组 Mx4，包含索引 4 个四面体顶点的行条目。取自模拟区域
  * vtx 是具有四面体网格顶点的矩阵 Nx3，包含 (x,y,z) 对的行条目。取自模拟区域
  * extrap_val（可选）：如果插值点在有限元网格之外，该点将被分配此值（默认为 Inf）

**示例**

请参阅 interptri 脚本函数的示例。

**相关命令**

- [quadtet](./quadtet.md)
- [quadtri](./quadtri.md)
- [interptri](./interptri.md)
