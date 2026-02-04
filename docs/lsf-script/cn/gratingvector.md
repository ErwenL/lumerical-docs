<!--
Translation from English documentation
Original command: gratingvector
Translation date: 2026-02-04 22:50:00
-->

# gratingvector

返回 该 relative strength 的 all physical grating orders 其中 向量 field information 是 returned 在 Cartesian coordinates. This 是 useful 当 studying 该 polarization effects. The 数据 是 normalized such 该 该 sum 的 |Ex|^2+|Ey|^2+ |Ez|^2 over all grating orders equals 1. See 该 [grating](/hc/en-us/articles/360034927213) 函数 documentation 用于 information 在 interpreting N, M, ux, uy 用于 various 监视器 orientations.

3D simulations: Data 是 returned 在 一个 NxMxPx3 矩阵 其中 N,M 是 该 数字 的 grating orders. P 是 该 数字 的 频率 points. The third 维度 是 Ex, Ey, Ez.

2D simulations: Data 是 returned 在 一个 NxPx3 矩阵 其中 N 是 该 数字 的 grating orders. P 是 该 数字 的 频率 points. The second 维度 是 Ex, Ey, Ez.

The results 是 returned 在 hemisphere 1m away. For more information 在 该 basis used please refer 到 [Understanding field polarization 在 far field projections](/hc/en-us/articles/360034914753)

**语法** |  **描述**  
---|---  
out = gratingvector( "mname", f, index, direction); |  返回 该 strength 的 all physical grating orders 从 monitorname. Output 是 在 Cartesian coordinates.  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  name 的 该 监视器 从 该 far field 是 calculated  
f |  optional |  1 |  向量 |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量.  
index |  optional |  值 at 监视器 center |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
direction |  optional |  direction 的 max power flow |  数字 |  Direction: 此 可以 为 +1 或 -1.  
  
**示例**

This 2D result shows 该 gratingvector gives 该 same result as 该 grating 函数 当 we 计算 |Ex|^2+|Ey|^2+ |Ez|^2.
    
    
    ?Gv=gratingvector("monitor1");
    result: 
    0.0476203+0.219991i 0.0509014+0.235148i 0+0i 
    0.0794422+0.373053i 0.0173684+0.0815601i 0+0i 
    0.638599+0.42186i -0.203101-0.134169i 0+0i 
    0.0335526+0.172349i -0.0480246-0.246687i 0+0i 
    ?sum(abs(Gv)^2,2);
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 
    ?G=grating("monitor1");
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingpolar ](/hc/en-us/articles/360034407034-gratingpolar) , [ Far field projections - Field polarization ](/hc/en-us/articles/360034914753-FFP-Field-polarization)
