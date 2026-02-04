<!-- Translation completed: Tue Feb 03 2026 -->
<!-- Original: savedata -->

# savedata

将工作区变量保存到 Lumerical 数据文件（ldf）中。要将监视器（D-card）数据保存到 ldf 文件，请参阅 savedcard 函数。

**语法** |  **描述**  
---|---  
savedata("filename");  |  将所有当前变量保存到指定文件。此函数不返回任何数据。  
savedata("filename", var1, var2,...);  |  仅将指定名称的变量保存到文件。  
  
**示例**

这是一个简单示例，显示如何将两个工作区变量保存到 .ldf 数据文件。
    
    
    x=1:10;
    y=x^2;
    savedata("x_squared_data", x, y);

此示例显示可用于保存名为 xy_monitor 的监视器中某些特定数据的代码段。数据首先通过 getdata 和 transmission 等脚本函数获取。然后使用 savedata 函数保存这些工作区变量。

注意，可以使用 num2str 命令创建复杂的文件名。这在进行参数扫描时很有用，因为扫描中的每个点都需要唯一的文件名。
    
    
    # get data from the simulation to be saved
    mname="xy_monitor";       # monitor name
    x=getdata(mname,"x");      # position vectors associated with Ex fields
    y=getdata(mname,"y");      # position vectors associated with Ex fields
    Ex=getdata(mname,"Ex");     # Ex fields at monitor
    T=transmission(mname);     # Power transmission through monitor
     
    # save variables x, y, Ex, T and i to a data file
    filename="results_"+num2str(i); # set filename. i could be a loop counter variable.
    savedata(filename, x,y,Ex,T,i); 

**另请参阅**

- [命令列表](./index.md)
- [savedcard](./savedcard.md)
- [loaddata](./loaddata.md)
- [workspace](./workspace.md)
- [matlabsave](./matlabsave.md)
