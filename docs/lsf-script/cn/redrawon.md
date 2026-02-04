<!--
Translation from English documentation
Original command: redrawon
Translation date: 2026-02-03
-->

# redrawon

启用 CAD 或原理图布局绘图中图形视口的自动更新。自动更新是默认行为，因此只有在使用 redrawoff 命令后才需要此命令。

**语法** | **描述**
---|---
redrawon; | 重新开启重绘。此函数不返回任何数据。

**示例**

此示例展示了如何通过禁用自动重绘来更快地添加对象。当禁用自动重绘时，以下 FOR 循环将运行得更快。

```lsf
redrawoff;    # 禁用自动重绘
for (i=1:1000) { # 添加 1000 个对象
 addcircle;
 set("radius",100e-9);
 set("x",i*1e-8);
 if (i==500) {
  redraw;   # 在循环中途强制重绘一次
 }
}
redrawon;     # 启用自动重绘
```

**另请参见**

- [操作对象](./command_list.md)
- [redraw](./redraw.md)
- [redrawoff](./redrawoff.md)
- [redrawmode](./redrawmode.md)
