<!--
Translation from English documentation
Original command: getsourceangle
Translation date: 2026-02-04 22:50:00
-->

# getsourceangle

返回 该 源 angle theta as 一个 函数 的 频率. Broadband sources inject fields 该 have 一个 constant 在-plane wavevector at all frequencies. This implies injection angle 必须 change as 一个 函数 的 频率. The 在-plane wavevector 是 chosen such 该 该 incidence angle at 该 center 频率 的 该 仿真 (\\(f_{sim}\\)) 将 match 该 源 angle theta (\\(\theta_{sim}\\)) specified 在 该 源 属性. Higher frequencies 将 为 injected at smaller angles, while lower frequencies 将 为 injected at larger angles. This 'theta vs 波长' plot 在 该 beam 源 edit window shows 该 same 函数.

$$ \theta(f) = \arcsin\bigg[\frac{sin(\theta_{sim})f_{sim}}{f}\bigg]$$

**语法** |  **描述**  
---|---  
theta = getsourceangle( "sourcename", f); |  返回 该 源 angle theta (degrees) as 一个 函数 的 频率. f 是 一个 向量 的 frequencies (Hz).  
  
**示例**

This example shows 如何 到 获取 该 源 injection angle as 一个 函数 的 频率. The 源 频率 range 是 300-600THz, 和 该 nominal 源 angle theta 是 10 degrees.
    
    
    f_max=600e12;  
    f_min=300e12;  
    f=linspace(f_min,f_max,5);  
    
    ?theta_f=getsourceangle("source1",f);  
    result:   
    15.0981   
    12.0273   
    10   
    8.55978   
    7.48324  

**参见**

[sourcepower](/hc/en-us/articles/360034925313-sourcepower), [Broadband injection angles](/hc/en-us/articles/360034382894-Plane-waves-Angled-injection), [BFAST](/hc/en-us/articles/360034902273-Source-BFAST)
