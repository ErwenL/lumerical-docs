<!--
Translation from English documentation
Original command: length
Translation date: 2026-02-03
-->

# length

返回矩阵中的元素数量。如果参数是字符串，它将返回字符串的长度。

**语法** |  **描述**
---|---
y = length(x); |  y 是矩阵中的元素数量。例如，如果 x 是 n×m 矩阵，则 y = length(x) = n * m。

**示例**

查找矩阵和字符串的长度。

    x=matrix(2,3,3);
    ?y=length(x);
    result:
    18

    ?length("hello");
    result:
    5

**相关命令**

- [List of commands](./List-of-commands.md)
- [size](./size.md)
