<!--
Translation from English documentation
Original command: h5read
Translation date: 2026-02-03
-->

# h5read

从 HDF5 文件中读取数据。该命令支持多种数据集类型，如整数、浮点数、双精度数、字符串、复合类型等。

**语法** |  **描述**
---|---
data = h5read("filename", "dataset_name");  |  读取名为 "filename" 的 HDF5 文件中名为 "dataset_name" 的数据集内的数据。

**参数** |  **类型** |  **描述**
---|---|---
filename  |  string  |  HDF5 文件的名称。
datasetname  |  string  |  要读取的数据集的名称（路径）。

**示例**

    filename = "samplefile.h5";
    info = h5info(filename);
    dataset_name = info.Group{1}.Datasets{1}.Name;  # 返回第一个组中第一个数据集的名称（路径）
    data = h5read(filename,dataset_name);

**相关命令**

- [h5info](./h5info.md)
- [h5readattr](./h5readattr.md)
- [Reading HDF5 files](./Reading-HDF5-files.md)
