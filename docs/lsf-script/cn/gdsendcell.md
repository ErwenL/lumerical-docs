# gdsendcell

此函数完成 GDSII 文件中的单元。此函数结束 GDSII 文件流中的当前单元。关闭单元之前必须调用 gdsbegincell 命令。

**语法** | **描述**
---
gdsendcell(f) | 完成 GDSII 文件中先前创建的单元。

**参数** | **类型** | **描述**
---|---|---
f | 字符串 | 之前用 gdsopen 打开的文件句柄。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddref](./gdsaddref.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)