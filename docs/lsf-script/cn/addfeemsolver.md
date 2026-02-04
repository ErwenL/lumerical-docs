<!--
Translation from English documentation
Original command: addfeemsolver
Translation date: 2026-02-04 22:49:29
-->

# addfeemsolver

添加 一个 [FEEM 求解器 region](/hc/en-us/articles/360034918393) 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addfeemsolver; |  添加 一个 FEEM 求解器 region 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addfeemsolver(struct_data);  |  Adds a FEEM solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 FEEM 求解器 到 该 对象 tree 和 print 该 name 的 all 的 its 属性.
    
    
    addfeemsolver;
    ?设置;

**示例 2**

The following 脚本 命令 将 添加 一个 FEEM 求解器 region 和 assign it 到 一个 仿真 region.
    
    
    addfeemsolver;
    设置("求解器 geometry","仿真 region 1");

**参见**

[ addfeemmesh ](/hc/en-us/articles/360034405014-addfeemmesh)
