# matrixdataset

创建空的矩阵数据集。矩阵数据集用于没有空间依赖性的数据（属性和参数）（即反射 vs 频率）。对于具有 x/y/z 空间坐标的数据集（即电场），请使用 rectilineardataset 或 unstructureddataset。

矩阵数据集可以参数化，并且可以包含任意数量的属性（参阅 addattribute）和参数（参阅 addparameter）。

有关更多信息，请参阅数据集介绍。

**语法** | **描述**
---|---
matrixdataset; | 创建空数据集。
matrixdataset("name"); | 创建名为 "name" 的空数据集。

**示例**

此示例使用矩阵数据集存储作为频率函数的横截面积（sigma）数据。在这种情况下，横截面积数据 sigma 是属性，频率是参数。为了允许用户通过频率或波长访问频率参数，频率（f）和波长（c/f）都被添加为相互依赖的参数。

```
sigma = matrixdataset("cross_section");
sigma.addparameter("lambda",c/f,"f",f); # 添加参数 f 和 lambda
sigma.addattribute("sigma",CS); # 添加属性 CS
visualize(sigma); # 在可视化器中可视化此数据集
```

以下脚本代码生成一些示例数据，然后创建 R(radius,height) 数据集。

```
# 创建示例结果
radius = 0:10;
height = 1:0.1:3;
reflection = randmatrix(length(radius),length(height));
# 创建反射数据集
R = matrixdataset("R"); # 初始化数据集
R.addparameter("radius",radius); # 添加半径参数
R.addparameter("height",height); # 添加高度参数
R.addattribute("R",reflection); # 添加反射属性
# 绘制数据
image(radius,height,reflection); # 使用原始矩阵
image(R.radius,R.height,R.R);  # 使用数据集
# 发送数据集到可视化器
visualize(R);
```

**另请参阅**

- [rectilineardataset](./rectilineardataset.md)
- [addattribute](./addattribute.md)
- [addparameter](./addparameter.md)
- [visualize](./visualize.md)
- [datasets](./datasets.md)
- [getparameter](./getparameter.md)
- [getattribute](./getattribute.md)
- [matrixdataset](./matrixdataset.md)
- [struct](./struct.md)
