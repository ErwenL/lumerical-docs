<!--
Translation from English documentation
Original command: importnk2
Translation date: 2026-02-03
-->

# importnk2

从脚本变量导入整个体素或表面的折射率（n 和 k）。此命令仅适用于导入图元。如果数据成功导入，函数返回 1。可以导入各向异性 nk 数据。

**语法** |  **描述**
---|---
out = importnk2(n,x,y,z); |  在三维模拟中从脚本变量导入 n（和 k）数据，n 可以是复数。所有参数都是必填的。n 的维度必须为 NxMxP 或 NxMxPx3，其中 N >= 2，M >= 2，P >= 2。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
n  |  必填  |  matrix  |  折射率。如果是复数值，则虚部被解释为 k。对于各向同性材料，在三维情况下应该是 NxMxP 矩阵，在二维情况下应该是 NxMx2 矩阵。对于各向异性材料，在三维情况下应该是 NxMxPx3 矩阵，在二维情况下应该是 NxMx2x3 矩阵。
x  |  必填  |  matrix  |  如果 n 是 NxMxP 矩阵，则 x 的维度应为 Nx1。对于二维模拟，如果 n 是 NxMx2 矩阵，则 x 的维度应为 Nx1。x 的值必须均匀分布。
y  |  必填  |  matrix  |  如果 n 是 NxMxP 矩阵，则 y 的维度应为 Mx1。对于二维模拟，如果 n 是 NxMx2 矩阵，则 y 的维度应为 Mx1。y 的值必须均匀分布。
z  |  必填  |  matrix  |  如果 n 是 NxMxP 矩阵，则 z 的维度应为 Px1。对于二维模拟，如果 n 是 NxMx2 矩阵，则 z 的维度应为 2x1。z 的值必须均匀分布。

**示例**

导入对象 - 空间（n,k）数据

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importnk](./importnk.md)
