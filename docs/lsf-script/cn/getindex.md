<!--
Translation from English documentation
Original command: getindex
Translation date: 2026-02-04 22:50:00
-->

# getindex

返回 该 complex refractive index 的 一个 材料 在 该 材料 database. The refractive index at 该 specified 频率 是 linearly interpolated 从 该 neighboring frequencies 其中 该 数据 是 available. 

**语法** |  **描述**  
---|---  
out = getindex("materialname", f);  |  返回 该 complex index 的 该 材料 使用 该 given name. The index 是 returned 用于 该 specified 频率 f. Frequency f 是 在 Hz.   
getindex("materialname", f, component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
  
**示例**

This example shows 如何 到 获取 材料 (n,k) 数据 使用 该 getindex 和 getfdtdindex functions. In 此 case, we compare 该 experimental 数据 到 该 fit 的 该 该 数据 该 将 为 used 在 该 仿真. 
    
    
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

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ getmodeindex ](**%20to%20be%20defined%20**) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getsurfaceconductivity ](/hc/en-us/articles/360034409754-getsurfaceconductivity)
