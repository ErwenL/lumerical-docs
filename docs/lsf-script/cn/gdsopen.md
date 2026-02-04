# gdsopen

此函数创建一个新的 .gds 文件并返回一个文件句柄，可与其他 GdsWriter 函数一起使用来写入文件。默认数据库单位为 0.1nm，用户单位为微米。GDSII 导出函数作为一组命令工作，如下所示作为示例。更多信息，请参阅 [GDSII - 导入和导出](../GDSII-Import-and-export-GDSII.md)。所有 gds 命令都会检查 coordinates/dataBaseUnit 的比率是否不大于 \\( 2^{31} \\)。

**语法** | **描述**
---
f = gdsopen("filename", "userUnit", "dataBaseUnit") | 在当前目录中打开 .gds 文件，指定用户单位的大小和 GDSII 文件单位的大小。f 是用于打开 GDSII 文件的文件句柄。

**参数** | **类型** | **描述**
---|---|---
filename | 字符串 | 要导出的 GDSII 文件名，也可以包含文件路径。
userUnit | 数字 | GDSII 文件单位中的用户单位大小。
databaseUnit | 数字 | GDSII 文件单位以米为单位的大小。

## 示例

这显示了一个通过脚本代码将一些简单结构导出为 GDSII 格式的示例

```powershell
f=gdsopen('GDS_export.gds');
# 创建 .gds 文件以写入代码。如果文件存在，将被覆盖。
gdsbegincell(f,'cell_1');# 创建名为 "cell_1" 的单元
gdsaddcircle(f, 5, 0, 0, 1.5e-6);# 添加一个圆
gdsendcell(f);# 完成 "cell_1"
gdsbegincell(f,'cell_2');# 创建另一个单元
gdsaddpoly(f, 5, [0,0; 1.5,0; 1.2,1.3]*1e-6);# 添加一个多边形
gdsaddcircle(f, 5, -3e-6, -3e-6, 1.5e-6);# 添加一个圆
gdsaddrect(f, 5, -3e-6, 3e-6, 1e-6, 2e-6);# 添加一个矩形
gdsaddref(f, 'cell_1', 3e-6, -3e-6);
# 从 "cell_1" 引用结构
gdsendcell(f);# 完成当前单元
gdsclose(f);# 关闭当前的 .gds 文件
gdsimport('GDS_export.gds','cell_1', 5);
# 在布局环境中显示导出的设计
```

脚本代码示例可在网页上找到。

**另请参阅**

[gdsclose](./gdsclose.md)、[gdsbegincell](./gdsbegincell.md)、[gdsendcell](./gdsendcell.md)、[gdsaddpoly](./gdsaddpoly.md)、[gdsaddcircle](./gdsaddcircle.md)、[gdsaddrect](./gdsaddrect.md)、[gdsimport](./gdsimport.md)、[gdsaddref](./gdsaddref.md)、[gdsaddpath](./gdsaddpath.md)、[gdsaddtext](./gdsaddtext.md)、[gdsaddstencil](./gdsaddstencil.md)