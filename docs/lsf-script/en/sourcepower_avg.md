# sourcepower_avg

Returns the total spectral average power injected into the simulation by the source. See
the Units and normalization -
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
section for more information.

This script function calculates the following quantities, depending on whether the
normalization state is cwnorm or nonorm:

$$ \\text {sourcepower}_{-}{\\text {avg}_{nonorm}}=\\int\_{0}^{+\\infty} \\text
{sourcepower}\_{nonorm}(\\omega) d\\omega $$

$$ \\text {sourcepower}_{-}{\\text
{avg}_{cwnorm}}(f)=\\frac{\\int\_{0}^{+\\infty}|s(\\omega)|^2 \\text
{sourcepower}_{cwnorm}(\\omega) d\\omega}{\\int_{0}^{+\\infty}|s(\\omega)|^2d\\omega} $$

where sourcepower is the quantity returned by the sourcepower script function, s(w) is
returned by sourcenorm, and ω=2πf. Typically, this function should be used in the cwnorm
state. Also see the sourcenorm2_pavg script function.

| **Syntax**                                   | **Description**                                                                                                                                                                                                                                                                           |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = sourcepower_avg;                       | Returns the spectrally averaged source power as defined above.                                                                                                                                                                                                                            |
| out = sourcepower_avg(option);               | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. |
| out = sourcepower_avg(option, "sourcename"); | This option allows you to obtain the spectrum of one source, rather than the sum of all sources. This option is only needed for simulations with multiple sources.                                                                                                                        |

**Example**

Please refer to [sourcepower](./sourcepower.md) and
[Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcenorm2_avg](https://optics.ansys.com/hc/en-us/articles/360034405474-sourcenorm2-avg),
[sourcepower](./sourcepower.md),
[sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg),
[transmission_avg](https://optics.ansys.com/hc/en-us/articles/360034405374-transmission-avg),
[sourceintensity_avg](https://optics.ansys.com/hc/en-us/articles/360034925393-sourceintensity-avg),
[cwnorm](./cwnorm.md), [nonorm](./nonorm.md),
[Units and Normalization](**%20to%20be%20defined%20**),
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
