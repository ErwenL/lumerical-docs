<!--
Translation from English documentation
Original command: addanalysisprop
Translation date: 2026-02-03
-->

# addanalysisprop

向结构和分析组中设置的用户定义添加用户自定义分析属性。

**Syntax** | **Description**
---|---
addanalysisprop("property name", type, value); | 向选定的对象组添加分析属性。名称设置为"property name"。类型是0到8的整数。对应的变量类型为：0 - 数字 1 - 字符串 2 - 长度 3 - 时间 4 - 频率 5 - 材料 6 - 矩阵 7 - 单元格 8 - 结构体。新用户属性的值设置为value。

**Example**

添加一个名为"Pname"的长度变量作为分析组的分析属性

    addanalysisgroup;
    set("name","group");
    addanalysisprop("Pname", 2, 1e-6); # 2 represents Length

**参见**

- [Manipulating objects](../lsf-script-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
- [addanalysisresult](./addanalysisresult.md)