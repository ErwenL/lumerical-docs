# mv

将文件移动到新位置。可以指定路径。

**语法** | **描述**
---|---
mv("file1","file2"); | 将 file1 移动到 file2。此函数不返回任何数据。
mv("path1\file1","path2\file2"); | 将 path1 中的 file1 移动到 path2 中的 file2。

**注意**：此命令不能在安全模式下使用。

**示例**

将 "myscript.lsf" 移动到 c:\working 并重命名为 "temp.lsf"。

```
mv("c:\myscript.lsf","c:\working\temp.lsf");
```

**另请参阅**

- [命令列表](./命令列表.md)
- [cp](./cp.md)
- [pwd](./pwd.md)
