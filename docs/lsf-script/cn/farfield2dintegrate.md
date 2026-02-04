# farfield2dintegrate

在 2D 仿真中计算远场投影在某个 theta 范围内的积分。角度以度为单位指定，但积分以弧度进行。

$$ \int_{\theta} E^{2}(\theta) d \theta $$

**语法** | **描述**
---|---
out = farfield2dintegrate(E2, theta, halfangle, theta0); | 积分 2D 远场投影数据。

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
E2 | 必填 | | 矩阵 | 来自 farfield2d 的 E 场数据
theta | 必填 | | 矩阵 | 来自 farfieldangle 的 theta
halfangle | 可选 | 90 | 向量 | 积分区域的半角（度）。必须与 theta0 长度相同或长度为 1。半角应在 0 到 90 度之间。
theta0 | 可选 | 0 | 向量 | 积分区域的中心角度 theta（度）。必须与 halfangle 长度相同或长度为 1。theta0 应在 -90 到 90 度之间。

**示例**

计算 20 到 70 度远场功率的比例。

```powershell
m="monitor1";
E2=farfield2d(m);
theta=farfieldangle(m);
?farfield2dintegrate(E2,theta,25,45) / farfield2dintegrate(E2,theta);
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfieldangle](./farfieldangle.md)