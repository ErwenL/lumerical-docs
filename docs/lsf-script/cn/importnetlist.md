<!--
Translation from English documentation
Original command: importnetlist
Translation date: 2026-02-03
-->

# importnetlist

此脚本命令可以导入光学 SPICE 网表。

**语法** |  **描述**
---|---
importnetlist("compound name", "filename"); |  导入光学 SPICE 网表。"compound name" 是可选的，如果未指定，将导入根元素级电路配置；如果指定，则将子电路导入到此指定的复合对象中。

**参数** |    |  **类型** |  **描述**
---|---|---|---
compound name  |  可选  |  string  |  复合对象名称
filename  |  必填  |  string  |  网表名称。

### 相关命令

- [List of commands](./List-of-commands.md)
- [exportnetlist](./exportnetlist.md)
