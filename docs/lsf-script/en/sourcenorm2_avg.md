# sourcenorm2_avg

Returns the source normalization spectrum used to normalize data in the cwnorm state for
the total spectral averaged quantities. See the Units and normalization -
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
section for more information.

The script function sourcenorm is defined as

$$ s(\\omega)=\\operatorname{sourcenorm}(\\omega)=\\frac{1}{N} \\sum\_{s o u r c s s}
\\int \\exp (i \\omega t) s\_{j}(t) d t $$

If sourcenorm2_avg is called without any arguments, it returns

$$ \\text {sourcenorm} 2\_{-}
\\operatorname{avg}=\\int\_{-\\infty}^{+\\infty}\\left|s\\left(\\omega^{\\prime}\\right)\\right|^{2}
d \\omega^{\\prime} $$

| **Syntax**                            | **Description**                                                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| out = sourcenorm2_avg;                | This function returns the source normalization for total spectral averaged quantities.                                                 |
| out = sourcenorm2_avg( "sourcename"); | This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum of all the sources. |

**Example**

Please refer to [sourcenorm](./sourcenorm.md) and
[Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcenorm](./sourcenorm.md),
[sourcenorm2_pavg](https://optics.ansys.com/hc/en-us/articles/360034405494-sourcenorm2-pavg),
[sourcepower_avg](https://optics.ansys.com/hc/en-us/articles/360034925333-sourcepower-avg),
[cwnorm](./cwnorm.md), [nonorm](./nonorm.md),
[Units and Normalization](**%20to%20be%20defined%20**),
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
