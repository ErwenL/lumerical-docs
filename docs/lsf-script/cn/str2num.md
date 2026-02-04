<!-- Translation completed: 2026-02-03 -->
<!-- Original command: str2num -->

# str2num

将字符串转换为浮点数。使用format脚本命令可更改输出精度。

**语法** | **描述**
---|---
`out = str2num(string);` | 将字符串转换为数值。

**示例**

将字符串转换为数字。

```
?str2num("1+2");
3
```

使用almostequal比较输出。

```
?almostequal(str2num("1.5677"), 1.5677);
result: 
1
```

**参见**

[命令列表](List_of_commands.md), [format](format.md), [findstring](findstring.md), [replace](replace.md), [replacestring](replacestring.md), [substring](substring.md), [lower](lower.md), [upper](upper.md), [toscript](toscript.md), [almostequal](almostequal.md)
