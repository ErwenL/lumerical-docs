<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getfdtdindex -->

# getfdtdindex

    n_exp=getindex(material,f_vector);
    n_fdtd=getfdtdindex(material,f_vector,source_min_f,source_max_f);
    plot(c/f_vector*1e9,实部(n_exp),实部(n_fdtd),"wavelenth (nm)","n",material);
    legend("experimental data","FDTD fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_fdtd),"wavelenth (nm)","k",material);
    legend("experimental data","FDTD fit");
    data=矩阵(100,5);
    data(1:100,1)=c/f_vector*1e9;
    data(1:100,2)=实部(n_exp);
    data(1:100,3)=imag(n_exp);
    data(1:100,4)=实部(n_fdtd);
    data(1:100,5)=imag(n_fdtd);
    写入(material+".txt","wavelength_nm exp_n exp_k fdtd_n fdtd_k");
    写入(material+".txt",num2str(data));
This 示例 shows how to get the 介电常数 of a material. The getfdtdindex 和 getindex functions always 返回 the material index, so we must apply eps = n^2 to get the 介电常数. 
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    n_fdtd=getfdtdindex(material,f_vector,source_min_f,source_max_f);
    eps_fdtd=n_fdtd^2;    

**语法** | **描述**
---|---
out = getfdtdindex( "materialname", f, fmin, fmax); | 返回 the 复数 index of the material with the given name. The index is returned for the specified 频率 f. Similar to getindex, but you also specify fmin and fmax, the span of 频率 of the FDTD 仿真. All 频率 units are in Hz.
getfdtdindex("materialname", f,fmin, fmax, component); | Optional 参数 component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.

**示例**

This 示例 shows how to get material (n,k) data with the getindex and getfdtdindex functions. In this case, we compare the experimental data to the FDTD fit of the that data that will be used in the 仿真. 
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

This 示例 shows how to get material (n,k) data with the getindex and getfdtdindex functions. In this case, we compare the experimental data to the FDTD fit of the that data that will be used in the 仿真. 
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getmodeindex ](/hc/en-us/articles/360034930073) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getnumericalpermittivity ](/hc/en-us/articles/360034930093-getnumericalpermittivity)
