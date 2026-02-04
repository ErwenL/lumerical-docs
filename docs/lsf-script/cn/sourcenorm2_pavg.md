# sourcenorm2_pavg

返回用于在cwnorm状态下归一化部分光谱平均量数据的源归一化频谱。有关更多信息，请参阅单位和归一化 - [光谱平均](./Spectral_Averaging.md)部分。

如果模拟中第j个源的源时间信号为$s_j(t)$，且N是活动源的数量，则：

$$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{sources} \int \exp (i \omega t) s_{j}(t) d t $$

部分光谱平均使用以下形式的洛伦兹加权。Delta是$|h|^2$的FWHM。

$$ \begin{array}{c}{\left|h_{2}\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{array} $$

如果此函数不带任何参数调用，它返回：

$$ sourcenorm2_{pavg }=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}\left|s\left(\omega^{\prime}\right)\right|^{2} d \omega^{\prime} $$

**语法** | **描述**
---|---
`out = sourcenorm2_pavg(f, delta);` | 此函数返回用于部分光谱平均量的源归一化。
`out = sourcenorm2_pavg(f, delta, "sourcename");` | 此函数可以使用一个源的频谱进行归一化，而不是所有源的总和。

**示例**

请参阅[sourcenorm](./sourcenorm.md)和[光谱平均 - 用法](./Spectral_Averaging_Usage.md)

**另请参阅**

[sourcenorm](./sourcenorm.md), [sourcenorm2_avg](./sourcenorm2_avg.md), [sourcepower_pavg](./sourcepower_pavg.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md), [光谱平均](./Spectral_Averaging.md)
