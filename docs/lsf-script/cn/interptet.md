<!--
Translation from English documentation
Original command: interptet
Translation date: 2026-02-04 22:50:01
-->

# interptet

Interpolates 一个 3D dataset 从 一个 tetrahedral grid 到 another tetrahedral 或 一个 rectilinear grid. The 数据 可以 为 complex.

This 函数 是 typically used 用于 resampling 数据 evaluated originally 在 一个 finite 元素 mesh (监视器 数据 从 CHARGE, 用于 example) 到 一个 新的 rectilinear grid.

[[注意:]] Since 2020a R7, [[interptet]] 可以 interpolate 一个 数据 设置 从 一个 tetrahedral 到 一个 rectangular grid 或 到 一个 list 的 points. The 数据 可以 为 vectorial.  
---  
**语法** |  **描述**  
---|---  
out = interptet(tet, vtx, u, xi, yi, zi, extrap_val); out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "rectilinear"); |  Does 一个 tetrahedral 到 rectilinear interpolation 的 一个 函数 和 outputs 一个 PxQxRxS 数组 的 interpolated 值, f(xi,yi,zi,p).

  * u 是 existing 数据 的 该 finite 元素 mesh (NxS)
  * xi, yi 和 zi 是 arrays 使用 长度 P, Q 和 R, respectively. They specify 该 points 其中 u 是 到 为 sampled 在 该 rectilinear mesh, 在 该 x-direction, y-direction 和 z-direction
  * tet 是 该 connectivity 数组, Mx4, containing row entries 该 index 该 4 vertices 的 M tetrahedra. Taken 从 该 仿真 region
  * vtx 是 一个 矩阵 使用 该 vertices 的 该 tetrahedral mesh, Nx3, containing row entries 的 (x,y,z) pairs. Taken 从 该 仿真 region
  * extrap_val(optional): 如果 一个 interpolation point 是 outside 的 该 finite 元素 mesh, 该 point 将 为 assigned 此 值 (default 是 Inf)

  
out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "unstructured");  |  Does 一个 tetrahedral 到 point cloud interpolation 的 一个 函数 和 outputs 一个 PxS 数组 的 interpolated 值.

  * u 是 existing 数据 的 该 finite 元素 mesh (NxS)
  * xi, yi 和 zi 是 arrays 使用 长度 P. They specify 该 P points 其中 u 是 到 为 sampled 在
  * tet 是 该 connectivity 数组, Mx4, containing row entries 该 index 该 4 vertices 的 M tetrahedra. Taken 从 该 仿真 region
  * vtx 是 一个 矩阵 使用 该 vertices 的 该 tetrahedral mesh, Nx3, containing row entries 的 (x,y,z) pairs. Taken 从 该 仿真 region
  * extrap_val(optional): 如果 一个 interpolation point 是 outside 的 该 finite 元素 mesh, 该 point 将 为 assigned 此 值 (default 是 Inf)

  
  
**示例**

See 该 example 用于 该 interptri 脚本 函数.

**参见**

[quadtet](/hc/en-us/articles/360034926633-quadtet), [quadtri](/hc/en-us/articles/360034406394-quadtri), [interptri](/hc/en-us/articles/360034405774-interptri)
