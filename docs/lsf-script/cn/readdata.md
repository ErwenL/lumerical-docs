<!--
Translation from English documentation
Original command: readdata
Translation date: 2026-02-03
-->

# readdata

读取以行/列格式包含数据的文件。用户可以使用 readdata 命令导入存储在文本文件中的数值。数据必须正确格式化，以便每一行具有相同的列数。Readdata 将忽略任何以字母开头的行。支持的文件格式为 ASCII。

**语法** | **描述**
---|---
M=readdata("filename.txt"); | 将文本文件 filename 加载到矩阵变量 M 中。任何以字母开头的行都会被忽略。注意：此函数将在当前工作目录中查找文件。如果要读取的文件位于不同目录中，请指定完整路径或更改当前工作目录。

**示例**

如果您有一个名为 `testfile.txt` 的文本文件，其中包含以下数据：

```
Time Value
0.0 3.2e-6
1.0 2.8e10
2.0 4.1e5
3.0 3.3
```

第一行包含列标题，接下来的四行包含数据。在这种情况下，readdata 将忽略第一行，并将数据导入为一个 4x2 的矩阵。

```lsf
M=readdata("testfile.txt");
?M;
```

结果：
```
0 3.2e-006
1 2.8e+010
2 4.1e+005
3 3.3
```

**另请参见**

- [命令列表](./command_list.md)
- [rm](./rm.md)
- [write](./write.md)
- [read](./read.md)
- [str2num](./str2num.md)
- [findstring](./findstring.md)
- [replace](./replace.md)
- [replacestring](./replacestring.md)
- [fileexists](./fileexists.md)
