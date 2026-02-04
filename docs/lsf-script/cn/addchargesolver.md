<!--
Translation from English documentation
Original command: addchargesolver
Translation date: 2026-02-04 22:49:04
-->

# addchargesolver

添加 一个 [electrical (CHARGE) 求解器 region](/hc/en-us/articles/360034924473) 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addchargesolver; |  添加 一个 electrical (CHARGE) 求解器 region 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addchargesolver(struct_data); |  Adds an electrical (CHARGE) solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal CHARGE 求解器 region, 设置 its 维度, 和 run 该 仿真. The 脚本 assumes 该 该 仿真 环境 already has 该 geometry 和 boundary conditions 设置 up.
    
    
    addchargesolver;
    设置("求解器 geometry",1);  # 2D y-normal
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("z",0);
    设置("z跨度",10e-6);
    run;

**参见**

- [List 的 commands](../lsf-脚本-commands-alphabetical.md)
- [设置](./设置.md)
- [run](./run.md)
