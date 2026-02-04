# gdsclose

此函数关闭要写入的 GDSII 文件。在调用此命令之前，必须先打开 .gds 文件，请参阅 [gdsopen](./gdsopen.md)。

**语法** | **描述**
---
gdsclose("filename") | 关闭当前工作目录中的 .gds 文件。

**参数** | **类型** | **描述**
---|---|---
filename | 字符串 | 要导出的 GDSII 文件名，也可以包含文件路径。

## 示例

脚本代码示例可在 [gdsopen](./gdsopen.md) 页面上找到。

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsaddref](./gdsaddref.md)、[gdsimport](./gdsimport.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)