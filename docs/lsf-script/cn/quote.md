<!--
Translation from English documentation
Original command: quote
Translation date: 2026-02-03
-->

# "

" 和 ' 是字符串操作符。字符串可以用单引号或双引号创建。

使用双引号创建字符串时，支持以下转义序列：

| 转义序列 | 描述 |
|---------|------|
| \" | 字符串中的双引号 |
| \n | 字符串中的换行符 |
| \\ | 字符串中的反斜杠 |

**语法** | **描述**
---|---
out="my string"; | 使用双引号创建字符串

**注意：字面量反斜杠和双引号**

在字符串中创建字面量反斜杠时，总是可以使用 \\\\。然而，如果 \ 不会被解释为转义序列的一部分（\n、\"、\\\\），那么 \ 也会产生一个字面量反斜杠。这个注意事项在将路径存储到字符串中时尤为重要。

假设我们要创建字符串 `C:\Program Files\Lumerical`。以下三个命令都是有效且等效的：

```lsf
mystring = 'C:\Program Files\Lumerical';  # 使用单引号
mystring = "C:\Program Files\Lumerical";  # 使用双引号
mystring = "C:\\Program Files\\Lumerical"; # 使用双引号和 \\ 转义字符
```

然而，假设我们要创建字符串 `C:\Program Files\Lumerical\`（唯一的区别是末尾多了一个反斜杠）。以下两个命令是有效且等效的：

```lsf
mystring = 'C:\Program Files\Lumerical\';   # 使用单引号
mystring = "C:\\Program Files\\Lumerical\\"; # 使用双引号和 \\ 转义字符
```

其他可能的命令（使用单个反斜杠）不是有效的语法，会导致错误。

```lsf
mystring = "C:\Program Files\Lumerical\";  # 使用双引号 - 错误！
```

问题在于脚本解释器会将末尾的 \" 解释为字面量双引号的转义字符，而不是单个反斜杠和结束双引号。当以这种方式解释时，该命令会导致语法错误，因为没有双引号字符来闭合字符串。

**示例**

将监视器名称存储在字符串中。

```lsf
m="time_monitor";
t=getdata(m,"t");
Ex=getdata(m,'Ex');
```

**字符串中的单引号和双引号**

```lsf
?"This is how you \"double quote\" a word";
```
输出：
```
This is how you "double quote" a word
```

```lsf
?"This is how you 'single quote' a word";
```
输出：
```
This is how you 'single quote' a word
```

以下是在字符串中添加反斜杠的方法。如果反斜杠在字符串中间，可以使用 \ 或 \\\\ 来创建反斜杠。然而，当反斜杠在字符串末尾时，必须使用 \\\\ 来创建反斜杠。单个反斜杠会导致语法错误，因为反斜杠和结束引号（即 \"）会被解释为字符串内的字面量双引号，而不是反斜杠和结束引号。

```lsf
?"Backslash in the middle \ of a string";
```
输出：
```
Backslash in the middle \ of a string
```

```lsf
?"Backslash in the middle \\ of a string";
```
输出：
```
Backslash in the middle \ of a string
```

```lsf
?"Backslash in the end of a string\\";
```
输出：
```
Backslash in the end of a string\
```

```lsf
?"Backslash in the end of a string\";
```
输出：
```
syntax error: prompt line: 1
```

这是用户如何使用双引号字符串创建多行字符串的方法。用户可以在字符串之间使用 `endl` 特殊字符，或在字符串内使用 \n 转义字符。

```lsf
?"This is how you create" + endl + "multi-line strings";
```
输出：
```
This is how you create
multi-line strings
```

```lsf
?"This is how you create \nmulti-line strings";
```
输出：
```
This is how you create
multi-line strings
```

**另请参见**

- [命令列表](./command_list.md)
- [单引号](./single_quote.md)
- [num2str](./num2str.md)
- [+](./plus.md)
- [endl](./endl.md)
- [write](./write.md)
- [eval](./eval.md)
- [system](./system.md)
