<!--
Translation from English documentation
Original command: adddgtdmesh
Translation date: 2026-02-04 22:49:04
-->

# adddgtdmesh

Adds a [mesh constraint (override region)](https://optics.ansys.com/hc/en-us/articles/360034397994) to a 'DGTD' simulation. A DGTD solver region must be present in the objects tree for this command to work.

**语法** |  **描述**  
---|---  
adddgtdmesh; |  添加 一个 mesh constraint 到 该 'DGTD' 仿真 环境. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 mesh constraint 到 该 DGTD 求解器 already present 在 该 对象 tree 和 print 该 name 的 all 的 its 属性.
    
    
    adddgtdmesh;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 mesh constraint 到 该 DGTD 求解器 region 在 Finite Element IDE, name it, assign it 到 一个 specific surface between two domains, 和 设置 该 maximum edge 长度 用于 any 元素 在 该 surface.
    
    
    adddgtdsolver;
    adddgtdmesh;
    设置("name","mesh_surface");
    设置("geometry 类型","surface");
    设置("surface 类型","domain:domain");
    设置("domain 1",2);
    设置("domain 2",3);
    设置("max edge 长度",0.05e-6);

**参见**

- [adddgtdsolver](./adddgtdsolver.md)
