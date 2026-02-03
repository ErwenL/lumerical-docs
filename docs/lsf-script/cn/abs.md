<!--
Translation from English documentation
Original command: abs
Translation date: 2026-02-03
-->

# abs

返回数字或矩阵的绝对值。

**Syntax** | **Description**
---|---
out = abs(x); | 返回x的绝对值。

**Example**

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