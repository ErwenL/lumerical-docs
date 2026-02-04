<!--
Translation from English documentation
Original command: addheatsolver
Translation date: 2026-02-04 22:49:29
-->

# addheatsolver

添加 一个 [thermal (HEAT) 求解器 region](/hc/en-us/articles/360034398234) 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addheatsolver; |  添加 一个 thermal (HEAT) 求解器 region 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addheatsolver(struct_data); |  Adds a thermal (HEAT) solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal HEAT 求解器 region, 设置 its 维度, 和 run 该 仿真. The 脚本 assumes 该 该 仿真 环境 already has 该 geometry 和 boundary conditions 设置 up.
    
    
    addheatsolver;
    设置("求解器 geometry",1);  #  2D y-normal
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("z",0);
    设置("z跨度",10e-6);
    run;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ run ](/hc/en-us/articles/360034931333-run)
