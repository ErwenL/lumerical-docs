# gdsaddpoly

此函数向 GDSII 文件流中添加多边形元素。在 GDS 术语中，多边形也称为边界元素。只有在已创建单元后才能调用此命令。由于 GDSII 边界中顶点数量的[限制](https://www.artwork.com/gdsii/max_vertex.htm)，单个多边形可以添加的最大顶点数为 8190。

对于需要更多顶点的复杂几何形状，请使用 [gdsaddstencil](./gdsaddstencil.md)。

**语法** | **描述**
---|---
gdsaddpoly(f, layer, [vertices]) | 在具有顶点的层上添加多边形元素。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 [gdsopen](./gdsopen.md) 打开的文件句柄。
layer | 字符串或数字 | 字符串：形式为 "layer:datatype" 的字符串（例如 "6:2"）可用于定义要从导入的 GDSII 文件中该结构的层号和数据类型。层和数据类型是整数。数字：定义层号并将数据类型设置为零。
vertices | 矩阵 | 多边形的顶点，在 Nx2 矩阵中，其中第一列表示 x，第二列表示 y，例如 [x1,y1; x2,y2;...xn,yn]。值以米为单位。第一个和最后一个值不应该相同，多边形将自动闭合。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddref](./gdsaddref.md)、[gdsimport](./gdsimport.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)