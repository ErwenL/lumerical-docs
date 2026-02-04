<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getmodeindex -->

# getmodeindex

    n_exp=getindex(material,f_vector);
    n_mode=getmodeindex(material,f_vector,1,1,0,source_min_f,source_max_f);
    plot(c/f_vector*1e9,实部(n_exp),实部(n_mode),"wavelenth (nm)","n",material);
    legend("experimental data","模式 fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_mode),"wavelenth (nm)","k",material);
    legend("experimental data","模式 fit");

**语法** | **描述**
---|---
out = getmodeindex( "materialname", f); | 返回 the 复数 index of the material with the given name. The index is returned for the specified 频率 f. This result is identical to getindex unless the optional arguments fitsampled and fitanalytic are used. All 频率 units are in Hz.
getmodeindex("materialname", f,component); | Optional 参数 component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.
getmodeindex("materialname", f,component, fitsampled, fitanalytic, fmin, fmax); | Optional arguments to specify if Sampled Materials or Analytic Materials should be fitted using Lumerical's multi-coefficient model (MCM), which is commonly used in FDTD simulations. If either of these options are set to 1 (真) then you must supply a 最小值 and 最大值 频率 for fitting. The MCM is typically used in 模式 for

**示例**

This 示例 shows how to get material (n,k) data with the getindex and getmodeindex functions. In this case, we compare the experimental data to the 模式 multi-coefficient fit of the that data that would be used in the 仿真. 
    material="Si (Silicon) - Palik";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

This 示例 shows how to get material (n,k) data with the getindex and getmodeindex functions. In this case, we compare the experimental data to the 模式 multi-coefficient fit of the that data that would be used in the 仿真. 
    material="Si (Silicon) - Palik";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial)
