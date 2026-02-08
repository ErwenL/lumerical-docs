# transmission

Returns the amount of power transmitted through power monitors and profile monitors,
normalized to the source power. A value of 0.3 means that 30% the optical power injected
by the source passed through the monitor. Negative values mean the power is flowing in
the negative direction.

The frequency domain power transmission is calculated with the following formula.

$$ T(f) = \\frac{ \\frac{1}{2} \\int\_{\\text{monitor}} \\mathbf{Re} (\\mathbf{P}(f))
\\cdot d\\mathbf{S} }{\\text{ sourcepower(f)} } $$

where

\\(T(f)\\) is the normalized transmission as a function of frequency

\\(\\mathbf{P}(f)\\) is the Poynting vector

\\(d\\mathbf{S}\\) is the surface normal

The normalization state (cwnorm or nonorm) does not affect the result because of the
source power normalization.

| **Syntax**                           | **Description**                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = transmission("mname");         | Transmission through monitor mname. It must be obvious from the shape of the monitor which axis is normal to the monitor surface.                                                                                                                                                         |
| out = transmission("mname", option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. |

**Example**

This example shows how to plot the power transmission through a monitor.

```
m="x2";    # monitor name  
f=getdata(m,"f");  
T=transmission(m);
plot(c/f*1e6,T,"wavelength(um)","transmission");  
```

**See Also**

[ sourcepower ](./sourcepower.md) , [ dipolepower ](./dipolepower.md) ,
[ transmission_avg ](https://optics.ansys.com/hc/en-us/articles/360034405374-transmission-avg)
,
[ transmission_pavg ](https://optics.ansys.com/hc/en-us/articles/360034405414-transmission-pavg)
,
[ Integrating Poynting vector ](https://kx.lumerical.com/t/integrating-the-poynting-vector/33595)
