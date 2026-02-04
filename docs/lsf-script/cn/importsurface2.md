<!--
Translation from English documentation
Original command: importsurface2
Translation date: 2026-02-03
-->

# importsurface2

从脚本变量导入表面数据。此命令仅适用于导入图元。如果数据成功导入，函数返回 1。在线帮助中可以找到显示如何使用这些函数的示例脚本文件。请参见用户指南的结构部分。

**语法** |  **描述**
---|---
out = importsurface2(Z,x,y,upper_surface); |  在三维模拟中从变量 Z、x 和 y 导入曲面。upper_surface 参数是可选的。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
Z  |  必填  |  matrix  |  定义曲面的二维矩阵。
x  |  必填  |  matrix  |  如果 Z 是 NxM 矩阵，则 x 的维度应为 Nx1。对于二维模拟，如果 Y 是 Nx1 矩阵，则 x 的维度应为 Nx1。
y  |  必填  |  matrix  |  如果 Z 是 NxM 矩阵，则 y 的维度应为 Mx1。
upper_surface  |  1  |  number  |  此可选参数应为 1 以导入上表面，0 以导入下表面。

**示例**

请参阅完整示例：导入对象 - 曲面

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importsurface](./importsurface.md)
