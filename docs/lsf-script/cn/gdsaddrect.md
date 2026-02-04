# gdsaddrect

此函数向 GDSII 文件流中添加矩形元素。这只是一个便捷函数，用于为矩形创建多边形。目前不支持矩形的其他元素类型（如 box）。多边形只能添加到 GDSII 单元中，因此只有在已创建单元后才能调用此命令。

**语法** | **描述**
---|---
gdsaddrect(f, layer, x, y, width, height) | 在具有 x、y 坐标、宽度和高度的层上添加矩形元素。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 gdsopen 打开的文件句柄。
layer | 字符串或数字 | 字符串：形式为 "layer:datatype" 的字符串（例如 "6:2"）可用于定义要从导入的 GDSII 文件中该结构的层号和数据类型。层和数据类型是整数。数字：定义层号并将数据类型设置为零。
x | 数字 | 中心位置的 x 坐标，单位为米。
y | 数字 | 中心位置的 y 坐标，单位为米。
width | 数字 | 矩形的宽度，单位为米。
height | 数字 | 矩形的高度，单位为米。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddref](./gdsaddref.md)、[gdsimport](./gdsimport.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)