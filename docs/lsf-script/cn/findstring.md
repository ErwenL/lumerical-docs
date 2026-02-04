# findstring

返回字符串中给定子字符串的位置。

**语法** | **描述**
---|---
pos = findstring(s,s1); | 返回 s1 在 s 中第一次出现的位置。如果在 s 中未找到 s1，则返回 -1。
pos = findstring(s,s1,p0); | 返回从位置 p0 开始，s1 在 s 中第一次出现的位置。如果从 p0 开始在 s 中未找到 s1，则返回 -1。

**示例**

以下是一些在字符串中查找子字符串的示例。

```powershell
?findstring("test12test34","test34");
result:
7
?findstring("test12test34","test");
result:
1
?findstring("test12test34","test",4);
result:
7
?findstring("test12test34","test",8);
result:
-1
```

**另请参阅**

[命令列表](../命令列表.md)、[length](./length.md)、[substring](./substring.md)、[replace](./replace.md)、[replacestring](./replacestring.md)、[str2num](./str2num.md)、[num2str](./num2str.md)、[splitstring](./splitstring.md)、[lower](./lower.md)、[upper](./upper.md)、[toscript](./toscript.md)