<!--
Translation from English documentation
Original command: farfieldexact3d
Translation date: 2026-02-04 22:49:48
-->

# farfieldexact3d

The three 维度 form 的 farfieldexact2d. This 函数 projects complete complex 向量 fields 到 specific locations. It 是 expected 到 为 correct down 到 distances 在 该 order 的 one 波长. The projections 从 multiple monitors 可以 为 added 到 创建 一个 total far field projection - see [ Projections 从 一个 监视器 box ](/hc/en-us/articles/360034915613-Projections-从-一个-监视器-box) .

farfieldexact3d projects any surface 到 该 grid points defined 通过 该 vectors x,y 和 z. If only E field 是 returned as 该 result, 该 数据 是 returned 在 一个 矩阵 的 维度 NxMxKx3 如果 one 频率 point 是 projected, 和 NxMxKx3xP 如果 more than one 频率 point 是 projected 其中 N 是 该 长度 的 该 向量 x, M 该 长度 的 该 向量 y, K 是 该 长度 的 该 向量 z, P 是 该 数字 的 频率 points, 和 该 fourth index represents Ex, Ey, 和 Ez. 注意 该 N, M 和 K 可以 为 1, 和 当 they 是 all 1, 该 函数 是 该 same as farfieldexact. If both E 和 H fileds 是 returned, 该 数据 是 returned as 一个 dataset 使用 该 E 和 H fields packaged 使用 该 对应的 x,y,z 和 频率/波长.

**语法** |  **描述**  
---|---  
out = farfieldexact3d( "mname", x, y, z, f, index); |  Projects 一个 given power 或 field profile 监视器 到 该 far field at grid points specified 通过 该 vectors x,y,z. 返回 E field only.  
out = farfieldexact3d( dataset, x, y, z, f, index); |  Projects 一个 given rectilinear dataset 到 该 far field at grid points specified 通过 该 vectors x,y,z. 返回 E field only.  
out = farfieldexact3d( "mname", x, y, z, opt); |  Projects 一个 given power 或 field profile 监视器 到 该 far field at grid points specified 通过 该 vectors x,y,z. 返回 E field 或 E 和 H fields. Refer 到 该 table below 用于 该 options.  
out = farfieldexact3d( dataset, x, y, z, opt); |  Projects 一个 given rectilinear dataset 到 该 far field at grid points specified 通过 该 vectors x,y,z. 返回 E field 或 E 和 H fields. Refer 到 该 table below 用于 该 options.  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  name 的 该 监视器 从 该 far field 是 calculated  
x |  required |  |  向量 |  x coordinates 的 该 grid points 其中 far field 是 calculated  
y |  required |  |  向量 |  y coordinates 的 该 grid points 其中 far field 是 calculated  
z |  required |  |  向量 |  z coordinates 的 该 grid points 其中 far field 是 calculated  
f |  optional | 1 |  向量 |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multithreaded projection was introduced since R2016b.  
index |  optional | 值 at 监视器 centre |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
opt |  optional |  |  结构体 |  该 'opt' 参数 includes 该 following options: "field": This 参数 是 optional. It defines 该 返回 field, 可以 either 为 "E" 或 "E 和 H". "f": This 参数 是 optional. It defines 该 index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multi-threaded projection was introduced since R2016b. "index": This 参数 是 optional. It defines 该 index 的 该 材料 到 use 用于 该 projection.  
  
[[注意:]] When 使用 一个 dataset, 该 default 值 的 该 refractive index 是 1.

**示例**

This 3D example 计算 该 far field electric field intensity 在 一个 2mm x 2mm image plane located 一个 distance 的 z=+1.5mm 从 该 仿真 region. For 该 example 的 far field projection 的 一个 rectilinear dataset see [farfield3d](/hc/en-us/articles/360034930693-farfield3d). 
    
    
    mname="trans";    # Monitor name
    num=25;       # resolution
    # define far field plane 到 image fields
    x=linspace(-1e-3,1e-3,num); 
    y=x;
    z=1.5e-3;
    # compute far field
    E=farfieldexact3d(mname,x,y,z,{"field":"E"}); 
    # select component
    Ex=pinch(E,4,1); 
    Ey=pinch(E,4,2);
    Ez=pinch(E,4,3);
    # image intensity
    E2= abs(Ex)^2 + abs(Ey)^2 + abs(Ez)^2;
    image(x*1e3,y*1e3,E2,"x (mm)","y (mm)","Electric field at z=1.5mm 从 源"); 

The following example shows 如何 farfieldexact 和 farfieldexact3d output 数据 differently.

When x=[1 2], y=[1 2], z=[0],

farfieldexact: The result 是 一个 2*3 矩阵. First 维度 是 position;second 是 field component. This 计算 该 far field at 该 positions [1,1,0] 和 [2,2,0] .

farfielexact3d: The result 是 一个 2*2*1*3 矩阵. First three dimensions 是 positions; 该 fourth 维度 是 field component. This 计算 该 far field at 该 positions [x,y,z] = [1,1,0], [1,2,0], [2,1,0], [2,2,0].
    
    
    x=1:2;
    y=1:2;
    z=0;
    m="监视器";
    E_far=farfieldexact3d(m,x,y,z,{"field":"E"});
    ?size(E_far);
     result: 
     2 2 1 3  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldexact2d ](/hc/en-us/articles/360034410234-farfieldexact2d) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact)
