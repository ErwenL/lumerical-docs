<!--
Translation from English documentation
Original command: getfdtdindex
Translation date: 2026-02-04 22:50:00
-->

# getfdtdindex

返回 该 complex refractive index 的 一个 材料 在 该 database 使用 材料 fit 该 将 为 used 在 一个 仿真 在 FDTD. 

Many materials (such as Sampled materials) have 属性 该 depend 在 频率. Using getfdtdindex, you 可以 specify 频率 range, 和 该 fitting routine 将 find 一个 best fit 的 该 材料 数据 over 该 range. The refractive index evaluated at 该 specified frequencies 是 那么 returned. 

注意 该 该 fit result depends 在 该 fit 参数, Max coefficients 和 Tolerance 设置 用于 该 材料, thus getfdtdindex result depends 在 那些 参数 as well. Tips 用于 setting 这些 参数 可以 为 found at [ Modifying 该 材料 fits ](/hc/en-us/articles/360034915053-Modifying-该-Material-Fits) . 

**语法** |  **描述**  
---|---  
out = getfdtdindex( "materialname", f, fmin, fmax);  |  返回 该 complex index 的 该 材料 使用 该 given name. The index 是 returned 用于 该 specified 频率 f. Similar 到 getindex, but you also specify fmin 和 fmax, 该 span 的 频率 的 该 FDTD 仿真. All 频率 units 是 在 Hz.   
getfdtdindex("materialname", f,fmin, fmax, component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
  
**示例**

This example shows 如何 到 获取 材料 (n,k) 数据 使用 该 getindex 和 getfdtdindex functions. In 此 case, we compare 该 experimental 数据 到 该 FDTD fit 的 该 该 数据 该 将 为 used 在 该 仿真. 
    
    
    材料="Au (Gold) - CRC";   # 材料 
    source_min_f=c/700e-9;      # 源 min 频率
    source_max_f=c/400e-9;      # 源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    # 获取 experimental 数据
    n_exp=getindex(材料,f_vector);
    # 获取 FDTD fit 的 experimental 数据
    n_fdtd=getfdtdindex(材料,f_vector,source_min_f,source_max_f);
    # plot results
    plot(c/f_vector*1e9,real(n_exp),real(n_fdtd),"wavelenth (nm)","n",材料);
    legend("experimental 数据","FDTD fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_fdtd),"wavelenth (nm)","k",材料);
    legend("experimental 数据","FDTD fit");
    # output index 数据 到 text 文件
    数据=矩阵(100,5);
    数据(1:100,1)=c/f_vector*1e9;
    数据(1:100,2)=real(n_exp);
    数据(1:100,3)=imag(n_exp);
    数据(1:100,4)=real(n_fdtd);
    数据(1:100,5)=imag(n_fdtd);
    write(材料+".txt","wavelength_nm exp_n exp_k fdtd_n fdtd_k");
    write(材料+".txt",num2str(数据));

This example shows 如何 到 获取 该 permittivity 的 一个 材料. The getfdtdindex 和 getindex functions always 返回 该 材料 index, so we 必须 apply eps = n^2 到 获取 该 permittivity. 
    
    
    材料="Au (Gold) - CRC";   # 材料 
    source_min_f=c/700e-9;      # 源 min 频率
    source_max_f=c/400e-9;      # 源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    # 获取 (n,k) 数据
    n_fdtd=getfdtdindex(材料,f_vector,source_min_f,source_max_f);
    # 获取 permittivity 数据
    eps_fdtd=n_fdtd^2;    

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getmodeindex ](/hc/en-us/articles/360034930073) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getnumericalpermittivity ](/hc/en-us/articles/360034930093-getnumericalpermittivity)
