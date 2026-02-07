<!--
Translation 从 English documentation
Original 命令: addbandstructuremonitor
Translation date: 2026-02-04 23:28:27
-->

# addbandstructuremonitor

添加 一个 [band 结构 监视器](/hc/en-us/articles/360034398174) 到 该 仿真 环境。 This 命令 需要 该 存在 的 一个 CHARGE 求解器 region 在 该 对象 tree。

**语法** | **描述**
---|---
addbandstructuremonitor; | 添加 一个 band 结构 监视器 到 该 仿真 环境。 This 函数 does not 返回any 数据。
addbandstructuremonitor(struct_data); |  Adds a band structure monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

The following 脚本 commands 将 添加 一个 bandstructure 监视器 到 该 仿真 环境 along 该 z axis， 设置 its 维度， 和 启用 保存 该 energy band 用于 该 vacuum level (Evac)。


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
