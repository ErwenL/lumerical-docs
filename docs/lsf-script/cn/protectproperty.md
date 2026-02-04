# protectproperty

保护给定"元素"的"属性"。

**语法** | **描述**
---|---
protectproperty (element,property,protect); | 保护给定"元素"的"属性"。参数 'protect' 是布尔值。如果 'protect' 为 true，则属性受保护；如果 'protect' 为 false，则属性不受保护。'protect' 的默认值为 true。

**示例**

```powershell
createcompound;
addproperty("COMPOUND_1", "test_property");
protectproperty("COMPOUND_1", "test_property", 1);
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[hidecategory](./hidecategory.md)、[annotateproperty](./annotateproperty.md)、[ispropertyactive](./ispropertyactive.md)、[hideproperty](./hideproperty.md)
