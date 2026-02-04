<!--
Translation from English documentation
Original command: question
Translation date: 2026-02-03 12:19:13
-->

# ?

#  ? (打印, 显示) - 脚本操作符 

[FDTD](../categories/FDTD.md) [MODE](../categories/MODE.md) [DGTD](../categories/DGTD.md) [CHARGE](../categories/CHARGE.md) [HEAT](../categories/HEAT.md) [FEEM](../categories/FEEM.md) [INTERCONNECT](../categories/INTERCONNECT.md)

将输出打印到屏幕。要更改输出精度，请使用 `format` 脚本命令。

**语法** |  **描述**
---|---
?command; |  在屏幕上显示命令的输出。此函数不返回任何数据。

**示例**

此示例展示了如何使用 "?" 命令在屏幕上显示计算结果。

```lsf
?(5+5);
```

结果：

```
10
```

此示例展示了如何使用 "?" 命令显示字符串。

```lsf
?"file_"+"name_"+num2str(1);
```

输出：

```
file_name_1
```

> **注意：** 当输出为矩阵时，最大显示长度为 2000。此限制不适用于字符串。

```lsf
?1:2001;
```

```
matrices of length greater than 2000 are not displayed to the output
```

```lsf
?num2str(1:2001)
```

```
1
2
3
⋮
2000
2001
```

**另请参见**

- [命令列表](./command_list.md)
- [write](./write.md)
- [format](./format.md)
- [#](./hash.md)
