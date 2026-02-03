<!--
Translation from English documentation
Original command: adddftmonitor
Translation date: 2026-02-03 10:57:34
-->

# adddftmonitor

向仿真环境中添加一个频域场分布监视器。默认情况下，此监视器会吸附到最近的网格单元以记录数据。若要在监视器放置的确切位置记录数据，请将对象属性中“高级”下的“空间插值”设置更改为“指定位置”。有关每种空间插值选项的详细信息，请参阅知识库文章 [Frequeny-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-Profile-and-Power-monitor-Simulation-object)。

**Syntax** |  **Description**  
---|---  
adddftmonitor; |  向仿真环境中添加一个场分布监视器。此函数不返回任何数据。  
adddftmonitor(struct_data); |  添加一个场分布监视器，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
以下脚本命令将向仿真区域添加一个 2D z-normal 频域场分布监视器，并设置其尺寸。
    
    
    adddftmonitor;  
    set("name","field_profile");  
    set("monitor type",7); # 2D z-normal  
    set("x",0);  
    set("x span",5e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);

**参见**

- [List of commands](./list-of-commands.md)
- [set](./set.md)
