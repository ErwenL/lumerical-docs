<!--
---
title: setnamed
command_type: property
---
-->

# setnamed

类似于`set`命令，但必须指定对象名称。此命令在分析模式下会返回错误。

**语法** | **描述**
---|---
`?setnamed("name");` | 返回名为name的对象的属性列表。
`setnamed("name", "property", value);` | 与set相同，但作用于具有特定名称的对象，而不是选定的对象。
`setnamed("name", struct);` | 结构体可以接受，代替"property"-value对参数。
`setnamed("name", "property", value, i);` | 当有多个对象具有相同名称时，此形式可用于设置第i个命名对象的属性。对象按其在对象树中的位置排序。最上面的选定对象被赋予索引1，索引号向下递增。
`setnamed("groupname::name", "property", value);` | 与set相同，但作用于在名为"groupname"的组中名为"name"的对象，而不是选定的对象。
`setnamed("groupname::name", "property", value, i);` | 当多个对象具有相同名称时，此形式可用于设置组"groupname"中第i个名为"name"的对象的属性。对象按其在对象树中的位置排序。最上面的选定对象被赋予索引1，索引号向下递增。

**示例**

将名为"circle"的对象的半径设置为10nm：

```
setnamed("circle", "radius", 10e-9);
```

为所有名为circle的选定对象的半径增加2微米：

```
for (i = 1; getnamednumber("circle")) {
    rad = getnamed("circle", "radius", i);
    setnamed("circle", "radius", rad + 2e-6, i);
}
```

使用结构体作为输入，设置名为"rectangle"的对象的坐标和尺寸：

```
coordinates = {"x": -3e-7,
               "x span": 1e-6,
               "y": 5e-6,
               "y span": 1e-5,
               "z": 1e-7,
               "z span": 2.2e-7};

setnamed("rectangle", coordinates);
```

**注意事项**

在INTERCONNECT中，在`setnamed`命令中输入元素属性值时必须使用固定的标准单位。在某些情况下，标准单位与属性视图中的默认单位不同。以下示例是设置ONA中心频率。中心频率的默认单位是THz，而标准单位是Hz，使用`setnamed`命令时，值需要以Hz为单位：

```
setnamed("ONA", "center frequency", 193.1e12);
```

要查找元素属性的标准单位，请在知识页面上打开该元素的帮助页面，查看默认单位列。当默认单位和标准单位不同时会包含一条注释。例如，参见[ONA](ona.md)的中心频率。

**另请参阅**

- [操作对象](manipulating-objects.md), [set](set.md), [get](get.md), [getnamed](getnamed.md), [getnamednumber](getnamednumber.md)
