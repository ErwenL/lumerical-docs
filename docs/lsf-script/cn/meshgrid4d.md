# meshgrid4d

在任意方向创建 4D 网格。

**语法** | **描述**
---|---
out = meshgrid4d(dim, x1, x2, x3, x4); | 4D 网格函数。dim 指定创建网格的维度，x1、x2、x3、x4 是每个方向的位置向量。

**示例**

从一组位置向量创建 4D 频率向量。

```
x=linspace(-10,10,20);
y=linspace(-10,10,21);
z=linspace(-10,10,22);
f=linspace(0,100,23);
F=meshgrid4d(4,x,y,z,f); # 在第 4 维（频率）创建网格
?size(F);          # 大小应等于每个位置向量的大小
result:
20 21 22 23
```

**另请参阅**

- [命令列表](./命令列表.md)
- [meshgridx](./meshgridx.md)
- [meshgridy](./meshgridy.md)
- [meshgrid3dy](./meshgrid3dy.md)
- [meshgrid3dz](./meshgrid3dz.md)
