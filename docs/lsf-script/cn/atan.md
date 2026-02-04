<!-- Translation completed: 2026-02-04 -->
<!-- Original command: atan -->

# atan

计算反三角正切函数（反正切）。角度单位为弧度。该函数适用于复数值。复数的相位在-π到π之间评估。如果x是复数或|x|>1，使用以下公式：

$$
	ext{arctan(x)} = rac{i}{2}	ext{ln}(rac{i+x}{i-x})
$$

**语法** | **描述**
---|---
out = atan(x); | 返回x的复数反正切。atan的范围是-π/2到π/2。

**示例**

绘制atan(y/x)在-π ≤ theta ≤ π范围内的图像。

```lsf
theta=linspace(-pi,pi,1000);
x=cos(theta);
y=sin(theta);
plot(theta*180/pi,atan(y/x)*180/pi,"theta (deg)","atan(y/x) (deg)","atan(y/x)");
plot(y/x,atan(y/x)*180/pi,"y/x","atan(y/x) (deg)","atan(y/x)");
```

计算atan(π/4 + i)。

```lsf
x=pi/4+1i;
?atan(x);
result: 
0.972497+0.50321i 
```

**另请参阅**

[命令列表](List_of_commands.md)、[atan2](atan2.md)、[tan](tan.md)
