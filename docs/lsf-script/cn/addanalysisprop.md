<!--
Translation 从 English documentation
Original 命令: addanalysisprop
Translation date: 2026-02-04 23:28:27
-->

# addanalysisprop

添加 一个 用户定义 自定义 分析 属性 到 该 setup 用户定义 在 结构 和 分析 groups。

**语法** | **描述**
---|---
addanalysisprop("属性 name"， 类型， 值); | 添加 一个 分析 属性 到 一个 选中的 对象 group。 The name 是 设置 到 "属性 name"。 The 类型 是 一个 integer 从 0 到 8。 The 对应的 变量 types 是: 0 - Number 1 - String 2 - Length 3 - Time 4 - Frequency 5 - Material 6 - Matrix 7 - Cell 8 - Struct The 值 的 该 新的 用户 属性 是 设置 到 值。

**示例**

添加 一个 长度 变量 called "Pname" as 一个 分析 属性 用于 该 分析 group


    addanalysisgroup;
    设置("name","group");
    addanalysisprop("Pname", 2, 1e-6); # 2 represents Length

**参见**

- [Manipulating 对象](../lsf-脚本-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
- [addanalysisresult](./addanalysisresult.md)
