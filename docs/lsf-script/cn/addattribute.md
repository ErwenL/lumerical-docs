<!--
Translation 从 English documentation
Original 命令: addattribute
Translation date: 2026-02-04 23:28:27
-->

# addattribute

添加 一个 attribute 到 一个 existing dataset。

**语法** | **描述**
---|---
R.addattribute("a_name"， 一个); | 添加 该 scalar attribute 一个 到 该 dataset R。 See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) 用于 details about 该 required dimensions 的 attribute 数据。
R.addattribute("a_vector"， a_1, a_2, a_3); | 添加 该 向量 attribute a_vector 到 该 existing dataset R。 The components 的 该 向量 是 a_1, a_2 和 a_3. See [ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) 用于 details about 该 required dimensions 的 attribute 数据。
R.addattribute("a_name"， [数据]， "类型"); | 添加 该 attribute "a_name" 到 该 unstructured dataset R。 [数据] 可以 为 在 one 的 该 forms below: vertex_scalar_attribute[npts; npar_1; npar_2; ...1] vertex_vector_attribute[npts; npar_1; npar_2; ...3] cell_scalar_attribute[ncells; 1] cell_vector_attribute[ncells; 3] (npts 是 该 数字 的 vertices， 该 长度 的 geometric 参数 'x'， 'y'， 'z' cells 是 该 数字 的 elements， equal 到 数字 的 rows 的 geometry 参数 'elements' ) The "类型" 参数 是 一个 optional 字符串 到 specify attribute 类型 和 可以 take 值 的 "vertex" 或 "单元格"。 If not provided， 该 函数 将 guess 该 attribute 类型 based 在 该 shape 的 [数据] 参数。

**示例**

This example uses 一个 矩阵 dataset 到 store cross section (sigma) 数据 as 一个 函数 的 频率。 In 此 case， 该 cross section 数据 sigma 是 该 attribute， 和 频率 是 该 参数。 To allow 该 用户 到 access 该 频率 参数 在 terms 的 频率 或 波长 ， both 频率 (f) 和 波长 (c/f) 是 added as interdependent 参数。


    sigma = matrixdataset("cross_section");
    sigma.addparameter("lambda",c/f,"f",f); # 添加 参数 f and lambda
    sigma.addattribute("sigma",CS); # 添加 attribute CS
    visualize(sigma); # visualize this dataset in the Visualizer

Alternatively， one 可以 also 创建一个 向量 rectilinear dataset (使用 该 name E)。


    E = rectilineardataset("E",x,y,z);
    E.addparameter("f",f);
    E.addattribute("E",Ex,Ey,Ez); # 添加 a 向量 E with the components Ex, Ey and Ez
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
