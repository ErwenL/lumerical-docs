# toscript

Returns a string containing the equivalent script to generate a variable. This script
function is particularly useful when debugging cells and structure variables.

| **Syntax**                      | **Description**                                                                                                                                                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out=toscript(variable, expand); | Returns a string containing the equivalent script to generate ‘variable’. If ‘expand’ is true, matrix values will also be converted to script, regardless of their size – this can lead to large strings. To prevent the matrix values conversion set expand to ‘false’. The default for 'expand' is true. |

**Example**

Create a cell of structure variables and find an equivalent script that generates the
same cell.

```
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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ substring ](./substring.md) , [ findstring ](./findstring.md) ,
[ replace ](./replace.md) , [ str2num ](./str2num.md) , [ num2str ](./num2str.md) ,
[ splitstring ](./splitstring.md) , [ lower ](./lower.md) , [ upper ](./upper.md)
