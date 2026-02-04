# plot

创建线图。所有数据集必须在相同的位置向量上采样。

有关在不同位置向量上采样的数据集，请参阅 plotxy。

**语法** | **描述**
---|---
out = plot(x,y); | 创建 y vs x 的图，y 和 x 都是长度相同的 1D 向量。返回图号。
plot(x,y); | x 是 nx1 矩阵。y 是 nxm 矩阵。这将生成包含 m 条线的图。（y(1:n,1) vs x，y(1:n,2) vs x 等）
plot(x,y1,y2,y3); | 创建包含 3 条曲线的图，x、y1、y2、y3 必须长度相同，返回图号。
plot(x,y, "x label", "y label", "title"); | 创建带坐标轴标签和标题的 y vs x 图，返回图号。
plot(x,y, "x label", "y label", "title", "options"); | 创建带有所需选项的图。选项列于下表中。返回图号。

绘图选项。可以包含单个字符串中的多个绘图选项，例如

```
"plot type=line, color=blue, pen=--, linewidth=2"
```

绘图类型 | line point bar
---|---|---
标记样式 | x o + s (方形) d (菱形)
笔划 | -- : -. -..
x 轴位置 | top bottom
y 轴位置 | left right
颜色 | blue red 等
灰度 |
绘图线 |
绘图条形 |
绘图点 |
标记大小（默认=4） | #
线宽（默认=1） | #

**示例**

此示例将生成包含两条线的图：sin(x) 和 (sin(x))^2。

```
x=linspace(0,10,100);
y1=sin(x);
y2=y1^2;
plot(x,y1,y2,"x","y","title");
legend("sin(x)", "sin(x)^2");
```

下图显示了示例代码的输出。

此示例将生成包含两条线 sin(x) 和 sin(x)^2 的图，带有更多绘图选项。

```
x=linspace(0,10,100);
y1=sin(x);
y2=y1^2;
plot(x,y1,"x","y","title", "plot type=line, color=red, pen=-., linewidth=2");
holdon;
plot(x,y2,"x","y","title", "plot type=line, color=blue, pen=--, linewidth=2");
legend("sin(x)", "sin(x)^2");
```

下图显示了示例代码的输出。

**另请参阅**

- [plotxy](./plotxy.md)
- [holdon](./holdon.md)
- [legend](./legend.md)
- [image](./image.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [visualize](./visualize.md)
- [vectorplot](./vectorplot.md)
- [polar](./polar.md)
