<!--
Translation from English documentation
Original command: importsurface2
Translation date: 2026-02-04 22:50:00
-->

# importsurface2

Imports surface 数据 从 脚本 variables. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. 示例 脚本 files showing 如何 到 use 这些 functions 可以 为 found 在 该 Online Help. See 该 User Guide, Structures section.

**语法** |  **描述**  
---|---  
out = importsurface2(Z,x,y,upper_surface); |  Import 一个 surface 从 该 variables Z, x 和 y 在 three dimensional simulations. The upper_surface 参数 是 optional.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
Z |  required |  矩阵 |  The two dimensional 矩阵 该 defines 该 surface.  
x |  required |  矩阵 |  If Z 是 一个 NxM 矩阵, 那么 x 应该 have 维度 Nx1. For two dimensional 仿真, 如果 Y 是 一个 Nx1 矩阵 那么 x 应该 have 维度 Nx1.  
y |  required |  矩阵 |  If Z 是 一个 NxM 矩阵, 那么 y 应该 have 维度 Mx1.  
upper_surface |  1 |  数字 |  This optional 参数 应该 为 1 到 import 该 upper surface 和 0 到 import 该 lower surface.  
  
**示例**

please refer 一个 complete example: [Import 对象 - Surfaces](/hc/en-us/articles/360034901973)

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importsurface](/hc/en-us/articles/360034408654-importsurface)
