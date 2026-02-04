<!--
Translation from English documentation
Original command: addfeemmesh
Translation date: 2026-02-03 23:46:26
-->

# addfeemmesh

向'FEEM'仿真中添加一个[mesh constraint (override region)](/hc/en-us/articles/360034397994)（网格约束/覆盖区域）。此命令要求对象树中存在FEEM求解器区域才能工作。

**Syntax** |  **Description**  
---|---  
addfeemmesh; |  向'FEEM'仿真环境中添加一个网格约束。此函数不返回任何数据。  
addfeemmesh(struct_data); |  添加一个FEEM网格约束，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例1**

以下脚本命令将向对象树中已存在的FEEM求解器添加一个网格约束，并打印其所有属性的名称。
    
    
    addfeemmesh;
    ?set;

**示例2**

以下脚本命令将向有限元IDE中的FEEM求解器区域添加一个网格约束，为其命名，将其分配给两个域之间的特定表面，并设置该表面上任何元素的最大边长。
    
    
    addfeemsolver;
    addfeemmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**参见**

- [addfeemsolver](./addfeemsolver.md)
