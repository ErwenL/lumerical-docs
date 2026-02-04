<!-- Translated: 2026-02-03 -->
<!-- Original: try -->

# try

即使块内发生错误，也允许脚本执行继续。

**语法** | **描述**
---| ---
try { Command1; Command2; ... } | 运行命令块。如果发生错误，将显示错误消息并且脚本继续。
try { Command1; Command2: ... } catch(errMsg); | 运行命令块。如果发生错误，错误消息将存储在变量 "errMsg" 中并且脚本继续。

**示例**

将显示错误消息，但脚本将继续：

```lsf
a=1;
try {
 ?C;
}
?a;
Error: prompt line 3: C is not a valid function or variable name
Result:
1
```

不会显示错误消息，但会存储在变量 errMsg 中：

```lsf
a=1;
try {
 ?C;
} catch(errMsg);
?a;
?errMsg;
Result:
1
Error: prompt line 3, C is not a valid function or variable name
```

**另见**

[命令列表](./list-of-commands.md)、[if](./if.md)
