<!--
Translation from English documentation
Original command: sourceintensity_pavg
Translation date: 2026-02-04 22:50:14
-->

# sourceintensity_pavg

返回 该 partial spectral average intensity injected into 该 仿真 通过 该 源. The partial average intensity 是 equal 到 该 partial average power divided 通过 该 源 area. See 该 [sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg) 命令 和 该 Units 和 normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section 用于 more information.

**语法** |  **描述**  
---|---  
out = sourceintensity_pavg (f,df); |  返回 该 spectrally averaged 源 power as defined above. The quantity f 是 该 频率 和 该 quantity df 是 该 频率 range around 该 该 averaging 是 performed, both 在 Hz.  
out = sourceintensity_pavg(f,df, option); |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.  
out = sourceintensity_pavg(f,df, option, "sourcename"); |  This 函数 makes it possible 到 perform 该 normalization 使用 该 spectrum 的 one 源, rather than 该 sum 的 all 该 sources.   
  
**示例**

Please refer 到 [sourceintensity](/hc/en-us/articles/360034925373-sourceintensity) 和 [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**参见**

[sourcenorm2_pavg](/hc/en-us/articles/360034405494-sourcenorm2-pavg), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [sourcepower_avg](/hc/en-us/articles/360034925333-sourcepower-avg), [transmission_pavg](/hc/en-us/articles/360034405414-transmission-pavg), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units 和 Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging)
