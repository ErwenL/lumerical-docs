<!--
---
title: setname
command_type: property
---
-->

# setname

脚本命令`setname`用于设置数据集的名称。

**语法** | **描述**
---|---
`setname("test");` | 返回变量a的数据集名称。

**示例**

以下是一个简短的示例，其中我们创建一个名为tt的矩阵数据集，并将其分配给名为T的变量。使用`setname`脚本命令可以更改数据集的名称。

```
T = matrixdataset("tt");
T.setname("test");
?getname(T);
test
?T.getname;
test
```

**另请参阅**

- [getname](getname.md), [数据集](datasets.md)
