<!-- Translation completed: 2026-02-03 -->
<!-- Original command: switchtolayout -->

# switchtolayout

将求解器切换到LAYOUT模式。LAYOUT模式允许您为新仿真添加和修改仿真对象。一旦运行仿真，求解器将进入ANALYSIS模式，此时无法添加或修改任何仿真对象(分析组的"Analysis"选项卡除外)。在ANALYSIS模式下，任何修改对象的命令都会返回错误。您必须切换到LAYOUT模式才能修改任何对象。注意：一旦求解器切换回LAYOUT模式，任何可用的结果都将丢失。

**语法** | **描述**
---|---
`switchtolayout;` | 从ANALYSIS模式切换到LAYOUT模式。此函数不返回任何数据。

**示例**

以下脚本命令首先运行FDTD仿真。求解器将进入ANALYSIS模式。然后使用"switchtolayout"命令进入LAYOUT模式，以便在下一行更改仿真温度。

```
run;
switchtolayout;
setnamed("FDTD","simulation temperature",400);  # simulation temp. set to 400 K
```

**参见**

[命令列表](List_of_commands.md), [layoutmode](layoutmode.md), [run](run.md), [setnamed](setnamed.md)
