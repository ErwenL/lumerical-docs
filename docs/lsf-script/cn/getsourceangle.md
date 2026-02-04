<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsourceangle -->

# getsourceangle

**语法** | **描述**
---|---
theta = getsourceangle( "sourcename", f); | 返回 the 光源 角度 theta (degrees) as a 函数 of 频率. f is a 向量 of frequencies (Hz).

**示例**

This 示例 shows how to get the 光源 injection 角度 as a 函数 of 频率. The 光源 频率 range is 300-600THz, and the nominal 光源 角度 theta is 10 degrees.
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

This 示例 shows how to get the 光源 injection 角度 as a 函数 of 频率. The 光源 频率 range is 300-600THz, and the nominal 光源 角度 theta is 10 degrees.
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

**另请参阅**

[sourcepower](/hc/en-us/articles/360034925313-sourcepower), [Broadband injection angles](/hc/en-us/articles/360034382894-Plane-waves-Angled-injection), [BFAST](/hc/en-us/articles/360034902273-Source-BFAST)
