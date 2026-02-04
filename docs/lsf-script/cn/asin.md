<!-- Translation completed: 2026-02-04 -->
<!-- Original command: asin -->

# asin

计算反三角正弦函数（反正弦）。角度单位为弧度。该函数适用于复数值。复数的相位在-π到π之间评估。如果x是复数或|x|>1，使用以下公式：

$$
\text{arcsin(x)} = -i\ln(ix+\sqrt{1-x^2})
$$

**语法** | **描述**
---|---
out = asin(x); | 返回x的复数反正弦值。

**示例**

计算asin(π/4 + i)。

```lsf
x=pi/4+1i;
?asin(x);
result: 
0.537282+0.992724i  
```

**另请参阅**

[命令列表](List_of_commands.md)、[sin](sin.md)
