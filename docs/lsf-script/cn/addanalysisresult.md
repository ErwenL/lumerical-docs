<!--
Translation from English documentation
Original command: addanalysisresult
Translation date: 2026-02-03
-->

# addanalysisresult

向分析组对象添加新结果。

**Syntax** | **Description**
---|---
addanalysisresult("A"); | 向分析组添加名为"A"的新结果。

**Example**

添加结果变量"A"用于输出。它必须在分析组内部计算。

    addanalysisgroup;
    set("name","group");
    addanalysisresult("A"); # "A" is a result variable inside the analysis group.

**参见**

- [Manipulating objects](../lsf-script-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)