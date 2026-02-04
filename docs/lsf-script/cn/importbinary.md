<!--
Translation from English documentation
Original command: importbinary
Translation date: 2026-02-03
-->

# importbinary

从文件导入整个体素的二进制数据（1 和 0）。对象将存在于二进制数据为 1 的任何地方，在为 0 时则不存在。此命令仅适用于导入图元。如果数据成功导入，函数返回 1。在线帮助中可以找到显示如何使用这些函数的示例脚本文件。请参见用户指南的结构部分。

**语法** |  **描述**
---|---
out = importbinary(filename,file_units,x0,y0,z0,reverse_index_order); |  在三维模拟中从文件名导入二进制数据。文件名后的所有参数都是可选的。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
filename  |  必填  |  string  |  要导入的二进制数据文件的名称。可以包含文件的完整路径，或相对于当前工作目录的路径。
file_units  |  "m"  |  string  |  可选的字符串参数 file_units 可以是 "m"、"cm"、"mm"、"microns" 或 "nm"，以指定文件中的单位。
x0  |  0  |  number  |  可选参数 x0、y0 和 z0 指定图形布局编辑器全局坐标中的数据原点。例如，如果您在空间中相对于特定点（例如 (0,0,-5) 微米）定义了体素，则应将 z0 设置为 -5 微米。
y0  |  0  |  number  |
z0  |  0  |  number  |
reverse_index_order  |  0  |  number  |  可选参数 reverse_index_order 可以设置为 1 以反转文件中索引的解释方式。在使用脚本命令之前，最好通过图形导入验证正确的设置。

注意：导入的二进制对象边界。导入的二进制对象的边界位于存在材料的顶点与不存在材料的顶点之间。此隐含边界的形状可能很复杂，视口不会显示全部细节。可以通过增加导入对象的"二进制阈值"属性将边界移动到更靠近存在材料的顶点。要确认求解器在模拟中使用的边界，请使用折射率监视器。

---

**示例**

有关详细信息，请参阅导入空间二进制示例。

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importbinary2](./importbinary2.md)
