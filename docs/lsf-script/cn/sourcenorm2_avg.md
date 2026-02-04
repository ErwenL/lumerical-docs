# sourcenorm2_avg

返回用于在cwnorm状态下归一化总光谱平均量数据的源归一化频谱。有关更多信息，请参阅单位和归一化 - [光谱平均](./Spectral_Averaging.md)部分。

脚本函数sourcenorm定义为：

$$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{sources} \int \exp (i \omega t) s_{j}(t) d t $$

如果sourcenorm2_avg不带任何参数调用，它返回：

$$ \text{sourcenorm}2_{-} \operatorname{avg}=\int_{-\infty}^{+\infty}\left|s\left(\omega^{\prime}\right)\right|^{2} d \omega^{\prime} $$

**语法** | **描述**
---|---
`out = sourcenorm2_avg;` | 此函数返回用于总光谱平均量的源归一化。
`out = sourcenorm2_avg("sourcename");` | 此函数可以使用一个源的频谱进行归一化，而不是所有源的总和。

**示例**

请参阅[sourcenorm](./sourcenorm.md)和[光谱平均 - 用法](./Spectral_Averaging_Usage.md)

**另请参阅**

[sourcenorm](./sourcenorm.md), [sourcenorm2_pavg](./sourcenorm2_pavg.md), [sourcepower_avg](./sourcepower_avg.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md), [光谱平均](./Spectral_Averaging.md)
