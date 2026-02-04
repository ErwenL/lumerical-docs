<!--
Translation from English documentation
Original command: linspace
Translation date: 2026-02-03
-->

# linspace

创建线性间隔的数组。

**语法** |  **描述**
---|---
x = linspace(min,max,num);  |  x 将是包含 num 个元素的数组，在 min 和 max 之间线性间隔。如果 num 设置为 1，则 x 将是 min 和 max 的平均值。

**示例**

    ?x=linspace(1,3,4);
    result:
    1
    1.66667
    2.33333
    3

使用 num 为 1 调用 linspace。结果将是 min 和 max 的平均值。

    ?linspace(1,2,1);
    result:
    1.5

**相关命令**

- [List of commands](./List-of-commands.md)
- [:](./Colon.md)
- [end](./end.md)
- [ [] ](./lbracketrbracket.md)
