<!--
---
title: seticon
command_type: property
---
-->

# seticon

为元素设置用户定义的图标。

**语法** | **描述**
---|---
`seticon (name, icon);` | 为名为'**name**'的元素设置用户定义图标。参数'**icon**'应为矢量图像格式SVG（可缩放矢量图形）文件。

**示例**

将图标'transmission.svg'设置到现有的复合元素'COMPOUND_1'：

```
seticon("COMPOUND_1", "transmission.svg");
```

**另请参阅**

- [操作对象](manipulating-objects.md)
