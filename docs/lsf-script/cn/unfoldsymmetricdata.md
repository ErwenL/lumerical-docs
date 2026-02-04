<!-- Translation: unfoldsymmetricdata -->
<!-- Date: 2026-02-03 -->
<!-- Original: unfoldsymmetricdata -->

# unfoldsymmetricdata

根据给定的对称平面对称数据集进行数据展开。该函数可用于从仅包含一半仿真数据的对称仿真中获取完整形式的数据。此命令仅支持非结构化数据集。

**语法** | **说明**
---|---
unfoldsymmetricdata(dataset,'symmetry_plane'); | 根据给定的对称平面对称数据集进行数据展开。第一个参数是2D或3D非结构化数据集。第二个参数是对称数据的对称平面，格式为[+-][xyz]，例如"-y"，指的是对称平面的轴（即作为对称平面的仿真区域的一侧）。

**示例**

下面是一个简单的示例，通过对称于"+y"平面的假设，展开从[unstructured_charge_example.mat](https://lumerical.zendesk.com/hc/article_attachments/360046127893/unstructured_charge_example.mat)文件中获取的数据生成的非结构化数据集。


    matlabload("unstructured_charge_example.mat");
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.elements;
    data = unstructureddataset("test",x,y,z,C);
    data_unfolded=unfoldsymmetricdata(data,'+y');

**参见**

[arrayperiodicdata](./arrayperiodicdata.md), [unstructureddataset](./unstructureddataset.md), [rectilineardataset](./rectilineardataset.md), [addattribute](./addattribute.md), [addparameter](./addparameter.md), [visualize](./visualize.md), [datasets](./datasets.md), [getparameter](./getparameter.md), [getattribute](./getattribute.md), [matrixdataset](./matrixdataset.md), [struct](./struct.md)
