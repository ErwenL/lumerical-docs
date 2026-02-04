<!--
Translation from English documentation
Original command: h5info
Translation date: 2026-02-03 10:57:40
Updated: 2026-02-03
-->

# h5info

返回有关 HDF5 文件结构的信息。

**语法** |  **描述**
---|---
info = h5info("filename");  |  返回一个结构体 "info"，包含名为 "filename" 的 HDF5 文件的结构信息。

**参数** |  **类型** |  **描述**
---|---|---
filename  |  string  |  HDF5 文件的名称。

**示例**

    filename = "samplefile.h5";
    info = h5info(filename);
    ?info;
    > Struct with fields:
    > Attributes
    > Datasets
    > Datatypes
    > FileName
    > Groups
    > Name

包含 HDF5 文件信息的结构体具有以下字段：

**所属** |  **字段** |  **描述**
---|---|---
文件  |  Attributes  |  包含文件属性列表的结构体。
数据集  |  结构体  |  包含文件中数据集列表的结构体。
数据类型  |  结构体  |  包含文件中数据类型列表的结构体。
文件名  |  string  |  包含文件名的字符串。
组  |  结构体  |  包含顶层组列表的结构体。
名称  |  string  |  包含根路径的字符串。该值始终为 "/"。
组  |  Attributes  |  包含组属性列表的结构体。
数据集  |  结构体  |  包含组中数据集列表的结构体。
数据类型  |  结构体  |  包含组中数据类型列表的结构体。
组  |  结构体  |  包含组内子组列表的结构体。
名称  |  string  |  包含组名称（路径）的字符串。
数据集  |  Attributes  |  包含数据集属性列表的结构体。
数据空间  |  结构体  |  包含数据集大小信息的结构体。
数据类型  |  结构体  |  包含数据集类型信息的结构体。
名称  |  string  |  包含数据集名称（路径）的字符串。
属性列表  |  结构体  |  包含数据集各种属性的结构体，如填充值、过滤器等。
数据类型  |  Class  |  包含数据类型 HDF5 类的字符串。
名称  |  string  |  包含数据类型名称的字符串。
大小  |  size  |  以字节为单位的数据类型大小。
类型  |  string  |  描述数据类型类型的字符串。

**相关命令**

- [h5read](./h5read.md)
- [h5readattr](./h5readattr.md)
- [Reading HDF5 files](./Reading-HDF5-files.md)
