<!--
Translation from English documentation
Original command: grating
Translation date: 2026-02-04 22:50:00
-->

# grating

返回 该 fraction 的 transmitted power 到 each physical grating orders 用于 一个 given 仿真. Results 是 normalized such 该 该 sum 的 all 该 orders 是 equal 到 1. To 转换 这些 值 into fractions 的 该 源 power, multiply 通过 该 该 transmission 脚本 函数. 

3D simulations: Data 是 returned 在 一个 NxMxP 矩阵 其中 N,M 是 该 数字 的 grating orders, 和 P 是 该 数字 的 频率 points. 

2D simulations: Data 是 returned 在 一个 NxP 矩阵 其中 N 是 该 数字 的 grating orders, 和 P 是 该 数字 的 频率 points. 

**语法** |  **描述**  
---|---  
out = grating("monitorname",f, index, direction );  |  返回 该 strength 的 all physical grating orders 从 monitorname.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
monitorname  |  required  |  |  字符串  |  name 的 该 监视器 从 该 far field 是 calculated   
f  |  optional  |  1  |  向量  |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multithreaded projection 到 allow multiple 频率 points 到 为 calculated simultaneously was introduced 在 R2016b.   
index  |  optional  |  值 at 监视器 center  |  数字  |  The index 的 该 材料 到 use 用于 该 projection.   
direction  |  optional  |  direction 的 max power flow  |  数字  |  Direction: 此 可以 为 +1 或 -1.   
  
The following table summarizes 如何 到 interpret 该 coordinate 向量 属性 用于 various 监视器 orientations. 

**Monitor orientation** |  **Monitor surface normal** |  **'N', 'ux', 'gratingn', 'gratingperiod1', 'gratingu1', 'gratingbloch1', correspond 到** |  **'M', 'uy', 'gratingm', 'gratingperiod2', 'gratingu2', 'gratingbloch2' correspond 到**  
---|---|---|---  
XY plane  |  Z  |  x axis  |  y axis   
XZ plane  |  Y  |  x axis  |  z axis   
YZ plane  |  X  |  y axis  |  z axis   
  
**示例**

This 2D example plots 该 relative strength 的 该 grating orders. 
    
    
    mname="T";          # 监视器 name
    theta=gratingangle(mname);  # angle 的 each grating order
    G=grating(mname);      # power 到 each order (fraction 的 transmitted power)
    plot(theta,G,"theta (deg)","relative power","grating orders","plot points");

This 3D example 计算 various grating quantities. 
    
    
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

计算 该 zeroth grating order transmission 从 一个 监视器 该 recorded multiple 频率 points. The grating 函数 operates 在 one 频率 point at 一个 时间, so 一个 用于 loop 是 required. 
    
    
    mname="T";       # 监视器 name
    f=getdata(mname,"f");  # 获取 频率 向量
    T=transmission(mname); # 获取 total transmission
    G00 = 矩阵(长度(f)); # initialize 矩阵
    # 获取 0,0 grating order 用于 each 频率
    用于 (i=1:长度(T)) {
     N=gratingn(mname,i);  # grating order numbers
     M=gratingm(mname,i); 
     temp=grating("T2",i);
     G00(i) = temp(find(N,0),find(M,0)); # select 0,0 grating order
    }
    plot(c/f*1e6,T,G00*T,"波长 (um)","power");
    legend("total transmission","0,0 grating transmission"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingpolar ](/hc/en-us/articles/360034407034-gratingpolar) , [ gratingvector ](/hc/en-us/articles/360034407054-gratingvector)
