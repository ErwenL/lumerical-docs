# setresult

> **原文**: setresult  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

设置脚本元素或复合元素的结果。注意，此命令不能从脚本提示符或脚本文件编辑器中使用。它应该在脚本元素或复合元素的"仿真"选项卡中使用。

| **语法** | **说明** |
| --- | --- |
| setresult("result",value); | 将脚本/复合元素的"result"设置为指定值。"result"可以是矩阵或数据集。 |
| setresult("result",value,"kind (unit)"); | 将脚本/复合元素的"result"设置为具有给定描述的指定值。注意单位应放在括号中。 |
| setresult("result",x,y,"x title",'y title'); | 为脚本/复合元素设置"result"的x、y参数。这对可视化很有用。 |

**相关命令**

[getresult](./getresult.md)
