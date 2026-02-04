<!--
Translation from English documentation
Original command: hideproperty
Translation date: 2026-02-03
-->

# hideproperty

隐藏给定"元素"的"属性"。

**语法** |  **描述**
---|---
hideproperty (element,property,hide);  |  隐藏给定"元素"的"属性"。参数 'hide' 是布尔值。如果 'hide' 为 true，则该属性不可见；如果 'hide' 为 false，则该属性可见。'hide' 的默认值为 true。

**示例**

    addelement("CW Laser");
    hideproperty("CWL_1","linewidth", true);

**相关命令**

- [List of commands](./List-of-commands.md)
- [hidecategory](./hidecategory.md)
- [annotateproperty](./annotateproperty.md)
- [ispropertyactive](./ispropertyactive.md)
- [protectproperty](./protectproperty.md)
