# farfieldvector3d

farfieldvector3d 函数类似于 farfield3d，但它返回的是复电场，而不是场强。如果投影一个频率点，数据以 NxMx3 矩阵形式返回；如果投影多个频率点，数据以 NxMx3xP 形式返回，其中 N 和 M 是空间索引，第三个索引表示球面坐标系中的 Ex、Ey 和 Ez，P 是频率点数。Ex、Ey 和 Ez 是电场矢量的复分量。请参阅 farfield3d 文档以获取有关各种监视器方向的 ux、uy、na、nb 解释信息。

**语法** | **描述**
---|---
out = farfieldvector3d( "mname",...); | 返回笛卡尔复电场。参数与 farfield3d 相同。
out = farfieldvector3d( dataset,...); | 返回笛卡尔复电场。参数与 farfield3d 相同。

**示例**

请参阅 [farfield3d](./farfield3d.md) 函数描述中的示例。

[了解远场投影中的场极化](**%20to%**)

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldpolar3d](./farfieldpolar3d.md)、[远场投影 - 场极化](**%20to\**)