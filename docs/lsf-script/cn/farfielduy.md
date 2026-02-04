# farfielduy

返回 3D 仿真中与 farfield3d 远场数据对应的 uy 矩阵。请参阅 farfield3d 文档以获取有关各种监视器方向的 ux、uy、na、nb 解释信息。

**语法** | **描述**
---|---
out = farfielduy("mname",f,na,nb,index); | 请参阅 farfield3d 帮助。参数与 farfield3d 相同。请注意，结果是一个 NxM 矩阵，其中 N 是空间索引，M 是频率点数。
out = farfielduy(dataset,f,na,nb,index); | 请参阅 farfield3d 帮助。参数与 farfield3d 相同。请注意，结果是一个 NxM 矩阵，其中 N 是空间索引，M 是频率点数。

**示例**

请参阅 [farfield3d](./farfield3d.md) 函数描述中的示例。

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldux](./farfieldux.md)、[farfieldspherical](./farfieldspherical.md)、[farfieldexact](./farfieldexact.md)、[远场投影 - 方向单位向量坐标](**%20to\**)