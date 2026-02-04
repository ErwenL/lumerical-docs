<!--
Translation from English documentation
Original command: adddevice
Translation date: 2026-02-04 22:49:04
-->

# adddevice

添加 一个 CHARGE 求解器 region 到 该 仿真 环境. 

注意:  The 'adddevice' 命令 是 deprecated 和 将 为 removed 在 future releases. Please refer 到 [ addchargesolver ](/hc/en-us/articles/360034924473-addchargesolver) as 一个 replacement.   
---  
**语法** |  **描述**  
---|---  
adddevice;  |  添加 一个 CHARGE 求解器 region 到 该 仿真 环境.  This 函数 does not 返回 any 数据.   
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal CHARGE 求解器 region, 设置 its 维度, 和 run 该 仿真. The 脚本 assumes 该 该 仿真 环境 already has 该 geometry 和 boundary conditions 设置 up. 
    
    
    adddevice;
    设置("求解器 geometry",1);  #  2D y-normal
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("z",0);
    设置("z跨度",10e-6);
    run;

**参见**

- [List 的 commands](./list-的-commands.md)
- [设置](./设置.md)
- [run](./run.md)
