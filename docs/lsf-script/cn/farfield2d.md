<!--
Translation from English documentation
Original command: farfield2d
Translation date: 2026-02-04 22:49:48
-->

# farfield2d

Projects 一个 given power 或 field profile 监视器 或 一个 rectilinear dataset 到 该 far field 到 一个 1 meter radius semi-circle. The electric field intensity |E|  2  是 returned. Farfield2d does not use 一个 设置 的 linearly spaced angles 用于 该 projection, use [farfieldangle - Script 命令](/hc/en-us/articles/360034930653) 到 获取 该 appropriate angle 向量. 

**语法** |  **描述**  
---|---  
out = farfield2d("mname", f, n, illumination, periods, index, direction); |  Projects 一个 given power 或 field profile 监视器 到 该 far field at 该 specified 频率 points. The result 是 一个 NxM 矩阵 其中 该 first 维度 是 该 resolution 的 该 far field projection, 和 该 second 维度 是 该 数字 的 频率 points projected.  
out = farfield2d(dataset, f, n, illumination, periods, index, direction); |  Projects 一个 given rectilinear dataset 到 该 far field at 该 specified 频率 points. The result 是 一个 NxM 矩阵 其中 该 first 维度 是 该 resolution 的 该 far field projection, 和 该 second 维度 是 该 数字 的 频率 points projected.  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  Name 的 该 监视器  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E 和 H  
f |  optional |  1 |  向量 |  Index 的 该 desired 频率 point. f 可以 为 一个 single 值, 或 一个 向量 的 频率 points. Multithreaded projection was introduced since R2016b.  
n |  optional |  2000 |  数字 |  The 数字 的 points 在 该 far field.  
illumination |  optional |  1 |  数字 |  For periodic structures Gaussian illumination: 1 Plane wave illumination: 2  
periods |  optional |  1 |  数字 |  数字 的 periods 到 为 used  
index |  optional |  值 at 监视器 center |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
direction |  optional |  direction 的 max power flow |  数字 |  Direction: 此 可以 为 +1 或 -1.  
  
**示例**

This example plots 该 far field projection 的 一个 1D 监视器 called 监视器. In 此 example 该 second 频率 point 是 projected. If 该 监视器 only contains 数据 at one 频率, 该 second 参数 是 not required.
    
    
    E2=farfield2d("监视器",2,501);
    theta=farfieldangle("监视器",2,501);
    plot(theta,E2,"angle (deg)","|E|^2 far field"); 

The following example plots 该 far field projection 的 一个 rectilinear dataset. Here, 该 dataset 是 从 一个 1D 监视器.
    
    
    dataset=getresult("监视器", "E");  
    dataset.addattribute("H",getattribute(getresult("监视器","H"),"H"));  
      
    E2=farfield2d(dataset,2,501);  
    theta=farfieldangle(dataset,2,501);  
    plot(theta,E2,"angle (deg)","|E|^2 far field"); 

For additional examples see [ Far field projection ](/hc/en-us/articles/360034914713) .

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldangle ](/hc/en-us/articles/360034930653-farfieldangle) , [ farfieldvector2d ](/hc/en-us/articles/360034930633-farfieldvector2d) , [ farfieldpolar2d ](/hc/en-us/articles/360034410094-farfieldpolar2d) , [ farfieldexact2d ](/hc/en-us/articles/360034410234-farfieldexact2d) , [ farfieldfilter ](/hc/en-us/articles/360034930613-farfieldfilter) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact) , [ farfield2dintegrate ](/hc/en-us/articles/360034930673-farfield2dintegrate)
