<!--
Translation from English documentation
Original command: farfieldvector2d
Translation date: 2026-02-04 22:49:49
-->

# farfieldvector2d

Projects 一个 given power 或 field profile 监视器 或 一个 rectilinear dataset 到 该 far field 到 一个 1 meter radius semi-circle. This 是 similar 到 该 farfield2d 脚本 命令 except 该 complex electric fields 是 returned, rather than field intensity. The 数据 是 returned as 矩阵 的 NxP 如果 one 频率 point 是 projected, 或 NxPx3 当 multiple 频率 points 是 projected 其中 N 是 该 resolution 的 该 far field projection, P 是 该 数字 频率 points projected, 和 该 last index refers 到 Ex, Ey 和 Ez 该 是 该 complex components 的 该 electric field 向量 在 Cartesian coordinates.

**语法** |  **描述**  
---|---  
out = farfieldvector2d( "mname",...); |  返回 该 Cartesian complex electric fields. Same 参数 as farfield2d.  
out = farfieldvector2d( dataset,...); |  返回 该 Cartesian complex electric fields. Same 参数 as farfield2d.  
  
**示例**

This example plots 该 amplitude 的 该 Ex component 的 该 far field projection 的 一个 1D 监视器 called "监视器". In 此 example 该 second 频率 point 是 projected. If 该 监视器 only contains 数据 at one 频率, 该 second 参数 是 not required. For 该 example 的 far field projection 的 一个 rectilinear dataset see [farfield2d](/hc/en-us/articles/360034410074-farfield2d). 
    
    
    E=farfieldvector2d("监视器",2,501);
    Ex = abs(pinch(E,2,1)); # amplitude 的 Ex
    theta=farfieldangle("监视器",2,501);
    plot(theta,Ex,"angle (deg)","Ex far field"); 

For additional examples see [ Far field projection ](/hc/en-us/articles/360034914713) .

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldpolar2d ](/hc/en-us/articles/360034410094-farfieldpolar2d) , [ farfieldangle ](/hc/en-us/articles/360034930653-farfieldangle)
