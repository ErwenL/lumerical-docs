<!--
Translation 从 English documentation
Original 命令: addchargemesh
Translation date: 2026-02-04 23:28:27
-->

# addchargemesh

添加 一个 [mesh constraint (override region)](/hc/en-us/articles/360034397994) 到 该 'CHARGE' 仿真。 A CHARGE 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work。

**语法** | **描述**
---|---
addchargemesh; | 添加 一个 mesh constraint 到 该 'CHARGE' 仿真 环境。 This 函数 does not 返回any 数据。
addchargemesh(struct_data); |  Adds a mesh constraint and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

The following 脚本 commands 将 添加 一个 mesh constraint 到 该 CHARGE 求解器 region 在 Finite Element IDE， name it， 设置 its 维度， 和 设置 该 maximum edge 长度 用于 any 元素 within 该 volume。


    addchargesolver;
    addchargemesh;
    设置("name","mesh_SCR");
    # 设置 dimension
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",0);
    设置("z跨度",10e-6);
    # restrict maximum edge length for elements
    设置("max edge length",5e-9);

**参见**

- [List of commands](../lsf-脚本-commands-alphabetical.md)
- [addchargesolver](./addchargesolver.md)
- [设置](./设置.md)
