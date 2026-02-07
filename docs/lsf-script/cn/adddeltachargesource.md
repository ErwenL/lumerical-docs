<!--
Translation 从 English documentation
Original 命令: adddeltachargesource
Translation date: 2026-02-04 23:30:14
-->

# adddeltachargesource

添加 一个 [delta optical generation 源](/hc/en-us/articles/360034398094) 到 该 仿真 环境。 This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree。

**语法** | **描述**
---|---
adddeltachargesource; | 添加 一个 delta optical generation 源 到 该 仿真 环境。 This 函数 does not 返回any 数据。
adddeltachargesource(struct_data); |  Adds a delta optical generation source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

The following 脚本 commands 将 添加 一个 delta optical generation 源， 设置 its location， 和 设置 该 generation rate 通过 defining 一个 net electron-hole-pair current (/sec)。


    adddeltachargesource;
    设置("name","delta");
    设置("x",0);
    设置("y",0);
    设置("z",5e-6);
    设置("源 类型",2);  #  ehp current
    设置("ehp current",1e12);  # net ehp current I_ehp = e*1e12 Amp

**参见**

- [List 的 commands](./list-的-commands.md)
- [设置](./设置.md)
- [addimportgen](./addimportgen.md)
- [addbulkgen](./addbulkgen.md)
