# findresonances

返回从用户在频率范围 \\( [f_{\text{min}}, f_{\text{max}}] \\) 内指定的纯实数或复数信号的时间轨迹中提取的共振频率、衰减常数、Q 因子、振幅和相位。findresonances 脚本命令使用一种称为滤波器对角化的谐波反演方法（参见参考文献 [1]），通过以下形式的指数衰减谐振动的叠加来近似时间信号：

$$ s(t) \approx \sum_{k=1}^{N} A_k \cos(2 \pi f_k t - \phi_k) e^{- \alpha_k t} \text{, 对于实数信号}$$

$$ s(t) \approx \sum_{k=1}^{N} A_k e^{-i (2 \pi f_k t - \phi_k)} e^{- \alpha_k t} \text{, 对于复数信号}$$

其中 \\( N \\) 是共振数量，每个共振由四个实值参数表征：

- \\( f_k \\)：共振频率。
- \\( \alpha_k \\)：衰减常数，其中 \\( \alpha_k \ge 0 \\)。或者，衰减由 Q 因子 \\( Q_k = \omega_k / 2 \alpha \\) 描述，其中 \\( \omega_k = 2 \pi f_k \\) 是相应的角频率。
- \\( A_k \\)：振幅。
- \\( \phi_k \\)：相位。

此外，findresonances 返回一个可用于识别脚本命令报告的虚假共振的误差估计。这是一个相对置信度的度量，即只有通过比较所有找到的共振的估计值才有意义。如果某个共振的误差估计值明显大于其他共振，则它更有可能是虚假共振。

重要说明：

- 要分析的信号应仅在所有源停止向系统注入能量后开始。如果未去除信号的上升部分，findresonances 可能会报告虚假共振，特别是错误的 Q 因子。
- 提供的信号越长，报告的模式就越准确。然而，Q 因子对此比共振频率敏感得多。通常可以从仅几个振荡周期获得非常准确的频率信息，而准确的 Q 因子需要更多的数据。
- 为了可靠地找到模式，它们必须在仿真中有足够的能量激发。确保激发带宽与频率窗口 \\( [f_{\text{min}}, f_{\text{max}} \\) 相当或更大是很重要的。
- 结果在频率间隔 \\( [f_{\text{min}}, f_{\text{max}}] \\) 中心附近更可靠。当扫描大频率间隔时，使用多个重叠的频率窗口运行 findresonances 可能会有帮助。
- 激发小频率范围有助于减少计算中的噪声。因此，对于已知频率的共振的仔细分析，使用以共振频率为中心的窄带脉冲激发系统。
- 此脚本命令无法可靠地找到 Q 因子非常低（\\(Q \lesssim 10\\)）的共振。特别是当存在高 Q 因子和低 Q 因子的模式时，低 Q 共振不会非常准确。

### 参考文献：

[1] V. A. Mandelshtam and H. S. Taylor, "Harmonic inversion of time signals and its application," J. Chem. Phys., vol. 107, no. 17, p. 6756-6769 (1997).

**语法** | **描述**
---|---
out = findresonances(time, signal, frequency_interval); | 返回从信号与时间数据中提取的共振参数。结果 _out_ 是一个 Nx6 实值矩阵，其中 N 是在 frequency_interval 指定的范围内找到的共振数量。如果未找到共振，矩阵 out 将为空。_out_ 的 6 列对应于：**[频率, 衰减常数, Q 因子, 振幅, 相位, 误差估计]** 输入 time 和 signal 必须是一维数组；time 必须是实值，而 signal 可以是实值或复值。输入 frequency_interval 是一个具有两个条目 \\( [f_{\text{min}}, f_{\text{max}}] \\) 的实值数组，限定搜索的频率范围。

**示例**

以下示例显示如何从两个衰减正弦信号的叠加中提取共振。我们对不同时长的信号进行采样，并显示结果相同。对于这个简单的分析信号，只需要几个振荡周期就可以获得所有共振参数的准确值。在实践中，更复杂的信号（例如，FDTD 仿真中时间监视器的信号）可能需要更多的振荡周期，特别是对于准确的衰减或 Q 因子值，如上重要说明中所述。最后，请注意两个共振的误差估计大致在相同的数量级内，因此它们的可靠性相当。

```powershell
# 分析信号的共振频率、衰减常数、振幅和相位：
f1 = 1.765;
alpha1 = 0.005;
ampl1=1.3;
phase1 = 0.4;
f2 = 2.345;
alpha2 = 0.012;
ampl2= 0.45;
phase2 = 1.234;
# 信号的时间间隔：
t_long = linspace(0,20,201);
t_short = t_long(1:20);
# 信号：
signal_long = ampl1*cos(2*pi*f1*t_long - phase1)*exp(-alpha1*t_long) + ampl2*cos(2*pi*f2*t_long - phase2)*exp(-alpha2*t_long);
signal_short = ampl1*cos(2*pi*f1*t_short - phase1)*exp(-alpha1*t_short) + ampl2*cos(2*pi*f2*t_short - phase2)*exp(-alpha2*t_short);
# 查找共振：
res_long = findresonances(t_long, signal_long, [1.5,3]);
res_short = findresonances(t_short, signal_short, [1.5,3]);
# 绘制信号并显示结果：
plotxy(t_long, signal_long, t_short, signal_short, "time", "signal");
legend("long signal", "short signal");
?"***Long signal***";
?"Resonant frequencies: " + num2str(transpose(res_long(:,1)));
?"Decay constant:       " + num2str(transpose(res_long(:,2)));
?"Q-factor:            " + num2str(transpose(res_long(:,3)));
?"Amplitude:           " + num2str(transpose(res_long(:,4)));
?"Phase:               " + num2str(transpose(res_long(:,5)));
?"Error estimate:       " + num2str(transpose(res_long(:,6)));
?"***Short signal***";
?"Resonant frequencies: " + num2str(transpose(res_short(:,1)));
?"Decay constant:       " + num2str(transpose(res_short(:,2)));
?"Q-factor:            " + num2str(transpose(res_short(:,3)));
?"Amplitude:           " + num2str(transpose(res_short(:,4)));
?"Phase:               " + num2str(transpose(res_short(:,5)));
?"Error estimate:       " + num2str(transpose(res_short(:,6)));
result:
***Long signal***
Resonant frequencies: 1.765 2.345
Decay constant:       0.005 0.012
Q-factor:            1108.98 613.92
Amplitude:            1.3 0.45
Phase:               0.4 1.234
Error estimate:       1.02591e-015 1.07493e-015
***Short signal***
Resonant frequencies: 1.765 2.345
Decay constant:       0.005 0.012
Q-factor:            1108.98 613.92
Amplitude:            1.3 0.45
Phase:               0.4 1.234
Error estimate:       3.13843e-016 1.64344e-015
```

**另请参阅**

[命令列表](../命令列表.md)、[findpeaks](./findpeaks.md)、[plotxy](./plotxy.md)、[transpose](./transpose.md)