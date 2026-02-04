<!-- Translation completed: 2026-02-04 -->
<!-- Original command: atan2 -->

# atan2

计算y/x的反三角正切函数（反正切），返回正确象限的角度。角度单位为弧度。该函数仅适用于实数值。

**语法** | **描述**
---|---
out = atan2(y,x); | x和y必须是实数。atan2的范围是-π到π。

**示例**

绘制atan2(y,x)在-π ≤ theta ≤ π范围内的图像。

```lsf
theta=linspace(-pi,pi,1000);
x=cos(theta);
y=sin(theta);
plot(theta*180/pi,atan2(y,x)*180/pi,"theta (deg)","atan2(y,x) (deg)","atan2(y,x)");
plot(y/x,atan2(y,x)*180/pi,"y/x","atan2(y,x) (deg)","atan2(y,x)");
```

计算atan2在(1,1)和(1,-1)处的值。角度转换为度数。

```lsf
?atan2(1,1)*180/pi;
result: 
45 
?atan2(1,-1)*180/pi;
result: 
135 
```

**另请参阅**

[命令列表](List_of_commands.md)、[atan](atan.md)、[tan](tan.md)
