<!--
Translation from English documentation
Original command: gratingangle
Translation date: 2026-02-04 22:50:00
-->

# gratingangle

返回 该 angle 向量 对应的 到 该 值 returned 通过 grating, 在 degrees, 用于 2D simulations. For 3D simulations, use gratingu1 和 gratingu2.

If Bloch boundary conditions 是 used, 该 Bloch 向量 必须 为 properly 设置 用于 此 命令 到 返回 该 correct results. To make sure 该 Bloch 向量 是 properly 设置, turn 在 该 "设置 based 在 源 angle" option 在 该 "Boundary conditions" tab 的 该 FDTD 求解器 settings.

**语法** |  **描述**  
---|---  
out = gratingangle( "monitorname", ...); |  Same 参数 as grating 函数.  
  
**示例**

This example plots 该 relative strength 的 该 grating orders.
    
    
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # angle 的 each grating order
    G=grating(mname);      # power 到 each order (fraction 的 transmitted power)
    plot(theta,G,"theta (deg)","relative power","grating orders","plot points");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingu2 ](/hc/en-us/articles/360034407114-gratingu2)
