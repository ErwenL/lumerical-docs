<!--
---
title: setlayer
command_type: property
---
-->

# setlayer

设置选定的层构建器对象的指定层属性。必须选择有层构建器对象。

**语法** | **描述**
---|---
`setlayer("layer name", "property name", "property value");` | 设置选定层构建器对象的指定层属性。

**示例**

```
setlayer("abc", "thickness", 0.5e-6);
setlayer("abc", "background material", "Ag (Silver) - CRC");
setlayer("abc", "layer number", "(2:0 and 3:0) or 1:0"); # 生成对应层1:0的模式加上层2:0和3:0重叠的模式
setlayer("abc", "pattern material", "Ag (Silver) - CRC");
setlayer("abc", "name", "abc123"); # 将"abc"的名称更改为"abc123"
```

有关更多详细信息，请参考[这个示例](layer-builder.md)。

**另请参阅**

- [addlayerbuilder](addlayerbuilder.md), [getlayerlist](getlayerlist.md), [setlayer](setlayer.md), [loadgdsfile](loadgdsfile.md), [addlayer](addlayer.md), [getcelllist](getcelllist.md), [getlayerlist](getlayerlist.md)
