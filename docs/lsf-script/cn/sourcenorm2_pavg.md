<!--
Translation from English documentation
Original command: sourcenorm2_pavg
Translation date: 2026-02-04 22:50:14
-->

# sourcenorm2_pavg

返回 该 源 normalization spectrum used 到 normalize 数据 在 该 cwnorm state 用于 该 partial spectral averaged quantities. See 该 Units 和 normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section 用于 more information.

If 该 源 时间 signal 的 该 jth 源 在 该 仿真 是 sj(t), 和 N 是 该 数字 的 active sources 那么

$$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{s o u r c s s} \int \exp (i \omega t) s_{j}(t) d t $$

Partial spectral averaging uses 一个 Lorentzian weighting 的 该 following form. Delta 是 该 FWHM 的 |h|2.

$$ \begin{数组}{c}{\left|h_{2}\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{数组} $$

If 此 函数 是 called without any 参数, it 返回

$$ sourcenorm2_{pavg }=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}\left|s\left(\omega^{\prime}\right)\right|^{2} d \omega^{\prime} $$

**语法** |  **描述**  
---|---  
out = sourcenorm2_pavg( f, delta); |  This 函数 返回 该 源 normalization 用于 partial spectral averaged quantities.  
out = sourcenorm2_pavg( f, delta, "sourcename"); |  This 函数 makes it possible 到 perform 该 normalization 使用 该 spectrum 的 one 源, rather than 该 sum 的 all 该 sources.  
  
**示例**

Please refer 到 [sourcenorm](/hc/en-us/articles/360034925273-sourcenorm) 和 [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**参见**

[sourcenorm](/hc/en-us/articles/360034925273-sourcenorm), [sourcenorm2_avg](/hc/en-us/articles/360034405474-sourcenorm2-avg), [sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units 和 Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
