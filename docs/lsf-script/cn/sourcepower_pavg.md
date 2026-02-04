<!--
Translation from English documentation
Original command: sourcepower_pavg
Translation date: 2026-02-04 22:50:14
-->

# sourcepower_pavg

返回 该 partial spectral average power injected into 该 仿真 通过 该 源. See 该 Units 和 normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section 用于 more information.

Partial spectral averaging uses 一个 Lorentzian weighting 的 该 form

$$ \begin{数组}{c}{\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{数组} $$

This 脚本 函数 计算 该 following quantities, depending 在 whether 该 normalization state 是 cwnorm 或 nonorm:

$$ \text{sourcepower}_{-}\text{pavg}_{nonorm}(f)=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} \text { sourcepower}_ {nonorm } (\omega ) d \omega $$

$$ \text{sourcepower}_{-}\text{pavg}_{cwnorm}(f)=\frac{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)|^2\text { sourcepower}_ {cwnorm } (\omega^{\prime} ) d \omega^{\prime}}{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)^{\prime}|^2 d\omega^{\prime}} $$

其中 sourcepower 是 该 quantity returned 通过 该 sourcepower 脚本 函数, s(w) 是 returned 通过 sourcenorm, 和 ω=2πf. Typically, 此 函数 应该 为 used 在 该 cwnorm state. Also see 该 sourcenorm2_pavg 脚本 函数.

**语法** |  **描述**  
---|---  
out = sourcepower_pavg(f,df); |  返回 该 spectrally averaged 源 power as defined above. The quantity f 是 该 频率 和 该 quantity df 是 该 频率 range around 该 该 averaging 是 performed, both 在 Hz.  
out = sourcepower_pavg(f, df,option); |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.  
out = sourcepower_pavg(f,df, option, "sourcename"); |  This option allows you 到 obtain 该 spectrum 的 one 源, rather than 该 sum 的 all sources. This option 是 only needed 用于 simulations 使用 multiple sources.  
  
**示例**

Please refer 到 [sourcepower](/hc/en-us/articles/360034925313-sourcepower) 和 [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**参见**

[sourcenorm2_pavg](/hc/en-us/articles/360034405494-sourcenorm2-pavg), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [sourcepower_avg](/hc/en-us/articles/360034925333-sourcepower-avg), [transmission_pavg](/hc/en-us/articles/360034405414-transmission-pavg), [sourceintensity_pavg](/hc/en-us/articles/360034925413-sourceintensity-pavg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units 和 Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
