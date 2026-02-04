# gdsaddstencil

基于由给定 z 平面与具有特定材料和部分名称的结构的交点形成的切片，向当前 gds 单元添加一个或多个多边形元素。当顶点数超过 8190 时会创建多个多边形。只有在已创建 gds 单元后才能使用此命令，例如使用 [gdsbegincell](./gdsbegincell.md)。

如果材料是 "Object defined dielectric"，则必须提供索引值。

此命令始终忽略禁用的几何体。

**语法** | **描述**
---|---
gdsaddstencil(f, layer, {"material": mat_name, "partialname": partial_name, "z": z, "curve_chord_tol": tol, "dx": dx, "dy": dy }); | 基于 z 平面和结构的交点添加一个或多个多边形元素。参数解释如下。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 [gdsopen](./gdsopen.md) 打开的文件句柄。
layer | 字符串或数字 | 字符串：形式为 "layer:datatype" 的字符串（例如 "6:2"）可用于定义要从导入的 GDSII 文件中该结构的层号和数据类型。层和数据类型是整数。数字：定义层号并将数据类型设置为零。
mat_name | 字符串 | 用于交点的材料名称。该命令仅为此名称的材料创建多边形。
partialname | 字符串 | 用于交点的对象部分名称。该命令仅在对象树中名称包含此字符串的对象创建多边形。
z | 数字 | 创建交点的 z 平面。只接受标量值。
curve_chord_tol | 数字 | 可选，默认为 0。面片边缘与其原始边缘实体之间的最大弦距。
dx | 数字 | 可选，默认为 0。用作 gds 坐标原点的切片内位置。
dy | 数字 | 可选，默认为 0。用作 gds 坐标原点的切片内位置。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddref](./gdsaddref.md)、[polystencil](./polystencil.md)