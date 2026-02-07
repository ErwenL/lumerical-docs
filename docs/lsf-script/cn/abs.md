<!--
Translation 从 English documentation
Original 命令: abs
Translation date: 2026-02-04
-->

# abs

返回数字或矩阵的绝对值。

**语法** | **描述**
---|---
out = abs(x); | 返回x的绝对值。

**示例**

计算数组中数字的绝对值。

    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?abs(x);
    result: 
    0 
    2.23607  

**参见**

- [real](./real.md)
- [imag](./imag.md)