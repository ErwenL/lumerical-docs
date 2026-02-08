# transmission_pavg

Returns the partial spectral average power through a monitor surface, normalized to the
partial spectral average of the source. See the Units and normalization -
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
section for more information.

$$ T\_{pavg}(f) = \\frac{\\frac{1}{2} \\int real(_{partial}).dS}{sourcepower_{pavg}(f)}
$$

where

Tpavg is the normalized partial spectral average transmission

is the partial spectral average Poynting vector

dS is the surface normal

The normalization state (cwnorm or nonorm) does not affect the result because of the
source power normalization.

| **Syntax**                                       | **Description**                                                                                                                                                                                                                                                                           |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = transmission_pavg ("monitorname");         | Returns the partial spectral average transmission through monitorname. It must be obvious from the shape of the monitor which axis is normal to the monitor surface.                                                                                                                      |
| out = transmission_pavg ("monitorname", option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. |

**Example**

Please refer to [transmission](./transmission.md) and
[Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg),
[transmission](./transmission.md),
[transmission_avg](https://optics.ansys.com/hc/en-us/articles/360034405374-transmission-avg),
[Units and Normalization](**%20to%20be%20defined%20**),
[Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging),
[Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)
