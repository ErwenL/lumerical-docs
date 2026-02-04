<!--
Translation from English documentation
Original command: getnumericalpermittivity
Translation date: 2026-02-04 22:50:00
-->

# getnumericalpermittivity

This advanced 函数 返回 该 permittivity 的 一个 材料 在 该 database as it 将 为 used 在 一个 actual FDTD 仿真, including 该 effects 的 一个 finite 时间 step, dt. In FDTD, 该 relationship between 该 displacement field, D, 和 该 electric field, E, 是 given 通过 

$$ \vec{D}(\omega)=\varepsilon_{0} \varepsilon_{\gamma}(\omega, d t) \vec{E}(\omega) $$ 

In 该 limit 其中 dt tends 到 zero, we have 

$$ \lim _{d t \rightarrow 0} \varepsilon_{r}(\omega, d t)=n^{2}(\omega) $$ 

其中 n(  ω  ) 是 该 refractive index returned 通过 该 脚本 函数 getfdtdindex, 或 shown 在 该 Materials Explorer. If you 设置 dt 到 zero 当 calling 此 函数, it 将 返回 exactly 该 same result as 该 square 的 getfdtdindex. 

The name 的 该 函数 是 一个 reminder 该 it 返回 该 numerical permittivity, i.e., 该 ratio 的 D 和 E, 该 是 different 从 该 refractive index, i.e. 该 ratio 的 该 speed 的 light 在 一个 vacuum 到 该 phase velocity 的 light 在 该 medium. To understand 该 relationship between them, we 必须 consider 该 full, numerical dispersion relation between  ω  和 k, 该 是 given 通过 

$$ \varepsilon_{r}(\omega, d t)\left[\frac{1}{c d t} \sin \left(\frac{\omega d t}{2}\right)\right]^{2}=\left[\frac{1}{d x} \sin \left(\frac{k_{x} d x}{2}\right)\right]^{2}+\left[\frac{1}{d y} \sin \left(\frac{k_{y} d y}{2}\right)\right]^{2}+\left[\frac{1}{d z} \sin \left(\frac{k_{z} d z}{2}\right)\right]^{2} $$ 

In 该 limit 其中 dt, dx, dy 和 dz tend 到 zero, it 是 easy 到 show 该 we have 该 expected result 

$$ \omega=\frac{c k}{\sqrt{\varepsilon_{r}(\omega, d t=0)}}=\frac{c k}{n(\omega)} $$ 

The spatial FDTD mesh 和 时间 step 是 generally chosen 到 obtain 一个 desired level 的 仿真 accuracy, essentially 通过 ensuring 该 该 参数 的 该 sine functions 是 sufficiently small 该 sin(x)~x 和 该 该 仿真 是 stable. For some materials, it 可能 为 desired 到 further reduce 该 值 的 该 时间 step, dt, without modifying 该 spatial FDTD mesh, 在 order 到 obtain 一个 higher level 的 accuracy 用于  ε  r  (  ω  ,dt). This 脚本 函数 makes it possible 到 计算, 在 advance, 该 值 的 dt required 到 obtain 该 desired accuracy 用于 该 permittivity. 

The results 从 getnumericalpermittivity 将 为 different 如果 该 Broadband Fixed Angle Source Technique (BFAST) 是 used. Since 该 脚本 函数 does not require 一个 calculation being performed beforehand, 该 用户 needs 到 specify 如果 该 computation uses BFAST 或 not. See 该 [ BFAST page ](/hc/en-us/articles/360034902273-Source-BFAST) 用于 more details about 此 technique. 

**语法** |  **描述**  
---|---  
out = getnumericalpermittivity ( "materialname", f, fmin, fmax, dt);  |  返回 该 complex permittivity 的 该 材料 使用 该 given name. The permittivity 是 returned 用于 该 specified 频率 f. This 是 similar 到 getfdtdindex except 用于 该 additional 参数 dt. All 频率 units 是 在 Hz.   
getnumericalpermittivity("materialname", f,fmin, fmax, dt, component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
getnumericalpermittivity("materialname", f,fmin, fmax, dt, component, use_bfast);  |  Optional 参数 use_bfast 可以 为 0 或 1. It indicates whether 该 仿真 是 performed 使用 该 Broadband Fixed Angle Source Technique (BFAST) 或 not. The default 是 0.   
  
**示例**

This example shows 如何 到 获取 该 材料 permittivity 使用 该 getindex, getfdtdindex 和 getnumerical permittivity functions. In 此 case, we compare 该 experimental permittivity 数据 到 该 theoretical FDTD fit 的 该 该 数据 as well as 到 该 numerical permittivity 该 将 result 使用 一个 finite 值 的 dt. 
    
    
    材料="Si (Silicon) - Palik";   # 材料 
    source_min_f=c/800e-9;      # 源 min 频率
    source_max_f=c/200e-9;      # 源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    component = 1; # desired permittivity component x (1), y (2) 或 z (3). Relevant 用于 anisotropic materials, default 1
    use_bfast = 0; # Change 到 1 如果 使用 BFAST, default 0 
    # 获取 experimental 数据
    eps_exp=(getindex(材料,f_vector))^2;
    # 获取 FDTD fit 的 experimental 数据
    eps_fit=(getfdtdindex(材料,f_vector,source_min_f,source_max_f))^2;
    # 获取 该 numerical FDTD result 用于 3 different 值 的 dt
    Tmin = 1/max(f_vector);
    dt = Tmin * [ 0.1; 0.05; 0.01 ];
    # alternate way 到 获取 dt 值: 100%, 10%, 1% 的 current dt 值
    # dt = getnamed("FDTD","dt");
    # dt = [dt; dt*0.1; dt*0.01];
     
    eps_numerical1=getnumericalpermittivity(材料,f_vector,source_min_f,source_max_f,dt(1),component,use_bfast);
    eps_numerical2=getnumericalpermittivity(材料,f_vector,source_min_f,source_max_f,dt(2),component,use_bfast);
    eps_numerical3=getnumericalpermittivity(材料,f_vector,source_min_f,source_max_f,dt(3),component,use_bfast);
    # plot results
    如果 (use_bfast==1){fdtd_method = "FDTD - BFAST";}
    否则{fdtd_method = "FDTD";}
    plot(c/f_vector*1e9,real(eps_exp),real(eps_fit),
              real(eps_numerical1),
              real(eps_numerical2),
              real(eps_numerical3),
              "wavelenth (nm)","Re(eps)",材料);
    legend("experimental 数据","FDTD fit",
        fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");
    plot(c/f_vector*1e9,imag(eps_exp),imag(eps_fit),
              imag(eps_numerical1),
              imag(eps_numerical2),
              imag(eps_numerical3),"wavelenth (nm)","Im(eps)",材料);
    legend("experimental 数据","FDTD fit",
        fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex)
