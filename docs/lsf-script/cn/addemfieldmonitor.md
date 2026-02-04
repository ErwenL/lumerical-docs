<!--
Translation from English documentation
Original command: addemfieldmonitor
Translation date: 2026-02-04 22:49:29
-->

# addemfieldmonitor

Adds a frequency domain [EM (electro-magnetic) field monitor](https://optics.ansys.com/hc/en-us/articles/360034918553) to a simulation with 'DGTD' solver . Along with the EM field data the monitor also reports the net flux through the surface of the monitor. A DGTD solver region must be present in the objects tree for this command to work.

**语法** |  **描述**  
---|---  
addemfieldmonitor; |  添加 一个 频率 domain EM field 监视器 到 该 'DGTD' 求解器. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 频率 domain EM field 监视器 到 该 'DGTD' 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 监视器.
    
    
    addemfieldmonitor;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 频率 domain EM field 监视器 到 该 'DGTD' 求解器, change its name, 设置 its 频率 span 到 为 该 same as 该 源, 和 assign it 到 一个 solid named "2D rectangle".
    
    
    addemfieldmonitor; 
    设置("name","T");
    设置("use 源 limits",1);
    设置("reference 源","plane_wave");  
    设置("surface 类型","solid");
    设置("solid","2D rectangle");

NOTE:  The 脚本 above assumes 该 there 是 already 一个 solid named "2D rectangle" 和 一个 源 named "plane_wave" present 在 该 对象 tree.  
---  
  
**参见**

[ adddgtdsolver ](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemabsorptionmonitor ](https://optics.ansys.com/hc/en-us/articles/360034405054-addemabsorptionmonitor) , [ addemfieldtimemonitor ](https://optics.ansys.com/hc/en-us/articles/360034925053-addemfieldtimemonitor)
