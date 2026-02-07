<!--
Translation 从 English documentation
Original 命令: addanalysisresult
Translation date: 2026-02-04 23:28:27
-->

# addanalysisresult

添加 一个 新的 result 到 一个 分析 group 对象。

**语法** | **描述**
---|---
addanalysisresult("A"); | 添加 一个 新的 result called "A" 到 一个 分析 group。

**示例**

添加 一个 result 变量 "A" 用于 output。 It 必须 为 calculated inside 该 分析 group。


    addanalysisgroup;
    设置("name","group");
    addanalysisresult("A"); # "A" is a result variable inside the analysis group. 

**参见**

- [Manipulating 对象](../lsf-脚本-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
