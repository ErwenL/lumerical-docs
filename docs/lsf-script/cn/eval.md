# eval

执行包含 Lumerical 脚本语言的字符串。

**语法** | **描述**
---|---
eval(string); | 执行字符串中的 Lumerical 脚本命令。此函数不返回任何数据。

**示例**

将字符串作为命令执行。

```powershell
eval("x=1+2;");
?x;
3
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[feval](./feval.md)、[str2num](./str2num.md)、[num2str](./num2str.md)、[lower](./lower.md)、[upper](./upper.md)、[toscript](./toscript.md)
