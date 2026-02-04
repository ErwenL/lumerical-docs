<!--
Translation from English documentation
Original command: holdon
Translation date: 2026-02-03
-->

# holdon

在单个图形上保持多个函数。请注意，只有第一个绘图的标签和绘图选项会被考虑；此时会报告警告。可以改用 setplot 命令。

**语法** |  **描述**
---|---
holdon;  |  打开在同一图形上保持多个数学函数的模式。

**示例**

此示例将基于 sin(x) 函数生成包含三条线的图形。

    # setup data
    # for logarithm, avoid non-positive values
    x1=linspace(1,10,100);
    x2=linspace(2,11,100);
    y1=sin(x1)+1.1;
    y2=y1^2+1.1;
    # plot y1, y2, y3
    plot(x1,y1,"x","y","holdon/off","log10x");
    holdon;
    plot(x2,y2,"xx","yy","title1","log10y, plot points");
    plot(x2,2*y2, "xxx","yyy", "title2", "greyscale");
    # plot labeling and options cannot work in hold on
    # use setplot command instead!
    legend("y1","y2","y3");
    holdoff;

下图显示了示例代码的输出。

**相关命令**

- [List of commands](./List-of-commands.md)
- [plot](./plot.md)
- [plotxy](./plotxy.md)
- [legend](./legend.md)
- [setplot](./setplot.md)
- [log](./log.md)
- [log10](./log10.md)
- [holdoff](./holdoff.md)
