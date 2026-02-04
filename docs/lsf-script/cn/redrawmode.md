<!--
Translation from English documentation
Original command: redrawmode
Translation date: 2026-02-03
-->

# redrawmode

此命令可用于确定自动重绘的当前状态。它还可以用于设置自动重绘的当前状态。在任何可能更改图形对象属性的脚本命令后，图形将重绘。

**语法** | **描述**
---|---
out = redrawmode; | out 的值指示自动重绘是关闭还是开启
| | - out=1：自动重绘开启
| | - out=0：自动重绘关闭
out = redrawmode(in); | 设置自动重绘关闭或开启。要开启，使用 in=1。要关闭，使用 in=0。执行命令后 out 的值被设置，使得执行此命令后 out=in。

**示例**

此示例使用 redrawmode 关闭自动重绘，然后将自动重绘恢复到执行此脚本之前的状态。

```lsf
redraw_state = redrawmode;
redrawoff;
for(i=1:60) {
  addcircle;
  set("x",i*1e-6);
}
redrawmode(redraw_state);
```

**另请参见**

- [操作对象](./command_list.md)
- [redraw](./redraw.md)
- [redrawoff](./redrawoff.md)
