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
  
**示例1**

The following script commands will add a mesh constraint to the DGTD solver already present in the objects tree and print the name of all of its properties.
    
    
    adddgtdmesh;
    ?set;

**Example 2**

The following script commands will add a mesh constraint to the DGTD solver region in Finite Element IDE, name it, assign it to a specific surface between two domains, and set the maximum edge length for any element on the surface.
    
    
    adddgtdsolver;
    adddgtdmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**See Also**

- [adddgtdsolver](./adddgtdsolver.md)
