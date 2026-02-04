<!--
---
title: setposition
command_type: property
---
-->

# setposition

设置元素的水平和垂直位置。

**语法** | **描述**
---|---
`setposition("element", x, y);` | 设置元素的垂直和水平位置。

**示例**

要将名为"Waveguide Coupler_1"的元素位置设置为x=1.0um和y=2um，使用以下脚本：

```
setposition("Waveguide Coupler_1", 1e-6, 2e-6);
```

**另请参阅**

- [操作对象](manipulating-objects.md), [getposition](getposition.md), [setrectangle](setrectangle.md)
