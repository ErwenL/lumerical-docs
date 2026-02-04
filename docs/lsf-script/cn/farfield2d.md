# farfield2d

将给定的功率或场分布监视器或直线数据集投影到远场，投影到 1 米半径的半圆上。返回电场强度 |E|^2。farfield2d 不使用一组线性间隔的角度进行投影，请使用 [farfieldangle 脚本命令](./farfieldangle.md) 获取适当的角度向量。

**语法** | **描述**
---|---
out = farfield2d("mname", f, n, illumination, periods, index, direction); | 将给定的功率或场分布监视器投影到指定频率点的远场。结果是一个 NxM 矩阵，第一维是远场投影的分辨率，第二维是投影的频率点数。
out = farfield2d(dataset, f, n, illumination, periods, index, direction); | 将给定的直线数据集投影到指定频率点的远场。结果是一个 NxM 矩阵，第一维是远场投影的分辨率，第二维是投影的频率点数。

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
mname | 必填 | | 字符串 | 监视器名称
dataset | 必填 | | 数据集 | 包含 E 和 H 的直线数据集
f | 可选 | 1 | 向量 | 所需频率点的索引。f 可以是单个值，也可以是频率点向量。R2016b 引入了多线程投影。
n | 可选 | 2000 | 数字 | 远场点数。
illumination | 可选 | 1 | 数字 | 对于周期性结构。高斯照明：1 平面波照明：2
periods | 可选 | 1 | 数字 | 要使用的周期数
index | 可选 | 监视器中心处的值 | 数字 | 用于投影的材料折射率。
direction | 可选 | 最大功率流方向 | 数字 | 方向：可以是 +1 或 -1。

**示例**

此示例绘制名为 monitor 的 1D 监视器的远场投影。在此示例中，投影第二个频率点。如果监视器只包含一个频率的数据，则不需要第二个参数。

```powershell
E2=farfield2d("monitor",2,501);
theta=farfieldangle("monitor",2,501);
plot(theta,E2,"angle (deg)","|E|^2 far field");
```

以下示例绘制直线数据集的远场投影。这里，数据集来自 1D 监视器。

```powershell
dataset=getresult("monitor", "E");
dataset.addattribute("H",getattribute(getresult("monitor","H"),"H"));

E2=farfield2d(dataset,2,501);
theta=farfieldangle(dataset,2,501);
plot(theta,E2,"angle (deg)","|E|^2 far field");
```

更多示例请参阅 [远场投影](../远场投影.md)。

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldangle](./farfieldangle.md)、[farfieldvector2d](./farfieldvector2d.md)、[farfieldpolar2d](./farfieldpolar2d.md)、[farfieldexact2d](./farfieldexact2d.md)、[farfieldfilter](./farfieldfilter.md)、[farfieldexact](./farfieldexact.md)、[farfield2dintegrate](./farfield2dintegrate.md)