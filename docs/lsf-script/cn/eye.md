# eye

创建 2D 单位矩阵。

**语法** | **描述**
---|---
I = eye; | 返回 1x1 矩阵，值为 1.0。
I = eye(n); | 返回 nxn 单位矩阵。
I = eye(n,m); | 返回 nxm 矩阵，主对角线上为 1

**示例**

以下是一些脚本命令使用的示例及其结果。

```powershell
?eye;
result:
1
?eye(3);
result:
1 0 0
0 1 0
0 0 1
?eye(2,3);
result:
1 0 0
0 1 0
?eye(3,2);
result:
1 0
0 1
0 0
```

**另请参阅**

[数据集](./Datasets.md)、[matrixdataset](./matrixdataset.md)、[rectilineardataset](./rectilineardataset.md)、[matlab](./matlab.md)、[matrix](./matrix.md)