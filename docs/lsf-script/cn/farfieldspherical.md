<!--
Translation from English documentation
Original command: farfieldspherical
Translation date: 2026-02-04 22:49:49
-->

# farfieldspherical

Interpolates far field 数据 (3D simulations) 从 E(ux,uy) 到 spherical coordinates E(theta,phi) 1D 数组. The far field projections functions generally 返回 该 projection as 一个 函数 的 ux,uy (direction cosines). farfieldspherical 可以 为 used 到 interpolate 此 数据 into 该 more common units 的 theta, phi. See 该 farfield3d documentation 用于 information 在 interpreting ux, uy, na, nb 用于 various 监视器 orientations.

**语法** |  **描述**  
---|---  
out = farfieldspherical( E2, ux, uy, theta, phi); |  Interpolate far field 数据 到 spherical coordinates. The output has 一个 size 的 (MxN,1)  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
E2 |  required |  |  矩阵 |  E field 数据 从 farfield3d  
ux |  required |  |  向量 |  ux 数据 从 farfieldux. 注意 该 该 result 应该 为 一个 向量, so it 是 sufficient 到 perform 该 farfieldux 脚本 命令 用于 only 1 频率 point.  
uy |  required |  |  向量 |  uy 数据 从 farfielduy. 注意 该 该 result 应该 为 一个 向量, so it 是 sufficient 到 perform 该 farfieldux 脚本 命令 用于 only 1 频率 point.  
theta |  required |  |  向量 |  theta 向量, 在 degrees. Must have 长度 M 或 1.  
phi |  required |  |  向量 |  phi 向量, 在 degrees. Must have 长度 N 或 1.  
  
**示例**

创建 一个 plot 的 该 E2_far vs theta, 用于 phi=0.
    
    
    m="Monitor1";  # Monitor name
    res = 201;    # projection resolution
    E2 = farfield3d(m,1,res,res);
    ux = farfieldux(m,1,res,res);
    uy = farfielduy(m,1,res,res);
    theta = linspace(-90,90,100); 
    phi = 0;
    plot(theta, farfieldspherical(E2,ux,uy,theta,phi) ,"theta", "E^2", "E^2 at phi=0");

Interpolate field 数据 到 一个 grid 的 theta 和 phi angles.
    
    
    theta = linspace(-90,90,10);
    phi = linspace(0,45,11);
    Theta = meshgridx(theta,phi);
    Phi = meshgridy(theta,phi);
    E2_angle = farfieldspherical(E2,ux,uy,Theta,Phi);  
    E2_angle = reshape(E2_angle, [长度(theta), 长度(phi)]);  
    image(theta, phi, E2_angle, "theta","phi","E2");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ Far field projections - Direction unit 向量 coordinates ](/hc/en-us/articles/360034394294-FFP-Direction-unit-向量-coordinates) , [ meshgridx ](/hc/en-us/articles/360034409334-meshgridx) , [ meshgridy ](/hc/en-us/articles/360034929673-meshgridy)
