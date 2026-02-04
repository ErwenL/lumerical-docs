<!--
Translation from English documentation
Original command: #
Translation date: 2026-02-03
-->

# #

注释脚本文件。# 字符后的任何内容都将被忽略。

**语法** |  **描述**
---|---
x=1; # set x to 1  |  # 字符后的任何内容都将被忽略。

**示例**

在脚本文件中添加注释

    ################################################
    # this section will calculate power transmission
    T=transmission("Monitor3"); # store transmission in T

多行注释：要创建多行注释，请使用如下所示的 if 语句。

    if (0) { # if 0, skip these lines. if 1, run these lines.
    a=1;
    b=2;
    c=a+b;
    }

可以创建包含 # 符号的字符串。只需按常规方式创建字符串，无需特殊操作或转义字符。唯一容易混淆的地方是自动文本着色方案会将 # 符号后的所有文本变为绿色。这看起来可能有些混乱，但不会导致任何错误。

    ?"this string contains a # symbol";

**相关命令**

- [List of commands](./List-of-commands.md)
