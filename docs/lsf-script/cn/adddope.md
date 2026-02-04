<!--
Translation from English documentation
Original command: adddope
Translation date: 2026-02-04 22:49:04
-->

# adddope

添加 一个 [constant doping 对象](/hc/en-us/articles/360034918653) 到 该 仿真 环境. This 命令 需要 一个 CHARGE 求解器 region 到 为 present 在 该 对象 tree.

**语法** |  **描述**  
---|---  
adddope; |  添加 一个 constant doping region. This 函数 does not 返回 any 数据.  
adddope(struct_data); |  Adds a constant doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 p-类型 constant doping 对象 和 设置 its 维度 和 concentration.
    
    
    adddope;
    设置("name","pwell");
    设置("dopant 类型","p");
    设置("concentration",1e25);  # SI unit (/m3)
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",1e-6);
    设置("z",5e-6);
    设置("z跨度",1e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ adddiffusion ](/hc/en-us/articles/360034924513-adddiffusion)
