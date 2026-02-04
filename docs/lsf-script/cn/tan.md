<!-- Translation completed: 2026-02-04 -->
<!-- Original command: tan -->

# tan

计算三角正切函数。角度单位为弧度。该函数适用于复数角度。复数的相位在-π到π之间评估。

**语法** | **描述**
---|---
out = tan(x); | 返回x的复数正切值。

**示例**

计算tan(π/4 + i)。

```lsf
theta=pi/4+1i;
?tan(theta);
result: 
0.265802+0.964028i 
```

**另请参阅**

[命令列表](List_of_commands.md)、[atan](atan.md)、[atan2](atan2.md)
