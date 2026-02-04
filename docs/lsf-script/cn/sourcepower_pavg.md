# sourcepower_pavg

返回源注入到模拟中的部分光谱平均功率。有关更多信息，请参阅单位和归一化 - [光谱平均](./Spectral_Averaging.md)部分。

部分光谱平均使用以下形式的洛伦兹加权：

$$ \begin{array}{c}{\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{array} $$

此脚本函数根据归一化状态是cwnorm还是nonorm计算以下量：

$$ \text{sourcepower}_{-}\text{pavg}_{nonorm}(f)=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} \text{sourcepower}_{nonorm}(\omega) d \omega $$

$$ \text{sourcepower}_{-}\text{pavg}_{cwnorm}(f)=\frac{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)|^2\text{sourcepower}_{cwnorm}(\omega^{\prime}) d \omega^{\prime}}{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)^{\prime}|^2 d\omega^{\prime}} $$

其中sourcepower是sourcepower脚本函数返回的量，s(ω)由sourcenorm返回，且ω=2πf。通常，此函数应在cwnorm状态下使用。另请参阅sourcenorm2_pavg脚本函数。

**语法** | **描述**
---|---
`out = sourcepower_pavg(f, df);` | 返回如上定义的光谱平均源功率。f是频率，df是进行平均的频率范围，两者都以Hz为单位。
`out = sourcepower_pavg(f, df, option);` | 额外的参数option可以是1或2。如果为2，则根据来自与x min、y min或z min处的边界相交的监视器的对称或反对称边界，尽可能展开数据。option的默认值为2。
`out = sourcepower_pavg(f, df, option, "sourcename");` | 此选项允许您获取一个源的频谱，而不是所有源的总和。此选项仅在具有多个源的模拟中需要。

**示例**

请参阅[sourcepower](./sourcepower.md)和[光谱平均 - 用法](./Spectral_Averaging_Usage.md)

**另请参阅**

[sourcenorm2_pavg](./sourcenorm2_pavg.md), [sourcepower](./sourcepower.md), [sourcepower_avg](./sourcepower_avg.md), [transmission_pavg](./transmission_pavg.md), [sourceintensity_pavg](./sourceintensity_pavg.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md), [光谱平均](./Spectral_Averaging.md)
