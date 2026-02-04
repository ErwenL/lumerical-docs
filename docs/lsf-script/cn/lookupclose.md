# lookupclose

关闭之前使用 lookupopen 命令创建的查找表文件。

**语法** | **描述**
---|---
lookupclose ("filename"); | 关闭之前使用 lookupopen 命令创建的文件。必须使用此命令才能关闭 lookupopen 打开的任何文件。

**示例**

要创建名为 "new_extracted" 的查找表 "new.xml"：

```
# 打开文件以写入查找表
lookupopen("new.xml", "new_extracted" );
...
# 写入 design/extracted 对
lookupwrite( "new.xml", design, extracted );
...
# 关闭文件
lookupclose("new.xml");
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
