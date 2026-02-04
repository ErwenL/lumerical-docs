<!--
Translation from English documentation
Original command: near2far
Translation date: 2026-02-04 22:50:14
-->

# near2far

计算 该 far field at 该 specified points 使用 该 provided near field 监视器 数据. 

**语法** |  **描述**  
---|---  
out = near2far(nearfield, farfield, n);  |  计算 该 far field 使用 该 provided near field 监视器 数据 at 该 specified far field points. The input unstructured 数据 设置 specifying 该 near fields 必须 contain 一个 attribute named 'E' parametrized 通过 频率. The output 是 一个 unstructured 数据 设置 使用 一个 attribute named 'E' containing 该 far field. The far field frequencies 是 determined 通过 该 near field frequencies while 该 far field points, connectivity 矩阵 和 surface normals associated 使用 该 output 数据 设置 是 taken 从 该 unstructured 数据 设置 specifying 该 far field points.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
nearfield  |  required  |  |  unstructured 数据 设置  |  Near field 数据 在 该 format returned 通过 DFT monitors. The electric field 可以 为 sampled 在 一个 segmented line 或 在 一个 triangulated surface. If sampled 在 一个 segmented line, 该 electric field 是 assumed 到 come 从 一个 2D 仿真 和 该 2D integral kernel 是 used 用于 该 far field projection. Similarly, 如果 该 electric field 是 sampled 在 一个 triangulated surface, it 是 assumed 到 come 从 一个 3D 仿真 和 该 3D integral kernel 是 used 用于 该 projection (see 该 provided reference).   
farfield  |  required  |  |  unstructured 数据 设置  |  Far field points 到 为 used 在 该 projection. If 该 near fields 是 sampled 在 segmented line, 该 far field points 必须 为 specified 使用 一个 segmented line. Similarly, 如果 该 near fields 是 sampled 在 一个 triangulated surface, 该 far field points 必须 为 sampled 在 一个 triangulated surface. The 命令  createsphericalsurface  可以 为 used 到 easily 创建 一个 unstructured 数据 设置 使用 一个 segmented line 或 一个 triangulated surface.   
n  |  optional  |  1.0  |  数字 或 向量  |  Background refractive index 的 该 far field medium. It 可以 为 一个 single 数字 或 一个 向量 使用 该 same 长度 as 该 near field 频率 参数.   
  
注意: Far field integration  For integration 的 far field over 一个 range 的 angles, 该 脚本 命令  quadtri  可以 为 used. See [ quadtri ](/hc/en-us/articles/360034406394-quadtri) 用于 more information.   
---  
  
**示例**

This example performs 一个 far field projection 在 一个 sphere 使用 该 near field 数据 collected 从 一个 监视器 named "监视器". 
    
    
    surf = createsphericalsurface;
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

For more information 在 如何 far field projections 是 computed please refer 到: 

John B. Schneider, Understanding the Finite-Difference Time-Domain Method, Chapter 14: Near-to-Far-Field Transformation, 2010 Available at: [ http://www.eecs.wsu.edu/~schneidj/ufdtd/ ](http://www.eecs.wsu.edu/~schneidj/ufdtd/)

**参见**

[ createsphericalsurface ](/hc/en-us/articles/360034930773-createsphericalsurface) , [ List 的 commands ](/hc/en-us/articles/360037228834) , 
