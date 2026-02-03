<!--
Translation from English documentation
Original command: addattribute
Translation date: 2026-02-03
-->

# addattribute

向现有数据集添加属性。

**Syntax** | **Description**
---|---
R.addattribute("a_name", a); | 向数据集R添加标量属性a。有关属性数据所需维度的详细信息，请参见[数据集介绍](/hc/en-us/articles/360034409554-Datasets)。
R.addattribute("a_vector", a_1, a_2, a_3); | 向现有数据集R添加向量属性a_vector。向量的分量为a_1、a_2和a_3。有关属性数据所需维度的详细信息，请参见[数据集介绍](/hc/en-us/articles/360034409554-Datasets)。
R.addattribute("a_name", [data], "type"); | 向非结构化数据集R添加属性"a_name"。[data]可以是以下形式之一：vertex_scalar_attribute[npts; npar_1; npar_2; ...1] vertex_vector_attribute[npts; npar_1; npar_2; ...3] cell_scalar_attribute[ncells; 1] cell_vector_attribute[ncells; 3]（npts是顶点数，几何参数'x'、'y'、'z'的长度；cells是元素数，等于几何参数'elements'的行数）。"type"参数是可选的字符串，用于指定属性类型，可以取"vertex"或"cell"值。如果未提供，函数将根据[data]参数的形状猜测属性类型。

**Examples**

此示例使用矩阵数据集将截面（sigma）数据存储为频率的函数。在这种情况下，截面数据sigma是属性，频率是参数。为了允许用户以频率或波长访问频率参数，频率（f）和波长（c/f）都作为相互依赖的参数添加。

    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # add parameter f and lambda
    sigma.addattribute("sigma",CS); # add attribute CS
    visualize(sigma); # visualize this dataset in the Visualizer

或者，也可以创建向量矩形数据集（名称为E）。

    E = rectilineardataset("E",x,y,z);
    E.addparameter("f",f);
    E.addattribute("E",Ex,Ey,Ez); # add a vector E with the components Ex, Ey and Ez
    visualize(E); # visualize this dataset in the Visualizer

**参见**

- [rectilineardataset](./rectilineardataset.md)
- [addattribute](./addattribute.md)
- [addparameter](./addparameter.md)
- [visualize](./visualize.md)
- [datasets](/hc/en-us/articles/360034409554-Datasets)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [matrixdataset](./matrixdataset.md)