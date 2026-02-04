<!--
Translation from English documentation
Original command: image
Translation date: 2026-02-03
-->

# image

创建 2D 图像图。

**语法** |  **描述**
---|---
out = image(x,y,z);  |  创建 z 中数据的 2D 图像图。如果 x 的维度为 N x 1，y 的维度为 M x 1，则 z 的维度必须为 N x M。返回图形编号。
image(x,y,z, "x label", "y label", "title");  |  创建带有坐标轴标签和标题的 2D 图像图。返回图形编号。
image(x,y,z, "x label", "y label", "title", "options");  |  创建带有坐标轴标签和选项的 2D 图像图，选项可以是：

  * logplot
  * polar
  * red2blue
  * 以上任意以逗号分隔的列表

**示例**

此示例生成 2D 函数 pic(x,y)=sin(x)+sin(y) 的图形。

    x=linspace(0,10,100);
    y=linspace(0,10,100);
    x2=sin(x);
    y2=sin(y);
    pic=meshgridx(x2,y2)+meshgridy(x2,y2);
    image(x,y,pic,"","","","logplot");
    image(x,y,pic,"","","","logplot,red2blue");

下图显示了示例代码的输出。

**相关命令**

- [List of commands](./List-of-commands.md)
- [plot](./plot.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [visualize](./visualize.md)
- [polarimage](./polarimage.md)
- [vectorplot](./vectorplot.md)
