<!--
Translation from English documentation
Original command: addbandstructuremonitor
Translation date: 2026-02-04 22:46:39
-->

# addbandstructuremonitor

添加 a [band 结构 监视器](/hc/en-us/articles/360034398174) to the 仿真 environment. This 命令 requires the presence of a CHARGE 求解器 region in the 对象 tree.

**语法** |  **描述**  
---|---  
addbandstructuremonitor; |  添加 a band 结构 监视器 to the 仿真 environment. This 函数 does not 返回 any 数据.  
addbandstructuremonitor(struct_data); |  Adds a band structure monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands will 添加 a bandstructure 监视器 to the 仿真 environment along the z axis, 设置 its dimension, and enable saving the energy band for the vacuum level (Evac).
    
    
    addbandstructuremonitor;
    设置("name","band");
    设置("监视器 type",4);  # linear z
    设置("x",0);
    设置("y",0);
    设置("z",0);
    设置("z跨度",5e-6);
    设置("record Evac",1);

**参见**

- [List of commands](../lsf-脚本-commands-alphabetical.md)
- [设置](./设置.md)
- [addefieldmonitor](./addefieldmonitor.md)
- [addchargemonitor](./addchargemonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)
