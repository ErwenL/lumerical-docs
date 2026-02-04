<!--
Translation from English documentation
Original command: sourcepower
Translation date: 2026-02-04 22:50:14
-->

# sourcepower

返回 该 power injected into 该 仿真 通过 该 源.

**Dipole sources**

The  sourcepower  脚本 函数 返回 该 power 该 dipole 源 would radiate 在 一个 homogeneous medium. This quantity 可以 为 calculated analytically (see [ Dipole 源](/hc/en-us/articles/360034382794-Sources-Dipoles)). The actual radiated power 是 not given 通过 该  sourcepower  函数. The actual radiated power 是 highly dependant 在 该 surrounding materials since 该 reflections 从 该 structures 将 interfere 使用 该 fields 从 该 dipole, changing 该 actual radiated power. To 获取 该 actual radiated power, see 该 [ dipolepower ](/hc/en-us/articles/360034925293-dipolepower) 脚本 函数.

**Other sources (Gaussian, plane wave, mode, etc)**

The  sourcepower  是 determined 从 该 equation below. 注意 该 \\(P(f)^{\text{Source}}\\) 是 该 Poynting 向量 determined 从 该 E, H fields injected 通过 该 源. The integral 是 evaluated over 该 injection plane 的 该 源.

$$ \text {源 power}_{\text {no_norm}}(f)=\frac{1}{2} \int \text{Re}\left(P(f)^{\text {Source}}\right) \cdot d S $$

$$ \text {源 power}_{\text {cw_norm}}(f)=\frac{\frac{1}{2} \int \text{Re}\left(P(f)^{\text {Source}}\right) \cdot d S}{ | \text {sourcenorm}\left.\right |^{ 2 }} $$

As stated above,  sourcepower  gives 该 amount 的 power injected into 该 仿真. The only exception 是 如果 该 仿真 是 设置 up such 该 there 是 radiation 该 travels through 该 injection plane 的 该 源 在 该 源 injection direction (pink arrow). In such cases, 该 actual amount 的 power injected 通过 该 源 将 not 为 given 通过  sourcepower  . In 此 situation, 该 incident radiation interferes 使用 该 源, changing 该 amount 的 injected power (similar 到 什么 happens 用于 该 dipole 源). In most cases, 此 means your 仿真 是 not 设置 up properly.

[[注意:]] Multiple sources 和 CW normalization In 该 case 的 multiple sources, 该 sourcepower(f) 命令 将 返回 该 sum 的 all sourcepowers 从 all sources. Since 该 值 的 该 sourcenorm depend 在 该 choice 的 cwnorm option, 该 calculated sourcepower 将 also 为 affected 通过 it.  
---  
**语法** |  **描述**  
---|---  
out = sourcepower(f); |  返回 该 源 power used 到 normalize transmission calculations at 该 向量 的 频率 points f (频率 在 Hz). The unit 的 该 源 power 是 Watts 如果 CW norm 是 used, 和 Watts/Hertz  2  如果 no norm 是 used.  
out = sourcepower(f, option); |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersects such 一个 boundary at x最小值, y最小值, 或 z最小值. The default 值 的 该 option 是 2.  
out = sourcepower(f, option, name); |  This option allows you 到 obtain 该 spectrum 的 one 源, rather than 该 sum 的 all sources. This option 是 only needed 用于 simulations 使用 multiple sources.  
  
**示例**

This example shows 如何 到 计算 该 power injected 通过 一个 源 as 一个 函数 的 频率.
    
    
    f=linspace(200e12,300e12,100);
    sp=sourcepower(f); # power 在 Watts, assuming CW norm 是 在.

This example shows 如何 到 use 该  transmission  和  sourcepower  functions 到 计算 该 power injected 通过 一个 plane wave 源.
    
    
    newproject;
    save("test");
     
    # 仿真 region
    addfdtd;
    设置("x跨度",1e-6); 设置("y跨度",1e-6); 设置("z跨度",1e-6);
    设置("x最小值 bc","periodic"); 设置("y最小值 bc","periodic");
     
    # plane wave 源
    addplane;
    设置("z",-0.3e-6);
    设置("x跨度",2e-6); 设置("y跨度",2e-6);
    设置("center 波长",500e-9);
    设置("波长 span",0);
     
    # power 监视器
    addpower; 
    设置("z",0.3e-6);        
    设置("x跨度",2e-6); 设置("y跨度",2e-6);
    # run 仿真 
    run;            
    # 获取 results 
    m="监视器";      
    f=getdata(m,"f");     # 获取 频率 向量
    T=transmission(m);     # 获取 power transmission (fraction 的 源 power)
    sp=sourcepower(f);     # 获取 power injected 通过 源 (Watts)
     
    # output results
    ?"Transmitted power (fraction 的 源 power): " +num2str(T);
    ?"Transmitted power (Watts): " +num2str(T*sp);
    ?"Source power (Watts): "+num2str(sp);
    > Transmitted power (fraction 的 源 power): 0.999986
    > Transmitted power (Watts): 1.26203e-015
    > Source power (Watts): 1.26204e-015

**参见**

[ sourcenorm ](/hc/en-us/articles/360034925273-sourcenorm) , [ sourcepower_avg ](/hc/en-us/articles/360034925333-sourcepower-avg) , [ sourcepower_pavg ](/hc/en-us/articles/360034925353-sourcepower-pavg) , [ dipolepower ](/hc/en-us/articles/360034925293-dipolepower) , [ transmission ](/hc/en-us/articles/360034405354-transmission) , [ sourceintensity ](/hc/en-us/articles/360034925373-sourceintensity) , [ cwnorm ](/hc/en-us/articles/360034405454-cwnorm) , [ nonorm ](/hc/en-us/articles/360034405434-nonorm)
