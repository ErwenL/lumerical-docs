<!--
Translation from English documentation
Original command: addfeemmesh
Translation date: 2026-02-04 22:49:29
-->

# addfeemmesh

添加 一个 [mesh constraint (override region)](/hc/en-us/articles/360034397994) 到 一个 'FEEM' 仿真.. A FEEM 求解器 region 必须 为 present 在 该 对象 tree 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addfeemmesh; |  添加 一个 mesh constraint 到 该 'FEEM' 仿真 环境. This 函数 does not 返回 any 数据.  
addfeemmesh(struct_data); |  Adds a FEEM mesh constraint and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 mesh constraint 到 该 FEEM 求解器 already present 在 该 对象 tree 和 print 该 name 的 all 的 its 属性.
    
    
    addfeemmesh;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 mesh constraint 到 该 FEEM 求解器 region 在 Finite Element IDE, name it, assign it 到 一个 specific surface between two domains, 和 设置 该 maximum edge 长度 用于 any 元素 在 该 surface.
    
    
    addfeemsolver;
    addfeemmesh;
    设置("name","mesh_surface");
    设置("geometry 类型","surface");
    设置("surface 类型","domain:domain");
    设置("domain 1",2);
    设置("domain 2",3);
    设置("max edge 长度",0.05e-6);

**参见**

[ addfeemsolver ](/hc/en-us/articles/360034405014-addfeemmesh)
