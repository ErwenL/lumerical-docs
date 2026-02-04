<!-- Translation: unstructureddataset -->
<!-- Date: 2026-02-03 -->
<!-- Original: unstructureddataset -->

# unstructureddataset

创建一个空数据集，该数据集与空间中任意x/y/z坐标相关联，并通过额外的矩阵——连通性矩阵进行连接。连通性矩阵位于x、y、z之后。与矩形数据集一样，非结构化数据集可以被参数化，并且可以包含任意数量的属性（参见[addattribute](./addattribute.md)）和参数（参见[addparameter](./addparameter.md)）。

有关更多信息，请参阅[数据集介绍](./datasets.md)。对于不与x/y/z坐标相关联的数据集（例如，作为频率函数的透射率），请参见[matrixdataset](./matrixdataset.md)。

**语法** | **说明**
---|---
unstructureddataset(x,y,z,C); | 创建一个与坐标x/y/z和连通性矩阵相关联的空非结构化数据集。参数'x'、'y'和'z'必须具有相同的长度；等于总点数。参数'C'应该是一个整数矩阵，其中行数等于网格中的形状数，列数应为2（线段）、3（三角形）或4（四面体），值应为整数。

**示例**

下面是非结构化数据集用法的简单示例。x、y和z向量表示空间中的任意点，C表示连接它们的连通性矩阵。向量的值可以从[unstructured_charge_example.mat](./unstructured_charge_example.mat)文件加载。可以进一步脚本化此过程并将数据导入对象，例如，np密度网格属性，请参见[importdataset](./importdataset.md)命令。


    # 构建非结构化数据集
    matlabload("unstructured_charge_example.mat"); # 从CHARGE仿真获取数据。数据可以来自不同来源
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.elements;
    data = unstructureddataset("test",x,y,z,C);
    V_cathode = charge.V_cathode;
    V_anode = charge.V_anode;
    n = pinch(charge.n);
    p = pinch(charge.p);
    data.addparameter("V_cathode",V_cathode);
    data.addparameter("V_anode",V_anode);
    data.addattribute("n",n);
    data.addattribute("p",p);
    visualize(data);

下一个示例创建一个名为"Absorption"的非结构化数据集，包含2个数据属性：功率吸收Pabs和折射率n。两个属性都是空间参数x/y/z和频率f的函数。还指定了连通性矩阵cm。为了允许用户以频率或波长形式访问频率参数，频率（f）和波长（c/f）都被添加为相互依赖的参数。


    Absorption = unstructureddataset("Absorption",x,y,z,cm);
    Absorption.addparameter("lambda",c/f,"f",f);
    Absorption.addattribute("Pabs",Pabs);
    Absorption.addattribute("refractive index",n);
    visualize(Absorption); # 在可视化工具中可视化此数据集

此示例展示如何在平面z=0中定义一个等边三角形


    x = [0;1;2];
    y = [0;sqrt(3);0];
    z = [0;0;0];
    C = [1,3,2];
    ds = unstructureddataset(x,y,z,C);

**参见**

[rectilineardataset](./rectilineardataset.md), [addattribute](./addattribute.md), [addparameter](./addparameter.md), [visualize](./visualize.md), [datasets](./datasets.md), [getparameter](./getparameter.md), [getattribute](./getattribute.md), [matrixdataset](./matrixdataset.md), [struct](./struct.md)
