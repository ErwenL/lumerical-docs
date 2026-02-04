<!--
Translation from English documentation
Original command: transmission_pavg
Translation date: 2026-02-04 22:50:15
-->

# transmission_pavg

返回 该 partial spectral average power through 一个 监视器 surface, normalized 到 该 partial spectral average 的 该 源. See 该 Units 和 normalization - [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging) section 用于 more information.

$$ T_{pavg}(f) = \frac{\frac{1}{2} \int real(_{partial}).dS}{sourcepower_{pavg}(f)} $$

其中

Tpavg 是 该 normalized partial spectral average transmission

是 该 partial spectral average Poynting 向量

dS 是 该 surface normal

The normalization state (cwnorm 或 nonorm) does not affect 该 result because 的 该 源 power normalization.

**语法** |  **描述**  
---|---  
out = transmission_pavg ("monitorname"); |  返回 该 partial spectral average transmission through monitorname. It 必须 为 obvious 从 该 shape 的 该 监视器 该 axis 是 normal 到 该 监视器 surface.  
out = transmission_pavg ("monitorname", option); |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.  
  
**示例**

Please refer 到 [transmission](/hc/en-us/articles/360034405354-transmission) 和 [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)

**参见**

[sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg), [transmission](/hc/en-us/articles/360034405354-transmission), [transmission_avg](/hc/en-us/articles/360034405374-transmission-avg), [Units 和 Normalization](**%20to%20be%20defined%20**), [Spectral averaging](/hc/en-us/articles/360034394254-Spectral-averaging), [Spectral averaging - Usage](/hc/en-us/articles/360034383174-Spectral-averaging)
