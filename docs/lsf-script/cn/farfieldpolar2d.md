<!--
Translation from English documentation
Original command: farfieldpolar2d
Translation date: 2026-02-04 22:49:48
-->

# farfieldpolar2d

Projects 一个 given power 或 field profile 监视器 或 一个 rectilinear dataset 到 该 far field 到 一个 1 meter radius semi-circle. This 是 similar 到 该 farfield2d 脚本 命令 except 该 complex electric fields 是 returned, rather than field intensity. The 数据 是 returned as 矩阵 的 NxP 如果 one 频率 point 是 projected, 或 NxPx3 当 multiple 频率 points 是 projected 其中 N 是 该 resolution 的 该 far field projection, P 是 该 数字 频率 points projected, 和 该 last index refers 到 E  r  , E  θ  和 E  z  , 在 cylindrical coordinates. For TM simulations, 此 函数 gives precisely 该 result 的 farfieldvector2d because 该 only non-zero field component 是 Ez.

**语法** |  **描述**  
---|---  
out = farfieldpolar2d( "mname",...); |  返回 该 polar complex electric fields. Same 参数 as farfield2d.  
out = farfieldpolar2d( dataset,...); |  返回 该 polar complex electric fields. Same 参数 as farfield2d.  
  
**示例**

This example plots 该 amplitude 的 该 Er component 的 该 far field projection 的 一个 1D 监视器 called "监视器". In 此 example 该 second 频率 point 是 projected. If 该 监视器 only contains 数据 at one 频率, 该 second 参数 是 not required. For 该 example 的 far field projection 的 一个 rectilinear dataset see [farfield2d](/hc/en-us/articles/360034410074-farfield2d). 
    
    
    E=farfieldpolar2d("监视器",2,501);
    Er = abs(pinch(E,2,1)); # amplitude 的 Er
    theta=farfieldangle("监视器",2,501);
    plot(theta,Er,"angle (deg)","Er far field"); 

For additional examples see [ Far field projection](/hc/en-us/articles/360034914713).

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldvector2d ](/hc/en-us/articles/360034930633-farfieldvector2d) , [ farfieldangle ](/hc/en-us/articles/360034930653-farfieldangle)
