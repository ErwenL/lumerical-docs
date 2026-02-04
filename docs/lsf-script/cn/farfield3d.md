<!--
Translation from English documentation
Original command: farfield3d
Translation date: 2026-02-04 22:49:48
-->

# farfield3d

Projects 一个 given power 或 field profile 监视器 或 一个 rectilinear dataset 到 该 far field 在 一个 3D 仿真. The electric field intensity |E|  2  是 returned.

**语法** |  **描述**  
---|---  
out = farfield3d("mname",f, na, nb, illumination, periodsa, periodsb, index, direction); |  Projects 一个 given power 或 field profile 监视器 到 该 far field. This 返回 一个 NxM 矩阵 如果 1 频率 point 是 projected, 或 一个 NxMxP 矩阵 如果 more than 1 频率 point 是 projected, 其中 N 和 M correspond 到 该 resolution 的 该 projection (na, 和 nb), 和 P corresponds 到 该 数字 的 频率 points projected.  
out = farfield3d(dataset,f, na, nb, illumination, periodsa, periodsb, index, direction); |  Projects 一个 given rectilinear dataset 到 该 far field. This 返回 一个 NxM 矩阵 如果 1 频率 point 是 projected, 或 一个 NxMxP 矩阵 如果 more than 1 频率 point 是 projected, 其中 N 和 M correspond 到 该 resolution 的 该 projection (na, 和 nb), 和 P corresponds 到 该 数字 的 频率 points projected.  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  Name 的 该 监视器  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E 和 H  
f |  optional |  1 |  向量 |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multithreaded projection 到 allow multiple 频率 points 到 为 projected simultaneously was introduced 在 R2016b.  
na |  optional |  150 |  数字 |  The 数字 的 points 在 该 far field.  
nb |  optional |  150 |  数字 |  The 数字 的 points 在 该 far field.  
illumination |  optional |  1 |  数字 |  For periodic structures. Gaussian illumination: 1 Plane wave illumination: 2  
periodsa |  optional |  1 |  数字 |  数字 的 periods 到 为 used 用于 periodic illumination  
periodsb |  optional |  1 |  数字 |  数字 的 periods 到 为 used 用于 periodic illumination  
index |  optional |  值 at 监视器 center |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
direction |  optional |  direction 的 max power flow |  数字 |  Direction: 此 可以 为 +1 或 -1.  
  
The following table summarizes 如何 到 interpret 该 ux, uy coordinate vectors 和 periods input 属性 用于 various 监视器 orientations.

**Monitor orientation** |  **Monitor surface normal** |  **'na', 'ux', 'periods 一个' correspond 到** |  **'nb', 'uy', 'periods b' correspond 到**  
---|---|---|---  
XY plane |  Z |  x axis |  y axis  
XZ plane |  Y |  x axis |  z axis  
YZ plane |  X |  y axis |  z axis  
  
**示例**

This example images 该 far field projection 的 一个 2D 监视器 called 监视器. In 此 example 该 second 频率 point 是 projected. If 该 监视器 only contains 数据 at one 频率, 该 second 参数 是 not required.
    
    
    E = farfield3d("监视器",2); 
    ux = farfieldux("监视器",2); 
    uy = farfielduy("监视器",2); 
    image(ux,uy,E,"","","title","polar"); 

The following example images 该 far field projection 的 一个 rectilinear dataset. Here, 该 dataset 是 从 一个 2D 监视器.
    
    
    dataset=getresult("监视器", "E");  
    dataset.addattribute("H",getattribute(getresult("监视器","H"),"H"));  
      
    E = farfield3d(dataset,2);   
    ux = farfieldux(dataset,2);   
    uy = farfielduy(dataset,2);   
    image(ux,uy,E,"","","title","polar"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldvector3d ](/hc/en-us/articles/360034410114-farfieldvector3d) , [ farfieldpolar3d ](/hc/en-us/articles/360034930713-farfieldpolar3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d) , [ farfieldfilter ](/hc/en-us/articles/360034930613-farfieldfilter) , [ farfield3dintegrate ](/hc/en-us/articles/360034410174-farfield3dintegrate)
