# farfieldpolar3d

farfieldpolar3d 函数类似于 farfield3d，但它返回的是复电场，而不是场强。如果投影一个频率点，数据以 NxMx3 矩阵形式返回；如果投影多个频率点，数据以 NxMx3xP 形式返回，其中 N 和 M 是空间索引，第三个索引表示球面坐标系中的 E_r、E_θ 和 E_φ，P 是频率点数。E_r、E_θ 和 E_φ 是电场矢量的复分量。请参阅 farfield3d 文档以获取有关各种监视器方向的 ux、uy、na、nb 解释信息。

注意：从 GUI 使用可视化器查看远场时，有三个属性可用：E2、Ep、Es。E2 对应 |E|^2，Ep 对应 Etheta，Es 对应 Ephi。

**语法** | **描述**
---|---
out = farfieldpolar3d( "mname",...); | 返回球面复电场。参数与 farfield3d 相同。
out = farfieldpolar3d( dataset,...); | 返回球面复电场。参数与 farfield3d 相同。

**示例**

请参阅 [farfield3d](./farfield3d.md) 函数描述中的示例。

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldvector3d](./farfieldvector3d.md)、[远场投影 - 场极化](**%20to%20be\**)