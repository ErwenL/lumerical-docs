<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getdata -->

# getdata

    x=getdata("监视器","x");
    y=getdata("监视器","y");
    z=getdata("监视器","z");
    f=getdata("监视器","f");
    Ex=getdata("监视器","Ex");
    ?大小(Ex);
    Ex = 压缩(Ex,4,1); 
    image(x*1e6,y*1e6,Ex,"x (um)","y (um)","Ex");
    E=getresult("监视器","E");
    ?大小(E.Ex);
    Ex = 压缩(E.Ex,4,1); # select first 频率 point to plot
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex"); 
Get a list of data in the 'Device 区域' object, then get the 'n' carrier concentration data.
    ?getdata("Device 区域");
    ?getdata("Device 区域","active");
    n=getdata("Device 区域","active","n");
    ?大小(n);
    > active drain 光源
    > n p Ei Ec Ev Efn Efp log10(N) mun mup 
    > result: 
    >  2826 1 9 1 

**语法** | **描述**
---|---
?getdata; | 返回 names of all objects with data.
?getdata("monitor") | 返回 list of of data within the 仿真 object.
out = getdata( "monitor", "dataname"); | Gets data from a 监视器. For 示例, you can use
out = getdata( "monitor", "dataname", option); | The optional 参数, option, can have a 值 of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a 监视器 that intersect such a 边界 at x min, y min or z min. The default 值 of option is 2. For Propagator simulations in 模式, this options also allow users to choose whether to expand the data to the correct 大小 for 维度 where the 场 component is 零. Option 1 will 返回 a singleton 值 of 0 for the 场 component in that 维度, and option 2 will 返回 a 矩阵 (composed of 零矩阵) that matches the 大小 of the other 场 components.
?getdata; | 返回 names of all objects with data.
?getdata("monitor") | 返回 list of of results within the 仿真 object.
?getdata( "monitor", "result"); | 返回 list of of data within the 仿真 object result.
out = getdata( "monitor", "result", "dataname"); | Gets the 仿真 data.

**示例**

This 示例 shows how to use getdata to check which data is available.
    ?getdata;
    ?getdata("监视器");
    > 监视器
    > 光源
    > 
    > x y z surface_normal 维度 f Ex Ey Ez
    > Hx Hy Hz 功率 
Next, we use getdata to create a image plot of Ex(x,y). We also show how getresult can be used to create the same figure.

This 示例 shows how to use getdata to check which data is available.
    ?getdata;
    ?getdata("监视器");
    > 监视器
    > 光源
    > 
    > x y z surface_normal 维度 f Ex Ey Ez
    > Hx Hy Hz 功率 
Next, we use getdata to create a image plot of Ex(x,y). We also show how getresult can be used to create the same figure.

**另请参阅**

[getresult](/hc/en-us/articles/360034409854-getresult), [havedata](/hc/en-us/articles/360034930213-havedata), [getelectric](/hc/en-us/articles/360034409974-getelectric), [getmagnetic](/hc/en-us/articles/360034930293-getmagnetic), [nonorm](/hc/en-us/articles/360034405434-nonorm), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [getsweepdata](/hc/en-us/articles/360034409794-getsweepdata), [getsweepresult](/hc/en-us/articles/360034409814-getsweepresult)
