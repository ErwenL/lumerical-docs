<!--
Translation from English documentation
Original command: importbinary2
Translation date: 2026-02-04 22:50:00
-->

# importbinary2

Import binary 数据 (1s 和 0s) over 一个 entire volume 从 脚本 variables. The 对象 将 为 present wherever 该 binary 数据 是 1 和 not 当 it 是 0. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. 示例 脚本 files showing 如何 到 use 这些 functions 可以 为 found 在 该 Online Help. See 该 User Guide, Structures section.

**语法** |  **描述**  
---|---  
out = importbinary2(binary,x,y,z); |  Import binary 数据 从 脚本 variables 在 three dimensional simulations. All 参数 是 required.  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
binary |  required |  矩阵 |  The binary 数据 This 应该 为 一个 NxMxP 矩阵 在 three dimensions 和 一个 NxM 矩阵 在 two dimensions. It 应该 have only 值 的 0 或 1. If other 值 是 present, all non-zero 值 将 为 interpreted as 1.  
x |  required |  矩阵 |  If n 是 一个 NxMxP 矩阵, 那么 x 应该 have 维度 Nx1. For two dimensional 仿真, 如果 n 是 一个 NxM 矩阵 那么 x 应该 have 维度 Nx1. Values 的 x 必须 为 uniformly spaced.  
y |  required |  矩阵 |  If n 是 一个 NxMxP 矩阵, 那么 y 应该 have 维度 Mx1. For two dimensional 仿真, 如果 n 是 一个 NxM 矩阵 那么 y 应该 have 维度 Mx1. Values 的 y 必须 为 uniformly spaced.  
z |  1 |  数字 |  If n 是 一个 NxMxP 矩阵, 那么 z 应该 have 维度 Px1. Values 的 z 必须 为 uniformly spaced.  
注意: Imported binary 对象 boundaries The boundary 的 该 import binary 对象 是 positioned between 该 vertices 其中 该 材料 是 present 和 该 vertices 其中 该 材料 是 not present. The shape 的 此 implied boundary 可以 为 complex, 和 该 viewport does not show 该 full detail. The boundary 可以 为 moved closer 到 vertices 其中 该 材料 是 present 通过 increasing 该 "binary threshold" 属性 的 该 import 对象. To confirm 该 boundary 该 将 为 used 在 该 仿真 通过 该 求解器, use 一个 index 监视器.  
---  
  
**示例**

Please refer 到 该 [importing spatial binary example](/hc/en-us/articles/360034382754-Import-对象-Binary-spatial-数据) 用于 details.

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importbinary](/hc/en-us/articles/360034408734-importbinary)
