# meshgridx

在 x 方向创建 2D 网格。

**语法** | **描述**
---|---
out = meshgridx(x,y); | 如果 x 和 y 分别是维度为 nX1 和 mX1 的单列（或单行）向量，则命令

  * X = meshgridx(x,y);

将创建维度为 nXm 的 2D 矩阵，其中 X(i,j)=x(i)。

**示例**

此示例使用 image 函数显示 meshgrid 的输出。另参阅 image 函数帮助中使用 meshgrid 的另一个示例。

```
x=linspace(0,10,100);
y=linspace(0,10,10);
image(x,y,meshgridx(x,y),"x","y","meshgridx");
image(x,y,meshgridy(x,y),"x","y","meshgridy");
```

下图显示了示例代码的输出。

此示例使用网格函数创建 2D 高斯函数 Z(x,y)=exp( -x^2-y^2) 的图像图。

```
x=linspace(-3,3,100);
y=x;
X=meshgridx(x,y);
Y=meshgridy(x,y);
Z=exp( -X^2 -Y^2);
image(x,y,Z);
```

**另请参阅**

- [命令列表](./命令列表.md)
- [image](./image.md)
- [meshgridy](./meshgridy.md)
- [meshgrid3dx](./meshgrid3dx.md)
