<!--
Translation from English documentation
Original command: addmode
Translation date: 2026-02-04 22:49:29
-->

# addmode

添加 一个 mode 源 到 该 仿真 环境 用于 FDTD. For MODE, 添加 一个 eigenmode (FDE) 求解器 region 到 该 仿真 环境.

注意:  The 'addmode' 命令 是 deprecated 在 MODE 和 将 为 removed 在 future releases. Please refer 到 [ addfde ](/hc/en-us/articles/360034404294-addfde) as 一个 replacement.  
---  
**语法** |  **描述**  
---|---  
addmode; |  For FDTD: 添加 一个 mode 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addmode; |  For MODE: 添加 一个 eigenmode 求解器 到 该 仿真 环境.  
addmode(struct_data); |  Adds a mode source (when used in FDTD) or an eigenmode solver (when used in MODE) and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 mode 源 在 FDTD 和 设置 its 维度 和 injection axis.
    
    
    addmode;
    设置("injection axis","x");
    设置("x",0);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",0);
    设置("z跨度",10e-6);

The following 脚本 commands 将 添加 一个 eigenmode (FDE) 求解器 region 在 MODE 在 该 XY plane 和 计算 该 eigen modes.
    
    
    addmode;
    设置("求解器 类型",3);
    设置("x",0);
    设置("x跨度",2e-6);
    设置("y",0);
    设置("y跨度",5e-6);
    设置("z",0);
    findmodes;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes)
