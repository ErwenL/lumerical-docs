<!--
Translation from English documentation
Original command: gratingprojection
Translation date: 2026-02-04 22:50:00
-->

# gratingprojection

Takes 该 near fields 从 一个 频率 domain 监视器 together 使用 该 periodicity vectors 的 该 system, 该 源 wave 向量 和 该 background refractive index 和 performs 一个 far field projection 到 determine 该 relative power 在 each propagating grating order. 

**语法** |  **描述**  
---|---  
out = gratingprojection(nearfield, period, 源, index);  |  返回 一个 矩阵 数据 设置 使用 all 该 projection results. The 参数 的 该 数据 设置 是 该 grating orders (integers n 和 m) 和 频率. Indexes n 和 m correspond 到 该 first 和 second periodicity directions specified 通过 该 input periodicity vectors. The attributes 的 该 数据 设置 是 该 same as 那些 returned 通过 该  gratingorders  命令 使用 该 addition 的 该 relative power into each propagating grating order (called projection). The projection result 是 normalized so 该 its sum over all grating orders 是 always equal 到 one. The 频率 参数 是 该 same as 该 的 该 input field 数据.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
nearfield  |  required  |  |  unstructured 数据 设置  |  Field 数据 从 一个 频率 domain 监视器.   
period  |  required  |  |  向量  |  Periodicity 向量(s) as returned 通过 该  getperiodicity  命令.   
源  |  required  |  |  向量  |  Source unit wave 向量 as returned 通过 该  getsourcedirection  命令.   
index  |  optional  |  1.0  |  数字 或 向量  |  Refractive index 的 该 background medium (typically 该 substrate 或 superstrate). It 可以 为 一个 scalar 或 一个 向量 的 该 same size as 该 频率 向量.   
  
**示例**

This example demonstrates 如何 到 计算 该 relative power into each propagating grating order 用于 一个 DGTD 仿真 使用 periodic boundary conditions. The near fields 是 collected 从 一个 频率 domain 监视器 named "监视器". The 源 wave 向量 是 collected 从 一个 plane wave 源 named "源". The periodicity vectors 是 collected 从 该 DGTD 仿真 对象. 
    
    
    # unstructured 数据 设置 使用 该 near field
    fields = getresult("DGTD::监视器","fields");
    # periodicity 向量
    period = getperiodicity("DGTD");
    # normalized 源 k-向量
    source_k = getsourcedirection("DGTD::源");
    # grating projection
    gp = gratingprojection(fields,period,source_k);
    visualize(gp); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders)
