# sourcepower_pavg

Returns the partial spectral average power injected into the simulation by the source. See the Units and normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section for more information.

Partial spectral averaging uses a Lorentzian weighting of the form

$$ \begin{array}{c}{\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{array} $$

This script function calculates the following quantities, depending on whether the normalization state is cwnorm or nonorm:

$$ \text{sourcepower}_{-}\text{pavg}_{nonorm}(f)=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} \text { sourcepower}_ {nonorm } (\omega ) d \omega $$

$$ \text{sourcepower}_{-}\text{pavg}_{cwnorm}(f)=\frac{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)|^2\text { sourcepower}_ {cwnorm } (\omega^{\prime} ) d \omega^{\prime}}{\int_{0}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} |s(\omega)^{\prime}|^2 d\omega^{\prime}} $$

where sourcepower is the quantity returned by the sourcepower script function, s(w) is returned by sourcenorm, and ω=2πf. Typically, this function should be used in the cwnorm state. Also see the sourcenorm2_pavg script function.

**Syntax** |  **Description**  
---|---  
out = sourcepower_pavg(f,df); |  Returns the spectrally averaged source power as defined above. The quantity f is the frequency and the quantity df is the frequency range around which the averaging is performed, both in Hz.  
out = sourcepower_pavg(f, df,option); |  The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2.  
out = sourcepower_pavg(f,df, option, "sourcename"); |  This option allows you to obtain the spectrum of one source, rather than the sum of all sources. This option is only needed for simulations with multiple sources.  
  
**Example**

Please refer to [sourcepower](/hc/en-us/articles/360034925313-sourcepower) and [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcenorm2_pavg](/hc/en-us/articles/360034405494-sourcenorm2-pavg), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [sourcepower_avg](/hc/en-us/articles/360034925333-sourcepower-avg), [transmission_pavg](/hc/en-us/articles/360034405414-transmission-pavg), [sourceintensity_pavg](/hc/en-us/articles/360034925413-sourceintensity-pavg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units and Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
