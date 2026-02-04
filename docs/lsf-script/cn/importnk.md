<!--
Translation from English documentation
Original command: importnk
Translation date: 2026-02-03
-->

# importnk

从文件导入整个体素或表面的折射率（n 和 k）。此命令仅适用于导入图元。如果数据成功导入，函数返回 1。可以导入各向异性 nk 数据。

**语法** |  **描述**
---|---
out = importnk(filename,file_units, x0,y0,z0,reverse_index_order); |  在三维（或二维）模拟中从文件名导入 n（和 k）数据。文件名后的所有参数都是可选的。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
filename  |  必填  |  string  |  要导入的 n（和 k）数据文件的名称。可以包含文件的完整路径，或相对于当前工作目录的路径。
file_units  |  "m"  |  string  |  可选的字符串参数 file_units 可以是 "m"、"cm"、"mm"、"microns" 或 "nm"，以指定文件中的单位。
x0  |  0  |  number  |  可选参数 x0、y0 和 z0 指定图形布局编辑器全局坐标中的数据原点。例如，您可以在空间中相对于特定点（例如 (0,0,-5) 微米）定义您的体素。
y0  |  0  |  number  |
z0  |  0  |  number  |
reverse_index_order  |  0  |  number  |  可选参数 reverse_index_order 可以设置为 1 以反转文件中索引的解释方式。在使用脚本命令之前，最好通过图形导入验证正确的设置。

**示例**

有关文件格式，请参阅导入对象 - 空间（n,k）数据示例。

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importnk2](./importnk2.md)
