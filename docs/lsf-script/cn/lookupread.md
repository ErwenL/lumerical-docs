# lookupread

从包含设计参数和提取参数查找表的文件中查找最近的提取值。

**语法** | **描述**
---|---
out = lookupread ("filename","table",design,"extracted"); | 从包含设计参数和提取参数查找表的文件中查找最近的提取值。参数 table 是文件内查找表的名称，design 是包含多个结构的单元数组，用于定义要搜索的设计参数，extracted 是要提取的参数名称。它将返回位于最近设计参数处的值。
out = lookupread ("filename"); | 返回一个脚本对象，在这种情况下是包含 xml 文件所有内容的单元数组。

**示例**

加载与耦合器间隙相关联的耦合长度索引：

```
# design 单元包含设计/布局参数（输入搜索参数）
# "gap" 是文件中的属性名称
w_gap=3.5e-07;
design = cell(1);
design{1} = struct;
design{1}.name = "gap";
design{1}.value = w_gap;
# 从文件中读取耦合长度（使用 design 作为输入搜索 "coupling_length"）
cl=lookupread( "coupler_map.xml", "coupler_extracted", design, "coupling_length" );
?c1
7.18624026618721e-06
```

其中 "coupler_map.xml" 是一个查找表，包含耦合器间隙与耦合长度值之间的映射：

```
?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name = "coupler_extracted">
  <association>
    <design>
      <value name="gap" type="double">3.5e-07</value>
    </design>
    <extracted>
      <value name="coupling_length" type="double">7.18624026618721e-06</value>
    </extracted>
  </association>
...
</lumerical_lookup_table>
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupclose](./lookupclose.md)
- [lookupopen](./lookupopen.md)
- [lookupwrite](./lookupwrite.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
- [insert](./insert.md)
