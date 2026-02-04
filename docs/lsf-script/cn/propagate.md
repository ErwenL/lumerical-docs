# propagate

计算任意模式在波导中传播一定距离后的最终模式分布。这是通过将模式分解为波导支持的模式来完成的。然后每个支持的模式通过波导传播。最终的模式相干叠加给出最终模式分布。此计算中使用的模式来自一个或多个 FDE 模拟。

有关重叠和耦合计算的更多详情，请参阅 [overlap](./overlap.md) 函数。

**语法** | **描述**
---|---
out = propagate(mode, d, n1, n2); |

- mode：包含要传播模式的监视器名称
- d：传播距离
- n1：最小折射率
- n2：最大折射率
- out：propagate 命令创建的结果数据集名称

out = propagate(mode, d, n1, n2, x, y); | 可以在计算 propagate 之前调整模式对齐方式。

- x 偏移量
- y 偏移量

**示例**

此示例改编自 [偏振旋转](https://optics.ansys.com/hc/en-us/articles/360042799593) 中的 polarization_rotator.lsf。您可以从 [偏振旋转](https://optics.ansys.com/hc/en-us/articles/360042799593) 页面下载 waveguideA.lms 和 waveguideB.lms。

以下脚本从波导 A 的模式列表中获取第一个模式，并在波导 B 中将此模式传播距离 L_rotation。它生成波导 A 的模式的 |E|² 以及在波导 B 中传播后的模式的图。

```powershell
# 找到波导 B 的前 2 个模式的索引
n1 = getdata("mode1","neff");
n2 = getdata("mode2","neff");
lambda_0 = c/getdata("mode1","f");

# 估计偏振旋转所需的传播长度
L_rotation = lambda_0/2/real(n1-n2);

# 传播距离 L_rotation
mode_L = propagate("TE_A",L_rotation,n1,n2);

?getdata(mode_L,"accounted_transmission");
结果：
0.845998

?getdata(mode_L); # 查看可用数据列表
f x y z num_modes Ex Ey Ez Hx
Hy Hz accounted_transmission accounted_reflection
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[copydcard](./copydcard.md)、[findmodes](./findmodes.md)、[coupling](./coupling.md)、[overlap](./overlap.md)、[bestoverlap](./bestoverlap.md)、[expand](./expand.md)
