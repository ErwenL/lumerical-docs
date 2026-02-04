<!-- Translation completed: 2026-02-04 -->
<!-- Original command: angle -->

# angle

以弧度为单位返回复数或矩阵的角度或相位。

**语法** | **描述**
---|---
out = angle(x); | 返回x的相位。相位在-π到π之间评估。

**示例**

计算数组中数值的相位。

```lsf
?x=linspace(0, 2+1i,2);
result: 
0+0i 
2+1i 
?angle(x)*180/pi;
result: 
0 
26.5651 
```

**另请参阅**

[命令列表](List_of_commands.md)、[real](real.md)、[imag](imag.md)、[unwrap](unwrap.md)
