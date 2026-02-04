# erfinv

计算逆误差函数，定义如下方程：

$$ \operatorname{erfinv}(z)=\sum_{k=0}^{\infty} \frac{c_{k}}{2 k+1}\left(\frac{\sqrt{\pi}}{2} z\right)^{2 k+1} $$

**语法** | **描述**
---|---
out=erfinv(z); | 返回 z 的逆误差函数，其中 z 是标量数字或标量数字矩阵。对于区间 (-1, 1) 之外的输入，erfinv 返回 NaN。

**示例**

绘制逆误差函数图，其中 -1 < z < 1。

```powershell
z=[-0.99:0.01:0.99];
erfinv_z = erfinv(z);
plot(z,erfinv_z,"z","erfinv");
```

下图显示了示例代码创建的图。

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[erf](./erf.md)、[erfc](./erfc.md)、[erfcinv](./erfcinv.md)
