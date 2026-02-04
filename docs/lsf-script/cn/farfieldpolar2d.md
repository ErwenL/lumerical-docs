# farfieldpolar2d

将给定的功率或场分布监视器或直线数据集投影到远场，投影到 1 米半径的半圆上。这与 farfield2d 脚本命令类似，只是返回的是复电场，而不是场强。如果投影一个频率点，数据以 NxP 矩阵形式返回；如果投影多个频率点，数据以 NxPx3 形式返回，其中 N 是远场投影的分辨率，P 是投影的频率点数，最后一个索引表示圆柱坐标系中的 E_r、E_θ 和 E_z。对于 TM 仿真，由于唯一的非零场分量是 Ez，此函数给出的结果与 farfieldvector2d 完全相同。

**语法** | **描述**
---|---
out = farfieldpolar2d( "mname",...); | 返回极坐标复电场。参数与 farfield2d 相同。
out = farfieldpolar2d( dataset,...); | 返回极坐标复电场。参数与 farfield2d 相同。

**示例**

此示例绘制名为 "monitor" 的 1D 监视器的远场投影中 Er 分量的幅度。在此示例中，投影第二个频率点。如果监视器只包含一个频率的数据，则不需要第二个参数。直线数据集的远场投影示例请参阅 [farfield2d](./farfield2d.md)。

```powershell
E=farfieldpolar2d("monitor",2,501);
Er = abs(pinch(E,2,1)); # Er 的幅度
theta=farfieldangle("monitor",2,501);
plot(theta,Er,"angle (deg)","Er far field");
```

更多示例请参阅 [远场投影](**%20to%20be\**)。

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfieldvector2d](./farfieldvector2d.md)、[farfieldangle](./farfieldangle.md)