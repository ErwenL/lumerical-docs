<!--
Translation 从 English documentation
Original 命令: adddgtdsolver
Translation date: 2026-02-04 23:30:33
-->

# adddgtdsolver

添加 一个 [DGTD 求解器 region](/hc/en-us/articles/360034397874) 到 该 仿真 环境。

**语法** | **描述**
---|---
adddgtdsolver; | 添加 一个 DGTD 求解器 region 到 该 仿真 环境。 This 函数 does not 返回any 数据。
adddgtdsolver(struct_data); |  Adds a DGTD solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例 1**

The following 脚本 commands 将 添加 一个 DGTD 求解器 到 该 对象 tree 和 print 该 name 的 all 的 its 属性。


    adddgtdsolver;
    ?设置;

**示例 2**

The following 脚本 命令 将 添加 一个 DGTD 求解器 region， assign it 到 一个 仿真 region， 和 设置 该 仿真 时间。


    adddgtdsolver;
    设置("求解器 geometry","仿真 region 1"); 
    设置("仿真 时间",100e-15);  # 100 fs

**参见**

[ adddgtdmesh ](/hc/en-us/articles/360034924993-adddgtdmesh)
