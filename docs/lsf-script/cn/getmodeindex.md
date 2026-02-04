<!--
Translation from English documentation
Original command: getmodeindex
Translation date: 2026-02-04 22:50:00
-->

# getmodeindex

This 函数 返回 该 材料 index 的 一个 材料 在 该 database as it 将 为 used 在 一个 actual MODE 仿真. 

Many materials (such as Sampled Materials) have 属性 该 depend 在 频率. Using getmodeindex, you 可以 obtain 该 refractive index as 一个 函数 的 该 specified 频率, f, as it 将 为 used 在 MODE calculations. 

注意 该 该 fit result depends 在 该 fit 参数, Max coefficients 和 Tolerance 设置 用于 该 材料, thus getfdtdindex result depends 在 那些 参数 as well. Tips 用于 setting 这些 参数 可以 为 found at [ Modifying 该 材料 fits ](/hc/en-us/articles/360034915053-Modifying-该-Material-Fits) . 

**语法** |  **描述**  
---|---  
out = getmodeindex( "materialname", f);  |  返回 该 complex index 的 该 材料 使用 该 given name. The index 是 returned 用于 该 specified 频率 f. This result 是 identical 到 getindex unless 该 optional 参数 fitsampled 和 fitanalytic 是 used. All 频率 units 是 在 Hz.   
getmodeindex("materialname", f,component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
getmodeindex("materialname", f,component, fitsampled, fitanalytic, fmin, fmax);  |  Optional 参数 到 specify 如果 Sampled Materials 或 Analytic Materials 应该 为 fitted 使用 Lumerical's multi-coefficient model (MCM), 该 是 commonly used 在 FDTD simulations. If either 的 这些 options 是 设置 到 1 (true) 那么 you 必须 supply 一个 minimum 和 maximum 频率 用于 fitting. The MCM 是 typically used 在 MODE 用于 

  * Sampled Materials 当 calculating waveguide dispersion, 和 用于 
  * Analytic Materials only 用于 该 purpose 的 使用 precisely 该 same materials 在 both FDTD 和 MODE simulations. 

The default 值 是 0 (false) 用于 fitsampled 和 fitanalytic.   
  
**示例**

This example shows 如何 到 获取 材料 (n,k) 数据 使用 该 getindex 和 getmodeindex functions. In 此 case, we compare 该 experimental 数据 到 该 MODE multi-coefficient fit 的 该 该 数据 该 would 为 used 在 该 仿真. 
    
    
    材料="Si (Silicon) - Palik";   # 材料 
    source_min_f=c/700e-9;      # 源 min 频率
    source_max_f=c/400e-9;      # 源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    # 获取 experimental 数据
    n_exp=getindex(材料,f_vector);
    # 获取 MODE multi-coefficient fit 的 experimental 数据
    n_mode=getmodeindex(材料,f_vector,1,1,0,source_min_f,source_max_f);
    # plot results
    plot(c/f_vector*1e9,real(n_exp),real(n_mode),"wavelenth (nm)","n",材料);
    legend("experimental 数据","MODE fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_mode),"wavelenth (nm)","k",材料);
    legend("experimental 数据","MODE fit");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial)
