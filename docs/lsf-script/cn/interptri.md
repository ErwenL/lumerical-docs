<!--
Translation from English documentation
Original command: interptri
Translation date: 2026-02-03
-->

# interptri

将数据集从三角形网格插值到另一个三角形或规则网格。数据可以是复数。

此函数通常用于对最初在有限元网格中评估的数据（例如来自 DGTD 的监视器数据）重新采样到新的规则网格。

**注意：** 一种特殊情况涉及在元素和顶点之间转换数据。这需要额外的处理，超出了 interptri 的范围，在以下文章中有详细介绍 - 有限元数据集中元素和顶点数据点之间的插值

**注意：** 自 2020a R7 起，interptri 可以将数据集从三角形插值到矩形网格或点列表。数据可以是矢量的。

**语法** |  **描述**
---|---
out = interptri(tri, vtx, u, xi, yi, extrap_val); out = interptri(tri, vtx, u, xi, yi, extrap_val, "rectilinear");  |  对函数进行三角形到规则网格插值，并输出 PxQxS 数组的插值 z(xi,yi,p)。

  * u 是有限元网格的现有数据（大小 NxS）
  * xi 和 yi 分别是长度 P 和 Q 的数组。它们指定在规则网格上在 x 方向和 y 方向上对 u 进行采样的点
  * tri 是连通数组 Mx3，包含索引 M 个三角形三个顶点的行条目。取自模拟区域
  * vtx 是具有三角形网格顶点的矩阵 Nx2，包含 (x,y) 对的行条目。取自模拟区域
  * extrap_val（可选）：如果插值点在有限元网格之外，该点将被分配此值（默认为 Inf）

out = interptri(tri, vtx, u, xi, yi, extrap_val, "unstructured");  |  对函数进行三角形到点云插值，并输出 PxS 数组的插值。

  * u 是有限元网格的现有数据（大小 NxS）
  * xi 和 yi 是长度为 P 的数组。它们指定要对其采样的点
  * tri 是连通数组 Mx3，包含索引 M 个三角形三个顶点的行条目。取自模拟区域
  * vtx 是具有三角形网格顶点的矩阵 Nx2，包含 (x,y) 对的行条目。取自模拟区域
  * extrap_val（可选）：如果插值点在有限元网格之外，该点将被分配此值（默认为 Inf）

**示例**

这是一个用于 CHARGE 的脚本示例，将电荷 "n" 在规则网格上重新采样。该示例假设已在 CHARGE 中运行了具有多个偏置电压的模拟。模拟域在 XZ 平面上。脚本将为第一个偏置电压选择电荷数据，并将 XZ 平面上的电荷信息重新采样到由 xrect 和 zrect 定义的新规则网格。这只是为了展示如何使用 interptri 命令。除非您尝试使用已运行的模拟运行类似的命令集，否则它不会实际绘制结果。

    # Read the charge data
    N = getdata("CHARGE","charge","n");# The dimension of N is [L, 1, bb, 1].
      # "L" is the number of vertices, "bb" is the number of bias points.
    temp = size(N);
    L = temp(1); # get the length of N (this is basically the number of vertices).
    vtx = getdata("CHARGE","charge","vertices"); # dimension is [L, 3]. It stores the x, y, z coordinates of all the vertices.
    tri = getdata("CHARGE","charge","elements");# dimension is [ee, 3]. It stores the index of the 3 vertices for all elements.
    # "ee" is the total number of triangular elements.
    # Set the array with the x coordinates of the new rectilinear grid:
    xmin = -.1e-6;
    xmax = .1e-6;
    xstep = .001e-6;
    xrect = xmin:xstep:xmax;
    # Set the array with the z coordinates of the new rectilinear grid:
    zmin = -0.8e-6;
    zmax = 0;
    zstep = .001e-6;
    zrect = zmin:zstep:zmax;
    # Prepare the N array to be used in the interptri command. N should have a dimension of L x 1.
    N = pinch(N); # Removing singleton dimensions.
    N = pinch(N(1:L,1)); # Getting data for just one bias voltage (the first one).
    # Prepare the vtx array to be used in the interptri command. vtx should have a dimension of L x 2.
    vtx = vtx(1:L,[1,3]); # getting only x and z axis information (removing the y data).
    # Creating the rectilinear data using interptri
    N_rect = interptri(tri,vtx,N,xrect,zrect);
    # Plot data
    image(xrect,zrect,N_rect);

**相关命令**

- [quadtri](./quadtri.md)
- [interptet](./interptet.md)
- [quadtet](./quadtet.md)
