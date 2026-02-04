<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getdgtdindex -->

# getdgtdindex

    n_exp=getindex(material,f_vector);
    n_dgtd=getdgtdindex(material,f_vector,source_min_f,source_max_f);
    plot(c/f_vector*1e9,实部(n_exp),实部(n_dgtd),"wavelenth (nm)","n",material);
    legend("experimental data","DGTD fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_dgtd),"wavelenth (nm)","k",material);
    legend("experimental data","DGTD fit");
    data=矩阵(100,5);
    data(1:100,1)=c/f_vector*1e9;
    data(1:100,2)=实部(n_exp);
    data(1:100,3)=imag(n_exp);
    data(1:100,4)=实部(n_dgtd);
    data(1:100,5)=imag(n_dgtd);
    写入(material+".txt","wavelength_nm exp_n exp_k dgtd_n dgtd_k");
    写入(material+".txt",num2str(data));

**语法** | **描述**
---|---
out = getdgtdindex( "materialname", f, fmin, fmax); | 返回 the 复数 index of the material with the given name. The index is returned for the specified 频率 f. Similar to getindex, but you also specify fmin and fmax, the span of 频率 of the DGTD 仿真. All 频率 units are in Hz.

**示例**

This 示例 shows how to get material (n,k) data with the getindex and getdgtdindex functions. In this case, we compare the experimental data to the DGTD fit of the that data that will be used in the 仿真. 
注意 that the material "Au (Gold) - CRC" with optical material properties must already exist in the Materials Group before running the 脚本. 
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

This 示例 shows how to get material (n,k) data with the getindex and getdgtdindex functions. In this case, we compare the experimental data to the DGTD fit of the that data that will be used in the 仿真. 
注意 that the material "Au (Gold) - CRC" with optical material properties must already exist in the Materials Group before running the 脚本. 
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # 光源 min 频率
    source_max_f=c/400e-9;      # 光源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);

**另请参阅**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver)
