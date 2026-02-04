<!--
Translation from English documentation
Original command: addemfieldtimemonitor
Translation date: 2026-02-04 22:49:29
-->

# addemfieldtimemonitor

添加 一个 时间 domain [EM (electro-magnetic) field 监视器](/hc/en-us/articles/360034918493) 到 仿真 使用 'DGTD' 求解器. A DGTD 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addemfieldtimemonitor; |  添加 一个 时间 domain EM field 监视器 到 该 'DGTD' 求解器. This 函数 does not 返回 any 数据.  
addemfieldtimemonitor(struct_data); |  Adds a time domain EM field monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 时间 domain EM field 监视器 到 该 'DGTD' 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 监视器.
    
    
    addemfieldtimemonitor;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 时间 domain EM field 监视器 到 该 'DGTD' 求解器, change its name, 和 assign it 到 一个 solid named "2D rectangle".
    
    
    addemfieldtimemonitor; 
    设置("name","时间");
    设置("geometry 类型","surface");
    设置("surface 类型","solid");
    设置("solid","2D rectangle");

NOTE:  The 脚本 above assumes 该 there 是 already 一个 solid named "2D rectangle" present 在 该 对象 tree.  
---  
  
**示例 3**

The following 脚本 commands 将 添加 一个 'point' 时间 domain EM field 监视器 到 该 'DGTD' 求解器 和 设置 its location.
    
    
    addemfieldtimemonitor; 
    设置("name","时间");
    设置("geometry 类型","point");
    设置("x",1e-6);
    设置("y",0);
    设置("z",0);

**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemfieldmonitor ](/hc/en-us/articles/360034925053-addemfieldtimemonitor) , [ addemabsorptionmonitor ](/hc/en-us/articles/360034405054-addemabsorptionmonitor)
