<!--
Translation from English documentation
Original command: importbinary
Translation date: 2026-02-04 22:50:00
-->

# importbinary

Import binary 数据 (1s 和 0s) over 一个 entire volume 从 一个 文件. The 对象 将 为 present wherever 该 binary 数据 是 1 和 not 当 it 是 0. This 命令 only applies 到 import primitives. The 函数 返回 1 如果 该 数据 是 successfully imported. 示例 脚本 files showing 如何 到 use 这些 functions 可以 为 found 在 该 Online Help. See 该 User Guide, Structures section.

**语法** |  **描述**  
---|---  
out = importbinary(文件名,file_units,x0,y0,z0,reverse_index_order); |  Import binary 数据 从 文件名 在 three dimensional simulations. All 参数 after 该 文件名 是 optional.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
文件名 |  required |  字符串 |  name 的 该 文件 使用 binary 数据 到 import. May contain complete path 到 文件, 或 path relative 到 current working directory  
file_units |  "m" |  字符串 |  The optional 字符串 参数 file_units 可以 为 "m", "cm, "mm", "微米" 或 "nm" 到 specify 该 units 在 该 文件.  
x0 |  0 |  数字 |  The optional 参数 x0, y0 和 z0 specify 该 数据 origin 在 该 global coordinates 的 该 Graphical Layout Editor. For example, 如果 you defined your volume 使用 respect 到 一个 particular point 在 space, 用于 example (0,0,-5) 微米, 那么 you 应该 设置 z0 到 -5 微米.  
y0 |  0 |  数字 |   
z0 |  0 |  数字 |   
reverse_index_order |  0 |  数字 |  The optional 参数 reverse_index_order 可以 为 设置 到 1 到 reverse 如何 该 indices 是 interpreted 在 该 文件. It 是 best 到 verify 该 correct setting 使用 一个 graphical import before 使用 该 脚本 命令.  
  
注意: Imported binary 对象 boundaries The boundary 的 该 import binary 对象 是 positioned between 该 vertices 其中 该 材料 是 present 和 该 vertices 其中 该 材料 是 not present. The shape 的 此 implied boundary 可以 为 complex, 和 该 viewport does not show 该 full detail. The boundary 可以 为 moved closer 到 vertices 其中 该 材料 是 present 通过 increasing 该 "binary threshold" 属性 的 该 import 对象. To confirm 该 boundary 该 将 为 used 在 该 仿真 通过 该 求解器, use 一个 index 监视器.  
---  
  
**示例**

Please refer 到 该 [importing spatial binary example](/hc/en-us/articles/360034382754-Import-对象-Binary-spatial-数据) 用于 details.

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importbinary2](/hc/en-us/articles/360034929013-importbinary2)
