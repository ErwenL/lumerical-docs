# lookupwrite

向查找表文件写入设计和提取参数对。此函数必须在 lookupopen 之后且 lookupclose 之前调用。

**语法** | **描述**
---|---
out = lookupwrite ("filename","table",design, "extracted"); | 向查找表写入设计和提取参数对。design 和 extracted 参数是包含多个结构的单元数组，允许在多个设计和提取参数之间映射。此函数可以多次调用，每次调用时设计和提取参数将追加到当前文件。此函数必须在 lookupopen 之后且 lookupclose 之前调用。
out = lookupwrite ("filename"); | 获取脚本对象（在这种情况下是包含 xml 文件所有内容的单元数组）并保存到文件。

**示例**

以下脚本映射波导宽度和高度两个值到有效折射率和群折射率。

```
design = cell(2);
# extracted 包含 neff 和 ng
extracted = cell(2);
# design（输入参数）
design{1} = struct;
design{1}.name = "width";
design{1}.value = 5.03333e-07;
design{2} = struct;
design{2}.name = "heigth";
design{2}.value = 2.18889e-07;
# extracted（输出结果）
extracted{1} = struct;
extracted{1}.name = "neff";
extracted{1}.value = 2.1;
extracted{2} = struct;
extracted{2}.name = "ng";
extracted{2}.value = 4.42;
# 打开文件以写入表
lookupopen( "new.xml", "new_extracted" );
# 写入第一个 design/extracted 对
lookupwrite( "new.xml", design, extracted );
# 第二个 design/extracted 对
design{1}.value = 6.03333e-07;
design{2}.value = 1.18889e-07;
extracted{1}.value = 2.2;
extracted{2}.value = 4.45;
# 写入第二个 design/extracted 对
lookupwrite( "new.xml", design, extracted );
# 关闭文件
lookupclose( "new.xml" );
```

其中 "new.xml" 是包含表 "new_extracted" 的查找表：

```
<?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name = "new_extracted">
<association>
  <design>
    <value name="width" type="double">5.03333e-07</value>
    <value name="heigth" type="double">2.18889e-07</value>
  <design>
  <extracted>
    <value name="neff" type="double">2.1</value>
    <value name="ng" type="double">4.42</value>
  </extracted>
</association>
<association>
  <design>
    <value name="width" type="double">6.03333e-07</value>
    <value name="heigth" type="double">1.18889e-07</value>
  <design>
  <extracted>
    <value name="neff" type="double">2.2</value>
    <value name="ng" type="double">4.45</value>
  </extracted>
</association>
</lumerical_lookup_table>
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupclose](./lookupclose.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
