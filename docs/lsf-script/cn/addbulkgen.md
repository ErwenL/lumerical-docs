<!--
Translation from English documentation
Original command: addbulkgen
Translation date: 2026-02-03
-->

# addbulkgen

向仿真环境添加一个[体（光学）生成区域](/hc/en-us/articles/360034398074)。体生成（源）对象可用于创建分析太阳生成剖面。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** | **Description**
---|---
addbulkgen; | 添加体（光学）生成区域。此函数不返回任何数据。
addbulkgen(struct_data); | 添加体（光学）生成区域，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将向CHARGE求解器区域添加体生成（源）对象。该对象设置为考虑AM1.5G太阳光谱计算硅中的太阳生成率。

    addbulkgen;
    set("name","solar");# set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);
    # set parameters for analytic profile
    set("illumination face",6);  #  upper z
    set("spectrum",0);  # AM1.5G
    set("material",0);  # silicon
    set("interface reflection",1);  # air interface

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addimportgen](./addimportgen.md)