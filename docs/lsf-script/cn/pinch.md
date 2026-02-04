# pinch

从矩阵中移除单例维度。

**语法** | **描述**
---|---
out = pinch(x); | 移除所有单例维度。例如，如果 x 是维度为 1x1x1xM 的矩阵，则

  * y=pinch(x);

将返回 Mx1 矩阵，其中

  * y(i) = x(1,1,1,i);

pinch(x,i); | 移除指定维度。如果 x 是 NxMxKxP 矩阵，则

  * y=pinch(x,2);

将返回 NxKxP 矩阵，其中

  * y(i,j,k) = x(i,1,j,k)

pinch(x,i,j); | 移除指定维度，但保留被移除维度的特定索引。如果 x 是 NxMxKxP 矩阵，则

  * y=pinch(x,2,4);

将返回 NxKxP 矩阵，其中

  * y(i,j,k) = x(i,4,j,k)

**示例**

此示例演示如何使用 pinch 从矩阵中移除单例维度。matrix 命令用于创建 6x1x4x1 矩阵。将 pinch 函数应用于此矩阵将移除两个单例维度，得到 6x4 矩阵。

```
x=matrix(6,1,4,1);
?size(x);
result:
6 1 4 1
?size(pinch(x));
result:
6 4
```

假设名为 "field" 的功率监视器是 XY 平面中的 2D 监视器，设置记录 200THz 到 300THz 之间的多个频率点。在这种情况下，变量 Ex 将是 4D 矩阵，维度为 length(X) by length(Y) by length(Z) by length(F)。由于这是 XY 平面中的 2D 监视器，只有一个 Z 位置，这意味着第三维（Z）的长度将为 1。

使用 pinch 和 find 命令，我们可以选择特定的频率进行成像。首先，find 命令用于确定最接近 250THz 的频率值的索引。接下来，pinch 命令用于选择与该频率对应的 Ex 中的数据。第二个 pinch 命令用于移除单例 Z 维度。最终结果是特定 z 和 f 值的 2D 矩阵 Ex(x,y)。

```
m="field";       # 监视器名称
x=getdata(m,"x");  # 获取监视器数据
y=getdata(m,"y");
z=getdata(m,"z");
f=getdata(m,"f");
Ex=getdata(m,"Ex");
fi=find(f,250e12);  # 找到对应 f=250THz 的索引
Ex=real(Ex);     # 取 Ex 的实部
?"Size of x: "+num2str(length(x)); # 在屏幕上打印矩阵大小
?"Size of y: "+num2str(length(y));
?"Size of z: "+num2str(length(z));
?"Size of f: "+num2str(length(f));
?"Size of Ex: "+num2str(size(Ex));
to_plot=pinch(Ex,4,fi);   # 选择频率。大小将为 length(x) by length(y) by length(z)
to_plot=pinch(to_plot);   # 移除单例 z 维度。大小将为 length(x) by length(y)
image(x*1e6,y*1e6,to_plot, "x (um)","y (um)","Ex at "+num2str(f(fi)/1e12)+ " THz" );
```

**另请参阅**

- [命令列表](./命令列表.md)
- [find](./find.md)
- [size](./size.md)
- [flip](./flip.md)
