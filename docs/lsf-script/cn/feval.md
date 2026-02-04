# feval

将字符串作为脚本文件求值。此函数可用于运行不在路径中的脚本文件和名称中包含空格的脚本文件。

**语法** | **描述**
---|---
feval(filename); | 执行包含脚本文件名称的字符串。此函数不返回任何数据。

**示例**

运行脚本文件 C:\temp\example.lsf。

```powershell
feval("C:\temp\example.lsf");
```

**另请参阅**

[命令列表](../命令列表.md)、[eval](./eval.md)、[str2num](./str2num.md)、[num2str](./num2str.md)、[lower](./lower.md)、[upper](./upper.md)、[toscript](./toscript.md)