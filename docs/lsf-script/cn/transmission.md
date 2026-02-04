<!--
Translation from English documentation
Original command: transmission
Translation date: 2026-02-04 22:50:15
-->

# transmission

返回 该 amount 的 power transmitted through power monitors 和 profile monitors, normalized 到 该 源 power. A 值 的 0.3 means 该 30% 该 optical power injected 通过 该 源 passed through 该 监视器. Negative 值 mean 该 power 是 flowing 在 该 negative direction.

The 频率 domain power transmission 是 calculated 使用 该 following formula.

$$ T(f) = \frac{ \frac{1}{2} \int_{\text{监视器}} \mathbf{Re} (\mathbf{P}(f)) \cdot d\mathbf{S} }{\text{ sourcepower(f)} } $$

其中

\\(T(f)\\) 是 该 normalized transmission as 一个 函数 的 频率

\\(\mathbf{P}(f)\\) 是 该 Poynting 向量

\\(d\mathbf{S}\\) 是 该 surface normal

The normalization state (cwnorm 或 nonorm) does not affect 该 result because 的 该 源 power normalization.

**语法** |  **描述**  
---|---  
out = transmission("mname"); |  Transmission through 监视器 mname. It 必须 为 obvious 从 该 shape 的 该 监视器 该 axis 是 normal 到 该 监视器 surface.  
out = transmission("mname", option); |  The additional 参数, option, 可以 have 一个 值 的 1 或 2. If it 是 2, 该 数据 是 unfolded 其中 possible according 到 该 symmetry 或 anti-symmetric boundaries 如果 it comes 从 一个 监视器 该 intersect such 一个 boundary at x最小值, y最小值 或 z最小值. The default 值 的 option 是 2.  
  
**示例**

This example shows 如何 到 plot 该 power transmission through 一个 监视器.
    
    
    m="x2";    # 监视器 name  
    f=getdata(m,"f");  
    T=transmission(m);
    plot(c/f*1e6,T,"波长(um)","transmission");  

**参见**

[ sourcepower ](/hc/en-us/articles/360034925313-sourcepower) , [ dipolepower ](/hc/en-us/articles/360034925293-dipolepower) , [ transmission_avg ](/hc/en-us/articles/360034405374-transmission-avg) , [ transmission_pavg ](/hc/en-us/articles/360034405414-transmission-pavg) , [ Integrating Poynting vector ](https://kx.lumerical.com/t/integrating-the-poynting-vector/33595)
