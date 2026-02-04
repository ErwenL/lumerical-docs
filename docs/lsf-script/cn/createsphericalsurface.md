<!--
Translation from English documentation
Original command: createsphericalsurface
Translation date: 2026-02-04 22:49:48
-->

# createsphericalsurface

创建 一个 triangulated spherical surface 或 一个 segmented circular arc. It 可以 为 used 到 define 该 far-field points 用于 一个 far field projection as 这些 是 often specified 使用 一个 spherical surface (3D simulations) 或 一个 circular arc (2D simulations). 

**语法** |  **描述**  
---|---  
out = createsphericalsurface([theta1,theta2],[phi1,phi2], [X,Y,Z],radius,lmax);  |  创建 一个 unstructured 数据 设置 使用 一个 triangulated surface 或 一个 segmented arc. Their dimensions 是 specified 通过 该 input angles, orientation axis 和 radius. The coarseness 的 该 triangulation (或 line segmentation) 是 specified as 该 maximum separation between adjacent points. The output 数据 设置 contains 该 IDs 的 each 元素 (triangles 或 lines) 和 该 对应的 areas (only 用于 triangles).   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
theta1  |  optional  |  0  |  数字  |  Starting 值 的 该 elevation angle (theta) range 在 radians 使用 respect 到 该 reference axis.   
theta2  |  optional  |  pi  |  数字  |  End 值 的 该 elevation angle (theta) range 在 radians 使用 respect 到 该 reference axis.   
phi1  |  optional  |  0  |  数字  |  Starting 值 的 该 azimuthal angle (phi) range 在 radians 使用 respect 到 该 reference axis.   
phi2  |  optional  |  2*pi  |  数字  |  End 值 的 该 azimuthal angle (phi) range 在 radians 使用 respect 到 该 reference axis.   
[X,Y,Z]  |  optional  |  [0,0,1]  |  向量  |  Orientation axis: [1,0,0] 用于 X-axis, [0,1,0] 用于 Y-axis 和 [0,0,1] 用于 Z-axis.   
radius  |  optional  |  1  |  数字  |  Radius 的 该 sphere 或 arc 到 为 created 在 米.   
lmax  |  optional  |  0.2  |  数字  |  Maximum separation between two adjacent 数据 points 在 far field location 在 米.   
  
**示例 1**

This example 创建 一个 spherical surface 和 performs 一个 far field projection 使用 该 near field 数据 从 一个 surface 监视器 named "监视器". 
    
    
    surf = createsphericalsurface([0,pi/4],[0,2*pi],[0,0,1],1,0.1);
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

**示例 2**

This example 创建 一个 arc (在 该 XZ plane) 和 performs 一个 far field projection 使用 该 near field 数据 从 一个 line 监视器 called "监视器" (also 在 该 XZ plane). 
    
    
    surf = createsphericalsurface([pi/2,pi/2],[pi,2*pi],[0,1,0],1,0.1);
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

**参见**

[ near2far ](/hc/en-us/articles/360034930753-near2far) , [ List 的 commands ](/hc/en-us/articles/360037228834) , 
