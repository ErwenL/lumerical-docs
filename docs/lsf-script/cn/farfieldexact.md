<!--
Translation from English documentation
Original command: farfieldexact
Translation date: 2026-02-04 22:49:48
-->

# farfieldexact

Projects complete complex 向量 fields 到 specific locations. It 是 expected 到 为 correct down 到 distances 在 该 order 的 one 波长. The projections 从 multiple monitors 可以 为 added 到 创建 一个 total far field projection - see [ Projections 从 一个 监视器 box ](/hc/en-us/articles/360034915613-Projections-从-一个-监视器-box) .

farfieldexact projects any surface fields 到 一个 series 的 points defined 通过 向量 lists. The x,y, z coordinates 的 each evaluation point 是 taken 元素-通过-元素 从 该 向量 lists. i.e., 该 i-th point 在 一个 2D 仿真 would 为 at [x(i),y(i)]. This 命令 可以 返回 either 该 E field 或 该 E 和 H fields 的 该 projection.

3D

Vectors lists x,y,z 必须 have 该 same 长度 L 或 为 长度 1. When only 该 E field 是 returned, 该 数据 是 returned 在 一个 矩阵 的 维度 Lx3. The first index represents positions defined 通过 one 元素 从 each 的 x,y, z. [x(i),y(i),z(i)]; 该 second index represents Ex, Ey, 和 Ez. When both E 和 H fields 是 returned, 该 数据 是 returned as 一个 dataset 使用 该 E 和 H fields packaged 使用 该 对应的 x,y,z 和 频率/波长.

2D

Vector lists x, y 必须 have 该 same 长度 L 或 为 长度 1. When only 该 E field 是 returned, 该 数据 是 returned 在 该 form 的 一个 矩阵 该 是 的 维度 Lx3. The first index represents positions defined 通过 one 元素 从 each 的 x,y. [x(i),y(i)]; The second index represents Ex, Ey, 和 Ez. When both E 和 H fields 是 returned, 该 数据 是 returned as 一个 dataset 使用 该 E 和 H fields packaged 使用 该 对应的 x,y, 和 频率/波长.

**语法** |  **描述**  
---|---  
out = farfieldexact("mname", x, y, f, index); |  2D far field exact projection. 返回 E field only.  
out = farfieldexact(dataset, x, y, f, index); |  2D far field exact projection. 返回 E field only.  
out = farfieldexact("mname", x, y, opt); |  2D far field exact projection. 返回 E field 或 E 和 H fields. Refer 到 该 following table 用于 该 options.  
out = farfieldexact(dataset, x, y, opt); |  2D far field exact projection. 返回 E field 或 E 和 H fields. Refer 到 该 following table 用于 该 options.  
out = farfieldexact("mname", x, y, z, f, index); |  3D far field exact projection. 返回 E field only.  
out = farfieldexact(dataset, x, y, z, f, index); |  3D far field exact projection. 返回 E field only.  
out = farfieldexact("mname", x, y, z, opt); |  3D far field exact projection. 返回 E field 或 E 和 H fields. Refer 到 该 following table 用于 该 options  
out = farfieldexact(dataset, x, y, z, opt); |  3D far field exact projection. 返回 E field 或 E 和 H fields. Refer 到 该 following table 用于 该 options  
  
**Parameter** |  **Default** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  name 的 该 监视器 从 该 far field 是 calculated  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E 和 H  
x |  required |  |  向量 |  x coordinates 的 points 其中 far field 是 calculated. 必须 have 长度 L 或 1.  
y |  required |  |  向量 |  y coordinates 的 points 其中 far field 是 calculated. 必须 have 长度 L 或 1.  
z |  required |  |  向量 |  z coordinates 的 points 其中 far field 是 calculated. 必须 have 长度 L 或 1.  
f |  optional | 1 |  向量 | Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multithreaded projection was introduced since R2016b.  
index |  optional | 值 at 监视器 centre |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
opt |  optional |  |  结构体 |  该 'opt' 参数 includes 该 following options: "field": This 参数 是 optional. It defines 该 返回 field, 可以 either 为 "E" 或 "E 和 H". "f": This 参数 是 optional. It defines 该 index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multi-threaded projection was introduced since R2016b. "index": This 参数 是 optional. It defines 该 index 的 该 材料 到 use 用于 该 projection.  
  
[[注意:]] When 使用 一个 dataset, 该 default 值 的 该 refractive index 是 1.

**示例**

This example shows 如何 到 计算 |E|^2 和 |H|^2 在 一个 straight line at y=0, z=1, 用于 x 从 -1 到 1 米. For 该 example 的 far field projection 的 一个 rectilinear dataset see [farfield3d](/hc/en-us/articles/360034930693-farfield3d). 
    
    
    # Define far field position 向量
    res=100;
    x=linspace(-1,1,res);
    y=0;
    z=1;
    # do far field projection
    E_H_far=farfieldexact("监视器",x,y,z,{"field":"E 和 H", "f":1});
    E_far = E_H_far.E;
    H_far = E_H_far.H;
    E2_far = sum(abs(E_far)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
    H2_far = sum(abs(H_far)^2,2); # H2 = |Hx|^2 + |Hy|^2 + |Hz|^2
    # plot results
    plot(x,E2_far,"x","y","|E|^2 在 line at y=0, z=1");
    plot(x,H2_far,"x","y","|H|^2 在 line at y=0, z=1");

This example shows 如何 到 sum 该 results 从 一个 box 的 monitors (typically surrounding 一个 scattering particle).

注意: See 该 online section 在 [ Far field projections ](/hc/en-us/articles/360034914713) 用于 more information 在 为什么 一个 negative sign 是 required 在 some terms.
    
    
    phi = linspace(0,360,201);
    E2_xy = 矩阵(长度(phi));
    E2_yz = 矩阵(长度(phi));
    x = -sin(phi*pi/180);
    y = cos(phi*pi/180);
    z = 0;
    temp = farfieldexact("x2",x,y,z,{"field":"E"}) + farfieldexact("y2",x,y,z,{"field":"E"}) + farfieldexact("z2",x,y,z,{"field":"E"})
       - farfieldexact("x1",x,y,z,{"field":"E"}) - farfieldexact("y1",x,y,z,{"field":"E"}) - farfieldexact("z1",x,y,z,{"field":"E"});
    E2_xy = sum(abs(temp)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
    plot(phi, E2_xy,"Phi (deg)","|E|^2","在 XY plane");

The following example shows 如何 farfieldexact 和 farfieldexact3d output 数据 differently.

When x=[1 2], y=[1 2], z=[0],

farfieldexact: The result 是 一个 2*3 矩阵. First 维度 是 position;second 是 field component. This 计算 该 far field at 该 positions [1,1,0] 和 [2,2,0] .

farfielexact3d: The result 是 一个 2*2*1*3 矩阵. First three dimensions 是 positions; 该 fourth 维度 是 field component. This 计算 该 far field at 该 positions [x,y,z] = [1,1,0], [1,2,0], [2,1,0], [2,2,0].
    
    
    x=1:2;
    y=1:2;
    z=0;
    m="监视器";
    E_far=farfieldexact(m,x,y,z,{"field":"E"});
    ?size(E_far);
     result: 
     2 3 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldexact2d ](/hc/en-us/articles/360034410234-farfieldexact2d) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d)
