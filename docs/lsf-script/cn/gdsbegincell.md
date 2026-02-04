# gdsbegincell

此函数在 GDSII 文件中创建一个单元。所有 GDS 元素（多边形、框、引用、数组引用等）必须放在单元内，因此必须在添加任何元素之前调用此函数。完成添加元素后，可以调用 gdsendcell 来完成单元。单元不能嵌套，因此在调用 gdsbegincell 后，在第一个调用的单元关闭之前不能再次调用新的单元。尽管 GDSII 文件是单元的平面列表，但单元可以引用其他单元，从而创建嵌套层次结构。更多详情请参阅 [gdsaddref](./gdsaddref.md)。GDS "单元" 在导入 FDTD 时作为"结构组"存在，更多详情请参阅 [gdsimport](./gdsimport.md)。

**语法** | **描述**
---
gdsbegincell(f, "cellname") | 在 GDSII 文件中创建一个新单元。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 gdsopen 打开的文件句柄。
cellname | 字符串 | 单元的名称。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

注意：需要澄清的是，GDS 单元与 FDTD 中的 [单元数组](../Cell.md) 不同。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddref](./gdsaddref.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)