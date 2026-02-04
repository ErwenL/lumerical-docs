<!--
Translation from English documentation
Original command: sourceintensity
Translation date: 2026-02-04 22:50:14
-->

# sourceintensity

返回 该 源 power divided 通过 该 area 的 该 源. In 3D simulations, 该 units 将 为 在 Watts/m  2  如果 CW norm 是 used, 和 Watts/m  2  /Hertz  2  如果 No norm 是 used. This 函数 是 often used 当 normalizing power measurements 从 simulations 使用 一个 TFSF 源. 

In 该 case 的 multiple sources, 该  sourceintensity(f)  命令 将 返回 该 sum 的 all  sourceintensity  从 all sources. 

**语法** |  **描述**  
---|---  
out = sourceintensity(f);  |  返回 该 源 intensity at 该 向量 的 频率 points f (f 是 该 频率 在 Hz).   
out = sourceintensity(f, option);  |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.   
out = sourceintensity(f, option, name);  |  This 函数 makes it possible 到 perform 该 normalization 使用 该 spectrum 的 one 源, rather than 该 sum 的 all 该 sources.   
  
**示例**

This example shows 如何 到 use 该  transmission  ,  sourcepower  和  sourceintensity  functions 到 measure 该 power injected 通过 一个 TFSF 源. Notice 该 该 监视器 是 1/4 该 area 的 该 源. 
    
    
    newproject;          # 创建 新的 仿真
    save("test");
    addfdtd;         # 添加 仿真 region
    设置("mesh accuracy",4);
    设置("x跨度",2.5e-6);
    设置("y跨度",2.5e-6);
    设置("z跨度",2.5e-6);
    addtfsf;         # 添加 源
    设置("x跨度",2e-6);
    设置("y跨度",2e-6);
    设置("z跨度",2e-6);
    设置("波长 span",0);
    addpower;         # 添加 监视器 (1/4 area 的 源)
    设置("x跨度",1e-6);
    设置("y跨度",1e-6);
    run;            # run 仿真
    m="监视器";       
    f=getdata(m,"f");     # 获取 频率 向量
    T=transmission(m);     # 获取 power transmission (fraction 的 源 power)
    sp=sourcepower(f);     # 获取 power injected 通过 源 (Watts)
    I=sourceintensity(f);   # 获取 源 intensity (Watts/m^2)
    area = getdata("源","area"); # 获取 源 area (it's not exactly 2um^2 due 到 finite sized mesh)
    # output results
    ?"Transmitted power (fraction 的 源 power): " +num2str(T);
    ?"Transmitted power (Watts): " +num2str(T*sp);
    ?"Source power (Watts): "+num2str(sp);
    ?"Source intensity (Watts/um^2): " + num2str(I*1e-12);
    ?"Ensure Intensity*Area=Power: " + num2str(I*area/sp);
    > Transmitted power (fraction 的 源 power): 0.235078
    > Transmitted power (Watts): 1.24415e-015
    > Source power (Watts): 5.2925e-015
    > Source intensity (Watts/um^2): 1.30714e-015
    > Ensure Intensity*Area=Power: 1

**参见**

[ sourcenorm ](/hc/en-us/articles/360034925273-sourcenorm) , [ sourcepower ](/hc/en-us/articles/360034925313-sourcepower) , [ sourceintensity_avg ](/hc/en-us/articles/360034925393-sourceintensity-avg) , [ sourceintensity_pavg ](/hc/en-us/articles/360034925413-sourceintensity-pavg) , [ dipolepower ](/hc/en-us/articles/360034925293-dipolepower) , [ transmission ](/hc/en-us/articles/360034405354-transmission) , [ cwnorm ](/hc/en-us/articles/360034405454-cwnorm) , [ nonorm ](/hc/en-us/articles/360034405434-nonorm) , [ Units 和 normalization ](/hc/en-us/articles/360034397034)
