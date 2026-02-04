<!--
Translation from English documentation
Original command: hidecategory
Translation date: 2026-02-03
-->

# hidecategory

隐藏给定"元素"的给定"类别"的所有属性。

**语法** |  **描述**
---|---
hidecategory(element,category,hide);  |  隐藏给定"元素"的给定"类别"的所有属性。参数 'hide' 是布尔值。如果 'hide' 为 true，则该类别不可见；如果 'hide' 为 false，则该类别可见。'hide' 的默认值为 true。

**示例**

    addelement("CW Laser");
    hidecategory("CWL_1","Polarization", true);

**相关命令**

- [List of commands](./List-of-commands.md)
- [hideproperty](./hideproperty.md)
- [protectproperty](./protectproperty.md)
- [annotateproperty](./annotateproperty.md)
- [ispropertyactive](./ispropertyactive.md)
