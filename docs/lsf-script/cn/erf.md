# erf

计算误差函数，定义如下方程：

$$ \operatorname{erf}(z)=\frac{2}{\sqrt{\pi}} \int_{0}^{z} \exp \left(-t^{2}\right) d t $$

**语法** | **描述**
---|---
out=erf(z); | 返回 z 的误差函数，其中 z 是标量数字或标量数字矩阵。

**示例**

绘制 z 从 -5 到 5 的误差函数图。

```powershell
z=linspace(-5,5,50); # 生成从 -5 到 5 包含 50 个点的数字向量
erf_z = erf(z);
plot(z,erf_z,"z","erf");
```

下图显示了示例代码创建的图。

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[erfc](./erfc.md)、[erfinv](./erfinv.md)、[erfcinv](./erfcinv.md)
