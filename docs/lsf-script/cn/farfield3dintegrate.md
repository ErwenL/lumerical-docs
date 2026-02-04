# farfield3dintegrate

在 3D 仿真中，围绕 theta0 和 phi0 中心的锥体上积分远场投影，半角由 halfangle 指定。远场电场是方向余弦（ux, uy）的函数，但 farfield3dintegrate 会自动进行变量转换。同样，角度以度为单位指定，但在计算积分之前会转换为弧度。请参阅 farfield3d 文档以获取有关各种监视器方向的 ux、uy、na、nb 解释信息。

$$ \iint_{\theta, \phi} E^{2}(u x, u y) \sin (\theta) d \theta d \phi $$

**语法** | **描述**
---|---
out = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); | 积分 3D 远场投影数据。

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
E2 | 必填 | | 矩阵 | 来自 farfield3d 的 E 场数据
ux | 必填 | | 向量 | 来自 farfieldux 的 ux 数据。请注意，结果应该是一个向量，因此只需对 1 个频率点执行 farfieldux 脚本命令即可。
uy | 必填 | | 向量 | 来自 farfielduy 的 uy 数据。请注意，结果应该是一个向量，因此只需对 1 个频率点执行 farfieldux 脚本命令即可。
halfangle | 可选 | 90 | 向量 | 积分锥体的半角。单位为度。长度必须为 L 或 1。半角应在 0 到 90 度之间。
theta0 | 可选 | 0 | 向量 | 积分锥体的中心角度 theta。单位为度。长度必须为 L 或 1。theta0 应在 0 到 90 度之间。
phi0 | 可选 | 0 | 向量 | 积分锥体的中心角度 phi。单位为度。长度必须为 L 或 1。phi0 应在 0 到 360 度之间。

**示例**

计算从源发射到以 theta=phi=0 为中心的 30 度锥体远场中的功率比例。

```powershell
m="monitor1";
res = 201;
E2 = farfield3d(m,1,res,res);
ux = farfieldux(m,1,res,res);
uy = farfielduy(m,1,res,res);
halfangle=30;
theta0=0;
phi0=0;
cone_30 = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); # 在 30 度锥体内积分
total = farfield3dintegrate(E2, ux, uy); # 在整个半球上积分
T = transmission(m); # 发射到远场的源功率比例
?cone_30/total;  # 远场功率在 30 度锥体内的比例
?cone_30/total*T; # 发射到远场 30 度锥体内的源功率比例
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldux](./farfieldux.md)、[farfielduy](./farfielduy.md)、[farfieldspherical](./farfieldspherical.md)