<!--
Translation from English documentation
Original command: gratingorders
Translation date: 2026-02-04 22:50:00
-->

# gratingorders

返回 一个 矩阵 数据 设置 使用 该 propagating grating orders, 一个 unit 向量 在 该 direction 的 该 wave 向量 (或 k-向量) 的 each order, 和 该 grating angles. The grating orders 是 该 same as 那些 used 通过 该  gratingprojection  命令 到 perform 一个 projection. 

**语法** |  **描述**  
---|---  
out = gratingorders(period, 源, 频率, index);  |  返回 一个 矩阵 数据 设置 使用 该 propagating grating orders (integers n 和 m), 一个 unit 向量 在 该 direction 的 该 k-向量 的 each order (call them **u** (n,m)) 和 their 对应的 angles (theta 和 phi). The 参数 的 该 数据 设置 是 n,m 和 频率. Indexes n 和 m correspond 到 该 first 和 second periodicity directions specified 通过 该 input periodicity vectors. The attributes 的 该 数据 设置 是 该 unit vectors **u** (n,m) 和 their 对应的 angles (theta 和 phi). The grating angles 是 defined 使用 respect 到 该 normal incidence direction 的 该 源 (call it 该 **n** -axis). The first angle (theta) 是 一个 elevation 从 该 **n** -axis 和 该 和 该 second angle (phi) 是 一个 rotation around 该 **n** -axis starting 从 该 first periodicity 向量. Angle phi 是 only returned 当 two periodicity vectors 是 specified.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
period  |  required  |  |  向量  |  [3x1] 或 [3x2] 矩阵 使用 该 periodicity vectors. These 是 typically retrieved 使用 该  getperiodicity  命令.   
源  |  required  |  |  向量  |  [3x1] 向量 使用 该 normalized 源 k-向量. This 是 typically retrieved 使用 该  getsourcedirection  命令.   
频率  |  required  |  |  向量  |  Vector 的 frequencies (在 Hz).   
index  |  optional  |  1.0  |  数字 或 向量  |  Refractive index 的 该 background medium (typically 该 substrate 或 superstrate). It 可以 为 一个 scalar 或 一个 向量 的 该 same size as 该 频率 向量.   
  
**示例**

This example shows 如何 到 find 该 propagating grating orders 从 一个 DGTD 仿真 使用 periodic boundary conditions. The 源 k-向量 和 频率 是 obtained 从 和 plane wave 源 对象 named "源" 和 一个 频率 domain 监视器 named "监视器", respectively. 
    
    
    # 频率 向量 的 该 near fields
    fields = getresult("DGTD::监视器","fields");
    频率 = fields.f; 
    # periodicity vectors
    period = getperiodicity("DGTD");
    # 源 k-向量
    source_k = getsourcedirection("DGTD::源");
    # propagating grating orders
    go = gratingorders(period,source_k,频率,1.0);
    visualize(go); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
