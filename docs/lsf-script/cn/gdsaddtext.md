# gdsaddtext

此函数在指定位置向 gds 文件添加文本符号。这通常只在注释层上完成。它支持在顶点位置添加文本。

**语法** | **描述**
---
gdsaddtext(fileHandle, layer, x, y, text); | 在 gds 文件的指定位置添加文本符号。

**参数** | **类型** | **描述**
---|---|---
fileHandle | 字符串 | 之前用 gdsopen 打开的文件句柄
layer | 整数 | 层必须是整数
x,y | 数字 | x, y 是放置文本的浮点坐标（文本框的左下角）
text | 字符串 | text 是构成注释主体的 ASCII 字符串

## 示例

脚本代码示例可在 [gdsaddpath](./gdsaddpath.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddstencil](./gdsaddstencil.md)