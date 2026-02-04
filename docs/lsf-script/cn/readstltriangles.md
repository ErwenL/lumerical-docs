<!--
Translation from English documentation
Original command: readstltriangles
Translation date: 2026-02-03
-->

# readstltriangles

从 STL 文件导入顶点位置矩阵。

**语法** | **描述**
---|---
out=readstltriangles("filename.stl",scaling_factor); | 返回一个 Mx3 矩阵，包含指定 STL 文件中所有 STL 三角形的顶点。scaling_factor：STL 文件不包含单位数据。要以微米为单位导入数据，将此值设置为 1e-6。对于纳米单位，设置为 1e-9。

**示例**

以下脚本命令将读取名为 "sample_file.stl" 的 STL 文件，并假设单位为微米保存顶点位置。

```lsf
vtx = readstltriangles("sample_file.stl",1e-6);
```

**另请参见**

- [命令列表](./command_list.md)
- [stlimport](./stlimport.md)
