<!--
Translation from English documentation
Original command: addchargemesh
Translation date: 2026-02-03
-->

# addchargemesh

向'CHARGE'仿真添加[网格约束（覆盖区域）](/hc/en-us/articles/360034397994)。对象树中必须存在CHARGE求解器区域，此命令才能正常工作。

**Syntax** | **Description**
---|---
addchargemesh; | 向'CHARGE'仿真环境添加网格约束。此函数不返回任何数据。
addchargemesh(struct_data); | 添加网格约束，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将向有限元IDE中的CHARGE求解器区域添加网格约束，为其命名，设置其尺寸，并设置体积内任何元素的最大边长。

    addchargesolver;
    addchargemesh;
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

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addchargesolver](./addchargesolver.md)
- [set](./set.md)