# sourceintensity_avg

Returns the total spectral average intensity injected into the simulation by the source. The average intensity is equal to the average power divided by the source area. See the [sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg) command and the Units and normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section for more information.

**Syntax** |  **Description**  
---|---  
out = sourceintensity_avg; |  Returns the spectrally averaged source intensity as defined above.  
out = sourceintensity_avg(option); |  The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2.  
out = sourceintensity_avg(option, "sourcename"); |  This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum of all the sources.   
  
**Example**

Please refer to [sourceintensity](/hc/en-us/articles/360034925373-sourceintensity) and [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**See Also**

[sourcenorm2_avg](/hc/en-us/articles/360034405474-sourcenorm2-avg), [sourceintensity](/hc/en-us/articles/360034925373-sourceintensity), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [transmission_avg](/hc/en-us/articles/360034405374-transmission-avg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units and Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
