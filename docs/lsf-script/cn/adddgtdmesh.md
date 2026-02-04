<!--
Translation from English documentation
Original command: adddgtdmesh
Translation date: 2026-02-03 12:19:07
-->

# adddgtdmesh

向 'DGTD' 仿真中添加一个 [mesh constraint (override region)](https://optics.ansys.com/hc/en-us/articles/360034397994)。对象树中必须存在 DGTD 求解器区域，此命令才能工作。

**Syntax** |  **Description**  
---|---  
adddgtdmesh; |  向 'DGTD' 仿真环境中添加一个网格约束。此函数不返回任何数据。  
  
**示例 1**

以下脚本命令将向对象树中已存在的 DGTD 求解器添加一个网格约束，并打印其所有属性的名称。
    
    
    adddgtdmesh;
    ?set;

**示例 2**

以下脚本命令将向有限元 IDE 中的 DGTD 求解器区域添加一个网格约束，为其命名，将其分配给两个域之间的特定表面，并设置该表面上任何元素的最大边长。
    
    
    adddgtdsolver;
    adddgtdmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**参见**

- [adddgtdsolver](./adddgtdsolver.md)
