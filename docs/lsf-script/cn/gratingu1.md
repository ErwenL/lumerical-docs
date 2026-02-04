<!--
Translation from English documentation
Original command: gratingu1
Translation date: 2026-02-04 22:50:00
-->

# gratingu1

返回 该 grating order direction unit vectors (u  1  和 u  2  ) 对应的 到 该 数据 从 该 grating 函数 从 3D 仿真. For 2D simulations, use 该 gratingangle 函数. See 该 grating 函数 documentation 用于 information 在 interpreting N, M, ux, uy 用于 various 监视器 orientations. 

**语法** |  **描述**  
---|---  
out = gratingu1( "monitorname", ...);  |  Same 参数 as grating 函数.   
  
**示例**

This example 计算 various grating quantities. 
    
    
    mname="T";       # 监视器 name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (可以 为 converted 到 theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # power 到 each order (fraction 的 transmitted power)
    T=transmission(mname); # total power transmitted through 监视器 (fraction 的 源 power)
    # Print all grating orders 到 prompt. Results 将 sum 到 1.
    # Then normalize grating results 到 该 injected 源 power.
    ?G;  # grating results
    ?G*T; # normalized 到 源 power
    # find strength 和 direction 的 0,0 grating order
    nx=find(N,0); # find 0th grating order
    ny=find(M,0); # find 0th grating order
    ?"Grating order 0,0 strength: " + num2str( G(nx,ny) );
    ?"Grating order 0,0 direction: Ux=" +num2str(u1(nx)) + " Uy=" +num2str(u2(ny));
    # image all grating orders, 使用 log scale
    image(u1,u2,G,"ux","uy","Grating order strength","logplot");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingu2 ](/hc/en-us/articles/360034407114-gratingu2) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ Direction unit 向量 coordinates ](/hc/en-us/articles/360034394294-FFP-Direction-unit-向量-coordinates)
