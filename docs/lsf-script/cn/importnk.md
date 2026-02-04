<!--
Translation from English documentation
Original command: importnk
Translation date: 2026-02-04 22:50:00
-->

# importnk

Imports 该 refractive index (n 和 k) over 一个 entire volume 或 surface 从 一个 文件. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. It 是 possible 到 import anisotropic nk 数据.

**语法** |  **描述**  
---|---  
out = importnk(文件名,file_units, x0,y0,z0,reverse_index_order); |  Import n (和 k) 数据 从 文件名 在 three dimensional (或 two dimensional) simulations. All 参数 after 该 文件名 是 optional.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
文件名 |  required |  字符串 |  name 的 该 文件 使用 n (和 k) 数据 到 import. May contain complete path 到 文件, 或 path relative 到 current working directory  
file_units |  "m" |  字符串 |  The optional 字符串 参数 file_units 可以 为 "m", "cm, "mm", "微米" 或 "nm" 到 specify 该 units 在 该 文件.  
x0 |  0 |  数字 |  The optional 参数 x0, y0 和 z0 specify 该 数据 origin 在 该 global coordinates 的 该 Graphical Layout Editor. For example, you 可以 define your volume 使用 respect 到 一个 particular point 在 space, 用于 example (0,0,-5) 微米.  
y0 |  0 |  数字 |   
z0 |  0 |  数字 |   
reverse_index_order |  0 |  数字 |  The optional 参数 reverse_index_order 可以 为 设置 到 1 到 reverse 如何 该 indices 是 interpreted 在 该 文件. It 是 best 到 verify 该 correct setting 使用 一个 graphical import before 使用 该 脚本 命令.  
  
**示例**

See 该 [Import 对象 - Spatial (n,k) 数据](/hc/en-us/articles/360034901993-Import-对象-Spatial-n-k-数据) example 用于 文件 format.

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importnk2](/hc/en-us/articles/360034408694-importnk2)
