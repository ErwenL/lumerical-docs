# polar2

创建极坐标图。特别地，当数据集在不同角度值数组上采样时使用此函数。

**语法** | **描述**
---|---
out = polar2(theta,rho) | 创建角度 theta 相对于半径 rho 的极坐标图。theta 是从 x 轴到以弧度指定的半径向量的角度；rho 是半径向量的长度。Theta 和 rho 可以是长度相同的向量，或者如果 theta 的长度为 n，则 rho 可以是 nxm 矩阵，对应 m 组 rho 值。返回图号。
polar2(theta1,rho1,theta2,rho2) | 创建带有两条曲线的图。两个数据集可以在不同的 theta 向量上采样。
polar2(theta,rho,"x label", "y label", "title") | 创建带坐标轴标签和标题的 y vs x 图，返回图号。
polar2(theta,rho,"x label", "y label", "title", "options") | 创建带有所需选项的图。选项可以是

  * greyscale
  * polar（与 polar 脚本命令相同）
  * 上述任何逗号分隔的列表

返回图号。

**示例**

在极坐标中绘制两个不同的数据集。

```
theta1 = linspace(0,2*pi,100);
r1 = cos(theta1);
theta2 = linspace(0,pi,50);
r2 = sin(theta2);
polar2(theta1,r1,theta2,r2);
```

下图显示了示例代码的输出。

**另请参阅**

- [命令列表](./命令列表.md)
- [polar](./polar.md)
- [legend](./legend.md)
- [image](./image.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [polarimage](./polarimage.md)
- [plot](./plot.md)
