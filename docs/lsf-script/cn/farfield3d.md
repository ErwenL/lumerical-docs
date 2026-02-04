# farfield3d

在 3D 仿真中将给定的功率或场分布监视器或直线数据集投影到远场。返回电场强度 |E|^2。

**语法** | **描述**
---|---
out = farfield3d("mname",f, na, nb, illumination, periodsa, periodsb, index, direction); | 将给定的功率或场分布监视器投影到远场。如果投影 1 个频率点，返回 NxM 矩阵；如果投影多个频率点，返回 NxMxP 矩阵，其中 N 和 M 对应投影的分辨率（na 和 nb），P 对应投影的频率点数。
out = farfield3d(dataset,f, na, nb, illumination, periodsa, periodsb, index, direction); | 将给定的直线数据集投影到远场。如果投影 1 个频率点，返回 NxM 矩阵；如果投影多个频率点，返回 NxMxP 矩阵，其中 N 和 M 对应投影的分辨率（na 和 nb），P 对应投影的频率点数。

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
mname | 必填 | | 字符串 | 监视器名称
dataset | 必填 | | 数据集 | 包含 E 和 H 的直线数据集
f | 可选 | 1 | 向量 | 所需频率点的索引。可以是单个数字或向量。R2016b 引入了多线程投影以允许同时投影多个频率点。
na | 可选 | 150 | 数字 | 远场点数。
nb | 可选 | 150 | 数字 | 远场点数。
illumination | 可选 | 1 | 数字 | 对于周期性结构。高斯照明：1 平面波照明：2
periodsa | 可选 | 1 | 数字 | 用于周期性照明的周期数
periodsb | 可选 | 1 | 数字 | 用于周期性照明的周期数
index | 可选 | 监视器中心处的值 | 数字 | 用于投影的材料折射率。
direction | 可选 | 最大功率流方向 | 数字 | 方向：可以是 +1 或 -1。

下表总结了如何解释各种监视器方向的 ux、uy 坐标向量和周期输入属性。

**监视器方向** | **监视器表面法线** | **'na'、'ux'、'periods a' 对应** | **'nb'、'uy'、'periods b' 对应**
---|---|---|---
XY 平面 | Z | x 轴 | y 轴
XZ 平面 | Y | x 轴 | z 轴
YZ 平面 | X | y 轴 | z 轴

**示例**

此示例显示名为 monitor 的 2D 监视器的远场投影。在此示例中，投影第二个频率点。如果监视器只包含一个频率的数据，则不需要第二个参数。

```powershell
E = farfield3d("monitor",2);
ux = farfieldux("monitor",2);
uy = farfielduy("monitor",2);
image(ux,uy,E,"","","title","polar");
```

以下示例显示直线数据集的远场投影。这里，数据集来自 2D 监视器。

```powershell
dataset=getresult("monitor", "E");
dataset.addattribute("H",getattribute(getresult("monitor","H"),"H"));

E = farfield3d(dataset,2);
ux = farfieldux(dataset,2);
uy = farfielduy(dataset,2);
image(ux,uy,E,"","","title","polar");
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfieldvector3d](./farfieldvector3d.md)、[farfieldpolar3d](./farfieldpolar3d.md)、[farfieldux](./farfieldux.md)、[farfielduy](./farfielduy.md)、[farfieldexact3d](./farfieldexact3d.md)、[farfieldfilter](./farfieldfilter.md)、[farfield3dintegrate](./farfield3dintegrate.md)