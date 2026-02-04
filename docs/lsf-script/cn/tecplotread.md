<!-- Translated: 2026-02-03 -->
<!-- Original: tecplotread -->

# tecplotread

从 Tecplot 格式文件（文本）导入数据。

**语法** | **描述**
---| ---
? tecplotread('filename.dat'); | 列出数据文件中的所有区域（域）。
? tecplotread('filename.dat','zonename'); | 列出与该区域相关联的所有数据字段。
out = tecplotread('filename.dat','zonename','dataname'); | 以数组形式检索数据

**示例**

以下示例展示了如何使用 tecplotread 命令将这些文件中的数据导入 CHARGE。特殊字段 "FETriangle" 表示三角剖分，X 和 Y 坐标作为节点数据处理。名称和单位取决于原始数据源，但我们必须将单位转换为 SI（米）。

tecplot_import_diode.lsf 文件的第一部分从 example_diode_tecplot.dat 文件中读取数据。脚本中的以下两行读取 Tecplot 文件中区域的名称以及各区域中可用的数据。

```lsf
filename = 'example_diode_tecplot.dat';
zonename = 'Silicon';
?"Available zones: " + tecplotread(filename);
?"Data in zone " + zonename + ": " + tecplotread(filename,zonename);
```

接下来的几行读取有限元网格的信息。这里 t 是连接矩阵，x、y 是顶点矩阵。注意坐标数据从微米单位转换为米。

```lsf
t = tecplotread(filename,zonename,'FETriangle');
x = 1e-6*tecplotread(filename,zonename,'X [um]'); # convert to SI from um to m
y = 1e-6*tecplotread(filename,zonename,'Y [um]'); # convert to SI, invert
```

以下行读取掺杂数据。

```lsf
NA_name = 'NA [1/cm3]';
ND_name = 'ND [1/cm3]';
NA = 1e6*tecplotread(filename,zonename,NA_name); # convert to SI (cm^-3 -- m^-3)
ND = 1e6*tecplotread(filename,zonename,ND_name); # convert to SI (cm^-3 -- m^-3)
```

读取数据后，代码为掺杂数据创建非结构化数据集并创建几何和导入掺杂对象。导入数据后，可以使用 CHARGE 中的[数据集构建器](./dataset-builder.md)执行相同任务。

**另见**

[system](./system.md)、[matlabload](./matlabload.md)、[h5read](./h5read.md)
