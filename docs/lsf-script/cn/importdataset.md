<!--
Translation from English documentation
Original command: importdataset
Translation date: 2026-02-03
-->

# importdataset

此命令可用于将规则或不规则数据集导入模拟对象。

**语法** |  **描述**
---|---
importdataset("filename") |  从当前工作目录中的指定 Matlab 文件导入数据集。必须选择要加载数据的对象。
importdataset(charge) |  从脚本工作区中的指定数据集导入数据。数据集可以使用 matlabload 命令从 Matlab 文件加载到脚本工作区。必须选择要加载数据的对象。

此命令可以在以下几种情况下使用

1. 将数据导入网格属性（数据可能来自有限元 IDE 中的电荷监视器或温度监视器）。

2. 将掺杂数据导入选定的"导入掺杂"对象。

3. 将光生数据导入选定的"导入生成"对象。

4. 将场数据导入导入源（FDTD）。

5. 将场数据导入端口对象（FDTD 和 MODE）。

该命令有两种使用方式。数据集可以保存在 matlab（.mat）文件中，可以调用该文件来加载数据；或者，该命令可以直接从脚本工作区调用数据集来加载到模拟对象中。在这两种情况下，数据集都需要具有以下属性：

**数据** |  **模拟对象** |  **数据集类型** |  **定义坐标数据的变量名称** |  **定义实际数据的变量名称**
---|---|---|---|---
液晶取向（3 元素单位向量） |  'lc orientation' 网格属性 |  规则 |  x, y, z |  u
旋转角度（弧度） |  'permittivity rotation' 网格属性 |  规则 |  x, y, z |  theta, phi, psi
酉变换矩阵（3x3 张量） |  'matrix transform' 网格属性 |  规则 |  x, y, z |  U
电荷密度 |  'np density' 网格属性 |  不规则 |  x, y, z, C |  n, p
掺杂分布 |  'Import doping' 对象 |  不规则或矩形 |  x, y, z, C (不规则); x, y, z (矩形) |  N
光生率 |  'Import generation' 对象 |  矩形 |  x, y, z |  G
温度（开尔文） |  'temperature' 网格属性 |  不规则 |  x, y, z, elements（有关更多信息，请参阅数据集构建器） |  N
E 和 H 场数据 |  FDTD 中的导入源 |  规则 |  x, y, z, f (可选)（有关更多信息，请参阅源 - 导入） |  E (必填), H (可选)
E 和 H 场数据 |  MODE EME 求解器中的端口（请注意，每个端口一次只能导入 1 个模式） |  规则 |  x,y,z（有关更多信息，请参阅导入任意源场） |  E, H

**示例**

此示例显示如何将不规则数据集 'charge' 导入到 'np Density' 网格属性。

    select("np density");
    importdataset("device_data.mat");

这也等价于以下方法。

    select("np Density");
    matlabload("device_data.mat");
    importdataset(charge);

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [cleardataset](./cleardataset.md)
- [matlabload](./matlabload.md)
- [Mach Zehnder](./Mach-Zehnder.md)
- [Import/export np Density](./Import-export-np-Density.md)
- [addgridattribute](./addgridattribute.md)
- [unstructureddataset](./unstructureddataset.md)
