<!--
Translation from English documentation
Original command: savedata
Translation date: 2026-02-04 22:50:14
-->

# savedata

Saves workspace variables 到 一个 Lumerical 数据 文件 (ldf) 文件. To save 监视器 (D-card) 数据 到 一个 ldf 文件, see 该 savedcard 函数. 

**语法** |  **描述**  
---|---  
savedata("文件名");  |  Saves all current variables 到 该 specified 文件.  This 函数 does not 返回 any 数据.   
savedata("文件名", var1, var2,...);  |  Saves only variables 使用 该 specified names 到 文件.   
  
**示例**

This 是 一个 simple example 该 shows 如何 到 save two workspace variables 到 一个 .ldf 数据 文件. 
    
    
    x=1:10;
    y=x^2;
    savedata("x_squared_data", x, y);

This example shows 一个 section 的 code 该 could 为 used 到 save some specific 数据 从 一个 监视器 named xy_monitor. The 数据 是 first obtained 使用 脚本 functions such as getdata 和 transmission. These workspace variables 是 那么 saved 使用 该 savedata 函数. 

注意 该 该 complex 文件 names 可以 为 created 使用 该 num2str 命令. This 是 useful 当 doing 参数 sweeps 其中 一个 unique 文件 name 是 required 用于 each point 在 该 sweep. 
    
    
    # 获取 数据 从 该 仿真 到 为 saved
    mname="xy_monitor";       # 监视器 name
    x=getdata(mname,"x");      # position vectors associated 使用 Ex fields
    y=getdata(mname,"y");      # position vectors associated 使用 Ex fields
    Ex=getdata(mname,"Ex");     # Ex fields at 监视器
    T=transmission(mname);     # Power transmission through 监视器
     
    # save variables x, y, Ex, T 和 i 到 一个 数据 文件
    文件名="results_"+num2str(i); # 设置 文件名. i could 为 一个 loop counter 变量.
    savedata(文件名, x,y,Ex,T,i); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ savedcard ](/hc/en-us/articles/360034411154-savedcard) , [ loaddata ](/hc/en-us/articles/360034411214-loaddata) , [ workspace ](/hc/en-us/articles/360034409394-workspace) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave)
