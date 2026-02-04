<!--
Translation from English documentation
Original command: addefieldmonitor
Translation date: 2026-02-03 22:38:09
-->

# addefieldmonitor

向仿真环境中添加一个 [电场监视器](/hc/en-us/articles/360034918793)。此命令要求对象树中存在 CHARGE 求解器区域。

**Syntax** |  **Description**  
---|---  
addefieldmonitor; |  向仿真环境中添加一个电场监视器。此函数不返回任何数据。  
addefieldmonitor(struct_data); |  添加一个电场监视器，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向仿真环境中添加一个 2D y-法向电场监视器，设置其尺寸，启用静电势保存，并将数据保存到 .mat 文件中。
    
    
    addefieldmonitor;
    set("name","E_field");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("z",0);
    set("y span",5e-6);
    set("record electrostatic potential",1);
    set("save data",1);
    filename = "electric_field.mat";
    set("filename",filename);

**参见**

- [set](./set.md)
- [addbandstructuremonitor](./addbandstructuremonitor.md)
- [addchargemonitor](./addchargemonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)
