# lookupappend

向现有查找表中插入新的关联关系。

**语法** | **描述**
---|---
lookupappend("filename", "table", design, "extracted"); | 向现有查找表中插入新的关联关系。

**示例**

加载查找表 "coupler_map.ixml" 并打印包含 .ixml 文件所有内容的单元数组。

```
clear;
tabCoupler = lookupread( "coupler_map.ixml" );
?toscript( tabCoupler );
```

其中 "coupler_map.ixml" 是一个查找表，包含耦合器参数与不同 s 参数之间的映射：

```
tabCoupler=cell(1);
tabCoupler{1}=struct;
tabCoupler{1}.association=cell(1);
tabCoupler{1}.association{1}=struct;
tabCoupler{1}.association{1}.design=cell(1);
tabCoupler{1}.association{1}.design{1}=struct;
tabCoupler{1}.association{1}.design{1}.name='gap';
tabCoupler{1}.association{1}.design{1}.value=3.5e-007;
tabCoupler{1}.association{1}.extracted=cell(1);
tabCoupler{1}.association{1}.extracted{1}=struct;
tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{1}.extracted{1}.value=7.18624e-006;
tabCoupler{1}.name='coupler_extracted';
```

以下命令向现有查找表中插入对象：

```
association=struct;
association.design=cell(1);
association.design{1}=struct;
association.design{1}.name='gap';
association.design{1}.value=5e-007;
association.extracted=cell(1);
association.extracted{1}=struct;
association.extracted{1}.name='coupling_length';
association.extracted{1}.value=9e-006;
# 在末尾位置插入关联
tabCoupler{1}.association = insert( tabCoupler{1}.association, association, 2 );
# 打印更新后的值
?toscript(tabCoupler);
lookupwrite( "coupler_map.ixml", tabCoupler );
```

现在表格打印如下：

```
tabCoupler=cell(1);
tabCoupler{1}=struct;
tabCoupler{1}.association=cell(2);
tabCoupler{1}.association{1}=struct;
tabCoupler{1}.association{1}.design=cell(1);
tabCoupler{1}.association{1}.design{1}=struct;
tabCoupler{1}.association{1}.design{1}.name='gap';
tabCoupler{1}.association{1}.design{1}.value=3.5e-007;
tabCoupler{1}.association{1}.extracted=cell(1);
tabCoupler{1}.association{1}.extracted{1}=struct;
tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{1}.extracted{1}.value=7.18624e-006;
tabCoupler{1}.association{2}=struct;
tabCoupler{1}.association{2}.design=cell(1);
tabCoupler{1}.association{2}.design{1}=struct;
tabCoupler{1}.association{2}.design{1}.name='gap';
tabCoupler{1}.association{2}.design{1}.value=5e-007;
tabCoupler{1}.association{2}.extracted=cell(1);
tabCoupler{1}.association{2}.extracted{1}=struct;
tabCoupler{1}.association{2}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{2}.extracted{1}.value=9e-006;
tabCoupler{1}.name='coupler_extracted';
```

以下命令将新关联追加到现有表中：

```
clear;
design=cell(1);
design{1}=struct;
design{1}.name='gap';
design{1}.value=6e-007;
# 创建提取参数
extracted=cell(1);
extracted{1}=struct;
extracted{1}.name='coupling_length';
extracted{1}.value=9.9e-006;
# 追加到现有表
lookupappend( "coupler_map.ixml", "coupler_extracted", design, extracted );
# 打印内容
?toscript( lookupread( "coupler_map.ixml" ) );
```

现在查找表打印如下：

```
value=cell(1);
value{1}=struct;
value{1}.association=cell(3);
value{1}.association{1}=struct;
value{1}.association{1}.design=cell(1);
value{1}.association{1}.design{1}=struct;
value{1}.association{1}.design{1}.name='gap';
value{1}.association{1}.design{1}.value=3.5e-007;
value{1}.association{1}.extracted=cell(1);
value{1}.association{1}.extracted{1}=struct;
value{1}.association{1}.extracted{1}.name='coupling_length';
value{1}.association{1}.extracted{1}.value=7.18624e-006;
value{1}.association{2}=struct;
value{1}.association{2}.design=cell(1);
value{1}.association{2}.design{1}=struct;
value{1}.association{2}.design{1}.name='gap';
value{1}.association{2}.design{1}.value=5e-007;
value{1}.association{2}.extracted=cell(1);
value{1}.association{2}.extracted{1}=struct;
value{1}.association{2}.extracted{1}.name='coupling_length';
value{1}.association{2}.extracted{1}.value=9e-006;
value{1}.association{3}=struct;
value{1}.association{3}.design=cell(1);
value{1}.association{3}.design{1}=struct;
value{1}.association{3}.design{1}.name='gap';
value{1}.association{3}.design{1}.value=6e-007;
value{1}.association{3}.extracted=cell(1);
value{1}.association{3}.extracted{1}=struct;
value{1}.association{3}.extracted{1}.name='coupling_length';
value{1}.association{3}.extracted{1}.value=9.9e-006;
value{1}.name='coupler_extracted';
```

**另请参阅**

- [命令列表](./命令列表.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupclose](./lookupclose.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [insert](./insert.md)
