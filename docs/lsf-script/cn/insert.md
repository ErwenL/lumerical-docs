<!--
Translation from English documentation
Original command: insert
Translation date: 2026-02-03
-->

# insert

将对象插入查找表中的现有单元格。

**语法** |  **描述**
---|---
out{1}.association = insert( out{1}.association, association, cell number );  |  将对象插入到现有单元格中。

**示例**

加载查找表 "coupler_map.ixml" 并打印包含 .ixml 文件所有内容的单元格数组

    clear;
    tabCoupler = lookupread( "coupler_map.ixml" );
    ?toscript( tabCoupler );

其中 "coupler_map.ixml" 是包含耦合器参数与不同 S 参数之间映射的查找表：

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

以下命令将对象插入到现有的查找表中

    association=struct;
    association.design=cell(1);
    association.design{1}=struct;
    association.design{1}.name='gap';
    association.design{1}.value=5e-007;
    association.extracted=cell(1);
    association.extracted{1}=struct;
    association.extracted{1}.name='coupling_length';
    association.extracted{1}.value=9e-006;
    # insert association at last position
    tabCoupler{1}.association = insert( tabCoupler{1}.association, association, 2 );
    # print updated values
    ?toscript(tabCoupler);
    lookupwrite( "coupler_map.ixml", tabCoupler );

现在表格打印如下：

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

以下命令将新的关联附加到现有的表中：

    clear;
    design=cell(1);
    design{1}=struct;
    design{1}.name='gap';
    design{1}.value=6e-007;
    # create extracted parameter
    extracted=cell(1);
    extracted{1}=struct;
    extracted{1}.name='coupling_length';
    extracted{1}.value=9.9e-006;
    # append to existing table
    lookupappend( "coupler_map.ixml", "coupler_extracted", design, extracted );
    # print contents
    ?toscript( lookupread( "coupler_map.ixml" ) );

现在查找表打印如下：

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

**相关命令**

- [List of commands](./List-of-commands.md)
- [lookupopen](./lookupopen.md)
- [lookupread](./lookupread.md)
- [lookupwrite](./lookupwrite.md)
- [lookupclose](./lookupclose.md)
- [lookupreadtable](./lookupreadtable.md)
- [lookupreadvalue](./lookupreadvalue.md)
- [lookupreadnportsparameter](./lookupreadnportsparameter.md)
- [lookupappend](./lookupappend.md)
