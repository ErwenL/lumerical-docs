# farfieldangle

返回与 2D 仿真中 farfield2d 数据对应的角度向量（以度为单位）。这是必需的，因为 farfield2d 不使用一组线性间隔的角度进行投影。使用 interp 或 spline 函数将数据重新插值到一组线性间隔的角度上通常很有用。

**语法** | **描述**
---|---
theta = farfieldangle( "mname", f, n, index); | 返回与 farfield2d 数据对应的角度矩阵
theta = farfieldangle( dataset, f, n, index); | 返回与 farfield2d 数据对应的角度矩阵

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
mname | 必填 | | 字符串 | 计算远场的监视器名称
dataset | 必填 | | 数据集 | 包含 E 和 H 的直线数据集
f | 可选 | 1 | 向量 | 所需频率点的索引。可以是单个数字或向量。如果 f 是向量，则 theta 的第二维将与频率点向量的长度匹配。R2016b 引入了多线程投影。
n | 可选 | 2000 | 数字 | 远场点数。
index | 可选 | 监视器中心处的值 | 数字 | 用于投影的材料折射率。

**示例**

此示例绘制名为 monitor 的 1D 监视器的远场投影。在此示例中，投影第二个频率点。如果监视器只包含一个频率的数据，则不需要第二个参数。直线数据集的远场投影示例请参阅 [farfield2d](./farfield2d.md)。

```powershell
E2=farfield2d("monitor",2,501);
theta=farfieldangle("monitor",2,501);
plot(theta,E2,"angle (deg)","|E|^2 far field");
```

更多示例请参阅 [远场投影](../远场投影.md)。

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfieldvector2d](./farfieldvector2d.md)、[farfieldpolar2d](./farfieldpolar2d.md)、[interp](./interp.md)、[spline](./spline.md)
