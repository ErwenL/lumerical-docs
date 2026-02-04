<!--
Translation from English documentation
Original command: importbinaryobfuscated
Translation date: 2026-02-03
-->

# importbinaryobfuscated

此命令与 importbinary 相同，但可以从已混淆的文件中导入数据有关如何混淆数据文件的详细信息，请参阅用户指南的结构部分中的在线帮助。

**语法** |  **描述**
---|---
out = importbinaryobfuscated(key,filename,file_units,x0,y0,z0,reverse_index_order); |  在三维模拟中从文件名导入二进制数据。文件名后的所有参数都是可选的。

**参数** |  **默认值** |  **类型** |  **描述**
---|---|---|---
key  |  必填  |  string  |  用于解密混淆文件的密钥。
filename  |  必填  |  string  |  要导入的二进制数据文件的名称。可以包含文件的完整路径，或相对于当前工作目录的路径。
file_units  |  "m"  |  string  |  可选的字符串参数 file_units 可以是 "m"、"cm"、"mm"、"microns" 或 "nm"，以指定文件中的单位。
x0  |  0  |  number  |  可选参数 x0、y0 和 z0 指定图形布局编辑器全局坐标中的数据原点。例如，如果您在空间中相对于特定点（例如 (0,0,-5) 微米）定义了体素，则应将 z0 设置为 -5 微米。
y0  |  0  |  number  |
z0  |  0  |  number  |
reverse_index_order  |  0  |  number  |  可选参数 reverse_index_order 可以设置为 1 以反转文件中索引的解释方式。在使用脚本命令之前，最好通过图形导入验证正确的设置。

**示例**

请参阅此示例混淆导入数据。

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [importbinary](./importbinary.md)
