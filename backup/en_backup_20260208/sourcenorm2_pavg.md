# sourcenorm2_pavg

Returns the source normalization spectrum used to normalize data in the cwnorm state for the partial spectral averaged quantities. See the Units and normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section for more information.

If the source time signal of the jth source in the simulation is sj(t), and N is the number of active sources then

$$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{s o u r c s s} \int \exp (i \omega t) s_{j}(t) d t $$

Partial spectral averaging uses a Lorentzian weighting of the following form. Delta is the FWHM of |h|2.

$$ \begin{array}{c}{\left|h_{2}\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{array} $$

If this function is called without any arguments, it returns

$$ sourcenorm2_{pavg }=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}\left|s\left(\omega^{\prime}\right)\right|^{2} d \omega^{\prime} $$

**Syntax** |  **Description**  
---|---  
out = sourcenorm2_pavg( f, delta); |  This function returns the source normalization for partial spectral averaged quantities.  
out = sourcenorm2_pavg( f, delta, "sourcename"); |  This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum of all the sources.  
  
**Example**

Please refer to [sourcenorm](/hc/en-us/articles/360034925273-sourcenorm) and [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcenorm](/hc/en-us/articles/360034925273-sourcenorm), [sourcenorm2_avg](/hc/en-us/articles/360034405474-sourcenorm2-avg), [sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units and Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
