# num2str

将整数、浮点数或矩阵转换为字符串。矩阵只能是 1D 或 2D。用户可以使用 format 脚本命令更改输出精度，或者自 2019b r6 版本起，用户可以通过向命令提供第二个参数来指定格式。

**语法** | **描述**
---|---
out = num2str(x); | 将数字 x 转换为字符串。x 也可以是 1D 或 2D 矩阵。制表符字符（而不是空格）将用作列之间的分隔符。
out = num2str(x, format); | 将数字 x 转换为字符串。x 也可以是 1D 或 2D 矩阵。格式类型选项包括：
**整数**：
%u：无符号整数，取输入的绝对值
%d：十进制有符号整数，对输入四舍五入
%i：十进制有符号整数，对输入四舍五入
**浮点数**：
%f：双精度
%g：双精度
%G：双精度，指数表示法使用大写 'E'
**指数**：
%e：双精度
%E：双精度，指数表示法使用大写 'E'
使用上述格式类型选项，可以为转换定义宽度和精度。也可以使用 Boost 格式化。这些标志直接出现在格式参数的 "%" 之后：
**标志**：
+：显示所有数字的符号
0：用前导零填充到完整宽度

**示例**

将 pi 转换为字符串。

```
format long;
?num2str(pi);
3.141592653589793
```

将 2D 矩阵转换为字符串并写入文本文件。

```
X=meshgridx(1:2,1:3);
?num2str(X);
write("filename.txt",num2str(X));> 1 1 1> 2 2 2
```

将 pi 转换为格式为整数、最小宽度为 4 个字符的字符串。

```
?num2str(pi, "%4d");
Warning: prompt line 1: Double values rounded to integers
> 3
```

将 pi 转换为格式为浮点数、小数点后 3 位数字的字符串。

```
?num2str(pi, "%.3f");3.142
```

将 pi 转换为最小宽度为 8 个字符、小数点后 3 个字符的字符串。

```
?num2str(pi, "%8.3f"); 3.142
```

将 pi 转换为最小宽度为 8 个字符、小数点后 3 个字符的字符串，并用前导零填充完整宽度。

```
?num2str(pi, "%08.3f");0003.142
```

将 4*pi 转换为指数表示法、4 位小数的字符串。

```
?num2str(4*pi, "%.4e");1.2566e+01
```

**另请参阅**

- [命令列表](./命令列表.md)
- [""](./.md)
- [+](./+.md)
- [?](./?.md)
- [endl](./endl.md)
- [write](./write.md)
- [format](./format.md)
- [str2num](./str2num.md)
- [findstring](./findstring.md)
- [replace](./replace.md)
- [replacestring](./replacestring.md)
- [substring](./substring.md)
- [eval](./eval.md)
- [lower](./lower.md)
- [upper](./upper.md)
- [toscript](./toscript.md)
