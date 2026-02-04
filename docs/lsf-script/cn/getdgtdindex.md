<!--
Translation from English documentation
Original command: getdgtdindex
Translation date: 2026-02-04 22:49:59
-->

# getdgtdindex

返回 该 complex refractive index 的 一个 材料 在 该 Materials Group 使用 材料 fit 该 将 为 used 在 一个 DGTD 仿真. 

Many materials (such as sampled materials) have 属性 该 depend 在 频率. Using getdgtdindex, you 可以 specify 频率 range, 和 该 fitting routine 将 find 一个 best fit 的 该 材料 数据 over 该 range. The refractive index evaluated at 该 specified frequencies 是 那么 returned. 

注意 该 该 fit result depends 在 该 fit 参数, Max coefficients 和 Tolerance 设置 用于 该 材料, thus getdgtdindex result depends 在 那些 参数 as well. Tips 用于 setting 这些 参数 可以 为 found at [ Modifying 该 材料 fits ](/hc/en-us/articles/360034915053-Modifying-该-Material-Fits) . 

**语法** |  **描述**  
---|---  
out = getdgtdindex( "materialname", f, fmin, fmax);  |  返回 该 complex index 的 该 材料 使用 该 given name. The index 是 returned 用于 该 specified 频率 f. Similar 到 getindex, but you also specify fmin 和 fmax, 该 span 的 频率 的 该 DGTD 仿真. All 频率 units 是 在 Hz.   
  
**示例**

This example shows 如何 到 获取 材料 (n,k) 数据 使用 该 getindex 和 getdgtdindex functions. In 此 case, we compare 该 experimental 数据 到 该 DGTD fit 的 该 该 数据 该 将 为 used 在 该 仿真. 

注意 该 该 材料 "Au (Gold) - CRC" 使用 optical 材料 属性 必须 already exist 在 该 Materials Group before running 该 脚本. 
    
    
    材料="Au (Gold) - CRC";   # 材料 
    source_min_f=c/700e-9;      # 源 min 频率
    source_max_f=c/400e-9;      # 源 max 频率
    f_vector=linspace(source_max_f,source_min_f,100);
    # 获取 experimental 数据
    n_exp=getindex(材料,f_vector);
    # 获取 DGTD fit 的 experimental 数据
    n_dgtd=getdgtdindex(材料,f_vector,source_min_f,source_max_f);
    # plot results
    plot(c/f_vector*1e9,real(n_exp),real(n_dgtd),"wavelenth (nm)","n",材料);
    legend("experimental 数据","DGTD fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_dgtd),"wavelenth (nm)","k",材料);
    legend("experimental 数据","DGTD fit");
    # output index 数据 到 text 文件
    数据=矩阵(100,5);
    数据(1:100,1)=c/f_vector*1e9;
    数据(1:100,2)=real(n_exp);
    数据(1:100,3)=imag(n_exp);
    数据(1:100,4)=real(n_dgtd);
    数据(1:100,5)=imag(n_dgtd);
    write(材料+".txt","wavelength_nm exp_n exp_k dgtd_n dgtd_k");
    write(材料+".txt",num2str(数据));

**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver)
