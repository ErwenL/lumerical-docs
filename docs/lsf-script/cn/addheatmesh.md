<!--
Translation from English documentation
Original command: addheatmesh
Translation date: 2026-02-04 00:14:16
-->

# addheatmesh

向'HEAT'仿真添加一个[网格约束（覆盖区域）](/hc/en-us/articles/360034397994)。要使此命令生效，对象树中必须存在HEAT求解器区域。

**Syntax** |  **Description**  
---|---  
addheatmesh; |  向'HEAT'仿真环境添加网格约束。此函数不返回任何数据。  
addheatmesh(struct_data); |  向'HEAT'仿真环境添加网格约束，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将在有限元IDE中向HEAT求解器区域添加网格约束，为其命名，设置其尺寸，并设置体积内任何单元的最大边长。
    
    
    addheatsolver;
    addheatmesh;
    set("name","mesh_SCR");
    # set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    # restrict maximum edge length for elements
    set("max edge length",5e-9);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [addheatsolver](./addheatsolver.md)
- [set](./set.md)
