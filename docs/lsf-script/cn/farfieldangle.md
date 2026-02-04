<!--
Translation from English documentation
Original command: farfieldangle
Translation date: 2026-02-04 22:49:48
-->

# farfieldangle

返回 该 向量 的 angles, 在 degrees, 对应的 到 该 数据 从 farfield2d 用于 一个 2D 仿真. Used 用于 2D simulations. This 是 required because 该 farfield2d does not use 一个 设置 的 linearly spaced angles 用于 该 projection. It 是 often useful 到 re-interpolate 该 数据 onto 一个 设置 的 linearly spaced angles 使用 该 interp 或 spline functions.

**语法** |  **描述**  
---|---  
theta = farfieldangle( "mname", f, n, index); |  返回 该 矩阵 的 angles 对应的 到 该 数据 在 farfield2d  
theta = farfieldangle( dataset, f, n, index); | 返回 该 矩阵 的 angles 对应的 到 该 数据 在 farfield2d  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  Name 的 该 监视器 从 该 far field 是 calculated  
dataset | required |  | dataset |  Rectilinear dataset containing both E 和 H  
f |  optional |  1 |  向量 |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. If f 是 一个 向量, 该 second 维度 的 theta 将 match 该 长度 的 该 向量 的 频率 points. Multithreaded projection was introduced since R2016b.  
n |  optional |  2000 |  数字 |  The 数字 的 points 在 该 far field.  
index |  optional |  值 at 监视器 center |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
  
**示例**

This example plots 该 far field projection 的 一个 1D 监视器 called 监视器. In 此 example 该 second 频率 point 是 projected. If 该 监视器 only contains 数据 at one 频率, 该 second 参数 是 not required. For 该 example 的 far field projection 的 一个 rectilinear dataset see [farfield2d](/hc/en-us/articles/360034410074-farfield2d). 
    
    
    E2=farfield2d("监视器",2,501);
    theta=farfieldangle("监视器",2,501);
    plot(theta,E2,"angle (deg)","|E|^2 far field"); 

For additional examples see [ Far field projection ](/hc/en-us/articles/360034914713) .

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldvector2d ](/hc/en-us/articles/360034930633-farfieldvector2d) , [ farfieldpolar2d ](/hc/en-us/articles/360034410094-farfieldpolar2d) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ spline ](/hc/en-us/articles/360034405794-spline)
