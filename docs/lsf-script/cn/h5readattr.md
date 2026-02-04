<!--
Translation from English documentation
Original command: h5readattr
Translation date: 2026-02-03
-->

# h5readattr

从 HDF5 文件中读取属性。

**语法** |  **描述**
---|---
attr = h5readattr("filename", "attr_path", "attr_name");  |  读取名为 "filename" 的 HDF5 文件中位置 "attr_path" 处名为 "attr_name" 的属性。

**参数** |  **类型** |  **描述**
---|---|---
filename  |  string  |  HDF5 文件的名称。
attr_path  |  string  |  属性所属的数据集或组的名称（路径）。
attr_name  |  string  |  要读取的属性名称。

**示例**

    filename = "samplefile.h5";
    A = h5info(filename);
    attr_path = A.Groups{1}.Name;
    attr_name = A.Groups{1}.Attributes{1}.Name;
    attr = h5readattr(filename, attr_path, attr_name);

**相关命令**

- [h5info](./h5info.md)
- [h5read](./h5read.md)
- [Reading HDF5 files](./Reading-HDF5-files.md)
