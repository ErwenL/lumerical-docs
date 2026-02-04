<!--
Translation from English documentation
Original command: matlabsave
Translation date: 2026-02-04 22:50:13
-->

# matlabsave

## 注意

  * Starting 使用 Lumerical 2024 R1, MATLAB Linux libraries 是 no longer packaged 使用 该 Lumerical Applications
  * We still support MATLAB 文件 load 和 save 用于 versions 7 和 greater
  * See this [KB for more information](https://optics.ansys.com/hc/en-us/articles/360026142074#toc_3). 



Save Lumerical workspace variables 到 MATLAB .mat 数据 files.

**语法** |  **描述**  
---|---  
matlabsave(""); |  Save all workspace variables 到 一个 .mat 文件 该 has 该 same name as 该 仿真 文件. This 函数 does not 返回 any 数据.  
matlabsave("文件名"); |  Saves all workspace variables 到 该 specified .mat 文件.  
matlabsave("文件名", var1, ..., varN); |  Saves 该 specified workspace variables 到 该 .mat 文件.  
  
**示例**

Simple example:
    
    
    x=1:10;
    y=x^2;
    matlabsave("x_squared_data", x, y);

Save 数据 从 一个 监视器 named xy_monitor. The 数据 是 first obtained 使用 脚本 functions such as getdata 和 transmission. These workspace variables 是 那么 saved 使用 该 matlabsave 函数. 注意 该 complex 文件 names 可以 为 created 使用 该 num2str 命令. This 是 useful 当 doing 参数 sweeps 其中 一个 unique 文件 name 是 required 用于 each point 在 该 sweep.
    
    
    # 获取 raw 矩阵 数据 从 该 仿真
    mname="xy_monitor";       # 监视器 name
    x=getdata(mname,"x");      # position vectors associated 使用 Ex fields
    y=getdata(mname,"y");      # position vectors associated 使用 Ex fields
    Ex=getdata(mname,"Ex");     # Ex fields at 监视器
    T=transmission(mname);     # Power transmission through 监视器
     
    # save 矩阵 variables x, y, Ex, T 和 i 到 一个 数据 文件
    i=1;
    文件名="results_"+num2str(i); # 设置 文件名. i could 为 一个 loop counter 变量.
    matlabsave(文件名, x,y,Ex,T,i); 

Save 一个 Lumerical dataset (eg. Electric field vs x,y,z,f) 到 一个 .mat 文件. Lumerical data设置将 为 imported into Matlab 使用 该 结构体 数据 类型。
    
    
    # 获取 electric field dataset 从 该 仿真
    mname="xy_monitor";       # 监视器 name
    E=getresult(mname,"E");     # E fields at 监视器
     
    # save dataset 到 mat 文件
    文件名="ElectricField";
    matlabsave(文件名, E); 

**参见**

[MATLAB](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-script-integration)[ script integration – Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-script-integration)

[matlabput](https://optics.ansys.com/hc/en-us/articles/360034408014-matlabput), [matlabsavelegacy](https://optics.ansys.com/hc/en-us/articles/360034928133-matlabsavelegacy), [matlabload](https://optics.ansys.com/hc/en-us/articles/360034408034-matlabload), [vtksave](https://optics.ansys.com/hc/en-us/articles/360034411354-vtksave)
