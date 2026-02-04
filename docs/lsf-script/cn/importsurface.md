<!--
Translation from English documentation
Original command: importsurface
Translation date: 2026-02-03
-->

# importsurface

导入表面数据。此命令仅适用于导入图元。如果数据成功导入，函数返回 1。在线帮助中可以找到显示如何使用这些函数的示例脚本文件。请参见用户指南的结构部分。

**语法** |  **描述**
---|---
out = importsurface(filename,upper_surface,file_units,x0,y0,z0,invertXY); |  在三维模拟中从字符串 filename 的文件导入曲面。文件名后的所有参数都是可选的。
out = importsurface(filename,upper_surface,file_units,x0,y0,invertXY); |  在二维模拟中从字符串 filename 的文件导入曲面。文件名后的所有参数都是可选的。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
filename  |  必填  |  string  |  要导入的表面数据文件的名称。可以包含文件的完整路径，或相对于当前工作目录的路径。
upper_surface  |  1  |  number  |  此可选参数应为 1 以导入上表面，0 以导入下表面。
file_units  |  "m"  |  string  |  可选的字符串参数 file_units 可以是 "m"、"cm"、"mm"、"microns" 或 "nm"，以指定文件中的单位。
x0  |  0  |  number  |  可选参数 x0、y0 和 z0 指定图形布局编辑器全局坐标中的数据原点。例如，如果您正在导入由 AFM 定义的表面，该 AFM 位于 0 到 2 微米的硅片上，则应将 z0 设置为 2 微米。
y0  |  0  |  number  |
z0  |  0  |  number  |
invertXY  |  0  |  number  |  可选参数 invertXY 可用于反转从文件中读取 x 和 y 轴的方式。

**示例**

请参阅完整示例：导入对象 - 曲面

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importsurface2](./importsurface2.md)
