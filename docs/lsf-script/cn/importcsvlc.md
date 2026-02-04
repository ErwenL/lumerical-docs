<!--
Translation from English documentation
Original command: importcsvlc
Translation date: 2026-02-03
-->

# importcsvlc

此命令添加 LC 网格属性或分析组，其中包含从指定 csv（逗号分隔值）文件导入数据的液晶结构和 LC 网格属性，而无需使用 GUI 导入向导。参数允许您做出与 GUI 中相同的选项选择有关 GUI 导入向导的更多信息，请参阅从 CSV 导入液晶对象。

**语法** |  **描述**
---|---
importcsvlc(filename); |  从指定的文件名导入 csv 文件。文件名后的所有参数都是可选的。
out = importcsvlc(filename,option); |  导入 csv 文件，但指定是作为单个网格属性导入还是添加到分析组 LC 结构中。
out = importcsvlc(filename,option,exported_from_xz_plane); |  导入 csv 文件并指定是否最初从 x-z 平面导出。此选项仅适用于 2D 数据集，但在导入到 x-y 平面的 FDTD 中时对于正确获取 LC 结构的方向至关重要。
out = importcsvlc(filename,option,exported_from_xz_plane,rotations); |  导入 csv 文件并带有附加轴旋转。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
filename  |  必填  |  string  |  要导入的 csv 文件的名称。可以包含文件的完整路径，或相对于当前工作目录的路径。
option  |  true  |  boolean  |  当设置为 1（true）时，导入将创建一个包含网格属性和矩形的分析组结构，与使用图形导入时相同。当设置为 0（false）时，它将仅导入网格属性。此参数是可选的。
exported_from_xz_plane  |  true  |  boolean  |  仅适用于 2D 数据集。这表示数据最初是从 x-z 平面导出的，在导入到 x-y 平面时应考虑这一点。
rotations  |  [0,0,0]  |  matrix  |  可选参数允许您指定围绕 x、y 和 z 轴的 3 个旋转，使用方式与图形导入向导完全相同。矩阵必须有 3 个元素，每个值将四舍五入到最近的 90 度。

**示例**

以下脚本命令将从文件 "myfile.csv" 导入网格属性到 LC 分析组，并围绕 x 轴旋转 90 度。

    importcsvlc("myfile.csv",true,true,[90,0,0]);

有关从脚本创建 LC 网格属性的更多示例，请参阅此知识库页面：LC 旋转。

**相关命令**

- [addgridattribute](./addgridattribute.md)
- [cleardataset](./cleardataset.md)
- [importdataset](./importdataset.md)
