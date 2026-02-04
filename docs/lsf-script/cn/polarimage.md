# polarimage

创建 2D 极坐标图像图。这通常用于绘制远场数据。

**语法** | **描述**
---|---
polarimage(ux,uy,data); | 创建 2D 图像图。data 必须是 N x M 维，并且

  * ux 是 N x 1 维，ux 从 -1 到 1
  * uy 是 M x 1 维，uy 从 -1 到 1

out = polarimage(ux,uy,data, "x label", "y label", "title"); | 创建带坐标轴标签的 2D 图像图。可选返回图号。
polarimage(ux,uy,data, "x label", "y label", "title", "options"); | 创建带坐标轴标签和选项的 2D 图像图，选项可以是

  * logplot

**示例**

此示例生成简单 2D 高斯函数的图像。

```
ux=linspace(-1,1,51);
uy=linspace(-1,1,61);
Ux=meshgridx(ux,uy);
Uy=meshgridy(ux,uy);
data = exp( 1-Ux^2-Uy^2);
# 使用 image 和 polarimage 脚本函数绘制数据
image(ux,uy,data,"ux","uy","Image plot");
polarimage(ux,uy,data,"ux","uy","Polar Image plot");
```

下图显示了结果图。

此示例演示如何将此函数与远场投影函数一起使用。

```
m="monitor1";   # 监视器名称
ux=farfieldux(m); # 位置向量
uy=farfielduy(m);
E2=farfield3d(m); # 远场 E2 数据
polarimage(ux,uy,E2,"ux","uy","far field |E|^2");
```

**另请参阅**

- [命令列表](./命令列表.md)
- [plot](./plot.md)
- [polar](./polar.md)
- [image](./image.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [visualize](./visualize.md)
- [命令列表](./命令列表.md)
