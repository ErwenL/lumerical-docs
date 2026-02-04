<!--
Translation from English documentation
Original command: addchargemonitor
Translation date: 2026-02-04 22:48:24
-->

# addchargemonitor

添加 一个 [charge 监视器](/hc/en-us/articles/360034398154) 到 该 仿真 环境. This 命令 requires 该 presence 的 一个 CHARGE 求解器 region 在 该 对象 tree.

**语法** |  **描述**  
---|---  
addchargemonitor; |  添加 一个 charge 监视器 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addchargemonitor(struct_data); |  Adds a charge monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 2D y-normal charge 监视器 到 该 仿真 环境, 设置 its dimension, 和 enable saving 该 charge 数据 在 一个 .mat file.
    
    
    addchargemonitor;
    设置("name","charge");
    设置("监视器 类型",6);  # 2D y-normal
    设置("x",0);
    设置("x跨度",5e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",0);
    设置("save 数据",1);
    filename = "charge_data.mat";
    设置("filename",filename);

**参见**

- [List 的 commands](../lsf-脚本-commands-alphabetical.md)
- [设置](./设置.md)
- [addbandstructuremonitor](./addbandstructuremonitor.md)
- [addefieldmonitor](./addefieldmonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)
