# erfcinv

计算逆互补误差函数，根据以下与逆误差函数 erfinv 的关系式定义：

$$ erfcinv(1-z)=erfinv(z) $$

**语法** | **描述**
---|---
out=erfcinv(z); | 返回 z 的逆互补误差函数，其中 z 是标量数字或标量数字矩阵。对于区间 (0, 2) 之外的输入，erfcinv 返回 NaN。

**示例**

绘制逆互补误差函数图，其中 0 < z < 2。

```powershell
z=0.01:0.05:1.99;
erfcinv_z = erfcinv(z);
plot(z,erfcinv_z,"z","erf");
```

下图显示了示例代码创建的图。

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[erf](./erf.md)、[erfc](./erfc.md)、[erfinv](./erfinv.md)
