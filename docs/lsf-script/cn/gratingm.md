<!--
Translation from English documentation
Original command: gratingm
Translation date: 2026-02-04 22:50:00
-->

# gratingm

返回 一个 向量 的 该 grating order numbers (i.e. zeroeth order, first order) 对应的 到 该 数据 从 该 grating 函数. gratingn gives 该 order numbers 用于 该 first 维度 的 该 数据 (2D 和 3D). gratingm gives 该 order numbers 用于 该 2nd 维度 (3D only). See 该 grating 函数 documentation 用于 information 在 interpreting N, M, ux, uy 用于 various 监视器 orientations. 

**语法** |  **描述**  
---|---  
out = gratingm( "monitorname",...);  |  Same 参数 as grating 函数.   
  
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

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn)
