<!--
Translation from English documentation
Original command: h5writeattr
Translation date: 2026-02-03
-->

# h5writeattr

将矩阵或字符串作为组或数据集的属性写入 HDF5 文件。

**语法** |  **描述**
---|---
h5writeattr("filename", "location_name", "attribute_name", data); |  根据给定的数据，在名为 "filename" 的 HDF5 文件中为名为 "location_name" 的组或数据集创建一个名为 "attribute_name" 的属性。如果 HDF5 文件 "filename" 不存在，则会创建该文件。如果不存在名为 "location_name" 的组或数据集，将创建一个名为 "location_name" 的新组。如果 HDF5 文件中给定组/数据集内已存在名为 "attribute_name" 的属性，则该属性将被覆盖。否则，属性将添加到 HDF5 文件中现有的组/数据集中。
h5writeattr("filename", "location_name", "attribute_name", data, ["access_mode"]); |  可选参数："append" 或 "overwrite"。"append"：如果属性名为 "attribute_name" 的属性在 HDF5 文件 "filename" 中名为 "location_name" 的组或数据集中尚不存在，则添加该属性。否则，它将被覆盖。如果 HDF5 文件 "filename" 不存在，此命令将创建一个 HDF5 文件。如果不存在名为 "location_name" 的组或数据集，将创建一个名为 "location_name" 的新组。"append" 选项是默认设置。"overwrite"：如果名为 "filename" 的 HDF5 文件已存在，该文件将被完全覆盖。否则，它将被创建。文件将仅包含名为 "location_name" 的组和名为 "attribute_name" 的属性。
h5writeattr("filename", "location_name", "attribute_name", data, [{"datatype": "datatype_name"}]); |  可选参数。此结构体指示数据在 HDF5 文件中存储的数据类型。可能的选项：{"datatype": "short"}：数据存储为短整数 {"datatype": "int"}：数据存储为整数 {"datatype": "long long"}：数据存储为长长整数 {"datatype": "double"}：数据存储为双精度浮点数。此数据结构体不适用于字符串值。在这种情况下，命令将抛出错误。

**参数** |  **类型** |  **描述**
---|---|---
filename |  string |  HDF5 文件的名称。
location_name |  string |  组或数据集的名称。
attribute_name |  string |  属性的名称。
data |  matrix/string |  实数/复数矩阵或字符串。
access_mode |  string |  可选参数。仅字符串 "append" 和 "overwrite" 是有效的选项。
{"datatype": "datatype_name"} |  struct |  可选参数。不适用于字符串值。如果给定，字符串 "datatype" 是结构体中的必填字段。该字段只能是字符串值 "short"、"int"、"long long" 和 "double"。后者是矩阵值的默认数据类型。

**示例**

首先使用默认数据类型，其次使用整数数据类型，将实数矩阵作为属性写入 HDF5 文件中的组。

    a = [1, 2, pi; 4, 5, 2*pi];
    h5writeattr("testfile.h5", "test_group", "double_matrix", a);
    h5writeattr("testfile.h5", "test_group", "int_matrix", a, {"datatype":"int"});

使用 [h5readattr](./h5readattr.md) 读取数据得到以下结果。

    ?h5readattr("testfile.h5", "/test_group", "double_matrix");
    result:
    1  2  3.14159
    4  5  6.28319

    ?h5readattr("testfile.h5", "/test_group", "int_matrix");
    result:
    1  2  3
    4  5  6

通过替换现有数据来覆盖现有的 HDF5 文件，创建一个包含属性 "vector" 的组 "new_group"。

    b = [2, 3, 5, 7, 11, 13];
    h5writeattr("testfile.h5", "new_group", "vector", b, "overwrite");

对 HDF5 文件应用 [h5info](./h5info.md) 和 [h5readattr](./h5readattr.md) 显示只有一个组和一个属性。该属性包含给定的 1D 实数矩阵。

    info = h5info("testfile.h5");
    ?info.Groups;
    Cell array with 1 elements

    info.Groups{1}.Attributes;
    Cell array with 1 elements
    ?h5readattr("testfile.h5", "/new_group", "vector");
    result:
    2  3  5  7  11  13

**相关命令**

- [List of commands](./List-of-commands.md)
- [h5write](./h5write.md)
- [h5info](./h5info.md)
- [h5read](./h5read.md)
- [h5readattr](./h5readattr.md)
- [Reading HDF5 files](./Reading-HDF5-files.md)
