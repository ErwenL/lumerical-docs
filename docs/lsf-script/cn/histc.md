<!--
Translation from English documentation
Original command: histc
Translation date: 2026-02-03
-->

# histc

创建直方图。

**语法** |  **描述**
---|---
out = histc(y);  |  创建 y 的直方图。返回图形编号。
histc(y,n);  |  使用 n 个 bin 创建 y 的直方图。返回图形编号。
histc (y,n, "x label", "y label", "title");  |  使用 n 个 bin 创建 y 的直方图，并带有坐标轴标签和标题。返回图形编号。

**示例**

以下是创建简单直方图的脚本。

    #Creates a histogram plot of y.
    y = randmatrix(1,10);
    y = y*10;
    out = histc(y);
    #Creates a histogram plot of y, using n bins.
    #Returns the figure number.
    y = randmatrix(1,10);
    y = y*10;
    n = 5;
    out = histc(y,n);
    #Creates a histogram plot of y, using n bins, with axis labels and a title.
    histc (y,n, "x label", "y label", "title");

**相关命令**

- [List of commands](./List-of-commands.md)
- [histogram](./histogram.md)
- [legend](./legend.md)
- [plot](./plot.md)
- [closeall](./closeall.md)
- [visualize](./visualize.md)
