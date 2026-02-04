<!--
Translation from English documentation
Original command: selectpartial
Translation date: 2026-02-03
-->

# selectpartial

选择具有给定部分名称的任何对象。

**语法** | **描述**
---|---
selectpartial("partialname"); | 选择对象名称中可以找到 "partialname" 的任何对象，前提是该对象不在组中。要选择位于组中的对象，请参阅下面的命令。
selectpartial("partialgroupname::partialname"); | 选择组名称中可以找到 "partialgroupname" 且对象名称中可以找到 "partialname" 的任何对象。

**示例**

创建两个对象并将它们放入组中。在组内创建三角形对象的额外副本。

```lsf
# 创建一个带有中心蚀刻通道的基底。将对象放入组中
addrect;
addtriangle;
selectpartial("angle"); # 选择 triANGLE 和 rectANGLE 两个对象
addtogroup("structure"); # 将选中的对象添加到组中
# 选择蚀刻并复制以创建第二个通道
selectpartial("structure::tri"); # 选择 TRIangle
copy(1e-6);            # 复制 TRIangle
```

**另请参见**

- [操作对象](./command_list.md)
- [groupscope](./groupscope.md)
