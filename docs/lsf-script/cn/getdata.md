<!--
Translation from English documentation
Original command: getdata
Translation date: 2026-02-04 22:49:59
-->

# getdata

获取 raw 数据 从 一个 仿真 对象. In most cases, it 是 more convenient 到 获取 一个 complete dataset 使用 [ getresult](/hc/en-us/articles/360034409854-getresult), rather than getting individual 数据 elements 使用 getdata.

Remember 到 run 该 仿真 before 使用 getdata.

For FDTD 和 MODE:

**语法** |  **描述**  
---|---  
?getdata; |  返回 names 的 all 对象 使用 数据.  
?getdata("监视器") |  返回 list 的 的 数据 within 该 仿真 对象.  
out = getdata( "监视器", "dataname"); |  获取 数据 从 一个 监视器. For example, you 可以 use

  * Ex = getdata("monitor1","Ex");

到 获取 该 Ex field 数据 从 monitor1.  
out = getdata( "监视器", "dataname", option); |  The optional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2. For Propagator simulations 在 MODE, 此 options also allow users 到 choose whether 到 expand 该 数据 到 该 correct size 用于 dimensions 其中 该 field component 是 zero. Option 1 将 返回 一个 singleton 值 的 0 用于 该 field component 在 该 维度, 和 option 2 将 返回 一个 矩阵 (composed 的 zeros) 该 matches 该 size 的 该 other field components.  
  
For CHARGE, HEAT, DGTD, FEEM:

**语法** |  **描述**  
---|---  
?getdata; |  返回 names 的 all 对象 使用 数据.  
?getdata("监视器") |  返回 list 的 的 results within 该 仿真 对象.  
?getdata( "监视器", "result"); |  返回 list 的 的 数据 within 该 仿真 对象 result.  
out = getdata( "监视器", "result", "dataname"); |  获取 该 仿真 数据.  
  
For INTERCONNECT: The getdata 命令 是 available 在 INTERCONNECT 用于 compatibility 使用 other Lumerical products, but it's best 到 use 该 getresult 脚本 函数 到 access INTERCONNECT 仿真 数据.

**示例**

This example shows 如何 到 use getdata 到 check 该 数据 是 available.
    
    
    ?getdata;
    ?getdata("监视器");
    > 监视器
    > 源
    > 
    > x y z surface_normal 维度 f Ex Ey Ez
    > Hx Hy Hz power 

Next, we use getdata 到 创建 一个 image plot 的 Ex(x,y). We also show 如何 getresult 可以 为 used 到 创建 该 same figure.
    
    
    # 获取 raw 数据 使用 getdata
    x=getdata("监视器","x");
    y=getdata("监视器","y");
    z=getdata("监视器","z");
    f=getdata("监视器","f");
    Ex=getdata("监视器","Ex");
    # select first 频率 point 的 Ex 数据, 那么 创建 plot
    ?size(Ex);
    Ex = pinch(Ex,4,1); 
    image(x*1e6,y*1e6,Ex,"x (um)","y (um)","Ex");
    # use getresult 到 获取 all 的 该 E field 数据 在 一个 single 命令
    E=getresult("监视器","E");
    # select first 频率 point 的 Ex 数据, 那么 创建 plot
    ?size(E.Ex);
    Ex = pinch(E.Ex,4,1); # select first 频率 point 到 plot
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex"); 

获取 一个 list 的 数据 在 该 'Device region' 对象, 那么 获取 该 'n' carrier concentration 数据.
    
    
    ?getdata("Device region");
    ?getdata("Device region","active");
    n=getdata("Device region","active","n");
    ?size(n);
    > active drain 源
    > n p Ei Ec Ev Efn Efp log10(N) mun mup 
    > result: 
    >  2826 1 9 1 
    

**参见**

[getresult](/hc/en-us/articles/360034409854-getresult), [havedata](/hc/en-us/articles/360034930213-havedata), [getelectric](/hc/en-us/articles/360034409974-getelectric), [getmagnetic](/hc/en-us/articles/360034930293-getmagnetic), [nonorm](/hc/en-us/articles/360034405434-nonorm), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [getsweepdata](/hc/en-us/articles/360034409794-getsweepdata), [getsweepresult](/hc/en-us/articles/360034409814-getsweepresult)
