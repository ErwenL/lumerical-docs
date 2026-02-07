<!--
Translation 从 English documentation
Original 命令: addcircle
Translation date: 2026-02-04 23:30:00
-->

# addcircle

添加 一个 [circle primitive](/hc/en-us/articles/360034901513) 到 该 仿真 环境。 Circles denote physical 对象 该 appear circular 或 ellipsoid 从 above。 These 对象 是 circles 或 ellipses 在 2D， 和 circular 或 ellipsoid cylinders 在 3D。

**语法** | **描述**
---|---
addcircle; | 添加 一个 circle primitive 到 该 仿真 环境。 This 函数 does not 返回any 数据。
addcircle(struct_data); |  Adds a circle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

The following 脚本 commands 将 创建一个 circle named "new_circle" 使用 一个 radius 的 5 um centered at (x，y，z) = (1, 2, 0) 微米。 The circle 将 have 一个 thickness (z跨度) 的 10 微米。


    addcircle;
    设置("name","new_circle");
    设置("x",1e-6);
    设置("y",2e-6);
    设置("radius",5e-6);
    设置("z",0);
    设置("z跨度",10e-6);

**参见**

- [List 的 commands](../lsf-脚本-commands-alphabetical.md)
- [设置](./设置.md)
