<!--
Translation 从 English documentation
Original 命令: acos
Translation date: 2026-02-03
-->

# acos

计算反三角函数余弦（反余弦）。角度单位是弧度。该函数定义在复数域上。复数的相位在 -π 到 π 之间计算。如果 x 是复数，或者 abs(x) > 1，则使用以下公式：

$$ \text{acos}(x) = -i\ln(x+i\sqrt{1-x^2}) $$

**语法** | **描述**
---|---
out = acos(x); | 返回x的复反余弦值。

**示例**

计算 acos( π /4 + i)。

    x=pi/4+1i;
    ?acos(x);
    result: 
    1.03351-0.992724i

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [cos](./cos.md)