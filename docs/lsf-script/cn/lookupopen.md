# lookupopen

打开文件以写入查找表。

**语法** | **Description**
---|---
lookupopen ("filename","table"); | 打开文件以写入查找表。在调用任何 lookupwrite 之前必须使用此命令。

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
- [lookupclose](./lookupclose.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
