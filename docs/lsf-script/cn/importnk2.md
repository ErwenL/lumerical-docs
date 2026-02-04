<!--
Translation from English documentation
Original command: importnk2
Translation date: 2026-02-04 22:50:00
-->

# importnk2

Imports 该 refractive index (n 和 k) over 一个 entire volume 或 surface 从 脚本 variables. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. It 是 possible 到 import anisotropic nk 数据.

**语法** |  **描述**  
---|---  
out = importnk2(n,x,y,z); |  Import n (和 k) 数据 从 脚本 variables 在 three dimensional simulations, n 可以 为 complex. All 参数 是 required. n 必须 为 的 维度 NxMxP 或 NxMxPx3 使用 N >= 2, M >= 2 和 P >= 2.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
n |  required |  矩阵 |  The refractive index. If it 是 complex-valued, 那么 该 imaginary part 是 interpreted as k. For isotropic 材料, 此 应该 为 一个 NxMxP 矩阵 在 three dimensions 和 一个 NxMx2 矩阵 在 two dimensions. For anisotropic 材料, 此 应该 为 一个 NxMxPx3 矩阵 在 three dimensions 和 一个 NxMx2x3 矩阵 在 two dimensions.  
x |  required |  矩阵 |  If n 是 一个 NxMxP 矩阵, 那么 x 应该 have 维度 Nx1. For two dimensional 仿真, 如果 n 是 一个 NxMx2 矩阵 那么 x 应该 have 维度 Nx1. Values 的 x 必须 为 uniformly spaced.  
y |  required |  矩阵 |  If n 是 一个 NxMxP 矩阵, 那么 y 应该 have 维度 Mx1. For two dimensional 仿真, 如果 n 是 一个 NxMx2 矩阵 那么 y 应该 have 维度 Mx1. Values 的 y 必须 为 uniformly spaced.  
z |  required |  矩阵 |  If n 是 一个 NxMxP 矩阵, 那么 z 应该 have 维度 Px1. For two dimensional 仿真, 如果 n 是 一个 NxMx2 矩阵 那么 z 应该 have 维度 2x1. Values 的 z 必须 为 uniformly spaced.  
  
**示例**

[Import 对象 - Spatial (n,k) 数据](/hc/en-us/articles/360034901993-Import-对象-Spatial-n-k-数据)

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importnk](/hc/en-us/articles/360034408674-importnk)
