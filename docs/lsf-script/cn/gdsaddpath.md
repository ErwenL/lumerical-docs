# gdsaddpath

此函数添加具有固定宽度的分段线路径。它支持带方形角样式的选项。

**语法** | **描述**
---|---
gdsaddpath(fileHandle, layer_datatype, width, vertices); | 添加具有固定宽度的分段线路径。

**参数** | **类型** | **描述**
---|---|---
fileHandle | 字符串 | 之前用 gdsopen 打开的文件句柄。
layer_datatype | 整数 | layer_datatype 与其他 gdsadd 命令相同，可以是整数层，也可以是整数层:整数数据类型，编码为字符串 'x:y'。
width | 数字 | width 是一个浮点数。
vertices | 矩阵 | 浮点坐标的 2 列矩阵。

## 示例

这显示了一个通过脚本代码将路径和文本导出为 GDSII 格式的示例

```powershell
f=gdsopen("path_text.gds", 1e-3, 1e-9);
gdsbegincell(f, 'example');
gdsaddpath(f, 1, 0.5e-6, [-1, 0; 1, 0]*1e-6);
gdsaddpath(f, '1:10', 0.5e-6, [-0.9, 0; -1.1, 0]*1e-6);
gdsaddpath(f, '1:10', 0.5e-6, [0.9, 0; 1.1, 0]*1e-6);
gdsaddtext(f, 10, -1e-6, 0, 'this is a pin');
gdsendcell(f);
gdsclose(f);
```

**另请参阅**

[gdsopen](./gdsopen.md)、[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)