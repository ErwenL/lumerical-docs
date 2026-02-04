<!--
Translation from English documentation
Original command: addsphere
Translation date: 2026-02-04 22:49:30
-->

# addsphere

添加 一个 sphere primitive 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addsphere; |  添加 一个 sphere primitive 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addsphere(struct_data); |  Adds a sphere primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 创建 一个 sphere 使用 一个 radius 的 5 um centered at (x,y,z) = (1, 2, 0) 微米.
    
    
    addsphere;
    设置("name","new_sphere");
    设置("x",1e-6);
    设置("y",2e-6);
    设置("z",0);
    设置("radius",5e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
