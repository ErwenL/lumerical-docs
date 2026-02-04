<!--
---
title: setplot
command_type: property
---
-->

# setplot

设置图形的绘图属性。

**语法** | **描述**
---|---
`?setplot;` | 创建一个字符串，列出当前选定图形的所有图形属性。除非调用了`selectfigure()`命令，否则将选择最近创建的绘图。
`setplot("property", "property value");` | 将当前选定图形的所需属性设置为属性值。

**示例**

此示例使用脚本命令`setplot`查看折线图形的属性，然后为图形添加标题。

```
plot(1:10, (1:10)^2);
?setplot;
x min
x max
y min
y max
title
x label
y label
legend position
setplot("title", "my figure");  # 为图形添加标题
```

此示例创建一个10x10矩阵的随机数图像（数值范围在0到1之间），然后使用`setplot`命令将颜色条限制设置为0.2 - 0.8。

```
data = randmatrix(10, 10);
image(1:10, 1:10, data);
setplot("colorbar min", 0.2);
setplot("colorbar max", 0.8);
```

**另请参阅**

- [命令列表](list-of-commands.md), [image](image.md), [plot](plot.md), [visualize](visualize.md)
