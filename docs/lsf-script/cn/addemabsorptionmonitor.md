<!--
Translation from English documentation
Original command: addemabsorptionmonitor
Translation date: 2026-02-04 22:49:04
-->

# addemabsorptionmonitor

添加 一个 [absorption 监视器](/hc/en-us/articles/360034918573) 到 该 'DGTD' 求解器 在 Finite Element IDE. The 监视器 reports 该 power absorbed within 该 监视器 volume. A DGTD 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addemabsorptionmonitor; |  添加 一个 absorption 监视器 到 该 'DGTD' 求解器. This 函数 does not 返回 any 数据.  
addemabsorptionmonitor(struct_data); |  Adds an absorption monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 absorption 监视器 到 该 'DGTD' 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 监视器.
    
    
    addemabsorptionmonitor;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 absorption 监视器 到 该 'DGTD' 求解器, change its name, 设置 its 频率 span 到 为 该 same as 该 源, 和 assign it 到 一个 solid named "nanoparticle".
    
    
    addemabsorptionmonitor; 
    设置("name","Pabs");
    设置("use 源 limits",1);
    设置("reference 源","plane_wave");  
    设置("volume 类型","solid");
    设置("volume solid","nanoparticle");

NOTE:  The 脚本 above assumes 该 there 是 already 一个 solid named "nanoparticle" 和 一个 源 named "plane_wave" present 在 该 对象 tree.  
---  
  
**参见**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemfieldmonitor ](/hc/en-us/articles/360034405054-addemabsorptionmonitor) , [ addemfieldtimemonitor ](/hc/en-us/articles/360034925053-addemfieldtimemonitor)
