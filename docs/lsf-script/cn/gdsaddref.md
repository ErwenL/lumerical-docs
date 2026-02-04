# gdsaddref

此函数向 GDSII 文件流的当前单元中添加对另一个单元的引用。此函数将引用的单元（必须之前已打开并完成）复制到当前单元，并创建嵌套层次结构。复制结构的层号遵循引用的单元。引用只能添加到 GDSII 单元中，因此只有在已创建当前单元后才能调用此命令，例如使用 [gdsbegincell](./gdsbegincell.md)。此外，被引用的单元必须在其被引用之前存在。

**语法** | **描述**
---|---
gdsaddref(f, "cellname", dx, dy, angle_in_deg) | 向当前单元添加对另一个单元（"cellname"）的引用，并指定 dx 和 dy 的移动。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 gdsopen 打开的文件句柄。
cellname | 字符串 | 被引用单元的名称。
dx | 数字 | 复制单元在当前单元中的 X 移动。
dy | 数字 | 复制单元在当前单元中的 Y 移动。
angle_in_deg | 数字 | 可选，复制单元的旋转角度（度）。对于此操作，**复制**的单元相对于**其自己的**原点旋转，然后将该单元放置在参数 dx 和 dy 指定的坐标处。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)