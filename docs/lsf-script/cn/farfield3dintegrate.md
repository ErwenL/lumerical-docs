<!--
Translation from English documentation
Original command: farfield3dintegrate
Translation date: 2026-02-04 22:49:48
-->

# farfield3dintegrate

Integrates 该 far field projection over 一个 cone centered at theta0 和 phi0, 使用 一个 width specified 通过 halfangle 用于 3D simulations. The far field electric field 是 一个 函数 的 该 direction cosines (ux,uy), but farfield3dintegrate automatically does 该 change 的 variables. Similarly, angles 是 specified 在 degrees, but converted 到 radians before 该 integral 是 calculated. See 该 farfield3d documentation 用于 information 在 interpreting ux, uy, na, nb 用于 various 监视器 orientations. 

$$ \iint_{\theta, \phi} E^{2}(u x, u y) \sin (\theta) d \theta d \phi $$ 

**语法** |  **描述**  
---|---  
out = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0);  |  Integrate 3D far field projection 数据.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
E2  |  required  |  |  矩阵  |  E field 数据 从 farfield3d   
ux  |  required  |  |  向量  |  ux 数据 从 farfieldux. 注意 该 该 result 应该 为 一个 向量, so it 是 sufficient 到 perform 该 farfieldux 脚本 命令 用于 only 1 频率 point.   
uy  |  required  |  |  向量  |  uy 数据 从 farfielduy. 注意 该 该 result 应该 为 一个 向量, so it 是 sufficient 到 perform 该 farfieldux 脚本 命令 用于 only 1 频率 point.   
halfangle  |  optional  |  90  |  向量  |  Half angle 的 该 integration cone. unit 在 degrees. 必须 have 长度 L 或 1. Half angle 应该 为 between 0 到 90 degrees.   
theta0  |  optional  |  0  |  向量  |  Center angle theta 的 该 integration cone. unit 在 degrees. 必须 have 长度 L 或 1. Theta0 应该 为 between 0 到 90 degrees.   
phi0  |  optional  |  0  |  向量  |  Center angle phi 的 该 integration cone. unit 在 degrees. 必须 have 长度 L 或 1. Phi0 应该 为 between 0 到 360 degrees.   
  
**示例**

计算 该 fraction 的 power 从 该 源 该 是 transmitted into 该 far field within 在 一个 30 degree cone centered at theta=phi=0. 
    
    
    m="monitor1";
    res = 201;
    E2 = farfield3d(m,1,res,res);
    ux = farfieldux(m,1,res,res);
    uy = farfielduy(m,1,res,res);
    halfangle=30;
    theta0=0;
    phi0=0;
    cone_30 = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); # integrate over 30 degree cone
    total = farfield3dintegrate(E2, ux, uy); # integrate over entire hemisphere
    T   = transmission(m); # fraction 的 源 power transmitted into far field 
    ?cone_30/total;  # fraction 的 far field power within 一个 30 degree cone
    ?cone_30/total*T; # fraction 的 源 power transmitted into 该 far field within 一个 30 degree cone

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ farfieldspherical ](/hc/en-us/articles/360034410194-farfieldspherical)
