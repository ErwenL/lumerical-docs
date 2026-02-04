<!--
---
title: setrectangle
command_type: property
---
-->

# setrectangle

设置元素矩形的宽度或高度。

**语法** | **描述**
---|---
`setrectangle ("element", w, h);` | 设置元素矩形的宽度（**w**）和高度（**h**）。

**示例**

要将名为"Straight Waveguide_1"的波导元素设置为w=1um和h=0.5um，使用以下脚本：

```
setrectangle("Straight Waveguide_1", 1e-6, 0.5e-6);
```

**另请参阅**

- [操作对象](manipulating-objects.md), [getrectangle](getrectangle.md), [setposition](setposition.md)
