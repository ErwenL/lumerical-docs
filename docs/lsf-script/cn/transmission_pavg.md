<!-- Translated: 2026-02-03 -->
<!-- Original: transmission_pavg -->

# transmission_pavg

返回通过监视器表面的部分光谱平均功率，归一化到源的部分光谱平均值。有关更多信息，请参阅单位和归一化 - [光谱平均](./spectral-averaging.md)部分。

$$ T_{pavg}(f) = \frac{\frac{1}{2} \int real(_{partial}).dS}{sourcepower_{pavg}(f)} $$

其中

Tpavg 是归一化的部分光谱平均传输

是部分光谱平均坡印廷矢量

dS 是表面法线

归一化状态（cwnorm 或 nonorm）不影响结果，因为有源功率归一化。

**语法** | **描述**
---| ---
out = transmission_pavg ("monitorname"); | 返回通过 monitorname 的部分光谱平均传输。从监视器的形状必须能明显看出哪个轴垂直于监视器表面。
out = transmission_pavg ("monitorname", option); | 附加参数 option 的值可以为 1 或 2。如果是 2，则根据对称或反对称边界尽可能展开数据，前提是数据来自在 x min、y min 或 z min 处与这些边界相交的监视器。option 的默认值为 2。

**示例**

请参阅 [transmission](./transmission.md) 和 [光谱平均 - 用法](./spectral-averaging-usage.md)

**另见**

[sourcepower_pavg](./sourcepower_pavg.md)、[transmission](./transmission.md)、[transmission_avg](./transmission_avg.md)、[Units and Normalization](./units-and-normalization.md)、[光谱平均](./spectral-averaging.md)、[光谱平均 - 用法](./spectral-averaging-usage.md)
