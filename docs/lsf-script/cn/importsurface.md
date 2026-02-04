<!--
Translation from English documentation
Original command: importsurface
Translation date: 2026-02-04 22:50:00
-->

# importsurface

Imports surface 数据. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. 示例 脚本 files showing 如何 到 use 这些 functions 可以 为 found 在 该 Online Help. See 该 User Guide, Structures section.

**语法** |  **描述**  
---|---  
out = importsurface(文件名,upper_surface,file_units,x0,y0,z0,invertXY); |  Import 一个 surface 从 该 文件 在 该 字符串 文件名 在 一个 three dimensional 仿真. All 参数 after 文件名 是 optional.  
out = importsurface(文件名,upper_surface,file_units,x0,y0,invertXY); |  Import 一个 surface 从 该 文件 在 该 字符串 文件名 在 一个 two dimensional 仿真. All 参数 after 文件名 是 optional.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
文件名 |  required |  字符串 |  name 的 该 文件 使用 surface 数据 到 import. May contain complete path 到 文件, 或 path relative 到 current working directory  
upper_surface |  1 |  数字 |  This optional 参数 应该 为 1 到 import 该 upper surface 和 0 到 import 该 lower surface.  
file_units |  "m" |  字符串 |  The optional 字符串 参数 file_units 可以 为 "m", "cm, "mm", "微米" 或 "nm" 到 specify 该 units 在 该 文件.  
x0 |  0 |  数字 |  The optional 参数 x0, y0 和 z0 specify 该 数据 origin 在 该 global coordinates 的 该 Graphical Layout Editor. For example, 如果 you 是 importing 一个 surface defined 通过 一个 AFM 该 是 在 一个 slab 的 Si 该 ranges 从 0 到 2 微米, you 应该 设置 z0 到 2 微米.  
y0 |  0 |  数字 |   
z0 |  0 |  数字 |   
invertXY |  0 |  数字 |  The optional 参数 invertXY 可以 为 used 到 reverse 如何 该 x 和 y axes 是 read 从 该 文件.  
  
**示例**

please refer 一个 complete example: [Import 对象 - Surfaces](/hc/en-us/articles/360034901973)

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importsurface2](/hc/en-us/articles/360034928993-importsurface2)
