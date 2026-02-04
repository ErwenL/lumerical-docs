# farfieldexact3d

farfieldexact2d 的三维形式。此函数将完整的复矢量场投影到特定位置。预期在距离相当于一个波长的数量级时是正确的。来自多个监视器的投影可以相加以创建总远场投影 - 请参阅 [来自监视器盒的投影](**%20to%20be%20defined\**)。

farfieldexact3d 将任何表面投影到由向量 x、y 和 z 定义的网格点。如果只返回 E 场作为结果，当投影一个频率点时，数据以 NxMxKx3 维矩阵形式返回；当投影多个频率点时，数据以 NxMxKx3xP 维矩阵形式返回，其中 N 是向量 x 的长度，M 是向量 y 的长度，K 是向量 z 的长度，P 是频率点数，第四个索引表示 Ex、Ey 和 Ez。注意 N、M 和 K 可以为 1，当它们都为 1 时，此函数与 farfieldexact 相同。如果同时返回 E 和 H 场，数据以数据集形式返回，E 和 H 场与相应的 x、y、z 和频率/波长一起打包。

**语法** | **描述**
---|---
out = farfieldexact3d( "mname", x, y, z, f, index); | 将给定的功率或场分布监视器投影到由向量 x、y、z 指定的网格点的远场。仅返回 E 场。
out = farfieldexact3d( dataset, x, y, z, f, index); | 将给定的直线数据集投影到由向量 x、y、z 指定的网格点的远场。仅返回 E 场。
out = farfieldexact3d( "mname", x, y, z, opt); | 将给定的功率或场分布监视器投影到由向量 x、y、z 指定的网格点的远场。返回 E 场或 E 和 H 场。请参阅下表了解选项。
out = farfieldexact3d( dataset, x, y, z, opt); | 将给定的直线数据集投影到由向量 x、y、z 指定的网格点的远场。返回 E 场或 E 和 H 场。请参阅下表了解选项。

**参数** |  | **默认值** | **类型** | **描述**
---|---|---|---|---
mname | 必填 | | 字符串 | 计算远场的监视器名称
x | 必填 | | 向量 | 计算远场的网格点的 x 坐标
y | 必填 | | 向量 | 计算远场的网格点的 y 坐标
z | 必填 | | 向量 | 计算远场的网格点的 z 坐标
f | 可选 | 1 | 向量 | 所需频率点的索引。可以是单个数字或向量。R2016b 引入了多线程投影。
index | 可选 | 监视器中心处的值 | 数字 | 用于投影的材料折射率。
opt | 可选 | | 结构体 | 'opt' 参数包括以下选项："field"：此参数可选。它定义返回的场，可以是 "E" 或 "E and H"。"f"：此参数可选。它定义所需频率点的索引。可以是单个数字或向量。R2016b 引入了多线程投影。"index"：此参数可选。它定义用于投影的材料折射率。

[[注意：]] 使用数据集时，折射率的默认值为 1。

**示例**

此 3D 示例计算位于仿真区域上方 z=+1.5mm 距离处的 2mm x 2mm 图像平面上的远场电场强度。直线数据集的远场投影示例请参阅 [farfield3d](./farfield3d.md)。

```powershell
mname="trans";    # 监视器名称
num=25;       # 分辨率
# 定义用于成像场的远场平面
x=linspace(-1e-3,1e-3,num);
y=x;
z=1.5e-3;
# 计算远场
E=farfieldexact3d(mname,x,y,z,{"field":"E"});
# 选择分量
Ex=pinch(E,4,1);
Ey=pinch(E,4,2);
Ez=pinch(E,4,3);
# 成像强度
E2= abs(Ex)^2 + abs(Ey)^2 + abs(Ez)^2;
image(x*1e3,y*1e3,E2,"x (mm)","y (mm)","Electric field at z=1.5mm from source");
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
E_far=farfieldexact3d(m,x,y,z,{"field":"E"});
?size(E_far);
result:
2 2 1 3
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield3d](./farfield3d.md)、[farfieldexact2d](./farfieldexact2d.md)、[farfieldexact](./farfieldexact.md)