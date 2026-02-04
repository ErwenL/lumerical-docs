<!-- Translated: 2026-02-03 -->
<!-- Original: transmission -->

# transmission

返回通过功率监视器和剖面监视器的传输功率量，归一化到源功率。值为 0.3 表示源注入的光功率有 30% 通过了监视器。负值表示功率沿负方向流动。

频域功率传输使用以下公式计算。

$$ T(f) = \frac{ \frac{1}{2} \int_{\text{monitor}} \mathbf{Re} (\mathbf{P}(f)) \cdot d\mathbf{S} }{\text{ sourcepower(f)} } $$

其中

\(T(f)\) 是作为频率函数的归一化传输

\(\mathbf{P}(f)\) 是坡印廷矢量

\(d\mathbf{S}\) 是表面法线

归一化状态（cwnorm 或 nonorm）不影响结果，因为有源功率归一化。

**语法** | **描述**
---| ---
out = transmission("mname"); | 通过监视器 mname 的传输。从监视器的形状必须能明显看出哪个轴垂直于监视器表面。
out = transmission("mname", option); | 附加参数 option 的值可以为 1 或 2。如果是 2，则根据对称或反对称边界尽可能展开数据，前提是数据来自在 x min、y min 或 z min 处与这些边界相交的监视器。option 的默认值为 2。

**示例**

此示例展示了如何绘制通过监视器的功率传输。

```lsf
m="x2";   # monitor name
f=getdata(m,"f");
T=transmission(m);
plot(c/f*1e6,T,"wavelength(um)","transmission");
```

**另见**

[sourcepower](./sourcepower.md)、[dipolepower](./dipolepower.md)、[transmission_avg](./transmission_avg.md)、[transmission_pavg](./transmission_pavg.md)、[Integrating Poynting vector](https://kx.lumerical.com/t/integrating-the-poynting-vector/33595)
