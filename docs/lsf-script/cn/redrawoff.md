<!--
Translation from English documentation
Original command: redrawoff
Translation date: 2026-02-03
-->

# redrawoff

禁用 CAD 或原理图布局绘图中图形视口的自动更新。这可以大大提高添加大量对象的脚本的速度。

**语法** | **描述**
---|---
redrawoff; | 阻止图形重绘。此函数不返回任何数据。不能在组设置脚本中使用此命令，因为重绘会自动关闭。

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
- [redrawon](./redrawon.md)
- [redraw](./redraw.md)
- [redrawmode](./redrawmode.md)
