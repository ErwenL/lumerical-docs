<!--
Translation from English documentation
Original command: besselj
Translation date: 2026-02-04 22:49:36
-->

# besselj

Computes 该 Bessel 函数 的 该 first kind. 

**语法** |  **描述**  
---|---  
out=besselj(nu, z);  |  "nu" 是 该 order 和 "z" could 为 一个 数组. Both nu 和 z need 到 为 real.   
  
**示例**

This example shows 如何 到 obtain 该 first order Bessel 函数 的 该 first kind 的 该 数组 z. 
    
    
    >z = 0.2:0.2:1;
    >?besselj(1,z);
    result: 
    0.0995008 
    0.196027 
    0.286701 
    0.368842 
    0.440051     

**参见**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besseli ](/hc/en-us/articles/360034926973-besseli) ,  [ besselk ](/hc/en-us/articles/360034406774-besselk)
