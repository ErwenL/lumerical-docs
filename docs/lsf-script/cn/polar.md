# polar

创建极坐标图。所有数据集必须在相同的角度值数组上采样。

有关在不同 theta 值数组上采样的数据集，请参阅 polar2。

**语法** | **描述**
---|---
out = polar(theta,rho) | 创建角度 theta 相对于半径 rho 的极坐标图。theta 是从 x 轴到以弧度指定的半径向量的角度；rho 是半径向量的长度。Theta 和 rho 可以是长度相同的向量，或者如果 theta 的长度为 n，则 rho 可以是 nxm 矩阵，对应 m 组 rho 值。返回图号。
polar(theta,rho1,rho2,rho3) | 创建带有三条曲线的极坐标图。theta、rho1、rho2、rho3 必须长度相同。返回图号。
polar(theta,rho,"x label", "y label", "title") | 创建带有坐标轴标签和标题的极坐标图。返回图号。
polar(theta,rho,"x label", "y label", "title", "options") | 创建带有所需选项的极坐标图。选项可以是

  * greyscale
  * polar（与 polar 脚本命令一起使用以生成与 polar 脚本命令相同的图）
  * 上述任何逗号分隔的列表

返回图号。

**示例**

创建简单的极坐标图。

```
theta = linspace(0,2*pi,100);
r = cos(theta);
polar(theta,r);
```

下图显示了示例代码的输出。

**另请参阅**

- [命令列表](./命令列表.md)
- [polar2](./polar2.md)
- [legend](./legend.md)
- [image](./image.md)
- [closeall](./closeall.md)
- [setplot](./setplot.md)
- [exportfigure](./exportfigure.md)
- [polarimage](./polarimage.md)
- [plot](./plot.md)
