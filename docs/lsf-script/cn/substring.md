<!-- Translation completed: 2026-02-03 -->
<!-- Original command: substring -->

# substring

从字符串中提取子串。

**语法** | **描述**
---|---
`s1 = substring(s,pos);` | 返回s的子串，从位置pos开始到s的末尾。位置pos可以从1到length(s)。
`s1 = substring(s,pos,len);` | 返回s的子串，从位置pos开始，长度为len个字符。如果len为-1(或任何小于0的值)，则返回从位置pos到s末尾的子串。len的默认值为-1。

**示例**

以下示例展示了从字符串提取子串的不同方法。

```
?substring("hello",3);
llo
?substring("hello",3,2);
ll
```

**参见**

[命令列表](List_of_commands.md), [length](length.md), [findstring](findstring.md), [replace](replace.md), [replacestring](replacestring.md), [str2num](str2num.md), [num2str](num2str.md), [splitstring](splitstring.md), [lower](lower.md), [upper](upper.md), [toscript](toscript.md)
