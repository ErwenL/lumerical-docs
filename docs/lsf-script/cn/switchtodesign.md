<!-- Translation completed: 2026-02-03 -->
<!-- Original command: switchtodesign -->

# switchtodesign

将INTERCONNECT切换到DESIGN模式。DESIGN模式允许您为新仿真添加和修改电路元件。一旦运行仿真，求解器将进入ANALYSIS模式，此时无法添加或修改任何元件。在ANALYSIS模式下，任何修改或添加元件的命令都会返回错误。您必须切换到DESIGN模式才能进行此类操作。注意：一旦求解器切换回DESIGN模式，任何可用的结果都将丢失。

**语法** | **描述**
---|---
`switchtodesign;` | 将INTERCONNECT从ANALYSIS模式切换到DESIGN模式。此函数不返回任何数据。

**示例**

以下脚本命令首先运行INTERCONNECT仿真。求解器将进入ANALYSIS模式。然后使用"switchtodesign"命令进入DESIGN模式，以便在下一行更改仿真"bitrate"。

```
run;
switchtodesign;
setnamed('::Root Element','bitrate',2e10);  # bit rate set to 20 Gbit/sec
```

**参见**

[命令列表](List_of_commands.md), [switchtolayout](switchtolayout.md), [layoutmode](layoutmode.md), [designmode](designmode.md)
