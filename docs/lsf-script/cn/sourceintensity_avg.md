# sourceintensity_avg

返回注入到模拟中的源的总光谱平均强度。平均强度等于平均功率除以源面积。有关更多信息，请参阅[sourcepower_pavg](./sourcepower_pavg.md)命令和单位与归一化 - [光谱平均](./Spectral_Averaging.md)部分。

**语法** | **描述**
---|---
`out = sourceintensity_avg;` | 返回如上定义的光谱平均源强度。
`out = sourceintensity_avg(option);` | 额外的参数option可以是1或2。如果为2，则根据来自与x min、y min或z min处的边界相交的监视器的对称或反对称边界，尽可能展开数据。option的默认值为2。
`out = sourceintensity_avg(option, "sourcename");` | 此函数可以使用一个源的频谱进行归一化，而不是所有源的总和。

**示例**

请参阅[sourceintensity](./sourceintensity.md)和[光谱平均 - 用法](./Spectral_Averaging_Usage.md)

**另请参阅**

[sourcenorm2_avg](./sourcenorm2_avg.md), [sourceintensity](./sourceintensity.md), [sourcepower](./sourcepower.md), [transmission_avg](./transmission_avg.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md), [单位和归一化](./Units_and_Normalization.md), [光谱平均](./Spectral_Averaging.md)
