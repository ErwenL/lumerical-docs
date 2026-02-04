<!--
Translation from English documentation
Original command: imag
Translation date: 2026-02-03
-->

# imag

返回数字或矩阵的虚部。

**语法** |  **描述**
---|---
out = imag(x);  |  返回 x 的虚部。

**示例**

计算数组中数字的虚部。

    ?x=linspace(0, 2+1i,2);
    result:
    0+0i
    2+1i
    ?imag(x);
    result:
    0
    1

**相关命令**

- [List of commands](./List-of-commands.md)
- [real](./real.md)
- [conj](./conj.md)
