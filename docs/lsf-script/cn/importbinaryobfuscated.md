<!--
Translation from English documentation
Original command: importbinaryobfuscated
Translation date: 2026-02-04 22:50:00
-->

# importbinaryobfuscated

This 命令 是 identical 到 importbinary but makes it possible 到 import 数据 从 一个 文件 该 has been obfuscated. For details 在 如何 到 obfuscate 该 数据 files, please see 该 Online Help 在 该 User Guide, Structures section.

**语法** |  **描述**  
---|---  
out = importbinaryobfuscated(key,文件名,file_units,x0,y0,z0,reverse_index_order); |  Import binary 数据 从 文件名 在 three dimensional simulations. All 参数 after 该 文件名 是 optional.  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
key |  required |  字符串 |  The key 该 是 used 到 decrypt 该 obfuscated 文件.  
文件名 |  required |  字符串 |  name 的 该 文件 使用 binary 数据 到 import. May contain complete path 到 文件, 或 path relative 到 current working directory  
file_units |  "m" |  字符串 |  The optional 字符串 参数 file_units 可以 为 "m", "cm, "mm", "微米" 或 "nm" 到 specify 该 units 在 该 文件.  
x0 |  0 |  数字 |  The optional 参数 x0, y0 和 z0 specify 该 数据 origin 在 该 global coordinates 的 该 Graphical Layout Editor. For example, 如果 you defined your volume 使用 respect 到 一个 particular point 在 space, 用于 example (0,0,-5) 微米, 那么 you 应该 设置 z0 到 -5 微米.  
y0 |  0 |  数字 |   
z0 |  0 |  数字 |   
reverse_index_order |  0 |  数字 |  The optional 参数 reverse_index_order 可以 为 设置 到 1 到 reverse 如何 该 indices 是 interpreted 在 该 文件. It 是 best 到 verify 该 correct setting 使用 一个 graphical import before 使用 该 脚本 命令.  
  
**示例**

Please refer 此 example [Obfuscating import 数据](**%20to%20be%20defined%20**).

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [importbinary](/hc/en-us/articles/360034408734-importbinary)
