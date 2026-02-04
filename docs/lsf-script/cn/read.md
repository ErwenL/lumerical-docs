<!--
Translation from English documentation
Original command: read
Translation date: 2026-02-03
-->

# read

从文本文件中读取数据作为字符串。支持的文件格式为 ASCII。

**语法** | **描述**
---|---
read(filename, size); | 以用户定义的大小 'size' 读取文本文件作为字符串。如果未指定，size 的默认值为 1e+6。注意：此函数将在当前工作目录中查找文件。如果要读取的文件位于不同目录中，请指定完整路径或更改当前工作目录。

**注意**：此命令不能在[安全模式](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode)下使用。

**示例**

如果您有一个名为 `testfile.txt` 的文本文件，其中包含以下字符串：

```
String saved in text file
```

```lsf
M=read("testfile.txt");
?M;
```

输出：
```
String saved in text file
```

**另请参见**

- [命令列表](./command_list.md)
- [readdata](./readdata.md)
- [struct](./struct.md)
- [cell](./cell.md)
