# gdsimport

此命令将 .gds 文件中的单元导入到布局环境中。这相当于通过 FILE->IMPORT 菜单执行 GDSII 导入。更多信息请参阅布局编辑器参考指南中的 [GDSII 导入](../GDSII-Import-and-export-GDSII.md)。

**语法** | **描述**
---
n = gdsimport("filename", "cellname", layer); | 将指定文件中指定单元的指定层导入到当前仿真环境中。创建的对象的材料将设置为对象定义电介质。在 3D 中，2D 几何数据将在 Z 维度上被挤压到默认值。可选的返回值 n 是从 gds 文件导入的对象数量。
n = gdsimport("filename", "cellname", layer, "material"); | 与上述命令相同，但导入对象的材料将设置为指定值。
n = gdsimport("filename", "cellname", layer, "material", zmin, zmax); | 此形式的命令仅在 3D 布局中允许。行为与上述命令相同，但结构将在 Z 维度上挤压到指定的 z 最小值和 z 最大值

**参数** | **类型** | **描述**
---|---|---
filename | 字符串 | 要导入的 GDSII 文件名。它可以包含文件的完整路径，或相对于当前工作目录的路径。
cellname | 字符串 | 要从 GDSII 文件导入的单元名称。
layer | 数字或字符串 | 要从 GDSII 文件导入的层号。如果只需要匹配特定数据类型的元素，可以使用形式为 "6:2" 的字符串来指定，其中所需的层为 6，所需的数据类型为 2。
material | 字符串 | 当前布局环境中材料的有效名称。材料的开头部分名称可以匹配。例如，"Al (3" 将匹配 "Al (300nm)"。
zmin | 数字 | 将 2D GDSII 数据挤压到 3D 对象的最小 z 值
zmax | 数字 | 将 2D GDSII 数据挤压到 3D 对象的最大 z 值

## 示例：

此命令从 GDS_export.gds 文件中的第一层导入 "cell_1"，并分配指定的材料、z 最小值和 z 最大值。更多示例，请访问布局编辑器参考指南中的 [GDSII 导入](../GDSII-Import-and-export-GDSII.md)。

```powershell
gdsimport("GDS_export.gds", "cell_1", 1, "Ag (Silver) - CRC", 0, 1e-6);
```

**另请参阅**

[命令列表](../命令列表.md)、[setnamed](./setnamed.md)、[fileexists](./fileexists.md)、[gdsopen](./gdsopen.md)、[gdsaddstencil](./gdsaddstencil.md)