<!--
Translation from English documentation
Original command: haveproperty
Translation date: 2026-02-03
-->

# haveproperty

返回具有特定属性的选定对象的数量。

**语法** |  **描述**
---|---
out = haveproperty("property");  |  返回具有指定属性的选定对象的数量。

**示例**

添加一个圆形和一个矩形。使用 haveproperty 显示两个对象都具有属性 'x'，但只有一个具有属性 'radius'。

    addcircle;
    addrect;
    selectall;
    ?haveproperty("x");
    ?haveproperty("radius");
    result:2
    result:
    1

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [get](./get.md)
- [set](./set.md)
