# farfieldspherical

将远场数据（3D 仿真）从 E(ux,uy) 插值到球坐标 E(theta,phi) 一维数组。远场投影函数通常将投影返回为 ux、uy（方向余弦）的函数。farfieldspherical 可用于将此数据插值为更常见的 theta、phi 单位。请参阅 farfield3d 文档以获取有关各种监视器方向的 ux、uy、na、nb 解释信息。

**语法** | **描述**
---|---
out = farfieldspherical( E2, ux, uy, theta, phi); | 将远场数据插值到球坐标。输出大小为 (MxN,1)

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
E2 | 必填 | | 矩阵 | 来自 farfield3d 的 E 场数据
ux | 必填 | | 向量 | 来自 farfieldux 的 ux 数据。请注意，结果应该是一个向量，因此只需对 1 个频率点执行 farfieldux 脚本命令即可。
uy | 必填 | | 向量 | 来自 farfielduy 的 uy 数据。请注意，结果应该是一个向量，因此只需对 1 个频率点执行 farfieldux 脚本命令即可。
theta | 必填 | | 向量 | theta 向量，以度为单位。必须长度为 M 或 1。
phi | 必填 | | 向量 | phi 向量，以度为单位。必须长度为 N 或 1。

**示例**

创建 phi=0 时 E2_far 对 theta 的图。

```powershell
m="Monitor1";  # 监视器名称
res = 201;    # 投影分辨率
E2 = farfield3d(m,1,res,res);
ux = farfieldux(m,1,res,res);
uy = farfielduy(m,1,res,res);
theta = linspace(-90,90,100);
phi = 0;
plot(theta, farfieldspherical(E2,ux,uy,theta,phi) ,"theta", "E^2", "E^2 at phi=0");
```

将场数据插值到 theta 和 phi 角度的网格。

```powershell
theta = linspace(-90,90,10);
phi = linspace(0,45,11);
Theta = meshgridx(theta,phi);
Phi = meshgridy(theta,phi);
E2_angle = farfieldspherical(E2,ux,uy,Theta,Phi);
E2_angle = reshape(E2_angle, [length(theta), length(phi)]);
image(theta, phi, E2_angle, "theta","phi","E2");
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldux](./farfieldux.md)、[farfielduy](./farfielduy.md)、[远场投影 - 方向单位向量坐标](**%20to\**)、[meshgridx](./meshgridx.md)、[meshgridy](./meshgridy.md)