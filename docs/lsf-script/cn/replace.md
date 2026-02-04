<!--
Translation from English documentation
Original command: replace
Translation date: 2026-02-03
-->

# replace

用新字符串替换字符串的子字符串。必须指定子字符串的起始位置。此函数也可用于在给定位置向字符串添加子字符串。

**语法** | **描述**
---|---
snew = replace(s,pos,len,s1); | 用 s1 中的字符串替换 s 中从位置 pos 开始的 len 个字符。如果 len 为 0，将在 pos-1 和 pos 之间插入字符串 s1。如果 len 为 -1（或任何小于 0 的值），将用 s1 替换 s 中从 pos 开始的所有剩余字符。位置 pos 可以是 1 到 length(s)。

**示例**

这些示例展示了如何替换字符串中的子字符串或在字符串的特定位置插入子字符串。

```lsf
?replace("1234567",3,1,"aa");
```
结果：
```
12aa4567
```

```lsf
?replace("1234567",3,0,"aa"); #插入字符串
```
结果：
```
12aa34567
```

```lsf
?replace("1234567",3,-1,"aa");
```
结果：
```
12aa
```

**另请参见**

- [命令列表](./command_list.md)
- [length](./length.md)
- [substring](./substring.md)
- [findstring](./findstring.md)
- [replacestring](./replacestring.md)
- [str2num](./str2num.md)
- [num2str](./num2str.md)
- [splitstring](./splitstring.md)
- [lower](./lower.md)
- [upper](./upper.md)
- [toscript](./toscript.md)
