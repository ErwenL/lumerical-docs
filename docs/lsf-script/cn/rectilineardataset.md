<!--
Translation from English documentation
Original command: rectilineardataset
Translation date: 2026-02-03
-->

# rectilineardataset

创建一个与 x/y/z 坐标关联的空直角坐标系数据集（例如 E 和 H 场）。与矩阵数据集一样，直角坐标系数据集可以进行参数化，并可以包含任意数量的属性（参见 [addattribute](./addattribute.md)）和参数（参见 [addparameter](./addparameter.md)）。

更多信息请参阅[数据集介绍](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)。

对于不与 x/y/z 坐标关联的数据集（例如作为频率函数的透射率），请参见 [matrixdataset](./matrixdataset.md)。

**语法** | **描述**
---|---
rectilineardataset(x,y,z); | 创建一个与坐标 x/y/z 关联的空直角坐标系数据集。参数 'x'、'y' 和 'z' 可以有不同的长度，总点数是它们长度的乘积。
rectilineardataset("dataset_name",x,y,z); | 创建一个名为 "dataset_name" 的空直角坐标系数据集，与坐标 x/y/z 关联。参数 'x'、'y' 和 'z' 可以有不同的长度，总点数是它们长度的乘积。

**示例**

此示例创建一个名为 "Absorption" 的直角坐标系数据集，其中包含 2 个数据属性：功率吸收 Pabs 和折射率 n。这两个属性都是空间参数 x/y/z 和频率 'f' 的函数。为了让用户能够以频率或波长的形式访问频率参数，频率 (f) 和波长 (c/f) 都被添加为相互依赖的参数。

```lsf
Absorption = rectilineardataset("Absorption",x,y,z);
Absorption.addparameter("lambda",c/f,"f",f);
Absorption.addattribute("Pabs",Pabs);
Absorption.addattribute("refractive index",n);
visualize(Absorption); # 在可视化工具中可视化此数据集
```

以下脚本代码展示了如何从 FDTD 的频率监视器中获取原始数据（使用 getdata），以及如何从这些数据手动创建数据集。它还展示了如何使用单个命令（使用 getresult）直接从监视器获取电场数据集。

```lsf
# 监视器名称
m="monitor";
# 使用 getdata 获取单个数据元素
x=getdata(m,"x");
y=getdata(m,"y");
z=getdata(m,"z");
f=getdata(m,"f");
Ex=getdata(m,"Ex");
Ey=getdata(m,"Ey");
Ez=getdata(m,"Ez");
# 从原始数据创建电场数据集
E_manual = rectilineardataset("E_manual",x,y,z);  # 初始化数据集并提供空间位置向量
E_manual.addparameter("lambda",c/f,"f",f);  # 添加额外参数：频率
E_manual.addattribute("E",Ex,Ey,Ez);     # 添加矢量电场属性
# 以上所有命令都可以用一个 getresult 命令避免
E_fromMonitor = getresult(m,"E");
```

以下脚本代码展示了如何访问上面示例中创建的 'E_manual' 数据集中存储的数据。

```lsf
# 将数据集内容输出到提示
?E_manual;
# 获取参数
x   = E_manual.x;
y   = E_manual.y;
z   = E_manual.z;
f   = E_manual.f;
lambda = E_manual.lambda;
x_1  = E_manual.x(1);
# 获取属性。记住 E 是矢量量
Ex = E_manual.Ex; # Ex 分量
Ey = E_manual.Ey; # Ey 分量
Ez = E_manual.Ez; # Ez 分量
E2 = E_manual.E2; # |E|^2
E = E_manual.E;  # 在单个矩阵中获取所有分量。将向矩阵添加一个长度为 3 的额外维度，用于每个矢量分量。
```

**另请参见**

- [rectilineardataset](./rectilineardataset.md)
- [addattribute](./addattribute.md)
- [addparameter](./addparameter.md)
- [visualize](./visualize.md)
- [datasets](./datasets.md)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [matrixdataset](./matrixdataset.md)
- [struct](./struct.md)
