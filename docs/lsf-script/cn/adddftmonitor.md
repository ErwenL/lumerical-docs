<!--
Translation 从 English documentation
Original 命令: adddftmonitor
Translation date: 2026-02-04 23:30:23
-->

# adddftmonitor

Adds a frequency domain field profile monitor to the simulation environment. This monitor will snap to the nearest mesh cell to record the data by default. To record data exactly where the monitor is placed, change the “spatial interpolation” settings under “Advanced” in the object properties to “specified position”. Specifics regarding each spatial interpolation option can be found in the Knowledge Base article on [Frequeny-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-Profile-and-Power-monitor-Simulation-object).

**语法** | **描述**
---|---
adddftmonitor; | 添加 一个 field profile 监视器 到 该 仿真 环境。 This 函数 does not 返回any 数据。
adddftmonitor(struct_data); |  Adds a field profile monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

The following 脚本 commands 将 添加 一个 2D z-normal 频率 domain field profile 监视器 到 该 仿真 region 和 设置 its 维度。


    adddftmonitor;  
    设置("name","field_profile");  
    设置("监视器 类型",7); # 2D z-normal  
    设置("x",0);  
    设置("x跨度",5e-6);  
    设置("y",0);  
    设置("y跨度",5e-6);  
    设置("z",0);

**参见**

- [List 的 commands](./list-的-commands.md)
- [设置](./设置.md)
