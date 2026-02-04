<!-- Translated: 2026-02-03 -->
<!-- Original: toscript -->

# toscript

返回包含生成变量的等效脚本字符串。此脚本函数在调试单元格和结构变量时特别有用。

**语法** | **描述**
---| ---
out=toscript(variable, expand); | 返回包含生成'variable'的等效脚本的字符串。如果 'expand' 为 true，矩阵值也将转换为脚本，无论其大小——这可能导致较大的字符串。要防止矩阵值转换，将 expand 设置为 'false'。'expand' 的默认值为 true。

**示例**

创建一个结构变量单元格并找到生成相同单元格的等效脚本。

```lsf
v=cell(2);
v{1}=struct;
v{1}.name='value 1';
v{1}.value=matrix(4);
v{1}.value(1)=1;
v{1}.value(2)=2;
v{1}.value(3)=3;
v{1}.value(4)=4;
v{2}=struct;
v{2}.name='value 2';
v{2}.value=matrix(4);
v{2}.value(1)=5;
v{2}.value(2)=6;
v{2}.value(3)=7;
v{2}.value(4)=8;
?toscript(v,true);
v=cell(2);
v{1}=struct;
v{1}.name='value 1';
v{1}.value=matrix(4);
v{1}.value(1)=1;
v{1}.value(2)=2;
v{1}.value(3)=3;
v{1}.value(4)=4;
v{2}=struct;
v{2}.name='value 2';
v{2}.value=matrix(4);
v{2}.value(1)=5;
v{2}.value(2)=6;
v{2}.value(3)=7;
v{2}.value(4)=8;
?toscript(v,false); # do not include matrix values
v=cell(2);
v{1}=struct;
v{1}.name='value 1';
v{1}.value=matrix(4);
v{2}=struct;
v{2}.name='value 2';
v{2}.value=matrix(4);
```

**另见**

[命令列表](./list-of-commands.md)、[length](./length.md)、[substring](./substring.md)、[findstring](./findstring.md)、[replace](./replace.md)、[str2num](./str2num.md)、[num2str](./num2str.md)、[splitstring](./splitstring.md)、[lower](./lower.md)、[upper](./upper.md)
