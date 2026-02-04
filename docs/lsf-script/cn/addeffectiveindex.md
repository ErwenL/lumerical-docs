<!--
Translation from English documentation
Original command: addeffectiveindex
Translation date: 2026-02-04 22:49:04
-->

# addeffectiveindex

添加 一个 [effective index 监视器](/hc/en-us/articles/360034396454) 到 该 仿真 环境. This 命令 需要 该 存在 的 一个 active varFDTD 求解器 region.

**语法** |  **描述**  
---|---  
addeffectiveindex; |  添加 一个 effective index 监视器 到 该 varFDTD 求解器 region. This 函数 does not 返回 any 数据.  
addeffectiveindex(struct_data); |  Adds an effective index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 effective index 监视器 到 该 仿真 region 和 设置 its 维度.
    
    
    addeffectiveindex;
    设置("name","neff");
    设置("x",0);
    设置("x跨度",5e-6);
    设置("y",0);
    设置("y跨度",5e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
