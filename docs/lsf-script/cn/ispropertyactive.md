<!--
Translation from English documentation
Original command: ispropertyactive
Translation date: 2026-02-03
-->

# ispropertyactive

如果元素"element"的属性"property"处于活动状态，则返回 true。

**语法** |  **描述**
---|---
out=ispropertyactive (element,property);  |  如果元素"element"的属性"property"处于活动状态，则返回 true。

**示例**

    addelement("CW Laser");
    ?ispropertyactive("CWL_1", "frequency");
    result:
    1

**相关命令**

- [List of commands](./List-of-commands.md)
- [hideproperty](./hideproperty.md)
- [hidecategory](./hidecategory.md)
- [annotateproperty](./annotateproperty.md)
