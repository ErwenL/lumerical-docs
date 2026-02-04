<!-- Translation completed: 2026-02-04 -->
<!-- Original command: sin -->

# sin

计算三角正弦函数。角度单位为弧度。该函数适用于复数角度。复数的相位在-π到π之间评估。

**语法** | **描述**
---|---
out = sin(x); | 返回x的复数正弦值。

**示例**

计算sin(π/4 + i)。

```lsf
theta=pi/4+1i;
?sin(theta);
result: 
1.09112+0.830993i 
```

**另请参阅**

[命令列表](List_of_commands.md)、[asin](asin.md)
