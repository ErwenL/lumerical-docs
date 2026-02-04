# farfieldexact

将完整的复矢量场投影到特定位置。预期在距离相当于一个波长的数量级时是正确的。来自多个监视器的投影可以相加以创建总远场投影 - 请参阅 [来自监视器盒的投影](**%20to%20be%20defined\**)。

farfieldexact 将任何表面场投影到由向量列表定义的点系列。每个评估点的 x、y、z 坐标从向量列表中逐元素获取。即，2D 仿真中第 i 个点位于 [x(i),y(i)]。此命令可以返回 E 场或 E 和 H 场的投影。

3D

向量列表 x、y、z 必须具有相同的长度 L 或长度为 1。当只返回 E 场时，数据以 Lx3 维矩阵形式返回。第一个索引表示由 x、y、z 中每个元素的一个元素定义的位置 [x(i),y(i),z(i)]；第二个索引表示 Ex、Ey 和 Ez。当同时返回 E 和 H 场时，数据以数据集形式返回，E 和 H 场与相应的 x、y、z 和频率/波长一起打包。

2D

向量列表 x、y 必须具有相同的长度 L 或长度为 1。当只返回 E 场时，数据以 Lx3 维矩阵形式返回。第一个索引表示由 x、y 中每个元素的一个元素定义的位置 [x(i),y(i)]；第二个索引表示 Ex、Ey 和 Ez。当同时返回 E 和 H 场时，数据以数据集形式返回，E 和 H 场与相应的 x、y 和频率/波长一起打包。

**语法** | **描述**
---|---
out = farfieldexact("mname", x, y, f, index); | 2D 远场精确投影。仅返回 E 场。
out = farfieldexact(dataset, x, y, f, index); | 2D 远场精确投影。仅返回 E 场。
out = farfieldexact("mname", x, y, opt); | 2D 远场精确投影。返回 E 场或 E 和 H 场。请参阅下表了解选项。
out = farfieldexact(dataset, x, y, opt); | 2D 远场精确投影。返回 E 场或 E 和 H 场。请参阅下表了解选项。
out = farfieldexact("mname", x, y, z, f, index); | 3D 远场精确投影。仅返回 E 场。
out = farfieldexact(dataset, x, y, z, f, index); | 3D 远场精确投影。仅返回 E 场。
out = farfieldexact("mname", x, y, z, opt); | 3D 远场精确投影。返回 E 场或 E 和 H 场。请参阅下表了解选项
out = farfieldexact(dataset, x, y, z, opt); | 3D 远场精确投影。返回 E 场或 E 和 H 场。请参阅下表了解选项

**参数** | **默认值** | **默认值** | **类型** | **描述**
---|---|---|---|---
mname | 必填 | | 字符串 | 计算远场的监视器名称
dataset | 必填 | | 数据集 | 包含 E 和 H 的直线数据集
x | 必填 | | 向量 | 计算远场的点的 x 坐标。必须长度为 L 或 1。
y | 必填 | | 向量 | 计算远场的点的 y 坐标。必须长度为 L 或 1。
z | 必填 | | 向量 | 计算远场的点的 z 坐标。必须长度为 L 或 1。
f | 可选 | 1 | 向量 | 所需频率点的索引。可以是单个数字或向量。R2016b 引入了多线程投影。
index | 可选 | 监视器中心处的值 | 数字 | 用于投影的材料折射率。
opt | 可选 | | 结构体 | 'opt' 参数包括以下选项："field"：此参数可选。它定义返回的场，可以是 "E" 或 "E and H"。"f"：此参数可选。它定义所需频率点的索引。可以是单个数字或向量。R2016b 引入了多线程投影。"index"：此参数可选。它定义用于投影的材料折射率。

[[注意：]] 使用数据集时，折射率的默认值为 1。

**示例**

此示例显示如何计算 y=0、z=1 时，x 从 -1 到 1 米的直线上 |E|^2 和 |H|^2。直线数据集的远场投影示例请参阅 [farfield3d](./farfield3d.md)。

```powershell
# 定义远场位置向量
res=100;
x=linspace(-1,1,res);
y=0;
z=1;
# 执行远场投影
E_H_far=farfieldexact("monitor",x,y,z,{"field":"E and H", "f":1});
E_far = E_H_far.E;
H_far = E_H_far.H;
E2_far = sum(abs(E_far)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
H2_far = sum(abs(H_far)^2,2); # H2 = |Hx|^2 + |Hy|^2 + |Hz|^2
# 绘制结果
plot(x,E2_far,"x","y","|E|^2 on line at y=0, z=1");
plot(x,H2_far,"x","y","|H|^2 on line at y=0, z=1");
```

此示例显示如何求和来自监视器盒的结果（通常围绕散射粒子）。

注意：请参阅在线章节 [远场投影](**%20to%20be%**20defined**) 了解更多关于某些项需要负号的原因。

```powershell
phi = linspace(0,360,201);
E2_xy = matrix(length(phi));
E2_yz = matrix(length(phi));
x = -sin(phi*pi/180);
y = cos(phi*pi/180);
z = 0;
temp = farfieldexact("x2",x,y,z,{"field":"E"}) + farfieldexact("y2",x,y,z,{"field":"E"}) + farfieldexact("z2",x,y,z,{"field":"E"})
   - farfieldexact("x1",x,y,z,{"field":"E"}) - farfieldexact("y1",x,y,z,{"field":"E"}) - farfieldexact("z1",x,y,z,{"field":"E"});
E2_xy = sum(abs(temp)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
plot(phi, E2_xy,"Phi (deg)","|E|^2","in XY plane");
```

以下示例显示 farfieldexact 和 farfieldexact3d 输出数据的不同方式。

当 x=[1 2], y=[1 2], z=[0]，

farfieldexact：结果是 2*3 矩阵。第一维是位置；第二是场分量。这计算位置 [1,1,0] 和 [2,2,0] 处的远场。

farfieldexact3d：结果是 2*2*1*3 矩阵。前三维是位置；第四维是场分量。这计算位置 [x,y,z] = [1,1,0]、[1,2,0]、[2,1,0]、[2,2,0] 处的远场。

```powershell
x=1:2;
y=1:2;
z=0;
m="monitor";
E_far=farfieldexact(m,x,y,z,{"field":"E"});
?size(E_far);
result:
2 3
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfield3d](./farfield3d.md)、[farfieldexact2d](./farfieldexact2d.md)、[farfieldexact3d](./farfieldexact3d.md)