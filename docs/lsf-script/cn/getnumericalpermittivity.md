<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getnumericalpermittivity -->

# getnumericalpermittivity

    eps_exp=(getindex(material,f_vector))^2;
    eps_fit=(getfdtdindex(material,f_vector,source_min_f,source_max_f))^2;
    Tmin = 1/max(f_vector);
    dt = Tmin * [ 0.1; 0.05; 0.01 ];
    eps_numerical1=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(1),component,使用_bfast);
    eps_numerical2=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(2),component,使用_bfast);
    eps_numerical3=getnumericalpermittivity(material,f_vector,source_min_f,source_max_f,dt(3),component,使用_bfast);
    if (使用_bfast==1){fdtd_method = "FDTD - BFAST";}
    else{fdtd_method = "FDTD";}
    plot(c/f_vector*1e9,实部(eps_exp),实部(eps_fit),
              实部(eps_numerical1),
              实部(eps_numerical2),
              实部(eps_numerical3),
              "wavelenth (nm)","Re(eps)",material);
    legend("experimental data","FDTD fit",
        fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");
    plot(c/f_vector*1e9,imag(eps_exp),imag(eps_fit),
              imag(eps_numerical1),
              imag(eps_numerical2),
              imag(eps_numerical3),"wavelenth (nm)","Im(eps)",material);
    legend("experimental data","FDTD fit",
        fdtd_method+", dt="+num2str(dt(1)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(2)*1e15)+"fs",
        fdtd_method+", dt="+num2str(dt(3)*1e15)+"fs");

**语法** | **描述**
---|---
out = getnumericalpermittivity ( "materialname", f, fmin, fmax, dt); | 返回 the 复数 介电常数 of the material with the given name. The 介电常数 is returned for the specified 频率 f. This is similar to getfdtdindex except for the additional 参数 dt. All 频率 units are in Hz.
getnumericalpermittivity("materialname", f,fmin, fmax, dt, component); | Optional 参数 component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.
getnumericalpermittivity("materialname", f,fmin, fmax, dt, component, use_bfast); | Optional 参数 use_bfast can be 0 or 1. It indicates whether the 仿真 is performed using the Broadband Fixed 角度 光源 Technique (BFAST) or not. The default is 0.

**示例**

This 示例 shows how to get the material 介电常数 with the getindex, getfdtdindex and getnumerical 介电常数 functions. In this case, we compare the experimental 介电常数 data to the theoretical FDTD fit of the that data as well as to the numerical 介电常数 that will result using a finite 值 of dt. 
    material="Si (Silicon) - Palik";   # material 
    source_min_f=c/800e-9;      # 光源 min 频率
    source_max_f=c/200e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    component = 1; # desired 介电常数 component x (1), y (2) or z (3). Relevant for anisotropic materials, default 1
    use_bfast = 0; # Change to 1 if using BFAST, default 0 

This 示例 shows how to get the material 介电常数 with the getindex, getfdtdindex and getnumerical 介电常数 functions. In this case, we compare the experimental 介电常数 data to the theoretical FDTD fit of the that data as well as to the numerical 介电常数 that will result using a finite 值 of dt. 
    material="Si (Silicon) - Palik";   # material 
    source_min_f=c/800e-9;      # 光源 min 频率
    source_max_f=c/200e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    component = 1; # desired 介电常数 component x (1), y (2) or z (3). Relevant for anisotropic materials, default 1
    use_bfast = 0; # Change to 1 if using BFAST, default 0 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex)
