# plotxy

创建线图。特别地，当数据集在不同位置向量上采样时使用此函数。

**语法** | **描述**
---|---
out = plotxy(x,y); | 创建 y vs x 的图，y 和 x 都是长度相同的 1D 向量。返回图号。
plotxy(x1,y1,x2,y2,xn,yn); | 创建包含多条曲线的图。xn-yn 对必须长度相同，但 x1、x2 和 xn 可以有不同的起始-结束值和分辨率。返回图号。
plotxy(x1,y1,x2,y2, "x label", "y label", "title"); | 创建带坐标轴标签和标题的线图，返回图号。

**示例**

此示例将生成包含两个不同分辨率的函数的图：

```
x1=linspace(0,2*pi,15);
y1=sin(x1);
x2=linspace(1,pi,3);
y2=x2/2;
plotxy(x1,y1,x2,y2,"x","y","title");
legend("y1=sin(x1) - 15 pts","y2=x2/2 - 3 pts");
```

下图显示了示例代码的输出。

**另请参阅**

- [命令列表](./命令列表.md)
- [plot](./plot.md)
- [legend](./legend.md)
- [image](./image.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [visualize](./visualize.md)
- [vectorplot](./vectorplot.md)
- [holdon](./holdon.md)
