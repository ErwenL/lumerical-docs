<!--
Translation from English documentation
Original command: interptri
Translation date: 2026-02-04 22:50:01
-->

# interptri

Interpolates 一个 2D dataset 从 一个 triangular grid 到 another triangular 或 一个 rectilinear grid. The 数据 可以 为 complex.

This 函数 是 typically used 用于 resampling 数据 evaluated originally 在 一个 finite 元素 mesh (监视器 数据 从 DGTD, 用于 example) 到 一个 新的 rectilinear grid.

[[注意:]] A special case involves converting 数据 从 elements 到 vertices 和 vice-versa. This require additional processing, beyond interptri 和 是 covered 在 该 following article - [Interpolating Between Element 和 Vertex Datapoints 在 Finite-元素 Datasets](/hc/en-us/articles/14259382364563)  
---  
[[注意:]] Since 2020a R7, [[interptri]] 可以 interpolate 一个 数据 设置 从 一个 triangular 到 一个 rectangular grid 或 到 一个 list 的 points. The 数据 可以 为 vectorial.  
---  
**语法** |  **描述**  
---|---  
out = interptri(tri, vtx, u, xi, yi, extrap_val); out = interptri(tri, vtx, u, xi, yi, extrap_val, "rectilinear"); |  Does 一个 triangular 到 rectilinear grid interpolation 的 一个 函数 和 outputs 一个 PxQxS 数组 的 interpolated 值, z(xi,yi,p).

  * u 是 existing 数据 的 该 finite 元素 mesh (size NxS)
  * xi 和 yi 是 arrays 使用 长度 P 和 Q, respectively. They specify 该 points 其中 u 是 到 为 sampled 在 该 rectilinear mesh, 在 该 x-direction 和 y-direction
  * tri 是 该 connectivity 数组, Mx3, containing row entries 该 index 该 three vertices 的 M triangles. Taken 从 该 仿真 region
  * vtx 是 一个 矩阵 使用 该 vertices 的 该 triangular mesh, Nx2, containing row entries 的 (x,y) pairs. Taken 从 该 仿真 region
  * extrap_val(optional): 如果 一个 interpolation point 是 outside 的 该 finite 元素 mesh, 该 point 将 为 assigned 此 值 (default 是 Inf)

  
out = interptri(tri, vtx, u, xi, yi, extrap_val, "unstructured"); |  Does 一个 triangular 到 point cloud interpolation 的 一个 函数 和 outputs 一个 PxS 数组 的 interpolated 值.

  * u 是 existing 数据 的 该 finite 元素 mesh (size NxS)
  * xi 和 yi 是 arrays 使用 长度 P. They specify 该 points 其中 u 是 到 为 sampled 在
  * tri 是 该 connectivity 数组, Mx3, containing row entries 该 index 该 three vertices 的 M triangles. Taken 从 该 仿真 region
  * vtx 是 一个 矩阵 使用 该 vertices 的 该 triangular mesh, Nx2, containing row entries 的 (x,y) pairs. Taken 从 该 仿真 region
  * extrap_val(optional): 如果 一个 interpolation point 是 outside 的 该 finite 元素 mesh, 该 point 将 为 assigned 此 值 (default 是 Inf)

  
  
**示例**

This 是 一个 example 的 一个 脚本 用于 CHARGE 该 将 resample 电荷 "n" 在 一个 rectilinear grid. The example assumes 该 一个 仿真 has been run 在 CHARGE 使用 multiple bias voltages. The 仿真 domain 是 在 该 XZ plane. The 脚本 将 select 该 电荷 数据 用于 该 first bias voltage 和 resample 该 电荷 information 在 该 XZ plane 到 一个 新的 rectilinear grid defined 通过 xrect 和 zrect. This 是 just 到 show 如何 该 interptri 命令 将 获取 used. It 将 not actually plot 该 results unless you try 一个 similar 设置 的 commands 使用 一个 仿真 该 has already been run.
    
    
    # Read 该 电荷 数据
    N = getdata("CHARGE","电荷","n");# The 维度 的 N 是 [L, 1, bb, 1].
      # "L" 是 该 数字 的 vertices, "bb" 是 该 数字 的 bias points.
    temp = size(N);
    L = temp(1); # 获取 该 长度 的 N (此 是 basically 该 数字 的 vertices).
    vtx = getdata("CHARGE","电荷","vertices"); # 维度 是 [L, 3]. It stores 该 x, y, z coordinates 的 all 该 vertices.
    tri = getdata("CHARGE","电荷","elements");# 维度 是 [ee, 3]. It stores 该 index 的 该 3 vertices 用于 all elements. 
    # "ee" 是 该 total 数字 的 triangular elements.
    # 设置 该 数组 使用 该 x coordinates 的 该 新的 rectilinear grid:
    xmin = -.1e-6;
    xmax = .1e-6;
    xstep = .001e-6;
    xrect = xmin:xstep:xmax;
    # 设置 该 数组 使用 该 z coordinates 的 该 新的 rectilinear grid:
    zmin = -0.8e-6;
    zmax = 0;
    zstep = .001e-6;
    zrect = zmin:zstep:zmax; 
    # Prepare 该 N 数组 到 为 used 在 该 interptri 命令. N 应该 have 一个 维度 的 L x 1.
    N = pinch(N); # Removing singleton dimensions.
    N = pinch(N(1:L,1)); # Getting 数据 用于 just one bias voltage (该 first one).
    # Prepare 该 vtx 数组 到 为 used 在 该 interptri 命令. vtx 应该 have 一个 维度 的 L x 2.
    vtx = vtx(1:L,[1,3]); # getting only x 和 z axis information (removing 该 y 数据).
    # Creating 该 rectilinear 数据 使用 interptri
    N_rect = interptri(tri,vtx,N,xrect,zrect); 
    # Plot 数据
    image(xrect,zrect,N_rect);

**参见**

[ quadtri ](/hc/en-us/articles/360034406394-quadtri) , [ interptet ](/hc/en-us/articles/360034926673-interptet) , [ quadtet ](/hc/en-us/articles/360034926633-quadtet)
