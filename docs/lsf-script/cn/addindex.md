<!--
Translation from English documentation
Original command: addindex
Translation date: 2026-02-04 22:49:29
-->

# addindex

添加 一个 index 监视器 到 该 仿真 环境. In MODE 一个 active varFDTD region needs 到 为 present 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addindex; |  添加 一个 index 监视器 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addindex(struct_data); |  Adds an index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal index 监视器 到 该 仿真 region 和 设置 its 维度.
    
    
    addindex;
    设置("name","index_monitor");
    设置("监视器 类型",2);  # 2D y-normal
    设置("x",0);
    设置("x跨度",5e-6);
    设置("y",0);
    设置("z",10e-6);
    设置("z跨度",5e-6);

If 一个 FDTD 该 index 监视器 holds results automatically without running simulations 如果 一个 求解器 region 是 present. The following 脚本 命令 将 添加 一个 求解器 region following 该 脚本 above 和 将 visualize 该 index preview.
    
    
    addfdtd;
    n = getresult("index_monitor","index preview");
    visualize(n);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addfdtd ](/hc/en-us/articles/360034924173-addfdtd) , [ addvarfdtd ](/hc/en-us/articles/360034924193-addvarfdtd) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
