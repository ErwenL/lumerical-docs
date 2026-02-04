<!--
Translation from English documentation
Original command: addrect
Translation date: 2026-02-04 22:49:30
-->

# addrect

添加 一个 rectangle primitive 到 该 仿真 环境.

**语法** | **描述**  
---|---  
addrect; |  添加 一个 rectangle primitive 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addrect(struct_data); |  Adds a rectangle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 创建 一个 rectangle primitive, 设置 its 维度, 和 assigns 一个 材料 到 it.
    
    
    addrect;
    设置("name","new_rectangle");
    设置("x",1e-6);
    设置("x跨度",2e-6);
    设置("y",1e-6);
    设置("y跨度",5e-6);
    设置("z",0);
    设置("z跨度",10e-6);
    设置("材料","Si (Silicon) - Palik");
    

**参见**

[List 的 commands ](/hc/en-us/articles/360037228834), [设置](/hc/en-us/articles/360034928773-设置)
